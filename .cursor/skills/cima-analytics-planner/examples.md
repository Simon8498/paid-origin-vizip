# Plan examples (output JSON only)

## 1. FY YoY · region5 × famnon

User: `FY2025 和 FY2026 按来源和家庭类型对比`

```json
{
  "summary": "FY2026 vs FY2025 按 region5、famnon 对比 PAID 分配 ATTN",
  "quality": { "score": 0.95, "notes": "标准年度对比" },
  "metric": "paid_allocated_attn",
  "filters": { "fy_old": 2025, "fy_new": 2026 },
  "dimensions": ["region5", "famnon"],
  "analysis_type": "yoy",
  "steps": [],
  "narrative_focus": ["总盘与 OC/Intl 贡献", "Family vs Non-Family 结构"]
}
```

## 2. Why · OC

User: `为什么 FY2026 OC 的 attendance 会掉？`

```json
{
  "summary": "FY2026 vs FY2025 Other China 入园变化原因拆解",
  "quality": { "score": 0.92, "notes": "区域诊断，默认全 famnon" },
  "metric": "paid_allocated_attn",
  "filters": { "fy_old": 2025, "fy_new": 2026, "region5": "Other China" },
  "dimensions": ["famnon", "group"],
  "analysis_type": "why",
  "steps": [],
  "narrative_focus": ["Family 是否拖累", "life stage 贡献"]
}
```

## 3. Monthly · OC all famnon (FY26 vs FY25 worst FM)

User: `帮我看一下OC在FY26哪个月相比FY25掉的最厉害`

```json
{
  "summary": "Other China FY2026 vs FY2025 财月 PAID ATTN 最大跌幅",
  "quality": { "score": 0.9, "notes": "未指定 famnon，OC 全量" },
  "metric": "paid_allocated_attn",
  "filters": { "fy_old": 2025, "fy_new": 2026, "region5": "Other China" },
  "dimensions": ["fm"],
  "analysis_type": "monthly",
  "output": {
    "monthly_primary_sort": "delta_asc",
    "monthly_show_fm_calendar": true
  },
  "steps": [],
  "narrative_focus": ["Rank#1 财月", "绝对量 vs 百分比最大跌幅"]
}
```

## 4. Monthly · OC Family

User: `OC Family 哪个月掉得最多？`

```json
{
  "summary": "Other China Family 财月同比找最大跌幅",
  "quality": { "score": 0.9, "notes": "" },
  "metric": "paid_allocated_attn",
  "filters": {
    "fy_old": 2025,
    "fy_new": 2026,
    "region5": "Other China",
    "famnon": "Family"
  },
  "dimensions": ["fm"],
  "analysis_type": "monthly",
  "steps": [],
  "narrative_focus": ["绝对量与百分比跌幅最大的 FM"]
}
```

## 5. YTD · region5 × famnon · subtotals

User: `按region5 famnon拆分FY27 YTD attendance，需要小计和总计`

```json
{
  "summary": "FY2027 YTD 按 region5、famnon 汇总 PAID 分配 ATTN，含区域小计与总计",
  "quality": { "score": 0.92, "notes": "" },
  "metric": "paid_allocated_attn",
  "filters": { "fy": 2027 },
  "dimensions": ["region5", "famnon"],
  "analysis_type": "ytd",
  "steps": [],
  "narrative_focus": ["YTD 截止财周", "region 小计", "Grand Total"]
}
```

## 6. Latest week

User: `看一下最近一周的表现`

```json
{
  "summary": "最近完整财周 PAID 总量、环比与区域结构",
  "quality": { "score": 0.88, "notes": "未指定 FY/FW，由本地取最新有效财周" },
  "metric": "paid_allocated_attn",
  "filters": {},
  "dimensions": ["region5", "famnon"],
  "analysis_type": "latest_week",
  "steps": [],
  "narrative_focus": ["是否财周未结束导致最新周无数", "OC Family life stage 若需另问"]
}
```

## 6. OC Family · group YoY

User: `FY2026 OC Family 各 life stage 同比`

```json
{
  "summary": "FY2026 vs FY2025 Other China Family 按 GROUP_C 同比",
  "quality": { "score": 0.93, "notes": "" },
  "metric": "paid_allocated_attn",
  "filters": {
    "fy_old": 2025,
    "fy_new": 2026,
    "region5": "Other China",
    "famnon": "Family"
  },
  "dimensions": ["group"],
  "analysis_type": "yoy",
  "steps": [],
  "narrative_focus": ["Pre-School / Elementary 等驱动"]
}
```

## 7. Adhoc · sample counts

User: `FY2025 FY2026 OC Family 各 group 样本量`

```json
{
  "summary": "OC Family 调查 distinct respid 样本（未加权）",
  "quality": { "score": 0.85, "notes": "样本非 ATTN 分配量" },
  "metric": "survey_sample",
  "filters": { "fy_old": 2025, "fy_new": 2026, "region5": "Other China", "famnon": "Family" },
  "dimensions": ["group"],
  "analysis_type": "adhoc",
  "steps": [
    {
      "tool": "run_python",
      "arguments": {
        "code": "from app.tools import run_tool\nprint(run_tool('survey_sample_counts', {'fy_list': [2025, 2026], 'region5': 'Other China', 'famnon': 'Family', 'group_by': 'group'}))"
      }
    }
  ],
  "narrative_focus": ["样本变化是否解释 ATTN 波动"]
}
```

Note: In cloud-only skill repo without `app/`, prefer `get_reference` + `run_sql` adhoc or set `analysis_type` `yoy` if executor supports sample tool by keyword fallback.
