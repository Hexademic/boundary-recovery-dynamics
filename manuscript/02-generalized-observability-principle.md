# 2. The Generalized Observability Principle

Let an adaptive system be defined by internal coordinates θ ∈ Θ ⊆ ℝ^P. The environment and task define a differentiable observation projection:

Π_O : Θ → 𝒴_obs

Any supervised objective evaluates errors exclusively over this projection:

L(θ) = ℓ(Π_O(θ))

By the chain rule,

∇_θ L(θ) = [DΠ_O(θ)]^T ∇_y ℓ(Π_O(θ))

This differential map induces an exact orthogonal decomposition of the parameter tangent space:

𝒯_θΘ = 𝒪_θ ⊕ 𝒰_θ

where

- 𝒪_θ = range([DΠ_O(θ)]^T) is the instrumented subspace,
- 𝒰_θ = ker(DΠ_O(θ)) is the blind subspace.

Only coordinates in 𝒪_θ receive restorative supervisory pressure. Coordinates in 𝒰_θ remain unconstrained unless a separate invariant signal is supplied.

This gives the central principle:

Observability defines recoverability.

## 2.1 The entropy of uncoupled coordinates

In an overparameterized system (P >> d_obs), external perturbations act broadly across the entire tangent space. The task loss L acts as a dissipative sink, but only along the low-dimensional subspace 𝒪_θ. Along the uncoupled subspace 𝒰_θ, there is no restorative gradient. The coordinates in 𝒰_θ behave like an unmonitored thermodynamic reservoir. In the absence of explicit monitoring, entropy accumulates in the blind coordinates.

## 2.2 What lives in the blind subspace?

The blind subspace is not itself the boundary structure. Rather, it is the permissive medium within which boundary structure can silently degrade without producing an error signal.

It contains three qualitatively different components:

1. gauge redundancies,
2. dormant task circuits,
3. load-bearing invariant normals.

Behavioral fine-tuning restores the instrumented subspace, but leaves invariant boundary structure fractured in the blind subspace.

## 2.3 Formal take-away

The principal lesson is straightforward: an optimization objective only exerts force in the observed directions. Recoverability is therefore constrained by observability before by optimization.
