---
name: ensemble-strategy
description: "Competition ensemble strategies: blending, stacking, rank averaging, diversity-based weights. Use for 'ensemble design', 'model blending', 'stacking', 'diverse model combination'."
---

# Ensemble Strategy

Combining models with **diverse error patterns** often beats a single public-LB-optimized model on private LB.

## Method Selection

| Method | Complexity | Best for | Caution |
|--------|------------|----------|---------|
| Simple average | low | similar-scale probs | scale mismatch |
| Weighted blend | medium | CV-optimized weights | weight overfit |
| Rank average | medium | different metric scales | rank-based comps |
| Stacking (OOF) | high | enough data/time | meta leakage |
| Multi-seed same model | low | variance reduction | limited diversity |

## Weighted Blend (CV optimization)

Optimize weights on **OOF predictions only** — never test labels.

```python
from scipy.optimize import minimize
# minimize negative metric on weighted sum of OOF preds
```

## Stacking (OOF Meta-Model)

Level-0: train per fold → save OOF. Level-1: meta on OOF. Test: average fold preds → meta input.

**Forbidden**: meta trained on in-sample level-0 preds.

## Diversity Check

| pred_corr | Interpretation | Action |
|-----------|----------------|--------|
| < 0.7 | good diversity | ensemble priority |
| 0.7–0.9 | moderate | weighted blend |
| > 0.9 | redundant | drop one or change features/algo |

## Portfolio Layers

| Layer | Candidates | Role |
|-------|------------|------|
| Base | Logistic / Linear | stable baseline |
| Trees | LGB, XGB, CatBoost | nonlinear |
| NN | TabNet, MLP | different bias |
| Domain | rule/stat features | shift defense |

Target: 3–5 low-correlation models.

## Metric Tips

| Metric | Hint |
|--------|------|
| AUC / logloss | probability or logit average |
| RMSE / MAE | weighted mean, down-weight outliers |
| Accuracy | voting or prob argmax |
| Custom ranking | rank average |

## Cost vs Gain

1. Different seeds, same model (cheap)
2. LGB + XGB + CatBoost blend
3. Stacking + Optuna weights (expensive; only if CV confirms)

Stop added complexity if CV gain < 0.001.

## Deliverable (`_workspace/03_training_plan.md`)

- base models + CV + fold std
- prediction correlation matrix
- ensemble method & weights
- OOF vs holdout
- inference command for submit
