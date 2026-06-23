# Presentation Designer Harness

A harness where an agent team collaborates to produce presentations: planning, storyboards, slides, and speaker notes.

## Structure

```
.cursor/
├── agents/
│   ├── storyteller.md           — Story Design (message structuring, logical flow, audience analysis)
│   ├── info-architect.md        — Information Architecture (data visualization, chart selection, information hierarchy)
│   ├── visual-designer.md       — Visual Design (slide layout, color, typography, images)
│   ├── presentation-coach.md    — Presentation Coaching (speaker notes, timing, Q&A prep, rehearsal guide)
│   └── deck-reviewer.md         — Deck QA (story<->info<->visual<->presentation consistency verification)
├── skills/
│   ├── presentation-designer/
│   │   └── skill.md             — Orchestrator (team coordination, workflow, error handling)
│   ├── slide-layout-patterns/
│   │   └── skill.md             — visual-designer extension (20 layout patterns, grids, design tokens)
│   └── data-visualization-guide/
│       └── skill.md             — info-architect extension (chart selection matrix, LATCH, color accessibility)
└── CURSOR.md                    — This file
```

## Usage

Use Cursor chat with natural-language requests, invoke `/presentation-designer` manually, or attach `@.cursor/skills/presentation-designer/skill.md` as context before execution.
## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_story_structure.md` — Story structure/message map
- `02_info_design.md` — Information design/data visualization guide
- `03_slide_deck.md` — Slide deck (markdown-based)
- `04_speaker_notes.md` — Speaker notes/timing/Q&A
- `05_review_report.md` — Review report
