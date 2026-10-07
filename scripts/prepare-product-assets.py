"""Optimize approved illustrations and crop genuine app captures without repainting UI.

Source files stay untouched. No generated UI, replacement text, or upscaling.
"""
import argparse
import hashlib
import json
from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--illustration-dir', type=Path, default=Path('/Users/woosyume/Desktop/jikyuchan-images/homepages'))
parser.add_argument('--app-repo', type=Path, default=root.parent / 'jikyuchan')
args = parser.parse_args()
output = root / 'assets/images'
records = []


def export(name, source, box=None, widths=(), illustration=False):
    image = Image.open(source).convert('RGBA')
    original_size = image.size
    if box:
        image = image.crop(box)
    # Alpha is retained. UI excerpts are encoded losslessly at their source resolution.
    options = {'quality': 90, 'method': 6} if illustration else {'lossless': True, 'method': 6}
    image.save(output / f'{name}.webp', **options)
    for width in widths:
        smaller = image.resize((width, round(image.height * width / image.width)), Image.Resampling.LANCZOS)
        smaller.save(output / f'{name}-{width}.webp', **options)
    records.append({
        'asset': f'{name}.webp', 'source': str(source),
        'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'original_dimensions': original_size, 'crop': box, 'dimensions': image.size,
        'responsive_widths': widths,
        'encoding': 'WebP quality 90 with alpha' if illustration else 'lossless WebP',
    })


for name in ('web_deposit', 'web_price_watch', 'web_choice', 'web_discovery', 'web_goal'):
    export(name, args.illustration_dir / f'{name}.png', widths=(800, 1200), illustration=True)

captures = (
    ('release-home', '21', (175, 211, 872, 1727)),
    ('release-queue', '49', (202, 451, 845, 1710)),
    ('release-price-current', '46', (202, 425, 845, 1348)),
    ('release-insight-top3', '36', (261, 449, 787, 1188)),
)
for name, second, box in captures:
    source = args.illustration_dir / f'ChatGPT Image Oct 7, 2026, 11_32_{second} PM.png'
    export(name, source, box)

export('release-consultation', args.app_repo / 'QA/AdditionalUXCorrection/new-consultation-3000-at-1500-is-two-hours.png', (60, 760, 1146, 2130))
summary = args.app_repo / 'QA/StatusDrillDown/summary-seven-normal.png'
export('release-summary-overview', summary, (48, 348, 1158, 1358), widths=(600,))
export('release-summary-timeline', summary, (48, 1363, 1158, 2024), widths=(600,))
for name, box in (
    ('pass', (0, 170, 463, 825)),
    ('keep', (460, 160, 1100, 824)),
    ('buy', (1117, 160, 1672, 824)),
):
    export(f'release-choice-{name}', args.illustration_dir / 'web_choice.png', box, illustration=True)

manifest = root / 'docs/product-redesign/asset-sources.json'
manifest.parent.mkdir(parents=True, exist_ok=True)
manifest.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Prepared {len(records)} approved asset exports; originals unchanged.')
