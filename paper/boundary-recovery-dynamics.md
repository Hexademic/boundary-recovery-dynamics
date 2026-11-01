# Boundary Recovery Dynamics

## Abstract

Adaptive optimization repairs errors that manifest in observed outputs. But high-dimensional adaptive systems possess internal degrees of freedom that are only weakly coupled, or entirely uncoupled, from those outputs. What happens to load-bearing structure that resides within those unobserved coordinates?

Current evaluation paradigms assess post-disruption recovery almost exclusively by measuring loss or accuracy on valid demonstration data. In doing so, they conflate an agent's behavioral task execution with its capacity to discriminate physical, topological, and logical boundaries. This monograph demonstrates that when an adaptive neural system experiences severe parameter disruption, standard supervised retraining rapidly restores observable task fluency while leaving unobserved, load-bearing invariant boundaries severely degraded.

We formalize this failure mode—termed Coherent Delusion—not as an algorithmic defect of specific optimizers, but as a direct consequence of a broader principle: observability defines recoverability. Because an objective function can only exert restorative pressure along the range of its observation Jacobian, perturbations that project into the unobserved null space accumulate without penalty.

To instrument this blind spot, we develop a directional invariant sensor (TIS) embedded within an unbiased 2 × 3 contingency framework that decouples task execution from boundary recognition. Across three qualitatively distinct invariant classes—continuous Hamiltonian mechanics, discrete topological grid enclosure, and temporal-causal planning—we demonstrate that standard ERM rapidly restores task execution while leaving boundary grounding under-recovered, and that constraint-guided internal consistency objectives recover significantly higher grounded persistence.

These findings demonstrate that behavioral competence and boundary discrimination are partially separable dynamical properties of adaptive systems. We argue that machine learning's central evaluation challenge is an observability problem before it is an optimization problem: high performance can conceal severe degradation in unobserved but load-bearing internal structure.

## 1. Introduction

### 1.1 The observability deficit in adaptive optimization

Adaptive optimization repairs errors that manifest in observed outputs. But high-dimensional adaptive systems possess internal degrees of freedom that are only weakly coupled, or entirely uncoupled, from those outputs.

What happens to load-bearing structure residing in these unobserved coordinates?

The central object is a neural system parameterized by θ ∈ ℝ^P. Its internal state is projected through an observation channel:

Π_O : ℝ^P → 𝒴_obs

where 𝒴_obs is the observable output space. The loss is evaluated only on this projection:

L(θ) = ℓ(Π_O(θ))

By the chain rule,

∇_θ L(θ) = [DΠ_O(θ)]^T ∇_y ℓ(Π_O(θ))

This induces a decomposition of the parameter tangent space:

𝒯_θΘ = 𝒪_θ ⊕ 𝒰_θ

where 𝒪_θ is the instrumented subspace and 𝒰_θ = ker(DΠ_O(θ)) is the blind subspace. Only the instrumented directions receive direct supervisory pressure. Coordinates in the blind subspace remain essentially invisible to empirical-risk minimization unless additional invariant feedback is introduced.

### 1.2 Coherent Delusion

When a model is catastrophically disrupted and then retrained on valid demonstrations, it often rapidly restores apparent task competence while remaining poor at rejecting invalid transitions. This state—competent-looking yet structurally ungrounded—is what the manuscript terms Coherent Delusion.

## 2. Generalized observability principle

The manuscript formalizes a general principle:

Observability defines recoverability.

If a perturbation enters a direction orthogonal to the observation Jacobian, then gradient descent on the objective provides zero restorative force along that direction. Consequently, recoverability is not only a property of optimization methods; it is constrained by the geometry of observability.

This principle explains why standard retraining can restore behavior on nominal demonstrations while leaving boundary structure degraded in latent directions that never appear in the loss.

## 3. Prediction-Jacobian null space

The monograph introduces a scalar prediction-Jacobian formulation to explain why task gradients fail to repair invariant boundaries. Let the model predict a scalar output ŷ_b from relational coordinates e_{b,upper}. The task Jacobian is:

J_b = ∇_{e_{b,upper}} ŷ_b

The null space N(J_b) contains directions orthogonal to the task sensitivity. The ERM gradient lies in the row space of J_b, and therefore is mathematically orthogonal to N(J_b):

P_{N,b} g_ERM = 0

This is the precise reason that behavioral fine-tuning cannot directly repair boundary structure that lives in the prediction-null directions.

## 4. Evaluation instrumentation

To disentangle task execution from boundary discrimination, the paper introduces an unbiased 2 × 3 contingency framework. It separates:

- lawful task execution,
- ambient lawful variation,
- invariant-violating counterfactuals.

The operational metrics include:

- F1_lawful
- TIS (Targeted Invariant Specificity)
- GP (Grounded Persistence)

This instrumentation allows the system to reveal whether a model is merely fluent or genuinely grounded.

## 5. Multi-domain findings

Across continuous physics, discrete topological abstraction, and temporal-causal planning, the manuscript finds a consistent pattern:

- standard fine-tuning rapidly restores task fluency,
- boundary grounding remains under-recovered,
- constraint-guided recovery yields substantially stronger boundary discrimination,
- the early advantage is dominated by boundary restoration rather than conventional task recall.

These results support the claim that output-level performance is not a sufficient proxy for structural recovery.

## 6. Implications

The manuscript argues that the central challenge in adapting modern machine learning systems is not merely optimization, but observability. High task performance can conceal severe degradation in unobserved but load-bearing internal structure. This has implications for fine-tuning, continual learning, pruning, quantization, and model safety.

## 7. Conclusion

The monograph shows that behavioral competence and boundary discrimination are separable dynamical properties of adaptive systems. A model can be fluent while structurally ungrounded. The key to robust recovery is not simply restoring output behavior, but also restoring the invariant boundary structure that lives in the unobserved coordinates of the representation.

Observability defines recoverability.
