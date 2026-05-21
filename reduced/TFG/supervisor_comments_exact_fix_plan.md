# Supervisor Comments - Exact Fix Plan Draft

Source PDF: `C:/Users/guill/Downloads/TFG_draft_21may_GV.pdf`

Purpose: this is the version I would use as the working edit script before touching the thesis. It says exactly what I would change, with proposed replacement text where the fix is local. You can correct the wording before we apply anything.

## Global Editorial Fix From Email

I would make the thesis less chronological and more final-method-first.

Exact high-level restructuring:

1. Keep Chapter 2 as background only. Remove thesis result values and final-model claims from the state-of-the-art chapter, except neutral phrases like "this thesis uses this evaluation contract".
2. Refactor Chapter 3 so it starts from the final pipeline: dataset and split, priors, final residual model, training/evaluation protocol. Move development history to the appendix.
3. Refactor Chapter 4 so it reports final results first, then comparison with literature. Move intermediate attempts and failed branches to the appendix.
4. Keep negative results in the main text only as a short lesson paragraph. Put the detailed "struggles" in the appendix.

Suggested final thesis narrative:

```text
Chapter 1: Problem, goals, final questions, and contribution summary in simple words.
Chapter 2: Background and SOTA limitations only.
Chapter 3: Final method and reproducibility contract.
Chapter 4: Final results, prior baselines, external comparison, runtime, limitations.
Chapter 5: Sustainability, economic impact, ethics.
Chapter 6: Conclusions, RQ answers, future work.
Appendix A: Development trace, failed attempts, diagnostic baselines, negative results.
```

## Naming Decision I Would Apply

I would name the final framework `AnchorGMM`.

Definition to introduce once:

```latex
\textsc{AnchorGMM} is the final prior-anchored Gaussian-mixture residual
surrogate used in this thesis. The name reflects its two main design choices:
predictions are anchored to frozen physical/statistical priors, and the neural
residual branch keeps a mixture-model representation of the remaining error.
```

Then use `\textsc{AnchorGMM}` in the introduction and conclusions instead of repeated phrases such as "selected prior-anchored residual model" or "final prior-anchored residual GMM-head model". In the technical chapters, after the name is defined, keep the longer architecture description when needed.

## SC-001 - Add 3GPP UxNB Terminology

File: `introduction.tex`

Exact replacement for the opening paragraph, replacing lines 3-14:

```latex
Reliable radio coverage prediction is a central requirement for future 6G
systems in which UAVs may act as aerial base stations, relays, or temporary
coverage nodes. In 3GPP terminology, a UAV-mounted radio access node is a
UxNB, defined as a radio access node on board a UAV
\cite{threegpp22125}. A classical ray-tracing simulator can produce detailed
channel knowledge maps, but this is too expensive to repeat every time the
transmitter height, the city environment, or the deployment assumptions change.
In the 6G literature, a channel knowledge map is a site-specific,
location-tagged repository of channel information that can support
environment-aware planning and reduce online channel-acquisition overhead
\cite{zengx2021ckm,ckmtutorial2024}. This thesis studies whether
\textsc{AnchorGMM}, a prior-anchored Gaussian-mixture surrogate, can predict
dense CKM target maps directly from urban geometry while preserving enough
physical structure to generalize to cities not seen during training.
```

Add this bibliography entry to `TFG.bib` near the other standards:

```bibtex
@techreport{threegpp22125,
  author      = {{3GPP}},
  title       = {Uncrewed Aerial System ({UAS}) Support in {3GPP}; Stage 1},
  institution = {3rd Generation Partnership Project},
  number      = {TS 22.125},
  year        = {2026},
  note        = {Specification details page, accessed 21 May 2026},
  url         = {https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3545},
}
```

## SC-002 - Check Reference Numbering Convention

Files: `config/styles.tex`, `styles.tex`

Current configuration uses `sorting=nyt`, so numeric citations are sorted alphabetically by author/title/year instead of order of first citation. I would change it to citation-order numbering.

Exact change in both files:

```latex
sorting=none,
```

instead of:

```latex
sorting=nyt,
```

Then rebuild with `lualatex -> biber -> lualatex -> lualatex`.

## SC-003 - Clarify Whether LoS/NLoS Mask Is an Input

File: `introduction.tex`

Exact replacement for lines 16-22:

