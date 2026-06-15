# Exact Implementation Plan for Sergi and Evgenii Comments

Source comment files:

1. `C:/Users/guill/Downloads/TFG_draft_21may_GV--SA.pdf`
2. `reduced/TFG/supervisor_comments_sergi_pending.md`
3. `reduced/TFG/supervisor_comments_checklist.md`
4. `reduced/TFG/supervisor_comments_reduced.md`
5. `reduced/TFG/supervisor_comments_exact_fix_plan.md`
6. `reduced/TFG/supervisor_comments_overview_meeting.md`
7. `reduced/TFG/supervisor_comments_overview_implementation.md`

Scope of this plan: reduced thesis source under `reduced/TFG`. The paper
version should be updated only after this pass is stable, because most comments
concern thesis structure rather than paper length.

Core rule for all edits: the main thesis must explain the final method first.
The development path, failed branches, and negative results belong in the
appendix unless they are needed in one or two sentences to justify a final
design choice.

## Current Pending Comment Map

### Sergi comments still requiring work

1. Add an appendix declaration about generative AI use.
2. Reduce the cognitive load at the start of the thesis.
3. Remove or shrink the introduction "Methods and procedures" section.
4. Make Chapter 3 visibly structured around the final pipeline.
5. Add a high level methodology block diagram.
6. Make Chapter 2 easier to navigate and clearly separate background from
   state of the art.
7. Keep Chapter 4 focused on final results, baselines, and previous papers.
8. Add one representative qualitative panel to Results if it is central
   evidence, while keeping the full gallery in the appendix.
9. Expand the sustainability economic impact discussion.
10. Audit bibliography entries that still cite arXiv when a published version
    may exist.
11. Run a global terminology, acronym, equation reference, and precision pass.
12. Clarify that delay spread and angular spread are evaluated against their
    ray-traced ground truth values on the same valid ground receiver pixels as
    channel attenuation.

### Evgenii comments still relevant after previous fixes

The old Evgenii checklist is mostly marked as fixed, but several items remain
relevant because Sergi raised the same structural concern on the newer commented
PDF:

1. Chapter 2 should be background and literature only, not a place for thesis
   result claims.
2. Chapter 3 should focus on the final model and final reproducibility
   contract, not on old attempts.
3. Chapter 4 should report final results first and compare them with previous
   work.
4. Negative results and old branches are valuable, but should be moved to
   appendices.
5. The reduced thesis should become shorter where the main text repeats details
   already present in the appendix or in dedicated prior detail files.

## Implementation Order

1. Add the generative AI appendix declaration.
2. Remove the introduction method section or reduce it to one transition
   paragraph.
3. Restructure Chapter 3 and add the high level block diagram.
4. Clean Chapter 2 around a reader map, simpler precision, and background only
   wording.
5. Clean Chapter 4 so it does not read like development history.
6. Clarify the spread evaluation contract in Methodology and Results.
7. Add the sustainability economic impact paragraph.
8. Run the global mechanical audits.
9. Compile and check the PDF.

## Task 1: Add Generative AI Declaration Appendix

### File

`reduced/TFG/appendices_compact.tex`

### Current anchor

Append at the very end of the file, after the current final `\endgroup` of
Appendix D.

### Exact edit

Add this new appendix chapter:

```latex
\chapter{Declaration on Generative AI Use}
\label{app:generative_ai_declaration}

Generative AI tools were used during the preparation of this thesis as writing
and coding assistance tools. Their role was limited to support tasks such as
summarising supervisor comments, proposing alternative wording, checking
internal consistency, drafting edit plans, assisting with LaTeX and Python code,
and helping identify possible terminology or structure problems.

The scientific content, experimental design, final reported numbers, plots,
tables, conclusions and responsibility for the submitted document remain with
the author. Numerical results were obtained from the project scripts, stored
artifacts and compiled thesis sources, not from generative model outputs.
References, equations, code changes and final text were reviewed by the author
before inclusion.

No confidential data beyond the local thesis files and project artifacts was
intentionally provided to generative AI tools. The CKM dataset itself was used
through local scripts and stored experiment outputs.
```

### Author confirmation needed before final compile

Before implementation, confirm whether the declaration should name specific
tools, for example ChatGPT, Codex, GitHub Copilot, Grammarly, or similar. If
the university expects named tools, replace the first sentence with:

