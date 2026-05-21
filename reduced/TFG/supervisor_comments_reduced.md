# Supervisor Comments - Reduced Fix List

Source PDF: `C:/Users/guill/Downloads/TFG_draft_21may_GV.pdf`

This file condenses the supervisor annotations into fix items. The PDF contains 67 annotations; paired highlights and note icons are merged below, and standalone highlights/strikeouts are kept as their own items when they appear to require review.

## General Comments From Email

- The draft is a good first draft, but it can probably become shorter.
- Methodology and Results should focus only on the final model; intermediate steps dilute the reader's attention.
- Negative results are valuable, but they should probably be kept in an appendix rather than the main text.
- Refactor Sections 3 and 4.
- Clean up Section 2 so it contains background only, without thesis results.

## Items

### SC-001 - Add 3GPP UxNB terminology
- Page: 16
- Refers to: "UAVs may act as aerial base stations, relays, or temporary coverage nodes."
- Supervisor note, reduced: 3GPP calls aerial base stations `UxNB`; mention this name and cite the 3GPP document where it is introduced.
- Fix: Add a short parenthetical definition near the first UAV/aerial base station mention.

### SC-002 - Check reference numbering convention
- Page: 16
- Refers to: First introduction paragraph, especially citations `[50, 51]`.
- Supervisor note, reduced: References usually follow order of appearance; check whether the template intentionally uses another convention.
- Fix: Verify bibliography style/order and rebuild references if needed.

### SC-003 - Clarify whether the LoS/NLoS mask is an input
- Page: 16
- Refers to: "a geometrically derived LoS/NLoS mask"
- Supervisor note, reduced: Make clear whether this mask is part of the final framework input.
- Fix: State explicitly whether the final model receives the LoS/NLoS mask or whether it is only used for analysis/masking.

### SC-004 - Fix path loss vs channel attenuation terminology
- Page: 16
- Refers to: "The outputs studied through the project are path loss, delay spread, and angular spread."
- Supervisor note, reduced: Be precise: the channel includes path loss, shadowing, and fading. "Channel attenuation" may be more correct in some places, while "two-ray" is specifically a path-loss model.
- Fix: Review the thesis globally and distinguish `path loss`, `channel attenuation`, `path gain`, `received power`, `delay spread`, and `angular spread`.

### SC-005 - Choose a clearer framework name
- Page: 16
- Refers to: "learned surrogate"
- Supervisor note, reduced: The current naming is boring and not very self-explanatory; consider a catchy framework name used consistently.
- Fix: Pick one readable name for the final system and use it early, with a short explanation.

### SC-006 - Define city-holdout early
- Page: 17
- Refers to: "strict city-holdout protocol"
- Supervisor note, reduced: Explain what city-holdout means.
- Fix: Add a simple definition: entire cities are held out from training and used only for validation/test.

### SC-007 - Avoid unexplained "prior-anchored residual model" in the intro
- Page: 17
- Refers to: "selected prior-anchored residual model"
- Supervisor note, reduced: Use the chosen framework name here; this technical phrase is not meaningful before the method is explained.
- Fix: Replace with the framework name plus a plain-language phrase.

### SC-008 - Specify "all three dense targets"
- Page: 17
- Refers to: "all three dense targets"
- Supervisor note, reduced: Be specific. Say whether this means channel/path-loss and spreads.
- Fix: Replace with "path loss, delay spread, and angular spread" or the corrected terminology chosen in SC-004.

### SC-009 - Simplify the research-question teaser
- Page: 17
- Refers to: Paragraph beginning "In the final version of the project these questions can be answered directly..."
- Supervisor note, reduced: The answers can stay in the introduction, but they must use very simple words because the reader has not learned the terminology yet. Save the technical answers for the conclusion.
- Fix: Rewrite the intro answers as a short non-expert teaser; keep the full technical answer in Chapter 6.

### SC-010 - Clarify "ground-only masking"
- Page: 17
- Refers to: "with ground-only masking"
- Supervisor note, reduced: The term is unclear.
- Fix: Explain that metrics/losses are computed only for valid ground receiver pixels, not building pixels.

### SC-011 - Clarify "city-holdout splits"
- Page: 17
- Refers to: "city-holdout splits"
- Supervisor note, reduced: The term is unclear here too.
- Fix: Either define once and reuse, or replace with "training, validation, and test sets contain different cities."

### SC-012 - Clarify "FR3 UAV dataset"
- Page: 17
- Refers to: "the FR3 UAV dataset"
- Supervisor note, reduced: A question mark was placed near this phrase.
- Fix: Explain FR3 briefly, or avoid the acronym if it is not essential in the contribution list.

### SC-013 - Expand or remove OLS jargon
- Page: 17
- Refers to: "OLS"
- Supervisor note, reduced: Standalone highlight; likely asks for clarification.
- Fix: Expand as "ordinary least squares (OLS)" at first use, or replace with simpler wording.