```latex
The project is formulated as dense image-to-image regression on
$513\times513$ pixel city maps. The final model receives a building-height
topology map, a LoS/NLoS visibility mask, the UAV antenna height, and the
frozen prior maps described later in the thesis. In the CKM experiments the
visibility mask is read from the dataset; for topology-only deployment it can
be generated geometrically from the building map and UAV height. The predicted
outputs are path loss, delay spread, and angular spread. The neural network
therefore does not infer visibility from scratch; it uses visibility as one of
the physical support inputs and learns the residual radio-map structure around
the calibrated priors.
```

## SC-004 - Fix Path Loss / Channel Attenuation Terminology

I would apply this rule globally:

```text
Use "path loss" only for the HDF5 `path_loss` target and for explicit PL models.
Use "path gain" only when discussing papers whose target is gain.
Use "received power" only with dBm units.
Use "channel attenuation" only when speaking generically about the combination
of attenuation effects, not when naming the dataset target.
Use "dense CKM target maps" instead of vague "channel maps" when the three
outputs PL/DS/AS are meant.
```

Exact local fixes:

1. In `introduction.tex`, use the replacement in SC-003.
2. In `state_of_art.tex`, fix the comparison checklist as described in SC-036.
3. In `results.tex`, keep "path-loss RMSE" for the final PL metric. Do not call it "channel power".
4. In `TFG.tex`, keep PDF keywords as `path loss, delay spread, angular spread`; those are the actual thesis targets.

## SC-005 - Choose a Clear Framework Name

Use `\textsc{AnchorGMM}`.

Exact first definition: add the definition from the "Naming Decision" section after the two opening paragraphs in `introduction.tex`.

Exact search/replace after definition:

```text
selected prior-anchored residual model -> \textsc{AnchorGMM}
final prior-anchored residual GMM-head model -> \textsc{AnchorGMM}
final residual GMM-head model -> \textsc{AnchorGMM}
```

Do not replace inside highly technical paragraphs where the architecture is being defined; there, write:

```latex
\textsc{AnchorGMM}, the final prior-anchored residual GMM-head model, ...
```

## SC-006 - Define City-Holdout Early

File: `introduction.tex`

The current definition is technically correct, but I would make it even simpler. Replace lines 50-54 with:

```latex
The most important methodological objective was not only to obtain a low
average RMSE, but to do so under a strict city-holdout split. City holdout
means that entire cities, not individual pixels or tiles, are reserved for
validation and testing. A test city therefore contains no samples that were
seen during training. This is harder and more deployment-relevant than random
pixel or random tile splitting, because the model must work on urban layouts
it has never seen.
```

## SC-007 - Avoid Unexplained "Prior-Anchored Residual Model" In The Intro

File: `introduction.tex`

Handled by SC-005 and SC-009. Do not use the phrase "selected prior-anchored residual model" in the introduction before defining the final framework name.

## SC-008 - Specify "All Three Dense Targets"

File: `introduction.tex`

Handled inside the SC-009 replacement. Use:

```latex
path loss, delay spread, and angular spread
```

instead of:

```latex
all three dense targets
```

## SC-009 - Simplify The Research-Question Teaser

File: `introduction.tex`

Exact replacement for lines 75-83:

```latex
In simple terms, the final answer to the three questions is positive within
the fixed CKM simulation setting used in this thesis. \textsc{AnchorGMM}
predicts path loss, delay spread, and angular spread on cities that were not
used for training. The reason it works is not that the neural network learns
all propagation physics from zero. Stable effects such as distance, visibility,
UAV height, and city type are first captured by calibrated priors; the neural
network then corrects the remaining local errors. The hardest cases are still
low-altitude and strongly blocked NLoS regions, so the results are always
reported by regime instead of only as one global RMSE. Chapter~\ref{chap:results}
and the conclusions give the full technical answer.
```

## SC-010, SC-011, SC-012, SC-013, SC-014, SC-015 - Rewrite Contribution List

File: `introduction.tex`

Exact replacement for lines 85-106:

