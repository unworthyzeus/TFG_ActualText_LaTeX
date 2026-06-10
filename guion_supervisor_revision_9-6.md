# Short Script for Presenting the Supervisor Revision

## Opening

I reviewed the methodology comments and cleaned up the structure, repeated material and notation. The main goal was to make Chapter 3 read as the final reproducible method, not as the development history. The development history stays in the appendix; this chapter now keeps only the pieces used by the final system.

## Exact Comment Fix List

Use this list while scrolling through the revised PDF. The short version is: every comment was treated either as a structure fix, a notation fix, a redundancy fix, or a code consistency fix.

1. **"Show the flow in Fig. 3.1 and describe it here."**
   I rewrote the Chapter 3 opening so it now points directly to the high level flow figure. The first paragraph explains the same sequence as the figure: raw CKM map and transmitter height, support maps, frozen priors, HARP-Net CKM residuals, and final PL, DS and AS maps.

2. **"The methodology start was too empty and repetitive."**
   I filled the first methodology page with useful structure instead of filler text. I added Table 3.1 as a chapter guide, so the page now gives the reader both the pipeline summary and the section map.

3. **"Remove the repeated pipeline text."**
   I deleted the old crossed out paragraphs that repeated the dataset, metric, priors and model ordering. That information now appears once in the opening and once in the framework table, not several times.

4. **"Move the framework section earlier. The old 3.3 should really be 3.2."**
   I moved General Framework and Data Flow before the support map details. The reader now sees the whole method first, then the geometry and morphology definitions used by the priors.

5. **"The table should have the same rows as the sections."**
   I rewrote Table 3.1 so its rows match the actual Chapter 3 sections. I also renamed the last row to HARP-Net CKM Neural Residual Model, because that section explains the network rather than a generic training protocol.

6. **"Stop using the word contract so much."**
   I removed that word from Table 3.1 and from the visible methodology section titles where it sounded bureaucratic. The text now uses more precise names such as receiver mask, evaluation rule, framework, prior, or neural residual model.

7. **"Define H, W, i, j and the transmitter center."**
   I made the index convention explicit: the map is 513 by 513, pixel indices follow the implementation convention, and the centered transmitter is at the corresponding center coordinate. This avoids the old ambiguity between one based and zero based notation.

8. **"Do not use b(x) if it is just 1 minus g(x)."**
   I removed the redundant building mask as a main thesis level quantity. The valid receiver set is defined through the ground mask, and building occupancy only appears where a morphology computation needs that complement.

9. **"Buildings being removed from losses and metrics belongs with evaluation, not support maps."**
   I stopped emphasizing metrics inside the support map section. The support map section now defines the valid receiver set, while the pixel weighted RMSE rule is defined in Results where the numerical tables are interpreted.

10. **"Do not use d3D."**
    I replaced the old direct 3D path notation with \(d_{\mathrm{LoS}}\). The direct path length and reflected path length are now named consistently as \(d_{\mathrm{LoS}}\) and \(d_{\mathrm{ref}}\).

11. **"Explain the angle normalization, especially the 90 pi expression."**
    I simplified the notation to the radian form and explained the intuition: the normalized elevation angle is the elevation angle divided by a 90 degree overhead reference, clipped to the unit interval. The old expression
    \[
    \frac{180\theta(x)}{90\pi}
    \]
    was only doing "radians to degrees" with \(180/\pi\), and then dividing by \(90^\circ\). Since \(90^\circ=\pi/2\) radians, the same normalization is simply
    \[
    \frac{\theta(x)}{\pi/2}=\frac{2\theta(x)}{\pi}.
    \]
    Meeting sentence: "There is no special \(90\pi\) constant; it was just a confusing degree conversion. I rewrote it directly in radians as \(2\theta/\pi\)."

12. **"Clarify whether LoS/NLoS masks come from the dataset or are calculated."**
    I clarified that the thesis experiments use the stored HDF5 LoS mask restricted to valid ground receivers. The CKMGenerator ray casting path is described as a deployment fallback for topology only inputs, not as the evaluation mask used for final reported numbers.

