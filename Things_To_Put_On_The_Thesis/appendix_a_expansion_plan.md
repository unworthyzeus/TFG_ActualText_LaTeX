# Appendix A Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand Appendix A so every numbered Try used in the thesis is mapped to a public definition, and the attempt history becomes a fuller technical timeline rather than a short summary.

**Architecture:** Appendix A remains the audit trail, while the main chapters stay compact. The appendix should start with a try-number map, then give a phase-by-phase chronology that explains what changed, why it changed, and which lesson survived into Try 78, Try 79, or Try 80.

**Tech Stack:** LaTeX `report` document, existing `tabularx` and `booktabs` table style, `siunitx` for units, no new package unless the table becomes impossible to lay out cleanly.

---

## Files

- Modify: `C:\TFG\FINAL_THESIS\TFG\appendices.tex`
- Reference: `C:\TFG\FINAL_THESIS\TFG\methodology.tex`
- Reference: `C:\TFG\FINAL_THESIS\TFG\results.tex`
- Reference: `C:\TFG\FINAL_THESIS\TFG\try_mentions_inventory_and_edit_plan.md`

Do not edit `methodology.tex` or `results.tex` for this task unless a cross-reference is clearly broken after Appendix A is expanded.

## Placement

Appendix A is the first chapter in `appendices.tex`:

```latex
\chapter{Detailed Attempt Log}
```

Insert the new material directly after the opening paragraph at `appendices.tex:3-6`, before the current `\section{Early image-to-image phase}`.

Target structure:

```latex
\chapter{Detailed Attempt Log}

opening paragraph

\section{How to read the attempt numbers}
\section{Try-number map}
\section{Expanded chronological timeline}
  \subsection{Early image-to-image baselines}
  \subsection{Geometry conditioning and artifact control}
  \subsection{Masking and evaluation contract}
  \subsection{Prior-guided residual learning}
  \subsection{PMHHNet and expert-routing phase}
  \subsection{Distribution-first diagnosis}
  \subsection{Frozen calibrated priors}
  \subsection{Final prior-anchored residual GMM model}
```

The current four sections can be reused, but their content should be expanded and reorganized under the structure above.

## Editorial Rules

- Appendix A may use internal Try numbers because its purpose is the audit trail.
- Every numbered Try from 1 to 80 should be mapped, even if some are mapped as small internal pivots rather than individually claimed results.
- Each row should name at least one distinguishing technical knob: data contract, target, prior, routing, architecture, loss, resolution, training schedule, diagnostic purpose, or outcome. Avoid repeating the same generic label for adjacent tries.
- If evidence for a row is thin, mark it as a provisional internal pivot, but still state how it differs from neighbouring attempts and verify before final LaTeX implementation.
- Do not put repository paths, script names, or checkpoint names in Appendix A unless they are needed for reproducibility and are already discussed in the implementation appendix.
- Keep exact headline metrics only where the thesis already uses them: Try 22, Try 41, Try 42, Try 44, Try 49, Try 50, Try 66, Try 76, Try 77, Try 78, Try 79, and Try 80.
- Preserve the taxonomy correction: Try 78 final path-loss calibration has 18 regimes; Try 79 has 36 exact regimes per metric, 72 exact total, and 114 keys including fallbacks.
- Name Try 80 as a "joint prior-anchored residual GMM model" in Appendix A.

## Proposed Intro Text

Add this after the current opening paragraph:

```latex
The attempt numbers are internal experiment identifiers. They are kept here
because they make the development path auditable, but they should not be read
as eighty independent thesis contributions. Many intermediate runs tested one
small change inside a larger phase. The table below maps each number to the
public technical role it plays in the thesis narrative.
```

## Try-Number Map To Add

Implement as several small `tabularx` tables rather than one very long float. This avoids adding a new `longtable` dependency and keeps page breaks manageable.

### Table A.1a: Early Image Regression And Geometry Conditioning

