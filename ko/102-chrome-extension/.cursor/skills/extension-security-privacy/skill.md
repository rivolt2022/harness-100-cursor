---
name: extension-security-privacy
description: "크롬 익스텐션 보안·개인정보·최소 권한 가이드. CSP, optional_permissions, 메시지 검증, HTTPS. '권한 최소화', '익스텐션 보안', 'CSP', '개인정보 처리방침' 요청에 사용한다."
---

# Extension Security & Privacy

권한 과다 요청은 **Web Store 심사 지연·거절의 1순위 원인**이다. 최소 권한 + 명확한 정당화가 출시 속도를 결정한다.

## 최소 권한 의사결정 트리

```
현재 탭만 사용자 클릭 시 필요?
  → YES: activeTab (host_permissions 없이 가능한 경우 많음)
  → NO: 구체적 host_permissions (와일드카드 최소화)

tab.url / tab.title 필요?
  → YES: tabs 권한 (없으면 tab.url은 undefined, 에러 없음)

모든 사이트?
  → 피하기. <all_urls> / https://*/* 는 수동 심사·전환율 하락

부가 기능만 필요?
  → optional_permissions + runtime request
```

## 권한 패턴

```json
{
  "permissions": ["storage", "activeTab"],
  "optional_permissions": ["tabs", "scripting"],
  "host_permissions": ["https://mail.google.com/*"]
}
```

```javascript
// 런타임 권한 요청
const granted = await chrome.permissions.request({
  permissions: ['tabs'],
  origins: ['https://calendar.google.com/*']
});
```

## Content Security Policy

Extension pages(popup, options) 기본: **inline script 금지**.

- 모든 JS는 별도 `.js` 파일
- `eval`, `new Function` 금지 (sandbox 페이지 예외)
- 필요 시 `'wasm-unsafe-eval'`만 최소 추가

## 메시지 보안

```javascript
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  // sender 검증
  if (!sender.id || sender.id !== chrome.runtime.id) {
    // 외부 — runtime.onMessageExternal + 화이트리스트
    return;
  }
  // 입력 검증
  if (typeof message?.type !== 'string') return;
  // ...
});
```

`externally_connectable`은 신뢰 도메인만 명시.

## 네트워크·데이터

- API 호출은 **HTTPS**만
- 민감 데이터는 extension storage에 평문 장기 보관 지양
- 서버 전송 시 목적·보관 기간을 개인정보 처리방침에 명시
- `web_accessible_resources` 최소화 — 사이트가 익스텐션 리소스 탐지 가능

## 개인정보 처리 (Chrome 정책)

데이터 수집·전송 시:
- [ ] 개인정보 처리방침 URL (스토어 필수)
- [ ] 수집 항목, 목적, 보관, 제3자 공유 여부
- [ ] 미래용 권한 선요청 금지 — 기능 출시 시점에 요청

## 심사 리스크 권한

| 권한 | 리스크 | 완화 |
|------|--------|------|
| `<all_urls>` host | 매우 높음 | 도메인 한정 + 스토어 설명 |
| `webRequest` (non-blocking) | 높음 | DNR 우선 |
| `cookies` | 높음 | 필요 도메인만 |
| `history` | 매우 높음 | 대체 설계 검토 |
| `debugger` | 매우 높음 | 개발 빌드만 |

## 코드 품질 (심사)

- 난독화 코드 지양 — 리뷰 거절·지연
- 소스와 제출 ZIP 일치
- 사용하지 않는 permission/manifest 키 제거

## 체크리스트 (reviewer 연동)

- [ ] manifest permissions = 실제 사용 API만
- [ ] host_permissions 구체적 도메인
- [ ] optional_permissions로 progressive disclosure
- [ ] CSP 위반 없음 (inline 없음)
- [ ] onMessage 입력 검증
- [ ] 개인정보 처리방침 (데이터 접근 시)
