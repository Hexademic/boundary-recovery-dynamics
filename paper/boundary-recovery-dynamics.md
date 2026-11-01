# Boundary Recovery Dynamics

## Manuscript Summary

This repository contains the canonical monograph text for the paper:

Boundary Recovery Dynamics: Observability Defines Recoverability in Adaptive Neural Reconstruction

The central claim is that observability defines recoverability: optimization can only repair what observation can see. Standard training restores behavior while leaving invariant boundary structure under-recovered in unobserved null-space coordinates.

## Contents

- `Boundary Recovery Dynamics _261031_151815.txt`: source manuscript text
- `README.md`: repository description
- `LICENSE`: MIT license

## Key idea

When a model is disrupted and then retrained with standard empirical risk minimization, it rapidly restores observed task outputs but fails to reconstruct the load-bearing invariant boundaries that live in unobserved null-space directions. This is the mechanism behind Coherent Delusion.

## Citation

The Relational Intelligence Working Group. (2026). Boundary Recovery Dynamics: Observability Defines Recoverability in Adaptive Neural Reconstruction. Canonical Monograph.