```latex
The main contributions corresponding to these questions are:

\begin{itemize}
  \item A reproducible CKM prediction pipeline for ground users served by a
        centred UAV transmitter. The evaluation uses \(513\times513\) maps,
        city-holdout train/validation/test splits, valid ground receiver
        pixels only, and continuous UAV altitude conditioning.
  \item A train-calibrated path-loss prior based on enhanced two-ray LoS
        propagation and ordinary least squares (OLS) NLoS calibration over
        environment features. On held-out cities this prior already reaches
        \SI{1.75}{dB} LoS and \SI{3.40}{dB} NLoS RMSE.
  \item Train-calibrated delay-spread and angular-spread priors based on
        log-domain ridge regression over geometry, visibility, UAV-height, and
        environment features.
  \item \textsc{AnchorGMM}, a shared neural model that receives the frozen PL,
        DS, and AS priors and learns bounded residual corrections for the three
        maps jointly.
  \item A distribution-shape analysis showing that earlier point-regression
        networks tended to average away difficult NLoS and spread-tail cases.
        This motivates using mixture-style residual predictions instead of a
        single direct regression value everywhere.
\end{itemize}
```

This fixes:

- "ground-only masking" by saying "valid ground receiver pixels only".
- "city-holdout splits" by saying train/validation/test cities are separated.
- "FR3 UAV dataset" by removing the acronym from the contribution list.
- "OLS" by expanding it.
- "head" by avoiding it in the introduction.
- "distribution-first diagnosis" by explaining the idea in simple words.

## SC-016 - Add Chapter Numbers To Thesis Outline

File: `introduction.tex`

Exact replacement for lines 108-122:

```latex
\section{Thesis outline}

Chapter~2 reviews the state of the art and the technical background needed for
the thesis: classical propagation models, radio-map deep learning, hybrid
physics/neural methods, distribution-aware prediction, and fair-comparison
criteria. Chapter~3 describes the final methodology: the CKM dataset, the
ground-receiver evaluation contract, the city-holdout split, the calibrated
priors, and the \textsc{AnchorGMM} residual model. Chapter~4 reports the final
quantitative results, the comparison with the frozen priors and the closest
published benchmarks, qualitative examples, runtime, and limitations.
Chapter~5 discusses sustainability, economic impact, social impact, and ethical
scope. Chapter~6 answers the research questions and presents future work. The
appendices preserve the development trace, representative panels, and generator
documentation.
```

## SC-017 - Remove "Canonical"

File: `introduction.tex`

Exact replacement:

```latex
The CKM dataset contains 66 real-city scenarios and 16180 samples.
```

instead of:

```latex
The canonical dataset contains 66 real-city scenarios and 16180 samples.
```

## SC-018 - Rephrase Ground Pixels As Ground Users

File: `introduction.tex`

Exact replacement for lines 149-154:

```latex
The physical receiver scenario is a ground user served by the UAV. Therefore,
losses and metrics are computed only on valid ground receiver pixels. Building
pixels remain in the topology input because they affect propagation, but they
are excluded from error accumulation because no receiver is placed inside a
building pixel. The fixed receiver height used in the analytic priors is
\SI{1.5}{m}. The transmitter is the UAV antenna, whose height varies
continuously across the dataset.
```

## SC-019 - Replace Chronological Work Plan With Final-Model Explanation

File: `introduction.tex`

Exact replacement for lines 156-178:

```latex
\section{Methods and procedures}

The final method follows a hybrid pipeline. First, the city map is represented
as a building-height raster with a centred UAV transmitter and a fixed
ground-user receiver grid. Second, geometric LoS/NLoS masks and calibrated
priors are prepared for path loss, delay spread, and angular spread. Third,
\textsc{AnchorGMM} receives the topology, masks, UAV height, and prior maps and
predicts bounded residual corrections for the three outputs. The final maps are
the prior predictions plus the learned residual corrections.

Earlier neural models are still useful scientifically, but mainly as
diagnostics. They showed that direct image-to-image prediction can produce
plausible-looking maps while missing NLoS and spread-tail behaviour. For this
reason the main text presents the final method first; the chronological attempt
trace is kept in the appendix.
```

Exact replacement for lines 180-203:

