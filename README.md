# paid-origin-vizip

**Cursor Cloud Agent** 使用的 CIMA Paid Origin Skill 仓库。本地 Web 项目在 `.env` 中设置：

```env
CURSOR_CLOUD_REPO_URL=https://github.com/Simon8498/paid-origin-vizip.git
```

Cloud Agent 会 clone 本仓库，读取 `.cursor/skills/cima-analytics-planner/` 做问题规划；**查库仍在 VPN 本机**由 FastAPI `execution_engine` 执行。

## 目录结构

```
.cursor/skills/cima-analytics-planner/
  SKILL.md              # Cloud Agent 主指令（输出 JSON 计划）
  reference.md          # 口径、维度、analysis_type → 本地执行映射
  examples.md           # 标准问题 → JSON 示例
  plan-schema.json      # 计划 JSON 结构（可选校验）
docs/
  architecture.md       # Web → Cloud → 本地执行 六步架构
  local-executor-contract.md
scripts/
  validate_plan.py      # 本地校验 plan JSON
```

## 与本地 Web 项目的关系

本地 `app/cloud_planner.py` 会加载 Skill（优先 `.cursor/skills/...`，其次 `github-upload/.cursor/skills/...`）。  
更新 Skill 后 push 到 GitHub，下次 Cloud 规划会使用新版本。
