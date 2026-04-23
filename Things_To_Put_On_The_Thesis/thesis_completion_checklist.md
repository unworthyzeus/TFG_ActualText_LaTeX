# TFG thesis completion checklist

Structured working copy of `summary.md`. Status values:

- `[ ]` pending
- `[~]` in progress
- `[x]` completed in thesis draft
- `[?]` needs user confirmation or final Try 80 data

## Foundations and scope

- [x] Explain the project problem and scope using the proposal and workplan.
- [x] Describe the dataset structure: 513x513 maps, topology, LoS mask, path loss, delay spread, angular spread, antenna height, sample number and city.
- [x] Explain dataset characteristics and limitations, including quantization/storage types for path loss and spreads.
- [x] State original performance goals: path loss below 5 dB RMSE, delay spread below 50 ns RMSE, angular spread below 20 degrees RMSE, globally and for LoS/nLoS.
- [x] Add all introduced abbreviations to `acronyms.tex`.

## Attempt history

- [x] Explain the first U-Net + cGAN approach and why it did not work.
- [x] Summarize architecture/data-processing attempts before the major architecture change, including Try 22.
- [x] Explain that cGAN training did not materially improve the results.
- [x] Explain why separated models for each output and early LoS/nLoS separation did not solve the problem.
- [x] Explain the first physical priors and why their catastrophic nLoS failure was initially hidden by the same weakness in the neural models.
- [x] Summarize prior variants, Try 66 state-of-the-art implementation, obstruction channels, and architectures around Try 50-75.
- [x] Explain the post-Try-75 histogram diagnosis and the decision to move to distribution-first prediction.
- [x] Explain why Try 76 strongly improved nLoS path loss while slightly worsening LoS.
- [x] Explain Try 77 improvements for delay and angular spreads and why spread distributions are harder than path loss.

## Final methods

- [x] Explain topology/expert splitting in Tries 76, 77 and 80, and the larger prior split used in Tries 78 and 79.
- [x] Explain the final train/validation/test split for Tries 76, 77 and 80, including why it is stricter than weaker alternatives.
- [x] Explain sinusoidal FiLM conditioning and its inspiration.
- [x] Include a full schema of final Tries 76-80, using diagrams from `TFGpractice` where useful.
- [x] Incorporate and adapt the internal documentation, especially `New Prior Formulas Try 78 and 79.tex`.
- [x] Explain the updated state-of-the-art comparison and how the final method differs from prior work.
- [x] Explain what is new in the project overall.

## Priors and final results

- [x] Explain Try 78 calibrated path-loss prior, with paper-backed formulas and LoS/nLoS results.
- [x] Explain Try 79 delay-spread and angular-spread priors, with paper-backed formulas and results.
- [?] Explain Try 80 joint prior-anchored model while leaving final trained-model results as placeholders.
- [x] Use existing good/bad panels and samples, adding more if needed.

## Planning, sustainability and closure

- [x] Modify the TikZ Gantt chart to show broad architecture phases: 1-20, 20-50, 50-75, and 76-80.
- [x] Explain how the project changed from the original plan and what worked or failed.
- [x] Add future work: varying frequencies and a general outdoor CKM model.
- [x] Discuss compute and sustainability: four RTX 2080 Ti GPUs, roughly 1500 W, 12 h final Try 80 run, 18 h for Tries 76-79, over 200 h overall not counted directly, and avoided simulation energy/time.
- [x] Leave acknowledgements and dedication untouched for the user.

## Build and review

- [x] Preserve the original template sections and only add subsections when needed.
- [x] Match the baseline style and formatting.
- [x] Number figures, equations and tables.
- [?] Compile the thesis and fix LaTeX errors. TeX is not installed/on PATH in this environment, so only static checks have been run.
