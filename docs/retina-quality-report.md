# Asset / Retina 품질 개선 보고서

승인된 구도·캐릭터·섹션 순서를 보존한 범위의 개선을 반영했습니다. **전체 Production Retina 품질은 아직 충족하지 못했습니다.** 동일한 고해상도 원본이 없는11개 항목은 NEEDS_SOURCE_ASSET으로 남겼습니다. 다른 표정·소품·장면으로 대체하거나 AI로 재생성하지 않았습니다.

변경 전 감사: [asset-audit-before.md](asset-audit-before.md). CSS 측정: [before](asset-before-display.json) / [after](asset-after-display.json). 앱 원본32개 조사: [source-asset-inventory.json](source-asset-inventory.json). 원본 crop 좌표: [SOURCES.md](../assets/images/SOURCES.md).

## 자산 비교표

단위 px. Max Display는 desktop/mobile에서 측정한 보수적 image box 최대값(일부 object-fit 여백, scene padding 포함).2x는 원본 해상도 요구치이며 확대·축소로 부족한 detail을 숨기지 않았습니다.

| Asset | Before Resolution | Max Display Size | Required Retina Resolution | After Resolution | Source | Format | Status |
|---|---|---|---|---|---|---|---|
| apple-touch-icon.png | 180×180 | 60×60 | 120×120 | 152×152 | Character Master | PNG | ALREADY_OK |
| discovery-friends.webp | 217×57 | 262.7×69 | 526×138 | 217×57 | Website mockup | WebP lossless | NEEDS_SOURCE_ASSET |
| favicon.png | 32×32 | 16×16 | 32×32 | 64×64 | Character Master | PNG | ALREADY_OK |
| gaman-friends.webp | 301×83 | 552×168.2 | 1104×337 | 301×83 | Website mockup | WebP lossless | NEEDS_SOURCE_ASSET |
| gamanmaru.webp | 209×151 | 90×65 | 180×130 | 209×151 | UI Master | WebP lossless | ALREADY_OK |
| goal-room.webp | 91×99 | 125.8×136.8 | 252×274 | 91×99 | Website mockup | WebP lossless | NEEDS_SOURCE_ASSET |
| hero-room.webp | 374×265 | 647.9×459.1 | 1296×919 | 374×265 | Website mockup | WebP lossless | NEEDS_SOURCE_ASSET |
| icon-night.webp | 41×39 | 32×34 | 64×68 | vector | Share Card Master | SVG | FIXED |
| icon-shopping.webp | 36×41 | 32×34 | 64×68 | vector | Share Card Master | SVG | FIXED |
| jikyuchan-happy.webp | 146×113 | 145×117.8 | 290×236 | 146×113 | UI Master | WebP lossless | NEEDS_SOURCE_ASSET |
| jikyuchan-normal.webp | 123×110 | 61.5×55 | 123×110 | 123×110 | UI Master | WebP lossless | ALREADY_OK |
| jikyuchan-thinking.webp | 144×117 | 145×117.8 | 290×236 | 144×117 | UI Master | WebP lossless | NEEDS_SOURCE_ASSET |
| jikyuchan.webp | 197×185 | 203.6×150 | 408×300 | 197×185 | Character Master | WebP lossless | NEEDS_SOURCE_ASSET |
| okaneko.webp | 208×184 | 231.8×205.1 | 464×411 | 208×184 | Character Master | WebP lossless | NEEDS_SOURCE_ASSET |
| price-room.webp | 150×148 | 247×243.7 | 494×488 | 150×148 | Website mockup | WebP lossless | NEEDS_SOURCE_ASSET |
| reading-room.webp | 106×147 | 103×142.8 | 206×286 | 106×147 | Website mockup | WebP lossless | NEEDS_SOURCE_ASSET |
| tamepyon.webp | 223×183 | 203.6×150 | 408×300 | 223×183 | Character Master | WebP lossless | NEEDS_SOURCE_ASSET |
| Wordmark / Apple mark | text / SVG | text / 15×18 | scalable | same | current site | HTML / SVG | ALREADY_OK |
| Price / choice / Goal / Insight / Discovery UI | HTML/CSS examples | responsive | scalable text | same | UI / Share Master | HTML/CSS | ALREADY_OK |

