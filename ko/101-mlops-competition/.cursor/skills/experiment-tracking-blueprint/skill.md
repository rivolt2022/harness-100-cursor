---
name: experiment-tracking-blueprint
description: "대회형 실험 추적 템플릿. MLflow/DVC 연동, 실험-제출 매핑, 재현성 필드를 표준화한다. '실험 추적', 'MLflow 대회', '제출 재현', 'DVC 파이프라인' 요청에 사용한다."
---

# Experiment Tracking Blueprint — 대회형 실험 추적

모든 제출은 **동일 명령으로 재생성** 가능해야 한다. 데이콘 2차 평가는 Private Score 복원을 요구한다.

## 표준 메타데이터 필드

| 필드 | 설명 | 예시 |
|------|------|------|
| experiment_id | 대회 단위 ID | `dacon-antenna-2024` |
| run_id | 단일 실험 | `exp_042_xgb_v3` |
| data_version | 데이터 스냅샷 | `train_v2.1`, DVC hash |
| feature_set | 피처 세트 태그 | `fe_v4_group_agg` |
| model_tag | 모델 식별 | `lgb_optuna_50t` |
| cv_scheme | CV 종류 | `StratifiedKFold_5` |
| seed | 랜덤 시드 | `42` |
| metric_offline | CV 점수 | `0.8312 ± 0.006` |
| metric_public_lb | public 점수 | `0.8291` |
| submission_file | 제출 경로 | `submission/exp_042.csv` |
| code_ref | git commit / notebook | `a1b2c3d` |
| env_ref | Python/CUDA | `py3.11, cuda12.1` |

## MLflow 통합 패턴

```python
import mlflow
import pandas as pd

mlflow.set_experiment("competition-name")

with mlflow.start_run(run_name="lgb-baseline-v1"):
    mlflow.log_params({
        "model": "LGBMClassifier",
        "cv": "StratifiedKFold_5",
        "seed": 42,
        "feature_set": "fe_v1",
    })
    mlflow.log_metrics({
        "cv_mean": cv_mean,
        "cv_std": cv_std,
        "public_lb": public_lb,  # 제출 후 수동/스크립트 갱신
    })
    mlflow.sklearn.log_model(model, "model")

    sub_path = "submission/run_001.csv"
    pd.DataFrame({"id": ids, "target": preds}).to_csv(sub_path, index=False)
    mlflow.log_artifact(sub_path)
    mlflow.log_artifact("requirements.txt")
```

### 자동 로깅 (선택)

```python
mlflow.lightgbm.autolog()
mlflow.xgboost.autolog()
```

## DVC 파이프라인 스켈레톤

```yaml
# dvc.yaml
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
    deps: [models/model.pkl, data/processed, pipeline_code/predict.py]
    outs: [submission/submission.csv]
```

`dvc repro` 한 번으로 Private Score 복원 경로를 증명한다.

## 제출-실험 매핑 규칙

1. 제출 파일명에 `run_id` 포함: `submission_{run_id}.csv`
2. 제출 직후 `metric_public_lb`를 run에 기록
3. best model 선정 근거를 **성능 + fold 안정성**으로 문서화
4. 실패 실험도 `fail_reason` 태그 후 보존 (같은 실수 반복 방지)

## 재현성 체크리스트

```python
reproducibility = {
    "python": sys.version,
    "seed": {"random": 42, "numpy": 42, "torch": 42},
    "data_hash": hashlib.sha256(open("train.csv","rb").read()).hexdigest()[:16],
    "git_commit": subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip(),
    "package_lock": "requirements.txt or uv.lock",
}
```

- [ ] 단일 진입점 스크립트 존재 (`make train` / `python main.py`)
- [ ] 상대 경로 또는 `/data` 규칙 문서화
- [ ] GPU 없이 CPU fallback 가능 (데이콘 검증 환경)
- [ ] 제출 CSV UTF-8 인코딩 (데이콘 필수)

## 실험 비교 워크플로

1. MLflow UI 또는 표로 `metric_offline` 정렬
2. 상위 5 run의 fold std, public_lb delta 비교
3. 앙상블 후보는 **예측 상관**이 낮은 조합 우선
4. reviewer가 재현성 체크리스트로 Go/No-Go

## 디렉토리 권장 구조

```
_workspace/
├── experiments/
│   └── experiment_log.md      # run 요약 표
├── pipeline_code/
│   ├── preprocess.py
│   ├── train.py
│   └── predict.py
├── submission/
│   ├── submission_exp_042.csv
│   └── validate_submission.py
├── metrics.json
└── requirements.txt
```

## 운영 원칙

- 노트북만 있고 스크립트 없음 → 🔴 마감 전 반드시 스크립트화
- 제출 without run 기록 → 🟡 권장 수정
- 외부 API 추론 without 캐시 → 재현성 리스크 명시
