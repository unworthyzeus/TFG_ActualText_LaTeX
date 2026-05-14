# Thesis reduction and restructure log - 2026-05-14

Goal: reduce the thesis body to approximately 70 pages before the appendices,
while keeping detailed audit material available in appendices.

## Page-count check

TeX-only compile estimate after the restructure:

- Chapter 1 starts on page 13.
- Appendix A starts on page 80.
- Main thesis body from Chapter 1 through Conclusions is therefore about 67 pages.
- The full document still has larger appendices because detailed material was moved rather than discarded.

Full PDF compilation is still blocked by the local MiKTeX `biber`/`biblatex`
version mismatch. A TeX-only compile succeeds, and a source reference check found
no missing or duplicate labels.

## Main-body changes

- `introduction.tex`
  - Renamed Section 1.2 to "Research questions, answers and contributions".
  - Added direct answers to RQ1, RQ2 and RQ3 in the introduction.
  - Updated the outline so it no longer promises the removed configuration-summary appendix.

- `methodology.tex`
  - Reframed the chapter around the fastest defensible route if the project were started again with the final evidence already known.
  - Kept the earlier U-Net, cGAN, PMNet and PMHHNet models as development evidence instead of deleting them.
  - Added the supervisor's guidance that path loss should replicate the final Try 80 line, while delay/angular spread should include a high-tail or outlier diagnostic.
  - Removed a duplicate distribution-first spread diagram from the main body.
  - Shortened the repeated explanation of why priors came back after distribution-first modelling.
  - Replaced the very long final-prior and final-model formula documentation with compact main-text summaries.

- `prior_detail_overview.tex`
  - Removed the duplicate executive-summary table.
  - Kept one literature-to-design mapping table.
  - Redirected detailed formula/fitting documentation to the appendix.

- `results.tex`
  - Added a compact state-of-the-art comparison table near the final target check.
  - Shortened the runtime repetition in the conclusions/sustainability connection.
  - Replaced the large qualitative-analysis gallery with a short qualitative summary.
  - Replaced the quantisation derivation and table in the limitations section with a short limitation paragraph.

- `conclusions.tex`
  - Shortened the repeated Barcelona runtime benchmark paragraph.
  - Kept the existing research-question answer section.

- `sustainability.tex`
  - Shortened the repeated runtime benchmark details and kept only the energy/sustainability interpretation.

## Appendix changes

- Removed the old Appendix B: "Final Residual GMM-Head Model Configuration Summary".
  - Its essential configuration is now in the methodology table.

- Removed the old Appendix C: "Formula Placement".
  - This was only an index to formulas and became unnecessary after restructuring.

- Removed the old Appendix E: "Implementation Snippets".
  - The code-level snippets were not needed in the thesis body or appendix after the methodology became more compact.

- Added Appendix D: "Additional Qualitative Diagnostics".
  - Moved the full histogram figures, split/regime bar plots, subexpert delta plot and representative inspection panel from Results.

- Added Appendix E: "Quantisation Detail for the Target Maps".
  - Moved the quantisation-floor derivation and table from Results.

- Added Appendix F: "Detailed Final Model Formula Documentation".
  - Moved the detailed path-loss prior, spread-prior and final residual GMM-head formula documentation out of the main methodology chapter.

## Content deleted rather than moved

- Duplicate explanation of priors as an "efficiency and stability device" in the methodology.
- Duplicate executive-summary table in the final-prior overview.
- Duplicate distribution-first spread architecture diagram; the text now explains that it follows the same structure as the path-loss diagram with spread-specific heads.
- Old appendix-only implementation snippets, because the full implementation is already represented by the delivered code and the methodology now contains the key configuration.
