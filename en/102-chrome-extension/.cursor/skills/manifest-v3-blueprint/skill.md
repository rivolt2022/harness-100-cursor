---
name: manifest-v3-blueprint
description: "Manifest V3 structure, service worker lifecycle, manifest.json fields, DNR, and offscreen guide. Use for 'manifest v3', 'service worker', 'declarativeNetRequest', 'offscreen document' requests."
---

# Manifest V3 Blueprint

MV3 rests on four pillars: **manifest + service worker + content scripts + UI**. Components not declared in the manifest do not exist.

## manifest.json Skeleton

```json
{
  "manifest_version": 3,
  "name": "Extension Name",
  "version": "1.0.0",
  "description": "One-line description for store",
  "permissions": ["storage", "activeTab"],
  "optional_permissions": ["tabs"],
  "host_permissions": ["https://api.example.com/*"],
  "background": {
    "service_worker": "src/background/service-worker.js",
    "type": "module"
  },
  "action": {
    "default_popup": "src/popup/popup.html",
    "default_title": "Open"
  },
  "content_scripts": [{
    "matches": ["https://*.example.com/*"],
    "js": ["src/content/main.js"],
    "run_at": "document_idle"
  }],
  "content_security_policy": {
    "extension_pages": "script-src 'self'; object-src 'self'"
  }
}
```

## Service Worker Lifecycle

| Property | Implication |
|----------|-------------|
| idle ~30s then terminate | global variable state is lost |
| restarts on events | recover from storage on every cold-start |
| no DOM | cannot use `window`/`document` |
| `setInterval` discouraged | `chrome.alarms` (watch min period) |

### Idempotent Initialization Pattern

```javascript
// src/background/service-worker.js
async function initialize() {
  const { initialized } = await chrome.storage.session.get('initialized');
  if (initialized) return;
  await setupListeners();
  await chrome.storage.session.set({ initialized: true });
}

chrome.runtime.onInstalled.addListener(initialize);
chrome.runtime.onStartup.addListener(initialize);
initialize();
```

## Storage Selection

| API | Purpose | Persistence |
|-----|---------|-------------|
| `chrome.storage.session` | queues, temporary session | browser session |
| `chrome.storage.local` | user settings | disk |
| `chrome.storage.sync` | synced settings (small) | account sync |

Always use `await`. Consider queue/lock pattern for concurrent writes.

## UI Component Declaration

| UI | manifest | Required trigger |
|----|----------|------------------|
| Popup | `action.default_popup` | icon click |
| Side panel | `side_panel.default_path` | `onClicked` or `setPanelBehavior` |
| Options | `options_ui.page` | user opens settings |
| Omnibox | `omnibox.keyword` | address bar keyword |

**Side panel note**: `default_path` alone does not open the panel. When combined with popup, call `chrome.sidePanel.open()` from a popup button.

## Icons

```json
// ✅ Real PNG per size (16×16, 48×48, 128×128)
"icons": {
  "16": "icons/icon-16.png",
  "48": "icons/icon-48.png",
  "128": "icons/icon-128.png"
}
// ✅ Or omit icons field — Chrome default icon
```

Never reference files that do not exist.

## Declarative Net Request (DNR)

Replaces blocking `webRequest`. Rules are JSON/static ruleset.

```json
"declarative_net_request": {
  "rule_resources": [{
    "id": "ruleset_1",
    "enabled": true,
    "path": "rules/rules.json"
  }]
}
```

Dynamic rules: `chrome.declarativeNetRequest.updateDynamicRules`.

## Offscreen Document

When DOM is needed but unavailable in the SW (e.g. clipboard, audio parse):

```javascript
await chrome.offscreen.createDocument({
  url: 'offscreen.html',
  reasons: ['DOM_PARSER'],
  justification: 'Parse HTML off main thread'
});
```

Close with `chrome.offscreen.closeDocument()` when done.

## MV2 → MV3 Migration Checklist

- [ ] `background.scripts` → `service_worker` (single file or import)
- [ ] `browser_action` → `action`
- [ ] `web_accessible_resources` array → `{ resources, matches }` object
- [ ] CSP string → `content_security_policy` object
- [ ] blocking webRequest → DNR
- [ ] global state → storage
- [ ] repeating setTimeout → alarms

## web_accessible_resources

Accessible from the web — **minimize**. Restrict with `matches` when needed.

```json
"web_accessible_resources": [{
  "resources": ["injected.css"],
  "matches": ["https://*.example.com/*"]
}]
```
