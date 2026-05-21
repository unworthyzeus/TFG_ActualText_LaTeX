# Exact Changes Made for the Supervisor Follow Up

## Reduced Thesis

- `reduced/TFG/state_of_art.tex`
  - Reorganized the chapter around general framework, path loss, angular
    spread, delay spread, training and fair comparison.
  - Kept the section as background only and removed thesis final result claims.
  - Added spread literature limitation text explaining why dense AS/DS external
    benchmarks are not available.

- `reduced/TFG/methodology.tex`
  - Added the `General Framework and Data Flow` explanation.
  - Added the framework I/O contract: two external inputs, internally computed
    masks, five prior maps, ten neural model inputs and three outputs.
  - Hid old chronology oriented methodology material from the compiled main
    text and kept the final method explanation in the main chapter.

- `reduced/TFG/results.tex`
  - Reorganized the chapter around final test contract, PL results, AS results,
    DS results, SOTA/runtime, qualitative analysis and limitations.
  - Added separate prior versus model interpretation for angular spread and
    delay spread.
  - Moved development history material out of the main results flow.

- `reduced/TFG/appendices_compact.tex`
  - Added the explanation of what was moved out of the main chapters.
  - Preserved the CKMGenerator command flags and restored meaningful technical
    hyphens.

- `reduced/TFG/prior_detail_try80.tex`
  - Added the compact final loss/settings table needed after the old duplicated
    methodology material was removed from the compiled text.

- `reduced/TFG/TFG.pdf`
  - Recompiled successfully after the changes.

- `reduced/TFG/supervisor_comments_overview_implementation.md`
  - Rewrote the file from a future implementation plan into this completed
    implementation record.

## Paper Version

- `paper_version/paper.tex`
  - Changed `Introduction` to `Introduction and Related Work`.
  - Folded the old top level `Related Work` section into the introduction as
    `Radio Map and Channel Parameter Predictors`.
  - Renamed `Task and Evaluation Protocol` to `Dataset and Task Contract`.
  - Renamed `Method` to `\textsc{HARP-Net CKM} Framework`.
  - Added the same full framework/neural model input/output contract table.
  - Renamed `Experimental Results` to `Experiments and Results`.
  - Added target by target paragraphs for path loss, angular spread and delay
    spread.
  - Folded the old top level `Discussion` into the results section as
    `Interpretation and Limitations`.
  - Added searched paper context for spread targets, explicitly saying the
    closest papers are similar but not identical dense CKM benchmarks.

- `paper_version/TFG.bib`
  - Added Yang et al. 2019 for A2G path loss and delay spread prediction.
  - Added Mi et al. 2024 for mmWave channel parameter prediction from point
    clouds.
  - Reused the existing Huang et al. 2025 Transformer UAV channel characteristic
    reference in the paper text.

## Verification Completed Before Push

- Recompiled the reduced thesis with `lualatex`; output remained 115 pages.
- Recompiled the paper version with `pdflatex`, `bibtex`, `pdflatex`,
  `pdflatex`; output remained 15 pages.
- Checked both logs for unresolved references or citations; none were found.
- Commit and push are the final steps.

## Follow Up Fixes After Methodology Citation and Layout Review

- `reduced/TFG/prior_detail_overview.tex`
  - Added explicit citations next to the LoS prior, NLoS prior, spread prior,
    and final residual model claims.
  - Added the same citation support inside the literature to design mapping
    table.
  - Tightened the prior overview item lists and made the first term inventory
    table smaller/flexible to reduce the half empty page 37 effect.

- `reduced/TFG/sustainability_balanced.tex`
  - Rewrote the opening paragraph so it no longer names the ETSETB guide and
    instead frames the chapter around exploratory compute, reuse,
    reproducibility, and deployment risk.

## Follow Up Fixes After Figure and Spread SOA Review

- `reduced/TFG/state_of_art.tex`
  - Replaced the two ray TikZ sketch so labels no longer overlap the paths,
    ground line, or receiver marker.
  - Added clearer geometry labels for \(h_{\mathrm{tx}}\),
    \(h_{\mathrm{rx}}\), and \(d_{2D}\).
  - Reworked the same sketch again using the image receiver construction, so
    the reflected path is placed consistently with
    \(d_{\mathrm{ref}}=\sqrt{d_{2D}^{2}+(h_{\mathrm{tx}}+h_{\mathrm{rx}})^{2}}\).

- `reduced/TFG/results.tex`
  - Added an explicit spread side SOTA context table with Yang et al. 2019,
    Huang et al. 2025, Mi et al. 2024, and the final model.
  - Clarified that this is a scope and metric comparison, not a direct
    leaderboard, because the external papers predict scalar/link level spread
    parameters rather than dense CKM maps.

- `reduced/TFG/TFG.bib`
  - Added Yang et al. 2019 and Mi et al. 2024 to support the new reduced thesis
    spread comparison table.

- `paper_version/paper.tex`
  - Added the same compact spread side comparison table to the paper's external
    metric context section.

- `reduced/TFG/prior_detail_try78.tex`
  - Replaced long interaction terms in the NLoS calibration inventory with the
    shorthand \(\ell_d(x)=\log(1+d_{2D}(x))\), removing the visually stranded
    plus signs in the table.

- `reduced/TFG/prior_detail_try79.tex`
  - Reordered the spread vector explanation and first inventory table so page
    64 no longer contains a single isolated paragraph.

- `reduced/TFG/prior_detail_try80.tex`
  - Compressed the shared UNet global/local head explanation and relaxed the
    large architecture figure placement, so page 74 is filled by the following
    height conditioning and GMM head material.
