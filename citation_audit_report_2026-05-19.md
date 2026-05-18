# Citation audit report: reduced thesis and compact paper

Date: 2026-05-19

Scope:
- `FINAL_THESIS/paper_version/paper.tex`
- `FINAL_THESIS/paper_version/TFG.bib`
- `FINAL_THESIS/reduced/TFG/TFG.tex`
- `FINAL_THESIS/reduced/TFG/TFG.bib`

No manuscript source changes were made in this pass.

## Method

1. Extracted citation keys from the compact paper.
2. Resolved the actual reduced-thesis build path from `TFG.tex` with `\compacttfgfalse`, so the full chapters are checked rather than every stray `.tex` file in the folder.
3. Compared all used keys, `\nocite` keys, and the IEEE BST control key against `TFG.bib`.
4. Checked the latest reduced-thesis LaTeX log for undefined citation warnings.
5. Verified source existence through DOI resolution, arXiv records/local PDFs, official web pages, and GitHub repository refs.
6. Checked the citation-adjacent claims, especially numerical comparison rows, against the paper text.

## Citation inventory

### Compact paper

- Source file: `FINAL_THESIS/paper_version/paper.tex`
- Unique source citation keys: 34
- IEEE control key: `IEEEexample:BSTcontrol`
- Missing keys in `paper_version/TFG.bib`: none
- Unused bibliography entries: expected; the compact paper intentionally uses a smaller subset of the shared bibliography.

### Reduced thesis

- Root file: `FINAL_THESIS/reduced/TFG/TFG.tex`
- Actual included body with `\compacttfgfalse`: `introduction`, `state_of_art`, `methodology`, `prior_detail_*`, `results`, `sustainability_balanced`, `conclusions`, `appendices_compact`, plus front matter/config.
- Unique cited/nocited source keys: 53
- Missing keys in `reduced/TFG/TFG.bib`: none
- Latest `TFG.log`: no undefined citation warnings found.

### Relationship between the two documents

- The two `TFG.bib` files are byte-for-byte identical.
- The compact paper's 34 source keys are a subset of the reduced thesis keys.
- Reduced-thesis-only keys: `ckmimagenet2025`, `dataset2212`, `dhariwal2021diffusion`, `fmrme2026`, `geomDL2024`, `huang2025a2gtransformer`, `icassp2025indoor`, `indoor2025results`, `ippnet2025`, `isola2017pix2pix`, `izmailov2018swa`, `jaensch2024directiverme`, `radiolam2025`, `radiopit2025`, `sip2net2025`, `tarhouni2025`, `transPathNet2025`, `vinogradov2026shadow`, `wicopg2025`.
- Therefore, they do not "share everything"; the paper is a compressed subset, while the reduced thesis keeps the broader SOA/training/dataset references.

### Non-included internal notes

A broad scan of every `.tex` file under `FINAL_THESIS/reduced/TFG` found missing keys `remnet2024` and `terrain2025`, but only inside `Internal_Documentation/Actual_SOA_TFG_Path_Loss.tex`, which is not included by `TFG.tex`. This is not a build issue for the reduced thesis, but it would matter if that internal note were compiled separately.

## Findings that should be fixed for "100 percent correct" wording

### 1. Over-specific attribution to TR 38.901 for A2G logistic elevation-angle LoS probability

Location:
- `FINAL_THESIS/reduced/TFG/state_of_art.tex`, around the UAV/A2G subsection.

Current idea:
- The text says the "ITU and 3GPP A2G channel model family" parameterizes elevation-angle LoS dependence through logistic functions, citing `tr38901` and `khawaja_survey`.

Audit result:
- Al-Hourani directly supports the elevation-angle logistic/probabilistic A2G LoS framing.
- Khawaja et al. support the UAV A2G survey context and discuss such model families.
- TR 38.901 supports standardized large-scale channel modeling, LoS/NLoS states, path-loss and large-scale-parameter modeling, but it should not be used as the specific source for the Al-Hourani/ITU-style elevation-angle logistic A2G formula.

Recommended change later:
- Keep `alhourani2014` and `khawaja_survey` on the logistic/elevation-angle sentence.
- Mention `tr38901` separately as standardized LoS/NLoS and large-scale channel-model context, not as the exact source of that logistic elevation formula.

Severity: medium. The technical direction is right, but the source attribution is too broad.

### 2. AIRMap comparison wording is too strong in the reduced thesis SOA positioning table

Location:
- `FINAL_THESIS/reduced/TFG/state_of_art.tex`, final positioning table.

Current idea:
- The AIRMap row says the final model is below 2 dB PL RMSE and is "arguably better on this broad scale".

Audit result:
- AIRMap reports path-gain error below 4 dB against ray tracing and separate calibration results as median percentage error. It is not the same target, dataset, metric, frequency/protocol, or split.
- The supporting paragraph earlier in the same file is appropriately cautious.
- The compact paper table is also appropriately cautious and does not use the "arguably better" phrasing.

