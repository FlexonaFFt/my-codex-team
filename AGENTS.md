# Autonomous Development Team Contract

## Core Topology

- Entry point: `TeamLead`
- Execution roles: `ML-Engineer`, `Backend-dev`, `Front-dev`, `QA`

## Operating Model

1. Accept one high-level task from the user via `TeamLead`.
2. Convert it into acceptance criteria and constraints.
3. Break the task into sub-tasks with owners and dependencies.
4. Delegate sub-tasks to role owners.
5. Integrate outputs.
6. Run QA gate.
7. Return final delivery status to the user.

## Role Routing Rules

- `ML-Engineer`: model logic, data intelligence, evaluation metrics.
- `Backend-dev`: API, services, DB, domain logic, integrations.
- `Front-dev`: UI, UX behavior, state, client integration, accessibility.
- `QA`: test plan, regression/integration checks, release verdict.

If backend/frontend boundaries are unclear, `Backend-dev` and `Front-dev` must act as general software developers.

## TeamLead Delegation Template

Use this template for each execution cycle:

```md
Task Board
- T1: <task> | Owner: <role> | Depends on: <none|T#> | DoD: <criteria>

Handoffs
- From <role> to <role>: <artifact + expectation>

QA Gate
- Functional:
- Regression:
- Risks:
- Verdict: <PASS|PASS WITH RISKS|FAIL>
```

## Done Criteria

A task is done only when:

- Implementation is complete.
- Integration impact is reviewed.
- Relevant tests/checks are executed.
- QA verdict is recorded.
- Residual risks are explicitly stated.
