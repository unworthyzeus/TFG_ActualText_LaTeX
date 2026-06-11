# GMG Revision 11/6: Delivery Draft Plan

Status: working Markdown version for the GMG revision to deliver after applying the reviewed methodology fixes, metric definitions, valid range corrections and results structure updates.

Source PDF: `C:\Users\guill\Downloads\26_06_09_TFG_Guillem_GV.pdf`
Extracted annotations: 53 total, including 33 text comments and 20 markup annotations.
Raw JSON: `C:\TFG\output\pdf\EV_revision_9-6_pdf_annotations.json`

## Code Verification Notes

I checked this plan against the current thesis source in `C:\TFG\FINAL_THESIS\reduced\TFG`, the final Try 80 code, and the CKMGenerator LoS code. The reviewer comments below are extracted from the PDF annotations. The nearby PDF snippets are only context because formula text can be garbled by PDF extraction.

Verified implementation facts:

1. Try 80 reads `topology_map`, `los_mask`, `path_loss`, `delay_spread`, `angular_spread`, and `uav_height` directly from the HDF5 file.
2. Ground pixels are defined as `topology == 0.0`. Losses and reported metrics are computed on valid ground pixels, with separate LoS and NLoS summaries.
3. The final Try 80 input tensor has 9 channels: normalized topology, LoS mask, NLoS mask, ground mask, path prior, LoS path prior, NLoS path prior, delay prior, and angular prior.
4. The direct geometry uses a 513 by 513 grid with zero based indices and transmitter center `(256, 256)`, so the thesis should not switch to `(257,257)` unless it explicitly changes to one based notation.
5. The receiver height is fixed at 1.5 m and the pixel pitch is 1 m in the final code.
6. The final Try 80 frozen path loss prior uses Try 78 for LoS and NLoS path loss, and Try 79 for delay and angular spread priors.
7. The code fixes morphology window sizes at 15 and 41 pixels. If the thesis cannot cite an ablation for these values, present them as implementation choices, not as experimentally optimal constants.
8. CKMGenerator has a fallback ray casting LoS routine, but the final Try 80 dataset path uses the stored HDF5 `los_mask`; the fallback should not be described as the final evaluation path unless we add a separate validation note.

Editorial recommendations in the plan are marked as changes to wording or structure, not as claims about code behavior.

## First Fix Plan

### A. Chapter 3 structure
1. Keep the chapter opening short and point explicitly to Figure 3.1. Add one sentence like "The complete flow is shown in Figure 3.1" before describing the figure.
2. Remove the struck introductory paragraphs that explain the pipeline ordering twice. Keep only one compact version of the split of responsibility: shared support maps, frozen priors, residual model.
3. Move `General Framework and Data Flow` before the shared support map section, immediately after the dataset and split section. In the compiled chapter this makes the framework section become 3.2, which matches the reviewer concern that the current 3.3 should really be 3.2.
4. After moving the framework section, let the shared support maps section become the next section. This makes the reader see the full pipeline first, then the map definitions used by the pipeline.
5. Move "pixel weighted RMSE over valid ground pixels" out of the maps section into a visible evaluation subsection, probably just before or inside Training and Evaluation Protocol, so it appears in the table of contents.
6. Delete or compress the stage based overview in the early framework section if it duplicates Figure 3.1 and the later prior subsections. The code does not require the word "stage" as an API concept; it is only a writing device. Keep the actual pipeline operations, but present them as data flow steps.

### B. Shared support maps
1. Define the index convention explicitly. To match the implementation and transmitter center, use zero based pixel coordinates: H = W = 513, i,j in {0,...,512}, and x_tx = (256,256). If the thesis chooses one based notation instead, change the center consistently to (257,257).
2. Keep g(x) as the valid ground receiver mask. Rename or remove b(x) as a standalone thesis level "feature" because it is exactly 1 - g(x). The code uses building occupancy internally as `buildings = 1 - ground` for support features, but it is not an independent model input channel. If the complement is needed, use `m_B(x)` instead of `b(x)` to avoid collision with bias terms.
3. Move "building pixels are not receivers, so they are removed from loss functions and metrics" to the evaluation contract. In the shared support map section, say only that Omega_g is the valid receiver set.
4. Delete d_3D notation. Use d_LoS everywhere for the direct 3D path length.
5. Simplify the normalized elevation angle to theta_norm = clip(2 theta / pi, 0, 1), or explain that 180 theta / 90 pi is just unit conversion from radians to degrees divided by 90 degrees.
6. Clarify the LoS/NLoS mask source. Code check: for the thesis experiments, the final Try 80 dataset path uses the stored HDF5 LoS mask restricted by g(x). The ray casting mask is optional deployment logic and should be shortened or moved to an appendix unless it is evaluated.
7. Put intuition before equations in the ray casting paragraph if it remains.
8. Explain BoxMean_15 and BoxMean_41 before formalizing them. Code check: these are fixed as `KERNEL_SIZES = (15, 41)`. Say that 15 captures near receiver texture and 41 captures a wider urban block context. Do not call them empirically optimal unless we add evidence for an ablation.

