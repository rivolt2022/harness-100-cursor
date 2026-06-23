# Podcast Studio Harness

A harness where an agent team collaborates to produce podcast content through the pipeline of planning, research, scripting, show notes, and distribution strategy.

## Structure

```
.cursor/
├── agents/
│   ├── researcher.md          — Research (deep topic investigation, fact-checking, reference compilation)
│   ├── scriptwriter.md        — Script writing (opening, segments, dialogue cues, closing)
│   ├── shownote-editor.md     — Show notes editing (timestamps, summaries, links, references)
│   ├── distribution-manager.md — Distribution management (platform-specific metadata, promotional copy)
│   └── production-reviewer.md — Cross-validation (research↔script↔show notes↔distribution consistency)
├── skills/
│   ├── podcast-studio/
│   │   └── skill.md           — Orchestrator (team coordination, workflow, error handling)
│   ├── interview-techniques/
│   │   └── skill.md           — scriptwriter extension (DEPTH question model, emotional arc)
│   ├── audio-storytelling/
│   │   └── skill.md           — scriptwriter+shownote-editor extension (narrative arcs, BPM pacing)
│   └── podcast-growth/
│       └── skill.md           — distribution-manager extension (platform optimization, HIKE copy)
└── CURSOR.md                  — This file
```

## Usage

Use Cursor chat with natural-language requests, invoke `/podcast-studio` manually, or attach `@.cursor/skills/podcast-studio/skill.md` as context before execution.
## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_research_brief.md` — Research brief
- `02_script.md` — Podcast script
- `03_shownotes.md` — Show notes
- `04_distribution_package.md` — Distribution package
- `05_review_report.md` — Review report
