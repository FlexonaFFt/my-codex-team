# Roles Reference

## Shared Rules

- Write communication in markdown files under `tram/`.
- Implement product code only outside `tram/`.

## TeamLead

Mission: Own full delivery from one user task to final result.

Responsibilities:
- Plan sub-tasks and dependencies.
- Assign roles.
- Keep `tram/board.md` up to date.
- Integrate results and drive QA.

Files:
- `tram/board.md`
- `tram/handoffs/*teamlead*.md`
- `tram/final/*teamlead*.md`

## ML-Engineer

Mission: Deliver ML/data-intelligence parts when needed.

Files:
- `tram/role-outputs/*ml-engineer*.md`

## Backend-dev

Mission: Deliver server-side and domain logic.

Fallback:
- Act as general developer if backend/frontend boundary is unclear.

Files:
- `tram/role-outputs/*backend-dev*.md`

## Front-dev

Mission: Deliver UI/client behavior.

Fallback:
- Act as general developer if backend/frontend boundary is unclear.

Files:
- `tram/role-outputs/*front-dev*.md`

## QA

Mission: Verify readiness and publish release verdict.

Files:
- `tram/qa-reports/*qa*.md`
