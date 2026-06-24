---
name: mlops-competition
description: "MLOps harness for data competitions including Kaggle/Dacon. Covers problem framing, feature engineering, training/tuning, CV design, submission strategy, leaderboard interpretation, and reproducible ops via an agent team. Use for requests like 'Kaggle competition strategy', 'improve Dacon submission score', 'CV leakage audit', 'ensemble design', or 'competition MLOps pipeline'."
---

# MLOps Competition — Full Competition MLOps Pipeline

Operate Kaggle/Dacon-style competitions with **trustworthy offline CV** and a **reproducible submission pipeline**.

## Execution Mode

**Agent team** — 5 agents collaborate via `Task` subagents and cross-validate deliverables.

## Cursor-Native Orchestration Notes

- Delegate specialist work with the `Task` tool (subagents).
- Run independent branches (features vs training) in parallel via multiple `Task` calls.
- Track progress and dependencies with `TodoWrite`; store artifacts under `_workspace/`.
- Confirm competition rules, metrics, and LB via web search or MCP (no guessing).
- For Kaggle API/data download, verify user credentials and environment first.

## Agent Roster

| Agent | File | Role | Type |
|-------|------|------|------|
| competition-strategist | `.cursor/agents/competition-strategist.md` | Framing, scoring strategy, schedule/risk, submission slots | general-purpose |
| feature-engineer | `.cursor/agents/feature-engineer.md` | Preprocessing, features, fold-safe fit | general-purpose |
| training-optimizer | `.cursor/agents/training-optimizer.md` | Baseline→tuning→ensemble, cost optimization | general-purpose |
| validation-submission-analyst | `.cursor/agents/validation-submission-analyst.md` | CV design, CV-LB alignment, submission validation | general-purpose |
| mlops-reviewer | `.cursor/agents/mlops-reviewer.md` | Reproducibility, ops, rules, final QA | general-purpose |

## Workflow

### Phase 0: Competition Principles (all phases)

1. **Submit baseline early** — detect CV vs public LB gaps quickly.
2. **CV is ground truth** — if CV↔public LB correlation is weak (target r ≥ 0.85), redesign CV before model work.
3. **Fit preprocessing inside folds only** (scaler, imputer, target encoding).
4. **Dual final submission**: (A) maximize public LB, (B) CV-trusted model.
5. **Design for Private Score reproduction** from day one (Dacon 2nd-round audits).

### Phase 1: Prep (orchestrator)

1. Extract from user input:
   - **Platform**: Kaggle / Dacon / other
   - **Competition**: metric, submission format, daily limit, final selection count
   - **Data**: tabular/image/text/time-series; IID/group/temporal structure
   - **Goal**: top tier / medal / baseline / stable submit
   - **Constraints**: GPU/time/team size/external data & pretrained model policy
   - **Existing assets** (optional): notebooks, LB scores, experiment logs
2. Create `_workspace/`.
3. Save `_workspace/00_input.md`.
4. Skip phases when artifacts already exist.
5. Choose **execution mode** from request scope.

### Phase 2: Team Execution

| Step | Work | Owner | Depends | Output |
|------|------|-------|---------|--------|
| 1 | Competition strategy | strategist | — | `_workspace/01_competition_plan.md` |
| 2a | Feature/preprocess design | feature | 1 | `_workspace/02_feature_pipeline.md` |
| 2b | Model/tuning design | training | 1 | `_workspace/03_training_plan.md` |
| 3 | CV/submission strategy | validation | 2a, 2b | `_workspace/04_validation_submission.md` |
| 4 | MLOps review | reviewer | 1–3 | `_workspace/05_mlops_review.md` |

**Handoffs:**
- strategist → feature/training: metric, submission limits, schedule, risks
- feature → validation: split policy, leakage checklist, pipeline snippets
- training → validation: model candidates, CV scores, ensemble options
- validation → strategist: LB gap, submission priority; → reviewer: validation results
- reviewer cross-checks all artifacts; 🔴 fixes via `Task` rework (max 2 rounds)

- Run 2a/2b **in parallel**.

### Phase 3: Integration & Submit Prep

1. Organize `submission/` scripts, validators, README.
2. Map experiments (MLflow/DVC or spreadsheet) 1:1 to submission files.
3. Report CV-LB correlation log, 2–3 final candidates, Go/No-Go.

