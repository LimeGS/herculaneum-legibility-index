#!/usr/bin/env python3
"""Regenerate figures/gold_density_by_wrap.png.

Gold-window density per panel of the deduplicated June+July wrap-series
union (June panels minus the two `_jordi` re-renders, plus the July
w104-106 panel whose June segment has no published ink map). One bar per
PANEL, drawn across its wrap range; density = gold windows (score >= 0.9)
as % of the panel's windows. The dashed line marks the provisional w037
proxy frontier for the formally transcribed block (see
docs/TRANSCRIPTION_CROSSWALK.md — provisional, not a measured boundary).

Input: full_index_complete.json from the HF dataset repo.
Run: python make_gold_density.py --index /path/to/full_index_complete.json
"""
import argparse
import collections
import json
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--index", default="full_index_complete.json")
    ap.add_argument("--out", default="gold_density_by_wrap.png")
    args = ap.parse_args()

    rows = json.load(open(args.index))
    wr = lambda p: re.search(r"w(\d+)-(\d+)", p)
    union = [w for w in rows if wr(w["panel"]) and
             (w["panel"].startswith("202606") and "_jordi" not in w["panel"]
              or w["panel"] == "20260701183141-w104-106")]
    tot, gold = collections.Counter(), collections.Counter()
    for w in union:
        key = tuple(map(int, wr(w["panel"]).groups()))
        tot[key] += 1
        if w["v3"] >= 0.9:
            gold[key] += 1

    fig, ax = plt.subplots(figsize=(10, 3.2), dpi=150)
    for (a, b), n in sorted(tot.items()):
        ax.bar((a + b) / 2, 100 * gold[(a, b)] / n, width=(b - a + 1) * 0.92,
               color="0.25", edgecolor="0.1")
    ax.axvline(37.5, color="black", linestyle="--", linewidth=1.2)
    ax.text(38.5, ax.get_ylim()[1] * 0.95,
            "w037 provisional proxy frontier\n(formally transcribed block lies to the left)",
            fontsize=8, va="top")
    ax.set_xlabel("wrap number (w010 = innermost, verified from panel geometry)")
    ax.set_ylabel("gold windows, % of panel")
    ax.set_title("Scroll 1: gold-window density by panel wrap range "
                 "(deduplicated June+July union)", fontsize=10)
    ax.set_xlim(8, 131)
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(args.out)
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
