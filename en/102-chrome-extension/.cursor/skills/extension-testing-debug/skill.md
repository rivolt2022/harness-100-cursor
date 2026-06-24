---
name: extension-testing-debug
description: "MV3 extension testing and debugging guide. cold-start, service worker logs, messaging and permission scenarios. Use for 'extension debugging', 'service worker not working', 'extension testing' requests."
---

# Extension Testing & Debug

Most MV3 bugs come from **cold-start** and **messaging/permissions**. Pass mandatory scenarios before release.

## Local Load

1. `chrome://extensions` → Developer mode
2. "Load unpacked" → `extension/` folder
3. Service worker "Inspect" → DevTools Console
4. Popup → right-click Inspect

## Cold-Start Test (Required)

```
1. Disable extension → re-enable
2. Open popup while service worker is "inactive"
3. Run all core features once
4. Wait 30s+ for SW termination → run features again
```

On failure: add init logic that recovers state from storage.

## Scenario Matrix

| # | Scenario | Expected |
|---|----------|----------|
| 1 | First install onInstalled | default settings, context menu, etc. |
| 2 | Browser restart onStartup | state recovery |
| 3 | popup → background → content | message round-trip |
| 4 | tab without permission | graceful error UI |
| 5 | optional permission denied | feature disabled + guidance |
| 6 | CSP-violating page | content affected only, SW OK |
| 7 | multiple tabs | correct tabId |
| 8 | MV3 alarm fires | chrome.alarms |

## Debugging Cheat Sheet

| Symptom | Where to check |
|---------|----------------|
| SW logs | chrome://extensions → service worker inspect |
| Content logs | tab DevTools Console |
| Popup logs | popup right-click inspect |
| Message failure | SW console + `return true` |
| Permissions | manifest vs `chrome.permissions.contains` |
| DNR | `chrome.declarativeNetRequest.getMatchedRules` |

## Force Service Worker Wake (Test)

```javascript
await chrome.runtime.getPlatformInfo(); // or storage read
```

For testing only — production should be event-driven.

## Automation (Optional)

- **Vitest + jsdom**: pure logic, messaging wrapper
- **Puppeteer + --load-extension**: E2E (heavy in CI)
- **WXT / Plasmo**: HMR for faster dev (build tool choice)

Minimum: message-contract unit tests + manual cold-start.

## Performance

- Content script: `document_idle`, chunk DOM work with `requestIdleCallback`
- SW: delegate heavy work to offscreen or content
- storage: batch frequent read/write

## Deliverable

Test results table in `_workspace/05_extension_review.md`:

| Scenario | Result | Notes |
|----------|--------|-------|
| cold-start | ✅/❌ | |

On 🔴 failure, rework via owning component agent.
