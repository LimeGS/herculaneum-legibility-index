# A Legibility Index for Scroll 1 (PHerc Paris 4)'s Official Ink Maps

**A validated, human-checked classifier that finds where Scroll 1's already-public
ink-detection maps carry connected, letter-scale text — 77.9% of the
deduplicated panel-series gold lies beyond the provisional w037 proxy for
the formally transcribed region.**

*July 2026. Built entirely from official, already-published ink-detection
maps (`s3://vesuvius-challenge-open-data`, CC BY-NC 4.0) — no new scanning,
no new inference on scan volumes.*

---

## Motivation

Scroll 1 (PHerc Paris 4) has 78 of 81 public segments with official
published ink maps as of 2026-07-08 (verified live against the S3 bucket;
this grew from 52 as of the campaign's initial 2026-07-03 census — coverage
is checked live in this index, not assumed from an earlier count). Nobody
has to guess where the text is on this scroll — the community's own models
already rendered it. What is comparatively cheap and unexplored is
*indexing* that output: quantifying, systematically and at physical scale,
how much of it is dense enough to actually read, and how that overlaps with
what has been formally transcribed.

## Method

The index was built in two passes. **Pass 1** tiled sixteen ink-detection
panels covering wraps w010–w100 (one continuous series, uploaded
2026-06-23) into a 512×512-pixel sliding-window grid (stride 256, ~50%
overlap; each window is physically ≈0.98 cm on a side at the panels'
downsample scale — the project scoring script). A ResNet-18
classifier (`proxy_v4.pt`) was trained through three rounds of
human-in-the-loop labeling on this pass's output:

1. **Round 1:** an unsupervised line-structure/brightness heuristic
   (autocorrelation of the row-brightness profile at the
   physical spacing of Herculaneum text lines, 2.3–5 mm) proposed candidate
   windows; a human tagged the top hits as "interesting" / "unsure" /
   noise, seeding `proxy_v3`.
2. **Round 2:** `proxy_v3` re-ranked all ~20k round-1 candidates; its top
   120 proposals were reviewed by a human one-by-one.
   **Result: 120/120 confirmed by the reviewer** on model-selected
   candidates (consolidated per-row in `train_labels.jsonl`, HF dataset repo) — a review of the model's own top-ranked
   output, not a population precision estimate.
3. **Round 3:** windows the model was genuinely uncertain about
   (0.35 ≤ score ≤ 0.70) were sampled and reviewed to sharpen the decision
   boundary, producing `proxy_v4`.

`proxy_v4`'s held-out spatial AUROC is **0.985** (held-out panels; logged
directly by the training script as "v4 era 0.985" —
the project training log). It was then run
exhaustively over every 512-px window of all 16 panels, closing Pass 1 at
29,853 windows / 4,491 gold.

