---
name: cv-leakage-guard
description: "CV design and data leakage prevention. Temporal/group/user splits, in-fold preprocessing, adversarial validation, target encoding guards. Use for 'CV leakage', 'data leakage', 'GroupKFold', 'time series CV', 'target encoding leak'."
---

# CV Leakage Guard

Design offline CV so it acts as a **proxy for private LB**. When CV and LB diverge, every "improvement" may hurt final rank.

## Core Principles

1. **Fit on train fold only; transform val/test** — scaler, imputer, encoders, target stats.
2. **Splits reflect problem structure** — no random KFold for non-IID data.
3. **Audit external data & pretrained models** for test overlap.
4. **CV reliability** matters more than a single model score.

## Split Selection Matrix

| Signal | Method | Hints |
|--------|--------|-------|
| Balanced classification, IID | StratifiedKFold | n_splits=5–10 |
| Group IDs | GroupKFold | group=customer_id |
| Imbalanced + groups | StratifiedGroupKFold | group + stratify |
| Time series | TimeSeriesSplit | gap/embargo |
| Finance/event series | PurgedKFold + embargo | remove overlap |
| train/test shift suspected | adversarial validation | AUC > 0.7 → redesign |

## Fold-Safe Preprocessing

```python
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# ❌ Forbidden: fit on full data then split
# ✅ Use Pipeline + cross_val_score
pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
    ("model", model),
])
scores = cross_val_score(pipe, X, y, cv=cv, scoring=metric)
```

### Target Encoding (inside fold)

Compute encoding from train fold only; apply smoothed stats to validation. Never encode with full-dataset targets.

## Adversarial Validation

If train vs test is separable, CV or split is wrong or shift is large.

```python
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
import lightgbm as lgb

X_adv = np.vstack([X_train, X_test])
y_adv = np.array([0]*len(X_train) + [1]*len(X_test))
# ... train classifier, AUC > 0.7 → revisit split
```

## Leakage Checklist

### Preprocessing
- [ ] No train+test concat statistics
- [ ] Target encoding uses no out-of-fold info
- [ ] Imputation values don't leak from validation
- [ ] Feature selection doesn't use full label distribution

### Feature engineering
- [ ] No future timestamps in past rows
- [ ] Aggregations only use history before prediction time
- [ ] No train/test ID overlap (GroupKFold)
- [ ] External joins don't pull test labels

### Modeling
- [ ] Early stopping on validation fold
- [ ] No direct test labels in pseudo-labeling
- [ ] Stacking meta uses OOF predictions only

## CV Quality Criteria

| Metric | Target | Action |
|--------|--------|--------|
| fold std/mean | < 20% | revisit split/sampling |
| CV vs public LB r | ≥ 0.85 | early submits to calibrate |
| adversarial AUC | < 0.65 | distributions similar |
| baseline LB direction | matches higher/lower_is_better | fix metric code |

## Common Failure Patterns

| Symptom | Cause | Fix |
|---------|-------|-----|
| CV 0.9+, LB 0.75 | target leak, wrong split | fold pipeline |
| High fold variance | rare groups/classes | GroupKFold, stratify |
| LB up, CV flat | public overfit | keep CV-trusted model |
| Inflated time-series CV | shuffled KFold | Purged/TimeSeriesSplit |

## Deliverable Items

Include in `_workspace/02_feature_pipeline.md` or `_workspace/04_validation_submission.md`:
- chosen CV scheme and **rationale**
- leakage checklist results
- adversarial validation (if run)
- fold-safe code snippets