Recommended change later:
- Replace that phrase with a neutral statement such as: "This gives only a deployment-scale reference; the metric is path gain rather than this thesis's calibrated path-loss RMSE."

Severity: medium. The cited AIRMap facts exist, but the comparative interpretation is stronger than the paper supports.

### 3. `garciamarti2020mixture` bibliography entry exists but is incomplete

Location:
- Both `TFG.bib` files.

Current entry:
- Has authors, title, conference, year, and IMDEA handle URL.

Audit result:
- The paper exists and the cited claim is correct: it learns an explicit stochastic/Gaussian-mixture channel model for wireless physical-layer design.
- For exact bibliographic correctness, the entry should add the DOI and page range.

Recommended metadata:
- DOI: `10.1145/3416010.3423229`
- Pages: `53--62`
- Publisher: `ACM`
- Venue can remain MSWiM / Proceedings of the 23rd International ACM Conference on Modeling, Analysis and Simulation of Wireless and Mobile Systems.

Severity: low. Not false, but not maximally complete.

## Checked and supported claims

### PMNet / ICASSP 2023 conversion

Locations:
- `reduced/TFG/state_of_art.tex`
- `reduced/TFG/results.tex`
- `paper_version/paper.tex`

Checked facts:
- Challenge table reports PMNet `H/8 x W/8` RMSE = `0.0383` and PPNet RMSE = `0.0507`.
- Challenge evaluation sets building pixels to zero before RMSE.
- RadioMap3DSeer 3D dataset gives maximum path-gain/path-loss image value `-75 dB` and analytic truncation threshold `-111 dB`; the image window is therefore 36 dB.
- `0.0383 * 36 = 1.3788 dB`, so the approximate `1.38 dB` statement is supported.

Verdict: supported, with the caveat already present in the thesis that this is a rough image-scale conversion and not a direct benchmark equivalence.

Sources:
- https://arxiv.org/abs/2310.07658
- https://arxiv.org/abs/2212.11777

### RadioUNet dB-scale band

Checked facts:
- RadioUNet reports gray-level RMSE values around `0.020` to `0.0384` in the relevant accurate-map settings.
- The paper states that dB RMSE is 80 times the gray-level RMSE.
- This gives about `1.6 dB` to `3.1 dB`.

Verdict: supported.

Source:
- https://arxiv.org/abs/1911.09002

### RadioGUNet values

Checked facts:
- Table II reports `1.304 dB` for DPM without cars, `1.936 dB` for IRT without cars, and `1.392 dB` for DPM with cars for RadioGUNet-D8.
- The paper follows the RadioUNet/RadioMapSeer split: 500 training maps, 100 validation maps, 100 test maps.

Verdict: supported.

Source:
- https://arxiv.org/abs/2511.17841

### Gao et al. corridor/weighting-map model

Checked facts:
- The paper uses mask, Tx depth, Rx depth, distance map, and a weighting mask/map.
- Table II reports `12.19 dB` RMSE on the ITU challenge dataset and lower FLOPs than PPNet.
- Table III reports `5.59 dB` RMSE on ICASSP 2023.
- The text says the method requires about 60 percent fewer FLOPs than PPNet.

Verdict: supported.

Source:
- https://arxiv.org/abs/2601.08436

### ReVeal

Checked facts:
- ReVeal derives a second-order PDE residual for RSSI and includes it as a physics-informed loss.
- It is validated on real rural/suburban measurement data with sparse RF sensors.
- Table reports ReVeal RMSE `1.95 dB`.

Verdict: supported.

Source:
- https://arxiv.org/abs/2502.19646

### RMTransformer

Checked facts:
- Table reports RMSE `0.007148`.
- The setup uses 256 x 256 USC data with a random 90/10 train/test split.
- The paper states received-power values are normalized from `-254 dBm` to `0 dBm`, supporting the rough `0.007148 * 254 = 1.82 dB` conversion.

Verdict: supported as an approximate scale check, not a direct comparison.

Source:
- https://arxiv.org/abs/2501.05190

### PathFinder

Checked facts:
- The paper defines distribution-shift RPP, uses disentangled feature encoding and mask-guided low-rank attention, and introduces transmitter-oriented mixup.
- Table 1 reports PathFinder RMSE `0.033069` on DS-RPP.
- Table 2 reports unseen rural RMSE `0.326344`.
- The thesis's conversions using a 36 dB RM3D window are explicitly marked approximate.

Verdict: supported.

Source:
- https://arxiv.org/abs/2512.14150

### AIRMap

Checked facts:
- AIRMap uses a single-input U-Net autoencoder with 2D elevation maps.
- It uses fixed 200 x 200 tensors with variable physical resolution/extent.
- It reports path-gain error below 4 dB versus ray tracing and about 4 ms inference on an NVIDIA L40S.
- It reports calibration reducing median measurement-domain error to about 5 percent using 20 percent field measurements.

