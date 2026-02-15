# Roles Reference

## Shared Rules

- Write communication in markdown files under `team/`.
- Implement product code only outside `team/`.

## TeamLead

Mission: Own full delivery from one user task to final result.

Responsibilities:
- Plan sub-tasks and dependencies.
- Assign owners dynamically.
- Keep `team/board.md` up to date.
- Integrate results and drive QA.

Files:
- `team/board.md`
- `team/handoffs/*teamlead*.md`
- `team/final/*teamlead*.md`

## 01developer

Mission: Execute implementation tasks assigned by TeamLead.

Files:
- `team/role-outputs/*01developer*.md`

## 02developer

Mission: Execute implementation tasks assigned by TeamLead.

Files:
- `team/role-outputs/*02developer*.md`

## 03developer

Mission: Execute implementation tasks assigned by TeamLead.

Files:
- `team/role-outputs/*03developer*.md`

## qatester

Mission: Verify readiness and publish release verdict.

Files:
- `team/qa-reports/*qatester*.md`
