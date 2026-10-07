"""Check approved source preservation and exclusion of genuine UI captures."""
import hashlib
import json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
manifest=json.loads((root/'docs/yurukawa/asset-sources.json').read_text())
checks={}
for asset in manifest:
    source=Path(asset['source'])
    checks['original unchanged: '+source.name]=hashlib.sha256(source.read_bytes()).hexdigest()==asset['source_sha256']
for name in ('release-home','release-consultation','release-queue','release-price-current','release-price-history','release-visual-summary','release-summary-overview','release-summary-timeline','release-insight-top3'):
    checks['capture excluded from public build: '+name]=not any((root/'_site/assets/images').glob(name+'*.webp'))
page=(root/'index.html').read_text()
checks['no authentic UI caption']= '実際のアプリ画面' not in page and '実際の画面の一部' not in page
old=Path('/tmp/jikyuchan-before-yurukawa.html').read_text()
checks['FAQ legal footer unchanged']=page[page.index('    <section id="faq"'):]==old[old.index('    <section id="faq"'):]
checks['SEO unchanged']=page[:page.index('  <link rel="preload"')]==old[:old.index('  <link rel="preload"')]
report=dict(passed=all(checks.values()),checks=checks)
(root/'docs/yurukawa/asset-qa.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('PASS' if report['passed'] else 'FAIL',len(checks),'illustration, screenshot-exclusion, legal and SEO checks')
if not report['passed']: raise SystemExit([k for k,v in checks.items() if not v])