```latex
\section{Work plan}
\label{sec:workplan}

The executed work plan can be grouped into five phases: literature and
simulation-contract review, dataset and split definition, calibrated-prior
construction, final residual-model training, and final evaluation/writing.
Figure~\ref{fig:gantt} shows these phases at project level rather than listing
all individual experiments.

\begin{figure}[ht]
  \centering
  \input{img/gantt_diagrama}
  \caption[Project's Gantt diagram]{Gantt diagram of the project grouped by
  the main thesis phases: background review, dataset contract, prior
  construction, final residual model, evaluation, and writing.}
  \label{fig:gantt}
\end{figure}

The main deviation from the original proposal was methodological rather than
administrative. The project moved from a generic image-to-image model toward a
hybrid CKM generator because the dataset showed strong radial, visibility, and
distributional structure that should not be left entirely to a black-box neural
network.
```

## SC-020 - Reduce Hyphen Overuse

Exact edits I would make:

```text
fair-comparison -> fair comparison
continuous-UAV-height -> continuous UAV-height
city-holdout protocol -> city-holdout split when used as adjective, city holdout when used as noun
ground-only masking -> ground-receiver masking or valid ground receiver pixels
prior-anchored residual model -> \textsc{AnchorGMM} in intro/conclusion, technical phrase only in method
```

I would run:

```powershell
rg -n "\w+-\w+-\w+|fair-comparison|ground-only|city-holdout|continuous-UAV-height" C:\TFG\FINAL_THESIS\reduced\TFG -g "*.tex"
```

Then simplify only prose, not equations, labels, filenames, or established acronyms.

## SC-021 - Use "Channel Gain" Only

File: `state_of_art.tex`

Exact replacement for lines 17-20:

```latex
The term channel knowledge map (CKM) refers to a site-specific database of
location-tagged channel knowledge, such as channel gain, angles, or delay
information, used to make future radio systems environment-aware
\cite{zengx2021ckm,ckmtutorial2024}.
```

## SC-022 - Remove Thesis Results From SOTA

File: `state_of_art.tex`

Exact replacement for lines 3-10:

```latex
Radio-map prediction sits at the intersection of classical wireless propagation
modelling, statistical channel analysis, and dense computer-vision regression.
This chapter reviews the background needed to understand the final design:
classical and empirical propagation models, deep learning for radio-map
estimation, physics-informed and hybrid neural approaches, distribution-aware
prediction, and fair comparison rules. The goal is to identify the limitations
of existing work and the tools that will be used later, not to report the
results of this thesis.
```

Exact deletion/move:

- Move the thesis-specific final model table in `state_of_art.tex` lines 704-729 to Chapter 4 if it is still useful.
- Delete or rewrite lines 731-736 because they report final model performance inside SOTA.
- Replace the final section title:

```latex
\section{Emerging techniques and implications for this thesis}
```

instead of:

```latex
\section{Emerging techniques and position of the final model}
```

Exact replacement for lines 689-699:

```latex
For the present thesis, the literature points to four practical design
requirements. First, the comparison contract must be explicit because datasets,
splits, height protocols, and target units differ widely. Second, A2G prediction
requires continuous UAV-height conditioning rather than a fixed transmitter
height. Third, LoS/NLoS and environment-type effects should be reported
separately because one global RMSE hides the hardest regimes. Fourth,
distribution-aware outputs are useful when targets contain multiple modes or
long tails. These observations motivate the methodology in Chapter~3.
```

## SC-023 - Define Two-Ray Equation Terms

File: `state_of_art.tex`

Exact replacement for lines 61-76:

```latex
FSPL is the single-direct-ray reference baseline in unobstructed conditions, not
a lower bound on the final path loss once coherent reflections are present. In
aerial scenarios a specular ground reflection can produce constructive or
destructive interference periodically with distance. Let \(d_{2D}\) be the
horizontal Tx-Rx distance, \(h_{\mathrm{tx}}\) the UAV height, and
\(h_{\mathrm{rx}}\) the receiver height. The direct and reflected path lengths
are
\begin{equation}
  d_{\mathrm{dir}} =
  \sqrt{d_{2D}^{2} + (h_{\mathrm{tx}}-h_{\mathrm{rx}})^{2}},
  \qquad
  d_{\mathrm{ref}} =
  \sqrt{d_{2D}^{2} + (h_{\mathrm{tx}}+h_{\mathrm{rx}})^{2}} .
\end{equation}
With wavelength \(\lambda\), the coherent two-ray model adds the direct and
ground-reflected fields before converting to dB:
\begin{equation}
  E_{\mathrm{total}}
  =
  \frac{e^{-j2\pi d_{\mathrm{dir}}/\lambda}}{d_{\mathrm{dir}}}
  +
  \Gamma
  \frac{e^{-j2\pi d_{\mathrm{ref}}/\lambda}}{d_{\mathrm{ref}}},
\end{equation}
where \(\Gamma\) is the effective ground-reflection coefficient. The received
field magnitude \(|E_{\mathrm{total}}|\) is then converted to a path-loss-like
dB prediction with a fitted calibration constant. This is the physical origin
of the radial rings later exploited by the path-loss prior.
```

