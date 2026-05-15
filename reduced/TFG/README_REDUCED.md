# Reduced TFG source notes

This folder contains the active reduced thesis source and several intermediate
compact drafts created during the page-reduction pass.

## Active compilation path

The current `TFG.tex` compilation uses the main chapter files unless explicitly
included otherwise. The active reduced appendix file is:

- `appendices_compact.tex`

This file is currently necessary because it contains the rebalanced Appendix A,
the CKMGenerator Appendix C, and the one-page Appendix D used by the compiled
PDF.

## Compact drafts kept for traceability

The following files were created as more aggressive compression drafts, but they
were not needed in the final reduced version:

- `introduction_compact.tex`
- `methodology_compact.tex`
- `state_of_art_compact.tex`
- `results_compact.tex`
- `sustainability_compact.tex`
- `conclusions_compact.tex`

They are intentionally kept as editing artifacts so the reduction process is
traceable, but they should not be treated as the canonical text unless `TFG.tex`
is later changed to include them.

The current thesis keeps the fuller chapter versions because the page target was
met through layout improvements, appendix rebalancing, and selective appendix
compression without needing to replace the main chapters with these shorter
drafts.
