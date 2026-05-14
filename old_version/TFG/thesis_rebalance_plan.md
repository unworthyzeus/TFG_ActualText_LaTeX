# Thesis Rebalance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebalance the thesis so Methodology stays dominant but less overloaded, while State of the Art and Conclusions become slightly stronger and more defensible.

**Architecture:** Keep the advisor-approved shape: Methodology around 50%, Results around 20%, SoTA around 15%, Sustainability under 5%, and Conclusions closer to 5%. The work is mostly editorial: remove duplicated explanations from Methodology, move implementation-heavy detail to appendices where needed, and add targeted synthesis to SoTA and Conclusions.

**Tech Stack:** LaTeX thesis sources in `C:\TFG\FINAL_THESIS\TFG`, compiled with `latexmk -pdf -interaction=nonstopmode -halt-on-error TFG.tex`.

---

## Execution Result

Final compiled main-body balance, excluding preliminaries, bibliography, and appendices:

| Chapter | Final pages | Final share |
|---|---:|---:|
| Introduction | 5 | 4.5% |
| State of the Art | 17 | 15.5% |
| Methodology | 56 | 50.9% |
| Results | 23 | 20.9% |
| Sustainability | 4 | 3.6% |
| Conclusions | 5 | 4.5% |

The first two methodology reductions were enough. The last-resort Try 78/Try 79
feature-engineering moves and Try 80 FiLM/GMM diagram moves were not used.

---

## Current Balance and Target

Compiled main body, excluding preliminaries, bibliography, and appendices:

| Chapter | Current pages | Current share | Practical target | Action |
|---|---:|---:|---:|---|
| Introduction | 5 | 4.5% | 5% | Leave mostly unchanged. |
| State of the Art | 15 | 13.4% | 15-16% | Add 2-3 pages of synthesis, not random literature. |
| Methodology | 62 | 55.4% | about 50% | Remove or move 5-7 pages of duplicated/detail-heavy material. |
| Results | 23 | 20.5% | about 20% | Leave mostly unchanged unless a moved explanation fits better here. |
| Sustainability | 4 | 3.6% | max 5% | Leave unchanged. |
| Conclusions | 3 | 2.7% | 4-5% | Add 2-3 pages of final interpretation and lessons learned. |

The target is not the original 35/35 Method/Results split. After the advisor message, the better target is roughly **50/20** for Methodology/Results.

---

## Methodology Reductions: What to Remove or Move

The goal is not to make Methodology small. It should remain the thesis core. The goal is to remove repeated explanations and implementation-manual detail that distracts from the defended method.

### 1. Compress Section 3.10 Prior Overview

**File:** `C:\TFG\FINAL_THESIS\TFG\prior_detail_overview.tex`

**Current role:** This section bridges Try 78, Try 79, and Try 80 before the detailed subsections.

**Problem:** It repeats ideas that already appear in:

- `C:\TFG\FINAL_THESIS\TFG\methodology.tex`, Section 3.5, `Distribution-first modelling`
- `C:\TFG\FINAL_THESIS\TFG\prior_detail_try78.tex`, detailed Try 78 construction
- `C:\TFG\FINAL_THESIS\TFG\prior_detail_try79.tex`, detailed Try 79 construction
- `C:\TFG\FINAL_THESIS\TFG\prior_detail_try80.tex`, detailed Try 80 architecture
- `C:\TFG\FINAL_THESIS\TFG\state_of_art.tex`, Section 2.10, `Position of Try 80 in the literature`

**Remove or shorten:**

- Lines 102-399: `How to construct a good prior` is too long for a bridge section.
- Lines 146-250: old-prior mismatch and mismatch scope can become one concise paragraph plus one table row.
- Lines 251-366: LoS/NLoS changes repeat Try 78 details; keep only the final design rule.
- Lines 400-483: literature reuse repeats SoTA positioning; either shorten here or use it as material for SoTA expansion.

**Keep:**

- Lines 57-99: high-level architecture, but shorten to a half-page bridge.
- A compact table explaining: Try 78 gives path-loss prior, Try 79 gives spread priors, Try 80 learns bounded residuals.

**Expected saving:** 3-4 pages.

**Replacement text shape:**

```latex
Section~\ref{sec:try78_detail} and Section~\ref{sec:try79_detail} describe
the frozen priors used by Try~80. Their role is not to replace learning, but
to remove the part of the target that is already explained by calibrated
propagation structure. Try~80 then learns only bounded residual corrections
around these priors.
```

