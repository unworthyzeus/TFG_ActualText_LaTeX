# Visual polish TODO

These are presentation-only improvements to consider after the content is stable.

- Shorten the List of Figures by using optional short captions:
  `\caption[Short caption]{Long caption}`.
- Consider `hidelinks` or a more restrained link color for print/export, because
  the current orange links dominate the contents and figure/table lists.
- Simplify the main-body Try 80 `6x3` inspection panel, whose labels are hard to
  read at thesis scale; keep the full diagnostic panel in the appendix.
- Replace informal labels such as `Try 80 huge` with wording like
  `large-width Try 80 variant` or `final high-capacity Try 80 configuration`.


- Also, apart from this, but a bit included, is maybe renaming the "tries"
  to actual descriptive names. To someone that doesn't have access to the 
  repo or hasn't worked on the project can be confusing. Try 76 and 77 called GMM head U-Net or similar, and the same but with prior and just predicting the difference for try 80.
- There are also some mentions to old tries (before 76) in tables, some graphs, etc. Also change those to some more appropiate name investigating what they exactly were. In the tables of how the methodology evolved, remove the exact try number, use their names, and just preserve order of trying to implement them.
- And, finally, linear regression is what's used in try 78 and 79, right?
 and that's Machine Learning, maybe the prior should be called ML calibrated prior. And explain the differences.
 Rename try 78 and 79 to correct name (based on how they predict), taking into account their 6 experts (topology classes)x3 (antenna height) x2 (LoS and nLoS, which are differently calibrated) (try 78) and 2 metrics x 6 experts x 3 antenna height x2 (LoS and nLoS), in total 72. And try 80 , even though it uses all these experts only reports 3 antenna heights x 3 experts. Maybe add why.