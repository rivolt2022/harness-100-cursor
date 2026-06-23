# Research Assistant Harness

학술 연구 보조 에이전트 팀 하네스.

## 구조

```
.cursor/
├── agents/
│   ├── literature-searcher.md
│   ├── note-taker.md
│   ├── critic-synthesizer.md
│   ├── reference-manager.md
│   └── research-coordinator.md
├── skills/
│   ├── research-assistant/
│   │   └── skill.md              — 오케스트레이터
│   ├── systematic-review-protocol/
│   │   └── skill.md              — 체계적 문헌 고찰 (PRISMA, PICO, Boolean 검색)
│   └── citation-formatter/
│       └── skill.md              — 인용 형식 변환 (APA/MLA/Chicago, BibTeX)
└── CURSOR.md                     — 이 파일
```

## 사용법

Cursor 채팅에서 자연어 요청으로 실행하거나, `/research-assistant`로 수동 호출하거나, `@.cursor/skills/research-assistant/skill.md`를 컨텍스트로 첨부해 실행한다.
