#!/usr/bin/env python3
"""Regenerate figures/pherc0139_examples.png.

Selection is DISCLOSED and deliberate — showcase examples, not a random
sample: from the 54 human-rated "clear text" windows (rating 1 in
docs/evidence_0139/review_0139_human.json), sorted by descending score,
keep the first window per segment, skip the title-region control and crops
that are >30% near-black, stop at six. Crops are raw windows of the
official PHerc0139 ds8 ink maps at each row's recorded window size,
resized to 256 px for display — no contrast or content editing. Typical
clear-text windows are less clean than these.

Inputs: the review JSON (this repo) and the official PHerc0139 ds8 ink
maps, laid out as <maps-dir>/<segment>/<...>-ds8.jpg (downloadable from
the public bucket under PHerc0139/segments/<segment>/ink-detection/downsampled/).

Run: python make_pherc0139_examples.py --maps-dir /path/to/pherc0139
"""
import argparse
import glob
import json
import re

import numpy as np
from PIL import Image, ImageDraw, ImageFont

Image.MAX_IMAGE_PIXELS = None


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--review", default="../docs/evidence_0139/review_0139_human.json")
    ap.add_argument("--maps-dir", required=True)
    ap.add_argument("--out", default="pherc0139_examples.png")
    args = ap.parse_args()

    rev = json.load(open(args.review))
    clear = sorted([d for d in rev["decisions"] if d["rating"] == 1],
                   key=lambda d: -d["score"])
    picks, seen = [], set()
    for d in clear:
        seg = d["segment"]
        if seg in seen or "title" in seg.lower():
            continue
        jpgs = glob.glob(f"{args.maps_dir}/{seg}/*ds8.jpg")
        if not jpgs:
            continue
        crop = Image.open(jpgs[0]).convert("L").crop(
            (d["x"], d["y"], d["x"] + d["win"], d["y"] + d["win"]))
        if (np.asarray(crop) < 15).mean() > 0.30:
            continue
        seen.add(seg)
        picks.append((d, crop))
        if len(picks) == 6:
            break

    try:
        import matplotlib
        font = ImageFont.truetype(
            str(matplotlib.get_data_path()) + "/fonts/ttf/DejaVuSans-Bold.ttf", 15)
    except Exception:
        font = ImageFont.load_default()
    T, PAD, LABEL = 256, 6, 24
    sheet = Image.new("L", (3 * T + 4 * PAD, 2 * (T + LABEL) + 3 * PAD), 30)
    dr = ImageDraw.Draw(sheet)
    for i, (d, crop) in enumerate(picks):
        m = re.search(r"-(w\d+)_", d["segment"])
        lab = m.group(1) if m else d["segment"][:10]
        cx = PAD + (i % 3) * (T + PAD)
        cy = PAD + (i // 3) * (T + LABEL + PAD)
        sheet.paste(crop.resize((T, T), Image.LANCZOS), (cx, cy))
        dr.text((cx + 4, cy + T + 3), f"{lab}  score {d['score']:.2f}  (clear)",
                fill=255, font=font)
    sheet.save(args.out)
    print(f"wrote {args.out}")
    for d, _ in picks:
        print(f"  {d['segment']} y={d['y']} x={d['x']} win={d['win']} score={d['score']}")


if __name__ == "__main__":
    main()
