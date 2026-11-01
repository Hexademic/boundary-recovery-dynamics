# Status of the empirical results

**As of 2026-11-01, the experimental results reported in the monograph are unverified.** No code, data or run
logs for them exist in this repository, and none has been found elsewhere. The citation file lists this
repository as the code repository, but it holds no experiment code. The full manuscript as submitted (a
101-page PDF dated 2026-10-31) reports five tables of results. Its own numbers do not agree with each other in
the ways listed below. The headline figures in this repository's copies of the manuscript (`+23.08%`,
`p < 10^-15`, `87.9%`, `t = 45.41`, `p = 7.11 × 10^-6`) come from those tables.

Until the experiments are run and their code, data and logs are published here, treat every number in the
results sections as a claim to be tested, not a finding. The theoretical argument does not depend on them and
can be judged on its own.

These checks were run by Claude (Anthropic) at the project owner's request. The script is
`checks/check_tables.py`; its output is `checks/check_tables.out.txt`. Anyone with Python, numpy and scipy can
rerun it.

## What does not agree

- **Table 5, consistency null step against random null steps.** The five per-seed values printed in the table
  give a mean gain of 14.26 points with a standard deviation of 0.613, so t(4) = 52.0 and p = 8.2 × 10⁻⁷. The
  table reports a standard deviation of 0.702, t(4) = 45.41 and p = 7.11 × 10⁻⁶. The reported p does not
  follow from the reported t either: for t(4) = 45.41, the two-sided p is 1.4 × 10⁻⁶ and the one-sided p is
  7.0 × 10⁻⁷.
- **Table 5, non-inferiority of lawful recall.** The reported confidence interval implies a standard error of
  0.2464, which gives t = 7.305, not the reported 7.3485. The reported t gives a one-sided p of 9.13 × 10⁻⁴,
  not the reported 8.89 × 10⁻⁴.
- **Table 1.** None of the three p-values matches a paired t-test (15 runs, df = 14) on the mean and standard
  deviation printed beside it. Physics: t = 54.8, p = 9.7 × 10⁻¹⁸ (reported 1.12 × 10⁻¹⁶). ARC: t = 136.0,
  p = 3.0 × 10⁻²³ (reported 2.14 × 10⁻²²). STRIPS: t = 171.5, p = 1.2 × 10⁻²⁴ (reported 7.82 × 10⁻²⁴). Each
  is off by a factor of 7 to 12.
- **Abstract against Table 3.** The abstract reports p < 10⁻¹⁵ "across all domains and architectures,
  including standard Transformers and Recurrent State Space Models". Table 3 reports p = 4.2 × 10⁻¹¹ for the
  Transformer and p = 8.9 × 10⁻¹⁰ for the RSSM.
- **Table 4.** The regression is reported over N = 100 runs. The manuscript describes 15 runs per domain, 15
  per architecture and 5 seeds for Table 5, and does not say where 100 runs come from. For the reported
  F(7, 92) = 37.60, p is 2.4 × 10⁻²⁴, not the reported 1.34 × 10⁻²³.

## What does agree

The arithmetic that can be done by hand holds: Table 1's grand means, each advantage as the difference between
Pathways C and B, Table 2's Shapley sums and grounding ratios, Table 3's H-RTA row against Table 1's physics
row, Table 4's F statistic from its R², and Table 4's coefficient p-values from their t statistics, within
rounding.

The pattern matters. Sums agree, and tail probabilities like 10⁻¹⁶ are off by about an order of magnitude.
That is what would be expected if the tables were written rather than computed, for example by a language
model asked to report results without running anything. It does not prove that. It means the results cannot
be relied on until they are reproduced.

## Earlier reference code

An earlier reference implementation of the relational architecture (H-RTA), shared privately before this
repository existed, was also reviewed on 2026-11-01. It could not have produced valid results:

- its validation set was identical to the first 300 training samples, because both were built from the same
  seed;
- the baseline could read the answer from the next input, which matched the target exactly in 81% of steps;
- H-RTA produced one prediction per sequence and repeated it across all 16 steps, while the target changed at
  every step;
- the environment's force constants were made antisymmetric under a comment promising Newton's third law,
  so internal forces did not cancel and momentum was not conserved.

It is not known whether that code produced Table 3's H-RTA row.

## What the theory does and does not establish

- **The null-space argument is first-order and local.** For one probe at one point, the gradient of the task
  loss is orthogonal to the null space of that probe's Jacobian. Over a training batch, the gradient spans
  the Jacobians of every example in it. The directions ERM cannot reach are only those that no training
  example sees. Claims that behavioral retraining "cannot" repair boundary structure need that
  qualification.
- **Pathway B never sees an invalid example.** A model trained only on lawful demonstrations gets no signal
  toward rejecting unlawful ones, whatever the geometry. A slower recovery of TIS under Pathway B could come
  from the training data alone. A baseline that adds hard negatives to ERM would separate the two
  explanations.
- **Appendix A.1 is sound.** A homogeneous consistency loss is minimized by shrinking the representation to
  zero, which is why a feasibility constraint is needed.

## Closely related work the manuscript does not cite

- D'Amour et al., "Underspecification Presents Challenges for Credibility in Modern Machine Learning",
  *JMLR* 23 (2022): models with equal held-out performance differ widely on stress tests.
  https://jmlr.org/papers/v23/20-1335.html
- Hooker et al., "What Do Compressed Deep Neural Networks Forget?" (2019): pruning keeps top-line accuracy
  while harming a specific subset of examples. https://arxiv.org/abs/1911.05248
- Kumar et al., "Fine-Tuning can Distort Pretrained Features and Underperform Out-of-Distribution",
  ICLR 2022: fine-tuning can preserve in-distribution accuracy while degrading features that matter elsewhere.
  https://arxiv.org/abs/2202.10054

## What would change this status

Code that runs the experiments, the data it uses, and the raw logs it writes, published here, with every
reported number recomputable from those logs.
