# Research Assistant Harness

An agent team harness for academic research assistance.

## Structure

```
.cursor/
├── agents/
│   ├── literature-searcher.md
│   ├── note-taker.md
│   ├── critic-synthesizer.md
│   ├── reference-manager.md
│   └── research-coordinator.md
├── skills/
│   ├── research-assistant/
│   │   └── skill.md              — Orchestrator
│   ├── systematic-review-protocol/
│   │   └── skill.md              — Systematic review (PRISMA, PICO, Boolean search)
│   └── citation-formatter/
│       └── skill.md              — Citation format conversion (APA/MLA/Chicago, BibTeX)
└── CURSOR.md                     — This file
```

## Usage

Use Cursor chat with natural-language requests, invoke `/research-assistant` manually, or attach `@.cursor/skills/research-assistant/skill.md` as context before execution.
