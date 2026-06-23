# Contract Analyzer Harness

A contract analysis agent team harness.

## Structure

```
.cursor/
├── agents/
│   ├── clause-analyst.md
│   ├── risk-assessor.md
│   ├── comparison-reviewer.md
│   ├── clause-drafter.md
│   └── contract-coordinator.md
├── skills/
│   ├── contract-analyzer/
│   │   └── skill.md              — Orchestrator
│   ├── clause-risk-database/
│   │   └── skill.md              — Clause risk DB (risk levels, standard clauses, amendment examples)
│   └── negotiation-playbook/
│       └── skill.md              — Negotiation playbook (BATNA, concession strategies, clause alternatives)
└── CURSOR.md                     — This file
```

## Usage

Use Cursor chat with natural-language requests, invoke `/contract-analyzer` manually, or attach `@.cursor/skills/contract-analyzer/skill.md` as context before execution.
