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
    crop.save(output / f"{name}.webp", "WEBP", quality=92, method=6)
    manifest.append(f"| `{name}.webp` | {boards[source]} | `{box}` | {crop.width} × {crop.height} |")
icon = images["character"].crop(crops["app-icon"][1]).resize((180, 180), Image.Resampling.LANCZOS)
icon.save(output / "apple-touch-icon.png")
icon.resize((32, 32), Image.Resampling.LANCZOS).save(output / "favicon.png")
(output / "SOURCES.md").write_text(
    "# Supplied artwork provenance\n\nAll artwork is cropped from the user's approved attachments. "
    "No replacement artwork was generated. Original source boards are not bundled. "
    "Artwork is not available as independent high-resolution/transparent exports; "
    "cream backgrounds are preserved. HTML supplies all section copy and current character names.\n\n"
    "| Asset | Source attachment | Crop (left, top, right, bottom) | Size |\n"
    "| --- | --- | --- | --- |\n" + "\n".join(manifest) + "\n\n"
    "`apple-touch-icon.png` and `favicon.png` are resized crops of `app-icon.webp`.\n",
    encoding="utf-8",
)
print(f"Extracted {len(crops)} WebP assets and 2 PNG icons.")
