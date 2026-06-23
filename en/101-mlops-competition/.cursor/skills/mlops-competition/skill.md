---
name: mlops-competition
description: "Competition-oriented MLOps harness for Kaggle/Dacon-style workflows: problem framing, feature engineering, model training/tuning, CV design, submission strategy, leaderboard interpretation, and reproducible operations."
---

# MLOps Competition — Full Competition Pipeline

## Execution Mode

**Agent Team** — 5 members coordinate via `Task` tool calls to subagents and cross-validate outputs.

## Cursor-native Orchestration Notes

- Delegate specialist work using `Task` tool calls to subagents.
- Run independent branches in parallel by issuing multiple `Task` calls together.
- Track progress and dependencies with `TodoWrite`, and keep deliverables in `_workspace/`.
- For external or live systems, prefer MCP tools/resources before manual web steps.

## Agent Roster

| Agent | File | Role | Type |
|-------|------|------|------|
| competition-strategist | `.cursor/agents/competition-strategist.md` | Problem framing, score strategy, timeline/risk | general-purpose |
| feature-engineer | `.cursor/agents/feature-engineer.md` | Preprocessing, feature generation, leakage prevention | general-purpose |
| training-optimizer | `.cursor/agents/training-optimizer.md` | Modeling, tuning, ensembling | general-purpose |
| validation-submission-analyst | `.cursor/agents/validation-submission-analyst.md` | CV design, submission QA, leaderboard analysis | general-purpose |
| mlops-reviewer | `.cursor/agents/mlops-reviewer.md` | Reproducibility/operability/final QA | general-purpose |

## Workflow

### Phase 1: Preparation (orchestrator)

1. Extract competition metadata, metric, constraints, and target.
2. Save normalized context to `_workspace/00_input.md`.
3. Select execution mode.

### Phase 2: Team execution

| Order | Task | Owner | Depends On | Output |
|-------|------|-------|------------|--------|
| 1 | Competition strategy | strategist | None | `_workspace/01_competition_plan.md` |
| 2a | Feature pipeline | feature | Task 1 | `_workspace/02_feature_pipeline.md` |
| 2b | Training/tuning plan | training | Task 1 | `_workspace/03_training_plan.md` |
| 3 | CV/submission strategy | validation | Tasks 2a, 2b | `_workspace/04_validation_submission.md` |
| 4 | MLOps review | reviewer | Tasks 1-3 | `_workspace/05_mlops_review.md` |

- Tasks 2a and 2b run in parallel.
- Reviewer requests rework on 🔴 must-fix issues (up to 2 rounds).

### Phase 3: Integration

1. Finalize submission generation/check flow under `submission/`.
2. Lock reproducibility checklist (seed/env/data/code versions).
3. Report final actionable submission plan.

## Scale-Based Modes

| Request Pattern | Mode | Agents |
|-----------------|------|--------|
| End-to-end competition run | Full pipeline | all 5 |
| CV/leakage check only | Validation mode | validation + reviewer |
| Feature work only | Feature mode | feature + reviewer |
| Submission optimization only | Submission mode | validation + strategist + reviewer |
| Final audit only | Review mode | reviewer |

## Error Handling

- **Leaderboard shake-up**: redesign CV and diversify ensemble portfolio.
- **Leakage suspicion**: immediately switch split policy (time/group/id-aware).
- **Non-reproducible runs**: recover environment lock and seed/version tracking first.
- **Submission failure**: auto-generate schema/format validation script.

## Agent Extension Skills

| Skill | Path | Target |
|-------|------|--------|
| leaderboard-strategy | `.cursor/skills/leaderboard-strategy/skill.md` | strategist, validation |
| cv-leakage-guard | `.cursor/skills/cv-leakage-guard/skill.md` | feature, validation |
| experiment-tracking-blueprint | `.cursor/skills/experiment-tracking-blueprint/skill.md` | training, reviewer |