### 2. Remove Duplicate City-Holdout and Mask Explanations

**Files:**

- `C:\TFG\FINAL_THESIS\TFG\methodology.tex`
- `C:\TFG\FINAL_THESIS\TFG\prior_detail_try80.tex`
- `C:\TFG\FINAL_THESIS\TFG\results.tex`
- `C:\TFG\FINAL_THESIS\TFG\conclusions.tex`

**Problem:** City-holdout, ground-only masking, and LoS/NLoS reporting are explained many times.

**Rule:**

- Keep the full definition in `methodology.tex`, Section 3.1, `Dataset protocol`.
- In Try 80 details, replace repeated split/mask paragraphs with one sentence: "Try 80 uses the same city-holdout, ground-only, target-mask protocol defined in Section~\ref{sec:dataset_protocol}."
- In Results and Conclusions, mention the protocol only as evidence context, not as a full definition.

**Expected saving:** 0.5-1 page.

### 3. Shorten Section 3.7 Loss Functions

**File:** `C:\TFG\FINAL_THESIS\TFG\methodology.tex`

**Current range:** Lines 819-949, `Loss functions of the final pipeline`.

**Problem:** This overlaps strongly with `prior_detail_try80.tex`, lines 462-663, `Composite Optimization Objective`.

**Remove or shorten:**

- Lines 863-936: paragraph-by-paragraph definitions of NLL, KL, moment matching, anchor/guard, outlier budget, RMSE/MAE.

**Keep:**

- One compact equation for the composite loss.
- One paragraph explaining that the final path-loss fine-tune disables NLL, KL, moment matching, and outlier budget while keeping RMSE/MAE plus light anchor/guard.
- A pointer to Section 3.13 for the Try 80-specific version.

**Expected saving:** 1.5-2 pages.

### 4. Last-Resort Only: Compress Try 78 Calibration and Feature Engineering Detail

**File:** `C:\TFG\FINAL_THESIS\TFG\prior_detail_try78.tex`

**Activation condition:** Do this only if the safer Methodology reductions are
not enough after compiling and recounting pages. The safer reductions are:

- compressing `prior_detail_overview.tex`;
- shortening `methodology.tex`, Section 3.7, `Loss functions of the final pipeline`.

**Current heavy ranges:**

- Lines 390-605: LoS calibration procedure, grid search, smoothing, radial residual correction, fitted values.
- Lines 793-1118: NLoS morphology features and box-mean operators.
- Lines 1119-1257: regime-wise calibration details.

**Problem:** These sections read partly like implementation documentation. They are valuable, but not all of them need to sit in the main Methodology chapter.

**Remove or move to appendix:**

- Detailed box-mean/integral-image operator derivation.
- Full multiscale feature-by-feature prose for density, height, support, elevation, shadowing, and interaction terms.
- Long fitted-coefficient lists or search-range explanations.

**Keep in main Methodology:**

- The enhanced two-ray LoS model equation.
- The fact that LoS calibration is fitted only on training cities.
- One table of NLoS feature groups: raw propagation, distance/elevation, building density, building height, NLoS support, interaction terms.
- The final Try 78 result and why it becomes the path-loss anchor.

**Expected saving:** 2-4 pages, depending on how aggressive the appendix move is.

### 5. Last-Resort Only: Compress Try 79 Feature Definitions

**File:** `C:\TFG\FINAL_THESIS\TFG\prior_detail_try79.tex`

**Activation condition:** Do this only if the safer Methodology reductions are
not enough after compiling and recounting pages. Try 79 feature definitions
should stay in the main text if Methodology is already close to the target.

**Current heavy ranges:**

- Lines 83-240: 23-feature vector and feature-specific explanations.
- Lines 241-327: ridge regression, fallback hierarchy, inverse transform.

**Problem:** This repeats the same pattern as Try 78: many feature definitions are useful for reproducibility but too granular for the main narrative.

**Remove or move to appendix:**

- Per-feature derivations for blocker depth, transmitter clearance, taller-building fraction, and similar local morphology features.

**Keep in main Methodology:**

- Why log-domain modelling is used.
- The regime structure: metric, topology class, LoS/NLoS state, antenna-height bin.
- The ridge-regression objective.
- The fallback hierarchy in one short list.
- Final Try 79 results.