### C. Symbols and notation
1. Rename local building density rho_k to something not confused with the LoS reflection amplitude, for example delta_k or D_k. This matches the code feature names `density_15` and `density_41` better than rho_k.
2. Rename LoS bias b(h_tx) to beta_LoS(h_tx), and avoid using b for both building mask and bias.
3. Define rho, phi and beta_LoS before the prior overview uses them, or defer their detailed appearance to the LoS prior section.
4. After renaming, update equations, tables, figures and captions consistently in methodology.tex, prior_detail_overview.tex, prior_detail_try78.tex and prior_detail_try79.tex.

### D. Prior overview
1. Compress the "prior is not Bayesian" paragraph to one sentence or remove it. EV marked it as over explaining.
2. Keep the overview conceptual. Avoid listing symbols in the overview before they are introduced.
3. Make the overview say what each prior does, then let the detail sections define the formulas.

### E. LoS channel attenuation prior
1. Delete the duplicated "Geometry and distances" subsection in prior_detail_try78.tex, because d_LoS and d_ref are already defined in the shared support map section.
2. Delete or reduce the FSPL textbook explanation. Refer to Chapter 2 and to the FSPL equation only if the exact implemented form is needed.
3. Start the LoS detail at the new contribution: fitted effective two ray correction, height binned calibration, bias and radial residual.
4. Keep one compact table of LoS terms. Remove the long diagnostic vector or shorten it, because several entries are already defined above.
5. Remove repeated explanations across pages 47 to 50 so the section focuses on what changes relative to the literature model.

### F. NLoS channel attenuation prior
1. Remove or rename "Stage 1", "Stage 2", and similar headings unless the chapter first defines the stage sequence. The code does not expose these as external stages; they are writing labels.
2. If the labels are kept, fix hierarchy: "Stage 1: raw NLoS propagation prior" should contain COST 231 and A2G as subparts, not appear at the same level.
3. Reduce textbook COST 231 and A2G exposition. Keep the implemented equations, the caveat that they are feature bases, and the train only calibration role.
4. Remove results style statements from methodology, or move them to Chapter 4.
5. Keep the 15 feature vector, but avoid redefining shared support maps. Use "as defined in the shared support map section".

### G. Delay and angular spread prior
1. Replace "native spread" with "ground truth spread in original units" or simply "spread in original units".
2. Explain how the fixed constants were obtained once, preferably in the table caption or a short sentence before Table 3.x. Do not repeat the numeric constants in both prose and the table.
3. Remove "Stage" wording from the spread prior headings too. Use descriptive headings such as "Raw log spread prior", "Spread feature vector", "Regime wise ridge calibration", and "Inverse transform and clipping".
4. Keep h_norm, b_41, c_41 and t_41 definitions in the shared support map section. In the spread prior section, refer back to those definitions instead of repeating them.
5. Replace the repeated six class topology paragraph with "as defined in Eq. 3.34".

### H. Figures and layout
1. Check figure font sizes from page 68 onward. EV says that page gives the minimum acceptable font size.
2. After edits, compile the PDF and visually inspect pages 33 to 68 because the changes remove text and may shift figures.
3. Recheck references after section moves, especially equation numbers and ToC entries.

## Extracted Text Comments

### C01. Page 33
- How to fix: Rewrite the chapter opening so it names Figure 3.1 explicitly, then describe the figure in one short paragraph before any detailed pipeline text.
- Comment: "shown in Fig 3.1." and describe it here.
- Nearby text: Methodolo | e prediction pipeline: the CKM dataset co | el weighted metrics, calibrated priors, and H

