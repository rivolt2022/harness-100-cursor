# Content Repurposer Harness

A harness where an agent team transforms a single source piece of content into multiple formats: blog posts, social media, newsletters, presentations, and scripts.

## Structure

```
.cursor/
├── agents/
│   ├── source-analyst.md        — Source Analyst (structure analysis, key extraction, conversion strategy)
│   ├── blog-writer.md           — Blog Writer (SEO-optimized blog posts)
│   ├── sns-copywriter.md        — Social Media Copywriter (platform-specific posts)
│   ├── presentation-builder.md  — Presentation Builder (slide composition)
│   └── quality-reviewer.md      — Quality Reviewer (cross-validation, message consistency)
├── skills/
│   ├── content-repurposer/
│   │   └── skill.md             — Orchestrator (team coordination, workflow, error handling)
│   ├── platform-adaptation/
│   │   └── skill.md             — sns-copywriter+blog-writer extension (platform DNA, conversion matrix)
│   └── content-atomization/
│       └── skill.md             — source-analyst+presentation-builder extension (MINE analysis, atom classification)
└── CURSOR.md                    — This file
```

## Usage

In Cursor chat, request with `@content-repurposer`.

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_source_analysis.md` — Source analysis report
- `02_blog_post.md` — Blog post
- `03_sns_package.md` — Social media post package
- `04_presentation.md` — Presentation slides
- `05_review_report.md` — Review report
