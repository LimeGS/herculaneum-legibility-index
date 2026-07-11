#!/usr/bin/env python3
"""Regenerate figures/gold_examples.png.

Selection is DISCLOSED and deliberate — these are showcase examples, not a
random sample: from the deduplicated June wrap-series panels beyond w037
(the candidate zone), take gold windows with score >= 0.99, at least 1536 px
from the panel's top edge and 1024 px from the left (interior windows), drop
crops that are >28% near-black (panel-boundary wedges), keep the first
window per panel by descending score, stop at six. Crops are raw 512 px
windows of the official ds8 ink maps, resized to 256 px for display — no
contrast or content editing.

Inputs: full_index_complete.json (HF dataset repo) and the official panel
jpgs (fetch with the dataset repo's generate_crops.py --download, or point
PANELS_DIR at a local copy).

Run: python make_gold_examples.py --index /path/to/full_index_complete.json \
        --panels-dir /path/to/panels --out gold_examples.png
"""
import argparse
import json
import re

import numpy as np
from PIL import Image, ImageDraw, ImageFont

Image.MAX_IMAGE_PIXELS = None


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--index", default="full_index_complete.json")
    ap.add_argument("--panels-dir", default=".")
    ap.add_argument("--out", default="gold_examples.png")
    args = ap.parse_args()

    rows = json.load(open(args.index))
    wr = lambda p: re.search(r"w(\d+)-(\d+)", p)
    cand = [w for w in rows
            if wr(w["panel"]) and w["panel"].startswith("202606")
            and "_jordi" not in w["panel"]
            and int(wr(w["panel"]).group(1)) >= 38
            and w["v3"] >= 0.99 and w["y"] >= 1536 and w["x"] >= 1024]
    cand.sort(key=lambda w: -w["v3"])

    cache = {}
    def crop(w):
        p = w["panel"]
        if p not in cache:
            cache[p] = Image.open(f"{args.panels_dir}/{p}.jpg").convert("L")
        return cache[p].crop((w["x"], w["y"], w["x"] + 512, w["y"] + 512))

    picks, seen = [], set()
    for w in cand:
        if w["panel"] in seen:
            continue
        if (np.asarray(crop(w)) < 15).mean() > 0.28:
            continue
        seen.add(w["panel"])
        picks.append(w)
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
    d = ImageDraw.Draw(sheet)
    for i, w in enumerate(picks):
        im = crop(w).resize((T, T), Image.LANCZOS)
        cx = PAD + (i % 3) * (T + PAD)
        cy = PAD + (i // 3) * (T + LABEL + PAD)
        sheet.paste(im, (cx, cy))
        d.text((cx + 4, cy + T + 3),
               f"{wr(w['panel']).group(0)}  score {w['v3']:.2f}",
               fill=255, font=font)
    sheet.save(args.out)
    print(f"wrote {args.out}")
    for w in picks:
        print(f"  {w['panel']} y={w['y']} x={w['x']} score={w['v3']}")


if __name__ == "__main__":
    main()
