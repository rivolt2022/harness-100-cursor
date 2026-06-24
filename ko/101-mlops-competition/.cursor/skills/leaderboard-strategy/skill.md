---
name: leaderboard-strategy
description: "대회 리더보드 운영 전략. public/private split, shake-up 대응, Explore/Exploit 제출 슬롯, dual final submission을 다룬다. '리더보드 전략', 'shake-up', '제출 슬롯', 'public private' 요청에 사용한다."
---

# Leaderboard Strategy — 리더보드 운영 전략

Public LB는 **약 30% 테스트**에 대한 피드백이다. Final은 private(나머지 ~70%)가 결정한다. Public을 과도하게 최적화하면 shake-up에서 급락한다.

## Public vs Private 이해

| 구분 | 역할 | 올바른 사용 |
|------|------|------------|
| Public LB | 조기 피드백, CV 보정 | 상관 확인용 lodestar |
| Private LB | 최종 순위 | CV 신뢰 모델이 대응 |
| Local CV | 의사결정 기준 | 모델 선택·튜닝의 ground truth |

**금지**: public LB 점수를 CV fold에 합산해 "평균 CV"를 만드는 것(과적합 유발).  
**권장**: 여러 모델의 (CV, public LB) 쌍을 기록하고 **상관**만 추적한다.

## 제출 슬롯 운영 (Explore / Exploit)

| 유형 | 목적 | 비율 가이드 | 예시 |
|------|------|-------------|------|
| Explore | CV-LB 보정, 새 아이디어 검증 | 초반 60~70% | 새 split, 새 피처, 단순 베이스라인 |
| Exploit | 검증된 파이프라인 미세 조정 | 중후반 30~40% | best seed, 앙상블 weight |
| Reserve | 마감 직전 | 1~2 슬롯 | CV 신뢰 + public best |

**데이콘**: 일일 3회 제한 대회가 많음 → 주간 제출 캘린더 필수.  
**Kaggle**: 일일 한도가 넉넉해도 explore 남발은 public 과적합 위험.

## Dual Final Submission

Kaggle은 최종 **2개 선택**을 허용한다. 데이콘도 대회별 1~2개 선택 규칙이 있다.

| 후보 | 선택 기준 | 목적 |
|------|----------|------|
| A — CV Champion | fold 평균 최고 + 안정성 | private shake-up 방어 |
| B — Public Peak | public LB 최고 | upside 옵션 |
| C — Diverse Ensemble | 상관 낮은 모델 blend | 분산 리스크 (선택 시 A/B 대체) |

마감 24~48시간 전에 후보를 고정하고, 마지막 슬롯은 **신규 실험보다 검증된 후보 재제출**에 사용한다.

## Shake-up 대응 플레이북

**증상**: public 상위 → private 공개 후 급락

1. public LB만 올린 모델 목록 분리
2. CV 상위·fold 안정 모델 목록 분리
3. 두 목록의 교집합을 최종 1순위로
4. 교집합 없으면 **CV 우선** (역사적으로 CV-trusted가 private에서 유리한 경우 다수)
5. 이후 실험은 adversarial validation + split 재설계

## CV-LB 추적 템플릿

| run_id | model | cv_mean | cv_std | public_lb | delta (cv-lb) | notes |
|--------|-------|---------|--------|-----------|---------------|-------|
| exp_001 | lgb_baseline | 0.812 | 0.008 | 0.798 | +0.014 | 초기 보정 |
| exp_012 | xgb_blend | 0.831 | 0.006 | 0.829 | +0.002 | 상관 양호 |

상관계수 r 목표: **≥ 0.85**. 미달 시 모델 개선 중단 → validation 에이전트 CV 재설계.

## 리스크 분산 전략

- **모델 다양성**: 트리 + 선형 + NN(해당 시) 포트폴리오
- **시드 다양성**: 동일 구조 3 seed — median 제출
- **피처 다양성**: 서로 다른 피처 subset 모델 앙상블
- **과도한 단일 모델 의존** 금지

## 대회 단계별 포커스

| 기간 | 초점 | 제출 |
|------|------|------|
| D-14~D-7 | 베이스라인, CV 보정 | explore 위주 |
| D-7~D-3 | 피처·튜닝·앙상블 | exploit 전환 |
| D-3~D-1 | 후보 고정, 재현성 | reserve only |
| D-day | 최종 선택 파일 확정 | CV champion + public peak |

## 산출물 체크리스트

`_workspace/01_competition_plan.md` / `_workspace/04_validation_submission.md`에 포함:
- 일일/총 제출 한도와 캘린더
- Explore/Exploit 비율
- 최종 후보 A/B (및 근거)
- CV-LB 상관 로그
- shake-up 시나리오 대응 (public↓ private↑ / 반대)