```latex
Generative AI tools, including [tool names to confirm], were used during the
preparation of this thesis as writing and coding assistance tools.
```

## Task 2: Remove or Shrink Introduction Methods Section

### File

`reduced/TFG/introduction.tex`

### Current anchors

1. `\section{Methods and procedures}` starts at current line 177.
2. `\section{Work plan}` starts at current line 193.

### Sergi comment covered

Old PDF page 18: "I don't think this chapter belongs here anymore. You have a
complete chapter on methods... I would remove..."

### Exact edit

Delete this whole block:

```latex
\section{Methods and procedures}

The final method follows a hybrid pipeline. First, the city map is represented
as a building-height raster with a centred UAV transmitter and a fixed
ground user receiver grid. Second, geometric LoS/NLoS masks and calibrated
priors are prepared for channel attenuation, delay spread, and angular spread. Third,
\textsc{HARP-Net CKM} receives the topology, masks, UAV height, and prior maps
and predicts bounded residual corrections for the three outputs. The final maps
are the prior predictions plus the learned residual corrections.

Earlier neural models are still useful scientifically, but mainly as
diagnostics. They showed that direct image to image prediction can produce
plausible-looking maps while missing NLoS and spread tail behaviour. For this
reason the main text presents the final method first; the chronological attempt
trace is kept in the appendix.
```

Do not add a replacement section. Chapter 3 already explains the method. The
Chapter 1 outline already tells the reader where to find it.

### Optional small replacement inside thesis outline

If the deletion makes the transition too abrupt, add one sentence at the end of
the Chapter 3 outline sentence, not as a separate section:

```latex
The method chapter is intentionally final-pipeline first; the chronological
attempt trace is kept in Appendix~A.
```

## Task 3: Rewrite the Opening of Chapter 3

### File

`reduced/TFG/methodology.tex`

### Current anchor

Lines 3 to 11, immediately after:

```latex
\chapter{Methodology}
\label{chap:methodology}
```

### Comment covered

Sergi email and old PDF pages 34, 36, 38. Evgenii email: methodology should
focus on the final model.

### Exact replacement

Replace the current opening paragraph with:

```latex
This chapter describes the final reproducible method. It first fixes the CKM
dataset contract, the ground receiver mask, the city holdout split and the
pixel weighted metrics. It then introduces the complete prediction pipeline:
building height map and UAV height are converted into support masks and frozen
prior maps; \textsc{HARP-Net CKM} receives those maps and predicts bounded
residual corrections; the final outputs are channel attenuation, delay spread
and angular spread maps. The development history that led to this choice is
kept in Appendix~A, while this chapter keeps only the final ingredients needed
to reproduce the reported results.
```

### Reason

The current text still says the chapter uses early neural models as diagnostics
and identifies target distributions. That is true historically, but it puts the
reader back into the chronology before the final method has been established.

## Task 4: Add Methodology Block Diagram

### File

`reduced/TFG/methodology.tex`

### Current anchor

Insert after the framework input/output table ending near current line 214,
before the paragraph beginning:

```latex
Therefore, the full framework has two external inputs and three final outputs.
```

### Comment covered

Sergi old PDF page 34: missing block diagram of the overall methodology.

### Exact edit

Add this figure:

```latex
\begin{figure}[htbp]
  \centering
  \resizebox{\textwidth}{!}{%
  \begin{tikzpicture}[
    >=Latex,
    node distance=0.75cm and 0.95cm,
    block/.style={draw, rounded corners=2pt, align=center, minimum height=0.8cm,
      minimum width=2.65cm, font=\scriptsize},
    input/.style={block, fill=blue!8},
    support/.style={block, fill=orange!10},
    prior/.style={block, fill=green!10},
    model/.style={block, fill=purple!8},
    output/.style={block, fill=red!8}
  ]
    \node[input] (topology) {Building height\\map};
    \node[input, below=of topology] (height) {UAV transmitter\\height};

    \node[support, right=of topology] (masks) {Ground mask\\LoS/NLoS mask};
    \node[prior, right=of masks] (priors) {Frozen priors\\PL, DS, AS};
    \node[model, right=of priors] (harp) {\textsc{HARP-Net CKM}\\residual model};
    \node[output, right=of harp] (outputs) {Channel attenuation\\delay spread\\angular spread};
    \node[support, below=of harp] (eval) {City holdout\\ground pixel metrics};

    \draw[->] (topology) -- (masks);
    \draw[->] (height) -| (masks);
    \draw[->] (topology) -- ++(1.0,0) |- (priors);
    \draw[->] (height) -- ++(1.0,0) |- (priors);
    \draw[->] (masks) -- (priors);
    \draw[->] (priors) -- (harp);
    \draw[->] (masks) -- ++(0,-1.1) -| (harp);
    \draw[->] (height) -- ++(3.2,0) |- (harp);
    \draw[->] (harp) -- (outputs);
    \draw[->] (outputs) |- (eval);
  \end{tikzpicture}}
  \caption{High level methodology flow. The user supplies the city height map
  and UAV transmitter height. The pipeline constructs support masks and frozen
  prior maps, then \textsc{HARP-Net CKM} predicts residual corrections for the
  three CKM outputs.}
  \label{fig:methodology_block_diagram}
\end{figure}
```

