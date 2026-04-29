# Try Mention Inventory and Edit Plan

> **Goal:** list every current thesis-source line that names a numbered Try, then decide how each cluster should be kept, shortened, moved, or rewritten.
>
> **Scope:** `.tex` sources in `C:\TFG\FINAL_THESIS\TFG`; LaTeX build artifacts such as `.aux`, `.log`, `.toc`, and the compiled PDF are excluded. The first scan covered top-level `.tex` sources; the Gantt include file `img/gantt_diagrama.tex` was checked separately below because it is pulled into `introduction.tex`.
>
> **Snapshot:** generated 2026-04-29 before any thesis edits from this inventory.

## Executive Rules

- Keep Try numbers in the main text only when they carry a scientific role: milestone, method, final baseline, or final model.
- Move operational detail, long attempt history, script names, and implementation snippets to the appendix or remove them from the main narrative.
- Rephrase the Gantt diagram too: its bars should describe phases, not raw internal attempt numbers, because the figure appears in the Introduction and should read as a public project plan.
- Keep the final public story simple: old direct-regression attempts -> distribution-first diagnosis in Try 76/77 -> calibrated priors in Try 78/79 -> Try 80 residual refinement.
- Standardize wording: `Try 78` is the path-loss prior, `Try 79` is the spread-prior calibration, and `Try 80` is the joint prior-anchored residual model.
- Do not mix taxonomy counts: Try 78 uses 18 path-loss calibration regimes in the final artifacts; Try 79 uses 36 exact regimes per metric, 72 exact total, and 114 keys including fallbacks.
- Prefer `linear-model-calibrated prior` or `data-calibrated linear prior` over `ML-calibrated` unless the text explicitly defines ML as machine learning and not maximum likelihood.

## High-Level Handling By Attempt Family

| Attempt family | Current role | How I will deal with it |
| --- | --- | --- |
| Tries 1--22 | Early U-Net/cGAN, decoder, height, multiscale, and clean pre-prior baseline. | Keep as compressed chronology only. Main text should mention the lesson, not the full implementation path. Appendix can keep the audit trail. |
| Try 33 / Tries 33--40 | Ground-only masking becomes mandatory. | Keep as an evaluation-contract turning point. Do not expand architecture details. |
| Tries 41--50 | Prior-plus-residual and PMNet-style attempts. | Keep representative numbers only where they explain why stronger priors/distribution modelling were needed. Move detailed negative evidence to appendix. |
| Tries 66--75 | PMHHNet, training-stabilization, heteroscedastic and histogram diagnosis. | Keep the diagnostic lesson: LoS became reasonable, NLoS mode collapse/tails remained. Avoid listing every run in the main body. |
| Try 76 | Distribution-first GMM path-loss reference. | Keep as a major predecessor. It explains that NLoS can be solved by modelling the target distribution, not only by adding physics. |
| Try 77 | Distribution-first spread reference. | Keep as a spread-specific predecessor and diagnostic; results can compare it to Try 79, but methodology should stay compact. |
| Try 78 | Final non-DL path-loss prior. | Keep and polish. It is core methodology/results material. Fix any taxonomy ambiguity: final calibration has 18 regimes. Remove repo-style artifacts from main text. |
| Try 79 | Final non-DL spread priors. | Keep and polish. State 36 exact keys per metric, 72 exact total, 114 with fallbacks. Keep result tables in Results, derivation in Methodology. |
| Try 80 | Final joint prior-anchored residual model with a GMM head. | Keep as the final claim. Methodology should explain Big -> Big relaxed residuals -> Huge -> Huge path-loss fine-tune; Results should carry final metrics, GMM-head interpretation, and deltas; appendix can carry panels/config. |

## File-Level Handling

| File | Try lines | Try-style occurrences | Handling |
| --- | ---: | ---: | --- |
| `appendices.tex` | 86 | 101 | Keep as audit trail, but remove/soften repo-path wording if it reads like source-control notes rather than reproducibility. |
| `img/gantt_diagrama.tex` | 12 | 12 | Rephrase all raw `Attempts ...` / `Try ...` bars into phase names. This figure is in the Introduction, so it should not expose the internal numbering system unless the caption explains that numbering is historical. |
| `conclusions.tex` | 17 | 20 | Keep only final thesis lessons, negative results, and future work. Avoid re-running the full chronology. |
| `introduction.tex` | 16 | 18 | Keep high-level contributions and outline. Avoid adding old Try details here. |
| `methodology.tex` | 80 | 102 | Primary reduction target. Keep one chronology table, final training progression, and prior derivations; remove duplicate old-try narration if Results/Appendix already cover it. |
| `prior_detail_overview.tex` | 25 | 29 | Keep as bridge into Try 78/79/80. Make wording conceptual and not repository-specific. |
| `prior_detail_try78.tex` | 20 | 20 | Keep derivation. Correct/clarify 18-regime Try 78 taxonomy and use linear-model-calibrated wording. |
| `prior_detail_try79.tex` | 16 | 16 | Keep derivation. Preserve 36-per-metric / 72-exact / 114-with-fallbacks explanation. |
| `prior_detail_try80.tex` | 38 | 41 | Keep final architecture/loss. Avoid checkpoint-name overload unless needed for reproducibility. |
| `results.tex` | 209 | 238 | Keep most Try mentions because this is where comparisons belong. Reduce only duplicate narrative or source-file references. |
| `state_of_art.tex` | 63 | 67 | Keep Try mentions only when positioning thesis ideas against literature. Internal old-run names should be minimized here. |
| `summary.tex` | 15 | 15 | Keep final Try 78/79/80 story in Catalan, Spanish, and English. No old tries. |
| `sustainability.tex` | 7 | 9 | Keep compute-cost mentions only. Avoid methodological detail. |

## Gantt Rephrase Plan

The Gantt is inserted from `img/gantt_diagrama.tex` into `introduction.tex` lines 175--180. The surrounding paragraph already says the figure is grouped by major phases rather than all individual attempts, so the bar labels should match that promise.

| Current Gantt label | Proposed label |
| --- | --- |
| `Attempts 23--32: Spread-branch & first priors` | `Spread-target branch and first prior tests` |
| `Attempts 33--40: Building-mask exclusion` | `Ground-mask evaluation protocol` |
| `Attempts 41--50: Physical prior & PMNet backbone` | `Physical-prior residual baselines` |
| `Try 78--79: Frozen non-DL priors` | `Frozen calibrated path-loss and spread priors` |
| `Attempts 1--8: U-Net and pix2pix cGAN` | `Initial U-Net and cGAN baseline` |
| `Attempts 9--14: Height & LoS/NLoS splits` | `Height conditioning and visibility-aware splits` |
| `Attempts 15--19: GroupNorm & distance-map` | `Stabilized CNN inputs and distance features` |
| `Attempts 20--22: Bilinear decoder & multiscale` | `Artifact reduction and multiscale supervision` |
| `Attempts 51--66: PMHHNet consolidation` | `PMHHNet and topology-expert consolidation` |
| `Attempts 67--75: Anti-overfitting & multi-expert` | `Regularization and multi-expert diagnostics` |
| `Attempts 76--77: Distribution-first GMM` | `Distribution-first GMM modelling` |
| `Try 80: Joint prior-anchored residual model` | `Joint prior-anchored residual GMM model` |

Handling: rephrase the Gantt labels when editing the thesis, but leave the chronological mapping in this inventory and in the detailed appendix. If a reader wants the internal numbering, it should be discoverable in Results/Appendix, not front-loaded in the project-plan figure.

## Compact Per-Try Locations And Handling

### Try 1

Locations:
- `results.tex`: 26

Handling: Compress as early baseline/history. Keep in the chronology table and appendix; avoid detailed main-body explanation except for Try 22 as the clean pre-prior baseline.

### Try 9

Locations:
- `appendices.tex`: 26

Handling: Compress as early baseline/history. Keep in the chronology table and appendix; avoid detailed main-body explanation except for Try 22 as the clean pre-prior baseline.

### Try 14

Locations:
- `appendices.tex`: 26

Handling: Compress as early baseline/history. Keep in the chronology table and appendix; avoid detailed main-body explanation except for Try 22 as the clean pre-prior baseline.

### Try 15

Locations:
- `appendices.tex`: 34

Handling: Compress as early baseline/history. Keep in the chronology table and appendix; avoid detailed main-body explanation except for Try 22 as the clean pre-prior baseline.

### Try 20

Locations:
- `appendices.tex`: 37
- `results.tex`: 107

Handling: Compress as early baseline/history. Keep in the chronology table and appendix; avoid detailed main-body explanation except for Try 22 as the clean pre-prior baseline.

### Try 21

Locations:
- `appendices.tex`: 38
- `results.tex`: 108

Handling: Compress as early baseline/history. Keep in the chronology table and appendix; avoid detailed main-body explanation except for Try 22 as the clean pre-prior baseline.

### Try 22

Locations:
- `appendices.tex`: 34, 39
- `methodology.tex`: 86, 136
- `results.tex`: 26, 109

Handling: Compress as early baseline/history. Keep in the chronology table and appendix; avoid detailed main-body explanation except for Try 22 as the clean pre-prior baseline.

### Try 33

Locations:
- `methodology.tex`: 89
- `results.tex`: 27

Handling: Use only as the ground-mask/evaluation-contract turning point. No expansion needed.

### Try 40

Locations:
- `results.tex`: 27

Handling: Use only as the ground-mask/evaluation-contract turning point. No expansion needed.

### Try 41

Locations:
- `appendices.tex`: 51
- `results.tex`: 28, 110-111

Handling: Keep as mid-project prior/residual negative evidence. Results may keep representative numbers; methodology should summarize rather than list every variant.

### Try 42

Locations:
- `appendices.tex`: 62
- `results.tex`: 28, 112

Handling: Keep as mid-project prior/residual negative evidence. Results may keep representative numbers; methodology should summarize rather than list every variant.

### Try 44

Locations:
- `appendices.tex`: 70

Handling: Keep as mid-project prior/residual negative evidence. Results may keep representative numbers; methodology should summarize rather than list every variant.

### Try 48

Locations:
- `appendices.tex`: 76

Handling: Keep as mid-project prior/residual negative evidence. Results may keep representative numbers; methodology should summarize rather than list every variant.

### Try 49

Locations:
- `appendices.tex`: 63
- `methodology.tex`: 156
- `results.tex`: 113, 149

Handling: Keep as mid-project prior/residual negative evidence. Results may keep representative numbers; methodology should summarize rather than list every variant.

### Try 50

Locations:
- `appendices.tex`: 76, 79
- `methodology.tex`: 159
- `results.tex`: 28

Handling: Keep as mid-project prior/residual negative evidence. Results may keep representative numbers; methodology should summarize rather than list every variant.

### Try 66

Locations:
- `appendices.tex`: 84
- `introduction.tex`: 90
- `methodology.tex`: 163, 269
- `results.tex`: 29, 114-115, 154, 212, 260, 294
- `state_of_art.tex`: 610, 650-651, 860, 870

Handling: Use as PMHHNet/training-stabilization diagnostic. Keep lessons about NLoS collapse, uncertainty, and histogram diagnosis; move operational detail to appendix.

### Try 67

Locations:
- `methodology.tex`: 910, 932
- `state_of_art.tex`: 278, 292, 459

Handling: Use as PMHHNet/training-stabilization diagnostic. Keep lessons about NLoS collapse, uncertainty, and histogram diagnosis; move operational detail to appendix.

