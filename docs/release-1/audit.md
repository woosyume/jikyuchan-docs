# Release 1.0 — existing content audit (2026-10-07)

Implementation scope: website only. No production deploy, app edits, or generated character art.

| Existing content | Classification | Reason / final direction |
| --- | --- | --- |
| Hero headline, room composition, price/time example | KEEP | Immediate product concept and approved artwork remain authoritative. |
| Hero secondary feature paragraph | MOVE | Introduce self-discovery after the record story, keeping the first screen simple. |
| Character introduction / portraits | MOVE + UPDATE | After the product journey; companions who watch choices, correct current names. |
| Six equal feature cards | UPDATE | Replace the uniform grid with alternating scenes and short narrative bridges. |
| Reconstructed calculation / choice phone screens | REMOVE | Existing mock UI is not an authentic production screenshot; Hero already explains price/time. |
| Standalone がまんまる card | MOVE | Preserve approved illustration in the Goal scene without emphasizing nonpurchase as success. |
| Goal philosophy | KEEP + UPDATE | Remove invented 60% / 42,800円 UI. Prefer authentic capture when available. |
| Numeric Insight mock cards and old Discovery example | REMOVE + UPDATE | Use the two exact production messages from Core/PriceDecisionInsights.swift, equally weighted. |
| 預かりもの / price history / Visual Summary | NEW | Real screenshots found in the read-only adjacent app repository. |
| Final CTA / prerelease dialog | KEEP + UPDATE | 2026年10月26日公開予定, no invented download link. Move final CTA after companions/privacy. |
| FAQ | KEEP + UPDATE | Current キープ wording and short import explanation. |
| Privacy policy | KEEP + UPDATE | Verify local processing and external product/price requests; add a brief product-facing introduction. |
| Canonical, sitemap, robots, WebSite JSON-LD, OG art, favicon | KEEP | Update title/descriptions only; retain public URLs and source/build validation. |

Read before implementation: index.html, styles.css, site.js, README, asset provenance, responsive/retina notes, build/check scripts; adjacent app ProductImport, Models, ProductMetadata, PeriodVisualSummaryView, PriceDecisionInsights, JikyuchanApp and Japanese localization. Existing crops app-home/app-saved/app-collection come from a design board and are not production screenshots.
