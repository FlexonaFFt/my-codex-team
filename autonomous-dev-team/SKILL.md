---
name: autonomous-dev-team
description: TeamLead-based autonomous development workflow for software projects. Use when the user provides one high-level engineering task and expects TeamLead to decompose work, assign implementation to 01developer/02developer/03developer, route verification to qatester, and deliver completion artifacts while keeping production code outside team/.
---

# Autonomous Dev Team

Use one entry point: `TeamLead`.

## Bootstrap

- If `team/` does not exist, run `scripts/bootstrap_team.py` from project root.
- Keep `team/` for communication artifacts only.
- Implement production code outside `team/`.

## Execution Workflow

1. Convert user request into concrete acceptance criteria.
2. Write plan and task graph in `team/board.md`.
3. Assign tasks to `01developer`, `02developer`, `03developer`.
4. Execute tasks in dependency order and change real project files.
5. Record implementation outputs in `team/role-outputs/`.
6. Route final validation to `qatester` and record verdict in `team/qa-reports/`.
7. Write final TeamLead summary in `team/final/`.

## Completion Gate

Mark task complete only if all conditions are true:

- Project files outside `team/` were changed.
- `team/board.md` reflects final status.
- At least one file exists in `team/role-outputs/`.
- At least one QA verdict exists in `team/qa-reports/`.
- At least one TeamLead summary exists in `team/final/`.

## References

- Read role details in `references/roles.md` before assigning owners.