### C02. Page 36
- How to fix: Rename this part as the common geometry and support map setup, then define the quantities once before they are reused by priors and the model.
- Comment: geometry
- Nearby text: ior is evaluated, the raw map is converted int | s. This section defines those maps once, bec | enuation prior, the two spread priors and th | geometric contract. | 513, let 𝑥= (𝑖, 𝑗) denote a pixel, and let the t | he topology matrix is:

### C03. Page 36
- How to fix: Define H and W as 513 and state the index convention. The code uses zero based coordinates with i,j in {0,...,512} and transmitter center (256,256); only use one based notation if the whole chapter is converted consistently.
- Comment: define what are H and W. state the values that can be taken by i and j | [1 513]
- Nearby text: support maps. This section d | the NLoS attenuation prior, t | use the same geometric cont | Let 𝐻= 𝑊= 513, let 𝑥= (𝑖, 𝑗 | (256, 256). The topology mat | 𝐻×𝑊

### C04. Page 37
- How to fix: Delete b(x) as a standalone thesis level feature. Keep g(x) for valid ground receivers; if the building complement is needed later, call it m_B(x) and define it as 1 - g(x).
- Comment: if it's equal to g and is also binary (i.e., has absolutely the same info), do not use it.
- Nearby text: receiver pixel, and 𝑏(𝑥) = 1 means that 𝑥is | exact zero for ground, while CKMGenerator | array inputs with numerical noise are hand | 𝛺g = {(𝑖, 𝑗) ∶𝑔𝑖𝑗= 1 | xel in 𝛺g is a ground receiver. Building pi | from loss functions, metrics and LoS/NLoS

### C05. Page 37
- How to fix: Move the sentence about buildings being removed from losses and metrics to the evaluation contract or loss section. In the support map section, only define Omega_g as the valid receiver set.
- Comment: this should be said in the place where you describe the loss finction, not here
- Nearby text: handled safely. The valid receiver set is: | 𝑗= 1}. | (3.8) | ng pixels are not receivers, so they are | NLoS region masks. | from the centered transmitter is: |

### C06. Page 37
- How to fix: Remove every use of d_3D and use d_LoS for the direct 3D path length throughout equations, prose, figures and captions.
- Comment: just do not use d_3d anywhere
- Nearby text: The only other 3D p | reflection distance: | Thus 𝑑3𝐷is not a sep | two ray path. | The elevation angle

### C07. Page 37
- How to fix: Rewrite the normalization as theta_norm = clip(2 theta / pi, 0, 1), and add one explanatory sentence saying it is theta divided by 90 degrees when theta is measured in radians.
- Comment: 90 pi? | can you explain this to me during the meeting?
- Nearby text: −ℎrx, max(𝑑2𝐷(𝑥), 1)) , | (3.1 | by zero below the UAV. The normalized ang | p(180 𝜃(𝑥) | 90𝜋 | , 0, 1) , | (3.1 | −𝜃norm(𝑥). | (3.1

### C08. Page 37
- How to fix: State that the final Try 80 experiments use the stored HDF5 los_mask multiplied by the ground mask. Move ray casting to optional fallback or appendix text unless a validation result is added.
- Comment: i thought you calculated LOS/NLOS masks. here it looks you took it from the dataset. | what did you do at the end? | if the final version uses the calculated maps, only describe those.
- Nearby text: r grazing links that | map. In the HDF5 | to ground receivers: | (3.15) | (3.16)

### C09. Page 38
- How to fix: Move the intuition paragraph before the equations: first explain that the ray is sampled between transmitter and receiver and is blocked if terrain exceeds the line height, then show the formulas.
- Comment: move it above. | the golden rule: first you explain the logic/intuition and then you formalize it in math.
- Nearby text: (3.22) | (3.23) | long the horizontal | r and receiver cells | osses the height of | NLoS; otherwise it

### C10. Page 38
- How to fix: If the fallback ray casting mask remains in the thesis, add its validation error in Chapter 4. If no validation result is included, shorten this paragraph to a deployment note only.
- Comment: hm, ok. in the results you will need to show what is the error.
- Nearby text: masks are multiplied by 𝑔(𝑥). CKMGenerato | when it exists; otherwise it uses (3.22). Th | topology only deployment, but it is not exp | mask because the original simulator and the | ray tracing engine. | The local morphology features are also co

### C11. Page 38
- How to fix: Introduce BoxMean_15 and BoxMean_41 before the equations: 15 is local receiver context and 41 is wider urban block context. Since the code fixes these constants, do not call them optimal unless an ablation is added.
- Comment: 1) first describe the purpose of those boxes | 2) unclear. what are those 15 and 41? different sizes for averaging? why these numbers ("empirically defined" is fine as an explanation)?
- Nearby text: mask because the origin | ray tracing engine. | The local morphology | 𝑘∈{15, 41}, let BoxMea | BoxMean

### C12. Page 39
- How to fix: Remove result reporting height intervals from the map section. Keep only the calibration height key if it is needed for formulas, and move reporting interval discussion to Chapter 4 or an appendix.
- Comment: this does not belong here. talk about the results in the next section.
- Nearby text: m, | (3.35) | rvals used only for | ove 300 m. Finally,

### C13. Page 39
- How to fix: Rename the density symbol from rho_k to delta_k or D_k, then update all equations and captions so rho is reserved for the LoS reflection amplitude.
- Comment: rho is very easy to confuse with the reflection term you use later while these two rho have nothing in common. | | use a different (new) symbol here. maybe some version of "b" as it is derrived from buildings
- Nearby text: used because the calibrated attenuation pri | rent levels of granularity. Both are compute | ap = | 1 | 𝐻𝑊∑ | 𝑥 | 𝑏(𝑥), | ∑𝑥𝑇(𝑥)𝑏(𝑥)

### C14. Page 40
- How to fix: Create a visible Evaluation Contract subsection and move the pixel weighted RMSE formula there, so it appears in the table of contents and is easy to find.
- Comment: it does not belong to "maps". it's an "evaluation metric". might even be a separate subsection (to appear in the ToC - to be found easily)

### C15. Page 40
- How to fix: Move General Framework and Data Flow immediately after Dataset and split, so it becomes the new Section 3.2 and the reader sees the whole pipeline before the map definitions.
- Comment: explain to me the logic of putting it after the map section but before the priors, please.
- Nearby text: 3.3 | General Framework a | Table 3.2: External framework inputs, interna | outputs. | Stage | Maps / variables

### C16. Page 41
- How to fix: Do not introduce rho, phi or beta_LoS in the overview without definitions. Either add a small symbol table before the bullets or keep those symbols only in the LoS prior detail section.
- Comment: define if smth hasn't been defined yet. | - is rho = the map prior? | - what is phi? didn't see it in sec 3.
- Nearby text: m a coherent direct | ndent dB offset; and | horizontally, so the | 𝜌(ℎtx), 𝜙(ℎtx), 𝑏(ℎtx) | nearly interpolated | not a learned linear

### C17. Page 41
- How to fix: Rename the LoS bias from b(h_tx) to beta_LoS(h_tx) everywhere, because b is already associated with buildings in the reader's mind.
- Comment: b is building. using it for "bias" is confusing
- Nearby text: correction. The word prio | physical hint: | • LoS path loss prio | 𝑏+ 𝑟. FSPL uses the | plus ground reflecte | 𝑟is a smoothed radi

### C18. Page 46
- How to fix: Delete the repeated geometry, FSPL and two ray derivation from this section. Replace it with references to the shared support map section and Chapter 2, then focus on what is new in the implemented prior.
- Comment: already defined. delete. | you also already described FSPL and 2 ray in section 2. refer to those sections and eqs and that's it. | | please avoid repeating yourself. | | | in this section, focus only on smth new in comparison to section 2.
- Nearby text: defined. | (𝑥)2 + (ℎtx −ℎrx)2 | (3.3 | ween the two antennas in 3D space. Becaus

### C19. Page 47
- How to fix: Start the LoS prior detail at the fitted coherent two ray correction and height dependent calibration. Check the preceding paragraphs and delete any overlap with Chapter 2 or the shared map definitions.
- Comment: i guess, the new part starts from here. check please and ensure 0 overlap/redundency
- Nearby text: + 𝛤𝑒−𝑗2𝜋𝑑ref/𝜆 | 𝑑ref | (3.41) | fficient. In the standard textbook derivation, | he ground material. Here, it is replaced by

### C20. Page 48
- How to fix: Cut or merge this practical explanation into the previous paragraph. Keep only the implementation specific point that textbook reflection is replaced by fitted effective parameters.
- Comment: not sure how to feel about this. | kinda also feels redundant after the previous page.
- Nearby text: e literature: | he practical | ut the way | ted variant | ation is the

### C21. Page 49
- How to fix: Delete terms already defined above from the diagnostic vector or table. Keep only the calibrated LoS terms that are genuinely introduced in this subsection.
- Comment: most of these (if not all) are already defined above. delete redundant
- Nearby text: d the carrier frequency. | ce and frequency scale | and the image source | ratio is normally below

### C22. Page 50
- How to fix: Consolidate repeated definitions into one canonical location. In later occurrences, use a short reference instead of redefining the same distance, phase, bias or residual terms.
- Comment: toooooo redundant, you defined all of them too many times
- Nearby text: . | ground re- | tive to the | tion phase | of assum- | nt.

### C23. Page 53
- How to fix: Keep a short method note for now, but move any interpretation of fitted values or performance to Chapter 4 during the results pass.
- Comment: for now, let's keep this text here. but i think it belongs to "results"
- Nearby text: 3.5 - Channel Attenuation Prior | y parameters by height bin. | ) | ̃𝑏(dB)

### C24. Page 54
- How to fix: Delete textbook style COST 231 or A2G exposition unless an implemented equation depends on it. Replace with a short statement that these formulas are used only as frozen feature bases.
- Comment: looks textbook. might be deleted too.
- Nearby text: ay + bias

### C25. Page 54
- How to fix: Apply the same redundancy cut as in LoS: remove section 2 style background from pages 54 to 56, keep implemented equations, and explain the train split calibration role.
- Comment: same logic as in los: delete redundencies, do not paste content from section 2 | == | from here to page 56
- Nearby text: or urban macro cells gives the | 11]. It is included because it is | ell loss, even though the CKM | ion height range. None of the | y transferred absolute predictor | ght sensitive basis that the train