FIXED는 달·가방 아이콘의 해상도 문제 해결만 뜻합니다. 무손실 재저장으로 원본 픽셀을 보존했더라도 해상도가 부족한 그림은 FIXED로 분류하지 않았습니다.

favicon은16px 표시 가정에서2x 이상이며64px export로 여유를 추가했습니다. Apple touch icon은 기존152×148→180×180 확대를 제거하고152×152 canvas에 원본을 가운데 배치했습니다. 홈 화면60px 가정에서는 유효 밀도2.47x로 최소2x 충족. iPhone3x용180px의 실제 원본 detail은 없습니다. 아이콘 표시 크기는 플랫폼 관례 기반 가정이며 페이지 DOM 측정이 아닙니다.

## NEEDS_SOURCE_ASSET 정확한 원본 요청 목록

| Asset | 현재 resolution | Desktop CSS max | Mobile CSS max | 권장 최소 원본(2x 보수적 기준) | 필요한 장면 / 표정 / 구도 |
|---|---|---|---|---|---|
| discovery-friends.webp | 217×57 | 262.7×69 | 247.5×65 | 526×138 | 가로 strip. 가운데 じきゅうちゃん과 옆의 がまんまる들. 식물·머그컵·전구가 있는 같은 장면. |
| gaman-friends.webp | 301×83 | 552×168.2 | 512×157.2 | 1104×337 | 가로 방 장면. 가운데 양손을 모은 じきゅうちゃん, 왼쪽 작은 がまんまる와 오른쪽 큰 がまんまる. 같은 식물·배경·위치·비율. |
| goal-room.webp | 91×99 | 125.8×136.8 | 106.9×116.3 | 252×274 | 모자 쓴 じきゅうちゃん, 파란 가방·여행 소품, 옆의 がまんまる와 식물. 현재 세로 crop과 동일한 여행 준비 구도. |
| hero-room.webp | 374×265 | 647.9×459.1 | 510×361.4 | 1296×919 | 책상 앞 양손을 모은 じきゅうちゃん, 왼쪽 머그컵, 펼친 책, 식물·창문, 오른쪽 がまんまる, 기울어진 시간 카드가 있는 정확한 Hero 구도. 카드 문구는 별도 HTML. 권장 여유 약1944×1380px(3x). |
| jikyuchan-happy.webp | 146×113 | 145×117.8 | 128×104 | 290×236 | UI Master 기쁨 표정. 감은 눈·미소, 볼 옆의 두 손과 동일한 새싹·반짝임. |
| jikyuchan-thinking.webp | 144×117 | 145×117.8 | 128×104 | 290×236 | UI Master 생각 중 표정. 미소를 유지한 채 턱에 손을 댄 포즈, 작은 새싹과 오른쪽 보라색 물음표. 앱 원본의 찡그린 입은 사용 불가. |
| jikyuchan.webp | 197×185 | 203.6×150 | 154.7×130 | 408×300 | Character Master의 엔화 주머니를 양손으로 잡고 웃는 포즈. 동일한 얼굴·새싹·볼·몸 윤곽. |
| okaneko.webp | 208×184 | 231.8×205.1 | 222.8×197.1 | 464×411 | Character Master의 새싹 없는 삼색 고양이. 엔화 주머니, 구부러진 꼬리, 같은 웃는 얼굴·손·무늬. |
| price-room.webp | 150×148 | 247×243.7 | 213.3×210.4 | 494×488 | 식물·머그컵·모래시계와 생각하는 じきゅうちゃん. 같은 위치의 타원 말풍선(문구는 HTML). |
| reading-room.webp | 106×147 | 103×142.8 | 0×0 | 206×286 | 파란 책을 읽는 じきゅうちゃん과 노란 がまんまる. 동일한 소파·식물 배경. |
| tamepyon.webp | 223×183 | 203.6×150 | 154.7×130 | 408×300 | Character Master의 연분홍 토끼. 옆으로 내려오는 긴 귀, 당근 주머니를 잡은 동일한 포즈·웃는 표정. |

