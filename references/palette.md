# 科研 SCI · 科技未来色系

Canonical anchors, in low-to-high order:

1. `#44035B` — RGB 68, 3, 91
2. `#404185` — RGB 64, 65, 133
3. `#31688E` — RGB 49, 104, 142
4. `#1F918D` — RGB 31, 145, 141
5. `#38B775` — RGB 56, 183, 117
6. `#90D543` — RGB 144, 213, 67
7. `#F8E620` — RGB 248, 230, 32

## Rules

- Continuous quantities interpolate through all seven anchors in this order and include a labeled colorbar.
- Ordered categories retain anchor order. Unordered categories use `1, 4, 7, 2, 5, 3, 6` for separation.
- Two-sided values use `#44035B → #31688E → #F5F7FA → #38B775 → #F8E620`, centered on a meaningful reference.
- Extensions: text `#172033`; secondary text `#60708A`; white background; panel `#F5F7FA`; grid/missing `#D9E1E8`.
- Preserve monotonically increasing lightness. Never use rainbow/jet.
- Yellow has low contrast on white: use it only for large marks or add a dark outline. Never use it for small body text.
- Do not rely on hue alone for overlapping series; add shape, line style, hatching, or direct labels.
- For more than seven unordered groups, prefer facets or direct labels. Interpolate only after checking separation and color-vision deficiency.
