"""Build-free static website integrity check; uses only Python's standard library."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

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

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
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

document = Document()
document.feed((root / "index.html").read_text(encoding="utf-8"))
errors = document.errors
if document.lang != "ja":
    errors.append("Document language must be Japanese")
if document.headings != 1:
    errors.append("Expected exactly one h1")
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
print(f"PASS: local assets, anchor/ARIA targets, Japanese metadata, image alt attributes, and current character names. Artwork: {size / 1024:.0f} KiB.")