### SC-014 - Replace "head" with simpler wording
- Page: 17
- Refers to: "regime-wise OLS NLoS head" and "GMM-head model"
- Supervisor note, reduced: "Head" may be too technical; use "based" or another simpler term.
- Fix: Rephrase unless the architecture term is necessary and already explained.

### SC-015 - Explain "distribution-first diagnosis"
- Page: 17
- Refers to: "distribution-first diagnosis"
- Supervisor note, reduced: This point is hard to understand even for an expert; reformulate for a non-expert.
- Fix: Replace with a plain sentence about discovering that previous models averaged away hard NLoS cases, motivating mixture-based predictions.

### SC-016 - Add chapter numbers to thesis outline
- Page: 18
- Refers to: Section 1.3, thesis outline.
- Supervisor note, reduced: Include chapter numbers.
- Fix: Rewrite outline as "Chapter 2...", "Chapter 3...", etc.

### SC-017 - Remove "canonical" from dataset wording
- Page: 18
- Refers to: "The canonical dataset contains..."
- Supervisor note, reduced: Strikeout on "canonical".
- Fix: Use "The dataset contains..." or "The CKM dataset contains..."

### SC-018 - Rephrase ground-pixel metric around ground users
- Page: 18
- Refers to: "All losses and metrics are computed only on ground pixels."
- Supervisor note, reduced: Consider wording like "we consider ground users served by the UAV."
- Fix: Reframe masking as the physical user scenario: ground receivers/users are served by the UAV.

### SC-019 - Replace chronological work plan with final-model explanation
- Page: 19
- Refers to: Section 1.6, work plan.
- Supervisor note, reduced: Chronological order may not be best; explain how the final model works.
- Fix: Make the work-plan section structure-first, not history-first.

### SC-020 - Reduce overuse of hyphenated expressions
- Page: 21
- Refers to: "fair-comparison"
- Supervisor note, reduced: Hyphens are overused; many are unnecessary.
- Fix: Search for repeated compound modifiers and simplify where natural.

### SC-021 - Use "channel gain" only
- Page: 21
- Refers to: "path loss, channel gain"
- Supervisor note, reduced: "Channel gain" is enough in this list.
- Fix: Remove redundant/ambiguous pairing if the list is about CKM quantities.

### SC-022 - Keep SOTA chapter separate from thesis results
- Page: 21
- Refers to: Chapter 2, "State of the Art and Technical Background."
- Supervisor note, reduced: This chapter should describe limitations of current models and provide background on tools used; it should not contain final results of this thesis.
- Fix: Move thesis result claims from Chapter 2 to Results/Conclusion; leave only literature background and limitations.

### SC-023 - Expand or define the two-ray equation
- Page: 22
- Refers to: `E_total = E_direct + Gamma E_reflected e^{j Delta phi}`.
- Supervisor note, reduced: The equation is too abstract. Provide a full expression with heights, or define `E_direct` and `E_reflected`.
- Fix: Add definitions for direct/reflected path lengths, fields, reflection coefficient, and phase difference, or simplify the equation.

### SC-024 - Make the two-ray explanation visual or simpler
- Page: 22
- Refers to: "the deterministic radial structure explains most LoS variance without any neural network."
- Supervisor note, reduced: This is not clear for readers who do not know the two-ray model; add an illustrative figure or remove/simplify.
- Fix: Add a small diagram of direct and reflected paths, or reduce the discussion to the intuition needed for the thesis.

### SC-025 - Replace vague "morphology" wording
- Page: 22
- Refers to: "morphology types"
- Supervisor note, reduced: "Morphology" is vague; use "city/environment types" such as rural or urban.
- Fix: Use concrete wording, then define morphology only if needed.

### SC-026 - Use simpler wording than "polynomials"
- Page: 22
- Refers to: "path-loss polynomials"
- Supervisor note, reduced: "Polynomials" sounds oversmart; "expressions" is enough.
- Fix: Replace with "path-loss expressions" unless the mathematical polynomial nature matters.

### SC-027 - Add formulas for delay and angular spread
- Page: 23
- Refers to: "The root-mean-square delay spread... The azimuth angular spread..."
- Supervisor note, reduced: Add formulas to calculate these quantities.
- Fix: Include compact formulas for RMS delay spread and angular spread, with variables defined.

### SC-028 - Reuse benchmark numbers in Results
- Page: 23
- Refers to: RadioUNet/RadioGUNet error numbers.
- Supervisor note, reduced: These numbers are useful and should appear again in the Results section for comparison.
- Fix: Add a comparison paragraph or table in Chapter 4 using the same caveats.

### SC-029 - Add consistent "Limitations" paragraphs in SOTA
- Page: 23
- Refers to: "These papers are useful path-loss scale references..."
- Supervisor note, reduced: In this and similar subsections, add a `\textbf{Limitations:}` paragraph; highlight SOTA limitations consistently.
- Fix: Standardize subsections 2.3 onward so each has a short limitations paragraph.

