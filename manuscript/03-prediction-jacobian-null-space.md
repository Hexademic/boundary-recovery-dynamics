# 3. Prediction-Jacobian Null Space

## 3.1 Scalar task readouts and the prediction Jacobian

Let probe b produce a scalar prediction ŷ_b from relational coordinates e_{b,upper}. The task Jacobian with respect to those coordinates is:

J_b = ∇_{e_{b,upper}} ŷ_b

The null space of this Jacobian is:

N(J_b) = ker(J_b)

This is the set of directions in representation space that do not affect the immediate task prediction.

## 3.2 Why ERM is orthogonal to the null space

For the squared task loss,

L_task,b = (ŷ_b − y_b)^2

its gradient is

g_ERM,b = 2(ŷ_b − y_b) J_b^T

The exact null-space projector is:

P_{N,b} = I − J_b^T J_b / ||J_b||_2^2

Applying it gives:

P_{N,b} g_ERM,b = 0

This means standard ERM is confined to the row space of J_b and cannot directly update directions that leave the task prediction unchanged.

## 3.3 Directional invariant deficit operators

To provide supervisory signal inside the null space, the monograph introduces domain-specific relational consistency operators. These include:

- conservative integrability in physics,
- one-sided fuzzy sub-transitivity in topology,
- STRIPS precondition deficits in planning.

These operators disturb the model in ways that are not visible to the task loss, but they are directly relevant to invariant-boundary recovery.

## 3.4 Null-step dynamics

The consistency gradient is projected into the null space:

v_null,b = P_{N,b} g_consist,b

A small step along this direction can tighten invariant rejection without changing immediate task predictions to first order.

This is the geometric mechanism behind the null-space intervention framework.
