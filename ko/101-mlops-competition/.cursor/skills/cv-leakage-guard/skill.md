---
name: cv-leakage-guard
description: "CV 설계 및 데이터 누수 방지 가이드. 시간/그룹/사용자 단위 분리와 피처 생성 시점 검증을 제공한다."
---

# CV Leakage Guard

## 목적
- 오프라인 CV 점수와 대회 LB 점수의 괴리를 줄인다.

## 가이드
- 데이터 생성 시점 기준으로 미래 정보 누수 차단
- GroupKFold/TimeSeriesSplit/StratifiedGroupKFold 우선 검토
- target encoding은 fold 내부에서만 계산
- 피처 스토어/전처리 로그에 split 정책 명시
