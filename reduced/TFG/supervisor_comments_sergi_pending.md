# Sergi Supervisor Comments - Pending Fix List

Source PDF: `C:/Users/guill/Downloads/TFG_draft_21may_GV--SA.pdf`

Source email: Sergi Abadal, attached PDF with comments on top of Genia's comments.

Scope: the PDF comments were made on an older draft. This file lists what still needs
attention after comparing those comments with the current local reduced thesis in
`reduced/TFG`. Page numbers refer to the annotated PDF, not necessarily to the
current compiled thesis.

Annotation count used for this pass: 109 PDF annotations, of which 66 contained
explicit text comments. Empty highlights and strikeouts were grouped with the
nearest explicit comment when their intent was clear.

## General Comments From Sergi's Email

Sergi's main message is structural rather than local. The thesis should assume
less prior knowledge from the reader, especially in the introduction. It should
also organize the information more clearly. Chapter 3 is the clearest problem:
it has too many sections and subsections, and the final method is still mixed
with the history of how the method was discovered. Sergi also asks for an
appendix declaration explaining whether generative AI was used in the thesis
and how.

## Highest Priority Remaining Work

- [ ] SG-001 - Add a generative AI use declaration appendix
  - Old PDF page: email comment, no PDF page.
  - Refers to: "as an appendix, I would like you to make a declaration of whether you have used generative AI in the thesis and how."
  - Current local status: missing. No current `reduced/TFG` file contains a generative AI declaration.
  - What to do: add a short appendix section after the current appendices. It should state which tools were used, for which tasks, what was checked by the author, and that technical responsibility remains with the author.

- [ ] SG-002 - Restructure Chapter 3 around the final method
  - Old PDF pages: 34, 36, 38, 86, and the email.
  - Refers to: comments that Chapter 3 is too large, hard to follow, too chronological, and should show what worked instead of the full struggle.
  - Current local status: partially addressed. Appendix A now keeps the attempt trace, but Chapter 3 still contains a long "Physical priors and PMHHNet" section, "Mathematical Evolution", "Limitations and Legacy", distribution first development, component count, loss functions, hyperparameters, training progression, and final priors. The current table of contents still shows many Chapter 3 entries.
  - What to do: make Chapter 3 final method first. A cleaner structure would be:
    1. Dataset, masks, split, and evaluation contract.
    2. Overall pipeline and block diagram.
    3. Frozen priors: channel attenuation, angular spread, and delay spread.
    4. `\textsc{HARP-Net CKM}` input contract and architecture.
    5. Losses, training setup, and evaluation protocol.
  - What to move out: PMHHNet history, failed residual phases, long distribution diagnosis, and detailed training progression should move to Appendix A or Appendix D unless they are needed to justify one final design choice.

- [ ] SG-003 - Add a clear methodology block diagram
  - Old PDF page: 34.
  - Refers to: "I miss a methodology figure that exemplifies in a block diagram kind of way, the overall methodology of the thesis."
  - Current local status: partially addressed. Chapter 3 has a framework data flow section and detailed model diagrams, but no single high level diagram that shows the full thesis pipeline end to end.
  - What to do: add a compact figure near the start of Chapter 3:
    `topology map + UAV height -> masks and priors -> frozen PL/DS/AS prior maps -> HARP-Net CKM residual model -> final CKM outputs -> masked city holdout evaluation`.
  - Keep it reader facing. The detailed FiLM and GMM diagrams can stay later or move to an appendix if Chapter 3 remains too long.

- [ ] SG-004 - Simplify the introduction for reader onboarding
  - Old PDF pages: 16, 17, 18, 19, plus email.
  - Refers to: unexplained terms at the start, too many technical solution details, and a too chronological explanation.
  - Current local status: much improved but not fully settled. The current introduction defines UxNB, channel attenuation terminology, city holdout, HARP-Net CKM, and the three targets. However, it still includes a "Methods and procedures" section, which Sergi explicitly suggested removing from the introduction because Chapter 3 is the methodology chapter.
  - What to do: either remove Section 1.5 or reduce it to a very short plain language bridge. Keep all architecture details, GMM details, FiLM details, PMHHNet history, and distribution diagnosis out of Chapter 1.

- [ ] SG-005 - Give Chapter 2 a clearer background versus state of the art structure
  - Old PDF pages: 21, 22, 23, 26, 29, 33.
  - Refers to: Sergi getting lost in Chapter 2, too many sections and subsections, possible separation between background and state of the art, and quantitative thesis results mixed with literature.
  - Current local status: partially addressed. The chapter title now says "State of the Art and Technical Background", and the chapter has more limitations text. It still has many small sections and may still feel like a long catalogue.
  - What to do: reorganize Chapter 2 so each major block has the same pattern: concept needed later, representative papers, limitations for this thesis. Keep final thesis result values out of Chapter 2 except when explicitly saying they will be compared in Chapter 4.