| Try | Public definition for Appendix A |
| --- | --- |
| 1 | Initial U-Net / pix2pix-style cGAN proof of concept for aligned CKM image-to-image regression. |
| 2 | Linear-scale path-loss training variant: physical normalization, dual dB/linear reporting, and optional distance-from-centre channel. |
| 3 | Hybrid path-loss branch on the early U-Net/cGAN base: coarse path-loss head, confidence head, saturation masking, and fused evaluation/export. |
| 4 | Differentiable fused-map path-loss objective in dB, turning the hybrid branch into the optimized prediction rather than only an export. |
| 5 | TinyGAN / BatchNorm / low-resolution discriminator stabilization run for the early cGAN family. |
| 6 | Second early cGAN stabilization run, keeping the TinyGAN-style low-resolution discriminator while checking repeatability. |
| 7 | Additional cluster replication of the low-resolution-discriminator cGAN baseline before changing the physical inputs. |
| 8 | Final early image-to-image baseline before explicit height and visibility conditioning became central. |
| 9 | First explicit UAV-height conditioning run, introducing FiLM-style height modulation beside the older image-to-image baseline. |
| 10 | LoS/NLoS split path-loss run, comparing visibility-specific training with and without height conditioning. |
| 11 | Follow-up height/visibility conditioning pivot, used to separate geometry information from pure adversarial image translation. |
| 12 | Late geometry-conditioning continuation before committing to FiLM-specialized LoS/NLoS branches. |
| 13 | FiLM-only cGAN variant, isolating height modulation without the full visibility-specialized split. |
| 14 | Separate LoS-FiLM and NLoS-FiLM branches; last geometry-conditioning run before artifact-control work. |
| 15 | Start of artifact-control phase: GroupNorm, distance features, weaker GAN pressure, and smoothing-oriented variants. |
| 16 | Artifact-control continuation focused on keeping the U-Net/cGAN structure while tuning normalization and distance features. |
| 17 | Training-stability artifact run before the decoder was changed, mainly testing whether artifacts came from optimization rather than architecture. |
| 18 | Late artifact-control branch with blended outputs and cluster experiment bookkeeping; still pre-decoder-fix. |
| 19 | Final artifact-control run before replacing the decoder path with explicit bilinear and multiscale tests. |
| 20 | Bilinear decoder change; reduced checkerboard artifacts. |
| 21 | Multiscale supervision change; improved large-scale field learning. |
| 22 | Combined bilinear decoder and multiscale supervision; strongest clean pre-prior baseline. |

### Table A.1b: Spread Branches, Masks, And First Priors

| Try | Public definition for Appendix A |
| --- | --- |
| 23 | Delay/angular multiscale branch, transferring the Try 21--22 multiscale idea to spread-related targets. |
| 24 | Intermediate spread-branch continuation before attention was added; kept as a provisional internal pivot. |
| 25 | Bottleneck-attention spread/path-loss branch, testing whether global context in the compressed representation helped. |
| 26 | Delay/angular gradient target/loss run, making spread prediction more sensitive to spatial change rather than only absolute value. |
| 27 | Intermediate spread/prior exploratory run before topology attention; kept as a provisional internal pivot. |
| 28 | Topology-attention variant, using environment class information more directly in the spread/path-loss branch. |
| 29 | Radial path-loss objective variant, testing whether distance-structured supervision reduced physically implausible maps. |
| 30 | Spread-priority objective, deliberately weighting delay/angular-spread behaviour more heavily than the path-loss baseline. |
| 31 | Prior-residual path-loss branch, early move from direct image regression toward learning corrections over a physical estimate. |
| 32 | Support-amplitude spread decomposition, last spread/prior exploratory run before the ground-mask contract changed. |
| 33 | Ground-only receiver mask becomes mandatory; building pixels are excluded from loss and metrics. |
| 34 | Restart under the corrected ground-mask evaluation contract, used to make post-mask scores comparable. |
| 35 | Spread-plus-building-mask run, applying the corrected receiver mask to spread-oriented learning. |
| 36 | Second spread-building-mask run, checking whether the masked spread branch was stable across reruns. |
| 37 | Building-mask path-loss rerun, returning the corrected receiver contract to path-loss prediction. |
| 38 | Hybrid two-ray prior input run, injecting a physical propagation prior as an input channel rather than only a loss/metric. |
| 39 | Building-mask continuation before Try 40; provisional internal pivot for masked evaluation and spread/path-loss balance. |
| 40 | Spread-building-mask consolidation, final masked-evaluation run before explicit prior-residual learning. |

### Table A.1c: Prior-Residual And PMNet-Style Phase

| Try | Public definition for Appendix A |
| --- | --- |
| 41 | Explicit physical-prior plus learned-residual formulation; raw prior and train-only calibrated prior were diagnosed. |
| 42 | PMNet-style residual regressor; improved over prior-only calibration but NLoS remained dominant. |
| 43 | PMNet no-prior direct-control run, testing how much of the result came from the learned network without a physical residual anchor. |
| 44 | No-prior PMNet-v3-style control; showed that LoS could be learned but NLoS remained weak. |
| 45 | PMNet residual run tied to the formal prior formulas and calibration notes; bridge between simple prior residuals and MoE routing. |
| 46 | LoS/NLoS mixture-of-experts prior run, splitting the residual learner by visibility regime. |
| 47 | U-Net prior-residual MoE with obstruction-feature precomputation and calibration, replacing the PMNet-only route. |
| 48 | Warm-started Try 42 branch with widened 96-channel PMNet and stage-2 refinement chains. |
| 49 | PMNet stage-1 w112 prior branch with MAE-dominant ablation and tail-refiner stage 2; reduced average error but left hard NLoS tails. |
| 50 | Prior-research/NLoS sandbox with formula-only, hybrid, HGBoost, tabular, and MLP-delta variants; confirmed scalar corrections over LoS-shaped priors were insufficient. |