**Expected saving:** 1-2 pages.

### 6. Last-Resort Only: Keep One Try 80 Architecture Figure, Move Detailed Diagrams if Needed

**File:** `C:\TFG\FINAL_THESIS\TFG\prior_detail_try80.tex`

**Activation condition:** Do this only if the compiled PDF still feels
methodology-heavy after the safer reductions and after expanding SoTA and
Conclusions. Prefer keeping the diagrams in the main text unless the page
balance still clearly needs another cut.

**Current heavy ranges:**

- Lines 181-312: shared U-Net with FiLM and high-level architecture figure.
- Lines 315-392: detailed sinusoidal height-conditioning path.
- Lines 396-459: detailed prior-anchored GMM head.
- Lines 462-663: composite objective.

**Problem:** Three detailed architecture/loss diagrams in the main methodology may be more than needed once the text already explains the architecture.

**Remove or move to appendix:**

- Move the detailed FiLM path figure if the high-level architecture figure already communicates conditioning.
- Move the detailed GMM-head figure if the equations for residual assembly and mixture expectation remain.
- Keep the composite loss figure only if Section 3.7 is shortened; otherwise the loss material is duplicated.

**Keep in main Methodology:**

- One architecture figure.
- Equations for residual cap, prior-anchored mean, mixture expected value, and prior guard.
- Final fine-tuning distinction: same head, RMSE-dominant objective.

**Expected saving:** 1-3 pages.

### 7. Do Not Cut Section 3.9 Again

**File:** `C:\TFG\FINAL_THESIS\TFG\methodology.tex`

**Current range:** Lines 1006-1054, `Try 80 training progression`.

**Reason:** This section now directly answers the supervisor concern: Try 80 started with little improvement and then moved through big, big relaxed residuals, huge, and huge path-loss fine-tuning. It is short, non-duplicated, and should stay.

---

## Exact Duplication Themes to Eliminate

### Duplicate Theme A: "Try 80 Does Not Learn From Scratch"

**Currently appears in:**

- `methodology.tex`, Section 3.9
- `prior_detail_overview.tex`, high-level architecture
- `prior_detail_try80.tex`, experimental protocol and residual model
- `state_of_art.tex`, Section 2.10
- `conclusions.tex`, RQ2 answer

**Final allocation:**

- Full technical explanation: `prior_detail_try80.tex`
- Literature framing: `state_of_art.tex`
- Final takeaway: `conclusions.tex`
- Short bridge only: `prior_detail_overview.tex`

### Duplicate Theme B: "Distribution-First Modelling Fixed Mode Collapse"

**Currently appears in:**

- `methodology.tex`, Section 3.5
- `methodology.tex`, Section 3.6
- `state_of_art.tex`, Sections 2.5 and 2.6
- `results.tex`, Try 76 interpretation
- `conclusions.tex`, contributions and negative results

**Final allocation:**

- Main explanation: `methodology.tex`, Section 3.5
- Literature support: `state_of_art.tex`, Sections 2.5-2.6
- Evidence: `results.tex`
- Short lesson learned: `conclusions.tex`

### Duplicate Theme C: "City-Holdout and Ground-Only Metrics"

**Currently appears in:**

- `methodology.tex`, Section 3.1
- `prior_detail_try80.tex`, protocol subsection
- `results.tex`, opening paragraphs and tables
- `conclusions.tex`, RQ1 and contributions

**Final allocation:**

- Full definition: `methodology.tex`, Section 3.1
- Evidence context only: `results.tex`
- Final claim qualifier only: `conclusions.tex`

### Duplicate Theme D: "Loss Terms"

**Currently appears in:**

- `methodology.tex`, Section 3.7
- `prior_detail_try80.tex`, `Composite Optimization Objective`
- `methodology.tex`, Section 3.9

**Final allocation:**

- General loss family overview: `methodology.tex`, Section 3.7
- Exact Try 80 objective and final fine-tune setting: `prior_detail_try80.tex`
- Training-path explanation: `methodology.tex`, Section 3.9

---

## State of the Art Expansion: Exact Additions

Add 2-3 pages total. Do not add unrelated papers unless needed. Use synthesis tables and paragraphs that connect literature to thesis design.

### Expansion 1: Add a Design-Gap Synthesis Table

**File:** `C:\TFG\FINAL_THESIS\TFG\state_of_art.tex`

