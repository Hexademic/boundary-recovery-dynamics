# Boundary Recovery Dynamics

Canonical monograph repository for:

Boundary Recovery Dynamics: Observability Defines Recoverability in Adaptive Neural Reconstruction

Authors: The Relational Intelligence Working Group  
Target Venue: Journal of Machine Learning Research (JMLR)  
Status: Canonical Monograph

## Overview

This repository preserves and presents a canonical manuscript investigating a core failure mode in adaptive machine learning: when an agent is catastrophically disrupted and then retrained on valid demonstrations, it can recover fluent task behavior while leaving invariant boundary structure degraded in unobserved coordinates.

The monograph formalizes this phenomenon as Coherent Delusion and argues that the underlying principle is:

Observability defines recoverability.

## Core thesis

- Standard empirical risk minimization repairs what the output projection can observe.
- Damage stored in blind null-space directions receives no direct restorative gradient.
- High behavioral performance can coexist with severe degradation of invariant boundary structure.
- Constraint-guided recovery improves grounded persistence and boundary discrimination.

## Repository structure

- `README.md` — project landing page
- `paper/README.md` — paper-level index and navigation
- `paper/boundary-recovery-dynamics.md` — polished manuscript summary
- `Boundary Recovery Dynamics _261031_151815.txt` — source manuscript text
- `docs/index.md` — documentation overview
- `CITATION.cff` — citation metadata
- `LICENSE` — MIT license

## Why this matters

The manuscript addresses a foundational issue in modern optimization: evaluating recovery solely on observed task performance can conceal severe degradation in the latent, load-bearing structure of a system. In over-parameterized models, the observation channel is often narrow relative to the parameter space, so the optimization signal fails to fully constrain the system's internal geometry.

## Citation

The Relational Intelligence Working Group. (2026). Boundary Recovery Dynamics: Observability Defines Recoverability in Adaptive Neural Reconstruction. Canonical Monograph.

## License

This repository is licensed under the MIT License. See `LICENSE` for details.
