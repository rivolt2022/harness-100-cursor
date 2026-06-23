# YouTube Production Harness

A harness where an agent team collaborates to produce YouTube video content through the pipeline of strategy, script, thumbnail, and SEO.

## Structure

```
.cursor/
├── agents/
│   ├── content-strategist.md  — Content strategy (topic analysis, competitive benchmarking, concept design)
│   ├── scriptwriter.md        — Script writing (hook, segments, CTA, visual cues)
│   ├── thumbnail-designer.md  — Thumbnail design + Gemini image generation
│   ├── seo-optimizer.md       — SEO package (title/description/tags/chapters/subtitles)
│   └── production-reviewer.md — Cross-validation (strategy↔script↔thumbnail↔SEO consistency)
├── skills/
│   └── youtube-production/
│       └── skill.md           — Orchestrator (team coordination, workflow, error handling)
└── CURSOR.md                  — This file
```

## Usage

Use Cursor chat with natural-language requests, invoke `/youtube-production` manually, or attach `@.cursor/skills/youtube-production/skill.md` as context before execution.
## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_strategist_brief.md` — Strategy brief
- `02_scriptwriter_script.md` — Video script
- `03_thumbnail_concept.md` — Thumbnail concept
- `04_seo_package.md` — SEO package
- `05_review_report.md` — Review report
- `subtitle.srt` — Subtitle file
