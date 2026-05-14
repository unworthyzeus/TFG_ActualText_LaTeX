#### Things to fix:

## Must-fix before defense
Budget vs sustainability contradict each other. budget.tex reports ~0 EUR; sustainability.tex reports ~7530 EUR. Make one table canonical, cross-reference from the other.
Try 80 placeholders leak into the abstract, results, and conclusions. Either freeze a checkpoint now with the same pixel-weighted contract as Try 78, or at minimum remove "results pending" from summary.tex and reframe as an in-flight extension.
Label collisions. prior_detail_try78_los.tex and prior_detail_try78_nlos.tex are near-duplicates of prior_detail_try78.tex and reuse the same \label{eq:d_los}, eq:cost231, fig:tworay, tab:los_params. LaTeX will warn; PDF will double-print. Delete both stub files (they're twins, not complements).
Factual typo: sustainability.tex says "RTX 2080 Ti" — the cluster is non-Ti. Same section claims "Try 76–79 required ~18h" but Try 78/79 are non-DL (CPU minutes).
High-impact additions — data already exists in the repo
These are quick wins: the numbers are sitting in JSON/CSV in the repo and simply need to be pulled into the thesis.

Addition	Where to put it	Source
Try 76 per-expert NLoS table (6 rows, 2.81–4.18 dB range)	results.tex after L110	TFGSeventySixthTry76/tmp_try76_nlos_directml_metrics.json
Try 78 LoS ablation waterfall (FSPL 3.95 → radial 3.71 → two-ray 1.75 dB)	Promote from prior_detail_try78.tex:1154 to results.tex	TFGSeventyEighthTry78/hybrid_out_final_dml/hybrid_eval_summary.json
PMNet baseline failure table (constant-predictor ~42 dB after oracle calibration)	New short section in state_of_art.tex or appendix	weird_tries/results_quad_calib/comparison.csv
9 Try 80 per-regime panels already in img/thesis_figures/ — not referenced anywhere	3×3 figure in appendices.tex	img/thesis_figures/try80_appendix_panels/*.png
Plus two that require one more evaluation run:

Per-city holdout RMSE table (at least Abu Dhabi, Rio, Shanghai + top 5) — the city-holdout claim is the thesis's strongest methodological novelty and it is currently unverified at the results level.
Per-UAV-height bin RMSE (12–50 / 50–150 / 150–300 / 300+ m) — continuous height is a stated novelty; no breakdown exists.
Try 71 RMSE-vs-coverage curve — state_of_art.tex:372-375 claims selective prediction works but no figure backs it up. Pull from cluster.
Structural gaps that a jury will flag
Introduction is missing three things every TFG needs: (1) an explicit Research Questions subsection, (2) a bulleted contributions list, (3) a thesis outline paragraph. Also no justification for the <5 dB / <50 ns / <20° targets.

Methodology is missing the two most important reproducibility artifacts:

A consolidated hyperparameter table (optimizer, LR, WD, batch, grad-accum, epochs, scheduler, augmentation) per active try. Jury-standard, currently absent.
Loss function equations for Try 76 — the figure shows map_nll, moment_match, outlier_budget, dist_kl, rmse_db but none of these are formalized beyond Eq. 3.4.
No K-choice justification for the GMM (config default K=5 vs docs/distribution_classes.md saying K=3 is sufficient — pick one and show NLL vs K).
No training-curve figures, no compute/wall-clock table.
Conclusions at 42 lines is too short. Expand to 3–5 pages with: (a) answers to the research questions (mirror the intro), (b) summary of contributions, (c) a "negative results and abandoned directions" subsection documenting what you tried and dropped (pix2pix cGAN, 6-expert partition, Try 70 quad-head, Try 71 as final, Try 76 as final) — this is jury-positive.

Narrative coherence — the Try 76 → 78 contradiction
As currently written, methodology.tex:498-502 argues "Try 76 showed priors weren't the essential ingredient" — but the very next contribution (Try 78/80) re-introduces priors as the dominant structural anchor. A reader will think these contradict. The actual logic — Try 78's fitted two-ray gave 1.75 dB LoS, beating every neural attempt, so Try 80 anchors on it as free accuracy rather than forcing the network to rediscover it — needs to be stated explicitly as a bridge paragraph.

Content that's in the wrong file
prior_detail_try80.tex (638 lines) is the thesis's main model and belongs in the methodology chapter, not in prior-detail appendices. Keep only a short cross-reference in the appendix.
prior_detail_overview.tex §"How to construct a good prior" (L102–397) is the thesis's core methodological argument. Move to methodology.
prior_detail_try78.tex (1275 lines) has ~600 lines of textbook material (FSPL derivation, Fresnel comparison) that belong in a preliminaries section or should be cut to 2–3 sentences.
The "why priors" motivation is currently scattered across three files (overview, appendices, try78) — consolidate into one page at the top of the methodology chapter.
SOA fairness — small labeling fixes with outsized credibility impact
state_of_art.tex:185-190 PMNet 1.38 dB correction assumes a 36 dB dynamic range — add a footnote with the arithmetic source from the dataset paper.
The tab:position row "Try 80 target <5 dB" sits next to others' measured numbers. Reframe as "Try 80 current validation: 1.77 dB (not final test)".
The AIRMap row should say (calibrated from 20% of test measurements) inline, not only in caption.
Gao et al. 5.6 dB appears without a section/table source — cite it or drop the number.
state_of_art.tex:270 "18% improvement" from knife-edge is stated without an in-thesis ablation — either add one from Try 67 or soften the claim.
Minor but worth noting
Abstract (summary.tex) does not mention city-holdout, UAV height range (12–478 m), or 66 cities — these are the most distinctive methodological claims.
Revised Gantt / actual-vs-planned timeline is missing from the introduction; a jury will ask about the Try 66 → Try 76 → Try 78 pivot.
appendices.tex:356-362 still contains a "Final-result placeholder" — red flag in a submitted PDF.
Representative-panels table (appendices.tex:227-247) lists 9 rows but only 3 figures are actually \includegraphics'd.
Try 77 is described in methodology as a 12-expert system but gets zero numbers in results. Either run evaluation or explicitly label "code delivered, numbers pending".
If you want, I can do the cheapest, highest-leverage batch first: pull the Try 76 per-expert JSON and Try 78 waterfall into results.tex, delete the two duplicate prior_detail_try78_los/nlos.tex files, and fix the sustainability/budget and RTX-2080 contradictions. Say the word and I'll make the edits.


#### What I said:

you are like totally wrong, first of all. 

"Must fixes":

1. True but budget is not in the project anywhere. I delete the file to not confuse you.
2. I will, just not now.
3. Are they? I think they are kinda different, check.
4. That's not true, they are 2080ti even if they are mislabeled. And well, try 76-77 needed them, and 78 and 79 needed some hours on directml to create the calibrations (it can be done on cpu too), clarify it if you want to.

High impact additions:
- Try 76 is not used in the end, but it showed me GMM worked! Maybe just add some references.
- Try 78 maybe add what worked and what didnt between the 3 priors, WHY the best one was two-ray 
-PMNet don't mention it more in the SOA, it's good in their environment, but it wasn't good in mind. At most say that their networks dirent generalice well on our dataset.
- The 9 try 80 could be included in the appendix if you want to

- Per city holdout, maybe necessary, actually create a .md in things to put on the thesis and we'll revisit later, add this as well "Try 80 placeholders leak into the abstract, results, and conclusions. Either freeze a checkpoint now with the same pixel-weighted contract as Try 78, or at minimum remove "results pending" from summary.tex and reframe as an in-flight extension."

- The per UAV height bin rmse, investigate yourself how it works in try 80 (and its included priors try 78 and 79 and include it yourself)
- The Try 71 is old, research it in the repo and if you dont find why just delete this part.

Structural gaps that a jury will flag
- This "Introduction is missing three things every TFG needs: (1) an explicit Research Questions subsection, (2) a bulleted contributions list, (3) a thesis outline paragraph. Also no justification for the <5 dB / <50 ns / <20° targets." can be found on C:\TFG\FINAL_THESIS\TFG\Internal_Documentation\project proposal and workplan (1).docx put it yourself

- The consolidated hyper parameter table could be included in a subsection, mention the ones of try 80, also the ones of try 76 and 77. And also older ones and how I used EMA, and other parameters and how they varied, it's a lot of parameters, research it and include them but focus on the later ones.
- The same for loss functions, they are there, put them in.
- The k-choice justification could be taken from an .md that is about distributions in try 76, put it and base yourself on that.
- The same for plots as per hyperparameters.

Narrative coherence — the Try 76 → 78 contradiction
- You are kinda right , maybe bullshit something. It's just that try 76 was just after the histograms showed me something was wrong. So first I fixed DL, then I decided to fix the priors, and voilah! Just invent something

Content that's in the wrong file
- The prior detail try 80 if you see the main index structure is correctly I think?
- The prior detail overview is methodology, but is structured correctly in the index. You can merge the files if you want to, but not necessary.
- Prior detail try 78 SHOULD NOT BE TOUCHED OR REDUCED.
- The "why priors" is not a priority to merge, I prefer to have multiple smaller files than one large one.

SOA fairness — small labeling fixes with outsized credibility impact
- Okay add a footnote.
- Ok fix that about try 80
- Ok fix that from the airmap
- Cite Go et al (actually research it if it's correct)
- Yeah, delete specific numbers of prior improvement like those from knife-edge. Just mention things that could be applied.

Minor but worth noting
- Yeah, maybe expand a bit the abstract.
- Yeah, it was a trial and error method. I wouldn't touch it though, I will in the end if my supervisor tells me.
- Do not touch the final results placeholder yet
- Ok you may add more figures
- Try 77 is in the repo just add results where you wanted to


Also, one more fix you didn't mention , the try 80 figures with 18 plots should be better labeled, fix the script. The 2 columns to the right are the GT vs prior, and prior vs prediction, which isn't specified. Also depending on where you include them, consider rotating them from 6x3 to 3x6. Maybe make a script that without regenerating them just takes the chunks from the images and put them in another way.


#### Continued after LaTeX pull - 2026-05-14:

This section supersedes the old TODO interpretation above when it conflicts with
the current LaTeX. Keep the earlier text as history of the supervisor-feedback
conversation; use this section for the next editing pass.

## Already handled in the pulled thesis

- Pulled latest `main` from the LaTeX repo: commit `eae5003` (`Reduce thesis body and restructure appendices`).
- Main body was reduced to about 67 pages before appendices. The detailed log is in `reduction_restructure_changes_2026-05-14.md`.
- `introduction.tex` now has explicit project targets, research questions, direct answers, contributions, and a thesis outline.
- Try 80 placeholders are no longer current. `summary.tex`, `results.tex`, `state_of_art.tex`, `conclusions.tex`, and `appendices.tex` now describe the final Try 80 checkpoint instead of an in-flight placeholder.
- Current headline final Try 80 test numbers are: `1.6519 dB` path loss, `26.5570 ns` delay spread, and `11.3854 deg` angular spread on the 14-city unseen test split.
- The old duplicate-label worry about `prior_detail_try78_los.tex` and `prior_detail_try78_nlos.tex` is obsolete in the current tree: those files are gone/not referenced. The active inputs are `prior_detail_overview.tex`, `prior_detail_try78.tex`, and `prior_detail_try80.tex`.
- `results.tex` now includes the main missing evidence that was requested earlier: Try 76 per-expert path-loss results, Try 77 spread results, Try 78/79 prior results, UAV-height breakdowns, topology/regime breakdowns, and final Try 80 model-versus-prior tables.
- The Try 76 -> Try 78 narrative contradiction is now explicitly bridged: distribution-first modelling showed the target was learnable, then the calibrated prior was used because it was cheaper, more auditable, and already very strong for LoS path loss.
- SOA fixes mostly landed: the PMNet 36 dB conversion footnote exists, Gao et al. is tied to the 5.59 dB table result, the Try 80 row reports final unseen-city results, and the knife-edge improvement claim is softened into a design option rather than a hard unsupported number.

## Still open / worth doing next

- Full PDF compilation is still blocked locally by a MiKTeX `biber`/`biblatex` mismatch. The pulled log says a TeX-only compile works and the source-reference check found no missing or duplicate labels, but the final PDF should still be built in a clean TeX setup before submission.
- Per-city holdout table is still the highest-value remaining quantitative addition. Now that Try 80 final artifacts exist, make a compact table with sample counts and PL/DS/AS RMSE by held-out city, ideally top-N cities plus a rest aggregate.
- Delay/angular spread high-tail diagnostic is still worth adding if there is time. The thesis now says high-tail/outlier diagnostics matter; a small figure/table showing tail contribution by split, city, height bin, or subexpert would make that claim harder to challenge.
- Try 80 18-panel figure labels still need a visual check. If the columns are still unclear, add a small script that relabels/reflows the exported panels without rerunning inference. The important labels are `GT vs prior` and `prior vs prediction`.
- `per_city_holdout_and_try80_freeze.md`, `static_audit_2026-04-26.md`, `summary.md`, and `thesis_completion_checklist.md` contain historical placeholder language. Do not treat those lines as current unless cross-checked against `try80_placeholder_cleanup_2026-04-28.md` and the current `.tex` files.
- Give the AirMap/calibration wording one final human skim. The nearby SOA fairness fixes are present, but I did not re-check the original AirMap source in this pass.
- If there is time after the per-city table, add a short "what changed after supervisor review" paragraph to the revision/history or internal notes: body reduced, final results frozen, detailed formula material moved to appendices, and the final story kept as priors plus bounded residual learning.

## What I would tell the supervisor now

- The thesis no longer depends on future Try 80 results. The final checkpoint is frozen and reported on unseen test cities.
- The body has been reduced without deleting the detailed derivations; detailed prior/formula material moved to appendices.
- The final narrative is now cleaner: early neural models exposed the failure modes, Try 76/77 showed distribution-first modelling could fix target statistics, Try 78/79 built strong calibrated priors, and Try 80 uses a residual neural model only where it improves those priors.
- The remaining weakness is not the main story but auditability by city/outlier case. A per-city table and one high-tail diagnostic would be the best final polish.
