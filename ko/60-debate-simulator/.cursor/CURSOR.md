# Debate Simulator Harness

토론 시뮬레이션 에이전트 팀 하네스.

## 구조

```
.cursor/
├── agents/
│   ├── topic-analyst.md
│   ├── pro-debater.md
│   ├── con-debater.md
│   ├── judge.md
│   └── rapporteur.md
├── skills/
│   ├── debate-simulator/
│   │   └── skill.md              — 오케스트레이터
│   ├── argumentation-framework/
│   │   └── skill.md              — 논증 구축 (Toulmin 모델, 증거 피라미드, 반박 5-Type)
│   └── logical-fallacy-detector/
│       └── skill.md              — 논리적 오류 검출 (4대 분류, 감점 기준, 루브릭)
└── CURSOR.md                     — 이 파일
```

## 사용법

Cursor 채팅창에 `@debate-simulator`으로 요청한다.
