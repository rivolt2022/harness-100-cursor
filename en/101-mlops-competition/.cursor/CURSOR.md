# MLOps Competition Harness

A harness for competition-grade MLOps workflows (including Kaggle/Dacon): problem framing, features/modeling, validation, submissions, and reproducible operations.

## Structure

```
.cursor/
├── agents/
│   ├── competition-strategist.md
│   ├── feature-engineer.md
│   ├── training-optimizer.md
│   ├── validation-submission-analyst.md
│   └── mlops-reviewer.md
├── skills/
│   ├── mlops-competition/
│   │   └── skill.md
│   ├── leaderboard-strategy/
│   │   └── skill.md
│   ├── cv-leakage-guard/
│   │   └── skill.md
│   └── experiment-tracking-blueprint/
│       └── skill.md
└── CURSOR.md
```

## Usage

Use Cursor chat with natural-language requests, invoke `/mlops-competition` manually, or attach `@.cursor/skills/mlops-competition/skill.md` as context before execution.

## Deliverables

All outputs are saved under `_workspace/`:
- `00_input.md`
- `01_competition_plan.md`
- `02_feature_pipeline.md`
- `03_training_plan.md`
- `04_validation_submission.md`
- `05_mlops_review.md`
- `submission/`