## SC-024 - Make Two-Ray Explanation Visual Or Simpler

File: `state_of_art.tex`

I would add a small schematic immediately after the two-ray equations. If there is no ready figure, use a simple TikZ figure.

Exact figure block:

```latex
\begin{figure}[ht]
  \centering
  \begin{tikzpicture}[scale=0.9]
    \draw[thick] (-0.5,0) -- (7,0);
    \node[below] at (3.2,0) {ground};
    \filldraw[blue] (0.5,3.0) circle (2pt) node[left] {UAV Tx};
    \filldraw[black] (6.2,0.35) circle (2pt) node[right] {ground Rx};
    \draw[->,thick] (0.5,3.0) -- node[above] {direct path} (6.2,0.35);
    \draw[->,thick,dashed] (0.5,3.0) -- node[left] {reflected path} (3.2,0);
    \draw[->,thick,dashed] (3.2,0) -- (6.2,0.35);
    \draw[<->] (0.2,0) -- node[left] {\(h_{\mathrm{tx}}\)} (0.2,3.0);
    \draw[<->] (6.5,0) -- node[right] {\(h_{\mathrm{rx}}\)} (6.5,0.35);
  \end{tikzpicture}
  \caption{Direct and ground-reflected paths in the two-ray model.}
  \label{fig:two_ray_schematic}
\end{figure}
```

If space is too tight, skip the figure and keep only the clearer text from SC-023.

## SC-025 - Replace Vague "Morphology"

File: `state_of_art.tex`

Exact replacement:

```latex
city or environment types
```

instead of:

```latex
morphology types
```

Use "morphology" only after a definition, e.g.:

```latex
In the rest of the thesis, morphology means these city/environment categories
as inferred from building density and building height.
```

## SC-026 - Replace "Polynomials"

File: `state_of_art.tex`

Exact replacement:

```latex
path-loss expressions
```

instead of:

```latex
path-loss polynomials
```

## SC-027 - Add Formulas For Delay And Angular Spread

File: `state_of_art.tex`

Insert after lines 128-132:

```latex
For multipath components with powers \(P_\ell\), delays \(\tau_\ell\), and
azimuth angles \(\phi_\ell\), the RMS delay spread is
\begin{equation}
  \bar{\tau} =
  \frac{\sum_\ell P_\ell \tau_\ell}{\sum_\ell P_\ell},
  \qquad
  \tau_{\mathrm{rms}} =
  \sqrt{
  \frac{\sum_\ell P_\ell(\tau_\ell-\bar{\tau})^2}{\sum_\ell P_\ell}
  } .
\end{equation}
For angular spread, the mean angle must be computed circularly:
\begin{equation}
  \bar{\phi} =
  \operatorname{atan2}\!\left(
    \sum_\ell P_\ell \sin\phi_\ell,
    \sum_\ell P_\ell \cos\phi_\ell
  \right),
  \qquad
  \sigma_{\mathrm{AS}} =
  \sqrt{
  \frac{\sum_\ell P_\ell\,\operatorname{wrap}(\phi_\ell-\bar{\phi})^2}
       {\sum_\ell P_\ell}
  } ,
\end{equation}
where \(\operatorname{wrap}(\cdot)\) maps angle differences to the
\((-\pi,\pi]\) interval.
```

## SC-028 - Reuse Benchmark Numbers In Results

File: `results.tex`

The results chapter already contains a comparison table at lines 807-922. I would keep it and make sure it includes the RadioUNet and RadioGUNet numbers from SOTA.

Exact action:

- Keep the existing `RadioUNet` row.
- Keep the existing `RadioGUNet` row.
- In Chapter 2, remove final-result claims and write "These numbers are used again in Chapter~\ref{chap:results} as scale references."

Exact SOTA sentence after RadioGUNet numbers:

