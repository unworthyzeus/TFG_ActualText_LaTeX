# Completed Implementation Record for Overview Meeting Comments

Source notes:

- `reduced/TFG/supervisor_comments_overview_meeting.md`
- `paper_version/supervisor_notes_summary.md`

Status: completed for the reduced thesis and applied to the paper version.

## What Was Implemented in the Reduced Thesis

### 1. Matching Reader Order Across Chapters

Chapters 2, 3 and 4 now follow the same reader-facing order:

1. general framework and evaluation contract,
2. path loss,
3. angular spread,
4. delay spread,
5. interpretation, comparison and limitations.

This fixes the earlier problem where the background, method and results used
different internal structures.

### 2. Full Framework Input/Output Contract

Chapter 3 now explicitly separates:

- the two external inputs to the full framework: building-height map and UAV
  transmitter height;
- the internally computed support maps: LoS/NLoS visibility and valid
  ground-receiver mask;
- the five frozen prior maps: combined path-loss prior, LoS path-loss prior,
  NLoS path-loss prior, delay-spread prior and angular-spread prior;
- the ten internal inputs to `\textsc{HARP-Net CKM}`;
- the three final outputs: path loss, delay spread and angular spread.

This directly addresses the supervisor note that the full framework and the
neural model should not be described as having the same inputs.

### 3. Symmetric Target Comparisons

Chapter 4 now has separate result discussions for:

- path loss,
- angular spread,
- delay spread.

Each target is compared against its frozen prior and interpreted separately.
Angular spread and delay spread no longer look like secondary afterthoughts.
The text also states why external comparisons are weaker for spread targets.

### 4. SOTA Kept as Background

Chapter 2 was kept free of thesis final-result values. It now prepares the
reader for Chapter 4 by explaining that most external spread-prediction papers
report scalar or link-level parameters, not dense CKM maps under city holdout.

### 5. Paper Search Added for Spread Context

I checked nearby spread-prediction literature and used the relevant lesson:
there are similar channel-parameter prediction papers, but they do not match
the dense CKM city-holdout task.

References verified during this pass:

- Yang et al., "Machine-learning-based prediction methods for path loss and
  delay spread in air-to-ground millimetre-wave channels", IET MAP, 2019,
  DOI `10.1049/iet-map.2018.6187`.
- Huang et al., "Transformer-Based Air-to-Ground mmWave Channel
  Characteristics Prediction for 6G UAV Communications", Sensors, 2025,
  DOI `10.3390/s25123731`.
- Mi et al., "Measurement-Based Prediction of mmWave Channel Parameters Using
  Deep Learning and Point Cloud", IEEE OJVT, 2024,
  DOI `10.1109/OJVT.2024.3436857`.

The conclusion from the search is now reflected in the paper version: these
works are close in target type but not direct benchmarks because they do not
predict full dense PL/DS/AS maps over unseen CKM cities.

### 6. Wording Simplification and Hyphen Cleanup

Overly difficult phrasing was simplified where it was not needed. Technical
hyphens were kept where they carry meaning, especially in command flags and
standard compounds such as `city-holdout`, `two-ray`, `path-loss prior`,
`knife-edge`, `delay-spread`, `angular-spread` and `RMSE-dominant`.

### 7. Main Chapters Are Self-Contained

The main chapters now explain the final framework without requiring Appendix A.
Appendix A keeps the development history, negative results and diagnostic
attempts, but the final method can be understood from the main text alone.

## What Was Applied to the Paper Version

The paper version was adapted to the shorter paper-style structure requested in
`paper_version/supervisor_notes_summary.md`:

1. `Introduction and Related Work`
2. `Dataset and Task Contract`
3. `\textsc{HARP-Net CKM} Framework`
4. `Experiments and Results`
5. `Code Availability`
6. `Conclusion`

The separate Related Work top-level section was folded into the introduction,
and the former Discussion section was folded into the results as
`Interpretation and Limitations`.

The paper also received:

- the same full-framework versus neural-model input/output clarification;
- a clearer target-by-target result discussion for PL, AS and DS;
- spread-literature context based on the additional paper search;
- two new bibliography entries for the A2G delay-spread and point-cloud
  channel-parameter papers.

## Acceptance Checklist

- [x] Reduced thesis chapters 2, 3 and 4 use visibly matching section order.
- [x] Chapter 3 states the full framework has two external inputs and three
  final outputs.
- [x] Chapter 3 states the neural model receives ten internal inputs and outputs
  three maps.
- [x] Chapter 4 has separate path-loss, angular-spread and delay-spread result
  discussions.
- [x] SOTA does not contain thesis final-result values.
- [x] Delay-spread and angular-spread comparisons are present.
- [x] The text explains that only one or two nearby papers have similar, not
  identical, spread-prediction goals.
- [x] Overly technical words are simplified where they are not needed.
- [x] Necessary technical hyphens and command flags are preserved.
- [x] Main chapters are understandable without Appendix A.
- [x] Appendix A remains the place for development history and negative
  attempts.
- [x] Paper version follows a more compact paper structure.
- [x] Paper version applies the same reduced-thesis lessons.
