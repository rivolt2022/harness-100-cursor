---
name: extension-testing-debug
description: "MV3 익스텐션 테스트·디버깅 가이드. cold-start, service worker 로그, 메시지·권한 시나리오. '익스텐션 디버깅', 'service worker 안 됨', '익스텐션 테스트' 요청에 사용한다."
---

# Extension Testing & Debug

MV3 버그의 대부분은 **cold-start**와 **메시지/권한**에서 발생한다. 배포 전 필수 시나리오를 통과해야 한다.

## 로컬 로드

1. `chrome://extensions` → 개발자 모드
2. "압축해제된 확장 프로그램 로드" → `extension/` 폴더
3. Service worker "검사" → DevTools Console
4. Popup → 우클릭 검사

## Cold-Start 테스트 (필수)

```
1. 익스텐션 비활성화 → 재활성화
2. Service worker "inactive" 상태에서 popup 열기
3. 모든 핵심 기능 1회 실행
4. 30초+ 대기 후 SW 종료 확인 → 다시 기능 실행
```

실패 시: storage에서 상태 복구하는 init 로직 추가.

## 시나리오 매트릭스

| # | 시나리오 | 기대 |
|---|----------|------|
| 1 | 최초 설치 onInstalled | 기본 설정, context menu 등 |
| 2 | 브라우저 재시작 onStartup | 상태 복구 |
| 3 | popup → background → content | 메시지 왕복 |
| 4 | 권한 없는 탭 | graceful error UI |
| 5 | optional permission 거부 | 기능 비활성 + 안내 |
| 6 | CSP 위반 페이지 | content만 영향, SW 정상 |
| 7 | 다중 탭 | 올바른 tabId |
| 8 | MV3 alarm 발화 | chrome.alarms |

## 디버깅 치트시트

| 증상 | 확인 위치 |
|------|----------|
| SW 로그 | chrome://extensions → service worker inspect |
| Content 로그 | 해당 탭 DevTools Console |
| Popup 로그 | popup 우클릭 검사 |
| 메시지 실패 | SW console + `return true` |
| 권한 | manifest vs `chrome.permissions.contains` |
| DNR | `chrome.declarativeNetRequest.getMatchedRules` |

## Service Worker 강제 깨우기

```javascript
await chrome.runtime.getPlatformInfo(); // 또는 storage read
```

테스트용 — 프로덕션에서는 이벤트 기반만.

## 자동화 (선택)

- **Vitest + jsdom**: pure logic, messaging 래퍼
- **Puppeteer + --load-extension**: E2E (CI 무거움)
- **WXT / Plasmo**: HMR로 개발 속도 향상 (빌드 도구 선택)

최소한: message-contract 단위 테스트 + 수동 cold-start.

## 성능

- Content script: `document_idle`, DOM 작업 청크·`requestIdleCallback`
- SW: 무거운 work는 offscreen 또는 content에 위임
- storage: 빈번한 read/write 배치

## 산출물

`_workspace/05_extension_review.md`에 테스트 결과 표:

| 시나리오 | 결과 | 비고 |
|----------|------|------|
| cold-start | ✅/❌ | |

🔴 실패 시 해당 컴포넌트 에이전트에 재작업.
