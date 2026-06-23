# Investor Report Harness

Investor report generation: an agent team collaborates to produce financial performance analysis, KPI dashboard, market trends, strategy updates, and risk disclosures.

## Structure

```
.cursor/
├── agents/
│   ├── financial-analyst.md     — Financial analysis (P&L, cash flow, key financial metrics)
│   ├── kpi-designer.md          — KPI dashboard (key metrics, trends, benchmarks)
│   ├── market-analyst.md        — Market trends (industry trends, competition, regulation)
│   ├── strategy-updater.md      — Strategy update (progress, roadmap, risk disclosure)
│   └── ir-reviewer.md           — Cross-validation (financial ↔ KPI ↔ market ↔ strategy consistency)
├── skills/
│   ├── investor-report/
│   │   └── skill.md             — Orchestrator (team coordination, workflow, error handling)
│   ├── financial-ratio-analyzer/
│   │   └── skill.md             — Financial ratio deep analysis (DuPont, SaaS metrics, 5 ratio categories)
│   ├── kpi-benchmark-engine/
│   │   └── skill.md             — KPI benchmarking (industry benchmarks, SMART-R, pyramid)
│   └── ir-narrative-builder/
│       └── skill.md             — IR narrative construction (Equity Story, investor-specific tone, EBITDA Bridge)
└── CURSOR.md                    — This file
```

## Usage

Use Cursor chat with natural-language requests, invoke `/investor-report` manually, or attach `@.cursor/skills/investor-report/skill.md` as context before execution.
## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_financial_analysis.md` — Financial performance analysis report
- `02_kpi_dashboard.md` — KPI dashboard
- `03_market_trends.md` — Market trends report
- `04_strategy_update.md` — Strategy update and risk disclosure
- `05_review_report.md` — Review report
- `06_investor_report_final.md` — Final integrated report