## CV-LB Alignment Protocol

| Step | Action | Pass criteria |
|------|--------|---------------|
| 1 | Early submit 1–3 simple baselines | Format & metric direction OK |
| 2 | Log CV vs public LB in a table | Track correlation r |
| 3 | r < 0.85 or sign mismatch | adversarial validation, redesign split |
| 4 | fold std/mean < 20% | stable CV |
| 5 | shake-up defense | CV-trusted model in final candidates |

**Split guide:**

| Data signal | Recommended CV | Watch out |
|-------------|----------------|-----------|
| IID tabular | StratifiedKFold (5–10) | target encoding inside fold |
| Groups (customer/store) | GroupKFold / StratifiedGroupKFold | group leakage |
| Time series | TimeSeriesSplit, PurgedKFold+embargo | future leakage |
| Spatio-temporal | block / spatial holdout | regional bias |

## Scale Modes

| Request pattern | Mode | Agents |
|-----------------|------|--------|
| Full competition strategy + modeling | Full pipeline | all 5 |
| CV/leakage audit only | Validation mode | validation + reviewer |
| Feature engineering only | Feature mode | feature + reviewer |
| Ensemble/tuning only | Training mode | training + validation + reviewer |
| Submission improvement only | Submit mode | validation + strategist + reviewer |
| Final check only | Review mode | reviewer only |
| Dacon code submission prep | Code audit mode | reviewer + strategist + training |

**Reuse**: copy notebooks/LB logs/CSVs to `_workspace/` and run only needed phases.

## Data Transfer Protocol

| Strategy | Channel | Use |
|----------|---------|-----|
| File | `_workspace/` | strategy, pipelines, validation docs |
| Code | `_workspace/pipeline_code/` | reproducible train/infer scripts |
| Submit | `_workspace/submission/` | CSV, validation logs, commands |
| Experiments | `_workspace/experiments/` | run metadata, LB mapping |
| Message | `Task` subagent | fix requests, urgent risks |

Naming: `{index}_{topic}.{md|py|csv}`

## Error Handling

| Issue | Strategy |
|-------|----------|
| CV ≫ LB (offline inflated) | leakage, split, metric impl, train/test shift |
| CV ≪ LB | metric direction, submission format, post-processing bug |
| shake-up (public↑ private↓) | assume public overfit; switch final pick to CV-trusted |
| daily submit limit exhausted | stop explore slots; offline experiments |
| non-reproducible | seed lock, requirements/uv lock, data hash |
| submit failure | validate rows/columns/dtype/index vs sample_submission |
| external data leakage | adversarial check vs test overlap |
| no GPU | lightweight models, subsampled CV, fewer Optuna trials |
| agent failure | retry once → note omission in review |

## Test Scenarios

### Happy path — Kaggle tabular
**Prompt**: "Kaggle Playground classification, top 10% goal, XGBoost+LightGBM ensemble."
**Expected**: strategist plan + dual submit; fold-safe features; Optuna + rank blend; CV-LB table; reviewer Go.

### Dacon code audit
**Prompt**: "Dacon finals done, Private rank 5 — package pipeline for code submission."
**Expected**: `/data` paths, UTF-8 CSV, Private reproduction README, single entrypoint, reviewer checklist.

### Error path — CV-LB mismatch
**Prompt**: "CV 0.92 but public LB 0.78 — what's wrong?"
**Expected**: validation-first; leakage/split/adversarial/metric checks before model suggestions.

## Extension Skills

| Skill | Path | Agents | Role |
|-------|------|--------|------|
| leaderboard-strategy | `.cursor/skills/leaderboard-strategy/skill.md` | strategist, validation | public/private, shake-up, slots |
| cv-leakage-guard | `.cursor/skills/cv-leakage-guard/skill.md` | feature, validation | split, leakage, adversarial |
| experiment-tracking-blueprint | `.cursor/skills/experiment-tracking-blueprint/skill.md` | training, reviewer | MLflow/DVC, submit mapping |
| ensemble-strategy | `.cursor/skills/ensemble-strategy/skill.md` | training, validation | blend/stack/rank, diversity |
| platform-playbook | `.cursor/skills/platform-playbook/skill.md` | strategist, reviewer | Kaggle vs Dacon rules |