13. **"If ray casting remains, explain intuition before math."**
    I rewrote that paragraph so the logic comes first: sample the line between transmitter and receiver, compare the line height with buildings, then formalize it. This follows the comment that intuition should precede equations. In the revised source, this paragraph appears before the definitions of \(L_x\), the sampled points and the generated masks.

14. **"If you use calculated LoS masks, show the error."**
    I avoided turning the fallback ray casting routine into an evaluated result. Since the final experiments use the HDF5 masks, I did not add an unsupported mask error table. The fallback is now presented only as generator behavior outside the HDF5 setting.

15. **"Explain BoxMean 15 and 41 before equations."**
    I added the purpose of the two window sizes before the formulas. The 15 pixel window is local receiver texture; the 41 pixel window is a wider urban block context. I also avoided claiming they are optimal without an ablation.

16. **"The height reporting intervals do not belong in the map section."**
    I removed the result reporting height interval discussion from the support map section. The methodology keeps only calibration keys and normalized features; result bins are discussed in the results chapter.

17. **"rho is confusing because it is also reflection amplitude."**
    I renamed local density notation away from \(\rho\). The LoS reflection amplitude keeps \(\rho\), while local building density uses a different symbol, so reflection and morphology are no longer mixed.

18. **"Define phi clearly."**
    I added the explicit meaning of \(\phi\): it is the fitted effective phase offset of the reflected path relative to the direct path. It is a calibrated CKM parameter, not a material constant.

19. **"Explain why log(401) appears despite the dataset maximum being near 500 m."**
    I added the explanation that the scale saturates a 400 m Tx to Rx height difference because high altitude samples are sparse after splitting by city and regime. The HDF5 maximum is higher, but the normalization is deliberately robust to the thin high altitude tail.

20. **"The prior overview overexplains Bayesian prior terminology."**
    I shortened the explanation. It now says once that prior means frozen deterministic estimator in this thesis, then immediately explains the LoS attenuation prior, NLoS attenuation prior, spread priors and residual model.

21. **"Remove duplicated geometry and textbook explanations from the LoS prior."**
    I removed the repeated geometry subsection from the prior detail and made the LoS section start from what is new in this thesis: fitted effective two ray correction, height dependent bias and radial residual.

22. **"Do not make the NLoS part sound like formal stages if the code is not staged."**
    I changed the language from stages to calculation blocks and branch components. COST231, A2G, morphology and OLS calibration are now described as parts of one calibrated NLoS prior branch.

23. **"Reduce redundancy in the spread prior."**
    I made the DS and AS section share one explanation of the log domain ridge prior. Reused support maps and topology classes are referenced instead of redefined.

24. **"Move the RMSE equation to Results."**
    I moved the pixel weighted RMSE formula into Chapter 4. This makes it easier to find when reading the numerical tables and avoids putting a results metric inside support map definitions.

25. **"Page 33 should explain the neural network section, not training and evaluation protocol."**
    I renamed the section and the page 33 table row to HARP-Net CKM Neural Residual Model. The description now says it explains the network used in the final system: input channels, height conditioning, bounded residual heads and training losses.

26. **"Do not mention internal late attempt labels in the visible text."**
    I replaced those visible labels in the page 33 guide and in the appendix final table with named components: calibrated path loss prior, calibrated spread priors and HARP-Net CKM. The text now talks about priors and the network, not internal attempt numbers.

27. **"Check the fixes against code and other repos."**
    I checked the thesis claims against the implementation facts: nine spatial channels plus scalar height, stored HDF5 LoS mask in the final dataset path, ground pixel masking, receiver height 1.5 m, 513 by 513 maps, centered transmitter, 15 and 41 morphology windows, and the final prior plus residual model flow.

## Page 33

I rewrote the chapter opening. Before, the page looked too empty and the first paragraph was longer and more repetitive. It now starts with a direct summary of the final pipeline, and Table 3.1 acts as a guide to the chapter.