**Location:** After Section 2.9, `Emerging techniques for closing the NLoS gap`, before Section 2.10, `Position of Try 80 in the literature`.

**New subsection title:**

```latex
\subsection{Synthesis: literature gaps mapped to thesis decisions}
```

**Exact content to add:**

A table with these rows:

| Literature family | What it contributes | Remaining gap for this thesis | Thesis response |
|---|---|---|---|
| U-Net / pix2pix / cGAN radio-map predictors | Dense image-to-image mapping | Visual plausibility can hide physical RMSE and NLoS tail errors | Ground-only physical metrics, LoS/NLoS reporting, rejected visual realism as primary objective |
| PMNet / PMHHNet-style radio-map backbones | Good spatial inductive bias and multi-scale context | Mostly single-target or benchmark-specific; does not solve target-distribution mismatch | Distribution-first heads, GMM marginals, regime diagnostics |
| Classical propagation and two-ray models | Strong LoS path-loss structure | Weak for blocked urban NLoS and spread targets | Try 78 LoS prior plus calibrated NLoS morphology model |
| Empirical spread models | Log-domain and regime-dependent spread statistics | Usually not dense pixel maps with building morphology | Try 79 log-domain ridge priors with topology, height, and LoS/NLoS regimes |
| Heteroscedastic / GMM / uncertainty heads | Captures multi-modal or heavy-tailed targets | Often not anchored to physical priors | Try 80 prior-anchored residual GMM |
| AIRMap / PathFinder / adaptive methods | Fast inference or domain-shift focus | Different task assumptions and benchmark contracts | Fair-comparison protocol and city-holdout interpretation |

**Expected gain:** About 1 page.

### Expansion 2: Strengthen "What Try 80 Does Not Claim"

**File:** `C:\TFG\FINAL_THESIS\TFG\state_of_art.tex`

**Current location:** Section 2.10.2, lines 723-737.

**Add exactly:**

- One paragraph explaining that Try 80 is not a universal radio-map foundation model.
- One paragraph explaining that the result is strongest as a controlled CKM result: fixed simulator family, fixed output definitions, strict unseen-city split.
- One paragraph explaining why this makes the comparison more honest, not weaker.

**Key wording to include:**

```latex
This limitation is also what makes the result interpretable: the thesis does
not claim a universal surrogate for all propagation environments, but a
carefully audited CKM predictor under a known dataset contract.
```

**Expected gain:** 0.5-0.75 page.

### Expansion 3: Add a Short Paragraph to the Benchmark Section

**File:** `C:\TFG\FINAL_THESIS\TFG\state_of_art.tex`

**Location:** Section 2.8, after the fair-comparison checklist.

**Add exactly:**

- A paragraph explaining why method rankings change when evaluation switches from random maps to city holdout.
- A paragraph explaining why path loss, delay spread, and angular spread should not be compared as if they were the same difficulty.

**Expected gain:** 0.5 page.

---

## Conclusions Expansion: Exact Additions

Add 2-3 pages total. The conclusion should feel more confident, not longer for its own sake.

### Expansion 1: Add "What the Final Result Means"

**File:** `C:\TFG\FINAL_THESIS\TFG\conclusions.tex`

**Location:** After the opening numerical paragraph, before `Answers to the research questions`.

**New subsection title:**

```latex
\subsection{What the final result means}
```

**Exact points to cover:**

1. Path loss: Try 80 reaching about 1.65 dB means the combination of prior plus residual correction is operating near the useful precision limit for this dataset, especially because Try 78 already reaches 1.92 dB.
2. Delay and angular spread: improvements are smaller but meaningful because these targets are more distributional and less deterministic than LoS path loss.
3. The final model is not a pure neural victory; it is evidence that calibrated priors and bounded residual learning are the right split of responsibility.

**Expected gain:** 0.75-1 page.

### Expansion 2: Add a Lessons-Learned Table

**File:** `C:\TFG\FINAL_THESIS\TFG\conclusions.tex`

**Location:** After `Negative results`, before `Future Directions`.

**New subsection title:**

```latex
\subsection{Lessons learned across the development path}
```

**Exact table rows:**

