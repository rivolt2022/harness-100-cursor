---
name: experiment-tracking-blueprint
description: "Competition experiment tracking template. MLflow/DVC integration, experiment-to-submission mapping, reproducibility fields. Use for 'experiment tracking', 'MLflow competition', 'submission reproduction', 'DVC pipeline'."
---

# Experiment Tracking Blueprint

Every submission must be **regenerable by one command**. Dacon 2nd-round audits require Private Score reproduction.

## Standard Metadata Fields

| Field | Description | Example |
|-------|-------------|---------|
| experiment_id | competition scope | `dacon-antenna-2024` |
| run_id | single run | `exp_042_xgb_v3` |
| data_version | data snapshot | DVC hash |
| feature_set | feature tag | `fe_v4_group_agg` |
| model_tag | model id | `lgb_optuna_50t` |
| cv_scheme | CV type | `StratifiedKFold_5` |
| seed | random seed | `42` |
| metric_offline | CV score | `0.8312 ± 0.006` |
| metric_public_lb | public score | `0.8291` |
| submission_file | path | `submission/exp_042.csv` |
| code_ref | git commit | `a1b2c3d` |
| env_ref | Python/CUDA | `py3.11` |

## MLflow Pattern

```python
import mlflow
import pandas as pd

mlflow.set_experiment("competition-name")
with mlflow.start_run(run_name="lgb-baseline-v1"):
    mlflow.log_params({"model": "LGBMClassifier", "cv": "StratifiedKFold_5", "seed": 42})
    mlflow.log_metrics({"cv_mean": cv_mean, "cv_std": cv_std, "public_lb": public_lb})
    mlflow.sklearn.log_model(model, "model")
    sub_path = "submission/run_001.csv"
    pd.DataFrame({"id": ids, "target": preds}).to_csv(sub_path, index=False)
    mlflow.log_artifact(sub_path)
    mlflow.log_artifact("requirements.txt")
```

## DVC Pipeline Skeleton

```yaml
stages:
  preprocess:
    cmd: python pipeline_code/preprocess.py
    deps: [data/raw, pipeline_code/preprocess.py]
    outs: [data/processed]
  train:
    cmd: python pipeline_code/train.py
    deps: [data/processed, pipeline_code/train.py, params.yaml]
    outs: [models/model.pkl, metrics.json]
  predict:
    cmd: python pipeline_code/predict.py
    deps: [models/model.pkl, data/processed]
    outs: [submission/submission.csv]
```

## Submission Mapping Rules

1. Filename includes `run_id`
2. Update `metric_public_lb` after each submit
3. Document best-model rationale: performance **and** fold stability
4. Tag failed runs with `fail_reason`

## Reproducibility Checklist

- [ ] Single entrypoint (`make train` / `python main.py`)
- [ ] Documented paths (`/data` for Dacon)
- [ ] CPU fallback for audit environments
- [ ] UTF-8 CSV (Dacon required)

## Recommended Layout

```
_workspace/
├── experiments/experiment_log.md
├── pipeline_code/{preprocess,train,predict}.py
├── submission/
├── metrics.json
└── requirements.txt
```

## Operating Principles

- Notebook-only without scripts → 🔴 scriptize before deadline
- Submit without run record → 🟡 recommended fix
- External API inference without cache → document reproducibility risk