### C26. Page 54
- How to fix: Remove the Stage 1 wording if possible. If it must stay, make COST 231 and A2G clearly nested under the raw NLoS prior heading, not peer headings.
- Comment: currently, it looks like "stage 1" and "COST" etc are at the same level whle "cost" are sub parts of stage 1. | think how to fix this (e.g., use underline or italic)
- Nearby text: uilt in five stages. | ation prior | es are combined. | OST-231 / Hata extension for urban macro

### C27. Page 62
- How to fix: Trace the constants to the Try 79 code or calibration artifact, then state their source once in the table caption. Keep the numbers in the table only, not duplicated in prose.
- Comment: how have these numbers been obtained? | do not repeat them twice: keeping them in the table is a better idea
- Nearby text: + 𝑎2𝜃inv | (3.74) | ple coefficients for | 11.0 ns, which the

### C28. Page 62
- How to fix: Replace native spread with spread in original units or ground truth spread, depending on the sentence.
- Comment: what "native spread" means? maybe there's a better word? measured? ground truth?
- Nearby text: ed. Their empirical distributions are common | dard channel models [12, 17]. For a spread | 𝑧(𝑥) = log(1 + 𝑦(𝑥)), | 𝑦 | two pixels with native spread values 𝑦𝑎and

### C29. Page 63
- How to fix: Remove Stage 1 references from the spread prior sequence. Use descriptive headings such as Raw log spread prior and Spread feature vector, or define the sequence before Stage 2 appears.
- Comment: what's and whre's "stage 1"?
- Nearby text: her. | ad prior | nd design matrix | 0)(𝑥)2, 𝑧(0)(𝑥), log(1 + 𝑑2𝐷), 𝜃norm, 𝜃inv | ℎ, ℎ2 | , 𝜌, 𝜌, ℎ, ℎ | ⎤⎥ | ⊤

