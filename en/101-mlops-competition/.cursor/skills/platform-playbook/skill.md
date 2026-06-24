---
name: platform-playbook
description: "Kaggle vs Dacon platform rules, submission, and code audit guide. Use for 'Kaggle rules', 'Dacon code submission', 'submission format', 'Private Score reproduction'."
---

# Platform Playbook — Kaggle vs Dacon

Submission limits, final selection, and code audits differ by platform. Confirm the competition Rules page, then adjust this playbook.

## Comparison

| Item | Kaggle | Dacon (typical) |
|------|--------|-----------------|
| Public/Private | ~30% / ~70% public test | varies (e.g. 50/100%) |
| Daily submits | usually generous | often **3/day** |
| Final selection | **2** submissions | **1–2** (comp-specific) |
| Code submit | optional sharing | **required** for top teams |
| Encoding | UTF-8 CSV recommended | **UTF-8 required** |
| Data path | `/kaggle/input` | often fixed `/data` |
| Cheating | API/external data policy | **disqualification** on leakage |
| 2nd round | comp-specific | code verify + PPT/presentation |

> Rules vary per competition — always verify the official Rules page.

## Kaggle Checklist

- [ ] Metric direction (higher/lower is better)
- [ ] Format vs `sample_submission.csv`
- [ ] Team merge / external data / notebook rules
- [ ] GPU session limits
- [ ] Early baseline for CV-LB calibration
- [ ] Final 2: CV champion + public peak

### Kaggle API

```bash
kaggle competitions download -c competition-slug
kaggle competitions submit -c competition-slug -f submission.csv -m "exp_042"
```

## Dacon Checklist

- [ ] Daily submit limit (3/day?)
- [ ] Final file count (1 or 2)
- [ ] Custom metric formula
- [ ] Public/Private ratio
- [ ] Code package deadline & email
- [ ] **Private Score reproduction** path
- [ ] `/data` I/O paths
- [ ] UTF-8 CSV
- [ ] No test-info leakage (disqualification risk)

### Dacon Submit Package

```
submit_package/
├── README.md          # run instructions, env, runtime
├── requirements.txt
├── main.py
├── src/
├── models/
└── submission.csv
```

README must include: Python version, install command, data paths, one-line train+infer, expected score.

## Common Validation Script

```python
import pandas as pd
sample = pd.read_csv("sample_submission.csv")
sub = pd.read_csv("submission/submission.csv")
assert list(sub.columns) == list(sample.columns)
assert len(sub) == len(sample)
assert sub.isnull().sum().sum() == 0
```

## Strategy Differences

| Strategy | Kaggle | Dacon |
|----------|--------|-------|
| Slots | explore OK | weekly calendar if 3/day |
| Finals | dual strategy | if 1 pick → CV champion |
| Docs | notebook cleanup | audit-grade README |
| Pre-deadline | reproducible scripts | `/data` test run |

## Reviewer Integration

For Dacon, mlops-reviewer treats as 🔴 required:
- Private reproduction README
- leakage / rule violations
- UTF-8, paths, dependencies complete
