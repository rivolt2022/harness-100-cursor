# MLOps Competition Harness

Agent-team harness for Kaggle/Dacon competitions: **trustworthy CV → reproducible pipeline → strategic submission**.

## Core Principles

1. **CV is ground truth** — target CV↔public LB correlation r ≥ 0.85
2. **Submit baseline early** — detect CV-LB gaps quickly
3. **Fit preprocessing inside folds** — block leakage
4. **Dual final submission** — CV champion + public peak
5. **Dacon** — Private Score reproduction package

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
│   ├── mlops-competition/skill.md       — orchestrator
│   ├── leaderboard-strategy/skill.md
│   ├── cv-leakage-guard/skill.md
│   ├── experiment-tracking-blueprint/skill.md
│   ├── ensemble-strategy/skill.md
│   └── platform-playbook/skill.md
└── CURSOR.md
```

## Usage

Natural language in Cursor chat, `/mlops-competition`, or `@.cursor/skills/mlops-competition/skill.md`.

**Example prompts**
- "Design strategy and CV for a Dacon tabular classification comp"
- "CV 0.9 but LB 0.78 — audit for leakage"
- "Build LightGBM+XGBoost ensemble and submission validator"
- "Package pipeline for Dacon code submission"

## Artifacts (`_workspace/`)

- `00_input.md` — competition, data, constraints
- `01_competition_plan.md` — strategy, submit calendar, risks
- `02_feature_pipeline.md` — EDA, fold-safe pipeline
- `03_training_plan.md` — models, tuning, ensemble
- `04_validation_submission.md` — CV-LB, submit validation
- `05_mlops_review.md` — final QA, Go/No-Go
- `pipeline_code/` — reproducible scripts
- `submission/` — CSV, validators
- `experiments/` — run log

## Skill Quick Reference

| Situation | Skill |
|-----------|-------|
| shake-up / submit slots | `leaderboard-strategy` |
| leakage / GroupKFold | `cv-leakage-guard` |
| MLflow / DVC | `experiment-tracking-blueprint` |
| ensemble | `ensemble-strategy` |
| Dacon code submit | `platform-playbook` |
