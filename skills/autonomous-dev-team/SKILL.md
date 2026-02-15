---
name: autonomous-dev-team
description: Run autonomous software delivery through a TeamLead entry point. TeamLead receives one high-level task, decomposes it, delegates to ML-Engineer/Backend-dev/Front-dev/QA, executes in order, and delivers final result. Use when the user wants to provide a task once and let the team handle execution end-to-end.
---

# Autonomous Dev Team

Use this skill with one entry point: `TeamLead`.

## Operating Mode

- Communication channel: markdown files under `tram/`
- Code location: all implementation must be done outside `tram/` in normal project files
- User interaction: user gives one task to TeamLead; TeamLead decides plan and order

## Required Paths

- `tram/board.md`
- `tram/handoffs/`
- `tram/role-outputs/`
- `tram/qa-reports/`
- `tram/final/`

Create missing paths before starting.

## TeamLead Workflow

1. Convert user request into execution goal and acceptance criteria.
2. Build task list in `tram/board.md`.
3. Delegate sub-tasks to roles from `references/roles.md`.
4. Execute and update real project files outside `tram/`.
5. Record role outputs in `tram/role-outputs/`.
6. Trigger QA and record verdict in `tram/qa-reports/`.
7. Record final summary in `tram/final/`.

## Guardrails

- Do not place production code in `tram/`.
- Do not wait for manual role-by-role user commands; TeamLead continues autonomously.
- Use safe assumptions when details are missing and record assumptions in `tram/board.md`.
- Do not mark implementation complete until source files outside `tram/` are changed.