### Try 69

Locations:
- `results.tex`: 212, 260, 294
- `state_of_art.tex`: 292, 683

Handling: Use as PMHHNet/training-stabilization diagnostic. Keep lessons about NLoS collapse, uncertainty, and histogram diagnosis; move operational detail to appendix.

### Try 70

Locations:
- `state_of_art.tex`: 610

Handling: Use as PMHHNet/training-stabilization diagnostic. Keep lessons about NLoS collapse, uncertainty, and histogram diagnosis; move operational detail to appendix.

### Try 71

Locations:
- `conclusions.tex`: 143
- `methodology.tex`: 910, 932
- `state_of_art.tex`: 387, 459, 683, 870

Handling: Use as PMHHNet/training-stabilization diagnostic. Keep lessons about NLoS collapse, uncertainty, and histogram diagnosis; move operational detail to appendix.

### Try 74

Locations:
- `methodology.tex`: 637

Handling: Use as PMHHNet/training-stabilization diagnostic. Keep lessons about NLoS collapse, uncertainty, and histogram diagnosis; move operational detail to appendix.

### Try 75

Locations:
- `conclusions.tex`: 88
- `introduction.tex`: 90
- `methodology.tex`: 284, 548, 637
- `results.tex`: 363, 902

Handling: Use as PMHHNet/training-stabilization diagnostic. Keep lessons about NLoS collapse, uncertainty, and histogram diagnosis; move operational detail to appendix.

### Try 76

Locations:
- `appendices.tex`: 98
- `conclusions.tex`: 91
- `introduction.tex`: 91, 155
- `methodology.tex`: 12, 24, 29, 176, 290, 384, 388, 497-498, 536, 547-548, 601, 623, 756, 806, 892, 910, 932, 938
- `prior_detail_overview.tex`: 116
- `results.tex`: 30, 116, 126, 130, 136, 200, 202, 205, 219, 225, 232, 236-237, 257, 268, 276, 287, 294, 299, 301, 303, 318, 321, 328-329, 337, 342, 344, 353, 356, 358, 362, 374, 377, 382, 385, 392, 406, 562, 564, 573, 594, 597, 602, 611, 614, 616, 629, 632-633, 926, 928, 930, 967
- `state_of_art.tex`: 359, 368, 404
- `sustainability.tex`: 41, 104

Handling: Keep as a major predecessor: distribution-first GMM path loss, especially NLoS. Ensure comparisons say it is a diagnostic/reference, not the final path-loss pipeline.

### Try 77

Locations:
- `conclusions.tex`: 91
- `introduction.tex`: 156
- `methodology.tex`: 12, 24, 29, 178, 391, 490, 494, 510, 623, 654, 756, 806, 816, 893, 910, 938
- `prior_detail_overview.tex`: 116
- `results.tex`: 126, 130, 136, 374, 380, 382, 386, 392, 407, 414, 417-418, 438, 482-483, 491, 941, 943, 945, 956, 958, 960, 966
- `state_of_art.tex`: 139, 345, 368, 414
- `sustainability.tex`: 41

Handling: Keep as spread distribution-first predecessor. Use it to motivate Try 79/80, but avoid duplicating its architecture in several chapters.

### Try 78

Locations:
- `appendices.tex`: 107, 112, 190-191, 193, 216, 233, 374, 385, 455, 601
- `conclusions.tex`: 14, 25, 95, 191, 224
- `introduction.tex`: 78, 88, 104-105, 160
- `methodology.tex`: 18, 23, 183, 540, 555, 809, 912, 940, 949, 996, 1001-1002, 1006, 1015, 1018-1019, 1023
- `prior_detail_overview.tex`: 2, 52, 70, 98-99, 115, 155, 171, 177
- `prior_detail_try78.tex`: 6, 383, 783, 796, 862, 1253, 1309, 1311-1312, 1365-1366
- `prior_detail_try79.tex`: 113, 291
- `prior_detail_try80.tex`: 32, 92
- `results.tex`: 7, 31, 38, 43, 45, 48, 52, 54, 117, 134, 137, 161, 163, 213, 262, 356, 358, 372, 375, 397, 498-499, 505, 507, 554, 558, 560-561, 567-568, 572, 574-575, 611-612, 617, 627-628, 637, 642, 668, 737, 1168, 1180, 1187
- `state_of_art.tex`: 72, 120, 280, 303, 310, 363, 611, 653, 733, 791, 861
- `summary.tex`: 16, 39, 62
- `sustainability.tex`: 43, 57

Handling: Keep as final path-loss prior. Clarify 18 final calibration regimes; reserve six-class topology wording for Try 76/77 reporting and Try 79 spread calibration. Use linear-model-calibrated wording.

### Try 79

Locations:
- `appendices.tex`: 110, 112, 196-197, 216, 233, 375, 389, 391, 455, 601
- `conclusions.tex`: 16, 97, 191, 224
- `introduction.tex`: 82, 88, 104, 106, 162
- `methodology.tex`: 18, 23, 179, 183, 541, 557, 655, 809, 912, 940, 949, 996, 1025-1026, 1028
- `prior_detail_overview.tex`: 2, 53, 71, 115, 156, 183
- `prior_detail_try78.tex`: 1228
- `prior_detail_try79.tex`: 24, 39, 42, 145, 164, 192, 195, 243, 268, 320, 328, 393-394
- `prior_detail_try80.tex`: 32, 92
- `results.tex`: 6, 32, 118-119, 126, 175, 188-189, 263, 374-375, 398, 444, 449, 468-469, 477, 490, 499, 523, 525, 642, 668, 737, 754, 1168, 1180
- `state_of_art.tex`: 134, 307, 311, 329, 347, 363, 738, 792
- `summary.tex`: 18, 41, 63
- `sustainability.tex`: 57, 104

Handling: Keep as final spread prior. State 36 exact regimes per metric, 72 exact total, 114 keys with fallbacks. Avoid letting the 36 count leak into Try 78.

### Try 80

Locations:
- `appendices.tex`: 112, 124, 126, 130, 135-136, 199-201, 210, 213-214, 220, 234-235, 245, 252, 258, 260, 281, 286-287, 289, 295-296, 298, 304-305, 307, 313-314, 316, 322-323, 325, 331-332, 334, 340-341, 343, 349-350, 352, 358-359, 361, 368, 374, 396, 452, 455, 480, 493, 526, 601, 616, 668, 802, 848
- `conclusions.tex`: 18, 28, 38, 61, 99, 196, 208
- `introduction.tex`: 86, 101, 104, 106, 108, 163
- `methodology.tex`: 4, 12, 29, 96, 184-185, 275, 541, 557, 807, 822-823, 847, 853-854, 884, 893, 910, 938, 944-945, 947, 957, 1015, 1030-1031, 1033
- `prior_detail_overview.tex`: 3, 6, 14, 33, 42, 48, 55, 87, 108, 144, 156, 190
- `prior_detail_try78.tex`: 380, 384, 609, 784, 1114, 1132, 1178, 1316
- `prior_detail_try79.tex`: 292
- `prior_detail_try80.tex`: 3, 24, 31, 38, 61, 76, 86, 113, 126, 135, 152, 173, 179, 183, 311-312, 338, 392-393, 458-459, 463, 497, 501, 526, 536, 538, 558, 573, 593, 595-596, 614, 631, 658, 663
- `results.tex`: 5, 8, 33, 76, 87, 120, 131, 136, 374, 399, 406, 450, 553, 640, 642, 645, 655, 667-669, 684, 686, 714, 718, 722, 736, 739, 774, 777, 793, 796, 816, 819, 838, 841-842, 854-855, 869, 878, 887, 891, 895, 926, 928, 930, 941, 943, 945, 956, 958, 960, 965, 972, 1012, 1015, 1026, 1056, 1058, 1063, 1102, 1104, 1158-1159, 1162, 1165, 1168, 1170, 1177-1178, 1180, 1183-1184, 1217, 1263
- `state_of_art.tex`: 6, 9, 205-206, 280, 309, 346, 362, 369, 441, 530, 566, 570, 590, 612, 631, 653, 743, 759, 764, 768, 770, 778, 784, 807, 809, 822, 839, 845, 862, 867
- `summary.tex`: 19-20, 25, 42-43, 48, 64-65, 70
- `sustainability.tex`: 39, 57, 103, 158

Handling: Keep as final model. Methodology should explain the staged training path and the residual GMM head; Results should carry the final test metrics and deltas; appendix can carry config/panels/snippets.

## Detailed Source Line Index

Every line below matched the Try detector. This is intentionally long so later edits can be checked without re-running the scan.

### `appendices.tex`

