# じきゅうちゃん 公式ホームページ

승인된 Website Mockup을 기준으로 구현한 일본어 단일 페이지입니다. 프레임워크, npm 설치, 빌드 과정 없이 GitHub Pages에서 실행됩니다. 앱 로직은 포함하거나 수정하지 않았습니다.

## Local preview

저장소 폴더에서 실행하세요.

```sh
python3 -m http.server 4173 --bind 127.0.0.1
```

브라우저에서 <http://127.0.0.1:4173/>를 엽니다. 변경 후 새로고침하면 반영됩니다.

검증:

```sh
python3 scripts/check-site.py
python3 scripts/build-site.py
```

## GitHub Pages 배포

1. GitHub 저장소 **Settings → Pages → Build and deployment → Source**에서 **GitHub Actions**를 선택합니다.
2. 이 파일들을 `main` 브랜치에 커밋하고 push합니다.
3. **Actions → Deploy static website to GitHub Pages**의 성공을 확인합니다. 필요하면 **Run workflow**로 수동 실행합니다.
4. 기본 주소는 `https://woosyume.github.io/jikyuchan-docs/`입니다. 실제 공개 여부는 Actions의 배포 결과와 Settings → Pages에서 확인하세요.

`.github/workflows/pages.yml`은 공개 파일만 `_site/`에 복사해 배포합니다. 원본 첨부 파일, 문서, 검증 스크립트는 배포 아티팩트에 넣지 않습니다. `pages: write`, `id-token: write`, `github-pages` 환경을 설정했습니다. 참고: [GitHub 공식 custom workflow 안내](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

GitHub의 브랜치 직접 배포를 선호하면 **Deploy from a branch → main → /(root)**도 사용할 수 있습니다. 이 경우 root의 문서와 스크립트도 공개되므로 Actions 방식을 권장합니다. 경로는 상대 경로여서 프로젝트 하위 경로에서도 작동합니다. 별도 도메인을 사용할 때는 `index.html`의 canonical, `og:url`, `og:image`를 실제 도메인으로 변경하세요.

이번 작업에서는 원격 push나 실제 공개 배포를 수행하지 않았습니다.

## 페이지 구성

Header → Hero → 캐릭터 소개 → 6개의 이야기 카드 → Final CTA → FAQ → 개인정보처리방침 → Footer.

이야기 카드 순서는 가격→시간, 생각과 선택, がまんまる, Goal, Insight, Discovery입니다. App Store 버튼은 공개 준비 안내를 열고, Discovery 버튼은 예시 발견을 펼칩니다. FAQ는 기본 HTML `details`로 구성했습니다. 가격/시간/선택/Goal 표시는 앱의 화면 예시이며 실제 계산기나 앱 기능이 아닙니다.

## Responsive / 접근성

- 최대 콘텐츠 너비 1160px. 701px 이상에서는 2열 카드, 700px 이하에서는 단일 열입니다.
- 모바일 Hero는 제목·설명 → 큰 방 그림 → CTA 순서로 재배치했습니다. 헤더는 펼칠 수 있는 메뉴로 바뀝니다.
- 701–1000px 태블릿 구간에는 카드·폰 크기와 글자 간격을 따로 조정했습니다. 320px 폭도 지원합니다.
- 일본어 `lang`, 제목/설명/canonical/OG, 제공 이미지 기반 favicon과 Apple touch icon을 포함했습니다.
- 키보드 포커스, skip link, 이미지 대체 텍스트, 메뉴 `aria-expanded`, 발견 `role="status"`, native dialog, Goal progressbar를 적용했습니다.
- `prefers-reduced-motion`에서는 애니메이션과 부드러운 스크롤을 해제합니다. JavaScript가 없어도 메뉴·본문·발견 내용을 읽을 수 있습니다.

## Assets / 미완성 항목 / 시안과의 차이

기존 저장소에는 이미지 자산이 없었습니다. 제공된 4개 PNG 보드에서 기존 그림을 그대로 잘라 WebP로 저장했습니다. 캐릭터를 새로 만들거나 AI 그림을 생성하지 않았습니다. 캐릭터 이름은 **じきゅうちゃん / おかねこ / ためぴょん**입니다. 모든 그림의 출처와 crop 좌표는 [assets/images/SOURCES.md](assets/images/SOURCES.md)에 기록했습니다.

- Hero 방: Website Mockup의 승인된 그림.
- 세 캐릭터와 앱 아이콘: Character Master의 기존 그림. 이름이 담긴 이미지 영역은 잘라냈습니다.
- 표정·がまんまる: UI Master의 기존 그림.
- 각 카드의 생활 장면: Website Mockup의 기존 그림.
- Insight 아이콘과 색상/정보 위계: Share Card Master. 메인 카드의 시간대 예시는 Master를 우선해 **밤에 더 구매하는 패턴(낮31% → 밤68%)**으로 통일했습니다.
- 가격/선택/Goal/Insight 카드는 웹에서 읽을 수 있도록 HTML로 구현했습니다. Goal 진행률 60%와 Insight 숫자는 표시 예시이며 실제 사용자 데이터가 아닙니다.

그림 placeholder는 없습니다. 다만 독립된 고해상도 투명 PNG/SVG 원본은 제공되지 않아 배경색이 남아 있고, 확대 시 원본 보드의 해상도에 따른 선명도 한계가 있습니다. 추후 원본 자산을 같은 파일 이름으로 교체할 수 있습니다. 로고 원본이 없어 확정 캐릭터의 기존 그림과 텍스트를 헤더에 사용했습니다.

개인정보처리방침은 페이지 하단의 `#privacy` 섹션에 작성했으며, Footer의 `<a href="#privacy">`로 직접 이동합니다. GitHub Pages 주소 뒤에 `#privacy`를 붙여 바로 연결할 수 있습니다. [TeacherPalette의 정책 구성](https://teacherpalette.com/#privacy)을 참고하고, 로컬 앱 코드에서 확인한端末 내 기록 처리, Google AdMob, 상품 URL 가져오기, 공유, 알림 및 리셋 동작을 반영했습니다. 참고 서비스의 개인정보 미수집/RevenueCat 사용 문구는 복사하지 않았습니다.

App Store URL과 문의 URL은 아직 준비되지 않았습니다. App Store는 준비 안내 dialog로 연결하고, 문의는 **準備中** 텍스트로 유지했습니다. 임의의 문의 주소나 SNS 계정을 만들지 않았습니다.

시안과 달라진 부분은 다음과 같습니다.

1. 원본 보드의 모바일 부분은 데스크톱보다 작은 캐릭터를 사용하지만, 실제 iPhone 가독성을 위해 방 그림과 UI를 크게 유지했습니다.
2. 확정 이름과 Master 그림을 적용해 시안 내 일부 캐릭터 표현을 통일했습니다.
3. 앱 UI의 정확한 예시 숫자와 선택 텍스트는 HTML로 표시했습니다. 폰 외곽선·카드·버튼은 UI Master의 색상과 모서리를 따랐습니다.
4. Discovery에 사용자가 직접 펼칠 수 있는 발견 예시를 적용했습니다. 신규 앱 기능이나 기록 분석 엔진을 만들지 않았습니다.
5. FAQ의 실제 답변을 확인할 수 있도록 Footer 위에 작은 FAQ 섹션을 추가했습니다.
6. 작은 흰 글자의 읽기 쉬움을 위해 CTA와 HTML 화면 예시의 메인 버튼은 같은 핑크 계열의 `#D3385B`를 사용했습니다(흰색과 명도 대비 약 4.68:1). 브랜드 기본 핑크 `#FF6B88`는 그대로 유지했습니다.

자산 재추출은 Pillow가 있는 Python 환경에서 원본 첨부 이미지 폴더를 지정해 실행할 수 있습니다. 사이트 실행/배포에는 Pillow가 필요 없습니다.

```sh
python3 scripts/extract-assets.py '/path/to/original-attachments'
```

## 파일

- `index.html`: 전체 일본어 페이지, SEO/OG, FAQ, 공개 준비 dialog.
- `styles.css`: 승인 시안의 레이아웃·색상·카드, 반응형 스타일, reduced motion.
- `site.js`: 모바일 메뉴, App Store 안내, Discovery 펼치기.
- `assets/images/`: 기존 그림 추출본, 아이콘, 출처 목록.
- `.github/workflows/pages.yml`, `.nojekyll`: GitHub Pages 배포 구조.
- `scripts/check-site.py`, `scripts/extract-assets.py`: 정적 파일 검증과 자산 재추출.
- `docs/`: 화면 검증 기록과 미리보기 이미지.

화면 검증 결과는 [docs/visual-qa.md](docs/visual-qa.md)를 참고하세요.

## Asset / Retina 개선 기록

공유 썸네일은 제공된 `ChatGPT Image Oct 4, 2026, 11_49_30 AM.png`를 무손실로 최적화한 `assets/images/og-jikyuchan.png`입니다(1536×1024, 약1.67MiB). Open Graph와 X의 large image 카드에 같은 절대 HTTPS URL을 설정했습니다. 공개 배포 후 공유 서비스가 이미지를 읽을 수 있으며, 서비스에 따라 미리보기 비율·크롭과 캐시가 달라질 수 있습니다. 사이트 본문의 Hero와 캐릭터는 교체하지 않았습니다.

전체 감사와 해상도 비교표, 필요한 정확한 원본 구도·표정, 최종 판정은 [docs/retina-quality-report.md](docs/retina-quality-report.md)에 기록했습니다. 승인된 그림을 그대로 유지하며 원본 보드 crop을 무손실 WebP로 재저장했습니다. 작은 responsive 후보 8개, 달·쇼핑백 SVG, Hero와 말풍선의 HTML 문구, preload/srcset/sizes, lazy loading과 명시적 dimensions를 적용했습니다. Apple touch icon의 기존 확대는 제거했습니다.

인접 앱 저장소의 원본은 현재 Master와 얼굴·표정·소품·구도가 달라 교체하지 않았습니다. Hero 등 11개 자산은 동일한 고해상도 원본이 필요하며 전체 Retina 품질이 완료된 상태는 아닙니다. 물리적 Retina 캡처는 제공 도구의 DPR=1 제한 때문에 수행하지 못했고, 실제 1440px/390px 브라우저 화면과 해상도 계산을 함께 검증했습니다.

`scripts/build-site.py`는 로컬과 GitHub Actions에서 같은 공개 산출물을 생성합니다. 현재 페이지/JS가 참조하는 WebP/PNG/SVG만 포함하며 문서·원본 목록·사용하지 않는 UI crop은 배포하지 않습니다. `CNAME`이 있으면 함께 복사합니다.
