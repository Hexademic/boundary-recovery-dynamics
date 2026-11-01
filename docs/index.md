# Project Overview

This repository archives and presents the canonical monograph on boundary recovery dynamics in adaptive neural systems.

## Purpose

The manuscript investigates a foundational problem in machine learning: when a model is disrupted and then retrained on valid data, how much of its internal structural integrity is restored? The central claim is that optimization can only repair what the observation channel can see. As a result, a model may recover fluent output behavior while leaving invariant boundary structure degraded in unobserved null-space coordinates.

## Core thesis

Observability defines recoverability.

In over-parameterized systems, the loss function is restricted to the observable projection and provides no direct supervisory signal for blind degrees of freedom. This creates a systematic asymmetry: standard empirical-risk minimization repairs task execution rapidly while leaving latent invariant boundaries under-constrained.

## Included materials

- Source manuscript: `../Boundary Recovery Dynamics _261031_151815.txt`
- Manuscript summary: `../paper/boundary-recovery-dynamics.md`
- Paper index: `../paper/README.md`
- Citation metadata: `../CITATION.cff`
- Bibliography: `../paper/references.bib`
- Repository landing page: `../README.md`

## Research themes

- adaptive optimization after parameter disruption
- observability, Jacobian structure, and null-space geometry
- invariant boundary discrimination
- Coherent Delusion
- grounded persistence and targeted invariant specificity (TIS)
- multi-domain recovery across physical, topological, and planning settings

## Citation

The Relational Intelligence Working Group. (2026). Boundary Recovery Dynamics: Observability Defines Recoverability in Adaptive Neural Reconstruction. Canonical Monograph.