**Pass 2** (2026-07-08) scored the 62 official maps that appeared or were
found after Pass 1 was built, using the identical unmodified pipeline (same
checkpoint, same window/stride grid, same preprocessing — verified
byte-for-byte SHA256-identical against the official pre-made ds8 preview
before trusting it on new segments). These 62 split into groups that matter
for how the totals below are reported: 23 "classic" individual segments
(name-lineage dedup: 18 physical surfaces — see
`docs/CLASSIC_EQUIVALENCE.md`) and
11 more panels from the same June series (wraps w101–w129), which Pass 1
never touched; of a further 26 panels from a
second complete series (uploaded 2026-07-01), 25 re-cover wrap ranges
**already indexed** — kept as a separate, non-additive bucket to avoid
double-counting the same underlying text — while the 26th (`w104-106`,
131 gold) covers the one wrap range whose June segment has no published
ink map, and therefore joins the deduplicated union; the 2 alternate-processing `_jordi` panels
re-cover indexed ranges as well. (An earlier version of this
index's source model card briefly miscounted the 2 alternate-processing
panels as distinct territory before an adversarial review caught it via a
gold-density-by-row fingerprint match against the originals — full account
in the model card's Coverage section.)

## Results

- **125,298 windows evaluated across all 78 currently-published official
  maps** (complete coverage, verified live 2026-07-08).
- Raw bucket accounting: 4,491 gold from Pass 1 (16 panels, w010–w100)
  + 2,684 from the 23 classic-lineage panels + 1,056 from 11 June panels
  extending to w129 (`full_index_complete.json` (in the HF dataset repo)). **Corrected
  canonical accounting (2026-07-11 peer review): the deduplicated wrap-series
  union is 5,678 gold windows** (June w010–w129 plus the one July panel
  covering w104–106, whose June segment has no published ink map; 131 gold), and the classic bucket
  reduces to 18 physical surfaces / 2,460 representative gold windows,
  kept OUTSIDE the wrap-series denominator because their physical overlap
  with the panel series is unresolved (`docs/CLASSIC_EQUIVALENCE.md`).
- A further **7,248 gold windows** come from the redundant/overlapping
  re-render groups (739 from the 2 alternate-processing panels, 6,285 from
  the 25 truly-redundant July panels, 224 from classic-lineage re-renders)
  — reported separately, never added to the union. These aren't wasted: `w028-037` independently
  scores gold at 50.9% and 40.0% in two unrelated renders, and
  `w046-052`/`w053-058` show matching gold-density fingerprints against
  their `_jordi`-processed counterparts — two informal but real consistency
  checks that the same physical text is being found each time, not scanner
  noise.
- **For Pass 1's original 16-panel scope specifically, 72.1% of gold
  windows lie beyond wrap w037** — i.e. outside the two innermost panels
  (w010–w027, w028–w037; innermost per the physically verified wrap
  orientation, see the crosswalk below) — the side of the scroll where the
  formally published block physically sits; w037 itself is a provisional
  proxy, not a measured block boundary. Computed directly from the
  panel breakdown of Pass 1's 4,491 gold windows: 1,254 in the w010–w037
  panels, 3,237 beyond (recomputable from the Pass-1 subset of the shipped
  full index; this figure itself was
  corrected once in the campaign's own history — an earlier, stale 77%
  carried over from the previous classifier version was caught and fixed to
  72% in commit `7753528`). The equivalent number for the full index is now computed in the
  transcription crosswalk below on the deduplicated June+July wrap-series
  union: 4,424/5,678 = 77.9% beyond the provisional w037 proxy frontier. The classic-segment bucket stays outside that
  denominator pending a physical-overlap resolution
  (`docs/CLASSIC_EQUIVALENCE.md`).

## Validation

- **Round 2 human review: 120/120 confirmed by the reviewer** on the
  classifier's own top-ranked candidates (rows in `train_labels.jsonl`, HF dataset repo)
  — model-selected sample, not a population precision estimate.
- **AUROC 0.985**, held-out panel split (project training log);
  independently frozen: `eval_checkpoint.py` in the public dataset repo
  deterministically rebuilds the split (81 positives / 123 negatives) and
  reproduces **AUROC 0.9853457794** against the published checkpoint.
- **AUROC 0.988** for the immediately preceding version (`proxy_v3`,
  logged by the project training script) — both versions
  independently clear the same high bar on held-out panels; v4 is the
  version actually used for the exhaustive index reported here.
- A held-out 6-window spot-check set (the `verification_only` rows in `train_labels.jsonl`) scores 1.0 on
  every entry — an additional, small-sample confirmation pass distinct
  from the round-2/round-3 human review.

Reported internal replication (2026-07-06 session): six zones spanning
w038-w100 were re-rendered from CT by this project's own pipeline and
correlated against the official panels, giving r = 0.947, 0.966, 0.960,
0.957, 0.966, 0.963 per zone. Scripts are preserved
(project-internal driver script) but the environment is not
packaged (machine-local paths, an SSH box, and a checkpoint outside this
release), so treat this as a reported internal check, not an end-to-end
reproducible artifact.

## Where formal transcription actually stands (crosswalk, corrected 2026-07-11)

The gap flagged in earlier versions of this note ("checking each flagged
region against the team's actual reading progress ... is outside the scope")
is now closed — `docs/TRANSCRIPTION_CROSSWALK.md` (numbers
below reflect its same-day peer-review correction):

- Formally transcribed Scroll 1 text as of 2026-07-11 remains the Grand
  Prize block: 11 columns / ~2000 characters / ~5%, published in ZPE ("The
  Final Columns of PHerc. Paris. 4", 16 final column portions). That text
  is the END of the work, physically the innermost wraps.
- What official sources say in June 2026: the scroll read end to end is
  PHerc 1667; for Paris 4 they report ink directly visible in the new
  high-resolution data, matching the Grand Prize reading one-to-one
  (scrollprize.org/firstscroll). Directly observable in the public bucket:
  official ink maps for panels labeled w010–w129 — ink-map coverage along
  ~120 wraps of the scroll. That coverage is what this index scores.
  Unwrapped/mapped is not transcribed: no formal transcription beyond the
  GP block has been published.
- Wrap orientation was verified physically (panel width per wrap grows
  monotonically 1182 → 7483 px/wrap from w010 to w100; circumference grows
  with radius), so w010 is the innermost wrap and the transcribed block
  lives at low w.
- Frontier: w037 is a **provisional proxy**, not the measured extent of
  the GP block (that requires a visual match against the public GP banner,
  still pending). Physical sizing of the choice: cumulative papyrus through
  w037 is ≈83 cm, and 11 Herculaneum columns span ≈65-90 cm depending on
  column/intercolumn width — w037 is the smallest panel boundary that
  plausibly contains the block, with thin margin either way, which is why
  it is not claimed to be conservative.
- Result on the deduplicated June+July wrap-series union: **4,424 of 5,678
  gold windows (77.9%) lie beyond the proxy frontier**, in territory with
  published official ink maps and no published formal transcription. If the
  18 classic representative surfaces are provisionally added to the
  denominator (their overlap with the series unresolved): 4,424/8,138 =
  54.4%.

Framing consequence: the official pipeline has read one scroll end to end
and is scaling; this index's value is **triage today** — a systematic,
human-reviewed map of where the official output is dense enough to read,
available before the formal transcriptions land — not discovery priority.

## What the index is (and is not)

This is an index over **existing, official, already-public ink-detection
maps** — it adds no new inference on raw scan volumes and reveals no scan
region that was not already processed by the community's own published
models. What it adds is triage: a systematically scored, human-verified
map of where that existing output is dense enough to plausibly contain
readable text, cross-referenced by physical wrap position against where
formal transcription work has concentrated so far.

## Artifacts (published 2026-07-11)

- Model (checkpoints + card): https://huggingface.co/LimeGS/herculaneum-legibility-proxy
- Labels, full 125,298-window index, frozen evaluator, training recipe:
  https://huggingface.co/datasets/LimeGS/herculaneum-legibility-proxy-labels
- Transcription crosswalk: `docs/TRANSCRIPTION_CROSSWALK.md`
  (with `CLASSIC_EQUIVALENCE.md` for the classic-bucket dedup)

## Limitations / what this does NOT claim

- This index does not itself transcribe any text; it flags regions as
  containing letter-scale connected structure at a resolution a human can
  then read.
- "Beyond w037" is grounded in the transcription crosswalk, with w037 as a
  provisional proxy frontier (see the section above and
  `docs/TRANSCRIPTION_CROSSWALK.md`). Residual
  uncertainty, declared: the GP block's wrap extent is bounded, not pinned
  (banner↔panel visual match pending; per the physical sizing in the
  crosswalk the margin is thin, so pinning it could shift the frontier in
  either direction), and the classic segments' physical overlap
  with the panel series is unresolved — they are excluded from the headline
  denominator rather than assumed distinct.
- Pass 1's gold-window area was estimated at the order of **~1,120 cm²**
  (window/stride geometry; ~1,080–1,170 cm² depending on exact per-panel
  pixel scale — an order-of-magnitude estimate, not a pixel-exact
  segmentation of gold-flagged surface). This has likewise not been
  recomputed for the corrected full-index accounting (5,678 wrap-series
  union + the separate classic bucket); scaling roughly by window count
  would put it in the low thousands of cm², but that is an extrapolation,
  not a reported figure.
- The classifier was trained on Scroll 1 imagery only; its Scroll 2/3
  adaptation (`proxy_S2S3_v1`, trained with S2/S3 negatives) is a separate,
  distinct artifact used in the campaign's negative sweep results, not in
  the numbers reported here.
- The 6-zone replication figures (r = 0.947–0.966) are a reported internal
  check, as flagged above — scripts preserved, environment not packaged.
