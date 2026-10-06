# Tamepyon background edit

Date: 2026-10-06 (JST).

Tool: built-in `image_gen.imagegen`, edit mode, opaque background. No CLI/API fallback.

Edit target: `assets/images/tamepyon.webp` (the existing panel-22 crop). Background references: `assets/images/jikyuchan.webp`, `assets/images/okaneko.webp`.

Active website outputs:

- `assets/images/tamepyon-light.webp` — 145×120 lossless WebP.
- `assets/images/tamepyon-light-112.webp` — 112×93 lossless WebP.

The tool's PNG output was downsampled and encoded for the existing website slot. Original assets are retained. The homepage uses the new filenames with the same dimensions, alt text and layout. Static site build and SEO/asset validation passed.

## Final prompt

```text
Use case: precise-object-edit. Edit target: image 1, the existing pink bunny Tamepyon hugging an orange carrot. Images 2 and 3 are background color references ONLY, not characters to add. Change only image 1's background: make the yellow cream field much lighter, nearly off-white warm ivory (#fffdfa), matching the extremely pale subtle background of the other two character portraits. Lighten the yellow sparkles and green ground patch substantially so they become subtle low-contrast pastel decoration. Preserve the bunny and carrot EXACTLY: same existing upright ears, body, face, cheeks, pose, expression, brown outlines, orange carrot and green carrot leaves, yen mark, proportions, crop and placement. Do not redraw, modernize, sharpen or redesign the character. Do not lighten or wash out the bunny or carrot. Keep original landscape aspect ratio 145:120 and full original composition, no added padding, no text, no new objects. Deliver only the edited bunny asset, not a three-character collage.
```