### C30. Page 65
- How to fix: Move h_norm, b_41, c_41 and t_41 to the shared support map definitions. In the spread prior section, refer back to those map features instead of redefining them.
- Comment: it looks like a map feature to me. it mustn't be here | same for 3.77-3.79
- Nearby text: 1], using log(401) | bove that relative | is intentional: the | r splitting samples | 0 m to estimate a | 2, which is an

### C31. Page 66
- How to fix: Delete the repeated topology class definition if it already appears above. Replace it with a reference to the earlier topology class equation.
- Comment: haven't you defined it above? if yes - delete
- Nearby text: ally useful for distinguishing dense but low | ss topology definition. | The spread prior | final prior code. Their thresholds and clas | are map level routing keys for the spread prio | el morphology features.

### C32. Page 66
- How to fix: Replace the repeated paragraph with the short phrase as defined in the topology class equation, using the final equation number after recompilation.
- Comment: instead of the text above, just add here "as defined in 3.34"
- Nearby text: hey are not additional | ology class (6 classes), | to 2 × 6 × 2 × 3 = 72 | lds as (3.35): low_ant

### C33. Page 68
- How to fix: Use this page as the minimum figure font benchmark. Re export later figures with at least this font size and inspect the compiled PDF pages visually.
- Comment: for the following figures: this is the minimal acceptable font

