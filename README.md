# Boundary Recovery Dynamics

Canonical monograph repository for:

Boundary Recovery Dynamics: Observability Defines Recoverability in Adaptive Neural Reconstruction

Authors: The Relational Intelligence Working Group  
Target Venue: Journal of Machine Learning Research (JMLR)  
Status: Canonical Monograph

## Overview

This repository preserves and presents a canonical manuscript on the principle that observability defines recoverability in adaptive neural systems. The work argues that optimization can only repair what observation can see, and that standard behavioral retraining can restore fluent task execution while leaving invariant boundary structure degraded in unobserved null-space coordinates.

## Repository structure

- `README.md` — project landing page
- `paper/boundary-recovery-dynamics.md` — manuscript summary in structured Markdown
- `Boundary Recovery Dynamics _261031_151815.txt` — source manuscript text as provided
- `docs/index.md` — project overview and navigation page
- `CITATION.cff` — citation metadata
- `LICENSE` — MIT license

## Core thesis

- Behavioral competence and boundary grounding are separable dynamical properties.
- ERM acts only along the observable task Jacobian, leaving blind null-space directions under-constrained.
- Unobserved coordinates can silently accumulate structural damage after disruption.
- Constraint-guided reconstruction restores grounded persistence more effectively than behavioral retraining alone.

## Citation

The Relational Intelligence Working Group. (2026). Boundary Recovery Dynamics: Observability Defines Recoverability in Adaptive Neural Reconstruction. Canonical Monograph.

## License

This repository is licensed under the MIT License. See `LICENSE` for details.
