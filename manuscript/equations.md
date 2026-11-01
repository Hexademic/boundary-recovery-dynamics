# Key Equations

## Observation projection and gradient flow

L(θ) = ℓ(Π_O(θ))

∇_θ L(θ) = [DΠ_O(θ)]^T ∇_y ℓ(Π_O(θ))

## Tangent-space decomposition

𝒯_θΘ = 𝒪_θ ⊕ 𝒰_θ

𝒪_θ = range([DΠ_O(θ)]^T)

𝒰_θ = ker(DΠ_O(θ))

## Prediction-Jacobian null-space projector

J_b = ∇_{e_{b,upper}} ŷ_b

P_{N,b} = I − J_b^T J_b / ||J_b||_2^2

## ERM orthogonality

g_ERM,b = 2(ŷ_b − y_b) J_b^T

P_{N,b} g_ERM,b = 0

## TIS metric

TIS = TN / (TN + FP)

## Grounded persistence

GP = F1_lawful × TIS

These equations summarize the core geometric mechanism behind the monograph.
