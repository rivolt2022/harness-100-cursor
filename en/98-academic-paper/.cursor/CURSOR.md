# Academic Paper Harness

An academic paper writing harness. An agent team collaborates to produce research design, experiment management, statistical analysis, paper writing, and submission preparation.

## Structure

```
.cursor/
├── agents/
│   ├── research-designer.md      — Research design (hypothesis, methodology, variables)
│   ├── experiment-manager.md     — Experiment management (protocol, data collection, quality control)
│   ├── statistical-analyst.md    — Statistical analysis (descriptive/inferential statistics, visualization)
│   ├── paper-writer.md           — Paper writing (IMRaD structure, academic writing)
│   └── submission-preparer.md    — Submission preparation (journal selection, formatting, cover letter)
├── skills/
│   ├── academic-paper/
│   │   └── skill.md              — Orchestrator (team coordination, workflow, error handling)
│   ├── research-methodology/
│   │   └── skill.md              — Research methodology (research-designer extension)
│   └── citation-standards/
│       └── skill.md              — Citation standards (paper-writer extension)
└── CURSOR.md                     — This file
```

## Usage

Use Cursor chat with natural-language requests, invoke `/academic-paper` manually, or attach `@.cursor/skills/academic-paper/skill.md` as context before execution.
## Outputs

All outputs are saved to the `_workspace/` directory:
- `00_input.md` — Research topic and conditions
- `01_research_design.md` — Research design document
- `02_experiment_protocol.md` — Experiment protocol
- `03_statistical_analysis.md` — Statistical analysis results
- `04_paper_draft.md` — Paper draft
- `05_submission_package.md` — Submission preparation package
