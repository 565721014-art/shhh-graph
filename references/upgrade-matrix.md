# 28-case scientific figure upgrade matrix

Grades: **A** preferred automatic upgrade; **B** conditional; **C** display-only unless explicitly requested.

| # | Basic → upgraded | Grade | Enable only when |
|---:|---|:---:|---|
| 1 | Pie/composition → circular waffle | B | Proportions are mutually exclusive, sum to 100%, and groups are few. |
| 2 | Grouped bars → radial grouped bars | B | Categories have cyclic meaning or compact overview is primary. |
| 3 | 3D scatter → surface + bottom contours | A/B | Continuous x-y-z coverage supports interpolation. |
| 4 | 100% stacks → 3D percent stacks | C | Explicitly requested for display; retain a 2D comparison. |
| 5 | Overplotted scatter → density scatter | A | Large n causes occlusion; retain points and colorbar. |
| 6 | Pie → rose/exploded donut | C/B | Few categories and overview, not exact comparison. |
| 7 | Box plot → raincloud | A | Density, raw points, and defined summary each add information. |
| 8 | Bars → radial progress bars | B | Few non-negative progress values share a meaningful range. |
| 9 | Heatmap → circular clustered heatmap | A/B | Matrix clustering is meaningful and linkage is real and connected. |
| 10 | Dual-Y bars → projected 3D bars | C | Display request only; aligned panels remain the accurate default. |
| 11 | Multiple heatmaps → stacked 3D heatmaps | B | Few equal-sized matrices and no important occlusion; otherwise facets. |
| 12 | Overlapping XRD → offset filled spectra | A | Curves share physical x and fills do not hide narrow peaks. |
| 13 | Bars → nested grouped bars | B | Same units/baseline and a real subset or upper-bound relation. |
| 14 | Grouped bars → 3D bars | C | Display request only; grouped bars or heatmap remain primary. |
| 15 | Multiple spectra → 3D wall | B/A | Ordered spectra or response curves benefit from plane separation. |
| 16 | Grouped bars → overlapping nested bars | B | Same units/baseline and the inner series stays fully visible. |
| 17 | Jitter scatter → beeswarm | A | Small-to-medium n and every observation should remain visible. |
| 18 | Two comparable bars → diverging bars | A/B | Same objects and directly comparable units; labels show absolute values. |
| 19 | Stacked bars → polar stacked bars | B | Categories have direction or cyclic meaning. |
| 20 | Composition lines → 100% stacked area | A | Ordered x and composition is normalized at every x. |
| 21 | Category matrix → color-area bubbles | A/B | Two categorical axes plus non-negative magnitude; size and color are explained. |
| 22 | 100% stacks → concentric donuts | C/B | Very few samples/components and overview is the only task. |
| 23 | Box/density panels → step ridgelines | A | Distributions share bin width and x range. |
| 24 | Two spectral families → dual-family 3D waterfall | B/C | Same x-domain, explicit units, and minimal occlusion; otherwise panels. |
| 25 | Multiple lines → 3D point-line | C/B | Sequence order itself has meaning; otherwise use small multiples. |
| 26 | Stacked bars + line → dual-axis composition/total | B/C | The joint explanation is necessary and both axes are explicit and audited. |
| 27 | Offset spectra → 3D waterfall | A/B | Spectral/chromatographic/dose order is real and peaks stay visible. |
| 28 | XPS fits → 3D XPS waterfall | A/B | Shared energy grid, correct axis direction, assignments, and residual meaning. |

Cross-case logic: reveal distributions; structure repeated groups; compact matrices only when traceable; separate overlapping spectra; choose an accurate part-to-whole layout; add a third encoding only when it is explained and useful.
