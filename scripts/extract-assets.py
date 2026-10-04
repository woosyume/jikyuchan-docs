"""Extract existing artwork from the four supplied approved reference boards.

No drawing, generation, retouching, or character redesign is performed.
Run with the directory containing the original four PNG attachments.
"""
import argparse
from pathlib import Path
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("source_dir", type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
output = root / "assets" / "images"
output.mkdir(parents=True, exist_ok=True)
boards = {
    "website": "ChatGPT Image Oct 4, 2026, 10_31_56 AM.png",
    "character": "ChatGPT Image Oct 4, 2026, 10_32_19 AM.png",
    "ui": "ChatGPT Image Oct 4, 2026, 10_32_24 AM.png",
    "share": "ChatGPT Image Oct 4, 2026, 10_32_27 AM.png",
}
images = {key: Image.open(args.source_dir / filename).convert("RGB") for key, filename in boards.items()}
# Coordinates refer to the original attachment pixels. Text/name rows are excluded.
crops = {
    "hero-room": ("website", (278, 45, 652, 310)),
    "jikyuchan": ("character", (222, 95, 419, 280)),
    "okaneko": ("character", (654, 96, 862, 280)),
    "tamepyon": ("character", (1077, 97, 1300, 280)),
    "jikyuchan-normal": ("ui", (437, 52, 560, 162)),
    "jikyuchan-happy": ("ui", (593, 50, 739, 163)),
    "jikyuchan-thinking": ("ui", (751, 47, 895, 164)),
    "gamanmaru": ("ui", (1297, 48, 1506, 199)),
    "gaman-friends": ("website", (24, 842, 325, 925)),
    "price-room": ("website", (23, 579, 173, 727)),
    "choice-room": ("website", (347, 588, 478, 725)),
    "goal-room": ("website", (347, 822, 438, 921)),
    "reading-room": ("website", (300, 993, 406, 1140)),
    "discovery-friends": ("website", (425, 1043, 642, 1100)),
    "room-day": ("character", (625, 622, 832, 757)),
    "room-night": ("character", (1083, 622, 1288, 757)),
    "app-home": ("ui", (389, 680, 572, 997)),
    "app-saved": ("ui", (770, 680, 953, 997)),
    "app-collection": ("ui", (1340, 680, 1523, 997)),
    "insight-night-art": ("share", (659, 558, 838, 773)),
    "insight-wait-art": ("share", (249, 593, 435, 773)),
    "insight-shopping-art": ("share", (452, 591, 636, 773)),
    "app-icon": ("character", (40, 622, 192, 770)),
    "icon-night": ("share", (662, 257, 703, 296)),
    "icon-shopping": ("share", (460, 254, 496, 295)),
}
manifest = []
for name, (source, box) in crops.items():
    crop = images[source].crop(box)
    # Preserve every source pixel. A higher quality setting cannot create detail.
    crop.save(output / f"{name}.webp", "WEBP", lossless=True, method=6)
    manifest.append(f"| `{name}.webp` | {boards[source]} | `{box}` | {crop.width} × {crop.height} |")
# Responsive candidates are smaller derivatives, never enlarged sources.
responsive = {
    "hero-room": 320, "jikyuchan": 100, "okaneko": 104,
    "tamepyon": 112, "jikyuchan-normal": 64,
    "jikyuchan-happy": 74, "jikyuchan-thinking": 72, "gamanmaru": 106,
}
for name, width in responsive.items():
    source, box = crops[name]
    crop = images[source].crop(box)
    height = round(crop.height * width / crop.width)
    crop.resize((width, height), Image.Resampling.LANCZOS).save(
        output / f"{name}-{width}.webp", "WEBP", lossless=True, method=6
    )
icon_source = images["character"].crop(crops["app-icon"][1])
# Keep the original detail rather than the previous 152 -> 180px enlargement.
icon = Image.new("RGB", (152, 152), icon_source.getpixel((0, 0)))
icon.paste(icon_source, (0, 2))
icon.save(output / "apple-touch-icon.png")
icon_source.resize((64, 64), Image.Resampling.LANCZOS).save(output / "favicon.png")
(output / "SOURCES.md").write_text(
    "# Supplied artwork provenance\n\nAll artwork is cropped from the user's approved attachments. "
    "No replacement artwork was generated. Original source boards are not bundled. "
    "Matching independent high-resolution/transparent exports were not found; "
    "cream backgrounds are preserved. Full-size WebP files are lossless and pixel-identical "
    "to the source crops. Smaller responsive candidates are downsampled only. "
    "HTML supplies section copy, Hero values, and current character names.\n\n"
    "| Asset | Source attachment | Crop (left, top, right, bottom) | Size |\n"
    "| --- | --- | --- | --- |\n" + "\n".join(manifest) + "\n\n"
    "`apple-touch-icon.png` is the original 152×148px app-icon crop centered in a152×152px "
    "canvas (no upscaling). `favicon.png` is a64×64px downsample.\n\n"
    "Responsive derivatives: " + ", ".join(f"`{name}-{width}.webp`" for name, width in responsive.items()) + ".\n\n"
    "`icon-night.svg` and `icon-shopping.svg` are manually authored simple vector icons "
    "following the Share Card Master's crescent/bag shapes and colors; no character tracing. "
    "Their old WebP crops remain available as provenance/reference, but are not served by the page. "
    "The wordmark is HTML text and the Apple symbol is inline SVG.\n\n"
    "App repository assets were inspected but rejected where face/pose/props/composition differed. "
    "See `docs/asset-audit-before.md` and `docs/retina-quality-report.md` for remaining source gaps.\n",
    encoding="utf-8",
)
print(f"Extracted {len(crops)} lossless crops, {len(responsive)} smaller candidates, and 2 PNG icons; no upscaling.")