캐릭터/표정은500–1000px급 투명 PNG/WebP 원본으로 여유를 확보하면 좋습니다. 위 CSS box 요구치를 맞출 때 윤곽을 늘리지 않고 원본 비율·구도를 유지해야 합니다. object-fit 여백과 CSS padding은 그림의 일부가 아니므로 실제 alpha 여백/비율에 맞춰 canvas 크기를 조정할 수 있습니다.

## 요청된14개 보고 항목

1. **수정 파일:** index.html(텍스트 분리, picture/srcset/sizes, 아이콘 선언), styles.css(문자 영역 SVG clip과 native text, Discovery 고정 비율), site.js(표정 srcset 동기화), scripts/extract-assets.py(무손실 원본·작은 파생본·확대 제거), scripts/check-site.py(srcset/dimensions/clip 검증), 신규 scripts/build-site.py, .github/workflows/pages.yml, README.md, assets/images/SOURCES.md, asset과 docs 감사/QA 기록.
2. **추가 asset:** hero-room-320.webp, jikyuchan-100.webp, okaneko-104.webp, tamepyon-112.webp, jikyuchan-normal-64.webp, jikyuchan-happy-74.webp, jikyuchan-thinking-72.webp, gamanmaru-106.webp 및 icon-night.svg/icon-shopping.svg. 기존 assets/images convention 유지.
3. **제거/교체:** 페이지에서 달·쇼핑백의 저해상도 WebP 사용을 SVG로 교체. 기존 crop은 참고용으로 보관하고 배포하지 않음.25개 crop을 동일 이름·동일 resolution의 무손실 WebP로 재저장(13개만 페이지 사용). 동일한 고해상도 illustration 교체0개. Apple touch icon의 기존 확대 제거.
4. **SVG:** 달·가방은 Share Master의 단순 형태·색을 따르는 수작업 vector. 캐릭터 tracing 없음. 기존 Apple SVG와 HTML wordmark 유지. 확정 캐릭터를 바꿔 로고를 새로 만들지 않음.
5. **WebP/AVIF:** full-size WebP25개가 원본 PNG board crop과 RGB 픽셀 단위로 동일함을 검증. 작은 후보만 축소. AVIF는 미적용. WebP가 현재 작은 이미지에 충분하며 손실 압축으로 원본 선·질감을 다시 손상시키지 않음.
6. **Raster text → HTML:** Hero의 ¥12,800 / 6時間24分 / 時給 ¥2,000 문구와 가격 장면의 この買い物、何時間ぶん…？. SVG clip은 문자 영역만 제거하고 방·캐릭터·카드 외곽선을 유지. 가격/선택/Goal 금액/Insight 비율/Discovery는 HTML 유지. 숫자 분리는 illustration 해상도 문제의 해결로 간주하지 않음.
7. **실제 screenshot 교체:**0개. 매칭하는 production screenshot 없음. 발견한 simulator 상품 목록 화면은 현재 예시와 다르므로 미사용. 기존 HTML/CSS 화면은 「表示例」로 유지하고 production capture라고 표현하지 않음.
8. **picture/srcset/sizes:** Hero picture/source와 preload의 후보·sizes 일치. 캐릭터 소개, 브랜드, 폰 예시, がまんまる, Discovery, 최종CTA/dialog에 smaller/full 후보. 소개는 viewport별 실제 column 크기 반영. Discovery는 src와 srcset을 함께 교체.2x에서 최고 기존 후보를 선택하더라도 없는 detail을 생성하지 않음.
9. **Loading / CLS:** Hero high priority + responsive preload. 그림 decoding=async와 width/height. Below-fold lazy 유지, Footer/dialog에도 lazy. Hero/말풍선 wrapper와 Discovery frame에 aspect-ratio. 표정 toggle에서도 frame 비율 유지.
10. **Desktop Retina QA:**1440×900 실제 브라우저 전체/상단 화면 확인. 가격·시간·Goal·Insight·Discovery native text와 SVG는 선명함. Hero/소개/생활 장면 blur는 여전히 보임. 도구의 DPR=1 제한으로 물리적2x screenshot은 촬영하지 못했으며2x 판정은 원본 resolution/CSS 계산에 기반.
11. **Mobile Retina QA:**390×900 별도 screenshot.320/390/540/700/701/768/1000/1160/1440px 모두 가로 overflow 없음. Hero 문구 내부 overflow 없음. 표시 이미지 로드 확인. 메뉴·anchor·CTA dialog·Discovery 표정/srcset·FAQ·#privacy 정상. 오류/경고 로그 없음. 남은 저해상도 그림의 Retina 품질은 FAIL.
12. **Production build:** `python3 scripts/build-site.py` PASS. 공개29개 파일만 _site에 생성하고 산출물의 asset/srcset/anchor/ARIA 재검증. _site/ 하위 경로에서 실제 페이지 QA로 프로젝트 상대 경로 확인. optional CNAME 보존 추가. 현재 CNAME/custom domain/DNS 미설정이므로 실제 custom domain 검증은 안 함. Node 문법 및 git diff --check PASS. 원격 push/Actions 배포 미실행.
13. **NEEDS_SOURCE_ASSET:** 위 목록11개. Hero, 소개3종, 생각/기쁨 표정, 가격·친구·여행·독서·Discovery 장면. 앱 원본은 얼굴·잎·손·주머니·귀·구도가 달라 사용하지 않음.
14. **예상 initial image payload:** 무손실 원본 보존으로 파일 크기 증가. 아래는 관찰된 선택 파일 크기의 합계이며 네트워크 transfer/Lighthouse 수치가 아님. browser cache, DPR, lazy 선행 로드 범위에 따라 실제 초기 요청량은 달라짐.

