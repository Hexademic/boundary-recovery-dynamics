# Boundary Recovery Dynamics

## Abstract

Adaptive optimization repairs errors that manifest in observed outputs. But high-dimensional adaptive systems possess internal degrees of freedom that are only weakly coupled, or entirely uncoupled, from those outputs. What happens to load-bearing structure that resides within those unobserved coordinates?

Current evaluation paradigms assess post-disruption recovery almost exclusively by measuring loss or accuracy on valid demonstration data. In doing so, they conflate an agent's behavioral task execution with its capacity to discriminate physical, topological, and logical boundaries. This monograph demonstrates that when an adaptive neural system experiences severe parameter disruption, standard supervised retraining rapidly restores observable task fluency while leaving unobserved, load-bearing invariant boundaries severely degraded.

We formalize this failure mode—termed Coherent Delusion—not as an algorithmic defect of specific optimizers, but as a direct consequence of a broader principle: observability defines recoverability. Because an objective function can only exert restorative pressure along the range of its observation Jacobian, perturbations that project into the unobserved null space accumulate without penalty.

To instrument this blind spot, we develop a directional invariant sensor (TIS) embedded within an unbiased 2 × 3 contingency framework that decouples task execution from boundary recognition. Across three qualitatively distinct invariant classes—continuous Hamiltonian mechanics, discrete topological grid enclosure, and temporal-causal planning—we demonstrate that:

1. Standard behavioral fine-tuning via Empirical Risk Minimization (ERM) rapidly restores task execution but consistently under-recovers boundary grounding.
2. Augmenting fine-tuning with an internal constraint-guided transitivity objective recovers significantly higher Grounded Persistence.
3. Shapley decomposition shows that most early reconstruction advantage is attributable to boundary discrimination rather than behavioral recall.
4. Using a Prediction-Jacobian null-space formulation, we prove that consistency gradients can update representations without perturbing immediate task predictions.

These findings demonstrate that behavioral competence and boundary discrimination are partially separable dynamical properties of adaptive systems. We argue that machine learning's central evaluation challenge is an observability problem before it is an optimization problem: high performance can conceal severe degradation in unobserved but load-bearing internal structure.

## 1. Introduction

### 1.1 The Observability Deficit in Adaptive Optimization

Adaptive optimization repairs errors that manifest in observed outputs. But high-dimensional adaptive systems possess internal degrees of freedom that are only weakly coupled, or entirely uncoupled, from those outputs.

What happens to load-bearing structure that resides within those unobserved coordinates?

Consider an adaptive neural agent parameterized by weights θ ∈ ℝ^P. When the agent interacts with its environment, its internal state is projected through an observation channel:

Π_O : ℝ^P → 𝒴_obs

where 𝒴_obs denotes the observable output space. The loss function L(θ) = ℓ(Π_O(θ)) provides feedback solely based on discrepancies between the model's projected output ŷ = Π_O(θ) and the empirical target y.

If an agent experiences catastrophic parameter disruption, the damage is distributed across the entire parameter space. When the system is subsequently retrained on valid demonstrations using ERM, the gradient ∇_θ L acts exclusively along the coordinates that affect the output projection. Coordinates orthogonal to this projection receive zero direct supervisory signal.

This creates a structural asymmetry: optimization repairs what the output sensor sees while remaining blind to damage in the unobserved null space.

### 1.2 The Epistemic Inversion in Sequential Models

Modern machine learning is dominated by sequence modeling trained via conditional likelihood maximization. This objective treats transition probabilities over surface tokens as generative primitives. But transition probabilities are often only observational shadows cast by deeper invariant constraint fields.

The epistemic inversion is this: probabilities are observational shadows; invariant relational constraints are the generative substrate.

As a result, a system trained only to match the empirical distribution of valid demonstrations can recover fluent task behavior while losing the capacity to reject unphysical or counterfactual transitions.

### 1.3 Coherent Delusion

When a model is severely disrupted and then retrained on valid demonstrations, it often rapidly recovers observable task competence while its boundary discrimination remains poor. This state—competent-looking, fluent, and task-successful, yet internally ungrounded—is what we call Coherent Delusion.

## 2. The Generalized Observability Principle

Let an adaptive system be defined by internal coordinates θ ∈ Θ ⊆ ℝ^P. The environment and task define a differentiable observation projection:

Π_O : Θ → 𝒴_obs

Any supervised objective evaluates errors exclusively over this projection:

L(θ) = ℓ(Π_O(θ))

By the chain rule,

∇_θ L(θ) = [DΠ_O(θ)]^T ∇_y ℓ(Π_O(θ))

This induces the tangent-space decomposition:

𝒯_θ Θ = 𝒪_θ ⊕ 𝒰_θ

where

- 𝒪_θ = range([DΠ_O(θ)]^T) is the instrumented subspace,
- 𝒰_θ = ker(DΠ_O(θ)) is the blind subspace.

Only coordinates in 𝒪_θ receive restorative supervisory pressure. Coordinates in 𝒰_θ remain unconstrained unless a separate invariant signal is supplied.

This gives the central principle:

Observability defines recoverability.

## 3. Prediction-Jacobian Null Space

A key mechanism behind the failure mode is that task gradients are confined to the row space of the prediction Jacobian. Let probe b produce a scalar task prediction ŷ_b. The task Jacobian with respect to relational coordinates is:

J_b = ∇_{e_{b,upper}} ŷ_b

Its null space is:

N(J_b) = ker(J_b)

For the empirical loss, the ERM gradient is proportional to J_b^T. Therefore, the task gradient lies entirely in the row space of J_b and is orthogonal to the null space:

P_{N,b} g_ERM = 0

Thus standard task training cannot directly repair the boundary structure that lives in the null-space directions.

## 4. Instrumentation and Evaluation

To separate behavioral competence from boundary discrimination, the monograph introduces an unbiased 2 × 3 contingency framework that evaluates:

- lawful task execution,
- boundary recognition quality,
- rejection of invariant violations.

The metrics include:

- F1_lawful
- TIS (Targeted Invariant Specificity)
- GP (Grounded Persistence)

These allow the project to treat task success and boundary grounding as distinct axes of recovery.

## 5. Empirical Findings

Across the three invariant domains studied—continuous Hamiltonian mechanics, discrete topological grid enclosure, and temporal-causal planning—the following pattern appears robustly:

- Behavioral fine-tuning rapidly restores apparent competence.
- Boundary grounding remains persistently under-recovered.
- Constraint-guided reconstruction improves boundary discrimination and grounded persistence substantially.
- The early advantage is concentrated in boundary recovery rather than task recall.

This is precisely the signature of Coherent Delusion.

## 6. Implications

The monograph argues that machine learning's central evaluation challenge is an observability problem before it is an optimization problem. High performance on standard supervised data can conceal severe degradation in unobserved but load-bearing internal structure.

This has implications for:

- post-training and fine-tuning,
- pruning and quantization,
- continual learning,
- model safety,
- and the broader challenge of invariant grounding in adaptive systems.

## Conclusion

The central contribution of this work is to show that behavioral competence and boundary discrimination are not interchangeable. A system can be fluent and still be structurally under-grounded. Measuring only output-level task success is therefore insufficient; evaluation must also account for whether the model preserves the invariant boundaries that make its behavior lawful, stable, and recoverable.

Observability defines recoverability.
