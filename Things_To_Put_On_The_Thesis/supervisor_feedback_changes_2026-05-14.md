# Supervisor feedback change log - 2026-05-14

Source note: `Things_To_Put_On_The_Thesis/things_my_supervisor_said_to_fix.md`.

Git status when checked: `git pull --ff-only` returned `Already up to date`.
The supervisor note itself is local/untracked, so it was not part of the pull.

## Summary

The current LaTeX draft already implements the supervisor's "Now" items after
the latest pull. This file records what changed and what was removed or moved,
so the restructure is traceable.

## Supervisor item mapping

| Supervisor item | Current status | Main files |
| --- | --- | --- |
| Answer the research questions in Section 1.2, and answer them again in Conclusions. | Done. Section 1.2 now states RQ1--RQ3, gives short direct answers immediately, and the Conclusions chapter answers the same questions in a dedicated block. | `TFG/introduction.tex`, `TFG/conclusions.tex` |
| Structure Methodology as "if I started with everything I know, what is the best and fastest way", without making that the visible section title. Keep the old models as development evidence. | Done. The chapter intro now frames the methodology this way, while the visible sections remain conventional. Earlier U-Net, cGAN, PMNet and PMHHNet attempts are retained as diagnostic baselines rather than deleted. | `TFG/methodology.tex` |
| For path loss, replicate the Try 80 line; for spreads, consider high-tail/outlier diagnostics. | Partly done. The methodology states this design rule, and Results reports the final Try 80 model versus the frozen priors. A richer spread high-tail/outlier diagnostic remains a good optional final polish. | `TFG/methodology.tex`, `TFG/results.tex` |
| Reduce about 30 thesis pages before the appendices. Remove duplicated explanations/results, improve structure, and move detail to appendices. | Done. The pulled restructure log estimates Chapter 1 through Conclusions at about 67 pages, with detailed material moved to appendices rather than discarded. | `Things_To_Put_On_The_Thesis/reduction_restructure_changes_2026-05-14.md`, `TFG/methodology.tex`, `TFG/results.tex`, `TFG/appendices.tex` |
| Delete old appendices C, E, and B, because B can be explained in Methodology. | Done. The old configuration-summary, formula-placement, and implementation-snippet appendices are gone. Essential configuration is now in Methodology; formula detail moved into the final detailed-formula appendix. | `TFG/methodology.tex`, `TFG/appendices.tex` |
| Add comparison to SOA in Results, using a metric close to the most similar results. | Done and refined. Results now compares the final model to path-loss radio-map papers and RMTransformer as a recent dense radio-map predictor. Scalar channel-parameter papers such as Mi et al. and Huang et al. are kept out of the Results table because they are not dense CKM-style map benchmarks. | `TFG/results.tex`, `TFG/state_of_art.tex`, `TFG/TFG.bib` |

## Removed from the main body

- Duplicate explanation of priors as an efficiency/stability device.
- Duplicate executive-summary table from the final-prior overview.
- Duplicate distribution-first spread architecture diagram.
- Long formula-heavy final-prior and final-model documentation from Methodology.
- Large qualitative gallery from Results.
- Quantisation-floor derivation and table from the Results limitations section.
- Repeated runtime-detail paragraphs from Results/Conclusions/Sustainability.

## Additional compacted-version pass

After recompiling the pulled thesis, the repository was reorganised into two
root-level version folders:

| Version | Source | PDF | Pages |
| --- | --- | --- | --- |
| Previous git version | `old_version/TFG` from commit `e86fa44` | `old_version/TFG_old_version.pdf` | 157 |
| Reduced current version | `reduced/TFG` after local compacting and SOA-comparison edits | `reduced/TFG_reduced.pdf` | 148 |

Additional removals/changes in the compacted current version:

- Added compact spacing only for the main thesis body in `TFG/TFG.tex`, then
  restored the previous spacing before the bibliography and appendix.
- Shortened the State of the Art ending by replacing two synthesis tables and
  several duplicated positioning subsections with a compact synthesis paragraph.
- Shortened the Methodology lesson section and moved the histogram detail to
  the existing appendix reference instead of showing the same figure again.
- Removed redundant Results material: the distribution-fit figure, the spread
  quantisation figure, and three auxiliary final-model delta tables.
- Shortened Conclusions by removing the repeated practical-scope explanation
  and the lessons-learned table already covered by Methodology.

Additional SOA comparison update after supervisor follow-up:

- Added bibliography entries for RadioUNet, noisy-environment radio-map
  prediction, Mi et al.'s measured point-cloud channel-parameter predictor,
  and related A2G/radio-map context papers. Later follow-up removed Huang et
  al. from the comparison tables because it is not dense-map comparable.
- State of the Art now states that the closest external spread numbers are
  scalar channel-characteristic predictors, not dense CKM maps.
- Results now reports the useful but uncomfortable comparison: the final
  path-loss RMSE is in the same range as strong path-loss-map references; the
  angular-spread RMSE is about 1.5x Mi et al.'s scalar angular-spread error;
  the delay-spread RMSE is much larger than scalar-channel papers, while still
  improving the same-protocol dense CKM spread baselines.
- Revised the reduced-version Results comparison table so the former
  `Final / reported metric` ratio column now states whether the final model is
  better, worse, mixed, or not physically comparable. The Conclusions answers
  to RQ1--RQ3 were expanded to make the strongest result, weakest result, and
  height-conditioning conclusion explicit.
- Reworded Table 4.14 again into plain comparison language: each row now states
  directly whether the final model is comparable, better, worse, mixed, or not
  convertible, and the last column says what conclusion is actually fair.
