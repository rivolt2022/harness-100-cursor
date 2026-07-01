# Debate Simulator Harness

An agent team harness for debate simulation.

## Structure

```
.cursor/
├── agents/
│   ├── topic-analyst.md         — Topic Analyst (issues, arguments, data)
│   ├── pro-debater.md           — Pro-side Debater (argumentation, rebuttal, evidence)
│   ├── con-debater.md           — Con-side Debater (argumentation, rebuttal, evidence)
│   ├── judge.md                 — Judge (evaluation, verdict, feedback)
│   └── rapporteur.md            — Rapporteur (summary, analysis, learning points)
├── skills/
│   ├── debate-simulator/
│       └── skill.md             — Orchestrator (team coordination, workflow, error handling)
│   ├── logical-fallacy-detector/
│   │   └── skill.md             — Logical Fallacy Detector (formal/informal fallacies)
│   └── argumentation-framework/
│       └── skill.md             — Argumentation Framework (Toulmin, logical structure)
└── CURSOR.md                    — This file
```

## Usage

In Cursor chat, request with `@debate-simulator`.

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_topic_analysis.md` — Topic analysis
- `02_pro_arguments.md` — Pro-side arguments
- `03_con_arguments.md` — Con-side arguments
- `04_verdict.md` — Verdict
- `05_debate_record.md` — Debate record
- `06_review_report.md` — Review report
