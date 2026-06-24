---
name: platform-playbook
description: "Kaggle vs 데이콘 플랫폼별 규칙·제출·코드 감사 가이드. '캐글 규칙', '데이콘 코드 제출', '제출 형식', 'Private Score 복원' 요청에 사용한다."
---

# Platform Playbook — Kaggle vs 데이콘

플랫폼마다 **제출 한도·최종 선택·코드 감사** 규칙이 다르다. strategist와 reviewer가 대회 페이지 규칙을 확인한 뒤 이 플레이북을 보정한다.

## 비교 요약

| 항목 | Kaggle | 데이콘 (일반적) |
|------|--------|----------------|
| Public/Private | ~30% / ~70% public test | 대회별 상이 (50/100% 등) |
| 일일 제출 | 대회별 (보통 넉넉) | 종종 **3회/일** |
| 최종 선택 | **2개** 제출 선택 | **1~2개** (대회별) |
| 코드 제출 | Discussion/노트북 공유 선택 | 상위팀 **필수** (Private 복원) |
| 인코딩 | CSV UTF-8 권장 | **UTF-8 필수** |
| 데이터 경로 | `/kaggle/input` | 종종 `/data` 고정 |
| 부정 행위 | API 규칙, external data 정책 | Data Leakage 시 **수상 제외** |
| 2차 평가 | 대회별 | 코드 검증 + PPT/발표 (상위팀) |

> 규칙은 대회마다 다르다. **반드시** 해당 대회 Rules 페이지를 웹에서 확인한다.

## Kaggle 체크리스트

- [ ] Evaluation metric 방향 (higher/lower is better)
- [ ] Submission file format (`sample_submission.csv` 대조)
- [ ] Team merge / external data / notebook output 규칙
- [ ] GPU session 시간 제한 (노트북 vs Scripts)
- [ ] Early baseline submit으로 CV-LB 보정
- [ ] Final 2 submissions: CV champion + public peak

### Kaggle API (로컬 파이프라인)

```bash
# 사용자 환경에 kaggle.json 필요
kaggle competitions download -c competition-slug
kaggle competitions submit -c competition-slug -f submission.csv -m "exp_042"
```

## 데이콘 체크리스트

- [ ] 일일 제출 횟수 (3회 제한 여부)
- [ ] 최종 선택 파일 개수 (1 or 2)
- [ ] 평가 메트릭 산식 (커스텀 formula 확인)
- [ ] Public/Private 비율 (규칙 페이지)
- [ ] 코드 제출 양식 (이메일, 기한, PPT)
- [ ] **Private Score 복원** 가능한 단일 실행 경로
- [ ] `/data` 입출력 경로 준수
- [ ] UTF-8 CSV
- [ ] Data Leakage 금지 (test 정보 학습 사용 시 실격)

### 데이콘 코드 제출 패키지

```
submit_package/
├── README.md              # 실행 방법, 환경, 예상 소요 시간
├── requirements.txt
├── main.py                # 또는 train.py + predict.py
├── src/
├── models/                # 또는 생성 방법 명시
└── submission.csv         # 재현 결과 샘플
```

README 필수 내용:
1. Python 버전, `pip install` 또는 `uv sync`
2. 데이터 배치 경로 (`/data/train.csv` 등)
3. 학습+추론 한 줄 명령
4. 예상 Private Score와 제출 CSV 생성 위치

## 공통 제출 검증 스크립트

```python
import pandas as pd

sample = pd.read_csv("sample_submission.csv")
sub = pd.read_csv("submission/submission.csv")

assert list(sub.columns) == list(sample.columns)
assert len(sub) == len(sample)
assert sub["id"].equals(sample["id"])  # id 컬럼명은 대회별 조정
assert sub.isnull().sum().sum() == 0
# metric direction smoke test (범위)
assert sub.iloc[:, -1].between(0, 1).all()  # 확률 대회 예시
```

## 플랫폼별 전략 차이

| 전략 | Kaggle | 데이콘 |
|------|--------|--------|
| 제출 슬롯 | explore 여유, 상관 수집 | 3회/일이면 주간 캘린더 필수 |
| 최종화 | 2개 dual strategy | 선택 1개면 CV champion 우선 |
| 문서화 | 노트북 정리 권장 | **코드 감사 필수** 수준 |
| 마감 전 | 재현 스크립트 | README + `/data` 테스트 |

## reviewer 연동

mlops-reviewer는 플랫폼이 데이콘이면 다음을 🔴 필수로 검사:
- Private Score 복원 README
- leakage·규칙 위반 여부
- UTF-8·경로·의존성 완전성