The table no longer uses the word "contract", and its rows now match the actual Chapter 3 sections, so it works as a reading map.

## Page 34

In the large framework figure, I changed the wording from "stages" to flow blocks. This avoids suggesting that the method is a staged training pipeline when it is really a sequence of calculation blocks, frozen priors and a residual model.

I also adjusted the visual notation: masks, distances and LoS/NLoS branches now match the text and the code more closely.

## Page 35

The dataset and split section is clearer now. It separates the HDF5 fields, the transmitter position, the 1.5 m receiver height and the rule that building pixels are not receivers.

I also moved the metric discussion out of Methodology. Here I only keep the receiver mask and the split; the exact RMSE formula is now defined in Results.

## Page 37

The framework section is now Section 3.2, as suggested. It appears before the support map definitions and gives the global view of the complete flow: inputs, derived maps, priors, HARP-Net CKM input channels and outputs.

## Pages 39 and 40

I cleaned up the support maps, masks and morphology section. The valid receiver definition is tied to \(\Omega_g\), and the LoS/NLoS masks are explained without repeating the evaluation discussion.

I also clarified the CKMGenerator ray casting logic and the reason for the morphology windows. On page 40 I added the explanation of \(\log(401)\): it is a practical saturation scale for a 400 m Tx-Rx height difference, not the true maximum of the HDF5 data. Even though the dataset reaches about 478 m, the high altitude tail has too few samples after the city and regime splits.

## Pages 41 to 43

I rewrote the prior overview so it is clear that "prior" here does not mean a Bayesian probability prior. It means a deterministic estimator that is frozen before the residual model.

I added a notation table to avoid ambiguity: \(\rho\) is reserved for the LoS reflection amplitude, \(\phi\) for the reflection phase in radians, \(\beta_{\mathrm{LoS}}\) for the LoS bias, and \(\delta_k\) for local density. This avoids mixing the old \(b\) notation for bias, building mask and other quantities.

## Pages 44 to 50

In the Channel Attenuation Prior section, I removed the repeated geometry definitions that had already been introduced earlier. The LoS prior now references the shared distances and focuses on FSPL, two ray correction, height bias and radial residual.

I also explicitly clarified what \(\phi\) is: it is the fitted effective phase offset of the reflected path relative to the direct path. This addresses the question of whether it was explained clearly.

## Pages 51 to 59

In the NLoS branch, I removed the "stage" language and turned it into calculation blocks. The branch is now presented as a calibrated prior using local morphology, obstruction, elevation and regime-wise regression.

I also reduced redundancy: geometry and masks are no longer redefined here, and the text points back to the shared support maps. I changed local densities to \(\delta_{15}\) and \(\delta_{41}\), so they cannot be confused with the LoS reflection \(\rho\).

## Pages 60 to 64

In the delay spread and angular spread prior, I removed repeated definitions that were already in the shared support sections. The text now says that the spread vector reuses those common features and only details the new parts: ridge regression, fallback keys, clipping and inverse transform.

The point here is that DS and AS share the same prior machinery, rather than having two duplicated explanations.

## Pages 65 to 72

In the HARP-Net CKM Neural Residual Model section, I made the network description more ordered: nine input channels, scalar height with FiLM, LoS/NLoS branches, bounded residuals and the loss function.

I also clarified an important code detail: `path_loss_nlos_prior` does not mean the map is zeroed outside NLoS. It is the calibrated NLoS branch, and the final selection is done by the explicit LoS/NLoS masks.

## Page 73

I moved the global RMSE formula to Results. It fits better here because this is where all numerical tables are interpreted.

Chapter 4 now defines that RMSE is pixel weighted over valid receivers, and the same rule is used for priors and the final model in PL, DS and AS.

## Closing

In summary, I addressed the comments in four main ways: I reduced redundancy, moved the metric definition to the results chapter, corrected the section structure, and revised the notation so it is consistent with the code and the actual priors. The compiled version is updated and has no broken references.
