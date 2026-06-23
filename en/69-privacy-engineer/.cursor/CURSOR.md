# Privacy Engineer Harness

A privacy engineering agent team harness.

## Structure

```
.cursor/
├── agents/
│   ├── privacy-law-analyst.md
│   ├── pia-assessor.md
│   ├── process-architect.md
│   └── consent-designer.md
├── skills/
│   ├── privacy-engineer/
│   │   └── skill.md              — Orchestrator
│   ├── gdpr-pipa-cross-reference/
│   │   └── skill.md              — GDPR-PIPA cross-reference (article mapping, requirements comparison, implementation guide)
│   └── data-flow-mapper/
│       └── skill.md              — Data flow mapper (data inventory, transfer mapping, legal basis matrix)
└── CURSOR.md                     — This file
```

## Usage

Use Cursor chat with natural-language requests, invoke `/privacy-engineer` manually, or attach `@.cursor/skills/privacy-engineer/skill.md` as context before execution.
