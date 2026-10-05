"""Change only the release badge with local font rendering; no generated artwork.

Run with a Japanese font path. Requires Pillow only when regenerating the asset.
The supplied original stays intact. This badge region belongs to the 1536x1024
approved sharing image; do not apply these coordinates to other artwork.
"""
import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser()
parser.add_argument("font", type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
source = Image.open(root / "assets/images/og-jikyuchan.png").convert("RGB")
if source.size != (1536, 1024):
    raise SystemExit("Expected the approved 1536x1024 sharing image")
output = source.copy()
# Clear only the old lettering, using the unobstructed badge colors above/below.
for x in range(1180, 1370):
    top = source.getpixel((x, 921))
    bottom = source.getpixel((x, 957))
    for y in range(922, 957):
        ratio = (y - 921) / 36
        output.putpixel((x, y), tuple(round(a + (b - a) * ratio) for a, b in zip(top, bottom)))
draw = ImageDraw.Draw(output)
for text, size, y in (("2026年10月26日", 22, 918), ("公開予定", 16, 944)):
    font = ImageFont.truetype(str(args.font), size)
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    draw.text((1278 - (right - left) / 2 - left, y - top), text, font=font, fill="white")
output.save(root / "assets/images/og-jikyuchan-20261026.png", optimize=True)
print("Updated release badge; original artwork preserved.")
