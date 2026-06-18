# Supervisor Comments Action Plan, 2026-06-18

Source comments were extracted from `C:\Users\guill\Downloads\26_06_18_TFG_Guillem_GV.pdf`. This file turns those comments, the extra screenshot notes, and the HARP-Net CKM contribution note into concrete edits for the thesis source under `reduced/TFG`.

## Overall Plan

1. Make the abstract and introduction readable without assuming the reader already knows the project.
2. Keep the main body focused on the final system names: calibrated attenuation prior, calibrated spread priors, and `\textsc{HARP-Net CKM}`. Move internal names such as `Try 78` and `Try 80` to the appendix or reproducibility notes unless the paragraph is explicitly about experiment history.
3. Strengthen the contribution statement: `\textsc{HARP-Net CKM}` predicts channel attenuation, delay spread and angular spread jointly, uses sinusoidal FiLM for UAV height, and uses a GMM residual head to model the output specific residual distributions.
4. Polish Chapter 1 wording using Sergi's introduction notes.
5. Normalize section style: use `Limitations` headings, remove repeated phrases, and add a few `\textbf{...}` labels in long methodology paragraphs.

## Extra Required Contribution Wording

Use this idea in both `reduced/TFG/introduction.tex` and `reduced/TFG/conclusions.tex`:

```tex
\textsc{HARP-Net CKM} is a variable height CKM predictor that jointly estimates
channel attenuation, delay spread and angular spread for unseen city layouts.
Its contribution is not only that the three outputs are predicted together. The
model uses sinusoidal FiLM conditioning to inject continuous UAV transmitter
height into the shared backbone, and a task aware GMM residual head to predict
residual distributions specific to channel attenuation, delay spread and angular
spread around their frozen priors.
```
##### Notes are added below things you've put as corrections. They should be followed. My comment on this is: For conclusions is ok. But for the introduction. Reduce it a lot. Just a bit longer than what is it now.


For Section 6.1.2, I would replace the first contribution paragraph with:

```tex
The first contribution is \textsc{HARP-Net CKM}, a variable height CKM
predictor that jointly estimates channel attenuation, delay spread and angular
spread for unseen city layouts. The joint prediction is central, but it is not
the only modelling contribution: the network also uses sinusoidal FiLM height
conditioning and a GMM style residual head. FiLM lets one shared model adapt to
continuous UAV transmitter height, while the GMM head keeps several plausible
residual correction modes for each output before the deterministic map used for
RMSE is formed. This is especially important because attenuation, delay spread
and angular spread have different residual scales and tail behaviour.
```
##### Ok



## Introduction Fixes From Sergi's Notes

Apply in `reduced/TFG/introduction.tex`.

| Current wording | Fix |
|---|---|
| `site specific` | `site-specific` |
| `support environment aware planning` | `support environment-aware planning` |
| `UAV mounted radio access node` | `UAV-mounted radio access node` |
| `as a UAV operating at \SI{7.125}{GHz}` | `as a UAV operating at a given carrier frequency, which is \SI{7.125}{GHz} in this dataset` |
| `over the same \(513\times513\) city map` | `over the same city map` |

Move `\section{Thesis outline}` so it comes after `\section{Work plan}`. Sergi explicitly wants the thesis outline after the work plan, as the last section of Chapter 1.
##### Ok, but be careful moving the section that all tables and figures are in the correct place and they don't leave a lot of space.


## Detailed Comment Actions