### Table A.1d: PMHHNet, Regularization, And Distribution Diagnosis

| Try | Public definition for Appendix A |
| --- | --- |
| 51 | Literature-backed PMNet prior stage-1, using a wider w112 branch and a stage-2 tail refiner. |
| 52 | Paper-routed city-type-aware PMNet branch: 112 channels, three city-type NLoS experts, automatic city-type routing, and a Try 52 teacher refiner. |
| 53 | Literature/cyclic PMNet branch with stage-2 teacher refinement and an added stage-3 NLoS global-context cyclic refiner. |
| 54 | First full partitioned-expert PMHHNet branch: six topology experts, topology classifier, continuous height conditioning, and no-data head. |
| 55 | Same partitioned PMHHNet layout as Try 54, but with the objective changed toward final-map RMSE plus auxiliary no-data loss and EMA. |
| 56 | Try 26 U-Net family converted into six topology experts, with topology-mask input, no-data output, and stronger configurable dropout. |
| 57 | Partitioned PMHHNet final-map-RMSE branch deployed across the six topology experts after the Try 54--55 objective change. |
| 58 | Try 26 topology-expert generator-only profile: topology mask, no-data BCE head, stronger dropout, AdamW/EMA defaults, and rewind-to-best. |
| 59 | Second Try 26 topology-expert generator-only pass under the Try 59 branch, later kept as a separate spread/prior source rather than merged with Try 58. |
| 60 | No-prior ablation of the Try 57 family: direct path-loss prediction from topology, LoS, distance, and height without formula/confidence prior channels. |
| 61 | No-prior NLoS-focused objective: strong LoS/NLoS reweighting, explicit NLoS term, composite checkpoint, and open-sparse-vertical split into LoS/NLoS experts. |
| 62 | Paper-like reset after Try 61: restored formula prior, added obstruction proxy channels, removed manual NLoS/no-data losses, and used a stage-2 refiner. |
| 63 | Coarse-to-fine Try 62 follow-up: cheap 128x128 stage 1 plus full 513x513 stage 2, with obstruction proxies still enabled. |
| 64 | Coarse-to-fine Try 63 follow-up with obstruction proxies disabled, isolating resolution/refinement from explicit blocker features. |
| 65 | Grokking-style stress test: single-stage 513 training, no early stopping, no rewind, no stage 2, high constant LR/weight decay, and very long horizon. |
| 66 | Consolidated PMHHNet reference: continuous multi-altitude prediction, sinusoidal height embedding into FiLM, physical channels, and topology experts; LoS was reasonable, but NLoS remained the bottleneck. |
| 67 | Try 66-family geometry-assisted pivot with knife-edge/physical-channel ideas; start of the late stabilization and diagnostic phase. |
| 68 | Try 66 rerun with PMHHNet stem, high-frequency-path fix, and CutMix removed when height FiLM was active. |
| 69 | Knife-edge and LoS/NLoS residual diagnostic with dense/mixed/open macro experts plus legacy sparse expert variants. |
| 70 | Try 68 PMHHNet with multi-scale quad residual heads at 513, 257, 129, and 65 grids. |
| 71 | Heteroscedastic uncertainty diagnostic; identified hard pixels but did not solve the map error. |
| 72 | Try 70-era open-sparse-lowrise expert continuation, checking whether the multi-scale PMHHNet refinements transferred to the hardest low-rise sparse regime. |
| 73 | Open-sparse-lowrise plus open-sparse-vertical continuation, broadening the Try 72 late-PMHHNet diagnostic to vertical sparse cases. |
| 74 | Band-45--55 all-city LoS/NLoS histogram experts, used to expose distribution mismatch and high-tail underprediction. |
| 75 | All-city small-LoS expert and decisive histogram diagnosis: NLoS path loss and spread tails required distribution-aware modelling. |

### Table A.1e: Final Distribution, Prior, And Joint Model Phase

