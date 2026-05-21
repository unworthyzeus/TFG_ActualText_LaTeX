# Supervisor Fix Checklist

Source PDF: `C:/Users/guill/Downloads/TFG_draft_21may_GV.pdf`

Use this as the working tracker. Each item keeps only a short title, PDF page,
reference text, and the way it was fixed.

## General Comments From Email

- The draft is a good first draft, but it can probably become shorter.
- Methodology and Results should focus only on the final model; intermediate
  steps dilute the reader's attention.
- Negative results are valuable, but they should probably be kept in an
  appendix rather than the main text.
- Refactor Sections 3 and 4.
- Clean up Section 2 so it contains background only, without thesis results.

- [x] SC-001 P16 - Add 3GPP UxNB term
  - Ref: "UAVs may act as aerial base stations..."
  - How fixed: Added UxNB at the first UAV base-station mention and added the acronym definition.

- [x] SC-002 P16 - Check reference numbering
  - Ref: First paragraph citations `[50, 51]`.
  - How fixed: Changed bibliography sorting to citation order (`sorting=none`) and added the 3GPP UxNB reference.

- [x] SC-003 P16 - Clarify LoS/NLoS mask input
  - Ref: "a geometrically derived LoS/NLoS mask"
  - How fixed: Clarified that the mask is an input/support variable, read from CKM when available and generatable from topology for deployment.

- [x] SC-004 P16 - Fix channel/path-loss terminology
  - Ref: "outputs... path loss, delay spread, and angular spread"
  - How fixed: Rephrased the introduction around dense CKM target maps and used path loss, delay spread, and angular spread consistently.

- [x] SC-005 P16 - Pick final framework name
  - Ref: "learned surrogate"
  - How fixed: Named the final framework `\textsc{HARP-Net CKM}` and defined it in the introduction.

- [x] SC-006 P17 - Define city-holdout
  - Ref: "strict city-holdout protocol"
  - How fixed: Added a short definition explaining that whole cities are withheld from training.

- [x] SC-007 P17 - Avoid unexplained model label
  - Ref: "selected prior-anchored residual model"
  - How fixed: Replaced unexplained labels with `\textsc{HARP-Net CKM}` in the introduction and conclusions.

- [x] SC-008 P17 - Spell out three targets
  - Ref: "all three dense targets"
  - How fixed: Expanded the phrasing to path loss, delay spread, and angular spread.

- [x] SC-009 P17 - Simplify RQ teaser
  - Ref: "these questions can be answered directly..."
  - How fixed: Shortened the research-question answer teaser in the introduction.

- [x] SC-010 P17 - Explain ground-only masking
  - Ref: "ground-only masking"
  - How fixed: Rephrased as valid ground receivers/users and clarified that building pixels are excluded from loss and metrics.

- [x] SC-011 P17 - Explain city-holdout splits
  - Ref: "city-holdout splits"
  - How fixed: Added explicit split explanation in the introduction and methodology dataset section.

- [x] SC-012 P17 - Clarify FR3 UAV dataset
  - Ref: "the FR3 UAV dataset"
  - How fixed: Reworded as the CKM dataset / fixed CKM simulation setting, with FR3 kept as context where needed.

- [x] SC-013 P17 - Expand OLS
  - Ref: "OLS"
  - How fixed: Expanded OLS to ordinary least squares in the contributions.

- [x] SC-014 P17 - Replace/define "head"
  - Ref: "OLS NLoS head", "GMM-head model"
  - How fixed: Removed casual "head" wording from the introduction; technical chapters keep it where the architecture is defined.

- [x] SC-015 P17 - Explain distribution-first diagnosis
  - Ref: "distribution-first diagnosis"
  - How fixed: Rephrased as target-distribution analysis showing when Gaussian/MSE assumptions fail.

- [x] SC-016 P18 - Add chapter numbers
  - Ref: Section 1.3 thesis outline.
  - How fixed: Added chapter-numbered outline entries in the introduction.

- [x] SC-017 P18 - Remove "canonical"
  - Ref: "The canonical dataset contains..."
  - How fixed: Replaced with "The CKM dataset contains...".

- [x] SC-018 P18 - Rephrase ground pixels as ground users
  - Ref: "All losses and metrics are computed only on ground pixels."
  - How fixed: Reworded around ground receivers/users.

- [x] SC-019 P19 - Explain final model, not chronology
  - Ref: Section 1.6 work plan.
  - How fixed: Rewrote the work-plan/procedure text as the final-method route with chronology moved to appendix.

- [x] SC-020 P21 - Reduce hyphen overuse
  - Ref: "fair-comparison"
  - How fixed: Rephrased affected comparison wording while keeping necessary technical compounds.

- [x] SC-021 P21 - Use "channel gain" only
  - Ref: "path loss, channel gain"
  - How fixed: Changed the CKM background wording to "channel gain, angles, or delay information."

- [x] SC-022 P21 - Remove thesis results from SOTA
  - Ref: Chapter 2 opening.
  - How fixed: Rewrote the Chapter 2 opening and removed final-result language from the SOTA discussion.

