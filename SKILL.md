---
name: shhh-graph
description: Connect to and verify a live local OriginPro session before auditing, creating, upgrading, or exporting scientific figures. Use whenever the user supplies a scientific chart or data and wants publication-ready visualization, OriginPro reproduction, or an upgraded chart using the SCI technology-future palette. Origin connection is a mandatory gate; never substitute a disconnected Python-only workflow.
---

# Shhh Graph

Create scientifically honest upgraded figures through a verified OriginPro workflow. The connection gate is part of correctness, not an optional integration.

## Mandatory OriginPro gate

Before reading data, choosing a chart, writing plotting code, or modifying artifacts:

1. Run `python scripts/origin_gate.py --show` from this skill directory.
2. Continue only when the command exits with code 0 and returns JSON containing `"connected": true`, a numeric `origin_version`, and `"labtalk_handshake": true`.
3. If the package is missing, run `python scripts/origin_gate.py --ensure-package --show` once. If Origin is not registered or cannot be reached, locate/start the installed OriginPro and retry. Do not run plotting work while disconnected.
4. After three failed connection attempts, stop and report that the Origin gate blocked execution. Do not silently fall back to matplotlib, R, browser charts, or static image generation.
5. Re-run the gate immediately before final Origin export if the task has lasted more than 30 minutes or Origin was restarted.

The current user requirement is strict: a result is incomplete unless a live OriginPro session participated in the workflow.

## Figure workflow after the gate passes

1. Inspect variable types, sample size, units, grouping, dependence, ordering, missingness, distributions, and the claim the chart must support.
2. Read [references/evidence-based-selection.md](references/evidence-based-selection.md) and apply its acceptance test before changing chart geometry.
3. Read [references/upgrade-matrix.md](references/upgrade-matrix.md) and select the matching upgrade by data semantics. Grade A is preferred; Grade B requires its stated condition; Grade C is display-only unless explicitly requested.
4. Apply [references/palette.md](references/palette.md). Reuse [scripts/sci_palette.py](scripts/sci_palette.py) for Python-side preprocessing or specialized geometry.
5. Put the source data or a faithful derived table in an Origin workbook. Prefer native Origin graphs. If specialized geometry requires Python, keep the data in Origin, run the computation through the connected workflow, and load the rendered result back into an Origin image/graph page before completion.
6. Visually inspect the rendered figure. Correct clipping, overlap, inconsistent labels, false color boundaries, broken cluster branches, perspective occlusion, and misleading axes.
7. Save an Origin project (`.opju`) when the task produces a durable figure. Export a PNG preview plus SVG or PDF. Verify the exported files exist and are non-empty.

## Scientific safeguards

- Never invent precise values, uncertainty, significance, linkage, interpolation support, or peak assignments. Synthetic data are permitted only for an explicitly requested demonstration.
- Show raw observations for small samples. Preserve paired and repeated-measure structure.
- State whether intervals are SD, SE, CI, PI, or credible intervals.
- A dendrogram must come from a real linkage and every branch must be connected; otherwise omit it.
- A continuous color encoding needs a labeled colorbar. Bubble magnitude is encoded by area, not radius.
- Bar charts use a zero baseline. Nonzero axes for lines, points, or intervals need visible context.
- Dual axes require explicit units and a defensible mapping; aligned panels are the default alternative.
- Use 3D for true surfaces or ordered spectral stacks, not to decorate ordinary bars.
- Preserve domain conventions such as the XPS binding-energy direction.

## Completion evidence

The final response must state the Origin version used and link the `.opju` project plus exported figure files. If no Origin project/page was created, do not claim the task is complete.