### Follow up text

Immediately after the figure, add:

```latex
Figure~\ref{fig:methodology_block_diagram} is the reader map for the rest of
the chapter. Sections~\ref{sec:priors_overview} to~\ref{sec:delay_method_summary}
define the frozen prior maps, and Section~\ref{sec:try80_detail} defines the
residual model and evaluation protocol.
```

## Task 5: Remove Dead Chronology Block From Methodology Source

### File

`reduced/TFG/methodology.tex`

### Current anchors

1. `\iffalse` at current line 239.
2. Matching `\fi` at current line 805.

### Comment covered

Sergi and Evgenii: Chapter 3 should not show the struggle or old chronology.

### Exact edit

Delete the entire hidden block from `\iffalse` through `\fi`.

### Why delete if it is hidden?

The block does not compile, but it is a long dead copy of the exact material
the supervisors are warning against. Keeping it increases the risk that it is
accidentally reenabled or edited instead of the visible methodology. The useful
lessons are already in Appendix A and Appendix D.

### Content that must remain visible elsewhere

Do not delete these visible final method sections:

1. `\section{Final priors: overview and literature basis}`
2. `\section{Path Loss Prior and Residual Prediction}`
3. `\section{Angular Spread Prior and Residual Prediction}`
4. `\section{Delay Spread Prior and Residual Prediction}`
5. `\section{Training and Evaluation Protocol}`

## Task 6: Rename the Path Loss Prior Section Carefully

### File

`reduced/TFG/methodology.tex`

### Current anchor

Current line 811:

```latex
\section{Path Loss Prior and Residual Prediction}
```

### Comment covered

Sergi and Evgenii terminology: the predicted dense target is channel
attenuation, while "path loss" is correct for physical propagation formulas and
dataset/model names.

### Exact edit

Replace the section heading with:

```latex
\section[Channel Attenuation Prior]{Channel Attenuation Prior and Residual Prediction}
\label{sec:try78_detail}
```

The short title avoids a long table of contents line. Keep the existing label.

### Exact reader map replacement

Replace the current first reader map paragraph with:

```latex
This section is intentionally detailed because it is the mathematical core of
the final channel attenuation result. The CKM dataset stores this target under
the name \texttt{path\_loss}, and the LoS branch is a physical path loss
model in the standard propagation sense. In the thesis prose, however, the
final dense predicted dB map is called channel attenuation, following the
terminology note in Chapter~1.
```

Then keep the rest of the reader map, but change:

```latex
the prior output becomes the frozen attenuation anchor consumed by the final residual GMM head model.
```

to:

```latex
the prior output becomes the frozen attenuation anchor consumed by
\textsc{HARP-Net CKM}.
```

## Task 7: Fix Equation References and Numbering

### Files

1. `reduced/TFG/methodology.tex`
2. `reduced/TFG/results.tex`
3. `paper_version/paper.tex`
3. `reduced/TFG/prior_detail_try78.tex`
4. `reduced/TFG/prior_detail_try79.tex`
5. `reduced/TFG/prior_detail_try80.tex`

### Sergi comment covered

Old PDF page 37: use `\eqref{}` so equation references include parentheses.

### Exact replacements in visible thesis files

In `methodology.tex`:

```latex
Eq.~\ref{eq:height_empirical_histogram}
```

becomes:

```latex
Eq.~\eqref{eq:height_empirical_histogram}
```

In `results.tex`:

```latex
Eq.~\ref{eq:height_empirical_histogram}
```

becomes:

```latex
Eq.~\eqref{eq:height_empirical_histogram}
```

