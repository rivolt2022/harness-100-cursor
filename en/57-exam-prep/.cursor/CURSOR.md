# Exam Prep Harness

An agent team harness for exam preparation: exam trend analysis, weakness diagnosis, customized study plans, mock exams, and error analysis.

## Structure

```
.cursor/
├── agents/
│   ├── trend-analyst.md         — Trend Analyst (frequency, patterns, predictions)
│   ├── diagnostician.md         — Diagnostician (by area, by type analysis)
│   ├── learning-designer.md     — Learning Designer (customized curriculum, strategy)
│   ├── examiner.md              — Examiner (exam-style questions, difficulty calibration)
│   └── error-analyst.md         — Error Analyst (patterns, root causes, remedies)
├── skills/
│   ├── exam-prep/
│       └── skill.md             — Orchestrator (team coordination, workflow, error handling)
│   ├── error-pattern-analyzer/
│   │   └── skill.md             — Error Pattern Analyzer (by type, by cause)
│   └── bloom-taxonomy-engine/
│       └── skill.md             — Bloom Taxonomy Engine (questions by cognitive level)
└── CURSOR.md                    — This file
```

## Usage

In Cursor chat, request with `@exam-prep`.

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_trend_analysis.md` — Exam trend analysis
- `02_diagnosis.md` — Diagnostic results
- `03_study_plan.md` — Study plan
- `04_mock_exam.md` — Mock exam
- `05_error_analysis.md` — Error analysis report
- `06_review_report.md` — Review report
