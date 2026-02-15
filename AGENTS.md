# TeamLead Simple Contract

## Goal

Run one autonomous workflow where you only talk to `TeamLead`.

## Folders

- `team/` is communication-only.
- All product code must be created/edited in the project root workspace outside `team/`.

## Team

- `TeamLead` (entry point)
- `01developer`
- `02developer`
- `03developer`
- `qatester`

TeamLead decides task ownership dynamically. There are no fixed specialization boundaries for developers.

## TeamLead Algorithm

1. Read user task.
2. Break task into sub-tasks.
3. Assign owners between `01developer`, `02developer`, `03developer`.
4. Execute in dependency order.
5. Integrate code changes in main project files.
6. Run QA gate through `qatester`.
7. Return final result.

## Communication Files

- `team/board.md` (single source of truth)
- `team/handoffs/` (role-to-role messages)
- `team/role-outputs/` (what each developer completed)
- `team/qa-reports/` (`qatester` verdict)
- `team/final/` (TeamLead final summary)

## Done Criteria

Task is done only if:

- real project files were changed outside `team/`
- `team/board.md` reflects final status
- at least one developer output exists in `team/role-outputs/`
- `qatester` verdict exists in `team/qa-reports/`
- TeamLead summary exists in `team/final/`