```latex
These values are used again in Chapter~\ref{chap:results} as scale references
for the final path-loss result.
```

## SC-029 - Add Consistent "Limitations" Paragraphs In SOTA

File: `state_of_art.tex`

For each SOTA subsection, add a short limitations paragraph. Example for RadioUNet/RadioGUNet:

```latex
\textbf{Limitations:} These papers are useful path-loss scale references, but
they do not report dense delay-spread or angular-spread maps and do not use the
CKM city-holdout, continuous UAV-height contract.
```

Example for PMNet:

```latex
\textbf{Limitations:} PMNet is a strong image-to-image radio-map benchmark, but
its challenge setting uses a different dataset, fixed rooftop-style
transmitters, a narrower target image window, and a masking convention that is
not the same as the CKM ground-receiver evaluation.
```

Example for transformers/foundation models:

```latex
\textbf{Limitations:} These models improve global context or pretraining
capacity, but the reported evaluations do not match the CKM setting of unseen
cities, continuous UAV altitude, \(513\times513\) outputs, and joint PL/DS/AS
prediction.
```

## SC-030 - Refer To Table 2.1 Explicitly

File: `state_of_art.tex`

Exact replacement for line 189:

```latex
Multiplying normalised RMSE by~36 gives the rough dB-scale references listed
in Table~\ref{tab:icassp2023corrected}.
```

## SC-031 - Review CKM Comparability Paragraph

File: `state_of_art.tex`

Exact replacement for lines 217-225:

```latex
\textbf{Limitations:} These values are scale references only. They are not
directly comparable to CKM because RadioMap3DSeer uses a different dataset,
fixed transmitter placement, a much narrower target image window, and a
different building-pixel convention. The CKM task later evaluated in this
thesis uses unseen real-city geometries, native \(513\times513\) maps,
continuous UAV altitude, and metrics over valid ground receiver pixels.
```

## SC-032 - Move PMNet Transfer-Test Results Out Of Background

File: `state_of_art.tex`

Delete lines 227-233 from Chapter 2.

Move the information to either Chapter 4 or Appendix A. I would put it in Appendix A because it is a diagnostic negative result, not the final result.

Appendix text:

```latex
\paragraph{PMNet transfer check.}
A separate diagnostic placed official PMNet checkpoints on CKM samples. The
best zero-shot result was approximately \SI{84}{dB} RMSE, with most models
collapsing to a nearly constant prediction. Even after oracle linear
calibration from test data, the minimum achievable RMSE was still approximately
\SI{42}{dB}. This check is not used as a final benchmark; it only confirms that
PMNet's strong challenge score does not transfer directly to the CKM contract.
```

## SC-033 - Review Transformer/Global-Context Claim

File: `state_of_art.tex`

Exact replacement for lines 248-252:

```latex
Recent attention and foundation-model variants extend the effective receptive
field of radio-map predictors \cite{wicopg2025,fmrme2026}. This is useful when
large-scale urban context affects the prediction, but these methods normally
need more data and compute than convolutional models and their reported
benchmarks do not match the CKM UAV-height contract.
```

## SC-034 - Review Foundation-Model Horizon Claim

File: `state_of_art.tex`

Exact replacement for lines 267-270:

```latex
\textbf{Limitations:} These foundation approaches are relevant as long-term
background, but they require training corpora and compute budgets beyond a
single CKM dataset. They are therefore cited as future context, not as methods
directly compared with the final thesis model.
```

## SC-035 - Explain Why Training Stabilisation Is Needed

File: `state_of_art.tex`

Insert after line 479, before `\subsection{Stochastic weight averaging}`:

```latex
The methods in this section are included because dense radio-map prediction is
easy to overfit. The model sees complete city maps with strong spatial
correlations, while validation and test cities are completely held out. Small
training subsets, heavy-tailed NLoS errors, and quantized targets can make the
training loss improve even when the deployment-relevant city-holdout error does
not. Stabilisation and regularisation techniques are therefore not cosmetic
training tricks; they are safeguards against selecting a model that only fits
the training cities.
```

## SC-036 - Fix Target Quantity Terminology And Units

File: `state_of_art.tex`

Exact replacement for lines 532-533:

```latex
  \item \textbf{Target quantity and units:} path loss (dB), path gain (dB),
        received power (dBm), delay spread (ns), or angular spread (degrees).
```

