# Pending: per-city holdout table and Try 80 freeze / placeholder handling

Two related things to revisit before defense. Both are about turning the city-holdout story and the Try 80 narrative into something the jury can check, not just take on faith.

## 1. Per-city holdout RMSE table

The city-holdout split is the thesis's single most distinctive methodological claim, but no table in `results.tex` currently shows RMSE broken down per held-out city. A jury can reasonably ask: "if the model generalises to unseen cities, what does it do on each of them?"

What to produce:

- Per-city RMSE on the test-split cities for at least:
  - Try 78 path loss (overall / LoS / NLoS)
  - Try 79 delay spread and angular spread (overall / LoS / NLoS)
  - Try 80 final joint model (once the checkpoint is frozen)
- Include the sample count per city so small-N outliers (e.g. high-rise cities with 50-ish samples) are obvious.
- Prefer top-N largest holdout cities + a row for "rest (aggregate)" rather than a 20-row table.

Where the data lives:

- `TFGSeventyEighthTry78/hybrid_out_final_dml/hybrid_eval_summary.json` — `per_sample` list contains `city`, `sample`, `uav_height_m`, `n_los`, `n_nlos`, and per-sample RMSE components. Aggregate per-city by pixel-weighting `n_los`/`n_nlos` against the per-sample RMSEs.
- `TFGSeventyNinthTry79/test_eval_test_verify/eval_summary_test.json` — same `per_sample` structure for delay/angular.
- Try 80 per-sample will need to be exported from the final validation/test run.

Target placement: new `\begin{table}` in `results.tex` after `tab:try79_results`, plus a one-paragraph interpretation (which city types break which prior, where Try 80 pays off).

## 2. Try 80 placeholders across chapters

The following files currently contain "placeholder / pending / not final" language that is fine for a draft but cannot ship:

- `summary.tex` — abstract mentions "Try 80 results intentionally left as placeholders" (do not ship in an abstract)
- `results.tex` — chapter intro L2-6, `tab:try80_placeholder` (L136-150), `fig:try80_val_placeholder` (L160-201), `fig:try80_history` (L222-228), limitations L299-303
- `conclusions.tex` — mentions Try 80 still training
- `appendices.tex` — placeholder text L356-362

Two options, pick one:

**Option A — freeze a checkpoint now.** Run `evaluate_try80.py` on the test split with the current best validation checkpoint. Report it under the same pixel-weighted contract as Try 78 (overall / LoS / NLoS, plus delay and angular spread). Replace every placeholder with those numbers. The caveat paragraph stays — "this is a single-seed, single-run result" — but the thesis no longer depends on a future event.

**Option B — reframe as an in-flight extension.** Keep the Try 78/79 frozen priors as the headline result. Present Try 80 explicitly as an unfinished exploration whose design, validation trajectory, and expected behaviour are documented, but whose final numbers are out of scope. Update:

- Abstract → drop the "placeholders" sentence; state that the prior pipeline is the main quantitative contribution.
- Results chapter intro → change "final test results are intentionally left as placeholders" to "Try 80 is an ongoing extension built on top of the frozen Try 78/79 priors; this chapter reports the frozen-prior results as the main quantitative outcome and the current Try 80 validation snapshot as a diagnostic."
- Conclusions → list Try 80 as future work, not pending result.

Recommended default until the checkpoint is frozen: apply Option B. It is internally consistent, honest with the jury, and does not block submission on an external training event. Option A supersedes it if a good checkpoint becomes available in time.

## Other open items (light)

- **Resolved (2026-04-24).** Gao et al. "5.6 dB" verified in the paper: Table III of arXiv:2601.08436 reports 5.59 dB RMSE on ICASSP 2023 data (PPNet baseline 8.09 dB, RPNet 9.56 dB, ViT 8.72 dB); Table II reports 12.19 dB on ITU Challenge 2024 large-area subset. `state_of_art.tex` now cites the 5.59 dB number with a specific table reference in both the in-text description (§ Gao et al.) and `tab:position`.
- **Resolved (2026-04-24).** Try 71 coverage-RMSE claim in `state_of_art.tex` softened: `TFGSeventyFirstTry71/` has no local `outputs/` directory and no entry in `cluster_outputs/`, so no RMSE-vs-coverage curve can be produced from current artefacts. The SOA paragraph now frames Try 71 as a conceptual step toward Try 76 rather than as a finalised experiment with a coverage curve. If the cluster run is ever completed, the paragraph can be upgraded to cite the real curve.
