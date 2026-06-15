# Sergi SA Revision Plan, 2026-06-15

Source inputs for this pass:

- `C:/Users/guill/Downloads/TFG--SA.pdf`
- Extracted non-link annotations: `C:/TFG/output/pdf/SA_revision_pdf_annotations.md`
- Email screenshot with general chapter comments
- Screenshot notes on Section 2.2.1, Figure 3.12, Section 3.6.3 constants, and Chapter 4 results

Important scope note: previous Sergi/Evgenii plans are treated as solved historical context. This plan only tracks comments from the new SA PDF and the new screenshots. When an item is already answered in the current source, the action is to verify or lightly polish, not to redo old restructuring.

User override added during implementation: the Work plan/Gantt must remain in
Chapter 1. The PDF comment suggesting moving it to an appendix is intentionally
ignored; the action is only to define the section more clearly. Also, per city
results should use the latest final CSVs when available. Training cities should
not be reported as generalisation results because the model and priors were
fitted with those cities.

## Comment Map and Actions

| ID | Source | Comment | Current status after source check | Planned action |
|---|---|---|---|---|
| SA-001 | PDF p.2 | Define acronyms in the abstract too. | Not fully answered. `summary.tex` uses CKM, UAV, LoS/NLoS, HARP-Net, DS/AS style terms without expansion. | Expand first use in Catalan, Spanish and English summaries. Keep translated prose with accents. |
| SA-002 | PDF p.15 | Define each acronym the first time it appears in text. | Partially answered by `acronyms.tex`, but Chapter 1 still uses UxNB, CKM and UAV before friendly expansion. | Rewrite the first introduction paragraphs so CKM, UAV and UxNB are introduced plainly at first use. |
| SA-003 | PDF p.15 | “UAV mounted ... UxNB ... on board a UAV” is redundant; highlighted `UAV-mounted`. | Needs edit. Current sentence repeats the definition. | Replace with one concise sentence: a UxNB is a 3GPP radio access node mounted on a UAV. Avoid needless repetition. |
| SA-004 | PDF p.15 | “studies or proposes?” | Needs edit. Current sentence says the thesis “studies HARP-Net CKM”. | Change to “proposes and evaluates” for the final system, while “studies” remains for the problem. |
| SA-005 | PDF p.15 | Highlighted unclear “????” in Chapter 1 opening. | Needs edit. Current wording about same fixed centre task and other elevated nodes is heavy. | Simplify the paragraph and move detailed simulation contract wording to requirements or methodology. |
| SA-006 | PDF p.15 | Highlight “experiments, the”. | Minor grammar issue. | Add a comma and smooth the phrase: “For the CKM experiments, the ...”. |
| SA-007 | PDF p.15 | “this has been mentioned before.” | Partially answered, but HARP-Net name and pipeline are repeated in the opening. | Merge the repeated HARP-Net definition into one paragraph and remove the second definition block. |
| SA-008 | PDF p.16 | Chapter 4 appears before the outline explains all chapters. | Needs edit. Current Work goals mentions Chapter 4 before the thesis outline. | Replace with “the results chapter” or move that runtime sentence into the outline/results discussion. |
| SA-009 | PDF p.17 | `two-ray` wording. | Needs consistency check. The source mostly uses “two-ray”. | Keep “two-ray” as the house style unless needed as a compound modifier. Rephrase awkward “two-ray LoS propagation” as “LoS propagation based on the coherent two-ray model.” |
| SA-010 | PDF p.17 | “train calibrated” sounds unclear. | Needs edit in Chapter 1 and results. | Replace visible prose uses with “calibrated only on training cities” or “training-city calibrated”. |
| SA-011 | PDF p.17 | Always refer to figures and tables in text. | Mostly answered for Gantt and methodology figures. | Verify new moved figures and added tables are referenced before or immediately after they appear. |
| SA-012 | PDF p.17 | “I would move this to an appendix.” | User explicitly overrode this comment. The Work plan/Gantt belongs in Chapter 1. | Keep the Work plan in Chapter 1 and define it more clearly. Do not duplicate it in the appendix. |
| SA-013 | PDF p.20 | Chapter 2 reader map has vague references and skips Sections 2.3/2.4. | Needs edit. Current opening has two separate reader map paragraphs and says Sections 2.1 to 2.2, then “the angular and delay spread sections”. | Fuse the opening and reader map into one clearer paragraph naming all major sections. |
| SA-014 | PDF p.20 | CKM acronym appears many times before definition. | Partly solved by Chapter 1, but abstract and Chapter 2 still need local clarity. | Define CKM in abstract and Chapter 1; in Chapter 2 opening, write “channel knowledge map (CKM)” if it is the first visible use in the chapter. |
| SA-015 | PDF p.21 and screenshot | Delete crossed out part in two-ray subsection. | Needs edit. `state_of_art.tex` still says the numerical gain is not reported here and fitted result is later in Chapter 4. | Delete the crossed out sentence. Keep Chapter 2 as physics/background only. |
| SA-016 | PDF p.22 and email | Chapter 2 mixes background and state of the art. | Partially answered by the chapter title, but the flow still blends classical models, recent papers and thesis design implications. | Add clearer subsection framing: background model paragraphs first, then related-work implications. Remove result style claims from Chapter 2. |
| SA-017 | PDF p.31 and email | Introduction should summarize state of the art, gap, objectives and contribution. | Partially answered by RQs, but missing a concise SOTA/gap paragraph before RQs. | Add a structured Chapter 1 paragraph: existing radio-map work is strong on easier contracts, but dense PL/DS/AS with continuous UAV height and city holdout is the gap. Link this to RQs. |
| SA-018 | PDF p.33 | Explain why these choices: GMM, U-Net, FiLM. | Partially answered across Chapter 2 and 3, but not as a clear rationale near the method overview. | Add a short “Design rationale” paragraph in Chapter 3 before the residual model: U-Net for dense maps, FiLM for continuous height, GMM/residual heads for multimodal and heavy tailed residuals, priors because physics is stable. |
| SA-019 | PDF p.39 | “How did you arrive to equations like this?” for support features such as blocker/clearance/tall building maps. | Partially answered by definitions, but derivation/provenance is weak. | Add a short derivation note before those equations: they are map derived approximations of blocker depth, transmitter clearance and over-UAV obstruction, chosen from geometry/morphology inspection and then judged by the ridge calibration, not fitted constants. |
| SA-020 | PDF p.47 | Table captions on top. | Needs edit. Some tables in `prior_detail_try78.tex` and `prior_detail_try79.tex` still put captions below the table. | Move captions above tabulars for affected tables and check the main document for remaining bottom captions in Chapter 3. |
| SA-021 | Screenshot Section 3.6.3 | Make constants more explicit, how derived or approximated. | Partially answered by Table 3.10 and prose, but still vague. | Expand Section 3.6.3: anchors came from coarse training data inspection and rounded target scale, topology offsets from observed topology ordering, and weights from hand tuned sign/magnitude approximations later corrected by ridge calibration. State they are fixed heuristics, not learned ridge weights. |
| SA-022 | Screenshot Figure 3.12 | Move Figure 3.12 diagram to Section 3.7, not 3.8. | Needs verification. Current residual architecture and loss figures are in `prior_detail_try80.tex`; compiled numbering may put the detailed GMM diagram too late. | Move the detailed HARP-Net/GMM diagram block immediately after the first Section 3.7 residual model introduction, before later subsections that can drift it to Section 3.8. Use `[!htbp]` or `[H]` only where it avoids wrong-section placement. |
| SA-023 | PDF p.71 and screenshot | What is generally considered a good RMSE for PL, DS, AS? | Partially answered by targets and SOA tables, but not concise enough at the start of results. | Add a “how to read RMSE” paragraph in Results: a few dB PL is strong for this strict CKM contract; DS/AS have no directly comparable dense per pixel benchmark, so targets and same protocol priors are the main reference. |
| SA-024 | User note about goals | Mention that PL/CA is very good for such a dataset; DS/AS are not generally calculated per pixel in comparable work. | Partially answered in Results and Chapter 2, but should be more explicit near Work goals or RQs. | Add one sentence to Work goals and one result-facing sentence in the SOA context. |
| SA-025 | PDF p.71 and screenshot | Show results per city. | The latest Try80 CSVs already contain per city validation/test rows. | Add compact validation and test per city tables from the final CSVs, plus topology and antenna height proportions. Omit train because it is not comparable for generalisation. |
| SA-026 | PDF p.83 and screenshot | Move the qualitative inspection figure earlier and explain it more; use it to explain method from ground truth to priors to corrections and final results. | Needs edit. Current Figure 4.1 is at the end in Qualitative Analysis. | Move the figure near the beginning of Chapter 4, before standalone prior subsections. Add text that explains each row: target, prior, residual/error, prediction, and what it says about the pipeline. |
| SA-027 | Email | Chapter 1 is chaotic; use paper-introduction structure. | Partially answered but still dense. | Restructure the opening as short paragraphs: general 6G/CKM context, UAV context, motivation, SOTA/gap, objectives, method/results summary, thesis organization. |
| SA-028 | Email | Chapter 3 has many details and may be hard to follow. | Partially answered with diagrams and guide table. | Add choice rationale, keep details final-method first, and avoid adding more chronology. If moving Figure 3.12 creates clutter, keep only the essential architecture diagram in main text. |
| SA-029 | Email | Chapter 4 should be qualitative first, then quantitative by city/profile, then average. | Needs edit. Current Chapter 4 starts with aggregate prior numbers and leaves qualitative analysis last. | Reorder Chapter 4: begin with the representative panel as reader map, then per city/profile grouped results, then aggregate headline metrics. Keep old aggregate tables but reposition their interpretation. |
| SA-030 | Email | Take care of acronyms and formal things. | Needs verification. | After edits, run searches for first-use acronyms, bottom captions, unresolved comments, and compile warnings. |