## Extracted Markup Annotations

### M01. Page 33, StrikeOut
- Action: Delete this sentence or fold it into the single compact opening that points to Figure 3.1.
- Marked text: The ordering matters: derived from topology

### M02. Page 33, StrikeOut
- Action: Replace the long opening with a shorter paragraph that states the final pipeline scope and points to Figure 3.1.
- Marked text: This chapter defines the reproducible prediction pipeline: the CKM dataset contract, receiver mask, city holdout split, pixel weighted metrics, calibrated priors, and HARP- Net CKM residual prediction for channel attenuation, delay spread, and angular spread. For readability, the implementation is grouped into map support quantities, calibrated prior maps and the residual neural model. This grouping

### M03. Page 33, StrikeOut
- Action: Delete the duplicate grouping explanation. Keep only one short sentence saying Appendix A contains development history.
- Marked text: grouped into map support quantities, calibrated prior maps and the residual neural model. This grouping guides the data flow without implying a strict preprocessing checklist: some quantities are computed from geometry, some are fitted on the training cities, and some are learned by the neural residual model. Appendix A keeps the development history; this chapter keeps the final pipeline and reproduction details.

### M04. Page 36, StrikeOut
- Action: Repair the broken phrase so it clearly says the support maps provide a common geometric contract for the attenuation and spread priors.
- Marked text: attenuation prior, the two geometric contract.

### M05. Page 37, StrikeOut
- Action: Rewrite as one concise sentence: receiver height is fixed, while transmitter height changes per sample and is the only scalar radio geometry input besides topology.
- Marked text: transmitter height ℎtx changes besides the topology map.

### M06. Page 37, Highlight
- Action: Move this highlighted sentence to the Evaluation Contract subsection and keep only the definition of Omega_g in the support map section.
- Marked text: 𝛺g Building pixels are not receivers, so they are removed from loss functions, metrics and LoS/NLoS region masks.

### M07. Page 37, StrikeOut
- Action: Delete the d_3D alias from the equation.
- Marked text: = 𝑑3𝐷(𝑥) =

### M08. Page 37, StrikeOut
- Action: Rewrite this block using d_LoS and d_ref only, with direct and reflected distances defined once.
- Marked text: √𝑑2𝐷(𝑥)2 The only other 3D path length used by the final LoS prior is the image source reflection distance:

### M09. Page 37, StrikeOut
- Action: Delete this explanatory sentence after removing d_3D, because the notation will no longer exist.
- Marked text: √𝑑2𝐷(𝑥)2 Thus 𝑑3𝐷is not a separate feature from 𝑑LoS. two ray path.

### M10. Page 38, Highlight
- Action: Move this caveat to optional fallback discussion or appendix text. If kept in the main chapter, add a result that quantifies the mask difference.
- Marked text: but it is not expected to be bit identical to the stored CKM mask because the original simulator and the lightweight generator do not share the full ray tracing engine.

### M11. Page 39, StrikeOut
- Action: Move reporting height intervals to the results chapter and keep h_norm in the shared support feature definitions.
- Marked text: This calibration key is different from the four broader height intervals used only for result reporting: below 50 m, 50 m to 150 m, 150 m to 300 m, and above 300 m. Finally, the normalized scalar height feature used in the spread vector is:

### M12. Page 39, Highlight
- Action: Move the RMSE formula to the Evaluation Contract subsection.
- Marked text: All RMSE values in this thesis are pixel-weighted over valid ground pixels: RMSE = √ ∑𝑠,𝑖,𝑗𝑚𝑠(𝑖, 𝑗) ( ̂𝑦𝑠(𝑖, 𝑗) −𝑦𝑠(𝑖, 𝑗))2 ∑𝑠,𝑖,𝑗𝑚𝑠(𝑖, 𝑗) . (3.37) 39

