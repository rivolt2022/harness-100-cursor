---
name: cv-leakage-guard
description: "Cross-validation design and leakage prevention guide for competition pipelines."
---

# CV Leakage Guard

## Goal
Improve offline-to-leaderboard consistency.

## Guardrails
- Block future-information leakage by event time.
- Prefer GroupKFold/TimeSeriesSplit/StratifiedGroupKFold when appropriate.
- Compute target encoding strictly inside each fold.
- Record split policy in preprocessing logs.