## Implementation Order

1. Patch Chapter 1 and the abstracts first: acronym definitions, cleaner introduction structure, less redundant UxNB/HARP-Net wording, clearer goals and SOTA gap.
2. Patch Chapter 2: fuse reader map, delete the crossed out two-ray sentence, separate background from related work more clearly.
3. Patch Chapter 3: add design rationale, improve support feature and raw spread constant provenance, move affected figure(s), and move table captions above tables.
4. Patch Chapter 4: move the representative inspection panel earlier, add RMSE interpretation, add per city results once the subagent output is available, and make the flow qualitative then grouped quantitative then aggregate.
5. Keep the Work plan/Gantt in Chapter 1, polish its wording, and ensure it is not duplicated in the appendix.
6. Run LaTeX compile and visual/PDF text checks for section placement, captions, figure references and first acronym uses.

## Verification Checklist

- [ ] `summary.tex` defines CKM, UAV, LoS/NLoS and HARP-Net CKM in all visible abstracts.
- [ ] Chapter 1 no longer repeats the UxNB definition or repeats HARP-Net explanation twice.
- [ ] Chapter 1 includes a compact SOTA/gap paragraph tied to RQs.
- [ ] “train calibrated” no longer appears in reader-facing prose unless explicitly explained.
- [ ] The crossed out Chapter 2 two-ray sentence is gone.
- [ ] Chapter 2 reader map mentions the whole chapter, not only Sections 2.1 to 2.2.
- [ ] Chapter 3 explains why the final choices are priors, U-Net, FiLM and GMM/residual heads.
- [ ] Section 3.6.3 states how the raw constants were approximated and that the ridge stage is the fitted part.
- [ ] Figure 3.12 or the intended detailed residual diagram appears in Section 3.7, not after Section 3.8 starts.
- [ ] Captions in the affected Chapter 3 tables are above the tables.
- [ ] Chapter 4 starts with the representative visual panel or introduces it before the quantitative blocks.
- [ ] Results include per city metrics or a documented blocker from the DirectML recalculation.
- [ ] Results explicitly explain what counts as “good RMSE” under this dataset contract.
- [ ] DS/AS comparison text says dense per-pixel DS/AS prediction is not directly available in the reviewed literature.
- [ ] `latexmk -pdf -interaction=nonstopmode -halt-on-error TFG.tex` succeeds from `FINAL_THESIS/reduced/TFG`.
