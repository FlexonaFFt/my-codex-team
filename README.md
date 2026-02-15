# Autonomous Dev Team Skill

This repository contains a Codex skill called `autonomous-dev-team` for running autonomous software delivery through a single entry point: TeamLead. You provide one high-level task, and TeamLead decomposes it, assigns execution to `01developer`, `02developer`, and `03developer`, routes verification to `qatester`, and drives the workflow to completion.

The core principle is separation of concerns between communication and implementation. The `team/` directory is used only for coordination artifacts (board, handoffs, role outputs, QA reports, final summary), while all real product code is created or modified in the project’s normal source directories outside `team/`.

# Installation

To install the skill, copy `/Users/flexonafft/my-codex-team/autonomous-dev-team` into `~/.codex/skills/`, restart Codex, and invoke it with `Use $autonomous-dev-team.` in any project.
