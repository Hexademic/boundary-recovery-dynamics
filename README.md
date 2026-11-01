# Boundary Recovery Dynamics

Canonical monograph repository for:

Boundary Recovery Dynamics: Observability Defines Recoverability in Adaptive Neural Reconstruction

Authors: The Relational Intelligence Working Group  
Target Venue: Journal of Machine Learning Research (JMLR)  
Status: Canonical Monograph

## Overview

This repository contains the canonical manuscript describing the observability hypothesis in adaptive neural systems: optimization can only repair what observation can see. The work formalizes the distinction between task competence and boundary grounding, showing that standard retraining can restore fluent behavior while leaving invariant structure degraded.

## Repository contents

- `paper/boundary-recovery-dynamics.md` — the manuscript in structured Markdown
- `Boundary Recovery Dynamics _261031_151815.txt` — the source manuscript text as provided
- `LICENSE` — MIT license

## Core thesis

- Behavioral fluency is not equivalent to invariant grounding.
- Empirical risk minimization acts only along the observation Jacobian.
- Unobserved null-space coordinates accumulate damage without restorative feedback.
- Constraint-guided reconstruction improves boundary discrimination and grounded persistence.

## Why this matters

The monograph argues that machine learning's central evaluation challenge is an observability problem before it is an optimization problem. Models can appear highly competent while silently degrading their internal boundary structure.

## Citation

The Relational Intelligence Working Group. (2026). Boundary Recovery Dynamics: Observability Defines Recoverability in Adaptive Neural Reconstruction. Canonical Monograph.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