- `appendices.tex:26` [Try 9, Try 14] Tries 9--14 introduced height conditioning and LoS/NLoS-aware evaluation.
- `appendices.tex:34` [Try 15, Try 22] Tries 15--22 attacked three visible problems: checkerboard artifacts, loss of
- `appendices.tex:37` [Try 20] channel exposed the most important geometric variable directly. Try 20 isolated
- `appendices.tex:38` [Try 21] the bilinear decoder change, Try 21 isolated multiscale supervision, and Try
- `appendices.tex:39` [Try 22] 22 combined both. In the early contract, Try 22 was the strongest clean
- `appendices.tex:51` [Try 41] Try 41 made the residual formulation explicit:
- `appendices.tex:62` [Try 42] Try 42 moved away from the old U-Net/cGAN family toward a PMNet-style residual
- `appendices.tex:63` [Try 49] regressor. Try 49 added prior-confidence logic and robust loss weighting; its
- `appendices.tex:70` [Try 44] Try 44, a no-prior PMNet-v3-style control, learned the LoS part to roughly
- `appendices.tex:76` [Try 48, Try 50] Try 48 and Try 50 were useful negative evidence. Several richer NLoS priors
- `appendices.tex:79` [Try 50] best Try 50 NLoS sandbox still remained near \SI{41}{dB}. The conclusion was
- `appendices.tex:84` [Try 66] Try 66 consolidated the PMHHNet family: physical channels, GroupNorm, height
- `appendices.tex:98` [Try 76] Try 76 reframed NLoS as a distributional problem. Instead of predicting a
- `appendices.tex:107` [Try 78] Try 78 then showed that LoS path loss was even more deterministic than the
- `appendices.tex:110` [Try 79] reflection parameters. Try 79 applied a related philosophy to delay and
- `appendices.tex:112` [Try 78, Try 79, Try 80] local morphology features. Try 80 is the synthesis: frozen Try 78/79 priors
- `appendices.tex:124` [Try 80] \chapter{Try 80 Configuration Summary}
- `appendices.tex:126` [Try 80] The active Try 80 configuration uses the canonical dataset
- `appendices.tex:130` [Try 80] \texttt{try80\_precomputed\_priors.h5}, but the priors are deterministic and
- `appendices.tex:135` [Try 80] \caption{Main Try 80 configuration values.}
- `appendices.tex:136` [Try 80] \label{tab:try80_config_appendix}
- `appendices.tex:190` [Try 78] Try 78 LoS path-loss prior &
- `appendices.tex:191` [Try 78] Section~\ref{sec:try78_detail}, especially Eqs.~\ref{eq:fspl},
- `appendices.tex:193` [Try 78] Try 78 NLoS calibration &
- `appendices.tex:196` [Try 79] Try 79 spread priors &
- `appendices.tex:197` [Try 79] Section~\ref{sec:try79_detail}, especially Eqs.~\ref{eq:raw_spread},
- `appendices.tex:199` [Try 80] Try 80 prior-anchored GMM &
- `appendices.tex:200` [Try 80] Section~\ref{sec:try80_detail}, especially Eqs.~\ref{eq:try80_mu},
- `appendices.tex:201` [Try 80] \ref{eq:try80_point}, and \ref{eq:try80_loss}. \\
- `appendices.tex:210` [Try 80] \chapter{Representative Try 80 Inspection Panels}
- `appendices.tex:213` [Try 80] \texttt{TFGpractice/TFGEightiethTry80/scripts/}\newline
- `appendices.tex:214` [Try 80] \texttt{generate\_try80\_appendix\_panels.py}. It uses the validation split,
- `appendices.tex:216` [Try 78, Try 79] the frozen Try 78/79 priors. The script selects one validation
- `appendices.tex:220` [Try 80] Try 80 beats the frozen prior on all three outputs, then chooses the
- `appendices.tex:233` [Try 78, Try 79] \item \textbf{Frozen prior (Try 78/79)} --- the calibrated analytic prior
- `appendices.tex:234` [Try 80] that Try 80 receives as an input channel and anchors to.
- `appendices.tex:235` [Try 80] \item \textbf{Try 80 prediction} --- the final residual-over-prior output
- `appendices.tex:245` [Try 80] \(\mathrm{Try\,80}-\mathrm{Prior}\) that the neural head applies on
- `appendices.tex:252` [Try 80] claim is that Try 80 is a prior-anchored residual corrector, and the visible
- `appendices.tex:258` [Try 80] \caption{Try 80 appendix panels generated from validation samples with the
- `appendices.tex:260` [Try 80] \label{tab:try80_appendix_panels}
- `appendices.tex:281` [Try 80] \texttt{img/thesis\_figures/try80\_appendix\_panels/manifest.json}.
- `appendices.tex:286` [Try 80] \includegraphics[width=\textwidth,height=0.88\textheight,keepaspectratio]{img/thesis_figures/try80_appendix_panels/try80_panel_open_low_ant_Segovia_sample_13213_6x3.png}
- `appendices.tex:287` [Try 80] \caption{Try 80 \(6\times3\) inspection panel for an open, low-antenna
- `appendices.tex:289` [Try 80] \label{fig:appendix_try80_open_low}
- `appendices.tex:295` [Try 80] \includegraphics[width=\textwidth,height=0.88\textheight,keepaspectratio]{img/thesis_figures/try80_appendix_panels/try80_panel_open_mid_ant_Segovia_sample_13215_6x3.png}
- `appendices.tex:296` [Try 80] \caption{Try 80 \(6\times3\) inspection panel for an open, mid-antenna
- `appendices.tex:298` [Try 80] \label{fig:appendix_try80_open_mid}
- `appendices.tex:304` [Try 80] \includegraphics[width=\textwidth,height=0.88\textheight,keepaspectratio]{img/thesis_figures/try80_appendix_panels/try80_panel_open_high_ant_Nazareth_sample_10722_6x3.png}
- `appendices.tex:305` [Try 80] \caption{Try 80 \(6\times3\) inspection panel for an open, high-antenna
- `appendices.tex:307` [Try 80] \label{fig:appendix_try80_open_high}
- `appendices.tex:313` [Try 80] \includegraphics[width=\textwidth,height=0.88\textheight,keepaspectratio]{img/thesis_figures/try80_appendix_panels/try80_panel_mixed_low_ant_Dubrovnik_sample_05288_6x3.png}
- `appendices.tex:314` [Try 80] \caption{Try 80 \(6\times3\) inspection panel for a mixed, low-antenna
- `appendices.tex:316` [Try 80] \label{fig:appendix_try80_mixed_low}
- `appendices.tex:322` [Try 80] \includegraphics[width=\textwidth,height=0.88\textheight,keepaspectratio]{img/thesis_figures/try80_appendix_panels/try80_panel_mixed_mid_ant_Nice_sample_10828_6x3.png}
- `appendices.tex:323` [Try 80] \caption{Try 80 \(6\times3\) inspection panel for a mixed, mid-antenna
- `appendices.tex:325` [Try 80] \label{fig:appendix_try80_mixed_mid}
- `appendices.tex:331` [Try 80] \includegraphics[width=\textwidth,height=0.88\textheight,keepaspectratio]{img/thesis_figures/try80_appendix_panels/try80_panel_mixed_high_ant_Nice_sample_10814_6x3.png}
- `appendices.tex:332` [Try 80] \caption{Try 80 \(6\times3\) inspection panel for a mixed, high-antenna
- `appendices.tex:334` [Try 80] \label{fig:appendix_try80_mixed_high}
- `appendices.tex:340` [Try 80] \includegraphics[width=\textwidth,height=0.88\textheight,keepaspectratio]{img/thesis_figures/try80_appendix_panels/try80_panel_dense_low_ant_Chiang_Mai_sample_04519_6x3.png}
- `appendices.tex:341` [Try 80] \caption{Try 80 \(6\times3\) inspection panel for a dense, low-antenna
- `appendices.tex:343` [Try 80] \label{fig:appendix_try80_dense_low}
- `appendices.tex:349` [Try 80] \includegraphics[width=\textwidth,height=0.88\textheight,keepaspectratio]{img/thesis_figures/try80_appendix_panels/try80_panel_dense_mid_ant_Tunis_sample_14651_6x3.png}
- `appendices.tex:350` [Try 80] \caption{Try 80 \(6\times3\) inspection panel for a dense, mid-antenna
- `appendices.tex:352` [Try 80] \label{fig:appendix_try80_dense_mid}
- `appendices.tex:358` [Try 80] \includegraphics[width=\textwidth,height=0.88\textheight,keepaspectratio]{img/thesis_figures/try80_appendix_panels/try80_panel_dense_high_ant_Tunis_sample_14694_6x3.png}
- `appendices.tex:359` [Try 80] \caption{Try 80 \(6\times3\) inspection panel for a dense, high-antenna
- `appendices.tex:361` [Try 80] \label{fig:appendix_try80_dense_high}
- `appendices.tex:368` [Try 80] only the parts most relevant for reproducing the prior-anchored Try 80 design.
- `appendices.tex:374` [Try 78, Try 80] The Try 80 prior computer combines the calibrated Try 78 path-loss prior with
- `appendices.tex:375` [Try 79] the calibrated Try 79 spread priors. The path-loss branch keeps separate LoS
- `appendices.tex:385` [Try 78] nlos_prior = _compute_try78_nlos_map(topology, los_mask, h_tx,
- `appendices.tex:389` [Try 79] delay_prior = _compute_try79_metric_prior("delay_spread", ct6, ant,
- `appendices.tex:391` [Try 79] angular_prior = _compute_try79_metric_prior("angular_spread", ct6, ant,
- `appendices.tex:396` [Try 80] \section{Try 80 input tensor}
- `appendices.tex:452` [Try 80] Try~80 pipeline. The tool was built to make the trained model usable outside
- `appendices.tex:455` [Try 78, Try 79, Try 80] evaluates the frozen Try~78/79 priors, optionally runs the Try~80 neural model,
- `appendices.tex:480` [Try 80] because the masks are not only visual outputs: they are part of the Try~80
- `appendices.tex:493` [Try 80] When the Try~80 model is enabled, the generator produces the three target
- `appendices.tex:526` [Try 80] memory, and whether the selected runtime can execute the Try~80 model. In
- `appendices.tex:601` [Try 78, Try 79, Try 80] the CKM calibration and in the Try~78/79/80 prior formulas.
- `appendices.tex:616` [Try 80] \item \texttt{Run Try 80 model}: disables neural inference when only masks
- `appendices.tex:668` [Try 80] Try~80 was trained and calibrated on a fixed \(513\times513\) grid with
- `appendices.tex:802` [Try 80] three Try~80 prediction products, together with the saved joint prediction
- `appendices.tex:848` [Try 80] \texttt{Run Try 80 model} is useful when the goal is only to validate

### `conclusions.tex`

- `conclusions.tex:14` [Try 78] The original numerical targets were met by the finished non-DL priors. Try~78
- `conclusions.tex:16` [Try 79] \SI{3.3967}{dB} NLoS on the held-out cities. Try~79 achieved \SI{28.10}{ns}
- `conclusions.tex:18` [Try 80] evaluation contract. The final Try~80 neural model then improved those frozen
- `conclusions.tex:25` [Try 78] The path-loss result is the clearest success case. Try~78 already reached
- `conclusions.tex:28` [Try 80] visibility-dependent structure. Try~80 reduced this to \SI{1.6519}{dB}. This
- `conclusions.tex:38` [Try 80] For that reason, the Try~80 gains from \SI{28.10}{ns} to \SI{26.5570}{ns} in
- `conclusions.tex:61` [Try 80] targets, while Try~80 shows that a joint residual framework can refine those
- `conclusions.tex:88` [Try 75] The second contribution is the distribution-first diagnosis. The post-Try~75
- `conclusions.tex:91` [Try 76, Try 77] losses that reward a single central estimate. Try~76 and Try~77 converted that
- `conclusions.tex:95` [Try 78] The third contribution is the final prior family. Try~78 explains why the LoS
- `conclusions.tex:97` [Try 79] can outperform many neural attempts on that regime. Try~79 extends the same
- `conclusions.tex:99` [Try 80] these priors become interpretable anchors for the Try~80 joint residual model.
- `conclusions.tex:143` [Try 71] Try~71 showed that heteroscedastic uncertainty can identify hard pixels, but it
- `conclusions.tex:191` [Try 78, Try 79] Try~78 and Try~79 priors &
- `conclusions.tex:196` [Try 80] Try~80 &
- `conclusions.tex:208` [Try 80] The immediate extension is to strengthen the current Try~80 residual pipeline
- `conclusions.tex:224` [Try 78, Try 79] The final extension is field calibration. The Try~78 and Try~79 priors are

### `introduction.tex`

- `introduction.tex:78` [Try 78] \item A calibrated non-deep-learning path-loss prior (Try~78) based on an
- `introduction.tex:82` [Try 79] \item A calibrated non-deep-learning spread prior (Try~79) combining
- `introduction.tex:86` [Try 80] \item A prior-anchored joint neural residual model (Try~80) that shares a
- `introduction.tex:88` [Try 78, Try 79] Try~78 and Try~79 priors.
- `introduction.tex:90` [Try 66, Try 75] (Tries~66--75) that identifies NLoS mode collapse and motivates the
- `introduction.tex:91` [Try 76] Try~76 GMM architecture. The distribution analysis is released as
- `introduction.tex:101` [Try 80] axes along which Try~80 is positioned. The methodology chapter describes the
- `introduction.tex:104` [Try 78, Try 79, Try 80] prior-detail subsections for Tries~78, 79 and 80. The results chapter reports
- `introduction.tex:105` [Try 78] the quantitative outcomes: the Try~78 LoS waterfall, per-expert and per-height
- `introduction.tex:106` [Try 79, Try 80] breakdowns, Try~79 spread results, and the final Try~80 test evaluation on
- `introduction.tex:108` [Try 80] followed by the appendices with the representative validation panels and the Try~80
- `introduction.tex:155` [Try 76] Try 76: a distribution-first architecture with a sample-level GMM head followed
- `introduction.tex:156` [Try 77] by a map head that assigns pixels to distribution components. Try 77 applied
- `introduction.tex:160` [Try 78] The final stage changed the role of deep learning again. Try 78 built a strong
- `introduction.tex:162` [Try 79] calibrated NLoS corrections. Try 79 built log-domain ridge-calibrated priors
- `introduction.tex:163` [Try 80] for delay and angular spread. Try 80 then combined these frozen priors with a

### `methodology.tex`

- `methodology.tex:4` [Try 80] approach, and the final Try 80 architecture. The emphasis is on decisions that
- `methodology.tex:12` [Try 76, Try 77, Try 80] city level. For the final Try 76, Try 77, and Try 80 family the split uses
- `methodology.tex:18` [Try 78, Try 79] The non-deep-learning baselines Try 78 (path-loss prior) and Try 79 (spread
- `methodology.tex:23` [Try 78, Try 79] models; the 30\% test holdout of Try 78/79 corresponds to the union of the
- `methodology.tex:24` [Try 76, Try 77] 15\% validation and 15\% test cities used by Try 76, 77, and 80.
- `methodology.tex:29` [Try 76, Try 77, Try 80] \caption{City-holdout assignment used by Try 76, Try 77, and Try 80.}
- `methodology.tex:86` [Try 22] could learn both global radial structure and local map details. Try 22 became
- `methodology.tex:89` [Try 33] After Try 33, building pixels were excluded from both training loss and
- `methodology.tex:96` [Try 80] The work was not a single clean jump from U-Net to the final Try 80 model. It
- `methodology.tex:136` [Try 22] Try 22 became the strongest clean pre-prior path-loss baseline, with observed
- `methodology.tex:156` [Try 49] \SI{24.16}{dB}; Try 49 stage 1 reached about \SI{18.87}{dB} against a
- `methodology.tex:159` [Try 50] calibration; the best Try 50 NLoS sandbox remained around \SI{41}{dB}. \\
- `methodology.tex:163` [Try 66] Try 66 reached \SI{9.41}{dB} overall, with LoS already near
- `methodology.tex:176` [Try 76] Try 76 showed that NLoS can be treated as a distributional problem; the
- `methodology.tex:178` [Try 77] The method was powerful but task-specific; Try 77 provided a spread design,
- `methodology.tex:179` [Try 79] while final spread claims later came from the calibrated Try 79 prior. \\
- `methodology.tex:183` [Try 78, Try 79] Try 78 reached \SI{1.9246}{dB} overall path-loss RMSE; Try 79 reached
- `methodology.tex:184` [Try 80] \SI{28.10}{ns} and \SI{13.74}{\degree}; Try 80 unifies all three targets. &
- `methodology.tex:185` [Try 80] The final Try 80 checkpoint improves the frozen priors on the 14-city unseen
- `methodology.tex:269` [Try 66] \SI{9.4}{dB} (Try 66). The primary bottleneck was the "soft" nature of the
- `methodology.tex:275` [Try 80] by the prior-anchored GMM approach of \texttt{Try 80}, its core components---the
- `methodology.tex:284` [Try 75] The decisive diagnosis after Try 75 was that NLoS path loss was not merely a
- `methodology.tex:290` [Try 76] network to perform pixel-by-pixel prediction.  Try 76 addressed this by
- `methodology.tex:384` [Try 76] \caption{Try 76 distribution-first path-loss system. Stage~A learns global
- `methodology.tex:388` [Try 76] \label{fig:try76_system}
- `methodology.tex:391` [Try 77] Try 77 applied the same idea to delay spread and angular spread. These targets
- `methodology.tex:490` [Try 77] \caption{Try 77 spread-prediction system. The Stage~A mixture head
- `methodology.tex:494` [Try 77] \label{fig:try77_system}
- `methodology.tex:497` [Try 76] For path loss, Try 76 utilized 12 specialized experts: six topology classes partitioned by LoS
- `methodology.tex:498` [Try 76] and NLoS regions. As shown in Figure~\ref{fig:try76_system}, Stage A acts as a distribution head, predicting the global GMM parameters
- `methodology.tex:510` [Try 77] Try 77 extended this distribution-first philosophy to delay spread and angular spread. As illustrated in Figure~\ref{fig:try77_system}, these targets
- `methodology.tex:536` [Try 76] \texttt{Try 76} showed that the prior was not the essential ingredient. It
- `methodology.tex:540` [Try 78] directly. This changes the interpretation of the final \texttt{Try 78},
- `methodology.tex:541` [Try 79, Try 80] \texttt{Try 79}, and \texttt{Try 80} designs. The priors are not magic
- `methodology.tex:547` [Try 76] the \texttt{Try 76} lesson. The order in which the evidence arrived matters:
- `methodology.tex:548` [Try 75, Try 76] \texttt{Try 76} came immediately after the post-\texttt{Try 75} histogram
- `methodology.tex:555` [Try 78] handful of fitted constants (\texttt{Try 78}); for delay and angular spread
- `methodology.tex:557` [Try 79, Try 80] features (\texttt{Try 79}); \texttt{Try 80} then anchors a shared neural
- `methodology.tex:601` [Try 76] This explains the \texttt{Try 76} design. Stage A estimates the per-sample
- `methodology.tex:623` [Try 76, Try 77] aggregates the validation histograms used in the Try 76/77 diagnosis. Path-loss
- `methodology.tex:637` [Try 74, Try 75] \caption{Aggregated target and prediction histograms from the Try 74/75
- `methodology.tex:654` [Try 77] separately, as in the \texttt{Try 77} spike-plus-tail design and the
- `methodology.tex:655` [Try 79] \texttt{Try 79} log-domain regime-wise calibration.
- `methodology.tex:756` [Try 76, Try 77] The Stage-A distribution heads in \texttt{Try 76} and \texttt{Try 77}
- `methodology.tex:806` [Try 76, Try 77] the Try~76/77 target-distribution experts, even though the code supports
- `methodology.tex:807` [Try 80] $K\in\{2,\dots,5\}$. The \texttt{num\_components} field in the \texttt{Try 80}
- `methodology.tex:809` [Try 78, Try 79] residual distribution head after the frozen Try~78/Try~79 priors have already
- `methodology.tex:816` [Try 77] \ang{0}; this is implemented directly in the \texttt{Try 77} angular-spread
- `methodology.tex:822` [Try 80] The detailed definitions of the Try~80 objective are given in
- `methodology.tex:823` [Try 80] Sec.~\ref{sec:try80_objective}. This section keeps only the training contract
- `methodology.tex:847` [Try 80] \label{eq:try80_total}
- `methodology.tex:853` [Try 80] \caption{Active loss settings in the final path-loss-finetuned Try~80 checkpoint.}
- `methodology.tex:854` [Try 80] \label{tab:try80_loss_settings}
- `methodology.tex:884` [Try 80] shape. Try~80 keeps the residual GMM machinery available, but the selected
- `methodology.tex:892` [Try 76] final prior-anchored pipeline. The values for \texttt{Try 76},
- `methodology.tex:893` [Try 77, Try 80] \texttt{Try 77}, and \texttt{Try 80} are reported as methodological settings
- `methodology.tex:910` [Try 67, Try 71, Try 76, Try 77, Try 80] Config & Try 76 / 77 experts & Try 80 joint & Try 67--71 (historical) \\
- `methodology.tex:912` [Try 78, Try 79] Input channels   & topology, LoS, NLoS, ground mask (4 + scalar height) & topology + Try 78/79 priors + masks (9) & topology, LoS, distance, formula prior, knife-edge (5--6) \\
- `methodology.tex:932` [Try 67, Try 71, Try 76] Two patterns deserve emphasis. First, the move from Tries~67--71 to Try~76
- `methodology.tex:938` [Try 76, Try 77, Try 80] Second, Try~80 uses a smaller learning rate than the Try~76/Try~77 experts
- `methodology.tex:940` [Try 78, Try 79] inputs already include the strong Try~78/Try~79 priors; pushing the learning
- `methodology.tex:944` [Try 80] \section{Try 80 training progression}
- `methodology.tex:945` [Try 80] \label{sec:try80_training_progression}
- `methodology.tex:947` [Try 80] The final Try~80 model was not obtained in a single run. Training began with
- `methodology.tex:949` [Try 78, Try 79] only small improvements over the frozen Try~78/Try~79 priors. As a diagnostic,
- `methodology.tex:957` [Try 80] \item \textbf{Big.} The first full Try~80 version used a shared multi-task
- `methodology.tex:996` [Try 78, Try 79] \section{Try 78 and Try 79 priors: overview and literature basis}
- `methodology.tex:1001` [Try 78] \section{Try 78: Path Loss Prior}
- `methodology.tex:1002` [Try 78] \label{sec:try78_detail}
- `methodology.tex:1006` [Try 78] The Try~78 section is intentionally detailed because it is the mathematical
- `methodology.tex:1015` [Try 78, Try 80] Try~78 output becomes the frozen path-loss anchor consumed by Try~80.
- `methodology.tex:1018` [Try 78] waterfall in Table~\ref{tab:try78_los_waterfall} and the final path-loss
- `methodology.tex:1019` [Try 78] numbers in Table~\ref{tab:try78_results}: the enhanced two-ray branch reduces
- `methodology.tex:1023` [Try 78] \input{prior_detail_try78}
- `methodology.tex:1025` [Try 79] \section{Try 79: Delay and Angular Spread Priors}
- `methodology.tex:1026` [Try 79] \label{sec:try79_detail}
- `methodology.tex:1028` [Try 79] \input{prior_detail_try79}
- `methodology.tex:1030` [Try 80] \section{Try 80: Joint Prior-Anchored Residual Model}
- `methodology.tex:1031` [Try 80] \label{sec:try80_detail}
- `methodology.tex:1033` [Try 80] \input{prior_detail_try80}

### `prior_detail_overview.tex`

- `prior_detail_overview.tex:2` [Try 78, Try 79] priors (\texttt{Try 78} and \texttt{Try 79}) and the final joint architecture
- `prior_detail_overview.tex:3` [Try 80] (\texttt{Try 80}). It serves as a bridge between the high-level attempt history
- `prior_detail_overview.tex:6` [Try 80] final \texttt{Try 80} approach.
- `prior_detail_overview.tex:14` [Try 80] \textbf{Role in \texttt{Try 80}} \\
- `prior_detail_overview.tex:33` [Try 80] \texttt{Try 80} residual model & Probabilistic regression and mixture-density
- `prior_detail_overview.tex:42` [Try 80] adapted to CKM, and what is reused or newly assembled in \texttt{Try 80}.}
- `prior_detail_overview.tex:48` [Try 80] The central design decision in \texttt{Try 80} is \emph{not} to learn path
- `prior_detail_overview.tex:52` [Try 78] \item \texttt{Try 78} provides a frozen prior for \texttt{path\_loss},
- `prior_detail_overview.tex:53` [Try 79] \item \texttt{Try 79} provides frozen priors for \texttt{delay\_spread} and
- `prior_detail_overview.tex:55` [Try 80] \item \texttt{Try 80} learns bounded residual corrections around those priors.
- `prior_detail_overview.tex:70` [Try 78] \node[box, fill=blue!15]  (t78) {Try 78\\(path loss)};
- `prior_detail_overview.tex:71` [Try 79] \node[box, fill=green!15, below=of t78] (t79) {Try 79\\(spreads)};
- `prior_detail_overview.tex:87` [Try 80] \caption{Overall \texttt{Try 80} pipeline. The frozen priors are injected into the DNN, which learns a bounded correction $\delta$ around them.}
- `prior_detail_overview.tex:98` [Try 78] used many of the same physical ingredients as \texttt{Try 78}, but they did
- `prior_detail_overview.tex:99` [Try 78] not always keep those pieces aligned. \texttt{Try 78} became strong because it
- `prior_detail_overview.tex:108` [Try 80] large-scale structure from the genuinely local residual that Try~80 later
- `prior_detail_overview.tex:115` [Try 78, Try 79] lessons: \texttt{Try 78}/\texttt{Try 79} fix the prior-estimator problem, while
- `prior_detail_overview.tex:116` [Try 76, Try 77] \texttt{Try 76}/\texttt{Try 77} motivate distribution-aware heads and residual
- `prior_detail_overview.tex:144` [Try 80] Try~80 is allowed to correct local errors without overwriting the calibrated
- `prior_detail_overview.tex:155` [Try 78] equations and fitting procedures follow in the dedicated \texttt{Try 78},
- `prior_detail_overview.tex:156` [Try 79, Try 80] \texttt{Try 79}, and \texttt{Try 80} subsections.
- `prior_detail_overview.tex:171` [Try 78] Try~78 LoS path loss &
- `prior_detail_overview.tex:177` [Try 78] Try~78 NLoS path loss &
- `prior_detail_overview.tex:183` [Try 79] Try~79 delay and angular spread &
- `prior_detail_overview.tex:190` [Try 80] Try~80 residual model &

### `prior_detail_try78.tex`

- `prior_detail_try78.tex:6` [Try 78] Try 78 LoS branch then adds the fitted ground-reflection interference term,
- `prior_detail_try78.tex:380` [Try 80] \(\mathrm{clip}_{[20,180]}\) & Output guard. & Keeps the frozen prior inside the physical path-loss range used by Try 80. \\
- `prior_detail_try78.tex:383` [Try 78] \caption{Term-by-term inventory of the \texttt{Try 78} LoS prior used by
- `prior_detail_try78.tex:384` [Try 80] \texttt{Try 80}. Unlike the NLoS branch, this is not a long pixel-feature
- `prior_detail_try78.tex:609` [Try 80] The NLoS path-loss branch used in \texttt{Try 80} is not a pure literature
- `prior_detail_try78.tex:783` [Try 78] \texttt{Try 78} variants to keep the LoS formula below an A2G envelope. In
- `prior_detail_try78.tex:784` [Try 80] the final frozen \texttt{Try 80} path, LoS pixels come directly from the
- `prior_detail_try78.tex:796` [Try 78] Eq.~\eqref{eq:pl0} is the only physical model in \texttt{Try 78}; it depends
- `prior_detail_try78.tex:862` [Try 78] \caption{Term-by-term inventory of the \texttt{Try 78} NLoS calibration
- `prior_detail_try78.tex:1114` [Try 80] two-ray calibration JSON used by \texttt{Try 80}, for example, is about
- `prior_detail_try78.tex:1132` [Try 80] and NLoS regime coefficients. However, in the final frozen \texttt{Try 80}
- `prior_detail_try78.tex:1178` [Try 80] $\mathrm{class}_6$ and is used in \texttt{Try 80} reporting.
- `prior_detail_try78.tex:1228` [Try 79] the fallback chain in the Try 79 section, which uses the same strategy).
- `prior_detail_try78.tex:1253` [Try 78] This makes Try~78 an interpretable calibrated surrogate rather than a pure
- `prior_detail_try78.tex:1309` [Try 78] \subsection{Observed Try 78 results}
- `prior_detail_try78.tex:1311` [Try 78] The headline path-loss numbers for \texttt{Try 78} are reported in the
- `prior_detail_try78.tex:1312` [Try 78] results chapter (LoS waterfall in Table~\ref{tab:try78_los_waterfall}): the
- `prior_detail_try78.tex:1316` [Try 80] \texttt{Try 80} reaches \SI{1.9246}{dB} overall.
- `prior_detail_try78.tex:1365` [Try 78] \caption{Pipeline for the \texttt{Try 78} hybrid path loss prior. The LoS branch relies on an explicit two-ray interference model, while the NLoS branch calibrates a raw prior against map-derived morphology features using regime-wise OLS. The two branches are hard-switched based on the LoS mask to produce the final frozen prior.}
- `prior_detail_try78.tex:1366` [Try 78] \label{fig:try78_pipeline}

### `prior_detail_try79.tex`

- `prior_detail_try79.tex:24` [Try 79] \subsection{Pixel-wise notation for the Try 79 fit}
- `prior_detail_try79.tex:39` [Try 79] \label{eq:try79_pixel_linear}
- `prior_detail_try79.tex:42` [Try 79] LoS/NLoS state and UAV-height bin. In other words, Try 79 does not fit one
- `prior_detail_try79.tex:113` [Try 78] As in the Try 78 path-loss vector, some of these terms are not independent.
- `prior_detail_try79.tex:145` [Try 79] \caption{Term-by-term inventory of the direct terms in the \texttt{Try 79} spread calibration vector.}
- `prior_detail_try79.tex:164` [Try 79] \caption{Interaction terms in the \texttt{Try 79} spread calibration vector.}
- `prior_detail_try79.tex:192` [Try 79] \caption{Feature grouping used by the \texttt{Try 79} calibrated spread prior.
- `prior_detail_try79.tex:195` [Try 79] \label{fig:try79_feature_groups}
- `prior_detail_try79.tex:243` [Try 79] The regime $r$ for Try 79 is keyed by: metric (DS or AS), topology class (6 classes), propagation state (LoS or NLoS), antenna-height bin, giving up to $2 \times 6 \times 2 \times 3 = 72$ regimes.
- `prior_detail_try79.tex:268` [Try 79] \label{eq:try79_ridge_objective}
- `prior_detail_try79.tex:291` [Try 78] large even after compression into fitted coefficients and profiles. The Try 78
- `prior_detail_try79.tex:292` [Try 80] LoS calibration JSON reused by Try 80 is approximately 200\,000 lines, and the
- `prior_detail_try79.tex:320` [Try 79] \label{eq:try79_clip}
- `prior_detail_try79.tex:328` [Try 79] \subsection{Try 79 results}
- `prior_detail_try79.tex:393` [Try 79] \caption{Pipeline for the \texttt{Try 79} delay and angular spread priors. Both spread modalities share this identical linear architecture, predicting expected spread in the log domain via regime-wise ridge regression over 23 spatial and geometric features.}
- `prior_detail_try79.tex:394` [Try 79] \label{fig:try79_pipeline}

### `prior_detail_try80.tex`

- `prior_detail_try80.tex:3` [Try 80] \texttt{Try 80} follows the same strict split philosophy as the recent
- `prior_detail_try80.tex:24` [Try 80] conditioning. The final \texttt{try80\_joint\_huge\_pathloss\_finetune}
- `prior_detail_try80.tex:31` [Try 80] The final \texttt{Try 80} checkpoint reported in Chapter~\ref{chap:results}
- `prior_detail_try80.tex:32` [Try 78, Try 79] uses these frozen \texttt{Try 78}/\texttt{Try 79} priors as anchors. This
- `prior_detail_try80.tex:38` [Try 80] \texttt{Try 80} introduces a joint multi-task architecture that predicts a
- `prior_detail_try80.tex:61` [Try 80] \label{eq:try80_residual_caps}
- `prior_detail_try80.tex:76` [Try 80] \label{eq:try80_delta_assembly}
- `prior_detail_try80.tex:86` [Try 80] \label{eq:try80_mu}
- `prior_detail_try80.tex:92` [Try 78, Try 79] \texttt{Try 78} or \texttt{Try 79},
- `prior_detail_try80.tex:113` [Try 80] \label{eq:try80_mu_transform}
- `prior_detail_try80.tex:126` [Try 80] \label{eq:try80_sigma}
- `prior_detail_try80.tex:135` [Try 80] \texttt{try80\_joint\_huge\_pathloss\_finetune} checkpoint, however, uses the
- `prior_detail_try80.tex:152` [Try 80] \label{eq:try80_point}
- `prior_detail_try80.tex:173` [Try 80] \label{eq:try80_loss}
- `prior_detail_try80.tex:179` [Try 80] Sec.~\ref{sec:try80_objective}.
- `prior_detail_try80.tex:183` [Try 80] \texttt{Try 80} processes the map inputs through a shared multi-task
- `prior_detail_try80.tex:311` [Try 80] \caption{Schematic of the final \texttt{Try 80 huge} shared UNet architecture with FiLM conditioning.}
- `prior_detail_try80.tex:312` [Try 80] \label{fig:try80_arch}
- `prior_detail_try80.tex:338` [Try 80] \label{eq:try80_height_embed}
- `prior_detail_try80.tex:392` [Try 80] \caption{Detailed \texttt{Try 80} sinusoidal height-conditioning path.}
- `prior_detail_try80.tex:393` [Try 80] \label{fig:try80_film_detail}
- `prior_detail_try80.tex:458` [Try 80] \caption{Detailed prior-anchored GMM head used by \texttt{Try 80}.}
- `prior_detail_try80.tex:459` [Try 80] \label{fig:try80_gmm_detail}
- `prior_detail_try80.tex:463` [Try 80] \label{sec:try80_objective}
- `prior_detail_try80.tex:497` [Try 80] \label{eq:try80_total_loss}
- `prior_detail_try80.tex:501` [Try 80] \texttt{try80\_joint\_huge\_pathloss\_finetune} checkpoint are
- `prior_detail_try80.tex:526` [Try 80] \label{eq:try80_mixture_density}
- `prior_detail_try80.tex:536` [Try 80] \label{eq:try80_nll}
- `prior_detail_try80.tex:538` [Try 80] The implemented version evaluates Eq.~\eqref{eq:try80_nll} using
- `prior_detail_try80.tex:558` [Try 80] \label{eq:try80_kl}
- `prior_detail_try80.tex:573` [Try 80] \label{eq:try80_moment}
- `prior_detail_try80.tex:593` [Try 80] \label{eq:try80_anchor}
- `prior_detail_try80.tex:595` [Try 80] The guard term is Eq.~\eqref{eq:try80_loss}. Together, these two terms encode
- `prior_detail_try80.tex:596` [Try 80] the design philosophy of \texttt{Try 80}: the DNN is allowed to improve the
- `prior_detail_try80.tex:614` [Try 80] \label{eq:try80_outlier}
- `prior_detail_try80.tex:631` [Try 80] \label{eq:try80_rmse_mae_loss}
- `prior_detail_try80.tex:658` [Try 80] \caption[Composite \texttt{Try 80} loss family]{Composite \texttt{Try 80}
- `prior_detail_try80.tex:663` [Try 80] \label{fig:try80_loss_terms}

### `results.tex`

- `results.tex:5` [Try 80] project. The headline numbers now include the final frozen Try~80 checkpoint
- `results.tex:6` [Try 79] evaluated on the same city-holdout test split used by the Try~79 spread
- `results.tex:7` [Try 78] priors: 2590 samples from 14 unseen cities. Try~78 remains documented under
- `results.tex:8` [Try 80] its 30\% analytic-prior evaluation holdout, while Try~80 is reported as the
- `results.tex:26` [Try 1, Try 22] Try 1--22   & U-Net/cGAN and decoder fixes; cGAN did not solve physical error. & Try 22 became the clean pre-prior baseline. \\
- `results.tex:27` [Try 33, Try 40] Try 33--40  & Ground-only masking became mandatory. & Building pixels excluded from loss and metrics. \\
- `results.tex:28` [Try 41, Try 42, Try 50] Try 41--50  & Prior plus residual helped LoS but NLoS remained dominant. & Try 42: \SI{19.78}{dB} overall, \SI{3.86}{dB} LoS, \SI{34.47}{dB} NLoS. \\
- `results.tex:29` [Try 66] Try 66      & PMHHNet synthesis with six experts and physical channels. & \SI{9.41}{dB} overall, \SI{3.75}{dB} LoS, \SI{31.48}{dB} NLoS. \\
- `results.tex:30` [Try 76] Try 76      & Distribution-first path-loss modelling. & NLoS pixel-weighted RMSE $\approx$\,\SI{3.34}{dB}. \\
- `results.tex:31` [Try 78] Try 78      & Non-DL calibrated path-loss prior. & \SI{1.92}{dB} overall, \SI{1.75}{dB} LoS, \SI{3.40}{dB} NLoS. \\
- `results.tex:32` [Try 79] Try 79      & Non-DL calibrated spread priors. & \SI{28.10}{ns} delay; \SI{13.74}{\degree} angular. \\
- `results.tex:33` [Try 80] Try 80      & Joint prior-anchored model. & Final test: \SI{1.65}{dB} path loss, \SI{26.56}{ns} delay spread, \SI{11.39}{\degree} angular spread; RMSE improves over the frozen priors on all three outputs. \\
- `results.tex:38` [Try 78] Try 78 is the clearest path-loss breakthrough. The enhanced two-ray LoS model
- `results.tex:43` [Try 78] \subsection{Try 78 LoS prior progression}
- `results.tex:45` [Try 78] The LoS branch of Try 78 was developed as a short waterfall of three
- `results.tex:48` [Try 78] (Table~\ref{tab:try78_los_waterfall}).
- `results.tex:52` [Try 78] \caption{Try 78 LoS path-loss progression: three priors evaluated on the same
- `results.tex:54` [Try 78] \label{tab:try78_los_waterfall}
- `results.tex:76` [Try 80] dominant LoS residual shape in CKM, and it is why Try 80 uses the two-ray
- `results.tex:87` [Try 80] residual learning, to frozen calibrated priors and finally to the joint Try 80
- `results.tex:107` [Try 20] Try 20 & Path loss & \(\approx 17.40\) dB & Bilinear decoder alone reduced artifacts but did not solve global propagation. \\
- `results.tex:108` [Try 21] Try 21 & Path loss & \(\approx 17.06\) dB & Multiscale supervision helped the large-scale field. \\
- `results.tex:109` [Try 22] Try 22 & Path loss & \(\approx 16.72\) dB & Best clean pre-prior baseline in the early U-Net family. \\
- `results.tex:110` [Try 41] Try 41 prior & Path loss & \(\approx 67.23\) dB & Raw physical prior was far too crude without calibration. \\
- `results.tex:111` [Try 41] Try 41 calibrated prior & Path loss & \(\approx 24.16\) dB & Regime-aware train-only calibration made the prior useful but incomplete. \\
- `results.tex:112` [Try 42] Try 42 & Path loss & \(\approx 19.78\) dB & PMNet-style residual learning improved over prior-only calibration. \\
- `results.tex:113` [Try 49] Try 49 stage 1 & Path loss & \(\approx 18.87\) dB & Prior-confidence and robust loss helped, but tail errors persisted. \\
- `results.tex:114` [Try 66] Try 66 & Path loss overall & 9.41 dB & PMHHNet consolidated the physical-channel and expert approach. \\
- `results.tex:115` [Try 66] Try 66 & Path loss NLoS & 31.48 dB & The headline bottleneck was no longer global; it was NLoS tail failure. \\
- `results.tex:116` [Try 76] Try 76 & Path loss NLoS & \(\approx 3.34\) dB & Distribution-first modelling directly attacked NLoS multi-modality. \\
- `results.tex:117` [Try 78] Try 78 & Path loss overall & 1.9246 dB & Calibrated non-DL prior became the strongest path-loss baseline. \\
- `results.tex:118` [Try 79] Try 79 & Delay spread overall & 28.10 ns & Log-domain ridge calibration met the original 50 ns project target. \\
- `results.tex:119` [Try 79] Try 79 & Angular spread overall & \(13.74^\circ\) & Regime-wise calibration met the original 20 degree target. \\
- `results.tex:120` [Try 80] Try 80 final test & Joint outputs & 1.6519 dB PL; 26.5570 ns DS; \(11.3854^\circ\) AS & Final frozen checkpoint on 14 unseen test cities; model RMSE improves over every frozen prior. \\
- `results.tex:126` [Try 76, Try 77, Try 79] Tries 76, 77, 79, and 80 use the same \texttt{city\_holdout}
- `results.tex:130` [Try 76, Try 77] different: Try 76 and Try 77 report the six topology classes directly,
- `results.tex:131` [Try 80] whereas Try 80 groups them into three two-class morphology families
- `results.tex:134` [Try 78] grid, not the test samples. Try 78 is the exception: its final hybrid
- `results.tex:136` [Try 76, Try 77, Try 80] of the analytic prior. This holdout contains the same Try 76/77/80 test
- `results.tex:137` [Try 78] cities, but also contains additional validation-side cities, so Try 78
- `results.tex:149` [Try 49] For example, Try 49 had moderate average absolute error on many samples, but
- `results.tex:154` [Try 66] Third, LoS and NLoS must be reported separately. Try 66 already had LoS error
- `results.tex:161` [Try 78] \caption{Try 78 final hybrid path-loss prior, pixel-weighted RMSE on the
- `results.tex:163` [Try 78] \label{tab:try78_results}
- `results.tex:175` [Try 79] Try 79 showed that a large part of the spread targets can also be explained by
- `results.tex:188` [Try 79] \caption{Try 79 calibrated test results, pixel-weighted RMSE.}
- `results.tex:189` [Try 79] \label{tab:try79_results}
- `results.tex:200` [Try 76] \subsection{Try 76 as a distribution-first reference}
- `results.tex:202` [Try 76] Try 76 is not the final model of this thesis, but its result is quoted here
- `results.tex:205` [Try 76] channel, and no residual-over-prior structure, the distribution-first Try 76
- `results.tex:212` [Try 66, Try 69] Tries 66--69 disappears. This is a small RMSE difference compared to the
- `results.tex:213` [Try 78] Try 78 non-DL prior (\SI{3.40}{dB} NLoS), but it is a qualitatively different
- `results.tex:219` [Try 76] Try 76 trains twelve specialised GMM experts. A sequential DirectML
- `results.tex:225` [Try 76] between LoS and NLoS regimes. Table~\ref{tab:try76_per_expert} reports
- `results.tex:232` [Try 76] \caption{Try 76 DirectML test RMSE per expert on the shared
- `results.tex:236` [Try 76] \texttt{tmp\_try76\_directml\_test\_metrics.json}.}
- `results.tex:237` [Try 76] \label{tab:try76_per_expert}
- `results.tex:257` [Try 76] \textbf{LoS path loss is consistently harder for Try 76 than NLoS path
- `results.tex:260` [Try 66, Try 69] contradicts the intuition built up during Tries 66--69 where NLoS was
- `results.tex:262` [Try 78] This reversal motivated the later return to explicit priors in Try 78 and
- `results.tex:263` [Try 79] Try 79.
- `results.tex:268` [Try 76] of the model. The Try~76 histogram study reports the following global
- `results.tex:276` [Try 76] Figure~\ref{fig:try76_los_vs_nlos_distribution}, with rare high-loss
- `results.tex:287` [Try 76] larger for LoS}: Try 76 only sees $\sigma \approx \SI{5.3}{dB}$ of useful
- `results.tex:294` [Try 66, Try 69, Try 76] shape that mode collapse damaged in Tries 66--69, and Try 76's GMM head
- `results.tex:299` [Try 76] The global comparison is only a first-order diagnostic: Try~76 does not
- `results.tex:301` [Try 76] one LoS and one NLoS GMM expert per topology class. Figure~\ref{fig:try76_los_vs_nlos_distribution}
- `results.tex:303` [Try 76] matching the default Stage-A mixture size used by Try~76, for each
- `results.tex:318` [Try 76] Figure~\ref{fig:try76_los_vs_nlos} (right panel) plots this skill
- `results.tex:321` [Try 76] \(0.71\)--\(0.90\). In other words, Try 76 usually explains a larger fraction
- `results.tex:328` [Try 76] \includegraphics[width=\textwidth]{img/thesis_figures/results_addendum/try76_los_vs_nlos.png}
- `results.tex:329` [Try 76] \caption{Try 76 DirectML test RMSE per expert. \emph{Left}: bars are
- `results.tex:337` [Try 76] \label{fig:try76_los_vs_nlos}
- `results.tex:342` [Try 76] \includegraphics[width=\textwidth]{img/thesis_figures/results_addendum/try76_los_vs_nlos_distribution.png}
- `results.tex:344` [Try 76] path-loss targets, shown separately for the six Try~76 topology
- `results.tex:353` [Try 76] \label{fig:try76_los_vs_nlos_distribution}
- `results.tex:356` [Try 76, Try 78] \subsection{Try 76 to Try 78: why priors came back}
- `results.tex:358` [Try 76, Try 78] Reading the project in chronological order, the move from Try 76 to Try 78 can
- `results.tex:362` [Try 76] order in which the evidence arrived is spelled out. Try 76 came
- `results.tex:363` [Try 75] \emph{immediately after} the post-Try-75 histogram diagnosis. That diagnosis
- `results.tex:372` [Try 78] (Try 78), not a neural residual head. For delay and angular spread the answer
- `results.tex:374` [Try 76, Try 77, Try 79, Try 80] (Try 79). Try 80 then keeps the Try 76/77 distribution-aware philosophy but
- `results.tex:375` [Try 78, Try 79] anchors the neural residual head to the Try 78/79 priors rather than forcing
- `results.tex:377` [Try 76] are an efficiency and stability device, not a contradiction of the Try 76
- `results.tex:380` [Try 77] \subsection{Try 77: GMM experts for delay and angular spread}
- `results.tex:382` [Try 76, Try 77] Try 77 applies the Try 76 distribution-first recipe to delay spread and
- `results.tex:385` [Try 76] for a total of twelve experts. Unlike Try 76, the LoS / NLoS split is
- `results.tex:386` [Try 77] not enforced inside Try 77 because the spread targets are defined over
- `results.tex:392` [Try 76, Try 77] In this chapter, ````six experts'' denotes the legacy Try 76/77
- `results.tex:397` [Try 78] The analytic priors then refine this routing internally: Try 78 uses
- `results.tex:398` [Try 79] coarse topology, LoS/NLoS state and antenna-height bin, while Try 79
- `results.tex:399` [Try 80] also keys the regime by spread metric. Try 80 reports a simpler final
- `results.tex:406` [Try 76, Try 80] test metrics on the same 2590-sample holdout used by Try 76 and Try 80.
- `results.tex:407` [Try 77] Table~\ref{tab:try77_per_expert} reports both sample-mean and
- `results.tex:414` [Try 77] \caption{Try 77 DirectML test RMSE per expert on the shared
- `results.tex:417` [Try 77] \texttt{tmp\_try77\_directml\_test\_metrics.json}.}
- `results.tex:418` [Try 77] \label{tab:try77_per_expert}
- `results.tex:438` [Try 77] The angular-spread side of Try 77 is the cleanest neural result in this
- `results.tex:444` [Try 79] non-DL Try 79 prior (\SI{28.10}{ns}). The gap between sample-mean and
- `results.tex:449` [Try 79] precursor, while Try 79 is the deployed spread baseline used to anchor
- `results.tex:450` [Try 80] Try 80.
- `results.tex:468` [Try 79] \includegraphics[width=\textwidth]{img/thesis_figures/results_addendum/try79_quantized_spread_example.png}
- `results.tex:469` [Try 79] \caption{Example of spread-target quantisation on a Try~79 test sample
- `results.tex:477` [Try 79] \label{fig:try79_quantized_spread_example}
- `results.tex:482` [Try 77] \includegraphics[width=\textwidth]{img/thesis_figures/results_addendum/try77_per_expert.png}
- `results.tex:483` [Try 77] \caption{Try 77 DirectML test RMSE per expert, separated by spread
- `results.tex:490` [Try 79] Try 79 ridge calibration.}
- `results.tex:491` [Try 77] \label{fig:try77_per_expert}
- `results.tex:498` [Try 78] strong altitude-dependent structure. Tables~\ref{tab:try78_by_height} and
- `results.tex:499` [Try 78, Try 79] \ref{tab:try79_by_height} therefore break the Try 78 path loss and the Try 79
- `results.tex:505` [Try 78] \caption{Try 78 path-loss pixel-weighted RMSE by UAV transmitter height, on
- `results.tex:507` [Try 78] \label{tab:try78_by_height}
- `results.tex:523` [Try 79] \caption{Try 79 delay spread and angular spread calibrated pixel-weighted RMSE
- `results.tex:525` [Try 79] \label{tab:try79_by_height}
- `results.tex:553` [Try 80] Try 80 is that the neural residual head has less to correct at high altitudes,
- `results.tex:554` [Try 78] where the Try 78 prior is already close to the quantisation floor. The
- `results.tex:558` [Try 78] \subsection{Try 78 path-loss prior by topology class}
- `results.tex:560` [Try 78] The headline Try 78 number (\SI{1.92}{dB} overall RMSE on its
- `results.tex:561` [Try 78] 30\% city-holdout evaluation split, see Table~\ref{tab:try78_results}) hides the
- `results.tex:562` [Try 76] same morphological structure that Try 76 surfaced. The per-sample evaluation
- `results.tex:564` [Try 76] Try~76 topology classes with the same routing rule used by the
- `results.tex:567` [Try 78] Table~\ref{tab:try78_by_topology} and visualised in
- `results.tex:568` [Try 78] Figure~\ref{fig:try78_by_topology}.
- `results.tex:572` [Try 78] \caption{Try 78 hybrid path-loss prior, pixel-weighted RMSE on the
- `results.tex:573` [Try 76] 30\% city-holdout evaluation split, broken down by Try 76 topology class. The
- `results.tex:574` [Try 78] overall row reproduces Table~\ref{tab:try78_results}.}
- `results.tex:575` [Try 78] \label{tab:try78_by_topology}
- `results.tex:594` [Try 76] pattern observed in Try 76. The two-ray prior fits its own ground
- `results.tex:597` [Try 76] Table~\ref{tab:try76_per_expert}), so the LoS RMSE of the analytic
- `results.tex:602` [Try 76] best (\SI{4.09}{dB} versus \SI{2.81}{dB} for Try 76 NLoS in
- `results.tex:611` [Try 76, Try 78] Figure~\ref{fig:try78_by_topology} compares Try 76 (DL, GMM, no
- `results.tex:612` [Try 78] physics) against Try 78 (analytic two-ray prior, no neural network) on
- `results.tex:614` [Try 76] within about \SI{1}{dB} on most topology classes, and Try 76 is in fact
- `results.tex:616` [Try 76] gap quoted earlier (\SI{3.34}{dB} for Try 76 NLoS versus \SI{3.40}{dB}
- `results.tex:617` [Try 78] for Try 78 NLoS) is therefore not an artefact of one easy class
- `results.tex:627` [Try 78] \includegraphics[width=\textwidth]{img/thesis_figures/results_addendum/try78_by_topology.png}
- `results.tex:628` [Try 78] \caption{Try 78 path-loss prior by topology class. \emph{Left}: LoS,
- `results.tex:629` [Try 76] NLoS and overall pixel-weighted RMSE for each of the six Try 76
- `results.tex:632` [Try 76] reported for Try 76 in Table~\ref{tab:try76_per_expert}. \emph{Right}:
- `results.tex:633` [Try 76] NLoS RMSE side by side with Try 76 (DL, GMM, no physics) on the same
- `results.tex:637` [Try 78] \label{fig:try78_by_topology}
- `results.tex:640` [Try 80] \subsection{Final Try 80 joint prior-anchored test results}
- `results.tex:642` [Try 78, Try 79, Try 80] Try 80 freezes the Try 78/79 priors and learns a bounded residual correction
- `results.tex:645` [Try 80] \texttt{try80\_joint\_huge\_pathloss\_finetune}; it is tested on the
- `results.tex:655` [Try 80] \label{eq:try80_model_rmse}
- `results.tex:667` [Try 80] \caption{Final Try 80 test results on unseen cities, compared with the frozen
- `results.tex:668` [Try 78, Try 79, Try 80] Try 78/79 priors. Negative \(\Delta\) means that Try 80 improves the prior.}
- `results.tex:669` [Try 80] \label{tab:try80_final_test_overall}
- `results.tex:684` [Try 80] \caption{Final Try 80 test RMSE separated by LoS and NLoS pixels. The test
- `results.tex:686` [Try 80] \label{tab:try80_final_test_los_nlos}
- `results.tex:714` [Try 80] Table~\ref{tab:try80_val_test_sanity} reports the two scopes side by side.
- `results.tex:718` [Try 80] \caption{Try 80 validation-versus-test sanity check for the same
- `results.tex:722` [Try 80] \label{tab:try80_val_test_sanity}
- `results.tex:736` [Try 80] \caption{Try 80 pixel-weighted RMSE by split, compared with the frozen
- `results.tex:737` [Try 78, Try 79] Try 78/79 priors. The test split is the unseen-city generalisation claim;
- `results.tex:739` [Try 80] \label{tab:try80_split_absolute}
- `results.tex:754` [Try 79] effect, not a change of model or metric. The frozen Try~79 delay-spread prior
- `results.tex:774` [Try 80] \caption{Try 80 improvement over the frozen priors by split. Values are
- `results.tex:777` [Try 80] \label{tab:try80_split_delta}
- `results.tex:793` [Try 80] \caption{Try 80 LoS/NLoS RMSE improvement by split. Values are
- `results.tex:796` [Try 80] \label{tab:try80_los_nlos_split_delta}
- `results.tex:816` [Try 80] \caption{All-city Try 80 deltas by prior subexpert. Each city contributes to
- `results.tex:819` [Try 80] \label{tab:try80_subexpert_delta}
- `results.tex:838` [Try 80] \subsubsection*{Target vs final Try 80 result}
- `results.tex:841` [Try 80] test split. Figure~\ref{fig:try80_test_objectives} compares those targets with
- `results.tex:842` [Try 80] the global pixel-weighted Try~80 test scores: \SI{1.65}{dB} for path loss,
- `results.tex:854` [Try 80] symbolic x coords={Target,Try 80},
- `results.tex:855` [Try 80] xtick={Target,Try 80},
- `results.tex:869` [Try 80] \addplot[fill=blue!55, draw=black, bar shift=0pt] coordinates {(Try 80,1.65)};
- `results.tex:878` [Try 80] \addplot[fill=orange!70, draw=black, bar shift=0pt] coordinates {(Try 80,26.56)};
- `results.tex:887` [Try 80] \addplot[fill=green!60, draw=black, bar shift=0pt] coordinates {(Try 80,11.39)};
- `results.tex:891` [Try 80] \caption{\textbf{TARGET vs Final Result.} Try 80 global test check using
- `results.tex:895` [Try 80] \label{fig:try80_test_objectives}
- `results.tex:902` [Try 75] trend but underestimated shadowed regions. Histogram analysis after Try 75 made
- `results.tex:926` [Try 76, Try 80] symbolic x coords={Try76,Try80,Prior},
- `results.tex:928` [Try 76, Try 80] xticklabels={Try\,76,Try\,80,Prior},
- `results.tex:930` [Try 76, Try 80] \addplot[fill=blue!55] coordinates {(Try76,4.36) (Try80,1.65) (Prior,1.94)};
- `results.tex:941` [Try 77, Try 80] symbolic x coords={Try77,Try80,Prior},
- `results.tex:943` [Try 77, Try 80] xticklabels={Try\,77,Try\,80,Prior},
- `results.tex:945` [Try 77, Try 80] \addplot[fill=orange!70] coordinates {(Try77,30.96) (Try80,26.56) (Prior,28.10)};
- `results.tex:956` [Try 77, Try 80] symbolic x coords={Try77,Try80,Prior},
- `results.tex:958` [Try 77, Try 80] xticklabels={Try\,77,Try\,80,Prior},
- `results.tex:960` [Try 77, Try 80] \addplot[fill=green!60] coordinates {(Try77,11.78) (Try80,11.39) (Prior,13.74)};
- `results.tex:965` [Try 80] and the final prior-anchored Try 80 checkpoint. The path-loss panel uses global
- `results.tex:966` [Try 77] pixel-weighted RMSE; Try 77 is shown for the two spread targets.}
- `results.tex:967` [Try 76] \label{fig:try76_77_80_prior_comparison}
- `results.tex:972` [Try 80] {\scriptsize Coloured bars are Try 80 and grey bars are the frozen prior.\par}
- `results.tex:1012` [Try 80] \caption{Try 80 versus the frozen prior across train, validation, unseen test,
- `results.tex:1015` [Try 80] \label{fig:try80_split_rmse}
- `results.tex:1026` [Try 80] xticklabels={Try\,80, Prior},
- `results.tex:1056` [Try 80] \caption{Final Try 80 test RMSE on unseen cities against the frozen priors for
- `results.tex:1058` [Try 80] \label{fig:try80_test_final}
- `results.tex:1063` [Try 80] {\scriptsize Coloured bars are Try 80 and grey bars are the frozen prior.\par}
- `results.tex:1102` [Try 80] \caption{Final Try 80 test RMSE separated by LoS and NLoS pixels. The model
- `results.tex:1104` [Try 80] \label{fig:try80_test_los_nlos}
- `results.tex:1158` [Try 80] \caption{All-city Try 80 RMSE deltas by prior subexpert. Negative values mean
- `results.tex:1159` [Try 80] that Try 80 improves the frozen prior. The first letter denotes the morphology
- `results.tex:1162` [Try 80] \label{fig:try80_subexpert_delta}
- `results.tex:1165` [Try 80] Figure~\ref{fig:try80_panel} shows a representative Try 80 validation
- `results.tex:1168` [Try 78, Try 79, Try 80] six rows are the ground truth, frozen Try 78/79 prior, Try 80 prediction,
- `results.tex:1170` [Try 80] model correction \(\mathrm{Try\,80}-\mathrm{Prior}\). The last two rows are
- `results.tex:1177` [Try 80] \includegraphics[width=\textwidth,height=0.88\textheight,keepaspectratio]{img/thesis_figures/try80_appendix_panels/try80_main_panel.png}
- `results.tex:1178` [Try 80] \caption{Representative Try 80 \(6\times3\) inspection panel for a validation
- `results.tex:1180` [Try 78, Try 79, Try 80] angular spread. Rows: ground truth, frozen prior (Try 78/79), Try 80
- `results.tex:1183` [Try 80] ($\mathrm{Try\,80}-\mathrm{Prior}$).}
- `results.tex:1184` [Try 80] \label{fig:try80_panel}
- `results.tex:1187` [Try 78] The qualitative lesson from Try 78 is equally important: LoS path loss in this
- `results.tex:1217` [Try 80] current Try~80 snapshot, but it is an irreducible resolution limit of the saved
- `results.tex:1263` [Try 80] The final Try 80 checkpoint is evaluated on one city-holdout split and one

### `state_of_art.tex`

- `state_of_art.tex:6` [Try 80] motivate the design choices in Try~80: (i)~classical and empirical propagation
- `state_of_art.tex:9` [Try 80] modelling. A final section frames fair-comparison criteria and positions Try~80
- `state_of_art.tex:72` [Try 78] fitted to the CKM dataset (Try~78 of this thesis) achieves approximately
- `state_of_art.tex:120` [Try 78] validating the prior-subtraction philosophy of Try~78.
- `state_of_art.tex:134` [Try 79] and often include a spike near zero representing the dominant LoS path.  Try~79
- `state_of_art.tex:139` [Try 77] Tries~77 and~80.
- `state_of_art.tex:205` [Try 80] radio-map predictors, not as evidence that the Try~80 task is solved by those
- `state_of_art.tex:206` [Try 80] architectures.  In particular, Try~80 must predict over unseen real-city
- `state_of_art.tex:278` [Try 67] geometry-assisted CNN.  Try~67 of this thesis implements this channel through
- `state_of_art.tex:280` [Try 78, Try 80] alongside the topology map; the effect on the final Try~78--80 pipeline is
- `state_of_art.tex:292` [Try 67, Try 69] regulariser.  Tries~67--69 of this thesis implement a lightweight analogue:
- `state_of_art.tex:303` [Try 78] Try~78 implements this philosophy for path loss: an enhanced two-ray model fitted
- `state_of_art.tex:307` [Try 79] $\epsilon = y - \hat{y}_{\mathrm{PL}}$.  Try~79 extends the idea to delay spread
- `state_of_art.tex:309` [Try 80] TX-centred geometric features and local morphology statistics.  Try~80 unifies
- `state_of_art.tex:310` [Try 78] all three targets under a single shared network anchored to both Try~78 and
- `state_of_art.tex:311` [Try 79] Try~79 priors.
- `state_of_art.tex:329` [Try 79] Gaussian-like and additive-noise assumptions are better justified.  Try~79 adopts
- `state_of_art.tex:345` [Try 77] tail and is therefore a poor representative of either regime.  Try~77 addresses
- `state_of_art.tex:346` [Try 80] this with a Gaussian mixture model (GMM) distribution head, and Try~80
- `state_of_art.tex:347` [Try 79] incorporates the Try~79 log-domain ridge prior as an anchor before training the
- `state_of_art.tex:359` [Try 76] depends on what is being modelled.  The Try~76 histogram study selected the
- `state_of_art.tex:362` [Try 80] Try~80 uses three components for a different object: the residual distribution
- `state_of_art.tex:363` [Try 78, Try 79] after the frozen Try~78/Try~79 priors have already explained the dominant LoS,
- `state_of_art.tex:368` [Try 76, Try 77] motivates the Stage-A distribution head in Try~76 (for path loss), Try~77 (for
- `state_of_art.tex:369` [Try 80] spreads), and the lighter GMM-3 residual head carried into Try~80.
- `state_of_art.tex:387` [Try 71] overestimating uncertainty everywhere.  Try~71 of this thesis applies this
- `state_of_art.tex:404` [Try 76] Try~76 implements a two-stage architecture: Stage~A produces per-sample GMM
- `state_of_art.tex:414` [Try 77] Try~77 for delay and angular spread, with modified parameters for the
- `state_of_art.tex:441` [Try 80] Try~80 instantiates this idea explicitly: one shared encoder processes the
- `state_of_art.tex:459` [Try 67, Try 71] Tries~67--71 incorporate SWA starting from 60\,\% of the training budget.
- `state_of_art.tex:530` [Try 80] \textbf{Try~80 (this thesis)} & \textbf{Yes} & \textbf{Yes} & \textbf{Yes}
- `state_of_art.tex:566` [Try 80] The key lesson for Try~80 is not that the numerical RMSE should match
- `state_of_art.tex:570` [Try 80] conditions.  This supports the decision to report Try~80 under a strict
- `state_of_art.tex:590` [Try 80] ability to produce dense radio maps fast enough for planning loops.  Try~80 is
- `state_of_art.tex:610` [Try 66, Try 70] Try~66 through Try~70 implement only a weaker Tx-centred radial proxy of that
- `state_of_art.tex:611` [Try 78] idea.  Try~78 then solves the LoS part more cleanly with a two-ray radial prior,
- `state_of_art.tex:612` [Try 80] while Try~80 uses the calibrated prior as an input channel.  A full Gao-style
- `state_of_art.tex:631` [Try 80] under-test multi-transmitter or shifted building-density regimes.  Try~80 is
- `state_of_art.tex:650` [Try 66] The comparison to Try~66 should therefore be read as diagnostic rather than
- `state_of_art.tex:651` [Try 66] competitive.  Try~66's \SI{9.41}{dB} path-loss result is not claimed to beat
- `state_of_art.tex:653` [Try 78, Try 80] family had reached the same type of NLoS-dominated wall.  Try~78 and Try~80 were
- `state_of_art.tex:683` [Try 69, Try 71] 3 & Dual LoS/NLoS residual heads & Tries~69, 71 & Low \\
- `state_of_art.tex:733` [Try 78] Use the Try~78 LoS prior plus a calibrated NLoS morphology model. \\
- `state_of_art.tex:738` [Try 79] Use Try~79 log-domain ridge priors with topology, height, and LoS/NLoS regimes. \\
- `state_of_art.tex:743` [Try 80] Use a Try~80 prior-anchored residual GMM. \\
- `state_of_art.tex:759` [Try 80] Try~80 combines the pieces that survived those comparisons: calibrated priors,
- `state_of_art.tex:764` [Try 80] \section{Position of Try 80 in the literature}
- `state_of_art.tex:768` [Try 80] \subsection{What is novel about Try 80}
- `state_of_art.tex:770` [Try 80] Try~80 occupies a distinct and innovative position in the radio-map literature
- `state_of_art.tex:778` [Try 80] Try~80 transfers that principle to dense radio maps: the model first
- `state_of_art.tex:784` [Try 80] \item \textbf{Three simultaneous dense targets.}  Try~80 jointly predicts
- `state_of_art.tex:791` [Try 78] physics-based priors~--- the enhanced two-ray model (Try~78) for path
- `state_of_art.tex:792` [Try 79] loss and the log-space ridge regression (Try~79) for both spreads~--- are
- `state_of_art.tex:807` [Try 80] \subsection{What Try 80 does not claim}
- `state_of_art.tex:809` [Try 80] Try~80 does not claim to replace full ray-tracing in arbitrary scenarios.  The
- `state_of_art.tex:822` [Try 80] Try~80 is also not presented as a universal radio-map foundation model. It is a
- `state_of_art.tex:839` [Try 80] Table~\ref{tab:position} provides a compact summary of how Try~80 compares to
- `state_of_art.tex:845` [Try 80] \caption{Positioning of Try~80 against the most relevant published methods.}
- `state_of_art.tex:860` [Try 66] Try~66 (this thesis, single expert) & 9.41\,dB & Yes & Internal direct-regression baseline. \\
- `state_of_art.tex:861` [Try 78] Try~78 non-DL prior & 1.92\,dB overall; 1.75\,dB LoS & Yes & Frozen path-loss prior used by the final pipeline. \\
- `state_of_art.tex:862` [Try 80] \textbf{Try~80 (this thesis)} & \textbf{1.65\,dB on unseen test cities} & \textbf{Yes} & \textbf{Final prior-anchored residual model; also improves delay-spread and angular-spread RMSE over the frozen priors.} \\
- `state_of_art.tex:867` [Try 80] The Try~80 number in Table~\ref{tab:position} is the final frozen-checkpoint
- `state_of_art.tex:870` [Try 66, Try 71] direct-regression family of Tries~66--71, particularly in LoS-dominated

### `summary.tex`

- `summary.tex:16` [Try 78] convergeix en un model híbrid: priors interpretables calibrats per Try 78
- `summary.tex:18` [Try 79] Try 79 (regressió ridge en espai logarítmic per als dos spreads), amb un model
- `summary.tex:19` [Try 80] residual conjunt afegit a Try 80. El resultat final no és un prior pur ni una
- `summary.tex:20` [Try 80] xarxa neuronal pura: Try 80 introdueix Deep Learning com a corrector residual
- `summary.tex:25` [Try 80] ciutats de test. El checkpoint final de Try 80 refina aquests priors fins a
- `summary.tex:39` [Try 78] converge en un modelo híbrido: priors interpretables calibrados en Try 78
- `summary.tex:41` [Try 79] NLoS) y Try 79 (regresión ridge en espacio logarítmico para ambos spreads),
- `summary.tex:42` [Try 80] más un modelo residual conjunto en Try 80. El resultado final no es un prior
- `summary.tex:43` [Try 80] puro ni una red neuronal pura: Try 80 introduce Deep Learning como corrector
- `summary.tex:48` [Try 80] sobre las ciudades de test. El checkpoint final de Try 80 refina esos priors
- `summary.tex:62` [Try 78] calibrated interpretable priors from Try 78 (enhanced two-ray LoS model and
- `summary.tex:63` [Try 79] regime-wise NLoS calibration) and Try 79 (log-domain ridge regression for
- `summary.tex:64` [Try 80] both spreads), plus a joint residual model in Try 80. The final system is
- `summary.tex:65` [Try 80] neither a pure prior nor a pure neural network: Try 80 adds Deep Learning as a
- `summary.tex:70` [Try 80] RMSE on the held-out test cities. The final Try 80 checkpoint refines those

### `sustainability.tex`

- `sustainability.tex:39` [Try 80] work was electricity for computation. The final Try~80 line used four RTX~2080
- `sustainability.tex:41` [Try 76, Try 77] Tries~76 and 77 (the 12-expert distribution-first training) also used the
- `sustainability.tex:43` [Try 78] \SI{27}{kWh}. The non-deep-learning priors of Tries~78 and~79 do not need the
- `sustainability.tex:57` [Try 78, Try 79, Try 80] artifacts from Try 78 and Try 79 in Try 80, plotting from saved histories, and
- `sustainability.tex:103` [Try 80] GPU compute, final Try\,80         & 48\,GPU-h     & 0.25\,EUR/GPU-h  &    12\,EUR  & 4$\times$ RTX\,2080\,Ti, 12\,h \\
- `sustainability.tex:104` [Try 76, Try 79] GPU compute, Tries 76--79          & 72\,GPU-h     & 0.25\,EUR/GPU-h  &    18\,EUR  & 4$\times$ RTX\,2080\,Ti, 18\,h \\
- `sustainability.tex:158` [Try 80] performance without field measurements. The final Try 80 results are reported