## SC-037 - Move Final-Model Values Out Of SOTA Table

File: `state_of_art.tex`

Exact action:

- Delete row lines 568-569 from Table `tab:fairness`, or replace it with a non-result contract row:

```latex
This thesis task contract & Yes & Yes & Yes & Reference contract \\
```

- Delete Table `tab:position` lines 704-729 from Chapter 2.
- Keep comparison table in `results.tex` lines 807-922.

## SC-038 - Rename Dataset Protocol

File: `methodology.tex`

Exact replacement for line 14:

```latex
\section{Dataset and split}
```

instead of:

```latex
\section{Dataset protocol}
```

## SC-039 - Add Height-Distribution Figure

File: `methodology.tex`

I would create a figure file:

```text
img/thesis_figures/dataset/uav_height_distribution.pdf
```

from `CKM_Dataset_270326.h5`, plotting the empirical `uav_height` histogram with the four reporting bins:

```text
<50 m, 50-150 m, 150-300 m, >300 m
```

Insert after line 68:

```latex
\begin{figure}[ht]
  \centering
  \includegraphics[width=0.82\textwidth]{img/thesis_figures/dataset/uav_height_distribution.pdf}
  \caption{Empirical UAV transmitter-height distribution in the CKM dataset.
  The vertical lines mark the reporting bins used later in the results:
  below \SI{50}{m}, \SIrange{50}{150}{m}, \SIrange{150}{300}{m}, and above
  \SI{300}{m}.}
  \label{fig:uav_height_distribution}
\end{figure}
```

Then refer to it before the paragraph:

```latex
Figure~\ref{fig:uav_height_distribution} shows the empirical height distribution.
```

## SC-040 - Rewrite Methodology Around Final Method

File: `methodology.tex`

Exact restructuring:

1. Keep section 1, renamed to `Dataset and split`.
2. Delete/move `\section{Diagnostic baselines retained from development}` lines 140-159 to Appendix A.
3. Delete/move `\section{Methodology structure after the development lessons}` lines 161-199 to Appendix A.
4. Replace them with a final pipeline overview.

Exact replacement after the dataset section:

```latex
\section{Final pipeline overview}

The final method is a prior-anchored residual pipeline. For each CKM sample, the
input preparation stage provides the topology map, the geometric LoS/NLoS mask,
the ground-receiver mask, the UAV height, and three frozen prior maps: one for
path loss, one for delay spread, and one for angular spread. These priors are
fitted only on training cities. The neural model then predicts residual
corrections around the priors instead of predicting the full maps from zero.

The pipeline has four reproducible stages:
\begin{enumerate}
  \item define the city-holdout split and the valid ground-receiver mask;
  \item calibrate the path-loss prior and the spread priors on training cities;
  \item train \textsc{AnchorGMM} as a shared residual model over the frozen
        priors;
  \item evaluate the frozen priors and the final residual model on the same
        held-out test cities.
\end{enumerate}

The development history that led to this structure is preserved in
Appendix~A. The main methodology focuses on the final reproducible system.
```

## SC-041 - Remove "Free-Space-Like"

File: `prior_detail_try78.tex`

Exact replacement for lines 769-772:

```latex
\item $\lambda_0$: a free-space reference offset that scales with UAV height and
      frequency~\cite{khawaja_survey,wocc2021}. The CKM dataset uses
      $f = 7.125$ GHz (FR3 6G frequency band); for
      $h_{\mathrm{tx}} = 50$ m at that frequency, $\lambda_0 \approx 83.5$ dB.
```

## SC-042 - Delete "The Addition Of 1 Is Not Cosmetic"

File: `prior_detail_try79.tex`

Exact replacement for lines 12-15:

```latex
The constant 1 keeps exact zeros finite, avoids \(\log(0)\), and makes the same
transform usable for both delay spread in nanoseconds and angular spread in
degrees. If two pixels have native spread values \(y_a\) and \(y_b\), their
difference in transformed space is
```

## SC-043 - Results Chapter Should Focus On Final Results

File: `results.tex`

Exact restructuring:

1. Keep the opening paragraph, but make it shorter.
2. Remove/move the milestone table lines 20-49 to Appendix A.
3. Move `RMSE evolution and interpretation` and intermediate distribution-first sections to Appendix A or a short "Diagnostic context" appendix.
4. Start the main results with final priors and final model.