| Phase | What seemed promising | What failed | What survived |
|---|---|---|---|
| U-Net and cGAN | Direct dense map synthesis | Visual quality did not imply physical accuracy | Ground-only physical metrics |
| Masked baselines | Cleaner supervision | Still weak on NLoS and tails | Explicit masks and LoS/NLoS reporting |
| PMNet / PMHHNet | Better spatial backbone and physical channels | Point regression collapsed distributions | Height conditioning, physical channels, regime metrics |
| Distribution-first models | GMM target modelling | Not enough alone for all targets | Target-shape diagnosis and mixture heads |
| Try 78 / Try 79 priors | Strong calibrated structure | Not a complete model for every pixel and target | Frozen anchors |
| Try 80 | Joint residual correction | Needed relaxed caps and RMSE-dominant fine-tune | Final prior-anchored residual design |

**Expected gain:** 1 page.

### Expansion 3: Make Future Work More Structured

**File:** `C:\TFG\FINAL_THESIS\TFG\conclusions.tex`

**Current location:** Section `Future Directions`, lines 89-end.

**Replace the current three paragraphs with three subparagraphs:**

```latex
\paragraph{Short-term.}
Improve final Try~80 reporting with more seeds, calibration curves, uncertainty
diagnostics, and additional held-out city groupings.

\paragraph{Medium-term.}
Add frequency, bandwidth, antenna pattern, and polarization conditioning so the
model is no longer tied to one radio configuration.

\paragraph{Long-term.}
Move from simulator-only CKM prediction to field-calibrated deployment, where a
small number of measurements adapts the priors and residual model to real
environments.
```

**Expected gain:** 0.5-0.75 page.

---

## Implementation Order

### Task 1: Add SoTA synthesis first

**Modify:** `C:\TFG\FINAL_THESIS\TFG\state_of_art.tex`

- [x] Add the design-gap synthesis table after Section 2.9.
- [x] Expand `What Try 80 does not claim`.
- [x] Add the benchmark fairness paragraphs.
- [x] Compile with `latexmk -pdf -interaction=nonstopmode -halt-on-error TFG.tex`.

### Task 2: Expand Conclusions

**Modify:** `C:\TFG\FINAL_THESIS\TFG\conclusions.tex`

- [x] Add `What the final result means`.
- [x] Add `Lessons learned across the development path`.
- [x] Add practical implications and scope to bring Conclusions closer to target.
- [x] Restructure `Future Directions` into short-term, medium-term, and long-term.
- [x] Compile with `latexmk -pdf -interaction=nonstopmode -halt-on-error TFG.tex`.

### Task 3: Reduce Methodology without weakening it

**Modify:**

- `C:\TFG\FINAL_THESIS\TFG\methodology.tex`
- `C:\TFG\FINAL_THESIS\TFG\prior_detail_overview.tex`
- `C:\TFG\FINAL_THESIS\TFG\prior_detail_try78.tex`
- `C:\TFG\FINAL_THESIS\TFG\prior_detail_try79.tex`
- `C:\TFG\FINAL_THESIS\TFG\prior_detail_try80.tex`
- possibly `C:\TFG\FINAL_THESIS\TFG\appendices.tex`

- [x] Compress `prior_detail_overview.tex` first; this is the safest 3-4 page reduction.
- [x] Shorten `methodology.tex` Section 3.7 loss function prose and point to Try 80 details.
- [x] Recompile and recount pages before touching Try 78/Try 79 feature engineering or Try 80 diagrams.
- [x] Confirm no need to move or compress Try 78/Try 79 feature engineering details after the first two reductions.
- [x] Confirm no need to move detailed Try 80 FiLM/GMM diagrams after the page recount.
- [x] Compile with `latexmk -pdf -interaction=nonstopmode -halt-on-error TFG.tex`.

### Task 4: Recompute chapter balance

**Files to inspect:**

- `C:\TFG\FINAL_THESIS\TFG\TFG.toc`
- `C:\TFG\FINAL_THESIS\TFG\TFG.pdf`

- [x] Count chapter page spans from the table of contents.
- [x] Confirm Methodology is around 50%, Results around 20%, SoTA around 15%, Conclusions around 4-5%.
- [x] Do not overcut Methodology below 48%; the advisor explicitly accepted a methodology-heavy thesis.

---

## Stop Conditions

Stop editing when these are true:

- Methodology is about 50% of main body pages.
- Results remain about 20%.
- SoTA is at least 15% or clearly close.
- Conclusions are at least 4% and feel complete.
- No thesis section references repository paths or internal script locations unless the section is explicitly an appendix about reproducibility tooling.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error TFG.tex` completes successfully.