In `prior_detail_try78.tex`, visible occurrences to convert:

1. `Eq.~\ref{eq:field_sum}` to `Eq.~\eqref{eq:field_sum}`
2. `Eq.~\ref{eq:nlos_mask_v2}` to `Eq.~\eqref{eq:nlos_mask_v2}`

In TikZ node labels, keep `Eq.~\ref{...}` only if `\eqref` breaks spacing in
the figure. Figure labels are less important than prose references.

### Numbering audit

Search after edits:

```powershell
rg -n "Eq\\.~\\\\ref|Eq\\. \\\\ref|Equation~\\\\ref|\\\\begin\\{equation\\*\\}|\\\\begin\\{align\\*\\}" reduced/TFG -g "*.tex"
```

Any equation referenced in prose must be in a numbered `equation`, `align`, or
similar environment. Do not number display equations that are never referenced.

## Task 8: Chapter 2 Reader Map and Structure Cleanup

### File

`reduced/TFG/state_of_art.tex`

### Current anchors

1. Chapter opening lines 3 to 9.
2. Major sections at current lines 13, 49, 400, 450, 487, and 608.

### Comments covered

Sergi old PDF pages 21 to 33, plus Evgenii request to clean Section 2 so it
contains background only.

### Exact opening replacement

Replace the current opening paragraph with:

```latex
This chapter gives the background needed before the method is introduced. It
has four roles. First, it defines the propagation and spread quantities used in
the thesis. Second, it reviews dense radio map prediction methods and their
limitations. Third, it introduces the training and distribution tools used
later. Fourth, it explains why external results cannot be compared as a simple
leaderboard. Final thesis results are reported only in Chapter~\ref{chap:results}.
```

### Add a reader map after the opening paragraph

Add:

```latex
\noindent\textbf{Reader map.}
Sections~\ref{sec:soa_ckm_context} to~\ref{sec:soa_classical} introduce CKMs,
path loss models and A2G propagation. The angular and delay spread sections
define the two non attenuation targets. Section~\ref{sec:soa_distribution}
collects the training tools and fair comparison rules that are needed to read
the methodology and results.
```

### Navigation cleanup

Do not split the chapter into two LaTeX chapters unless page count allows it.
Instead, keep the existing chapter but make the hierarchy easier to scan:

1. Keep `\section{General Framework: CKM Surrogates and Evaluation Contracts}`.
2. Keep `\section{Path Loss Prediction}` because the physical literature uses
   that term.
3. Keep `\section{Angular Spread Prediction}`.
4. Keep `\section{Delay Spread Prediction}`.
5. Rename `\section{Training and Fair Comparison}` to:

```latex
\section{Distribution, Training Tools and Fair Comparison}
```

6. Inside that section, keep GMM, diffusion, multitask and stabilization as
   tools used later. This addresses the comment that some subsections did not
   look like state of the art.

## Task 9: Chapter 2 Local Wording and Precision Fixes

### File

`reduced/TFG/state_of_art.tex`

### Two-ray wording

Current line 86:

```latex
field magnitude \(|E_{\mathrm{total}}|\) is then converted to a path loss like
dB prediction with a fitted calibration constant.
```

Replace with:

```latex
field magnitude \(|E_{\mathrm{total}}|\) is then converted to a dB attenuation
prediction with a fitted calibration constant.
```

### Where the 1.75 dB comes from

After the two-ray paragraph, add:

```latex
The numerical gain of this prior is not reported here because this chapter is
background. The fitted CKM result is evaluated later in
Chapter~\ref{chap:results}.
```

### RMTransformer precision

Current lines around 301 to 309 include:

```latex
0.007148
0.01046
0.008099
```

Replace with:

```latex
\(7.15\times10^{-3}\)
\(1.05\times10^{-2}\)
\(8.10\times10^{-3}\)
```

Then rewrite the sentence as:

```latex
It reports a normalised RMSE of \(7.15\times10^{-3}\), compared with
\(1.05\times10^{-2}\) for PMNet under a random 90/10 split on
\(256\times256\) maps.
```

and:

```latex
the reported channel prediction error of \(8.10\times10^{-3}\) corresponds to
roughly \SI{2.06}{dB}.
```

### Path gain and received power wording

Current line around 307:

```latex
received power/path loss
```

Replace with:

```latex
received power or path loss, depending on the paper convention,
```

This avoids implying that received power, path gain and path loss are the same
quantity.