Exact replacement for lines 4-18:

```latex
This chapter reports the final quantitative and qualitative outcomes of the
thesis. All main numbers use the same final 2590-sample, 14-city test split and
the same valid ground-receiver mask. The frozen priors are reported first
because they are part of the final system, not weak baselines. The final
\textsc{AnchorGMM} model is then compared with those priors, with the original
thesis targets, with the closest external path-loss benchmarks, and with the
ray-tracing runtime baseline.
```

Exact new first section title:

```latex
\section{Final test contract and frozen priors}
```

Move the old experiment timeline to Appendix A with this intro:

```latex
\section{Development results moved from the main chapter}

The following tables preserve the intermediate milestones used during
development. They are diagnostic evidence, not the main thesis result, because
masking rules, objectives, and model families changed during the project.
```

## SC-044 - Reframe Economic Impact

File: `sustainability_balanced.tex`

Exact replacement for lines 74-82:

```latex
\section{Economic and social impact}

The economic value of the final model is its potential to reduce repeated
ray-tracing runs during UAV network planning. In the Barcelona runtime check,
the complete generator produced the three dense maps in \SI{0.88}{s}, compared
with \SI{99.89}{s} for the MATLAB ray-tracing path used as reference. This
does not remove the need for ray tracing or field validation, but it changes
where expensive simulation is spent: planners can use the surrogate to screen
many UAV heights, city layouts, and candidate deployments, then reserve detailed
simulation or measurement for the most relevant cases.

In practical terms, the final model could lower the marginal cost of what-if
studies. A network planner could quickly compare whether raising the UAV,
moving it to another candidate site, or changing the service area improves
ground-user coverage before launching a full deterministic simulation. The
economic impact is therefore not the training cost of this academic prototype,
but the possible reduction in repeated planning time once a validated surrogate
is reused.
```

Keep the social-impact paragraphs after this replacement.

## SC-045 - Positive Note

No action needed. I would not create a checklist task for this. If the surrounding conclusion is shortened, preserve the idea that the final distribution-aware design was motivated by earlier failures.

## SC-046 - Move Struggles To An Annex

File: `conclusions.tex`

Exact replacement for lines 158-172:

```latex
\subsection{Negative results}

The main negative-result lesson is that plausible-looking radio maps are not
enough. Earlier direct-regression and image-translation models could reproduce
some visual structure while still missing NLoS path-loss modes and rare
spread-tail regions. This is why the final thesis uses calibrated priors and a
distribution-aware residual model instead of only scaling up a generic neural
backbone. The detailed attempt trace and failed branches are kept in
Appendix~A, where they can be useful for reproducibility without interrupting
the main argument.
```

## Extra Cleanup Connected To Several Comments

### Acronyms

Add to `acronyms.tex` if using UxNB:

```latex
\DeclareAcronym{UxNB}{
  short = UxNB,
  long  = UAV-mounted radio access node,
  tag = abbrev
}
```

### Section 2 Final Cleanup Pass

After all SOTA edits, run this search:

```powershell
rg -n "final model|this thesis.*achiev|1\\.65|26\\.56|11\\.39|Final model \\(this thesis\\)|prior-anchored residual GMM-head model" C:\TFG\FINAL_THESIS\reduced\TFG\state_of_art.tex
```

Expected result: no numeric final results in `state_of_art.tex`. It is acceptable to keep neutral phrases like:

```text
the methodology in Chapter 3
the evaluation contract used in this thesis
```

### Sections 3 And 4 Final Cleanup Pass

After moving chronology to the appendix, run:

```powershell
rg -n "first implementation|next phase|development lessons|chronological|earlier models|attempt|Try~|failed|struggles" C:\TFG\FINAL_THESIS\reduced\TFG\methodology.tex C:\TFG\FINAL_THESIS\reduced\TFG\results.tex
```

Expected result: only very short diagnostic references in the main text. Detailed attempt history should appear in `appendices_compact.tex`.

### Results Comparison Table

Keep the Chapter 4 comparison table, but make the wording more neutral:

```latex
The table is a context table, not a leaderboard. The only directly comparable
rows are the frozen priors and \textsc{AnchorGMM}, because they share the CKM
test split, target definitions, and ground-receiver mask.
```

