"""SCI technology-future palette helpers for Shhh Graph."""

from __future__ import annotations

from matplotlib.colors import LinearSegmentedColormap, to_rgb

ANCHORS = (
    "#44035B", "#404185", "#31688E", "#1F918D",
    "#38B775", "#90D543", "#F8E620",
)
NEUTRALS = {
    "text": "#172033", "secondary_text": "#60708A",
    "background": "#FFFFFF", "panel": "#F5F7FA",
    "grid": "#D9E1E8", "missing": "#D9E1E8",
}


def sequential(name: str = "sci_tech_future") -> LinearSegmentedColormap:
    return LinearSegmentedColormap.from_list(name, ANCHORS, N=256)


def diverging(name: str = "sci_tech_future_diverging") -> LinearSegmentedColormap:
    colors = (ANCHORS[0], ANCHORS[2], NEUTRALS["panel"], ANCHORS[4], ANCHORS[6])
    return LinearSegmentedColormap.from_list(name, colors, N=256)


def categorical(n: int) -> list:
    if n < 1:
        return []
    order = (0, 3, 6, 1, 4, 2, 5)
    if n <= len(order):
        return [ANCHORS[index] for index in order[:n]]
    cmap = sequential()
    return [cmap(index / (n - 1)) for index in range(n)]


def relative_luminance(hex_color: str) -> float:
    def linearize(value: float) -> float:
        return value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4

    red, green, blue = (linearize(value) for value in to_rgb(hex_color))
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def contrast_ratio(first: str, second: str) -> float:
    lighter, darker = sorted((relative_luminance(first), relative_luminance(second)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


def audit_palette() -> dict[str, object]:
    luminance = [relative_luminance(color) for color in ANCHORS]
    yellow_contrast = contrast_ratio(ANCHORS[-1], NEUTRALS["background"])
    return {
        "anchor_count": len(ANCHORS),
        "relative_luminance": [round(value, 4) for value in luminance],
        "monotonic_luminance": all(a < b for a, b in zip(luminance, luminance[1:])),
        "yellow_on_white_contrast": round(yellow_contrast, 2),
        "yellow_requires_outline_or_large_mark": yellow_contrast < 3.0,
    }


def apply_matplotlib_style() -> None:
    import matplotlib as mpl

    mpl.rcParams.update({
        "figure.facecolor": NEUTRALS["background"],
        "axes.facecolor": NEUTRALS["background"],
        "axes.edgecolor": NEUTRALS["text"],
        "axes.labelcolor": NEUTRALS["text"],
        "text.color": NEUTRALS["text"],
        "xtick.color": NEUTRALS["text"],
        "ytick.color": NEUTRALS["text"],
        "grid.color": NEUTRALS["grid"],
        "axes.spines.top": False,
        "axes.spines.right": False,
        "savefig.facecolor": NEUTRALS["background"],
        "savefig.bbox": "tight",
    })


if __name__ == "__main__":
    print(audit_palette())