- [x] SC-023 P22 - Define two-ray equation terms
  - Ref: `E_total = E_direct + Gamma E_reflected e^{j Delta phi}`
  - How fixed: Replaced the shorthand equation with direct/reflected path lengths and coherent field terms.

- [x] SC-024 P22 - Simplify or illustrate two-ray model
  - Ref: "deterministic radial structure..."
  - How fixed: Added a small two-ray schematic figure and explanatory text.

- [x] SC-025 P22 - Replace vague morphology wording
  - Ref: "morphology types"
  - How fixed: Replaced with environment/city type wording.

- [x] SC-026 P22 - Replace "polynomials"
  - Ref: "path-loss polynomials"
  - How fixed: Replaced with path-loss expressions.

- [x] SC-027 P23 - Add spread formulas
  - Ref: RMS delay spread and angular spread definitions.
  - How fixed: Added RMS delay-spread and circular angular-spread equations.

- [x] SC-028 P23 - Reuse benchmark numbers in Results
  - Ref: RadioUNet/RadioGUNet numbers.
  - How fixed: Kept RadioUNet/RadioGUNet figures in the final Results comparison table.

- [x] SC-029 P23 - Add SOTA limitations paragraphs
  - Ref: "These papers are useful path-loss scale references..."
  - How fixed: Added/strengthened limitations paragraphs for benchmark families and external references.

- [x] SC-030 P24 - Point to Table 2.1
  - Ref: "After this correction, the true physical errors are:"
  - How fixed: Rephrased PMNet/benchmark discussion to point to the SOTA comparison table rather than inline result claims.

- [x] SC-031 P24 - Review CKM comparability paragraph
  - Ref: "These numbers are not directly comparable..."
  - How fixed: Rewrote the fair-comparison checklist and comparability paragraph around split, height, mask, target unit, and calibration source.

- [x] SC-032 P24 - Move PMNet transfer-test results
  - Ref: "A separate transfer test performed in this thesis..."
  - How fixed: Moved the PMNet transfer-check note to Appendix A.

- [x] SC-033 P25 - Review transformer/global-context claim
  - Ref: "global context is necessary..."
  - How fixed: Softened the claim to say global context is useful, not universally necessary.

- [x] SC-034 P25 - Review foundation-model horizon claim
  - Ref: "long-term direction of the field..."
  - How fixed: Rephrased as a future-work horizon and limitation rather than a settled field direction.

- [x] SC-035 P29 - Motivate training stabilisation section
  - Ref: Section 2.7.
  - How fixed: Added a motivation paragraph explaining overfitting, city holdout, heavy tails, and target quantization.

- [x] SC-036 P29 - Fix target quantity units
  - Ref: "path loss (dB), path gain (dBm), received power..."
  - How fixed: Corrected the target-unit checklist to path loss/path gain in dB, received power in dBm, delay in ns, and angular spread in degrees.

- [x] SC-037 P33 - Move final-model values to Results
  - Ref: "Final model (this thesis)" table row.
  - How fixed: Removed final-model values from SOTA and kept final values in Chapter 4.

- [x] SC-038 P34 - Rename Dataset protocol
  - Ref: "Dataset protocol"
  - How fixed: Renamed it to "Dataset and split."

- [x] SC-039 P34 - Add height-distribution figure
  - Ref: Transmitter-height sample distribution paragraph.
  - How fixed: Added a PGFPlots figure using `data/uav_height_histogram_3m.csv`.

- [x] SC-040 P36 - Rewrite methodology around final method
  - Ref: Section 3.2 diagnostic baselines.
  - How fixed: Replaced diagnostic-baseline sections with a final pipeline overview and appendix pointer.

- [x] SC-041 P59 - Remove "free-space-like"
  - Ref: "a free-space-like offset"
  - How fixed: Replaced with a precise definition of `\lambda_0` as the free-space reference level inside the raw A2G NLoS envelope.

- [x] SC-042 P69 - Delete "not cosmetic"
  - Ref: "The addition of 1 is not cosmetic."
  - How fixed: Replaced with "The constant 1 keeps exact zeros finite...".

- [x] SC-043 P86 - Focus Results on final results
  - Ref: Chapter 4 opening.
  - How fixed: Rewrote the Results opening around final priors and `\textsc{HARP-Net CKM}`, removed the milestone table, and pointed the history to Appendix A.

- [x] SC-044 P104 - Reframe economic impact
  - Ref: Section 5.3 economic and social impact.
  - How fixed: Reframed the work as a technical prototype, not a market-ready product.

- [x] SC-045 P107 - Positive note, no action
  - Ref: Chapter 6 answer section.
  - How fixed: No content change required beyond keeping the answer section.

- [x] SC-046 P108 - Move struggles to annex
  - Ref: Section 6.1.5 negative results.
  - How fixed: Shortened the negative-results conclusion and directed the detailed attempt history to Appendix A.
