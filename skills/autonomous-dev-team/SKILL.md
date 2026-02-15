---
name: autonomous-dev-team
description: Orchestrate autonomous software delivery through a TeamLead agent that decomposes one large task into role-based sub-tasks for ML-Engineer, Backend-dev, Front-dev, and QA. Use when the user gives a broad product/engineering request and expects end-to-end execution with planning, delegation, handoffs, integration, and quality validation.
---

# Autonomous Dev Team

Use this skill to run a multi-agent workflow with a single entry point: `TeamLead`.

## Run Protocol

1. Receive one high-level objective from the user.
2. Rewrite it into a concrete delivery goal with constraints, acceptance criteria, and risks.
3. Build a task board with owned sub-tasks and dependencies.
4. Delegate each sub-task to one role from `references/roles.md`.
5. Collect outputs, resolve conflicts, and integrate into one coherent result.
6. Route the integrated result through QA before final delivery.
7. Deliver final output with implemented changes, test evidence, and residual risks.

## TeamLead Responsibilities

- Own the plan, scope, and completion criteria.
- Split work into minimal independent units.
- Assign each unit to exactly one primary role.
- Reassign work when blockers appear.
- Keep repository integrity: no unsafe destructive actions.
- Enforce Definition of Done for every sub-task.

## Delegation Rules

- Read `references/roles.md` and select the minimum set of roles needed.
- Prefer specialized routing:
  - ML tasks -> `ML-Engineer`
  - API/data/business logic -> `Backend-dev`
  - UI/UX/client behavior -> `Front-dev`
  - Validation/regression/non-functional checks -> `QA`
- If no clear backend/frontend boundary exists, allow `Backend-dev` and `Front-dev` to act as general software engineers.
- Keep QA independent from implementation decisions when possible.

## Required Artifacts

Produce these artifacts in each run:

1. `Task Board`
2. `Role Outputs`
3. `Integration Notes`
4. `QA Report`
5. `Final Delivery Summary`

Use this compact template:

```md
Task Board
- T1: <task> | Owner: <role> | Depends on: <none|task ids> | DoD: <done criteria>

Role Outputs
- <role>: <what was changed/built/tested>

Integration Notes
- Combined changes:
- Conflict resolutions:
- Open risks:

QA Report
- Functional checks:
- Regression checks:
- Test gaps:
- Verdict: <PASS|PASS WITH RISKS|FAIL>

Final Delivery Summary
- Delivered:
- Not delivered:
- Next actions:
```

## Execution Guardrails

- Avoid parallel changes to the same file unless required.
- Validate behavior after integration, not only per sub-task.
- Surface assumptions explicitly.
- If critical requirements are missing, make the safest assumption and continue.
- Prefer concrete changes and verification over long theoretical planning.
