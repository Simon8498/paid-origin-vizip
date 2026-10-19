#!/usr/bin/env python3
"""Validate a planner JSON file against plan-schema.json (stdlib only)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1] / ".cursor" / "skills" / "cima-analytics-planner"
SCHEMA_PATH = SKILL_DIR / "plan-schema.json"

REQUIRED_TOP = {"summary", "quality", "metric", "filters", "dimensions", "analysis_type", "steps", "narrative_focus"}
VALID_ANALYSIS = {"yoy", "why", "monthly", "latest_week", "wow", "adhoc"}
VALID_TOOLS = {"run_sql", "run_python", "get_reference", "test_db_connection", "get_schema"}


def validate(plan: dict) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED_TOP - set(plan.keys())
    if missing:
        errors.append(f"missing keys: {sorted(missing)}")

    q = plan.get("quality")
    if not isinstance(q, dict):
        errors.append("quality must be object")
    else:
        score = q.get("score")
        if not isinstance(score, (int, float)) or not (0 <= float(score) <= 1):
            errors.append("quality.score must be 0..1")
        if not isinstance(q.get("notes"), str):
            errors.append("quality.notes must be string")

    at = plan.get("analysis_type")
    if at not in VALID_ANALYSIS:
        errors.append(f"invalid analysis_type: {at}")

    steps = plan.get("steps")
    if not isinstance(steps, list):
        errors.append("steps must be array")
    else:
        for i, step in enumerate(steps):
            tool = (step or {}).get("tool")
            if tool not in VALID_TOOLS:
                errors.append(f"step {i}: invalid tool {tool}")

    return errors


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: validate_plan.py plan.json", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    plan = json.loads(path.read_text(encoding="utf-8"))
    errors = validate(plan)
    if errors:
        for e in errors:
            print("ERROR:", e)
        return 1
    print("OK:", path)
    if SCHEMA_PATH.is_file():
        print("(schema file present at", SCHEMA_PATH, ")")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
