"""Prepare the same publishable static artifact locally and in GitHub Actions."""
from pathlib import Path
import re
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(root / "scripts/check-site.py")], check=True)
destination = root / "_site"
if destination.is_symlink():
    raise SystemExit("Refusing to build into a symlink")
if destination.exists():
    shutil.rmtree(destination)
destination.mkdir()
public_files = {"index.html", "styles.css", "site.js", ".nojekyll", "robots.txt", "sitemap.xml"}
for source in ("index.html", "styles.css", "site.js"):
    public_files.update(re.findall(r"assets/images/[\w-]+\.(?:webp|png|svg)", (root / source).read_text()))
if (root / "CNAME").is_file():
    public_files.add("CNAME")
for relative in sorted(public_files):
    target = destination / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / relative, target)
subprocess.run([sys.executable, str(root / "scripts/check-site.py"), str(destination)], check=True)
print(f"PASS: {len(public_files)} public files prepared in _site; no audit/source documents published.")