| Source | Comment or mark | What I would do | Comments by the User |
|---|---|---|---|
| Page 2, abstract note | The abstract should be understandable without reading the thesis. It should state UAVs are base stations, not users, avoid overemphasizing receiver pixels, mention city types and unseen cities. | Rewrite the abstract opening with the reviewer provided text, then add one sentence about unseen city layouts and the final FiLM plus GMM model. Keep receiver pixel details to a short phrase such as `valid ground receiver evaluation`, not a full abstract topic. | Do not be add another sentence here, just put the supervisor text | 
| Page 2, highlights | `visibility information`, `complete cities outside training`, and a long final contribution sentence. | Keep the ideas but compress them. Say `strict city holdout evaluation` once. Replace the long list of `valid receiver pixels, city holdout splitting and reporting...` with `strict city holdout and LoS/NLoS aware evaluation`. | Nah, just put what the supervisor said |
| Page 12 | Reviewer says internal `Try 80` and `Try 78` names should have been abandoned in the main thesis. | Search the main body for `Try 80`, `Try 79`, and `Try 78`. In Chapters 1 to 6, replace them with descriptive names unless the paragraph is explicitly about chronological development. Suggested replacements: `calibrated attenuation prior`, `calibrated spread priors`, `final joint prior anchored residual model`, and `\textsc{HARP-Net CKM}`. Keep try numbers in Appendix A and file provenance notes. | Yes, this is totally correct. |
| Page 16 | Add more supervisor papers. `https://ieeexplore.ieee.org/abstract/document/11080135` was specifically mentioned. | Add the paper to the related work context after checking its BibTeX metadata. Do not claim a live citation count unless it is verified at the time of submission. Use it to show the thesis is aware of the supervisor's broader wireless and 6G context. | Yes |
| Page 21 | `has been defined` near repeated `channel knowledge map (CKM)`. | After CKM is defined once in Chapter 1 and once at the start of Chapter 2 if needed, use `CKM` only. Remove repeated expansions in the nearby paragraph. | Yes |
| Page 21 | `it gives LLM away too much`. | Remove over explanatory or generic wording. Replace any sentence like `This framing is more precise...` with a direct technical statement about why CKM is the right abstraction for dense radio map prediction. | No, don't do any of this. He highlights `channel knowledge map (CKM)` which means that he means that repeating this a lot means LLM. Just do what you said on the previous step and none of this |
| Page 23 | `keep [16], add this: https://arxiv.org/abs/2605.17378`. | Keep citation `[16]` and add UPSim: `UxNB Propagation Simulator for 3D Map-Driven FR3 Deployments`, arXiv:2605.17378. This fits the FR3 UxNB, map driven, visibility and altitude aware propagation context. | Yes (keep in mind what citation 16 is currently and add the other one by Vinogradov) |
| Page 26 | `add the arxive paper too`. | Add the same UPSim citation in the physical prior or simulator discussion if that section explains shadow projection, FR3, UxNB simulation, or fast alternatives to ray tracing. | Yes |
| Page 28 | Use the same style as previous sections, use `Limitations`. | Rename any local subsection such as `Limitations for this thesis` to just `Limitations`. | Yes |
| Page 28, strikeouts | `for this thesis.` twice. | Delete the trailing phrase where it is redundant. If the paragraph already sits inside this thesis discussion, the phrase adds no information. | Yes |
| Page 33, strikeout | `Synthesis:`. | Rename `Synthesis: Gap Addressed by This Thesis` to `Gap Addressed by This Thesis`, or use `Literature Gaps Mapped to Thesis Decisions` if the section is a bridge table. | Use "Gap Adressed by this thesis" | 
| Page 41 | Long paragraph. Add a few `\textbf{...}` labels. | Add only a small number of labels inside the long methodology block, for example `\textbf{Geometry.}`, `\textbf{Map support.}`, `\textbf{Topology classes.}`, and `\textbf{Height conditioning.}`. Do not turn the section into a list if the flow still reads well. | Yes, precisely |
| Page 61 | `\par?` | Add a paragraph break before the displayed or bolded item if the current PDF shows bold text running into the next sentence. Prefer `\paragraph{...}` for named mini blocks or `\par\smallskip` if it is only spacing. | Yes |
| Page 67 | `\par?` or question about bold text followed by text on the same line. | Make the style consistent. If `Fallback hierarchy.` is a label, use `\paragraph{Fallback hierarchy.}` and keep the sentence on the same line. If it starts a new logical block, put a paragraph break before it. | Yes |
| Page 76 | Empty note. | Reopen the PDF around page 76 before editing. Since the note has no text, treat it as a possible accidental comment unless visual inspection shows a marked issue. | Probably accidental, yes, don't do anything... Maybe define map corr and, specially z score a bit more explicitly actually.
| Page 93, strikeout | Remove: `The qualitative evidence supports the quantitative story without needing the full inspection gallery...` | Delete the sentence. It sounds defensive and repeats what the results chapter already shows. Let the figure caption and appendix pointer carry the point. | Yes |
| Page 104 | `i hope it was useful`. | No source edit needed. Treat as closing feedback. | Truly |

## Suggested Abstract Replacement

Use this as a compact basis for the abstract or first summary paragraph:

```tex
This thesis studies channel knowledge map (CKM) prediction for 6G networks
based on base stations deployed on unmanned aerial vehicles. The goal is to
generate dense maps of channel attenuation, delay spread and angular spread
from building maps and transmitter height, including city layouts not seen
during training. The proposed system, \textsc{HARP-Net CKM}, combines calibrated
physical and statistical priors with a shared residual neural network. The
priors model distance, geometry, urban morphology, visibility and height; the
network uses sinusoidal FiLM conditioning and a GMM style residual head to
correct the three maps jointly. The result is a reproducible and interpretable
hybrid strategy for faster dense CKM generation under strict city holdout
evaluation.
```
##### As I said use what he said
## Suggested Chapter 1 Edit Order

1. Apply the exact wording fixes from Sergi's email at the start of `introduction.tex`.
2. Move `\section{Thesis outline}` after the work plan so it is the final section of Chapter 1.
3. Strengthen the `Proposed approach and headline results` paragraph with FiLM and GMM wording.
4. Check that the `Contributions` list includes joint PL, DS and AS prediction, FiLM height conditioning, and the GMM residual head.
5. Rebuild the PDF and search the extracted text for `site specific`, `environment aware`, `UAV mounted`, `7.125GHz`, `same 513`, `Try 80`, and `Try 78`.
##### Yes just be careful with what I mentioned earlier
## Citation Notes To Verify

1. `https://arxiv.org/abs/2605.17378` is UPSim: `UxNB Propagation Simulator for 3D Map-Driven FR3 Deployments`, by Evgenii Vinogradov, submitted 2026-05-17. It is a good fit for the UxNB, FR3, map driven simulator context. Local PDF: `cited_papers/upsim2026__UPSim_UxNB_Propagation_Simulator_for_3D_Map_Driven_FR3_Deployments.pdf`.
2. `https://ieeexplore.ieee.org/abstract/document/11080135` should be added only after confirming the exact title, authors, venue and BibTeX metadata from IEEE Xplore or the supervisor.
##### Yes, but download any paper you cite.
## Final Verification Checklist

1. Compile the thesis after edits.
2. Extract text from the PDF and run search checks for the old phrases.
3. Confirm there are no visible main body occurrences of `Try 78` or `Try 80` except intentional chronology or appendix references.
4. Confirm Section 6.1.2 explicitly says that `\textsc{HARP-Net CKM}` predicts the three targets jointly and that FiLM plus the GMM residual head are part of the contribution.
5. Confirm Chapter 1 ends with the thesis outline after the work plan.
##### Yes