## Task 10: Chapter 4 Focus Pass

### File

`reduced/TFG/results.tex`

### Comments covered

Evgenii: Results should focus on final model. Sergi old PDF page 86: same as
Section 3, present final results and compare with previous papers.

### Current anchors

1. `\section{Channel Attenuation Results}` starts at current line 65.
2. Hidden development block starts at current line 168 with `\iffalse`.
3. Hidden block ends at current line 429 with `\fi`.
4. `\section{Qualitative Analysis}` starts at current line 970.

### Exact deletion

Delete the hidden `\iffalse` block from current line 168 to current line 429.
It is not compiled, but it is still old development history in the source.

### Shorten method explanation inside Results

Replace the long method recap after the split comparability note with this
shorter result focused text:

```latex
The calibrated attenuation prior is the strongest non neural baseline in the
thesis. It is split into LoS and NLoS branches because those regimes have
different error mechanisms, but the construction details belong to
Chapter~\ref{chap:methodology}. In this chapter the prior is used as a frozen
baseline for the final test comparison.

The final reporting separates LoS and NLoS wherever the target definition
allows it. A single overall number can hide whether the model is improving
direct visibility pixels, blocked pixels, or only the easier majority regime.
```

Keep Table `tab:try78_results` and the spread prior table if page count allows,
because they are final baselines. If Chapter 4 remains long after compile,
move the explanatory dictionary paragraph about 114 spread keys back to
methodology and keep only the final table in Results.

## Task 10A: Clarify Delay and Angular Spread Evaluation

### Files

1. `reduced/TFG/methodology.tex`
2. `reduced/TFG/results.tex`

### New Sergi email clarification

Sergi asked whether delay spread and angular spread evaluation is obtained from
the prediction versus the real value. The answer must be explicit in the thesis:
yes. The CKM ground truth contains delay spread and angular spread values for
all valid ground pixels, because each non-building pixel is a receiver. The
spread metrics therefore use the same valid ground receiver grid as channel
attenuation: compare the predicted dense map with the ray-traced dense ground
truth and compute RMSE over all valid ground receivers.

### Exact edit in Methodology

After Eq.~\eqref{eq:rmse}, add a plain sentence explaining that the same
pixel-weighted valid-ground RMSE contract applies to channel attenuation, delay
spread and angular spread. State that every non-building pixel is a receiver
for the spread targets too, so the spread RMSE is prediction versus ray-traced
ground truth over all valid ground receivers.

### Exact edit in Results

After the definition of `model_rmse` around Eq.~\eqref{eq:try80_model_rmse},
add the same clarification in result-facing language: delay spread and angular
spread are not special aggregate metrics; they are dense pixel-wise prediction
errors against CKM ground truth, accumulated over the valid receiver mask.

### Exact edit in Paper Version

After the paper's target-specific RMSE equation, add the compact version of the
same clarification. Keep it short: the paper should state that DS and AS are
evaluated on the same valid ground receiver pixels, comparing dense predictions
with dense CKM ground truth values.

## Task 11: Add One Representative Qualitative Panel to Results

### File

`reduced/TFG/results.tex`

### Current anchor

Insert inside `\section{Qualitative Analysis}`, after its first paragraph at
current line 973.

### Comments covered

Sergi old PDF pages 116 and 126: "why not this in the results?"

### Exact edit

Add:

```latex
\begin{figure}[!htbp]
\centering
\includegraphics[width=\textwidth,height=0.78\textheight,keepaspectratio]{img/thesis_figures/try80_appendix_panels/try80_panel_dense_mid_ant_Vancouver_sample_15265_6x3.png}
\caption[Representative final model inspection panel.]%
{Representative final model inspection panel for a dense, mid altitude,
held out test sample in Vancouver. The full gallery remains in
Appendix~\ref{app:qualitative_diagnostics}; this panel is kept here because it
shows the final prior, residual correction and prediction side by side.}
\label{fig:try80_panel_results}
\end{figure}
```

### Appendix adjustment

In `appendices_compact.tex`, keep the three detailed panels unless page count
becomes a problem. If page count rises too much, remove the Vancouver duplicate
from Appendix B and keep only open/low and mixed/mid there, with the full
gallery still referenced as generated files.

## Task 12: Expand Sustainability Economic Impact

### File

`reduced/TFG/sustainability_balanced.tex`

### Current anchor

