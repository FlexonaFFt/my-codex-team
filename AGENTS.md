# TeamLead Simple Contract

## Goal

Run one autonomous workflow where you only talk to `TeamLead`.

## Folders

- `tram/` is communication-only.
- All product code must be created/edited in the project root workspace outside `tram/`.

## Roles

- `TeamLead` (entry point)
- `ML-Engineer`
- `Backend-dev`
- `Front-dev`
- `QA`

If backend/frontend boundaries are unclear, `Backend-dev` and `Front-dev` act as general developers.

## TeamLead Algorithm

1. Read user task.
2. Break task into sub-tasks.
3. Assign role owners.
4. Execute in dependency order.
5. Integrate code changes in main project files.
6. Run QA gate.
7. Return final result.

## Communication Files

- `tram/board.md` (single source of truth)
- `tram/handoffs/` (role-to-role messages)
- `tram/role-outputs/` (what each role completed)
- `tram/qa-reports/` (QA verdict)
- `tram/final/` (TeamLead final summary)

## Done Criteria

Task is done only if:

- real project files were changed outside `tram/`
- `tram/board.md` reflects final status
- at least one role output exists in `tram/role-outputs/`
- QA verdict exists in `tram/qa-reports/`
- TeamLead summary exists in `tram/final/`
