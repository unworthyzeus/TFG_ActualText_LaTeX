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
| Add comparison to SOA in Results, using a metric close to the most similar results. | Done and expanded. Results now compares the final model to path-loss radio-map papers plus the closest external scalar spread papers: Mi et al. for measured PL/DS/AS point-cloud prediction and Huang et al. for UAV A2G DS/angular-spread prediction. | `TFG/results.tex`, `TFG/state_of_art.tex`, `TFG/TFG.bib` |

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
  and Huang et al.'s UAV A2G Transformer channel-characteristic predictor.
- State of the Art now states that the closest external spread numbers are
  scalar channel-characteristic predictors, not dense CKM maps.
- Results now reports the useful but uncomfortable comparison: the final
  path-loss RMSE is in the same range as strong path-loss-map references; the
  angular-spread RMSE is about 1.5x Mi et al.'s scalar angular-spread error;
  the delay-spread RMSE is much larger than scalar-channel papers, while still
  improving the same-protocol dense CKM spread baselines.

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
