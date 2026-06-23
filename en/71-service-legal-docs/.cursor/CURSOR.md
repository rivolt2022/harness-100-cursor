# Service Legal Docs Harness

A service terms and legal document drafting agent team harness.

## Structure

```
.cursor/
├── agents/
│   ├── tos-specialist.md
│   ├── privacy-specialist.md
│   ├── consumer-analyst.md
│   └── consistency-reviewer.md
├── skills/
│   ├── service-legal-docs/
│   │   └── skill.md              — Orchestrator
│   ├── unfair-terms-detector/
│   │   └── skill.md              — Unfair terms detector (unfairness criteria, regulatory examples, amendment suggestions)
│   └── cross-document-linker/
│       └── skill.md              — Cross-document linker (term consistency, cross-reference mapping, version management)
└── CURSOR.md                     — This file
```

## Usage

Use Cursor chat with natural-language requests, invoke `/service-legal-docs` manually, or attach `@.cursor/skills/service-legal-docs/skill.md` as context before execution.
