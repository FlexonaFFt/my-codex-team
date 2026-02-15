#!/usr/bin/env python3
"""Initialize team/ communication workspace in the current repository from skill assets."""

from __future__ import annotations

from pathlib import Path
import shutil


def copy_if_missing(src: Path, dst: Path) -> None:
    if dst.exists():
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def main() -> int:
    repo_root = Path.cwd()
    skill_root = Path(__file__).resolve().parent.parent
    assets_root = skill_root / "assets" / "team"

    if not assets_root.exists():
        raise SystemExit(f"Missing skill assets directory: {assets_root}")

    team_root = repo_root / "team"

    for rel in ["handoffs", "role-outputs", "qa-reports", "final", "templates"]:
        (team_root / rel).mkdir(parents=True, exist_ok=True)

    for src in assets_root.rglob("*"):
        if src.is_file():
            rel = src.relative_to(assets_root)
            copy_if_missing(src, team_root / rel)

    print(f"Initialized team workspace at: {team_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
