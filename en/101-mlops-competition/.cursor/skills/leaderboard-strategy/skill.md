---
name: leaderboard-strategy
description: "Competition leaderboard operations: public/private split, shake-up handling, Explore/Exploit submission slots, dual final submission. Use for 'leaderboard strategy', 'shake-up', 'submission slots', 'public private'."
---

# Leaderboard Strategy

Public LB reflects roughly **30% of test data**. Finals use private (~70%). Over-optimizing public causes shake-down.

## Public vs Private

| Surface | Role | Correct use |
|---------|------|-------------|
| Public LB | early feedback, CV calibration | correlation lodestar |
| Private LB | final rank | CV-trusted models |
| Local CV | decision basis | model select & tune |

**Avoid**: adding public LB into CV folds.  
**Do**: log (CV, public LB) pairs and track **correlation**.

## Explore / Exploit Slots

| Type | Purpose | Ratio | Examples |
|------|---------|-------|----------|
| Explore | CV-LB calibration, new ideas | early 60–70% | new split, features, baselines |
| Exploit | refine validated pipeline | mid-late 30–40% | best seed, ensemble weights |
| Reserve | pre-deadline | 1–2 slots | CV-trusted + public best |

**Dacon**: often **3 submits/day** — weekly calendar required.  
**Kaggle**: generous limits still risk public overfit if explore is unchecked.

## Dual Final Submission

Kaggle allows **2 final picks**. Dacon varies (1–2).

| Candidate | Criteria | Purpose |
|-----------|----------|---------|
| A — CV Champion | best stable CV | shake-up defense |
| B — Public Peak | best public LB | upside option |
| C — Diverse Ensemble | low pred correlation | variance hedge |

Lock candidates 24–48h before deadline; last slots for **verified reruns**, not new experiments.

## Shake-up Playbook

**Symptom**: strong public → drop on private

1. List models that only improved public LB
2. List stable CV-top models
3. Prefer intersection for final #1
4. If empty, **prefer CV** (historically robust on private)
5. Run adversarial validation + split redesign

## CV-LB Tracking Template

| run_id | model | cv_mean | cv_std | public_lb | delta | notes |
|--------|-------|---------|--------|-----------|-------|-------|

Target correlation r: **≥ 0.85**. If below, pause model work → redesign CV.

## Risk Diversification

- Model diversity: trees + linear + NN (if applicable)
- Seed diversity: 3 seeds → median submit
- Feature diversity: different subsets in ensemble
- Avoid single-model dependency

## Phase Focus

| Period | Focus | Submissions |
|--------|-------|-------------|
| D-14~D-7 | baseline, CV calibration | explore |
| D-7~D-3 | features, tuning, ensemble | exploit |
| D-3~D-1 | lock candidates, reproducibility | reserve |
| D-day | finalize selected files | CV + public pair |

## Deliverable Checklist

In `_workspace/01_competition_plan.md` / `_workspace/04_validation_submission.md`:
- daily/total submit limits & calendar
- Explore/Exploit ratio
- final A/B candidates with rationale
- CV-LB correlation log
- shake-up response scenarios
