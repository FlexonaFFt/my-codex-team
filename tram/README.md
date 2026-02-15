# tram Workspace

`tram/` is the communication channel for agent coordination.

## Use `tram/` for

- planning (`tram/board.md`)
- handoffs (`tram/handoffs/`)
- role reports (`tram/role-outputs/`)
- QA verdicts (`tram/qa-reports/`)
- final summary (`tram/final/`)

## Do not use `tram/` for

- production source code
- project runtime files

All implementation code must live in normal project folders outside `tram/`.
