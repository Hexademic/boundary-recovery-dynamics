# 4. Instrumentation and Evaluation

## 4.1 The unbiased 2 × 3 contingency framework

The evaluation framework separates behavioral competence from boundary discrimination by constructing a test suite with three mutually exclusive categories:

- Ω_agent: lawful transitions under baseline coupling,
- Ω_amb: lawful transitions under alternative valid parameters,
- Ω^-_hard: invariant-violating counterfactuals.

This avoids collapsing task acceptance into a single scalar figure of merit for lawful behavior.

## 4.2 Metrics

The monograph uses the following quantities:

- F1_lawful: task-level lawful behavior score,
- TIS: Targeted Invariant Specificity,
- GP: Grounded Persistence.

The key operational quantity is:

TIS = TN / (TN + FP)

This is used as a directional strain gauge on the boundary layer: it measures whether a model rejects invariant violations while preserving lawful behavior.

## 4.3 Why TIS matters

TIS is not a universal measure of intelligence. It is an instrumented metric along a specific invariant normal direction. It is valuable precisely because it isolates whether the model recognizes the boundary that matter for a particular class of transition.

## 4.4 Shapley decomposition

The manuscript decomposes recovery advantage into behavioral and boundary components. The central insight is that early recovery is dominated by boundary restoration rather than by task recall. This explains why a model can appear to recover quickly while still remaining structurally unsound.
