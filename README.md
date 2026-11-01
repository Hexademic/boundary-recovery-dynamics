# Boundary Recovery Dynamics

Canonical monograph repository for:

Boundary Recovery Dynamics: Observability Defines Recoverability in Adaptive Neural Reconstruction

Authors: The Relational Intelligence Working Group  
Target Venue: Journal of Machine Learning Research (JMLR)  
Status: Canonical Monograph

## Overview

This repository archives and presents a canonical manuscript on a central question in adaptive machine learning: when a model is disrupted and retrained on valid demonstrations, how much of its internal structural integrity is restored? The monograph argues that optimization can only repair what the observation channel can measure, and that task fluency can recover while invariant boundary structure remains degraded in unobserved null-space coordinates.

The manuscript formalizes this failure mode as Coherent Delusion and advances the principle:

Observability defines recoverability.

## Research theme

The work connects signal observability, representation geometry, invariant enforcement, and recovery dynamics. It argues that evaluations based only on observable task outputs can conceal severe degradation in the unobserved but load-bearing structure of adaptive systems.

## Repository structure

- `README.md` — project overview and entry point
- `manuscript/README.md` — manuscript archive index
- `manuscript/abstract.md` — abstract
- `manuscript/01-introduction.md` — introduction and problem framing
- `manuscript/02-generalized-observability-principle.md` — generalized observability principle
- `manuscript/03-prediction-jacobian-null-space.md` — prediction-Jacobian null-space analysis
- `manuscript/04-instrumentation-and-evaluation.md` — evaluation framework
- `manuscript/05-experimental-findings.md` — experimental findings
- `manuscript/06-implications.md` — implications and risks
- `manuscript/07-conclusion.md` — conclusion
- `manuscript/equations.md` — key equations
- `paper/README.md` — manuscript landing index
- `paper/boundary-recovery-dynamics.md` — polished manuscript summary
- `paper/references.bib` — bibliography
- `Boundary Recovery Dynamics _261031_151815.txt` — source manuscript text archive
- `docs/index.md` — documentation overview
- `CITATION.cff` — machine-readable citation metadata
- `LICENSE` — MIT license

## Key claims

- Behavioral competence and boundary grounding are partially separable properties.
- Standard ERM restores observed task outputs more rapidly than it restores invariant boundary discrimination.
- Unobserved null-space coordinates can silently accumulate structural damage after disruption.
- Constraint-guided recovery improves grounded persistence beyond behavioral fine-tuning alone.
- The primary challenge is not only optimization but observability of the system's latent structure.

## Citation

The Relational Intelligence Working Group. (2026). Boundary Recovery Dynamics: Observability Defines Recoverability in Adaptive Neural Reconstruction. Canonical Monograph.

## License

This repository is licensed under the MIT License. See `LICENSE` for details.
