# Reference — PAID allocation & local executor mapping

## Metric

**PAID allocated ATTN** (本项目 Web 默认口径):

- Numerator: `SURVEY_ORIGINS` regional weekly PAID attendance (by FY/FW).
- Mix: VIZIP segment shares from `SURVEY_VIZIP_CUST_CHANNEL` / related VIZ tables.
- Logic: canonical script in repo root `sql.txt` (Origins total × segment mix).

Not the same as raw survey row sums without allocation.

## Core dimensions

| Dimension | Column / label | Values |
|-----------|----------------|--------|
| region5 | `REGION5_C` | Shanghai, Neighboring Provinces, Other China, Greater China, International |
| famnon | `FAMNON_C` | Family, Non-Family |
| group | `GROUP_C` | Life stage groups (e.g. Pre-School Family, Elementary School Family, …) |
| time | FY, FW, FM | Fiscal year / week / month |

## `analysis_type` → local backend behavior

| analysis_type | When to use | Local handler |
|---------------|-------------|-----------------|
| `yoy` | FY compare, tables by dimensions | `attendance_yoy` tool |
| `why` | Region attendance drop/rise narrative | `explain_region_attendance_change` |
| `monthly` | Which fiscal month drove change | `explain_monthly_yoy_drop` |
| `latest_week` | 最近一周 / 最近完整财周 | `explain_latest_week_performance` |
| `wow` | Week-over-week (if explicit) | Same as latest_week or adhoc steps |
| `adhoc` | Custom SQL/Python | `steps[]` via `run_sql` / `run_python` |

## Filter inference cheatsheet

| User phrase | filters / dimensions |
|-------------|----------------------|
| OC Family 生命周期 | region5=Other China, famnon=Family, dimensions=[group] |
| FY2025 vs FY2026 region famnon | fy_old=2025, fy_new=2026, dimensions=[region5,famnon] |
| 为什么 OC 掉 | analysis_type=why, region5=Other China |
| 哪个月 OC Family 掉最多 | analysis_type=monthly, region5=Other China, famnon=Family |
| 最近一周表现 | analysis_type=latest_week, steps=[] |
| 样本量 / respid | adhoc: run_tool survey_sample_counts or run_python |

## Key tables (CIMATEMP.dbo)

- `D_DATE` — calendar, FY, FM, FW, labels
- `SURVEY_ORIGINS` — regional weekly PAID attendance
- `SURVEY_VIZIP_CUST_CHANNEL` — VIZIP mix dimensions
- `SURVEY_VIZ_IP`, `SURVEY_VIZ_OL` — supplements

## quality.score guidance

| Score | Meaning |
|-------|---------|
| 0.9–1.0 | Clear FY, metric, dimensions; standard analysis_type |
| 0.6–0.8 | Missing year or region but reasonable defaults applied |
| &lt;0.6 | Ambiguous; note in `quality.notes` what was assumed |

## Glossary (short)

- **Attendance / 人天** — resort visit-days; here PAID allocated slice.
- **Paid / PAID** — paid ticket attendance (not AP/Comp).
- **OC** — Other China origin region in region5.

Full glossary: repo `_kb_extract.txt` when available.
