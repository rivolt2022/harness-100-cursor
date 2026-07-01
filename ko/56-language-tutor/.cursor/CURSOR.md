# Language Tutor Harness

외국어 학습을 위한 레벨 테스트, 커리큘럼, 레슨, 퀴즈, 복습 관리 에이전트 팀 하네스.

## 구조

```
.cursor/
├── agents/
│   ├── level-assessor.md
│   ├── curriculum-designer.md
│   ├── lesson-tutor.md
│   ├── quiz-master.md
│   └── review-coach.md
├── skills/
│   ├── language-tutor/
│   │   └── skill.md              — 오케스트레이터
│   ├── spaced-repetition/
│   │   └── skill.md              — 간격 반복 알고리즘 (SM-2, 에빙하우스, 복습 설계)
│   └── cefr-assessment/
│       └── skill.md              — CEFR 레벨 평가 (6단계 기술자, 적응형 진단, 시험 매핑)
└── CURSOR.md                     — 이 파일
```

## 사용법

Cursor 채팅창에 `@language-tutor`으로 요청한다.