| 이미지 범위 | Before | After estimate (관찰된 DPR1 선택) |
|---|---:|---:|
| Desktop1440×900의 화면 안 이미지 | 52.0KiB | 214.6KiB |
| Mobile390×900의 화면 안 이미지 | 27.1KiB | 107.5KiB |
| favicon 별도 | 2.3KiB | 7.6KiB |

전체 배포 WebP 후보 합계 약538KiB(브라우저가 전부 다운로드하는 값이 아님). 최종 공개 파일 전체는 약0.62MiB.2x에서 화면 안 이미지가 모두 최고 기존 후보를 고르면 desktop 약222KiB/mobile 약115KiB. 원본 pixel preservation을 위해 기존 손실 압축보다 무거워졌지만 초기 이미지가 수십 MB가 되는 상황은 없음. 정확한 cold-cache 속도/CLS/LCP는 이번 브라우저 도구에서 측정하지 않음.

## 최종 판정

| 요구 항목 | 판정 | 원인 / 근거 |
|---|---|---|
| Hero Retina quality | FAIL |374×265를 최대 약648×459 CSS로 표시. 최소1296×919의 동일 구도 원본 필요. native text는 개선됐지만 그림은 약0.58x. |
| Character Retina quality | FAIL |소개3종과 thinking/happy 표현이2x 미달. normal/がまんまる와 로고 텍스트는 최소 기준 충족. |
| App UI Retina quality | FAIL |HTML UI 숫자·버튼·Goal·Insight는 선명하나, choice 화면의 thinking portrait는144px source를77px로 표시해2x에 필요한154px 미달. 동일한 실사용 screenshot도 없음. |
| Desktop visual regression | PASS |승인된 그림/구도/섹션 유지.1440px 및 중간 크기에서 확인. native 글자·simple SVG 변환은 요청된 변경. |
| Mobile visual regression | PASS |390px 별도 확인,320px 지원 및 overflow 없음. 메뉴·CTA·Discovery·FAQ·privacy 정상. |
| GitHub Pages build | PASS |로컬에서 Actions와 동일한 static build·산출물·하위 경로 검증. 실제 원격 배포를 의미하지 않음. |

Screenshot: [Desktop top](retina-desktop-top.jpg), [Desktop full](retina-desktop-full.jpg), [Mobile top](retina-mobile-top.jpg), [Mobile full](retina-mobile-full.jpg). 모두 DPR1 실제 브라우저 캡처입니다. 원본이 없는 항목을 선명해진 것으로 표시하거나 전체 Retina 개선이 완료됐다고 선언하지 않습니다.
