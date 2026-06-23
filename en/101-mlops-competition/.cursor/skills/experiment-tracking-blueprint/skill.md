---
name: experiment-tracking-blueprint
description: "Template for experiment tracking and reproducibility in competition workflows."
---

# Experiment Tracking Blueprint

## Required fields
- experiment_id, run_id, data_version, feature_set, model_tag
- cv_scheme, seed, metric_offline, metric_public_lb
- submission_file, notebook/script hash

## Operating rules
- Store each submission with reproducible generation scripts.
- Record final-model decisions with performance and stability rationale.
- Keep failed runs with tagged root causes.
