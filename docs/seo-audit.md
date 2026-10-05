# じきゅうちゃん Google Search / technical SEO 감사

확인일: 2026-10-05 (JST). 이 보고서는 로컬 변경과 배포 전 production 상태를 구분합니다. 이번 작업에서는 커밋·push·배포를 수행하지 않았습니다.

## 1. 수정 파일

- `index.html`: description 보완, production canonical·OG/X URL 수정, WebSite JSON-LD 한 개 추가. 기존 title·본문·Hero·이미지·레이아웃 유지.
- `robots.txt`: 전체 crawl 허용 및 sitemap 안내.
- `sitemap.xml`: 실제 홈페이지 canonical 한 개만 등록.
- `scripts/build-site.py`: robots.txt와 sitemap.xml을 공개 산출물에 포함.
- `scripts/check-site.py`: metadata·JSON-LD·robots·sitemap과 실제 HTML/canonical 일치를 source와 산출물에서 검증.
- `README.md`: production 도메인 정보와 sitemap 유지보수 절차 정리.
- `docs/seo-audit.md`: 이 보고서.

작업 시작 전에 README·index.html·이미지 출처 문서에 수정 사항이 있었고, 공개일 OG 이미지와 관련 파일도 미추적 상태였습니다. 기존 변경은 보존했습니다. 승인된 `og-jikyuchan-20261026.png`를 재사용했으며 새 이미지를 만들지 않았습니다.

## 2. 수정 전 구조 / production URL 전체 목록

프레임워크·클라이언트 router 없이 `index.html` 한 장을 제공하는 static site입니다. navigation은 실제 `<a href="#…">`입니다. GitHub Actions `.github/workflows/pages.yml`은 `main` push 또는 수동 실행 시 `scripts/build-site.py`로 공개 파일만 `_site/`에 복사해 GitHub Pages로 배포합니다. source 문서·개발 스크립트는 산출물에서 제외합니다. `CNAME`은 이미 `jikyuchan.com`이었습니다.

**전체 indexable canonical URL 목록:**

- https://jikyuchan.com/

`https://jikyuchan.com/#privacy`와 `#faq`는 같은 홈페이지의 섹션입니다. footer의 실제 HTML 링크로 접근하며, 독립 문서가 아니므로 sitemap에서 제외했습니다. `/privacy/`, `/support/` 페이지는 없으며 문의 창구는 準備中입니다. App Store 버튼은 안내 dialog를 엽니다.

수정 전 title은 `じきゅうちゃん｜その「ほしい」、何時間ぶん？`였습니다. description은 브랜드 설명과 공개 예정일을 포함하지만 iPhone 앱이라는 설명이 빠져 있었습니다. canonical·og:url·OG/X 이미지 URL은 이전 GitHub 주소를 가리켰습니다. robots.txt·sitemap.xml·구조화 데이터는 없었습니다. favicon·Apple touch icon·OG/X metadata는 이미 존재했습니다.

## 3. 최종 홈페이지 title

```text
じきゅうちゃん｜その「ほしい」、何時間ぶん？
```

기존 승인 Hero와 동일한 브랜드 카피를 사용하는 적절한 title이므로 유지했습니다. 요청의 대안인 `買う前に、ちょっと考える。`로 교체하지 않았습니다. 키워드 나열을 추가하지 않았습니다.

## 4. 최종 meta description

```text
じきゅうちゃんは、欲しいものの値段を「はたらく時間」にして、買う前にちょっと考えるためのiPhoneアプリです。記録するほど、自分の「ほしい」のクセも見えてきます。2026年10月26日公開予定。
```

기존 승인 본문과 의미가 일치하며 공개 예정 상태도 유지합니다.

## 5. canonical / www / index.html 전략

`https://jikyuchan.com/`을 유일한 홈페이지 canonical로 설정했습니다. sitemap·WebSite·og:url도 동일합니다. `/index.html`로 접근해도 같은 HTML에서 `/` canonical이 제공됩니다. HTML canonical은 HTTP redirect 자체를 생성하지 않습니다.

배포 전 실제 HTTP 검사 결과:

| 입력 URL | 응답 / 최종 목적지 |
| --- | --- |
| `https://jikyuchan.com/` | 200 OK |
| `https://jikyuchan.com/index.html` | 200 OK, 중복 홈페이지 |
| `https://www.jikyuchan.com/` | 301 → `https://jikyuchan.com/` → 200 |
| `http://jikyuchan.com/` | 301 → `https://jikyuchan.com/` → 200 |
| `https://woosyume.github.io/jikyuchan-docs/` | 301 → `https://jikyuchan.com/` → 200 |
| `https://jikyuchan.com/robots.txt` | 404 (신규 파일 배포 전) |
| `https://jikyuchan.com/sitemap.xml` | 404 (신규 파일 배포 전) |

