# Citation Audit Report - Reduced Thesis and Paper Version

Date checked: 2026-05-18/19  
Scope:

- Active reduced thesis build rooted at `FINAL_THESIS/reduced/TFG/TFG.tex`
- Paper build rooted at `FINAL_THESIS/paper_version/paper.tex`
- Shared bibliographies:
  - `FINAL_THESIS/reduced/TFG/TFG.bib`
  - `FINAL_THESIS/paper_version/TFG.bib`

## Executive Summary

Result: the active `reduced` thesis and `paper` version are mostly citation-safe.

- The two BibTeX files are identical.
- The paper cites 35 unique keys. The active reduced thesis cites 53 unique keys.
- No cited key is missing from the bibliography in either active build.
- Existing build logs show no unresolved-citation warnings.
- All external URLs/DOIs in the bibliography resolved during the audit. The only scripted HTTP anomaly was the MDPI Sensors page returning 403 to the script, but the page opens normally in browser context.
- The major numerical comparison claims were checked against paper text/PDF extracts and are supported.
- The paper version has no unique high-risk citation problem.

Main things I would change before final submission:

1. `FINAL_THESIS/reduced/TFG/state_of_art.tex:135-136` mentions WINNER II and COST 2100 adopting the same log-spread convention, but the sentence only cites 3GPP TR 38.901 and there is no COST 2100 bibliography entry. Add `winner2` and either add a COST 2100 reference or remove COST 2100.
2. `FINAL_THESIS/reduced/TFG/state_of_art.tex:340-342` says TR 38.901 gives polynomial fits for spread mean/std as functions of 2D distance and transmitter height across UMa/UMi/RMa. This is directionally right about log-domain large-scale parameters, but too specific for a UAV-height thesis. Safer wording should say TR 38.901 provides scenario/state/frequency/distance/height-dependent large-scale-parameter tables and formulas, not direct CKM/UAV-height priors.
3. Inactive internal documentation file `FINAL_THESIS/reduced/TFG/Internal_Documentation/Actual_SOA_TFG_Path_Loss.tex` cites missing keys `remnet2024` and `terrain2025`. This does not affect the active reduced PDF, but it is a latent issue if that file is compiled or reused.

## Local Citation Integrity

Extraction method:

- Parsed LaTeX citation commands.
- Expanded the reduced thesis custom `\inputmainchapter{compact}{full}` macro according to `\compacttfgfalse`, so the full chapters were audited.
- Checked `\nocite`, regular citation commands, and paper `\bstctlcite`.

Active build results:

| Document | Unique cited keys | Bib entries | Missing active keys |
|---|---:|---:|---|
| `paper_version/paper.tex` | 35 | 54 | 0 |
| `reduced/TFG/TFG.tex` active full build | 53 | 54 | 0 |

The paper and reduced thesis do not need to share all citations. The current difference is expected: the reduced thesis includes a broader state-of-the-art discussion, while the paper is shorter.

Build-log check:

- `paper_version/paper.blg` reports 0 warnings.
- `reduced/TFG/TFG.blg` has no warning/error/missing/undefined citation messages.

## Existence and Metadata Check

All bibliography URLs or DOI redirects tested as reachable:

- IEEE/DOI examples: `khawaja_survey`, `wocc2021`, `alhourani2014`, `zengx2021ckm`, `ckmtutorial2024`, `ckmdata2024`, `pmnet2023`, `pmnet_icassp2023`, `vinogradov2026shadow`, `sip2net2025`, `ippnet2025`, `transPathNet2025`, `geomDL2024`, `radiodiff2025`, `saleh2021probabilistic`, `perez2018film`, `goldsmith`.
- arXiv examples: `saboor2025height`, `icassp2023challenge`, `dataset2212`, `jaensch2024directiverme`, `ckmimagenet2025`, `icassp2025indoor`, `radiogunet2025`, `rmtransformer2025`, `tarhouni2025`, `gao2026`, `airmap2025`, `pathfinder2025`, `wicopg2025`, `fmrme2026`, `radiolam2025`, `reveal2025`, `radiopit2025`, `isola2017pix2pix`, `kendall2017uncertainties`, `izmailov2018swa`, `cai2019`, `dhariwal2021diffusion`, `lee2024timevarying`.
- Standards/books/reports: `tr38901`, `cost231`, `winner2`, `rappaport`.
- Project repositories: all four GitHub repository URLs resolve, the three commit URLs resolve, and tag `final-thesis-2026-05-15` resolves.

Minor metadata-completeness notes:

- `pmnet2023` exists and the DOI is correct. DBLP lists pages 4601-4606; the bibliography currently omits pages. Not a correctness problem, but adding pages would improve completeness.
- `tr38901` cites the 3GPP archive rather than a specific zip version. This is acceptable, but for maximum precision use the specific Release 19 `38901-j20.zip` version if the thesis wants a frozen standard version.
- `radiolam2025` is an arXiv/preprint-style entry but the arXiv page says accepted by IEEE JSAC. The citation exists; publication metadata may be updated later if desired.

## Checked Claim Support

