# Product Manager Harness

A harness where an agent team collaborates to generate the full PM workflow: Roadmap, PRD, User Stories, Sprint Plan, and Retrospective.

## Structure

```
.cursor/
├── agents/
│   ├── strategist.md          — Strategist (vision, roadmap, prioritization framework)
│   ├── prd-writer.md          — PRD Writer (product requirements document)
│   ├── story-writer.md        — Story Writer (AC, story map, points)
│   ├── sprint-planner.md      — Sprint Planner (planning, capacity, risk)
│   └── pm-reviewer.md         — PM Reviewer (consistency, feasibility review)
├── skills/
│   ├── product-manager/
│       └── skill.md           — Orchestrator (team coordination, workflow, error handling)
│   ├── rice-prioritizer/
│   │   └── skill.md           — RICE Prioritizer (scoring formula, ICE/MoSCoW supplements)
│   └── story-point-estimator/
│       └── skill.md           — Story Point Estimator (Fibonacci, velocity, decomposition criteria)
└── CURSOR.md                  — This file
```

## Usage

Use Cursor chat with natural-language requests, invoke `/product-manager` manually, or attach `@.cursor/skills/product-manager/skill.md` as context before execution.
## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_product_roadmap.md` — Product roadmap
- `02_prd.md` — Product requirements document
- `03_user_stories.md` — User story list
- `04_sprint_plan.md` — Sprint plan
- `05_review_report.md` — PM review report