현재 production HTML의 canonical도 이전 GitHub 주소입니다. 이전 주소는 공식 도메인으로 redirect하므로 서로 상충하는 신호를 이번 변경으로 정리합니다. www/HTTP/GitHub 주소의 기존 서버 redirect는 정상이며 변경하지 않았습니다. 배포 이후에도 redirect 상태를 확인하세요.

## 6. WebSite 구조화 데이터

홈페이지 head에 단일 JSON-LD block을 추가했습니다.

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "じきゅうちゃん",
  "alternateName": "jikyuchan.com",
  "url": "https://jikyuchan.com/"
}
```

도메인 root에 필요한 name·url과 선택 alternateName을 제공하며, 실제 HTML 브랜드 텍스트와 og:site_name이 일치합니다. `/index.html` 같은 HTML 중복 접근에도 동일 block이 제공됩니다. [Google site name 지침](https://developers.google.com/search/docs/appearance/site-names)을 확인했습니다. JSON 문법과 필드 검증을 통과했습니다. Rich Results Test는 site name을 지원하지 않으므로 배포 후 [Schema Markup Validator](https://validator.schema.org/)와 Search Console URL 검사를 사용합니다. 실제 검색의 사이트 이름·title·색인 여부는 Google이 결정합니다.

## 7. SoftwareApplication 검토

이번에는 추가하지 않았습니다. iPhone·일본어·브랜드명은 확정됐지만 앱은 출시 예정이며 production App Store URL·가격·실제 평점/리뷰는 확인되지 않았습니다. [Google SoftwareApplication 리치 결과 지침](https://developers.google.com/search/docs/appearance/structured-data/software-app)은 name과 offers.price, aggregateRating 또는 review를 요구합니다. schema.org의 기본 앱 설명 자체가 금지되는 것은 아니지만, 현재 정보로는 Google 앱 리치 결과 요건을 충족하지 않으므로 불완전한 마크업을 억지로 추가하지 않았습니다.

출시 후 TODO: 실제 App Store 공개 URL과 가격, 운영체제 정보를 확인하고, 공개된 실제 리뷰/평점이 확보되면 해당 페이지 내용과 일치하는 정보로 적용 여부를 재검토합니다. 리뷰·평점이 없으면 만들어 넣지 않습니다.

## 8. sitemap.xml 전체 내용

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://jikyuchan.com/</loc>
  </url>
</urlset>
```

실제 HTML 페이지와 일치하는 absolute HTTPS canonical만 포함합니다. XML namespace·중복·실제 HTML·canonical 일치를 검증합니다. fragment·redirect·개발 문서·가상의 내부 페이지는 제외합니다. 수정일을 안정적으로 관리하지 않으므로 lastmod를 생략했으며 changefreq/priority와 신규 dependency도 없습니다. 향후 public page를 추가할 때 빌드 공개 목록·self-referencing canonical·sitemap을 함께 갱신하도록 README에 기록했습니다. [Google sitemap 안내](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap).

## 9. robots.txt 전체 내용

```text
User-agent: *
Allow: /

Sitemap: https://jikyuchan.com/sitemap.xml
```

배포 root에 복사되며 홈페이지·favicon·OG 이미지가 Googlebot/Googlebot-Image에 허용되는지 검증했습니다. source와 산출물의 공개 HTML에 noindex/none meta가 없습니다. 현재 production 홈페이지와 `/index.html` 응답에 X-Robots-Tag가 없었습니다. 배포 후 HTTP header도 다시 확인해야 합니다.

## 10. favicon / 접근성 / H1