Inside `\section{Economic and social impact}`, after the first paragraph ending
with:

```latex
surrogate could reduce repeated simulation runs and enable faster scenario
studies over UAV heights or city layouts.
```

### Comments covered

Sergi old PDF page 104: potential economic impact, patent, sale, company,
operator actions, applications enabled by accurate radio maps.

### Exact insertion

```latex
The most realistic economic path is a planning tool rather than a standalone
consumer product. A mature version could be licensed as software for network
planning teams, integrated into a digital twin workflow, or offered as a
service for rapid UAV coverage studies. Operators could use faster CKM
generation to compare UAV heights, test temporary base station locations,
identify weak streets or squares before deployment, and decide where expensive
ray tracing or field measurements are really needed. Better radio maps would
not create capacity by themselves, but they would make planning iterations
cheaper and could reduce the risk of sending equipment or measurement teams to
poor candidate sites. Patentability would require a novelty analysis beyond
this thesis, because CKMs, radio map prediction and hybrid physics neural
models already exist in the literature; the more plausible near term value is
know how, implementation, calibration data and integration into operator
planning workflows.
```

## Task 13: Bibliography Audit for arXiv Entries

### File

`reduced/TFG/TFG.bib`

### Comment covered

Sergi old PDF page 110: replace arXiv entries with conference or journal
versions where available, and add volume, issue, pages and DOI.

### Exact keys to audit

Search and verify these keys first because the current `.bib` still contains
`howpublished = {arXiv:...}` or arXiv only URLs:

1. `saboor2025height`
2. `icassp2023challenge`
3. `dataset2212`
4. `jaensch2024directiverme`
5. `ckmimagenet2025`
6. `icassp2025indoor`
7. `radiogunet2025`
8. `rmtransformer2025`
9. `tarhouni2025`
10. `gao2026`
11. `airmap2025`
12. `pathfinder2025`
13. `wicopg2025`
14. `fmrme2026`
15. `radiolam2025`
16. `reveal2025`
17. `radiopit2025`
18. `cai2019`
19. `lee2024timevarying`

Also verify arXiv URLs attached to entries that already have DOIs:

1. `radiounet2020`
2. `pmnet2023`
3. `ippnet2025`
4. `transPathNet2025`
5. `geomDL2024`
6. `radiodiff2025`
7. `isola2017pix2pix`
8. `kendall2017uncertainties`
9. `izmailov2018swa`
10. `perez2018film`
11. `dhariwal2021diffusion`

### Exact audit rule

For each key:

1. Search the title in IEEE Xplore, ACM, Springer, Elsevier, MDPI, arXiv, DBLP
   or Crossref.
2. If a peer reviewed version exists, convert the entry type from `@misc` to
   `@inproceedings` or `@article`.
3. Keep the arXiv URL only if it is useful as an open version, but do not make
   arXiv the main publication venue when a venue exists.
4. Add `doi`, `booktitle` or `journal`, `volume`, `number`, `pages`, `year`,
   and `publisher` where available.
5. Rebuild with `biber` and inspect the bibliography page around the changed
   entries.

### Exact command to list remaining arXiv items

```powershell
rg -n "arXiv|arxiv" reduced/TFG/TFG.bib
```

## Task 14: Global Terminology Audit

### Files

All visible thesis `.tex` files under `reduced/TFG`.

### Comments covered

Sergi old PDF pages 16, 21 and 29, plus later user request about path loss
versus channel attenuation.

### Rules

Use "channel attenuation" for the final predicted dense dB CKM target.

Keep "path loss" in these cases:

1. Physical propagation formulas, for example FSPL, two-ray, COST 231, 3GPP
   path loss.
2. Names of cited papers, datasets, challenges or model fields.
3. Code or dataset identifiers such as `path_loss` and PL.
4. The final prior if the sentence is explicitly about the physical LoS path
   loss model.

Avoid "path gain" unless the cited paper really reports gain rather than loss.
Avoid "received power" unless the unit is dBm and the paper actually reports
received power.

### Exact search

```powershell
rg -n "\\bpath loss\\b|\\bPath Loss\\b|path-loss|pathloss|path gain|received power" reduced/TFG -g "*.tex"
```

### Exact replacements to consider

1. `Final path loss prior` can stay if the paragraph is about Try 78 or the
   physical prior.
2. `path loss map` in final output prose should become `attenuation map`.
3. `PL means channel attenuation RMSE` should remain in Results because it
   explains the abbreviation.
