# Short Script for Presenting the Supervisor Revision

## Opening

I reviewed the methodology comments and cleaned up the structure, repeated material and notation. The main goal was to make Chapter 3 read as the final reproducible method, not as the development history. The development history stays in the appendix; this chapter now keeps only the pieces used by the final system.

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

In Training and Evaluation Protocol, I made the final model description more ordered: nine input channels, scalar height with FiLM, LoS/NLoS branches, bounded residuals and the loss function.

I also clarified an important code detail: `path_loss_nlos_prior` does not mean the map is zeroed outside NLoS. It is the calibrated NLoS branch, and the final selection is done by the explicit LoS/NLoS masks.

## Page 73

I moved the global RMSE formula to Results. It fits better here because this is where all numerical tables are interpreted.

Chapter 4 now defines that RMSE is pixel weighted over valid receivers, and the same rule is used for priors and the final model in PL, DS and AS.

## Closing

In summary, I addressed the comments in four main ways: I reduced redundancy, moved the metric definition to the results chapter, corrected the section structure, and revised the notation so it is consistent with the code and the actual priors. The compiled version is updated and has no broken references.
