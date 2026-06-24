---
name: cv-leakage-guard
description: "CV 설계 및 데이터 누수 방지 가이드. 시간/그룹/사용자 단위 분리, fold 내 전처리, adversarial validation, target encoding 가드를 제공한다. 'CV 누수', '데이터 누수', 'GroupKFold', '시계열 CV', 'target encoding 누수' 요청에 사용한다."
---

# CV Leakage Guard — CV 설계 및 누수 방지

오프라인 CV가 **private LB의 대리 지표**가 되도록 설계한다. CV와 LB가 어긋나면 모든 "개선"이 역효과일 수 있다.

## 핵심 원칙

1. **Fit은 train fold에서만, transform은 val/test에 적용** — scaler, imputer, encoder, target stats 전부 동일.
2. **Split은 문제 구조를 반영** — IID가 아니면 random KFold 금지.
3. **외부 데이터·사전학습 모델**도 test와 중복 여부를 검사한다.
4. **CV 점수의 신뢰성**이 단일 모델 성능보다 중요하다.

## Split 선택 매트릭스

| 신호 | 권장 방법 | 파라미터 힌트 |
|------|----------|--------------|
| 균형 분류, IID | StratifiedKFold | n_splits=5~10 |
| 그룹 ID 존재 | GroupKFold | group=customer_id |
| 불균형+그룹 | StratifiedGroupKFold | group + stratify |
| 시계열 | TimeSeriesSplit | gap/embargo 고려 |
| 금융/이벤트 시계열 | PurgedKFold + embargo | overlap 제거 |
| train/test 분포 차이 의심 | adversarial validation | AUC > 0.7이면 재분할 |

## Fold-Safe 전처리 패턴

```python
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

# ❌ 금지: 전체 데이터로 fit 후 split
# scaler.fit(X_full); X_train = scaler.transform(X_train)

# ✅ 권장: Pipeline + cross_val_score / cross_validate
pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
    ("model", model),
])
scores = cross_val_score(pipe, X, y, cv=cv, scoring=metric)
```

### Target Encoding (fold 내부)

```python
# 각 fold에서 train 통계만으로 encoding 계산
# validation fold에는 smoothing 적용된 train 통계만 사용
# 전역 mean으로 full-data encoding 금지
```

## Adversarial Validation

train과 test가 구분 가능하면 split/CV가 잘못되었거나 분포 이동이 크다.

```python
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
import lightgbm as lgb

X_adv = np.vstack([X_train, X_test])
y_adv = np.array([0]*len(X_train) + [1]*len(X_test))

oof = np.zeros(len(X_adv))
for tr, va in StratifiedKFold(5, shuffle=True, random_state=42).split(X_adv, y_adv):
    m = lgb.LGBMClassifier(n_estimators=200, random_state=42)
    m.fit(X_adv.iloc[tr], y_adv[tr])
    oof[va] = m.predict_proba(X_adv.iloc[va])[:, 1]

auc = roc_auc_score(y_adv, oof)
# auc > 0.7 → 분포 차이 큼 → time/group split 또는 domain adaptation 검토
```

## 누수 체크리스트

### 전처리
- [ ] train+test concat 후 통계 계산 없음
- [ ] target encoding이 fold 밖 정보 사용 안 함
- [ ] 결측 대체값이 validation에 누수되지 않음
- [ ] 피처 선택이 전체 label 분포를 보지 않음

### 피처 엔지니어링
- [ ] 미래 시점 데이터가 과거 행에 합쳐지지 않음
- [ ] 집계 피처의 시간 창이 prediction 시점 이전만 포함
- [ ] 동일 ID의 train/test 교차 없음 (GroupKFold)
- [ ] 외부 조인 키가 test 정보를 역으로 끌어오지 않음

### 모델링
- [ ] early stopping이 validation fold 기준
- [ ] pseudo-labeling 시 test label 직접 사용 없음
- [ ] stacking meta-model이 같은 fold 예측만 사용

## CV 품질 기준

| 지표 | 목표 | 조치 |
|------|------|------|
| fold 간 std/mean | < 20% | split/샘플링 재검토 |
| CV vs public LB 상관 r | ≥ 0.85 | LB early submit으로 보정 |
| adversarial AUC | < 0.65 | 분포 유사, CV 신뢰 가능 |
| 베이스라인 LB 방향 | 메트릭 higher/lower_is_better 일치 | 메트릭 구현 버그 수정 |

## 흔한 실패 패턴

| 증상 | 원인 | 수정 |
|------|------|------|
| CV 0.9+, LB 0.75 | target leak, wrong split | fold pipeline 재구성 |
| fold별 점수 편차 큼 | 소수 그룹/클래스 | GroupKFold, stratify |
| LB만 오르고 CV 정체 | public 과적합 | CV 신뢰 모델 유지 |
| 시계열에서 CV 과대 | shuffle KFold | Purged/TimeSeriesSplit |

## 산출물에 포함할 항목

`_workspace/02_feature_pipeline.md` 또는 `_workspace/04_validation_submission.md`에:
- 선택한 CV 스킴과 **선택 근거**
- 누수 방지 체크리스트 결과 (✅/❌)
- adversarial validation 결과 (해당 시)
- fold-safe 코드 스니펫 또는 Pipeline 다이어그램
