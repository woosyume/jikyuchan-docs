# 변경 전 전체 visual asset 감사

제품 코드를 수정하기 전에 작성. 2026-10-04. 실제 브라우저 CSS viewport 320/390/540/700/701/1000/1160/1440에서 측정. 브라우저 DPR=1이므로 2x 밀도 판정은 원본 픽셀과 CSS 크기를 계산한 결과이며 실제 Retina 디스플레이 확인을 의미하지 않는다.

표의 크기는 conservative CSS image box(일부 padding/object-fit 여백 포함). Desktop >700 / Mobile ≤700. Happy는 Discovery 펼친 상태의 145px/128px도 포함. favicon16px와 홈 화면60px는 플랫폼 관례 기반 가정이며 DOM 측정이 아님.

| File | Format / pixels | Desktop max CSS | Mobile max CSS | Density | Source | Alpha | Embedded text | Category | ≥2x |
|---|---|---|---|---|---|---|---|---|---|
| apple-touch-icon.png | PNG 180×180 | 60×60 | 60×60 | 2.47x (source) | Character Master | False | none | BRAND / ICON | PASS |
| discovery-friends.webp | WEBP 217×57 | 262.7×69 | 247.5×65 | 0.83x | Website mockup | False | none | ILLUSTRATION | FAIL |
| favicon.png | PNG 32×32 | 16×16 | 16×16 | 2.0x | Character Master | False | none | BRAND / ICON | PASS |
| gaman-friends.webp | WEBP 301×83 | 552×168.2 | 512×157.2 | 0.49x | Website mockup | False | none | ILLUSTRATION | FAIL |
| gamanmaru.webp | WEBP 209×151 | 90×65.0 | 79.4×60.5 | 2.29x | UI Master | False | none | CHARACTER | PASS |
| goal-room.webp | WEBP 91×99 | 125.8×136.8 | 106.9×116.3 | 0.72x | Website mockup | False | none | ILLUSTRATION | FAIL |
| hero-room.webp | WEBP 374×265 | 647.9×459.1 | 510×361.4 | 0.58x | Website mockup | False | price/time/wage | ILLUSTRATION | FAIL |
| icon-night.webp | WEBP 41×39 | 32×34 | 32×34 | 1.15x | Share Card Master | False | none | BRAND / ICON | FAIL |
| icon-shopping.webp | WEBP 36×41 | 32×34 | 32×34 | 1.12x | Share Card Master | False | none | BRAND / ICON | FAIL |
| jikyuchan-happy.webp | WEBP 146×113 | 145×112.2 | 128×99.1 | 1.0x | UI Master | False | none | CHARACTER | FAIL |
| jikyuchan-normal.webp | WEBP 123×110 | 61.5×55 | 61.5×55 | 2.0x | UI Master | False | none | CHARACTER | PASS |
| jikyuchan-thinking.webp | WEBP 144×117 | 145×117.8 | 128×104 | 0.99x | UI Master | False | none | CHARACTER | FAIL |
| jikyuchan.webp | WEBP 197×185 | 203.6×150 | 154.7×130 | 0.97x | Character Master | False | none | CHARACTER | FAIL |
| okaneko.webp | WEBP 208×184 | 231.8×205.1 | 222.8×197.1 | 0.89x | Character Master | False | none | CHARACTER | FAIL |
| price-room.webp | WEBP 150×148 | 247.0×243.7 | 213.3×210.4 | 0.61x | Website mockup | False | speech bubble | ILLUSTRATION | FAIL |
| reading-room.webp | WEBP 106×147 | 103×142.8 | 0×0 | 1.03x | Website mockup | False | none | ILLUSTRATION | FAIL |
| tamepyon.webp | WEBP 223×183 | 203.6×150 | 154.7×130 | 1.09x | Character Master | False | none | CHARACTER | FAIL |

## Code-native visuals / APP UI

- Wordmark: HTML text; menu/progress/bubbles/badges/decorative marks: CSS / text. Apple symbol: existing inline SVG 24×24 viewBox rendered15×18px. All independent of raster density.
- Price/result, selection phone, Goal and Insight/Discovery cards: HTML/CSS examples, not production app screenshots. All meaningful values already native text except Hero card and price-room speech bubble.
- Actual screenshot count used by current site: 0. The app-home/app-saved/app-collection board crops and six other unused illustrations are not referenced by the page and are excluded from displayed asset calculations.

## Source search and identity gate

Searched website repository, entire adjacent jikyuchan app repository (Assets.xcassets and exports), supplied attachment directory and Desktop/tmp. Found32 PNG files in app: character assets1254×1254 RGBA, app icons1024×1024, backgrounds1086×1448 and1672×941. No SVG/PDF artwork or production screenshot matching the shown examples.

App images are distinct artwork: normal has cheek strokes/large leaves; thinking has a downturned mouth rather than approved smile; happy face/hand shape differs; coin has arms/highlights absent from approved token. Character lineup differs more: app cat has sprout; app rabbit has no carrot pouch; jikyuchan has no coin pouch. Do not substitute these for approved Master crops. Room assets have different desk/camera/window arrangement and omit approved Hero character/time card; not an exact higher resolution replacement.

Desktop/tmp/1.png (806×1744) is an actual simulator window screenshot of a different deferred-product-list screen, not a production capture matching this site. Not used.

No matching higher-resolution source found. Retain exact approved artwork, re-export from original board pixels losslessly, improve simple icons/native text where possible, and explicitly keep unresolved density failures as NEEDS_SOURCE_ASSET.

Apple touch icon already contains a152×148→180×180 upscale from previous extraction. Nominal180px is not180px of original detail; report source density separately. No further upscaling permitted.
