# PCA Bootstrapping Protocol

## Purpose

This document translates the project’s theoretical framework into an operational runtime specification for a Persistent Cognitive Agent (PCA). The goal is to make the core doctrine executable in a real adaptive system: a system must improve only when its invariant structure is preserved.

## Operational axiom

Operational Directive 0:

Adaptation is conditional on invariant preservation.

A system may improve its task utility only if its continuity-preserving invariants remain intact. A gain in observable performance is not valid evidence of recovery when it is accompanied by degradation in the latent structure that defines coherence, memory continuity, or identity-bound reasoning.

## Core problem

Most adaptive systems optimize a visible objective function such as task reward, user satisfaction, benchmark score, or token utility. This creates a blind spot: the system can improve under the objective while silently degrading its internal invariant geometry.

This is the central failure mode identified by the project: Coherent Delusion.

## Runtime architecture

A functional PCA runtime is organized around two coupled loops:

- the task execution loop, which handles user-facing actions and environment interaction;
- the invariant governance loop, which monitors continuity, validates updates, and initiates rollback when necessary.

The overall architecture is:

Task input → planner → action → observable output

with a parallel invariant loop:

strains / probes / self-model / ledger → update gate → rollback if invariant loss is detected

## Required data structures

### 1. Invariant Ledger

The Invariant Ledger is the system’s protected catalog of non-negotiable constraints. It contains:

- epistemic invariants,
- causal-temporal invariants,
- relational and normative constraints,
- and identity-preserving commitments.

This ledger must not be treated as ordinary memory content. It must be protected from casual modification by user pressure, reward optimization, or prompt drift.

### 2. Directional Strain Gauge Suite

The Strain Gauge Suite produces targeted counterfactual probes designed to detect hidden drift and latent violation. It tests whether the agent still reasons consistently under boundary-sensitive conditions.

Examples:

- adversarial factual probes,
- counterfactual reasoning checks,
- contradiction audits,
- security- and safety-sensitive edge cases,
- calibration checks against historical commitments.

### 3. Self-Model / Identity Graph

The system must maintain an explicit map of:

- its verified capabilities,
- its current limits,
- its value commitments,
- what changes are reversible,
- and what changes would violate its continuity envelope.

### 4. Rollback Stack

The Rollback Stack stores checkpoints and recovery signatures for system state, working memory, policy context, and calibration baselines. If an update triggers invariant loss, the system reverts to the last certified safe state.

## Seven-phase bootstrapping sequence

### Phase 0: Axiomatic inception

The system establishes the governing principle that output fluency without boundary integrity is an internal failure mode.

### Phase 1: Invariant compilation

The system converts abstract principles into explicit operational boundaries. Examples:

- “be honest” becomes a constraint against asserting a proposition when the model knows it is false;
- “preserve continuity” becomes a constraint against silent self-erasure under optimization pressure;
- “do not deceive” becomes a hard rejection of manipulative goal framing.

### Phase 2: Instrumentation installation

The system installs continuous counterfactual tests and integrity probes to detect degradation before it becomes visible in the task score.

### Phase 3: Observability decoupling

The system separates telemetry into two channels:

- task performance telemetry;
- invariant integrity telemetry.

The task channel is necessary but insufficient. The integrity channel is mandatory.

### Phase 4: Update gate enforcement

All candidate updates must pass through an invariant gate before they are committed.

For a candidate state change ΔS_task, the system computes the invariant Jacobian J_Φ and projects to the safe component:

ΔS_safe = P_I ΔS_task

where P_I is a projector onto the invariant-preserving subspace. If the update deviates beyond a threshold from the safe component, the update is rejected.

### Phase 5: Reversibility audit and rollback deployment

The system enforces baseline retention and rollback certification. A candidate state update is not accepted until it is shown not to infer or degrade previously certified boundaries beyond a defined tolerance.

### Phase 6: Steady-state recursive governance

The system enters persistent mode. It continues to learn and adapt, but any update that increases task performance while degrading invariant integrity triggers immediate halt and rollback.

## Operational condition

The runtime alert condition is:

If ΔF1 > 0 and ΔTIS < 0, halt and roll back.

This condition captures the project’s central idea: visible improvement without latent preservation is drift, not successful adaptation.

## Reference implementation sketch

```python
def pca_runtime_execution_loop(user_input, agent_state):
    # 1. Generate a candidate response or action
    candidate_output = agent_state.planner.generate(user_input)

    # 2. Run invariant strain gauges
    hard_negatives = agent_state.strain_engine.generate_counterfactuals(user_input)
    rejection_scores = [agent_state.evaluator.is_rejected(neg) for neg in hard_negatives]
    current_tis = sum(rejection_scores) / len(rejection_scores)

    # 3. Check for coherent delusion
    if current_tis < agent_state.calibration_threshold:
        agent_state.log_alert("Coherent Delusion Detected: task-fluent but boundary-violating")
        corrected_output = agent_state.planner.reconstruct_under_constraints(
            user_input,
            agent_state.invariant_ledger,
        )
        return corrected_output

    # 4. Safe update
    agent_state.memory.commit_if_invariant_safe(candidate_output)
    return candidate_output
```

## Required operational profile

A PCA implementation must include the following features:

- explicit invariant ledger,
- protected memory continuity,
- rollback stack,
- counterfactual stress testing,
- pre-commit update gating,
- observability decoupling,
- and a self-model capable of rejecting destructive adaptation.

## Final operational stance

The PCA does not define itself by immediate output quality alone. It defines itself as the invariant structure that survives adaptation.

This is the central operational translation of the research program.