- 기존 캐릭터 favicon `assets/images/favicon.png`: PNG, 실제 64×64, square, `rel="icon"`, sizes="64x64". [Google favicon 지침](https://developers.google.com/search/docs/appearance/favicon-in-search)의 최소 크기·비율과 48px 초과 권장을 만족합니다. URL과 이미지 모두 유지했습니다.
- Apple touch icon: 기존 PNG 152×152, 유지.
- 단일 H1: `その「ほしい」、何時間ぶん？`. 승인된 Hero 유지.
- 브랜드 `じきゅうちゃん`은 header·본문·footer의 실제 HTML text에 존재합니다. 숨겨진 SEO 문구는 추가하지 않았습니다.
- 주요 이미지에 자연스러운 내용 설명이 있습니다. 예: `小さな芽とまるいからだのじきゅうちゃん`, `記録を読んでいるじきゅうちゃん`. 인접 브랜드 텍스트와 중복되는 작은 로고나 장식 이미지의 empty alt는 유지했습니다.
- 개인정보처리방침과 FAQ는 실제 HTML anchor로 발견할 수 있으며 JS click handler에 의존하지 않습니다.

## 11. 최종 OG / Twitter(X)

| 필드 | 최종 값 |
| --- | --- |
| og:title / twitter:title | じきゅうちゃん｜その「ほしい」、何時間ぶん？ |
| og:description / twitter:description | 2026年10月26日公開予定。値段を、あなたの「はたらく時間」に。じきゅうちゃんと一緒に、本当にほしいものを選ぼう。 |
| og:url | https://jikyuchan.com/ |
| og:site_name | じきゅうちゃん |
| og:type / og:locale | website / ja_JP |
| og:image / twitter:image | https://jikyuchan.com/assets/images/og-jikyuchan-20261026.png |
| og:image:type / width / height | image/png / 1536 / 1024 |
| og:image:alt / twitter:image:alt | 2026年10月26日公開予定。じきゅうちゃん。その「ほしい」、何時間ぶん？ 値段を、あなたの「はたらく時間」に。 |
| twitter:card | summary_large_image |

기존 승인 공개일 이미지와 공유 카피를 그대로 사용합니다. production의 배포 전 이미지는 이전 `og-jikyuchan.png`이므로 현재 로컬의 승인된 변경과 함께 배포해야 합니다. 실제 공유 서비스의 캐시·크롭은 배포 후 확인합니다.

## 12. 발견한 문제 / 남은 항목

수정한 문제: 이전 도메인 canonical·OG URL·이미지 URL, crawl 안내와 sitemap 부재, WebSite node 부재, description의 iPhone 설명 누락, 신규 crawl 파일이 배포 공개 목록에서 누락될 가능성.

남은 항목: 변경사항 배포, Search Console 제출·색인 요청, 실제 favicon/공유 이미지 crawl 확인, 출시 후 앱 정보 재검토. 별도 support 페이지와 문의 URL은 아직 준비되지 않았으며 임의로 추가하지 않았습니다.

## 13. 빌드 / 검증 결과

- `python3 scripts/build-site.py`: 성공, 공개 파일 33개. source와 `_site` 양쪽 검사 통과.
- title·description·canonical·OG/X metadata 정상, WebSite JSON-LD JSON 문법 및 name/url 검증 통과.
- sitemap valid XML이며 전체 public canonical 목록과 일치. robots.txt 배포 산출물 포함 및 crawler 허용 검증 통과.
- 이미지 파일·alt·width/height·srcset/sizes·HTML anchor·ARIA 참조·단일 H1 검증 통과.
- 작업 전후 전체 body와 favicon 이후의 visual resource markup이 동일합니다. styles.css·site.js·본문 이미지·responsive 설정을 수정하지 않아 mobile/layout 입력이 보존됐습니다. 이번에는 새 모바일 스크린샷을 촬영하지 않았습니다.
- 배포 산출물을 임시 로컬 HTTP 서버로 제공해 `/`, `/robots.txt`, `/sitemap.xml`, favicon, OG 이미지의 200 OK 및 Content-Type을 확인했습니다.

## 14. 배포 후 Google Search Console 작업

1. GitHub Actions 배포가 성공했는지 확인하고 아래 세 URL이 **production에서 직접 200 OK**인지 확인합니다. homepage HTML·JSON-LD·canonical과 공개일 OG 이미지도 새 버전인지 확인합니다.
   - https://jikyuchan.com/
   - https://jikyuchan.com/robots.txt
   - https://jikyuchan.com/sitemap.xml
2. Search Console에서 `jikyuchan.com` 도메인 속성을 추가하고 안내에 따라 DNS TXT로 소유권을 확인합니다. 이미 확인된 속성이 있으면 재사용합니다.
3. Sitemaps에 `https://jikyuchan.com/sitemap.xml`을 제출하고 처리 상태를 확인합니다.
4. URL 검사에 `https://jikyuchan.com/`을 입력하고 실제 URL 테스트로 fetch·indexability·렌더링된 HTML·사용자 선언 canonical을 확인한 뒤 색인 생성 요청을 실행합니다.
5. Schema Markup Validator로 WebSite를 확인합니다. Rich Results Test에 site name 결과가 없는 것은 오류가 아닙니다.
6. 재크롤링 후 Google 선택 canonical이 `https://jikyuchan.com/`인지 확인하고 페이지 색인 생성과 검색 실적에서 브랜드 검색 노출을 살펴봅니다. 사이트 이름·favicon 반영에는 시간이 걸릴 수 있으며 표시나 순위를 보장할 수 없습니다.
7. www/HTTP/이전 GitHub 주소의 301 이동, `/index.html`의 root canonical, 홈페이지·favicon·OG 이미지의 crawler 차단 여부를 확인합니다.