### CKM and Dataset Claims

Supported:

- CKM as site-specific/location-tagged channel knowledge: supported by `zengx2021ckm` and `ckmtutorial2024`.
- CKM construction data/accuracy tradeoff: supported by `ckmdata2024`.
- RadioMap3DSeer / pathloss and ToA dataset, dense urban maps, RSS/ToA maps: supported by `dataset2212`.
- ICASSP 2023 challenge task and results: supported by `icassp2023challenge`.
- Directive antenna radio-map dataset and CKMImageNet existence/context: supported by `jaensch2024directiverme` and `ckmimagenet2025`.

Important nuance:

- `state_of_art.tex:181-182` says building interior pixels are masked to zero error in the challenge family. This is supported by the challenge text: predictions at building pixels were set to zero so prediction error is zero there.

### Classical and A2G Propagation Claims

Supported:

- FSPL, coherent two-ray/image-source construction, reflection coefficient and far-distance fourth-power behavior: supported by Rappaport/Goldsmith and the WOCC 2021 UAV two-ray paper.
- COST231/Hata urban macro formula and metropolitan correction: supported by the COST 231 final report.
- TR 38.901 frequency scope from 0.5 to 100 GHz and UMa/UMi/RMa/indoor standardized channel-model context: supported by the 3GPP archive.
- Al-Hourani elevation-angle LoS-probability/morphology framing: supported by `alhourani2014`.
- Saboor and Vinogradov 26 GHz height-dependent PLE/shadowing statement: supported by the arXiv abstract and PDF text.
- Vinogradov et al. 3D shadow projections for spatially consistent A2G LoS maps: supported by the DOI/search metadata and available ICNC PDF.

Needs wording cleanup:

- `state_of_art.tex:135-136`: add `winner2` and either a COST 2100 reference or remove COST 2100.
- `state_of_art.tex:340-342`: soften "polynomial fits ... as functions of 2D distance and transmitter height" to avoid implying a direct UAV transmitter-height model.

### Deep Radio-Map and Numeric Benchmark Claims

Supported:

- RadioUNet RMSE values around 0.0203-0.0384 and the 80 dB conversion context are present in the RadioUNet paper.
- PMNet / ICASSP values 0.0383 and PPNet 0.0507 are present in the challenge paper. The thesis conversion to 1.38 dB and 1.83 dB using a 36 dB window is mathematically correct, and the caveat text is appropriate.
- RadioMap3DSeer properties used in the comparison are supported: 256 x 256 maps, rooftop Tx 3 m above rooftop, path-gain/pathloss image clipping values around -111 and -75 dB depending on dataset variant.
- RadioGUNet values 1.304 dB DPM, 1.936 dB IRT, and 1.392 dB with cars are present in the paper text/table.
- RMTransformer values 0.007148, 0.01046, 0.008099, 256 x 256 maps, and -254 to 0 dBm normalization are present in the PDF.
- Gao et al. values 5.59 dB, 12.19 dB, 8.09 dB, 9.56 dB, 8.72 dB, and 60% lower FLOPs are present in the PDF/abstract.
- AIRMap claims are supported: single-input U-Net/elevation map, path gain under 4 dB RMSE, 4 ms L40S inference, 20% field-measurement calibration, around 5% median error, fixed 200 x 200 input, and 2.5-15 m/pixel variable spatial resolution.
- PathFinder claims are supported: disentangled building/transmitter encoding, mask-guided low-rank attention, transmitter-oriented mixup, S2MT/DS-RPP framing, unseen-rural MSE 0.1068 and RMSE 0.3263. The DS-RPP value in the paper text is 0.033069, so the thesis `0.0331` rounding is fine.
- ICASSP 2025 indoor challenge values are supported by the official results page and paper abstracts: SIP2Net 9.411, IPP-Net 9.501, TerRaIn 10.325, TransPathNet 10.397.

No change needed, but keep caveats:

- The thesis/paper correctly warns that these are not like-for-like comparisons because of different split, target, mask, dynamic range, transmitter setup, and calibration protocols. Do not remove those caveats.

### Emerging/Foundation/Physics-Informed Methods

Supported:

- WiCo-PG: RGB auxiliary modality, dual VQGANs plus Transformer, frequency-guided shared-routed MoE, NMSE 0.012.
- RadioLAM: fine-grained 3D radio maps from ultra-low sampling rates using large generative models.
- FM-RME: self-supervised pretraining and foundation-model framing for radio-map estimation.
- RadioPiT: real-world sparse radio map generation, Pixel Transformer, TTA strategy.
- Geometry-assisted diffraction/scattering model: virtual obstacles, multi-screen knife-edge features, local scattering geometry.
- ReVeal: second-order PDE residual in the neural loss; 1.95 dB RMSE with 30 training samples across the cited outdoor/rural-scenario setup.
- RadioDiff: conditional diffusion framing for sampling-free/dynamic RadioMapSeer radio-map construction, with RMSE/SSIM/PSNR comparisons.

### Distributional and Training Claims

Supported:

- Kendall and Gal heteroscedastic framework: predicts log variance and uses a learned attenuation/NLL-style loss. The thesis formula omits constant 1/2 factors, which is standard when writing proportional losses.
- Saleh et al.: MDN/probabilistic path-loss predictors for mmWave networks.
- Garcia Marti et al.: Gaussian-mixture stochastic channel model for physical-layer design.
- Lee et al. 2024: mixture density network for conditional PDF of received power.
- SWA, FiLM, diffusion-model conditioning citations support their respective method summaries.

## Active Paper-Specific Findings

No paper-only high-risk issue found.

The `paper.tex` related-work section uses broad, defensible statements:

- Dense radio-map prediction as image-to-image regression.
- Recent models adding attention/equivariance/domain-shift/corridor/digital-twin ideas.
- Classical and hybrid priors used only as shape priors, with coefficients calibrated train-only.
- Distribution-aware heads motivated by heteroscedastic regression, MDNs/GMMs, and diffusion radio-map work.

The paper also avoids the reduced thesis's COST 2100 unsupported sentence and uses the safer phrase "3GPP/WINNER-style models" with both `tr38901` and `winner2`.

## Inactive Source Issue

If all `.tex` files under `FINAL_THESIS/reduced/TFG/` are scanned, two missing keys appear:

- `remnet2024`
- `terrain2025`

Both occur only in:

- `FINAL_THESIS/reduced/TFG/Internal_Documentation/Actual_SOA_TFG_Path_Loss.tex`

This file is not included by the active reduced thesis build. It is not a current PDF problem, but it should be fixed if the internal documentation is meant to compile independently.

## Suggested Next Edits

1. Fix `state_of_art.tex:135-136` by changing:
   - "The WINNER II and COST 2100 models adopt the same convention."
   - to something like:
   - "WINNER II follows the same broad log-domain large-scale-parameter convention \cite{winner2}."
   - Or add a proper COST 2100 reference if COST 2100 must stay.

2. Fix `state_of_art.tex:340-342` by changing:
   - "TR 38.901 provides polynomial fits for the log-normal mean and standard deviation as functions of 2D distance and transmitter height across UMa, UMi, and RMa scenarios."
   - to something like:
   - "TR 38.901 provides scenario- and state-specific large-scale-parameter tables/formulas for delay and angular spreads, with log-domain modelling and dependencies on variables such as distance, frequency, terminal heights, and scenario class."

3. Optionally add pages to `pmnet2023`:
   - pages = {4601--4606}

4. Optionally make `tr38901` version-specific:
   - note the exact `38901-j20.zip` Release 19 version if you want a frozen standard citation rather than archive-level citation.

5. Either remove or complete the inactive internal documentation citations:
   - add `remnet2024` and `terrain2025`, or remove/comment those references from `Internal_Documentation/Actual_SOA_TFG_Path_Loss.tex`.

## Source Links Used

- 3GPP TR 38.901 archive: https://www.3gpp.org/ftp/Specs/archive/38_series/38.901/
- RadioMap3DSeer dataset: https://arxiv.org/abs/2212.11777
- ICASSP 2023 challenge: https://arxiv.org/abs/2310.07658
- Indoor challenge results: https://indoorradiomapchallenge.github.io/results.html
- RadioUNet: https://arxiv.org/abs/1911.09002
- PMNet: https://arxiv.org/abs/2211.10527
- RadioGUNet: https://arxiv.org/abs/2511.17841
- RMTransformer: https://arxiv.org/abs/2501.05190
- Gao et al.: https://arxiv.org/abs/2601.08436
- AIRMap: https://arxiv.org/abs/2511.05522
- PathFinder: https://arxiv.org/abs/2512.14150
- Saboor and Vinogradov height-dependent UAV model: https://arxiv.org/abs/2511.10763
- CKMImageNet: https://arxiv.org/abs/2504.09849
- WiCo-PG: https://arxiv.org/abs/2511.15030
- RadioLAM: https://arxiv.org/abs/2509.11571
- FM-RME: https://arxiv.org/abs/2602.22231
- RadioPiT: https://arxiv.org/abs/2512.01451
- Geometry-assisted diffraction/scattering: https://arxiv.org/abs/2403.00229
- RadioDiff: https://arxiv.org/abs/2408.08593
- Cai A2G LTE model: https://arxiv.org/abs/1901.07930
- Isola pix2pix: https://arxiv.org/abs/1611.07004
- IPP-Net: https://arxiv.org/abs/2501.06414
- TransPathNet: https://arxiv.org/abs/2501.16023
- Saleh probabilistic path-loss predictors: https://aaltodoc.aalto.fi/items/53d79022-6586-4454-b6f0-e147ae034778
- Garcia Marti mixture density channel model: https://dspace.networks.imdea.org/handle/20.500.12761/886
- COST 231 final report: https://op.europa.eu/en/publication-detail/-/publication/f2f42003-4028-4496-af95-beaa38fd475f
- WINNER II report: https://www.cept.org/files/8339/winner2%20-%20final%20report.pdf
- Huang et al. A2G Transformer: https://www.mdpi.com/1424-8220/25/12/3731