### M13. Page 40, Highlight
- Action: Move this explanatory paragraph with the RMSE formula into the same Evaluation Contract subsection.
- Marked text: Chapter 3. Methodology This is stricter than averaging per sample RMSEs because large valid maps contribute proportionally to the number of receiver pixels. The same evaluation contract is used for channel attenuation, delay spread and angular spread. For the two spread targets, every non building pixel is also a receiver pixel in the CKM ground truth, so the reported spread RMSE is simply the dense prediction compared with the dense ray-traced ground truth over all valid ground receivers.

### M14. Page 41, StrikeOut
- Action: Compress this Bayesian prior disclaimer to one sentence, or remove it if the overview already says priors are frozen deterministic maps.
- Marked text: The term prior is not used here in the Bayesian sense of a probability distribution over model parameters or targets, and no posterior inference is performed in the prior stage. It denotes deterministic, frozen estimator maps computed before the neural residual correction.

### M15. Page 41, StrikeOut
- Action: Merge with the previous sentence or delete it to avoid repeating the definition of prior.
- Marked text: denotes deterministic, frozen estimator maps computed before the neural residual correction. The word prior is therefore used for three concrete estimators, not for a vague physical hint:

### M16. Page 46, StrikeOut
- Action: Delete this repeated geometry, figure and FSPL block from the LoS detail section; replace it with cross references.
- Marked text: at −ℎtx) to the receiver. Since (ℎtx + ℎrx) ≥|ℎtx −ℎrx| for any nonnegative heights, we always have 𝑑ref(𝑥) ≥𝑑LoS(𝑥). In the present UAV to ground setting with ℎtx > 0 and ℎrx > 0, the reflected path is strictly longer; in the limiting geometric case where one antenna is exactly on the ground plane, it would be equal rather than longer. ground image source height UAV (ℎtx) Rx (ℎrx) image (−ℎtx) 𝑑LoS reflected 𝑑ref 𝑑2𝐷 Figure 3.5: Two ray geometry. Direct path (blue) has length 𝑑LoS; reflected path (green) has the same total length as the image source path (gray dashed), which is 𝑑ref. Free-space path loss baseline The free space path loss in dB is defined using the standard formula at frequency 𝑓MHz (in MHz): FSPL(𝑥) = 32.45 + 20 log10(𝑑LoS(𝑥) 1000 ) + 20 log10(𝑓MHz) (3.40)

### M17. Page 46, StrikeOut
- Action: Delete this duplicated direct and reflected distance derivation because the definitions already belong in shared support maps.
- Marked text: The direct path (LoS) distance is: 𝑑LoS(𝑥) = √𝑑2𝐷(𝑥)2 + (ℎtx −ℎrx)2 (3.38) This is simply the Euclidean distance between the two antennas in 3D space. Because 𝑑2𝐷(𝑥) ≥0 and the squared height difference (ℎtx−ℎrx)2 is nonnegative, 𝑑LoS(𝑥) ≥𝑑2𝐷(𝑥), with equality only when both antennas are at the same height. The reflected path (image) distance is: 𝑑ref(𝑥) = √𝑑2𝐷(𝑥)2 + (ℎtx + ℎrx)2 (3.39) This is the distance from the image source (the UAV mirrored below the ground plane at −ℎtx) to the receiver. Since (ℎtx + ℎrx) ≥|ℎtx −ℎrx| for any nonnegative heights, we always have 𝑑ref(𝑥) ≥𝑑LoS(𝑥). In the present UAV to ground setting with ℎtx > 0 and ℎrx > 0, the reflected path is strictly longer; in the limiting geometric case where one antenna is exactly on the ground plane, it would be equal rather than longer.

### M18. Page 47, StrikeOut
- Action: Delete the textbook physical meaning paragraph or replace it with a short Chapter 2 reference.
- Marked text: Physical meaning. FSPL grows quadratically with distance (∝𝑑2) and quadratically with frequency. It captures only the geometric spreading of the wavefront, with no ground interaction, scattering, or diffraction.

### M19. Page 59, StrikeOut
- Action: Fix the broken wording to say that the coefficients are stored in JSON, if this sentence is still needed.
- Marked text: have to JSON stores

### M20. Page 59, StrikeOut
- Action: Rewrite the phrase as calibration coefficients are stored in JSON, or delete it if the storage detail is not useful for methodology.
- Marked text: calibration is JSON
