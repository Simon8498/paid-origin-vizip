# Architecture — six steps

1. **User** submits question on web → **FastAPI** `POST /api/chat`
2. **Backend** calls **Cursor Cloud Agent** (`CURSOR_API_KEY`, `CURSOR_CLOUD_REPO_URL`)
3. **Cloud Agent** loads skill `cima-analytics-planner`, outputs **JSON execution plan** (+ `quality`)
4. **Agent result** returns to backend (plan text / parsed JSON)
5. **Backend** runs **local** `execution_engine` (`run_sql`, `run_python`, structured YoY/why/monthly/latest_week)
6. **Backend** writes **`tasks/{task_id}/`** (`meta.json`, `plan.json`, `quality.json`, `execution.json`, `reply.md`)

Database credentials stay on the VPN machine only (`cimatemp database connection.txt`).