| Try | Public definition for Appendix A |
| --- | --- |
| 76 | Distribution-first GMM path-loss architecture: sample-level mixture estimation plus pixel assignment. |
| 77 | Distribution-first spread architecture: delay/angular spread GMM or spike-plus-tail modelling. |
| 78 | Final non-DL path-loss prior: enhanced two-ray LoS branch plus regime-wise linear NLoS calibration with 18 final calibration regimes. |
| 79 | Final non-DL spread priors: log-domain ridge calibration for delay and angular spread, with 36 exact regimes per metric and fallbacks. |
| 80 | Final joint prior-anchored residual GMM model: frozen Try 78/79 priors plus a shared neural residual model selected through Big -> Big relaxed residuals -> Huge -> Huge path-loss fine-tuning. |

## Expanded Timeline Content

Appendix A should not be just a table. After the map, expand the timeline with concise subsections:

1. **Early image-to-image baselines**
   Explain Try 1--8 as the starting point: aligned CKM image translation was feasible, but adversarial texture was not aligned with physical RMSE.

2. **Geometry conditioning and artifact control**
   Explain Try 9--22: height, LoS/NLoS diagnosis, GroupNorm, distance maps, bilinear decoding, and multiscale supervision. Keep Try 22 as the named baseline.

3. **Masking and evaluation contract**
   Explain Try 33--40: building pixels were invalid receiver locations, so the metric contract changed. This section should make clear why older numbers are not strict leaderboards.

4. **Prior-guided residual learning**
   Explain Try 41--50: raw physical priors were too crude, calibration helped, residual learning helped, but NLoS tails remained unsolved.

5. **PMHHNet and expert-routing phase**
   Explain Try 51--66: PMHHNet, physical channels, height FiLM, topology experts, and the key Try 66 result.

6. **Regularization and distribution diagnosis**
   Explain Try 67--75: SWA/EMA/CutMix/uncertainty-style refinements were useful diagnostics but not the solution; histogram analysis made the distribution mismatch visible.

7. **Distribution-first modelling**
   Explain Try 76 and Try 77: Stage A estimates distribution/modes; Stage B places pixels or spread structure. This is the main conceptual bridge to GMM heads.

8. **Frozen calibrated priors**
   Explain Try 78 and Try 79: Try 78 solves path loss with a calibrated prior; Try 79 solves spread baselines with log-domain ridge calibration.

9. **Final joint prior-anchored residual GMM model**
   Explain Try 80: starts with little improvement, then follows Big -> Big relaxed residuals -> Huge -> Huge path-loss fine-tune. Emphasize that the GMM head remains part of the final residual output, even when the final checkpoint is selected by deterministic RMSE.

## Concrete Editing Tasks

### Task 1: Add The Try-Number Map

- [ ] Insert `\section{How to read the attempt numbers}` after the Appendix A opening paragraph.
- [ ] Add the proposed intro text.
- [ ] Add `\section{Try-number map}`.
- [ ] Convert the five map tables above into LaTeX `tabularx` tables.
- [ ] Use `\scriptsize` and compact columns: `p{0.11\textwidth}` for the Try number and `X` for the definition.
- [ ] Keep table captions short, for example `Try-number map, early image-regression phase`.

### Task 2: Expand The Timeline

- [ ] Replace the current four short sections in Appendix A with the nine timeline subsections listed above.
- [ ] Reuse current text where it is already good, especially the Try 41, Try 66, Try 76, Try 78, Try 79, and Try 80 paragraphs.
- [ ] Add one or two sentences per phase that explain why the phase ended, while preserving the per-try distinctions in the map.
- [ ] Keep the appendix operational but not repository-specific.

### Task 3: Cross-Reference Main Text

- [ ] Add a sentence at the end of the try-number map: "The main chapters use only the attempts that carry a methodological or quantitative claim; this appendix keeps the full numbering context."
- [ ] In Appendix A, refer readers to Methodology for equations and Results for metric tables rather than repeating full derivations.
- [ ] Do not duplicate the Try 78/79 formulas here.

### Task 4: Verify

- [ ] Run `latexmk -pdf -interaction=nonstopmode -halt-on-error TFG.tex` from `C:\TFG\FINAL_THESIS\TFG`.
- [ ] Check the Appendix A pages in the PDF for table overflow.
- [ ] Check the table of contents to confirm Appendix A remains readable.
- [ ] Search the compiled log for new overfull boxes introduced by the map tables.

## Acceptance Criteria

- Appendix A contains an explicit definition map for every Try number 1--80.
- Appendix A gives every Try a distinct role, even when the role is only a small pivot inside a larger phase.
- Try 80 is named as a joint prior-anchored residual GMM model.
- The main-body Methodology can stay shorter because the detailed attempt chronology now has a proper home.
- The thesis compiles successfully.
