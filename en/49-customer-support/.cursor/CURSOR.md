# Customer Support Harness

Build a customer support system: an agent team collaborates to produce FAQ, response manuals, escalation policies, and analytics.

## Structure

```
.cursor/
├── agents/
│   ├── faq-builder.md           — FAQ construction (question collection/classification, answer writing, search optimization)
│   ├── response-specialist.md   — Response manual (scenario-based scripts, tone & manner)
│   ├── escalation-manager.md    — Escalation (level design, routing, SLA)
│   ├── cs-analyst.md            — CS analytics (metrics, trends, improvement proposals)
│   └── cs-reviewer.md           — Cross-validation (FAQ ↔ manual ↔ escalation ↔ analytics consistency)
├── skills/
│   ├── customer-support/
│       └── skill.md             — Orchestrator (team coordination, workflow, error handling)
│   ├── csat-analyzer/
│   │   └── skill.md             — CSAT analysis (NPS/CES, VOC, CS dashboard)
│   └── escalation-flowchart/
│       └── skill.md             — Escalation design (L1/L2/L3, SLA, crisis response)
└── CURSOR.md                    — This file
```

## Usage

Use Cursor chat with natural-language requests, invoke `/customer-support` manually, or attach `@.cursor/skills/customer-support/skill.md` as context before execution.
## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_faq.md` — FAQ document
- `02_response_manual.md` — Response manual
- `03_escalation_policy.md` — Escalation policy
- `04_cs_analytics.md` — CS analytics framework
- `05_review_report.md` — Review report