- [ ] SG-006 - Clean the bibliography, especially arXiv entries
  - Old PDF page: 110.
  - Refers to: "For all papers where you have an ARXIV URL: check if there is a conference/journal version..."
  - Current local status: pending. This needs a source by source bibliography audit.
  - What to do: for each arXiv only entry, search whether a conference, journal, or IEEE/ACM version exists. If it exists, cite that version instead and add volume, issue, pages, DOI, and publisher data where available. Keep arXiv only for true preprints.

- [ ] SG-007 - Expand the sustainability economic impact discussion
  - Old PDF page: 104.
  - Refers to: "potential economic impact of your final model", patenting, selling, company creation, operator use, and applications enabled by more accurate radio maps.
  - Current local status: partially addressed. The current chapter discusses planning workflows and reduced repeated simulation, but it does not yet answer the commercialization and operator value questions directly.
  - What to do: add a paragraph on possible value paths: network planning tools, UAV coverage planning, emergency or temporary deployments, operator what if analysis, licensing or software service potential, and the fact that patentability would depend on novelty beyond known CKM and radio map prediction methods.

- [ ] SG-008 - Keep Chapter 4 focused on final results and literature comparison
  - Old PDF pages: 86, 116, 126.
  - Refers to: present only final results and compare them with previous papers; consider whether appendix panels belong in results.
  - Current local status: mostly addressed, but verify. Chapter 4 now has final results and a state of the art context section. It still includes diagnostic references and points to appendix panels.
  - What to do: check that every Chapter 4 subsection either reports final priors, final HARP-Net CKM results, final diagnostics needed for interpretation, or literature comparison. If a panel is essential evidence, keep one representative panel in results and keep the full gallery in the appendix.

## Medium Priority Remaining Work

- [ ] SG-009 - Run a global acronym and jargon audit
  - Old PDF pages: 2, 16, 17, 21, 22, 29.
  - Refers to: acronyms defined after first use, acronyms defined more than once, and terms such as FiLM, GMM head, PMHHNet, FR3, city holdout, and ground only being introduced too early or without explanation.
  - Current local status: partially addressed. The introduction now avoids several old problems, and `acronyms.tex` includes key definitions. The full document still needs a pass because Chapter 2 and Chapter 3 use many technical terms.
  - What to do: search the compiled text or source for first occurrence of each acronym. Use `\ac{}` where possible. In the introduction, keep only terms a new reader can understand immediately.

- [ ] SG-010 - Audit path loss, channel attenuation, gain, and received power terminology
  - Old PDF pages: 16, 21, 29.
  - Refers to: use "channel attenuation" for the predicted CKM dB target, keep "path loss" for true path loss formulas and dataset/code names, avoid mixing path gain and received power.
  - Current local status: mostly addressed in the introduction and many current chapters. Some older text and captions may still use path loss too freely.
  - What to do: keep the current terminology note, then review every prose use of "path loss". Accept it in standard propagation models, cited path loss priors, dataset field names, code labels, PL abbreviations, and historical model names. Prefer "channel attenuation" for the final predicted dense dB target.

- [ ] SG-011 - Audit equation numbering and equation references
  - Old PDF pages: 34, 37.
  - Refers to: all important equations should have numbers, and references should use `\eqref{}`.
  - Current local status: partially addressed. Some equations were numbered, but this needs a mechanical pass.
  - What to do: search for `Eq.~`, `Eq.`, and direct equation numbers in prose. Replace with `\eqref{...}`. Ensure displayed equations that are referenced use numbered environments.

- [ ] SG-012 - Reduce odd precision in background numeric values
  - Old PDF page: 24.
  - Refers to: values such as `0.007148`, `0.01046`, and `0.008099` having too many decimals for thesis prose.
  - Current local status: pending unless already removed during later edits.
  - What to do: use two or three significant figures in prose, or scientific notation only where it improves readability. Keep full precision only in reproducibility tables if needed.

- [ ] SG-013 - Make the two ray explanation self contained
  - Old PDF page: 22.
  - Refers to: define the direct and reflected fields, include height dependent expression or an illustrative diagram, and justify where the calibrated result comes from.
  - Current local status: mostly addressed. The current version has a corrected diagram and a clearer two ray section. Still verify the paragraph does not claim the 1.75 dB result without pointing to Chapter 4 or the methodology prior evaluation.
  - What to do: ensure Chapter 2 explains the physics only, while Chapter 4 reports the numeric result.

- [ ] SG-014 - Explain why training stabilization techniques are needed
  - Old PDF page: 29.
  - Refers to: need a paragraph before SWA, EMA, FiLM, and related methods.
  - Current local status: likely partially addressed, but Chapter 2 should be checked after the structural rewrite.
  - What to do: add a short reader bridge: city holdout and small per regime subsets make validation noisy and overfitting easy, so the later methodology uses regularization and stable validation choices.

