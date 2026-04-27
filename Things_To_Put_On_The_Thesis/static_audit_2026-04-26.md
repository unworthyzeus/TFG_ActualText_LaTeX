# Static thesis audit - 2026-04-26

Scope: `C:\TFG\FINAL_THESIS\TFG`.

## Checks completed

- No duplicate `\label{...}` values were found across the top-level thesis
  `.tex` files.
- No citation key used by `\cite{...}` was missing from `TFG.bib`.
- The current LaTeX log reports an empty bibliography because the generated
  `TFG.bbl`/`TFG.blg` files are absent or stale. This should be fixed by
  rebuilding with Biber, not by adding bibliography entries.
- Source-only `git diff --check` passes for `.tex` files.

## Edits applied

- Polished global caption/link styling in `TFG/config/styles.tex`.
- Added `\emergencystretch` and rewrote several wide tables/equations to reduce
  likely overfull boxes.
- Cleaned old template comments and small typos in `TFG.tex`.
- Expanded `conclusions.tex` with research-question answers, contributions,
  negative results, limitations, and future work.
- Cleaned informal wording in `results.tex`.
- Split one long Try 80 paragraph in `prior_detail_try80.tex`.

## Remaining intentional blockers

- `\setReviewer{TBD}` is still present in `TFG.tex`; fill it when the reviewer
  is known.
- Try 80 final-test placeholders remain in `results.tex`, `appendices.tex`,
  `state_of_art.tex`, and `sustainability.tex` by project choice until the
  frozen checkpoint/test split is ready.
- The PDF was not rebuilt in this pass. Project instructions say not to run
  LaTeX compilation automatically.

## Recommended rebuild command

From `C:\TFG\FINAL_THESIS\TFG`:

```powershell
latexmk -lualatex -interaction=nonstopmode -file-line-error TFG.tex
biber TFG
latexmk -lualatex -interaction=nonstopmode -file-line-error TFG.tex
```
