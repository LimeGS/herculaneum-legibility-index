# PHerc 0139: Legible Text Outside the Published Title Region

**A literacy-index sweep of PHerc 0139's official ink maps, human-reviewed
window by window, finds 52 gold-flagged windows across 14 wraps with no
traceable public transcription — outside the title region the community
has already formally published.**

*July 2026. Built from official, already-published ink-detection maps
(`s3://vesuvius-challenge-open-data`), plus a targeted web-research pass
to check each finding against the public transcription record.*

## Background

PHerc 0139 has 38 of 38 segments with official ink-detection maps from a
single model (`new_canon_autoresearch_recipe`, dated 20260417190342),
rendered at 2.399 µm / 78 keV. The scroll's title — *Φιλοδήμου περὶ θεῶν Η*
("Philodemus, On Gods, Book 8") — was formally published on 25-jun-2026
(arXiv 2606.29085, announced at the Biblioteca Nazionale di Napoli
alongside PHerc 1667's complete reading). Outside the title and a handful
of loose terms quoted near it, the paper explicitly does not claim a body
transcription of PHerc 0139
(`docs/evidence_0139/TRANSCRIPTION_STATUS.md`).

## Method

The same window-scoring approach used for Scroll 1
(`WRITEUP_S1_INDEX.md`) was applied to PHerc 0139's 38
official ink maps, using the physical-scale-audited window geometry
described in `docs/evidence_0139/INVENTORY.md` (window size derived from
real mesh vertex spacing, not from an absent `area_vx2` metadata field —
0/38 segments clamped, i.e. every window fit inside its segment).

## Results

- **4,905 windows scored** across 38 segments; **63 windows scored ≥0.9**
  ("gold", 1.28%) (`docs/evidence_0139/STATS.md`).
- **Positive control passes.** The segment named `title` (physically the
  region already known to carry the published title) shows the
  **second-highest gold density of any segment on the scroll** — 2/16 =
  12.5%, essentially tied with wrap w043 (12.82%) — a sanity check,
  consistent with the index surfacing known-legible text before it is
  used to flag anything new (`docs/evidence_0139/STATS.md`).
- **Every one of the 63 gold windows was reviewed by a human, one by one**
  (`docs/evidence_0139/review_0139_human.json`): **54 "clear text" (85.7%)
  + 9 "possible" + 0 "noise" + 0 "artifact"** — none rejected as
  noise/artifact at the gold threshold. Single reviewer, no inter-rater
  check; "clear text" is that reviewer's visual judgment, not a
  transcription.
- The 54 clear-text windows span **15 distinct wraps**: w043 (10), w047
  (8), w044 (7), w049 (4), w046 (4), w024 (4), w045 (3), w034 (3), w059
  (3), w056 (2), title (2, the positive control), and w041/w058/w025/w042
  (1 each) (`docs/evidence_0139/PACKAGE_0139.md`).
- **Web-research cross-check against the public record**
  (`docs/evidence_0139/TRANSCRIPTION_STATUS.md`, 2026-07-07): only the
  title region has a formal published transcription. No public source —
  arXiv 2606.29085, scrollprize.org, or any community repository — was
  found covering wraps w024, w025, w034, w041, w042, w043, w044, w045,
  w046, w047, w049, w056, w058, or w059 (14 wraps). **52 of the 54
  clear-text windows (all except the 2 in the title control) fall in this
  untranscribed territory.**

## Validation

- **Positive control (sanity check):** the title region ranks in the top
  2 of 38 segments by gold density (12.5%, max score 0.961) — consistent
  with the index surfacing known-legible text. A useful external check,
  not by itself a reliability guarantee (`docs/evidence_0139/STATS.md`).
- **Physical scale audited independently of segment metadata:** pixel
  size derived from real mesh vertex distances, cross-checked against the
  theoretical ds8 downsample of the 2.399 µm native volume (measured
  15.3–18.3 µm/px vs. theoretical 19.2 µm/px — consistent within expected
  curvature/flattening discrepancy) (`docs/evidence_0139/INVENTORY.md`).
- **Human review of all 63 gold windows** with a three-way rating scheme
  (clear / possible / noise) rather than a binary accept/reject: 54 clear,
  9 possible, 0 rejected (`docs/evidence_0139/review_0139_human.json`). One reviewer; treat
  "clear" as strong visual candidacy, not verified reading.

## Status of transcription (re-verified 2026-07-11)

Only the title-bearing sequence is formally published (arXiv 2606.29085,
still v1 as of 2026-07-11): *"the title-bearing sequence is read as ...
Φ̣ι[λοδ]ή̣μου περὶ θεῶν Η̅"*, plus a handful of unlocated loose terms near it
(χωρὶς προνο[ί]α̣ς, ἀόρατα, καὶ τὸ κατ̣ὰ̣ φύσις) with no column, wrap, or
segment identifiers given. Because those loose terms exist, "body never
examined" would overstate it; the precise, defensible statement is:
**no wrap-specific public transcription of this scroll's body was located
as of 2026-07-11**. An earlier community observation (9-oct-2025,
scrollprize.org) noted PHerc 0139 as showing the strongest ink signal among
tested scrolls, including a visible tau character — explicitly logged at
the time as "not formally transcribed." No subsequent publication updates
that status for the body of the scroll
(`docs/evidence_0139/TRANSCRIPTION_STATUS.md`).

## Artifacts (published 2026-07-11)

- The classifier used here (checkpoints + card): https://huggingface.co/LimeGS/herculaneum-legibility-proxy
- Its labels/index/evaluator dataset: https://huggingface.co/datasets/LimeGS/herculaneum-legibility-proxy-labels

## Limitations / what this does NOT claim

- "No public transcription found" is the result of web-research passes on
  2026-07-07 and 2026-07-11 against arXiv, scrollprize.org/Substack, and
  public GitHub repositories — it is not a guarantee that no papyrological
  team is actively working on this material, only that no completed,
  published transcription of these specific wraps could be located. Given
  the official pipeline's June-2026 acceleration (PHerc 1667 read end to
  end; official ink-map coverage of Paris 4 now spans wraps w010-w129),
  treat this finding as time-limited triage, not discovery priority.
  `docs/evidence_0139/TRANSCRIPTION_STATUS.md` states this caveat explicitly: "sin
  transcripción pública" ≠ "nadie la está preparando."
  Verification with the papyrological team is the appropriate next step
  before treating any specific window as a discovery.
- This is a legibility index over official, already-public ink maps —
  it identifies where connected letter-scale structure exists, it does
  not transcribe or identify individual letters or words.
- The single-model score used here (no second model exists for PHerc 0139,
  unlike PHerc 172/Scroll 5, where a two-model cross-check exists in project work not yet published) means
  there is no independent-model cross-check comparable to the one applied
  to Scroll 5; the positive control (title region) is the main internal
  validation.
- The nine "possible" (9/63) windows are explicitly not counted
  among the "clear text" findings and should be treated as lower
  confidence.
