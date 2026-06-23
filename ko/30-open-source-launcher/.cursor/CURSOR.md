# Open Source Launcher Harness

오픈소스 프로젝트 런칭의 코드정리→문서→라이선스→커뮤니티 구축을 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```
.cursor/
├── agents/
│   ├── code-organizer.md        — 코드 정리자 (구조재편, 리팩토링, 코드표준)
│   ├── doc-writer.md            — 문서 작성자 (README, 기여가이드, API문서, 튜토리얼)
│   ├── license-specialist.md    — 라이선스 전문가 (라이선스선정, 호환성, 법적검토)
│   ├── community-manager.md     — 커뮤니티 매니저 (거버넌스, CoC, 이슈템플릿, CI/CD)
│   └── launch-reviewer.md       — 런칭 리뷰어 (교차검증, 런칭준비도, 최종체크리스트)
├── skills/
│   ├── open-source-launcher/
│   │   └── skill.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── license-compatibility-matrix/
│   │   └── skill.md              — 오픈소스 라이선스 호환성 가이드
│   └── community-health-metrics/
│       └── skill.md              — 오픈소스 커뮤니티 건강도 가이드
└── CURSOR.md                    — 이 파일
```

## 사용법

Cursor 채팅에서 자연어 요청으로 실행하거나, `/open-source-launcher`로 수동 호출하거나, `@.cursor/skills/open-source-launcher/skill.md`를 컨텍스트로 첨부해 실행한다.
## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_code_organization.md` — 코드 정리 계획 및 결과
- `02_documentation.md` — 문서 패키지 (README, 가이드 등)
- `03_license_review.md` — 라이선스 검토 및 선정
- `04_community_setup.md` — 커뮤니티 구성 및 거버넌스
- `05_launch_report.md` — 런칭 리뷰 보고서
- `generated_files/` — 생성된 파일들 (README, LICENSE, CONTRIBUTING 등)
