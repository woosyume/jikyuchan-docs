# Release 1.0 홈페이지 업데이트 완료 보고

2026-10-07 · 홈페이지 코드 수정 및 로컬 검증 완료. iOS 앱 소스와 동작은 변경하지 않았으며 commit / push / production deploy도 수행하지 않았습니다.

1. **유지:** Hero의 `その「ほしい」、何時間ぶん？`, 가격→시간 개념, 승인된 방 그림과 캐릭터, 크림색·핑크·그린, 공개 예정 dialog, FAQ와 정책 본문, 기존 hosting 구조를 보존했습니다.
2. **수정:** 6개 기능 카드 격자를 이야기 흐름으로 재구성했습니다. 세 선택은 같은 크기·색·정보 위계로 보여줍니다. Characters는 이야기 뒤로 이동하고 선택을 함께 지켜보는 문구로 정리했습니다. Goal은 절약 경쟁이 아닌 원하는 것의 우선순위를 선택하는 경험으로 소개합니다. 정책에는 가격 확인 시 외부 통신도 반영하고, 기록 전반에 대한 포괄적인 외부 자동 전송 없음 문장은 구체적인 로컬 저장/처리 설명으로 정리했습니다.
3. **추가:** 공유로 맡기는 흐름, 기다리는 짧은 장면, 실제 가격 기록, 실제 Visual Summary, 두 가지 production Insight를 대비하는 발견 구간, 짧은 Privacy 소개를 추가했습니다.
4. **삭제/통합:** 실제 앱처럼 재구성했던 계산·선택 화면, 임의의 Goal 60%/42,800円, 오래된 숫자 Insight와 Discovery 예시, 독립적인 がまんまる 기능 카드를 제거했습니다. がまんまる 그림은 Goal에 재사용합니다. 공개 HTML/JS/CSS에서 `考え中`, `後で考える`와 오래된 캐릭터 이름은 없습니다.
5. **최종 narrative:** 気になる → 預ける → 待つ → お値段と気持ちの変化 → 自分で選ぶ → 振り返る → 気づく → 本当にほしいものへ → 仲間たち → Privacy → CTA. FAQ와 전문 정책은 그 뒤 지원 영역으로 유지했습니다.
6. **실제 자산:** 「お値段の様子」와 최신 7日 Visual Summary를 실제 앱의 Simulator QA 캡처에서 추출했습니다. WebP와 원본 사각형의 RGB 픽셀 일치를 검증했습니다. 예시 기록임을 화면 아래에 표시합니다. Insight 두 문구는 `Core/PriceDecisionInsights.swift`의 `DROP_BUT_NOT_BOUGHT` / `LONG_KEEP_BOUGHT`에서 그대로 사용합니다. Hero 및 じきゅうちゃん / おかねこ / ためぴょん은 기존 master 계열 자산입니다. 공유 흐름·Insight 말풍선·Goal 그림은 홈페이지 설명 구성이고 가상 앱 화면이 아닙니다. [정확한 화면 출처](screenshot-sources.json), [기존 그림 출처](../../assets/images/SOURCES.md).
7. **Mobile QA:** 320px와 390px에서 Hero·줄바꿈·그림·카드·선택·CTA를 캡처하고 확인했습니다. 320px의 캐릭터 이름을 한 줄로 보정했습니다. 가로 넘침/이미지 누락/잘림을 검사했고 CTA는 높이 46px입니다. 메뉴 열기→이동→닫기, 공개 예정 dialog와 Escape 닫기, FAQ 펼치기가 통과했습니다. [390px Hero](hero-390.png), [390px 발견](discovery-390.png), [320px 전체](preview-320.png).
8. **Desktop QA:** 768px 태블릿, 1280px 일반 데스크톱, 1920px 대형 데스크톱에서 레이아웃과 동작이 정상입니다. 다섯 폭 모두 문서 너비와 화면 너비가 같고 가로 넘침·이미지 누락·콘솔/페이지/HTTP 오류가 0입니다. [1280px 전체](preview-1280.png), [1920px 전체](preview-1920.png), [검증 데이터](browser-qa.json). 캡처는 Chrome의 CSS viewport / DPR 1 기준이며 실기기 Retina 검증은 아닙니다.
9. **SEO:** title을 `じきゅうちゃん｜買う前に、ちょっと考える。`로 변경하고 description과 OG/X 문구에 맡기기·기록 돌아보기를 반영했습니다. canonical, robots, sitemap, WebSite JSON-LD, favicon, 날짜가 반영된 기존 OG 그림과 내부 정책 주소는 유지했습니다. 빌드 검증에서 metadata/참조/ARIA/alt/이미지 크기/캐릭터 이름/상태 용어가 통과했습니다. 외부 정책 링크 3개도 모두 HTTP 200입니다. [외부 링크 결과](external-links.json).
10. **Build / deploy:** `scripts/build-site.py`가 원본과 `_site`를 각각 검사하고 공개 파일 30개를 생성했습니다. JS 문법과 diff 공백 검사를 통과했습니다. 모션 감소 설정에서는 scroll-behavior가 auto이고 활성 애니메이션은 0입니다. JavaScript 없이도 메뉴·본문·발견을 읽을 수 있습니다. 로컬 미리보기는 <http://127.0.0.1:4173/>입니다. Production 배포는 하지 않았습니다.
11. **추가로 필요한 실제 화면/자산:** 깨끗한 Share Sheet→あずかりもの 캡처, 진행 중 또는 달성 Goal 화면, 필요하면 カテゴリーなし가 포함된 최신 요약 화면을 추가하면 경험을 더 직접적으로 보여줄 수 있습니다. 현재 Goal 관련 확보 캡처는 debug seeder 화면이라 사용하지 않았습니다. 기존 Hero·일부 작은 캐릭터/여행 그림의 같은 구도 고해상도 원본도 필요합니다. 이를 대신할 캐릭터나 UI는 생성하지 않았습니다.

기존 구간의 분류와 근거는 [수정 전 감사](audit.md)에 기록했습니다. README도 현재 구조·자산·한계·미리보기 절차에 맞춰 갱신했습니다.
