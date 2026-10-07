# Product story redesign — 2026-10-08

本文を全面再構成し、実際のアプリ画面と承認済みイラストの役割を分けました。イラストは気持ち・世界観を、画面は現在の製品体験を伝えます。「買わないためじゃない。納得して選ぶため。」を軸に、三つの選択を同等に扱っています。

## 調査したもの

作業前に現行HTML/CSS/JS、画像と来歴、GitHub Pages設定、公開URL、SEO、FAQ、ポリシー、リンクを確認しました。提供された商品紹介ボード・旧UIボードは参考資料に限定し、実際のUIとして掲載していません。既存のキャラクター画像はそのまま使用しています。隣接するiOSアプリのソースは読み取りだけで、変更していません。

## 変更したもの

- `index.html`: 新しい本文構成、実際のUI、大きな承認イラスト、意味のある日本語alt、モバイルのホーム画面開閉。
- `styles.css`: 最大1240px、全幅の背景、左右の対話、画面と絵の重なり、中央の選択場面、大きな記録の詳細、モバイルの縦構成。
- `scripts/prepare-product-assets.py`: 元画像を保持するWebP最適化、実画面の無損失抽出、選択場面のモバイル切り出し。
- `assets/images/`: 承認イラストのWebPと反応型候補、実UIの抽出画像。READMEとSOURCESも現行構成に更新。

## イラストの原本

1. `web_deposit.png`
2. `web_price_watch.png`
3. `web_choice.png`
4. `web_discovery.png`
5. `web_goal.png`

ページでは同名の`.webp`と800/1200px候補を使用します。透過を維持し、原本のファイルは変更していません。モバイルの選択画像三枚は`web_choice.png`の別々の領域です。描き直しはありません。

## 実際のアプリ画面の原本

- Home: `ChatGPT Image Oct 7, 2026, 11_32_21 PM.png`
- あずかりもの: `ChatGPT Image Oct 7, 2026, 11_32_49 PM.png`
- お値段の様子: `ChatGPT Image Oct 7, 2026, 11_32_46 PM.png`
- 「ほしい」のクセ TOP 3: `ChatGPT Image Oct 7, 2026, 11_32_36 PM.png`
- 買いものの相談: `QA/AdditionalUXCorrection/new-consultation-3000-at-1500-is-two-hours.png`
- きろく: `QA/StatusDrillDown/summary-seven-normal.png`

最後の二枚は隣接する読み取り専用アプリリポジトリから取得しました。画面の文字・値・UIを合成せず、元の領域のピクセルを無損失WebPで保持しています。キャプションに実際の画面・表示例を明示しました。Goalは適切な実画面がないため、承認された旅の絵で構成し、架空の進捗UIは加えていません。

[全ファイルのパス、座標、寸法、SHA-256](asset-sources.json)

## ページの順序

Hero → 預かりもの → お値段の様子 → 三つの選択 → きろく → 新しい発見 → 本当にほしいものへ → Characters → Privacy紹介 → Final CTA → FAQ → Privacy Policy → Footer。

## 検証結果

[ブラウザー検証記録](browser-qa.json)の320 / 390 / 768 / 1280 / 1920pxすべてで、横方向のはみ出し、画像の欠落、ページ・コンソール・HTTPエラーはありません。CTA、モバイルメニュー、FAQ、Privacyリンク、Escapeでのダイアログ閉鎖、モバイルのホーム画面開閉を確認しました。JavaScriptを無効にしても本文とナビゲーションが読めます。キーボードの本文移動リンクが動作し、モーション軽減ではスクロールがauto、アニメーションが0です。

実際の画面を目視しました。スマートフォンでは見出し→本文→主ビジュアルの順に並び、Visual Summaryを割合/カテゴリーと日ごとの変化に分けて大きく表示します。Discoveryの実カードと三つの選択の絵も小さなサムネイルにせず表示します。絵の縦横比は維持しています。既存キャラクターの紹介画像は提供された小さな元画像の解像度が上限です。

- [1280px 全体](preview-1280.png)
- [1920px 全体](preview-1920.png)
- [390px 全体](preview-390.png)
- [320px 全体](preview-320.png)
- [デスクトップ Hero](hero-1280.png)
- [モバイルの記録](summary-section-390.png)
- [モバイルの発見](discovery-section-390.png)

部分確認用のキャプチャでは、スクロール時に重なる固定ヘッダーと本文移動リンクだけをキャプチャ時に非表示にしています。全体キャプチャは実際のヘッダーを含みます。

`python3 scripts/build-site.py`: PASS。49の公開ファイルを用意し、ソースと公開成果物の両方でHTML・画像・alt・寸法・アンカー・ARIA・SEO・JSON-LD・robots/sitemapを検証しました。原本・出典・QA文書は公開成果物に含めていません。`git diff --check`: PASS。

[原本・画面・法的文面・SEO・公開設定の比較](preservation-qa.json): 52項目PASS。FAQ以降のHTMLは作業前の保存内容と完全一致。title、description、canonical、OG/X、JSON-LD、faviconのheadも完全一致。robots/sitemap、CNAME、Pages workflow、既存build scriptを保持しています。

## 動作とリンク

既存の内部アンカーと法的外部リンクを保持しました。公開予定CTAは従来どおり案内を開きます。追加したホーム画面の開閉は、モバイルで任意の補助画面を見るためのネイティブdetailsです。アプリ機能は追加・変更していません。架空のApp Store URL・バッジはありません。コミット・push・本番公開は行っていません。

Fake app UI added? NO

Existing FAQ content materially modified? NO

Privacy Policy materially modified? NO

GitHub Pages deployment modified? NO

Existing canonical/SEO metadata preserved? YES

Mobile responsive QA passed? YES
