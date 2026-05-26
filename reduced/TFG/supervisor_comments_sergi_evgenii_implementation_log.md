# Implementation Log for Sergi and Evgenii Comments

Date: 26/05/2026

Scope: reduced thesis source under `reduced/TFG`.

## 1. New Comment Tracking Files

Created:

1. `supervisor_comments_sergi_pending.md`
2. `supervisor_comments_sergi_evgenii_exact_implementation_plan.md`
3. `supervisor_comments_sergi_evgenii_implementation_log.md`

## 2. Front Matter

Updated `revision_history_en.tex` so the late review sequence is explicit:

1. EV first correction of the final text on 18/05/2026.
2. SA second correction of the final text on 26/05/2026.
3. GMG corrected version after supervisor feedback on 29/05/2026.

## 3. Introduction

Updated `introduction.tex`:

1. Removed the old `Methods and procedures` section from Chapter 1.
2. Reworked the chapter outline so Chapter 3 is introduced as the final reproducible pipeline.
3. Moved the development history framing to Appendix A instead of presenting it as main methodology.
4. Mentioned the generative AI appendix in the thesis outline.

## 4. Chapter 2

Updated `state_of_art.tex`:

1. Added a reader map explaining the role of the background chapter.
2. Reduced result like claims in the two ray and SOA sections.
3. Clarified that papers may report received power or path loss depending on convention.
4. Converted RMTransformer normalised errors to scientific notation for readability.
5. Renamed the training section to include distribution aware methods and fair comparison.

## 5. Chapter 3

Updated `methodology.tex`:

1. Rewrote the opening to explain the final pipeline first.
2. Added a high level methodology block diagram with the flow:
   height map and UAV height, CKM support maps, frozen priors, HARP-Net CKM, final outputs, evaluation.
3. Removed the hidden legacy methodology block that repeated older attempts.
4. Renamed the path loss prior section to `Channel Attenuation Prior and Residual Prediction`.
5. Added a reader map before the attenuation prior explaining the dataset name `path_loss` versus the thesis term channel attenuation.
6. Kept detailed mathematical derivations in the prior detail files.

Updated `prior_detail_try78.tex` and `prior_detail_try79.tex`:

1. Replaced remaining prose equation references with `\eqref`.
2. Removed manual `Eq.` wording from two flowchart labels so the PDF no longer contains plain `Eq. 3.x` references.

## 6. Chapter 4

Updated `results.tex`:

1. Rewrote the opening of the channel attenuation results so it reports outcomes instead of repeating methodology.
2. Added one representative HARP-Net CKM qualitative panel to Results.
3. Kept the larger qualitative gallery in Appendix B.
4. Removed hidden development history from the active results source.
5. Changed remaining final model naming to HARP-Net CKM.

## 7. Sustainability

Updated `sustainability_balanced.tex`:

1. Added a more concrete economic impact paragraph.
2. Explained value for planning, licensing or service transfer, operators, and integration know how.
3. Avoided claiming patentability without a novelty analysis.

## 8. Appendices

Updated `appendices_compact.tex`:

1. Added Appendix E, `Declaration on Generative AI Use`.
2. Clarified that CKMGenerator is delivered with the HARP-Net CKM pipeline.

## 8A. Spread Evaluation Clarification

Updated `supervisor_comments_sergi_evgenii_exact_implementation_plan.md`,
`methodology.tex`, `results.tex`, and `paper_version/paper.tex` after
Sergi's follow-up email:

1. Added the clarification as a plan item and as Task 10A.
2. Stated in Methodology that channel attenuation, delay spread and angular
   spread share the same pixel-weighted valid-ground receiver RMSE contract.
3. Stated in Results that delay spread and angular spread are prediction versus
   ray-traced ground truth at every valid ground receiver pixel, accumulated
   over all valid ground receivers.
4. Added the same compact clarification to the paper version's evaluation
   contract.

## 9. Summary and Conclusions

Updated `summary.tex` and `conclusions.tex`:

1. Replaced the old phrase `final prior anchored residual GMM head model` with HARP-Net CKM.
2. Preserved the numerical claims already used in the thesis.

## 10. Bibliography Audit

Updated `TFG.bib` entries where a formal publication record was verified:

1. `icassp2023challenge`: ICASSP 2023 proceedings, DOI `10.1109/ICASSP49357.2023.10433928`.
2. `dataset2212`: IEEE DataPort dataset, DOI `10.21227/0GTX-6V30`.
3. `ckmimagenet2025`: IEEE Transactions on Communications, DOI `10.1109/TCOMM.2025.3615778`.
4. `icassp2025indoor`: ICASSP 2025 proceedings, DOI `10.1109/ICASSP49660.2025.10889381`.
5. `tarhouni2025`: IEEE Transactions on Vehicular Technology, DOI `10.1109/TVT.2025.3633604`.
6. `pathfinder2025`: Pattern Recognition, DOI `10.1016/j.patcog.2026.113725`.
7. `reveal2025`: IEEE DySPAN 2025, DOI `10.1109/DYSPAN64764.2025.11115911`.
8. `rmtransformer2025`: IEEE VTC2025 Spring, DOI `10.1109/VTC2025-Spring65109.2025.11174709`.
9. `gao2026`: IEEE Transactions on Vehicular Technology, DOI `10.1109/TVT.2026.3658966`.
10. `radiolam2025`: IEEE Journal on Selected Areas in Communications, DOI `10.1109/JSAC.2026.3677149`.
11. `radiopit2025`: APCC 2025, DOI `10.23919/APCC64555.2025.11279807`.
12. `cai2019`: IEEE Transactions on Vehicular Technology, DOI `10.1109/TVT.2018.2886961`.
13. `lee2024timevarying`: IEEE VTC2024 Fall, DOI `10.1109/VTC2024-Fall63153.2024.10757531`.

Remaining arXiv only entries after the audit:

1. `saboor2025height`
2. `jaensch2024directiverme`
3. `radiogunet2025`
4. `airmap2025`
5. `wicopg2025`
6. `fmrme2026`

These were left as preprints because I did not verify a formal publication record.

## 11. Verification

Build commands run from `reduced/TFG`:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error TFG.tex
biber TFG
pdflatex -interaction=nonstopmode -halt-on-error TFG.tex
pdflatex -interaction=nonstopmode -halt-on-error TFG.tex
```

`latexmk` could not be used because MiKTeX could not find Perl.

Final PDF status:

1. `TFG.pdf` builds successfully.
2. No undefined references or undefined citations remain in `TFG.log`.
3. PDF text audit found no remaining `Methods and procedures`, old GMM head phrase, old RMTransformer decimals, or plain `Eq. 3.x` references.
4. Appendix E appears in the PDF.

## 12. Plan Execution Audit

Checked the exact implementation plan after the follow-up clarification:

1. Task 1 completed: Appendix E exists and appears in the PDF. The declaration
   remains generic because no official list of specific AI tools was confirmed.
2. Task 2 completed: the `Methods and procedures` section no longer exists in
   the active introduction or PDF table of contents.
3. Task 3 completed: Chapter 3 opens with the final method and evaluation
   contract rather than old attempts.
4. Task 4 completed: the high level methodology diagram is present.
5. Task 5 completed: the hidden chronology block was removed from
   `methodology.tex`.
6. Task 6 completed: the old path loss prior heading is now framed as channel
   attenuation while preserving physical path loss terminology where it belongs.
7. Task 7 completed: visible prose equation references use parenthesised
   references; flowchart labels no longer produce plain `Eq. 3.x` text in the
   PDF.
8. Task 8 completed: Chapter 2 has a reader map and clearer structure.
9. Task 9 completed: two ray wording, RMTransformer precision and received
   power/path loss wording were corrected.
10. Task 10 completed: Chapter 4 is result focused and hidden development
    history was removed.
11. Task 10A completed: spread evaluation is explicitly described as prediction
    versus dense ground truth over all valid ground receivers.
12. Task 11 completed: one representative final model panel is included in
    Results.
13. Task 12 completed: sustainability economic impact was expanded.
14. Task 13 completed: bibliography entries were audited and updated where a
    formal publication record was verified.
15. Task 14 completed: final-output terminology was changed toward channel
    attenuation while preserving physical path loss where appropriate.
16. Task 15 completed: acronym-heavy framing was reduced in the introduction
    and first-method explanations.
17. Task 16 completed: visible excessive precision and unnecessary prose
    hyphens found during the pass were cleaned, while code identifiers and
    established technical terms were left intact.
18. Task 17 completed: the paper version now keeps the final HARP-Net CKM
    naming in the final-model labels and includes the compact spread evaluation
    clarification without adding the thesis appendix material.
19. Task 18 completed: the reduced thesis was rebuilt manually and checked with
    PDF text extraction.