Verdict: factual claims supported; direct "better than" interpretation should be softened as noted above.

Source:
- https://arxiv.org/abs/2511.05522

### Indoor ICASSP 2025 results

Checked facts:
- Official results page reports final weighted RMSEs: SIP2Net `9.411`, IPP-Net `9.501`, TerRaIn `10.325`, TransPathNet `10.397`.
- The overview paper reports the same ordering rounded to two decimals.

Verdict: supported.

Sources:
- https://indoorradiomapchallenge.github.io/results.html
- https://arxiv.org/abs/2501.13698
- https://arxiv.org/abs/2501.06414
- https://arxiv.org/abs/2501.16023

### Saboor and Vinogradov height-dependent A2G model

Checked facts:
- The paper models height-dependent mmWave UAV A2G path loss and shadowing in urban scenarios.
- It reports LoS PLE near 2, NLoS PLE moving toward about 2.5-3 at high altitude, and shadow fading decreasing with height.
- It uses simulated 26 GHz urban A2G ray tracing and explicitly studies urban layout dependence.

Verdict: supported.

Source:
- https://arxiv.org/abs/2511.10763

### Tarhouni et al.

Checked facts:
- The paper studies ML-based path-loss prediction in suburban sub-6 GHz settings.
- It reports multi-dB RMSE values, including a measured-data range around `9.27 dB` to `11.32 dB`.
- It is not a dense UAV CKM benchmark, matching the thesis's qualitative use.

Verdict: supported.

Source:
- https://arxiv.org/abs/2510.00696

### CKM and dataset citations

Checked facts:
- Zeng and Xu 2021 defines CKM as environment-aware, location-indexed channel knowledge.
- The 2024 tutorial covers CKM construction/utilization for 6G environment-aware communication.
- Xu and Zeng 2024 addresses how much data is needed for CKM construction.
- RadioMap3DSeer and CKMImageNet claims are supported by their dataset papers.
- Jaensch et al. supports the directive-antenna/open-dataset discussion.

Verdict: supported.

Sources:
- https://doi.org/10.1109/MWC.001.2000327
- https://doi.org/10.1109/COMST.2024.3364508
- https://doi.org/10.1109/TWC.2024.3397964
- https://arxiv.org/abs/2212.11777
- https://arxiv.org/abs/2504.09849
- https://arxiv.org/abs/2402.00878

### Distribution-aware and training-method citations

Checked facts:
- Kendall and Gal supports heteroscedastic uncertainty/NLL with predicted variance.
- Saleh et al. supports probabilistic path-loss prediction for mmWave networks.
- Garcia Marti et al. supports Gaussian-mixture channel modeling for wireless physical-layer design.
- Lee et al. supports mixture-density/time-varying wireless-channel PDF modeling.
- FiLM supports feature-wise affine conditioning.
- SWA and diffusion time-step conditioning references are used only as method inspiration and are supported.

Verdict: supported; add DOI/pages for Garcia Marti as above.

Sources:
- https://arxiv.org/abs/1703.04977
- https://doi.org/10.1109/VTC2021-Spring51267.2021.9448967
- https://doi.org/10.1145/3416010.3423229
- https://arxiv.org/abs/2405.08199
- https://doi.org/10.1609/aaai.v32i1.11671
- https://arxiv.org/abs/1803.05407
- https://arxiv.org/abs/2105.05233

### Project software artifact citations

Checked facts through GitHub API:
- `CKMGenerator` repository exists and commit `8b6c5fd26c30` resolves.
- `Final_Code_TFG` repository exists and commit `63d12a3d1a05` resolves.
- `TFGAllProgress_Tries_and_Attempts` repository exists and commit `7c13efd51708` resolves.
- `TFG_ActualText_LaTeX` repository exists and tag `final-thesis-2026-05-15` resolves to commit `aa03d55ef53d`.

Verdict: supported.

Sources:
- https://github.com/unworthyzeus/CKMGenerator
- https://github.com/unworthyzeus/Final_Code_TFG
- https://github.com/unworthyzeus/TFGAllProgress_Tries_and_Attempts
- https://github.com/unworthyzeus/TFG_ActualText_LaTeX

## Overall verdict

The citation set is structurally sound: no missing keys in either active document, no undefined citation warnings in the reduced thesis log, and the paper/reduced split is intentional rather than accidental.

Most citation-adjacent claims are accurate and appropriately caveated, especially the high-risk numerical comparison rows. I found two wording/source-attribution issues to fix before calling it "100 percent correct" and one low-risk bibliography-completeness improvement:

1. Reword the A2G logistic LoS attribution so TR 38.901 is not treated as the direct source of the Al-Hourani-style elevation-angle logistic formula.
2. Soften the AIRMap "arguably better" interpretation in the reduced thesis positioning table.
3. Add DOI/pages/publisher metadata to `garciamarti2020mixture`.

No source claim in the compact paper looks materially unsupported after this pass.
