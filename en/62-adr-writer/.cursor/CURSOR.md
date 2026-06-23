# ADR Writer Harness

An agent team harness for creating Architecture Decision Records (ADRs).

## Structure

```
.cursor/
├── agents/
│   ├── context-analyst.md
│   ├── alternative-researcher.md
│   ├── tradeoff-evaluator.md
│   ├── adr-author.md
│   └── impact-tracker.md
├── skills/
│   ├── adr-writer/
│   │   └── skill.md              — Orchestrator
│   ├── quality-attribute-analyzer/
│   │   └── skill.md              — Quality attribute analysis (CAP theorem, weighted evaluation, ATAM)
│   └── madr-template-engine/
│       └── skill.md              — MADR format (ADR status management, numbering system, dependency graph)
└── CURSOR.md                     — This file
```

## Usage

Use Cursor chat with natural-language requests, invoke `/adr-writer` manually, or attach `@.cursor/skills/adr-writer/skill.md` as context before execution.
