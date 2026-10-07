"""Compare preserved content and source pixels with the audited inputs."""
import hashlib
import json
from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parents[2]
baseline = json.loads((root / 'docs/product-redesign/preserved-baseline.json').read_text())
page = (root / 'index.html').read_text()
checks = {}
for filename, digest in baseline.items():
    if filename == 'faq_and_legal_suffix_sha256':
        content = page[page.index('    <section id="faq"'):].encode()
    elif filename == 'seo_head_sha256':
        content = page[:page.index('  <link rel="preload"')].encode()
    else:
        content = (root / filename).read_bytes()
    checks[filename] = hashlib.sha256(content).hexdigest() == digest
assets = json.loads((root / 'docs/product-redesign/asset-sources.json').read_text())
for asset in assets:
    source = Path(asset['source'])
    checks['original unchanged: ' + source.name] = hashlib.sha256(source.read_bytes()).hexdigest() == asset['source_sha256']
    if asset['encoding'] == 'lossless WebP':
        original = Image.open(source).convert('RGBA').crop(tuple(asset['crop']))
        exported = Image.open(root / 'assets/images' / asset['asset']).convert('RGBA')
        checks['exact screenshot pixels: ' + asset['asset']] = original.tobytes() == exported.tobytes()
    image = Image.open(root / 'assets/images' / asset['asset'])
    checks['dimensions: ' + asset['asset']] = image.size == tuple(asset['dimensions'])
    for width in asset['responsive_widths']:
        candidate = Image.open(root / 'assets/images' / (Path(asset['asset']).stem + f'-{width}.webp'))
        checks[f'responsive size: {asset["asset"]} {width}'] = candidate.size == (width, round(image.height * width / image.width))
report = {'passed': all(checks.values()), 'checks': checks}
(root / 'docs/product-redesign/preservation-qa.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(f'{"PASS" if report["passed"] else "FAIL"}: {len(checks)} source, screenshot, legal, SEO, hosting and dimension checks')
if not report['passed']:
    raise SystemExit([name for name, passed in checks.items() if not passed])
