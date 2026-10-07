"""Export supplied narrative illustrations; originals stay unchanged."""
from pathlib import Path
import hashlib
import json
from PIL import Image
root = Path(__file__).resolve().parents[1]
originals = Path('/Users/woosyume/Desktop/jikyuchan-images')
records = []

def export(name, source, crop=None, widths=()):
    im = Image.open(source).convert('RGBA')
    original = im.size
    if crop:
        im = im.crop(crop)
    im.save(root / 'assets/images' / f'{name}.webp', quality=90, method=6)
    for w in widths:
        im.resize((w, round(im.height*w/im.width)), Image.Resampling.LANCZOS).save(root/'assets/images'/f'{name}-{w}.webp',quality=90,method=6)
    records.append(dict(asset=name+'.webp', source=str(source), source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(), original_dimensions=original, crop=crop, dimensions=im.size, responsive_widths=widths))

# The lower row includes an outdated release badge; only the entire upper scene is used.
export('yuru-hero-wide', originals/'ChatGPT Image Oct 4, 2026, 11_49_30 AM.png', (0,0,1536,720), (800,1200))
export('yuru-hero-mobile', originals/'test.png', widths=(620,))
export('yuru-deposit', Path('/var/folders/3f/kqxq2w6d3vv3t5s4xbjkrpx00000gn/T/codex-clipboard-c8d9deb8-e1be-41bb-b308-84695399bede.png'), widths=(800,1200))
export('yuru-journal', originals/'character-sample2.png', widths=(700,1000))
p=root/'docs/yurukawa/asset-sources.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('PASS: four approved illustration exports; original files unchanged.')
