# Knowledge Base Builder Harness

An agent team harness for building organizational knowledge management systems.

## Structure

```
.cursor/
├── agents/
│   ├── knowledge-collector.md
│   ├── taxonomy-designer.md
│   ├── wiki-builder.md
│   ├── search-optimizer.md
│   └── maintenance-planner.md
├── skills/
│   ├── knowledge-base-builder/
│   │   └── skill.md              — Orchestrator
│   ├── information-architecture/
│   │   └── skill.md              — Information architecture design (4 IA systems, card sorting, tags)
│   └── content-lifecycle-manager/
│       └── skill.md              — Content lifecycle (quality scorecard, RACI, auditing)
└── CURSOR.md                     — This file
```

## Usage

Use Cursor chat with natural-language requests, invoke `/knowledge-base-builder` manually, or attach `@.cursor/skills/knowledge-base-builder/skill.md` as context before execution.