- Tightened Table 4.14 wording so the verdict column explicitly says "our final
  PL/DS/AS" rather than leaving the metric owner implicit.
- Clarified the Mi et al. row in Table 4.14: even though their numbers are much
  better, the row now states that the comparison is not direct because that work
  predicts scalar channel snapshots from point-cloud/RGB/mask inputs rather than
  dense CKM maps.
- Revised Table 4.14 to keep only external comparison rows plus the final-model
  reference row. Removed internal PMHHNet / predecessor / frozen-prior rows from
  the table, removed Gao et al. from this results-side comparison, and replaced
  the indoor/noisy row with more outdoor references: RadioGUNet and ReVeal.
- Reworked Table 4.14 verdict wording so rows no longer start with "Better" or
  "Worse"; they now state "our final PL/DS/AS RMSE is X times better/worse".
- Tried the PathFinder physical-unit conversion: the RM3D DS-RPP normalized
  RMSE is converted with the 36 dB RadioMap3DSeer window, while the unseen-rural
  conversion is explicitly marked as an approximate same-window scale check.
- Aligned the Section 2 positioning table with the cleaned comparison: removed
  the indoor/noisy, Gao et al., PMHHNet, and frozen-prior rows; added RadioGUNet,
  ReVeal, and PathFinder as the outdoor/unseen-domain context rows.
- Replaced the Gao et al. row in the Section 2 evaluation-condition table with
  RadioGUNet, keeping Gao et al. only as background literature context.
- Checked Huang et al. against the source paper and clarified that it is only a
  weak scalar A2G spread reference: the dataset is a Wireless InSite Shandong
  University Software Campus trajectory dataset with two UAV positions, three
  mmWave frequencies, and three flight altitudes, not dense CKM maps.
- Updated the AIRMap comparison to say that the final model is below 2 dB PL
  RMSE and therefore arguably much better than AIRMap's reported below-4 dB
  path-gain threshold, while still noting that an exact ratio is not recoverable.
- Removed Huang et al. from the results and positioning comparison tables,
  keeping only a brief State-of-the-Art note that it is not comparable because
  it predicts scalar link-level A2G channel characteristics rather than dense
  CKM maps.
- Added RMTransformer as the recent, more comparable replacement row: it reports
  dense path-loss radio-map prediction on USC/PMNet maps, with 0.007148
  normalised pixel RMSE (about 1.82 dB under its 254 dB scaling window) and
  0.008099 channel prediction error (about 2.06 dB).
- Strengthened the PMNet/ICASSP row in Table 4.14 so the 1.20x path-loss gap is
  explicitly only a scale reference, not a direct ranking, because PMNet uses a
  different test setup and does not match the unseen-CKM-city, UAV-height, and
  three-target PL/DS/AS conditions used by the final model.
- Moved the detailed Try 78, Try 79, and Try 80 formula/model documentation
  back into Methodology as in the old version instead of leaving it as a
  separate final appendix. Returned the target-map quantisation derivation to
  the Results limitations section, where it lived before.
- Removed Mi et al. from Table 4.14 and changed the table framing so scalar
  channel-parameter papers are not presented as dense CKM map benchmarks.
- Clarified RQ1 with the actual experiment names: Try 76 Distribution-First GMM
  Path-Loss Model and Try 77 Distribution-First Spread Experts show that good
  separate dense PL/DS/AS results are possible without explicit priors, while
  Try 80 Joint Prior-Anchored Residual GMM-Head Model shows that the three
  targets can be predicted jointly.

Version folders now kept inside the same repository:

- `old_version`
- `reduced`

## Moved to appendices

- Detailed path-loss, delay-spread, angular-spread, and final residual GMM-head
  formula documentation now lives under `Detailed Final Model Formula Documentation`.
- Full histogram figures, split/regime bar plots, subexpert delta plot, and
  representative inspection panel now live under `Additional Qualitative Diagnostics`.
- Quantisation derivation and target-map storage detail now live under
  `Quantisation Detail for the Target Maps`.

## Replaced appendix structure

Old appendices removed:

- Old Appendix B: `Final Residual GMM-Head Model Configuration Summary`.
- Old Appendix C: `Formula Placement`.
- Old Appendix E: `Implementation Snippets`.

Current relevant appendices:

- `Detailed Attempt Log`.
- `Representative Final Residual GMM-Head Model Inspection Panels`.
- `CKM Generator Interface and Reproducibility Tool`.
- `Additional Qualitative Diagnostics`.
- `Quantisation Detail for the Target Maps`.
- `Detailed Final Model Formula Documentation`.

## Remaining optional follow-up

- Add a compact per-city holdout table for the final model and priors. This is
  not explicitly in the supervisor note, but it would strengthen the city-holdout
  claim.
- Add one spread-tail diagnostic table or figure, since the supervisor note
  mentions outliers for delay/angular spread.
- If the target remains a full 30-page reduction without touching the appendix,
  the next likely cuts are more aggressive: move more Results breakdowns to
  appendices, shorten Sustainability, and remove further historical Methodology
  detail. The current compacted version saves 9 pages while keeping the
  appendix compiled and adding the new closest-SOA comparison.

## Later paper task

The "Later" section of the supervisor note is intentionally not implemented in
the thesis draft. It should become a separate paper copy with an IEEE-style
two-column LaTeX layout, around 15 pages maximum, keeping the compact result
tables and the key methodology/results figures rather than the full thesis
appendix material.
