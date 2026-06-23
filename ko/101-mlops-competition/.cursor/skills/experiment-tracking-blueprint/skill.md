---
name: experiment-tracking-blueprint
description: "대회형 실험 추적 템플릿. 실험 버전, 데이터 버전, 코드 해시, 제출 파일 매핑을 표준화한다."
---

# Experiment Tracking Blueprint

## 표준 필드
- experiment_id, run_id, data_version, feature_set, model_tag
- cv_scheme, seed, metric_offline, metric_public_lb
- submission_file, notebook/script hash

## 운영 원칙
- 모든 제출은 재생성 가능한 스크립트와 함께 보관
- best model 선택 근거(성능+안정성) 기록
- 실패 실험도 원인 태깅 후 보존
