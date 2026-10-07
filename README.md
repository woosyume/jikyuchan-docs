# じきゅうちゃん 公式ホームページ

Release 1.0의 실제 앱 화면과 승인된 다섯 일러스트로 구성한 일본어 홈페이지입니다. 그림은 감정과 이야기를, 실제 Simulator 캡처는 제품 기능을 보여줍니다. 프레임워크 없이 GitHub Pages에서 실행하며, iOS 앱 소스는 수정하지 않습니다.

## 미리보기와 빌드

```sh
python3 scripts/check-site.py
python3 scripts/build-site.py
python3 -m http.server 4173 --bind 127.0.0.1 --directory _site
```

[로컬 미리보기](http://127.0.0.1:4173/)에서 확인합니다. `_site/`는 공개 파일만 포함하며 Git에서 제외됩니다. 원본을 편집하면 다시 빌드합니다.

## 본문 구성

Hero → 預かりもの → お値段の様子 → 三つの選択 → きろく → 新しい発見 → 本当にほしいものへ → Characters → Privacy 소개 → Final CTA → FAQ / Privacy Policy → Footer.

최대 본문 폭은 1240px입니다. 실제 구매 상담과 홈 화면으로 시작하여, 큰 그림과 あずかりもの, 가격 그래프와 그림의 겹침, 넓은 선택 장면, 확대된 기록 화면, 발견 카드, 여행 장면으로 구도를 바꿉니다. 모든 섹션을 카드 안에 넣지 않습니다. 모바일은 문구와 주 시각 자료를 순서대로 배치하고, 선택 그림 세 장면을 각각 확대합니다. 홈 화면은 모바일에서 `ホーム画面も見る`를 펼치면 볼 수 있습니다.

`がまんした / キープ中 / 買った`은 동등한 선택입니다. 핵심은 「買わないためじゃない。納得して選ぶため。」입니다. 공개 예정일은 **2026年10月26日**입니다. 기존 CTA는 예정 안내를 여는 동작을 유지하며, 없는 App Store URL이나 배지를 만들지 않습니다.

## 그림과 실제 앱 화면

사용자 제공 `web_deposit.png`, `web_price_watch.png`, `web_choice.png`, `web_discovery.png`, `web_goal.png`에서 WebP와 반응형 후보를 만듭니다. 원본은 변경하지 않으며, 알파 채널을 유지합니다. 선택 장면의 모바일 버전은 동일 그림의 영역 추출입니다.

최신 사용자 제공 Simulator 캡처에서 Home, あずかりもの, お値段の様子, 「ほしい」のクセ TOP 3를 추출합니다. 인접 앱 저장소에서 구매 상담과 7日 Visual Summary를 추출합니다. 앱 화면의 원래 픽셀을 무손실로 저장하며, 금액·텍스트·UI를 합성하지 않습니다. 화면에는 예시 기록임을 표시합니다. Goal에는 적합한 실제 화면이 없어 승인 그림만 사용합니다.

- [원본 파일·영역·해시](docs/product-redesign/asset-sources.json)
- [그림 출처와 기존 캐릭터](assets/images/SOURCES.md)
- [검증 보고서](docs/product-redesign/report.md)

Pillow가 있는 Python 환경에서 원본을 다시 추출할 수 있습니다. 홈페이지 실행에는 Pillow가 필요 없습니다.

```sh
python3 scripts/prepare-product-assets.py --illustration-dir '/path/to/homepages' --app-repo '/path/to/jikyuchan'
```

## 접근성·SEO·법적 문구

일본어 lang, 의미 있는 제목과 alt, 이미지 크기, 반응형 이미지, lazy loading, skip link, 키보드 포커스, 네이티브 dialog/details를 사용합니다. 모션 감소 설정에서는 부드러운 스크롤을 해제합니다. JavaScript 없이도 본문·메뉴·발견·FAQ·모바일 홈 화면을 읽을 수 있습니다.

기존 title, description, canonical, OG/X, WebSite JSON-LD, favicon, robots.txt와 sitemap.xml은 보존합니다. FAQ와 전체 Privacy Policy, footer, 법적 외부 링크의 내용은 변경하지 않았습니다. 공식 정책 주소는 [Privacy Policy](https://jikyuchan.com/#privacy)입니다.

## GitHub Pages

`.github/workflows/pages.yml`, `CNAME`, `.nojekyll`과 기존 빌드 구성을 유지합니다. 배포 산출물은 `scripts/build-site.py`가 공개 파일만 복사하여 만듭니다. 문서, 출처와 검증 캡처는 게시되지 않습니다. 이번 수정에서는 commit·push·production deploy를 하지 않았습니다.
