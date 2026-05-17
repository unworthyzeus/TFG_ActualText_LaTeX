# Latest changes

Date: 2026-05-17

Scope: restore the Try78 path-loss prior audit on the same city-holdout
contract used by Try79/Try80, update the reduced thesis and paper wording, and
keep the previous tables here for traceability.

## Source artifacts restored

Supporting audit artifacts were restored in `C:\TFG\TFGpractice`:

- `TFGEightiethTry80/scripts/recalibrate_priors/run_try78_on_try80_split.py`
- `TFGSeventyEighthTry78/hybrid_out_try80_split/README.md`
- `TFGSeventyEighthTry78/hybrid_out_try80_split/hybrid_eval_summary_try80_valtest.json`
- `TFGSeventyEighthTry78/hybrid_out_try80_split/hybrid_eval_summary_try80_test.json`
- `TFGSeventyEighthTry78/hybrid_out_try80_split/try78_try80_valtest_grouped_metrics.json`
- `TFGSeventyEighthTry78/hybrid_out_try80_split/calibrations/*.json`

The validation+test audit uses `split_seed = 42`, 10840 train samples, 2750
validation samples, 2590 test samples, and 5340 held-out validation+test
samples. Its aggregate path-loss prior metrics are:

| Region | RMSE (dB) |
| --- | ---: |
| LoS | 1.7379 |
| NLoS | 3.3591 |
| Overall | 1.9072 |

The final Try80 model comparison table still reports the frozen prior baseline
already used by Try80 on the final 14-city test split: 1.9383 dB.

## Files and line locations changed

- `reduced/TFG/methodology.tex:72-75`: split-contract wording now states that
  Try78 and Try79 share the Try79/Try80 `split_seed = 42` training partition,
  with Try78 audited on the full validation+test pool and Try80 reported on
  the final test split.
- `reduced/TFG/results.tex:5-12`: chapter intro now explains the Try78
  validation+test audit and the Try80 final-test comparison separately.
- `reduced/TFG/results.tex:43`: representative milestone row updated from
  1.9246/1.75/3.40 to 1.9072/1.74/3.36.
- `reduced/TFG/results.tex:54-76`: path-loss prior narrative and LoS waterfall
  updated.
- `reduced/TFG/results.tex:149-154`: split-comparability note updated to
  describe the shared train partition and the held-out validation+test pool.
- `reduced/TFG/results.tex:205-214`: final hybrid path-loss prior table updated.
- `reduced/TFG/results.tex:528-541`: path-loss prior by height table updated.
- `reduced/TFG/results.tex:587-647`: path-loss prior by topology table and
  interpretation updated.
- `reduced/TFG/results_compact.tex:30,39-65`: compact results table and compact
  Try78 tables updated.
- `reduced/TFG/conclusions.tex:23-25`: conclusion headline Try78 number
  updated to 1.9072 dB on the held-out validation+test split.
- `reduced/TFG/conclusions_compact.tex:13-14`: compact conclusion headline
  updated.
- `reduced/TFG/prior_detail_try78.tex:1459-1462`: detailed Try78 section
  updated to the same 1.7379/3.3591/1.9072 values.
- `reduced/TFG/Internal_Documentation/New Prior Formulas Try 78 and 79.tex:1389-1450`:
  internal formula-results table and plot coordinates updated.
- `paper_version/paper.tex:1437-1441`: paper now states that the path-loss
  table uses the held-out validation+test split after fitting 10840 training
  references.
- `paper_version/paper.tex:1460-1472`: paper path-loss height table updated.
- `paper_version/paper.tex:1499-1504`: paper topology summary updated.
- `paper_version/paper.tex:1580-1584`: paper discussion updated to the 1.9072
  dB Try78 result.

Generated PDFs, extracted text checks, and result-addendum figures were also
updated in the thesis repository as build/artifact outputs; those files do not
have stable source line numbers.

## Previous tables preserved

These are the values that were present immediately before this same-split
Try78 audit was restored.

### Old LoS path-loss prior progression

| Prior | LoS RMSE (dB) | Gain over previous |
| --- | ---: | ---: |
| FSPL only | 3.9540 | N/A |
| FSPL + radial residual | 3.7086 | -0.25 |
| Enhanced two-ray | 1.7516 | -1.96 |

### Old final hybrid path-loss prior

| Region | RMSE (dB) |
| --- | ---: |
| LoS | 1.7516 |
| NLoS | 3.3967 |
| Overall | 1.9246 |

### Old path-loss prior by UAV height

| UAV height bin | Overall | LoS | NLoS | Samples |
| --- | ---: | ---: | ---: | ---: |
| 12 to 50 | 2.180 | 1.797 | 3.756 | 1211 |
| 50 to 150 | 1.936 | 1.785 | 3.228 | 2634 |
| 150 to 300 | 1.680 | 1.666 | 2.259 | 786 |
| 300 to 500 | 1.627 | 1.619 | 2.255 | 362 |

### Old path-loss prior by topology class

| Topology class | LoS | NLoS | Overall | Samples |
| --- | ---: | ---: | ---: | ---: |
| open sparse lowrise | 1.39 | 2.92 | 1.43 | 895 |
| open sparse vertical | 1.43 | 3.91 | 1.55 | 370 |
| mixed compact lowrise | 1.81 | 2.91 | 1.90 | 1240 |
| mixed compact midrise | 1.91 | 3.84 | 2.21 | 1060 |
| dense block midrise | 2.19 | 3.20 | 2.40 | 1325 |
| dense block highrise | 2.44 | 4.09 | 2.97 | 104 |
| Overall | 1.75 | 3.40 | 1.92 | 4994 |
