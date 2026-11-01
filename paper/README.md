# Paper Index

> **Status (2026-11-01):** the experimental results reported in this monograph are unverified. No code, data or logs exist for them, and the reported statistics do not agree with each other. See [`RESULTS-STATUS.md`](../RESULTS-STATUS.md).

## Manuscript

Boundary Recovery Dynamics: Observability Defines Recoverability in Adaptive Neural Reconstruction

## Contents

- `boundary-recovery-dynamics.md` — manuscript summary with abstract, framing, technical sections, and conclusion
- `references.bib` — bibliography used to ground the monograph in machine learning and representation theory
- `Boundary Recovery Dynamics _261031_151815.txt` — original plain-text manuscript source as preserved in the repository

## Overview

This paper addresses a core representational issue in adaptive systems: when models are disrupted and then retrained on valid demonstrations, output-level competence often recovers much faster than boundary discrimination and latent invariant geometry. The project measures and models this gap as a recoverability problem rather than a simple performance problem.

## Publication framing

The manuscript is organized around three pillars:

1. The generalized observability principle
2. The geometry of prediction-Jacobian null spaces
3. A decoupled evaluation protocol for boundary grounding

Together, these argue that behavioral competence and boundary discrimination are separable but related dynamical properties of adaptive systems. The experiments meant to test this have not yet been run in reproducible form.

## Canonical citation

Boundary Recovery Dynamics project. (2026). Boundary Recovery Dynamics: Observability Defines Recoverability in Adaptive Neural Reconstruction. GitHub repository. https://github.com/Hexademic/boundary-recovery-dynamics

## Bibliography

The canonical literature base for the paper is maintained in `references.bib` and includes foundational work in observability, geometric learning, causal representation, robustness evaluation, and statistical diagnostics.