### SC-030 - Refer to Table 2.1 explicitly
- Page: 24
- Refers to: "After this correction, the true physical errors are:"
- Supervisor note, reduced: Write that the errors are provided in Table 2.1.
- Fix: Replace the dangling colon with "The corrected errors are provided in Table 2.1."

### SC-031 - Review the long CKM comparability paragraph
- Page: 24
- Refers to: Paragraph beginning "These numbers are not directly comparable to the CKM evaluation..."
- Supervisor note, reduced: Standalone highlight.
- Fix: Check whether this belongs in SOTA, a limitations paragraph, or Results; shorten if it repeats later.

### SC-032 - Move PMNet transfer-test results out of background
- Page: 24
- Refers to: Paragraph beginning "A separate transfer test performed in this thesis..."
- Supervisor note, reduced: Standalone highlight, also related to SC-022.
- Fix: Move thesis-specific PMNet transfer-test numbers to Results or an appendix; in SOTA keep only the comparison caveat.

### SC-033 - Review transformer/global-context claim
- Page: 25
- Refers to: "They are attractive when global context is necessary..."
- Supervisor note, reduced: Standalone highlight.
- Fix: Decide whether to keep, shorten, or move this as part of the SOTA cleanup.

### SC-034 - Review foundation-model horizon claim
- Page: 25
- Refers to: "These foundation approaches represent the long-term direction..."
- Supervisor note, reduced: Standalone highlight.
- Fix: Keep only if it clearly supports the thesis positioning; otherwise shorten.

### SC-035 - Explain why training stabilisation is needed
- Page: 29
- Refers to: Section 2.7, "Training stabilisation and regularisation techniques."
- Supervisor note, reduced: Add a paragraph explaining why these techniques are needed.
- Fix: Add a short motivation before SWA/regularisation details.

### SC-036 - Fix target quantity terminology and units
- Page: 29
- Refers to: "Target quantity: path loss (dB), path gain (dBm), received power..."
- Supervisor note, reduced: Received power is likely in dBm; path loss and gain are related quantities and should not be mixed loosely.
- Fix: Correct the units and clarify sign conventions for path loss, path gain, and received power.

### SC-037 - Move final-model values out of the SOTA table
- Page: 33
- Refers to: Literature comparison table row for "Final model (this thesis)".
- Supervisor note, reduced: This belongs in Results; do not mix thesis values with background literature.
- Fix: Remove final-model row from Chapter 2 or replace with a forward reference to Chapter 4.

### SC-038 - Shorten "Dataset protocol" heading
- Page: 34
- Refers to: "Dataset protocol"
- Supervisor note, reduced: Strikeout on "protocol."
- Fix: Rename heading to "Dataset", "Dataset and split", or similar.

### SC-039 - Add height-distribution figure
- Page: 34
- Refers to: Paragraph about transmitter-height samples and beta-mixture variants.
- Supervisor note, reduced: A PDF/histogram figure of heights would be useful here.
- Fix: Insert the UAV-height distribution plot or create one from the HDF5 heights.

### SC-040 - Rewrite methodology to present what worked
- Page: 36
- Refers to: Section 3.2, "Diagnostic baselines retained from development."
- Supervisor note, reduced: Readers want the final method, not the development struggle. Chronology is not a good thesis structure; rewrite so the final model can be understood without reading failed attempts.
- Fix: Put final method first; move the experiment chronology and negative results to an appendix or short diagnostic subsection.

### SC-041 - Remove "free-space-like" wording
- Page: 59
- Refers to: "a free-space-like offset"
- Supervisor note, reduced: Highlight/strikeout on "like."
- Fix: Replace with "free-space offset" or a clearer parameter description.

### SC-042 - Remove "not cosmetic" sentence
- Page: 69
- Refers to: "The addition of 1 is not cosmetic."
- Supervisor note, reduced: Strikeout.
- Fix: Delete or replace with a neutral technical explanation if still needed.

### SC-043 - Results chapter should focus on final results and comparisons
- Page: 86
- Refers to: Chapter 4, "Results."
- Supervisor note, reduced: Same issue as Section 3: present only final results and compare them with previous papers.
- Fix: Trim development-history material from Results; emphasize final model, baselines, and literature comparison.

### SC-044 - Reframe economic/social impact
- Page: 104
- Refers to: Section 5.3, "Economic and social impact."
- Supervisor note, reduced: The expected focus is the potential economic impact of the final model.
- Fix: Discuss deployment value, reduced simulation cost, faster planning, and possible operator/network-planning benefits.

### SC-045 - Positive note
- Page: 107
- Refers to: Chapter 6 answer section around the distribution-first explanation.
- Supervisor note, reduced: "thanks."
- Fix: No fix required; keep as positive acknowledgement unless nearby text changes during restructuring.

### SC-046 - Move struggles to an annex
- Page: 108
- Refers to: Section 6.1.5, "Negative results."
- Supervisor note, reduced: Mention an annex with the struggles; do not keep them in the main text.
- Fix: Move long negative-results history to an appendix/annex and keep only the lessons needed for the final method.
