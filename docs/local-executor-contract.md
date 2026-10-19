# Local executor contract (FastAPI)

The cloud planner JSON is consumed by `app/execution_engine.py`:

## Structured path (prefer empty `steps`)

| analysis_type | Required filters | Notes |
|---------------|------------------|-------|
| yoy | fy_old, fy_new | `dimensions` + optional region5/famnon |
| why | fy_old, fy_new, region5 | |
| monthly | fy_old, fy_new, region5 | famnon optional, default Family |
| latest_week / wow | — | Ignores FY unless in adhoc steps |

## Steps path

Each step: `{ "tool": "<name>", "arguments": { ... } }`  
Tools implemented in `app/analyst_tools.py`.

## Response packaging

`app/orchestrator.py` saves artifacts under `tasks/` and returns:

- `reply` — markdown for chat
- `task_id` — for `GET /api/tasks/{task_id}`
- `quality` — from plan
- `phases.planner` / `phases.executor`