4. Captions of prior tables can keep "path loss prior" when the table is about
   the calibrated physical prior.

## Task 15: Acronym and Jargon Audit

### Files

1. `reduced/TFG/introduction.tex`
2. `reduced/TFG/state_of_art.tex`
3. `reduced/TFG/methodology.tex`
4. `reduced/TFG/acronyms.tex`

### Comments covered

Sergi old PDF pages 2, 16, 17, 21, 22 and 29.

### Exact checks

Search:

```powershell
rg -n "\\bCKM\\b|\\bUxNB\\b|\\bLoS\\b|\\bNLoS\\b|\\bFiLM\\b|\\bGMM\\b|\\bPMHHNet\\b|\\bFR3\\b|\\bOLS\\b|\\bRMSE\\b|\\bMAE\\b|\\bSWA\\b|\\bEMA\\b" reduced/TFG -g "*.tex"
```

Then check the first visible occurrence of each term in the compiled text.

### Rules

1. In the introduction, define only what a reader needs immediately.
2. Avoid `FiLM`, `GMM`, `PMHHNet`, `SWA`, `EMA` in Chapter 1 unless there is a
   one sentence explanation.
3. Use `\ac{}` or the existing acronym system for first use where practical.
4. Do not repeatedly define acronyms in later chapters.

## Task 16: Precision and Hyphen Cleanup

### Files

All visible `.tex` files, especially `state_of_art.tex`.

### Comments covered

Sergi old PDF page 24 and user preference about redundant hyphens.

### Precision rules

1. Literature scale numbers in prose: two or three significant figures.
2. Thesis final metrics in final result tables: keep the reported precision
   already used in Chapter 4.
3. Conversion examples: show one calculation if needed, not many decimals.

### Hyphen rules

Remove unnecessary prose hyphens such as:

1. `reader-facing` if `reader facing` reads fine.
2. `long-term` if `long term` is not used adjectivally.
3. `state-of-the-art` in prose if `state of the art` reads fine.

Keep necessary technical hyphens:

1. LaTeX commands and command flags.
2. File names, labels, and code identifiers.
3. Established technical terms such as `LoS/NLoS`, `image-to-image` when it is
   used as a compound modifier, `two-ray` if the chosen style keeps the model
   name, and `HARP-Net CKM`.

### Exact search

```powershell
rg -n "\\w-\\w" reduced/TFG -g "*.tex"
```

Review manually. Do not mechanically delete all hyphens.

## Task 17: Paper Version Follow Up

Only after the reduced thesis compiles cleanly:

1. Apply terminology changes to `paper_version`.
2. Apply the final HARP-Net CKM naming consistently.
3. Do not add the full AI declaration to the paper unless the venue or
   supervisor asks for it.
4. Keep the paper much shorter than the thesis. Do not port the full appendix
   or full Chapter 3 restructure unless the paper still contains the same
   reader problem.

## Task 18: Final Verification

### Compile

From `reduced/TFG`:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error TFG.tex
```

If bibliography changed:

```powershell
biber TFG
latexmk -pdf -interaction=nonstopmode -halt-on-error TFG.tex
```

### PDF text checks

After compile, update or regenerate the extract if needed, then search:

```powershell
pdftotext TFG.pdf TFG_check_extract.txt
rg -n "Methods and procedures|Generative AI|Eq\\. [0-9]|GMM-head|prior-anchored residual GMM-head|Final Review|Presentation" TFG_check_extract.txt
```

Expected outcomes:

1. "Methods and procedures" no longer appears in the table of contents.
2. "Declaration on Generative AI Use" appears in the appendix.
3. Chapter 3 table of contents is shorter and final method first.
4. Chapter 4 contains one representative final model panel in the results.
5. The old hidden development blocks no longer exist in source.
6. No important equation reference appears without parentheses.
7. Delay spread and angular spread evaluation is explicitly described as
   prediction versus ray-traced ground truth over all valid ground receiver
   pixels.

### Git checks

Before committing or pushing:

```powershell
git status --short
git diff -- reduced/TFG/introduction.tex reduced/TFG/methodology.tex reduced/TFG/state_of_art.tex reduced/TFG/results.tex reduced/TFG/sustainability_balanced.tex reduced/TFG/appendices_compact.tex reduced/TFG/TFG.bib
```

Do not commit generated PDF auxiliary churn unless the project convention
requires it.