- [ ] SG-015 - Decide whether some path loss prior background belongs outside Chapter 3
  - Old PDF page: 34.
  - Refers to: Chapter 3 may contain material that is really background.
  - Current local status: still relevant. Some prior theory and PMHHNet history in Chapter 3 could be moved to Chapter 2 or Appendix A.
  - What to do: keep only final prior construction in Chapter 3. Move general propagation background to Chapter 2 and failed prior variants to Appendix A.

## Already Mostly Resolved, But Verify Before Final Compile

- [x] SG-DONE-001 - Add UxNB and cite 3GPP
  - Old PDF page: 16.
  - Current local status: fixed in `introduction.tex` and `acronyms.tex`.

- [x] SG-DONE-002 - Use a clearer final framework name
  - Old PDF pages: 16 and 17.
  - Current local status: fixed with `\textsc{HARP-Net CKM}`.

- [x] SG-DONE-003 - Clarify LoS/NLoS mask input
  - Old PDF page: 16.
  - Current local status: fixed in the introduction and methodology input contract.

- [x] SG-DONE-004 - Add channel attenuation terminology note
  - Old PDF page: 16.
  - Current local status: fixed in the introduction. Needs only the global terminology audit in SG-010.

- [x] SG-DONE-005 - Define city holdout and ground receiver evaluation
  - Old PDF pages: 17 and 18.
  - Current local status: fixed in the introduction and methodology.

- [x] SG-DONE-006 - Add chapter numbers to the outline
  - Old PDF page: 18.
  - Current local status: fixed in `introduction.tex`.

- [x] SG-DONE-007 - Move the work plan to the end of Chapter 1
  - Old PDF page: 18.
  - Current local status: fixed. The Gantt appears after the methods/procedures section.

- [x] SG-DONE-008 - Improve the Gantt plan
  - Old PDF page: 18, plus later supervisor requests.
  - Current local status: fixed in the current branch after removing final review and extending work packages into mid June.

- [x] SG-DONE-009 - Add height distribution context
  - Old PDF page: 34.
  - Current local status: fixed. Chapter 3 includes transmitter height density.

- [x] SG-DONE-010 - Define `Beta(4,4)`
  - Old PDF page: 34.
  - Current local status: fixed.

- [x] SG-DONE-011 - Remind the reader what dataset is used before pixel detail
  - Old PDF page: 34.
  - Current local status: fixed in the introduction and dataset section.

- [x] SG-DONE-012 - Move long struggles to an appendix
  - Old PDF pages: 36 and 108.
  - Current local status: partially fixed and mostly working. Appendix A now keeps the development trace. Chapter 3 still needs the structural pass in SG-002.

- [x] SG-DONE-013 - Add limitations paragraphs to state of the art sections
  - Old PDF page: 23.
  - Current local status: mostly fixed. Verify consistency after the Chapter 2 rewrite.

- [x] SG-DONE-014 - Keep selected qualitative panels in the thesis
  - Old PDF pages: 116 and 126.
  - Current local status: mostly fixed. The reduced thesis keeps three full size panels and stores the remaining gallery externally or in appendix context.

## Page By Page Map

- Page 2: acronym definition and delay/angular spread wording. Covered by SG-009.
- Pages 16 to 19: introduction onboarding, naming, city holdout, mask input, terminology, chapter outline, and chronology. Mostly fixed, but SG-004, SG-009, and SG-010 remain.
- Pages 21 to 33: Chapter 2 structure, background versus state of the art, two ray explanation, spread formulas, limitations paragraphs, precision, training stabilization bridge, and misplaced quantitative comparison. Covered by SG-005, SG-012, SG-013, and SG-014.
- Pages 34 to 38: Chapter 3 structure, dataset reminder, height distribution, methodology diagram, numbered equations, PMHHNet chronology, and legacy material. Covered by SG-002, SG-003, SG-011, and SG-015.
- Page 59 and page 69: local wording strikeouts around path loss and explanatory overstatement. Covered by SG-010 and the local prose cleanup pass.
- Page 86: results should focus on final results and comparison. Covered by SG-008.
- Page 104: sustainability economic impact and operator value. Covered by SG-007.
- Pages 107 to 108: conclusions should mention appendix for struggles rather than keeping them in the main text. Mostly fixed through Appendix A; verify after SG-002.
- Page 110: bibliography quality and arXiv replacement. Covered by SG-006.
- Pages 116 and 126: decide whether appendix figures or documentation should be in results. Covered by SG-008 and SG-DONE-014.

## Suggested Implementation Order

1. Add the generative AI declaration appendix.
2. Restructure Chapter 3 and add the block diagram.
3. Simplify or remove the introduction methods/procedures section.
4. Reorganize Chapter 2 after Chapter 3 has its final shape.
5. Polish Chapter 4 around final results, external comparison, and essential panels.
6. Expand the sustainability economic impact paragraph.
7. Run the global terminology, acronym, equation reference, precision, and bibliography audits.
