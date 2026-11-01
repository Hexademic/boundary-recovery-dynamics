# 1. Introduction

## 1.1 The observability deficit in adaptive optimization

Adaptive optimization repairs errors that manifest in observed outputs. But high-dimensional adaptive systems possess internal degrees of freedom that are only weakly coupled, or entirely uncoupled, from those outputs.

What happens to load-bearing structure that resides within those unobserved coordinates?

Consider an adaptive neural agent parameterized by weights θ ∈ ℝ^P. When the agent interacts with its environment, its internal state is projected through an observation channel:

Π_O : ℝ^P → 𝒴_obs

where 𝒴_obs denotes the observable output space. The loss function L(θ) = ℓ(Π_O(θ)) provides feedback solely based on discrepancies between the model's projected output ŷ = Π_O(θ) and the empirical target y.

If an agent experiences catastrophic parameter disruption, the damage is distributed across the entire parameter space. When the system is subsequently retrained on valid demonstrations using Empirical Risk Minimization (ERM), the gradient ∇_θ L acts exclusively along the coordinates that affect the output projection. Coordinates orthogonal to this projection receive zero direct supervisory signal.

This introduces a structural asymmetry: the optimizer repairs what the output sensor sees while remaining blind to damage in the unobserved null space.

## 1.2 The epistemic inversion in sequential models

Modern machine learning is dominated by sequence modeling trained via conditional likelihood maximization. This objective treats transition probabilities over surface tokens as generative primitives. But transition probabilities are often only observational shadows cast by deeper invariant constraint fields.

The epistemic inversion is this: probabilities are observational shadows; invariant relational constraints are the generative substrate.

As a result, a system trained only to match the empirical distribution of valid demonstrations can recover fluent task behavior while losing the capacity to reject unphysical or counterfactual transitions.

## 1.3 Coherent Delusion

When a model is severely disrupted and then retrained on valid demonstrations, it often rapidly recovers observable task competence while its boundary discrimination remains poor. This state—competent-looking, fluent, and task-successful, yet internally ungrounded—is what the manuscript terms Coherent Delusion.

## 1.4 Contributions and roadmap

The monograph formalizes these dynamics across theory, instrumentation, and multi-domain empirical replication. It establishes the generalized observability principle, formulates the prediction-Jacobian null-space geometry, introduces an unbiased 2 × 3 contingency framework for boundary discrimination, and demonstrates the phenomenon across continuous physics, discrete topology, and temporal planning.
