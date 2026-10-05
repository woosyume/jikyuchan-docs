"""Build-free static website integrity check; uses only Python's standard library."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from urllib.robotparser import RobotFileParser
import json
import re
import sys
import xml.etree.ElementTree as ET

root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]

class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.references = []
        self.headings = 0
        self.errors = []
        self.lang = None
        self.social_images = []
        self.metadata = {}
        self.canonicals = []
        self.json_ld = []
        self.in_json_ld = False
        self.title = ""
        self.in_title = False

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        if tag == "meta":
            key = attributes.get("property") or attributes.get("name", "").lower()
            self.metadata.setdefault(key, []).append(attributes.get("content", ""))
            if key in ("robots", "googlebot", "googlebot-news") and re.search(r"\b(noindex|none)\b", attributes.get("content", ""), re.I):
                self.errors.append("Public page must not have noindex")
        if tag == "link" and "canonical" in attributes.get("rel", "").split():
            self.canonicals.append(attributes.get("href"))
        if tag == "title":
            self.in_title = True
        if tag == "script" and attributes.get("type") == "application/ld+json":
            self.in_json_ld = True
            self.json_ld.append("")
        if tag == "meta" and (attributes.get("property") == "og:image" or attributes.get("name") == "twitter:image"):
            image_url = attributes.get("content", "")
            self.social_images.append(image_url)
            # Social crawlers require a public absolute URL. Validate its bundled file too.
            parsed = urlsplit(image_url)
            if parsed.scheme != "https" or not parsed.netloc:
                self.errors.append("Social image must use an absolute HTTPS URL")
            if "/assets/images/" in parsed.path:
                self.references.append("assets/images/" + parsed.path.split("/assets/images/", 1)[1])
        if tag == "html":
            self.lang = attributes.get("lang")
        if tag == "h1":
            self.headings += 1
        if "id" in attributes:
            identity = attributes["id"]
            if identity in self.ids:
                self.errors.append(f"Duplicate ID: {identity}")
            self.ids.add(identity)
        for attribute in ("src", "href"):
            if attribute in attributes:
                self.references.append(attributes[attribute])
        for attribute in ("srcset", "imagesrcset"):
            self.references.extend(candidate.strip().split()[0] for candidate in attributes.get(attribute, "").split(",") if candidate.strip())
            if attributes.get(attribute) and not attributes.get("sizes" if attribute == "srcset" else "imagesizes"):
                self.errors.append(f"Responsive image missing sizes: {tag}")
        if tag == "img" and "alt" not in attributes:
            self.errors.append("Image missing alt attribute")
        if tag == "img" and not all(attributes.get(key, "").isdigit() for key in ("width", "height")):
            self.errors.append("Image missing explicit width/height")
        for attribute in ("aria-controls", "aria-labelledby", "aria-describedby"):
            self.references.extend("#" + identity for identity in attributes.get(attribute, "").split())

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_json_ld:
            self.json_ld[-1] += data

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "script":
            self.in_json_ld = False

document = Document()
document.feed((root / "index.html").read_text(encoding="utf-8"))
errors = document.errors
if document.lang != "ja":
    errors.append("Document language must be Japanese")
if document.headings != 1:
    errors.append("Expected exactly one h1")

home = "https://jikyuchan.com/"
if document.canonicals != [home]:
    errors.append("Expected one homepage canonical on the production domain")
if not document.title.startswith("じきゅうちゃん｜"):
    errors.append("Homepage title must begin with the official brand name")
if len(document.metadata.get("description", [])) != 1 or not document.metadata["description"][0]:
    errors.append("Expected one nonempty meta description")
for key in ("og:title", "og:description", "og:image", "twitter:title", "twitter:description", "twitter:image"):
    if len(document.metadata.get(key, [])) != 1 or not document.metadata[key][0]:
        errors.append(f"Missing or duplicate social metadata: {key}")
for key, value in {"og:url": home, "og:site_name": "じきゅうちゃん", "og:type": "website", "twitter:card": "summary_large_image"}.items():
    if document.metadata.get(key) != [value]:
        errors.append(f"Unexpected social metadata: {key}")
if any(not image.startswith(home + "assets/images/") for image in document.social_images):
    errors.append("Social images must use the production domain")
try:
    nodes = [json.loads(block) for block in document.json_ld]
    websites = [node for node in nodes if isinstance(node, dict) and node.get("@type") == "WebSite"]
    if len(websites) != 1 or any(websites[0].get(key) != value for key, value in {
        "@context": "https://schema.org", "name": "じきゅうちゃん", "alternateName": "jikyuchan.com", "url": home
    }.items()):
        errors.append("Expected one valid WebSite node with the official site name and URL")
except ValueError as error:
    errors.append(f"Invalid JSON-LD: {error}")

try:
    sitemap = ET.parse(root / "sitemap.xml").getroot()
    namespace = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    if sitemap.tag != namespace + "urlset":
        errors.append("Sitemap must have the standard XML namespace")
    locations = [entry.findtext(namespace + "loc", default="") for entry in sitemap.findall(namespace + "url")]
    public_canonicals = []
    # Source-only directories aren't published by the Pages artifact builder.
    for page in root.rglob("*.html"):
        relative = page.relative_to(root)
        if any(part.startswith(".") or part in ("_site", "docs", "scripts") for part in relative.parts):
            continue
        parsed = Document()
        parsed.feed(page.read_text(encoding="utf-8"))
        errors.extend(f"{relative}: {error}" for error in parsed.errors)
        page_path = relative.as_posix()
        page_url = home + (page_path[:-10] if page_path.endswith("index.html") else page_path)
        if parsed.canonicals != [page_url]:
            errors.append(f"{relative}: canonical must match its public URL")
        public_canonicals.append(page_url)
    if len(locations) != len(set(locations)) or set(locations) != set(public_canonicals):
        errors.append("Sitemap must contain exactly the public canonical HTML URLs, without duplicates")
except (OSError, ET.ParseError) as error:
    errors.append(f"Invalid or missing sitemap: {error}")

try:
    robots = RobotFileParser()
    robots.parse((root / "robots.txt").read_text().splitlines())
    if robots.site_maps() != [home + "sitemap.xml"]:
        errors.append("robots.txt must reference the production sitemap")
    for url in (home, home + "assets/images/favicon.png", *document.social_images):
        for crawler in ("Googlebot", "Googlebot-Image", "*"):
            if not robots.can_fetch(crawler, url):
                errors.append(f"robots.txt blocks {crawler}: {url}")
except OSError as error:
    errors.append(f"Missing robots.txt: {error}")
for reference in document.references:
    url = urlsplit(reference)
    if url.scheme or url.netloc:
        continue
    if url.path and not (root / unquote(url.path)).is_file():
        errors.append(f"Missing local file: {reference}")
    if url.fragment and not url.path and url.fragment not in document.ids:
        errors.append(f"Missing anchor: {reference}")
for source in ("index.html", "styles.css", "site.js"):
    content = (root / source).read_text(encoding="utf-8")
    for obsolete_name in ("うさじまる", "うさぴまる"):
        if obsolete_name in content:
            errors.append(f"Obsolete character name in {source}")
    if source == "site.js":
        for image in re.findall(r"assets/images/[\w-]+\.webp", content):
            if not (root / image).is_file():
                errors.append(f"Missing dynamic image: {image}")
    if source == "styles.css":
        for identity in re.findall(r"url\(#([\w-]+)\)", content):
            if identity not in document.ids:
                errors.append(f"Missing SVG clip definition: {identity}")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
size = sum(path.stat().st_size for path in (root / "assets/images").glob("*.webp"))
print(f"PASS: assets, anchor/ARIA targets, Japanese SEO/social metadata, WebSite JSON-LD, crawl rules, sitemap coverage, image alt attributes, and character names. Artwork: {size / 1024:.0f} KiB.")
