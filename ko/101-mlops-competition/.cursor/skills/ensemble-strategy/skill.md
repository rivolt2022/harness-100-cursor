---
name: ensemble-strategy
description: "대회용 앙상블 전략. blending, stacking, rank averaging, 다양성 기반 가중치를 다룬다. '앙상블 설계', '모델 블렌딩', '스태킹', '다양한 모델 조합' 요청에 사용한다."
---

# Ensemble Strategy — 대회용 앙상블

단일 최고 모델보다 **다양한 오류 패턴**을 가진 모델 조합이 private LB에서 유리한 경우가 많다. public LB만 맞춘 단일 모델은 shake-up에 취약하다.

## 앙상블 방식 선택

| 방식 | 복잡도 | 적합 상황 | 주의 |
|------|--------|----------|------|
| Simple average | 낮음 | 유사 스케일 회귀/확률 | 스케일 불일치 시 비효율 |
| Weighted blend | 중간 | CV로 weight 탐색 | weight 과적합 |
| Rank average | 중간 | 메트릭 스케일 상이 | 순위 기반 대회 |
| Stacking (OOF) | 높음 | 충분한 데이터·시간 | meta leakage 방지 |
| Multi-seed same model | 낮음 | variance 감소 | 다양성 제한 |

## Weighted Blend (CV 최적화)

```python
import numpy as np
from scipy.optimize import minimize

# preds: list of (n_samples,) OOF or test predictions
# y_val: validation labels

def blend_loss(weights):
    w = np.array(weights)
    w = w / w.sum()
    blended = sum(wi * pi for wi, pi in zip(w, preds))
  # metric: maximize → minimize negative
    return -metric_fn(y_val, blended)

n = len(preds)
w0 = np.ones(n) / n
bounds = [(0, 1)] * n
constraints = {"type": "eq", "fun": lambda w: sum(w) - 1}
result = minimize(blend_loss, w0, bounds=bounds, constraints=constraints)
```

**규칙**: weight는 **OOF 예측**으로만 최적화. test label 사용 금지.

## Stacking (OOF Meta-Model)

```python
# Level-0: 각 fold에서 train만 학습 → val OOF 저장
# Level-1: OOF features로 meta-model 학습
# Test: fold별 모델 예측 평균 → meta-model 입력

# ❌ 금지: full train으로 level-0 학습 후 같은 train으로 meta fit (leakage)
# ✅ 권장: sklearn StackingClassifier 또는 manual OOF loop
```

## 다양성 평가

앙상블 전에 base 모델 예측 상관을 확인한다.

| pred_corr | 해석 | 조치 |
|-----------|------|------|
| < 0.7 | 다양성 양호 | 앙상블 우선 후보 |
| 0.7 ~ 0.9 | 보통 | weight blend |
| > 0.9 | 거의 동일 | 하나 제거 또는 다른 피처/알고리즘 추가 |

```python
import pandas as pd
corr = pd.DataFrame({"m1": p1, "m2": p2, "m3": p3}).corr()
```

## 모델 포트폴리오 구성 가이드

| 계층 | 후보 | 역할 |
|------|------|------|
| 베이스 | Logistic / Linear | 안정 baseline, 메타 피처 |
| 트리 | LightGBM, XGBoost, CatBoost | 비선형, 범주 |
| NN | TabNet, MLP (tabular) | 다른 inductive bias |
| 도메인 | 규칙·통계 피처 모델 | 분포 이동 방어 |

**목표**: 상관 낮은 3~5개 모델. 10개 이상은 관리·과적합 비용 증가.

## 대회 메트릭별 팁

| 메트릭 | 앙상블 힌트 |
|--------|------------|
| AUC / logloss | 확률 평균 또는 logit 평균 |
| RMSE / MAE | 가중 평균, outlier 모델 down-weight |
| Accuracy | voting 또는 확률 argmax |
| Custom ranking | rank average 우선 |

## 비용 대비 효과

1. **먼저**: 서로 다른 seed 동일 모델 (저비용)
2. **다음**: LGB + XGB + CatBoost blend
3. **마지막**: stacking + Optuna weight (고비용, CV 확인 후)

CV 개선 < 0.001이면 앙상블 복잡도 증가를 중단한다.

## 산출물 템플릿 (`_workspace/03_training_plan.md`)

- base 모델 목록 + CV 점수 + fold std
- 예측 상관 행렬
- 선택한 앙상블 방식과 weight
- OOF vs holdout 성능
- 제출용 inference 명령 (재현 경로)
