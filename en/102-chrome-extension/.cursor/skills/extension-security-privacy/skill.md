---
name: extension-security-privacy
description: "Chrome extension security, privacy, and least-privilege guide. CSP, optional_permissions, message validation, HTTPS. Use for 'minimize permissions', 'extension security', 'CSP', 'privacy policy' requests."
---

# Extension Security & Privacy

Over-requesting permissions is the **#1 cause of Web Store review delays and rejections**. Least privilege + clear justification determines release velocity.

## Least-Privilege Decision Tree

```
Need current tab only on user click?
  → YES: activeTab (often works without host_permissions)
  → NO: specific host_permissions (minimize wildcards)

Need tab.url / tab.title?
  → YES: tabs permission (without it tab.url is undefined, no error)

All sites?
  → Avoid. <all_urls> / https://*/* triggers manual review and lower conversion

Only for optional features?
  → optional_permissions + runtime request
```

## Permission Patterns

```json
{
  "permissions": ["storage", "activeTab"],
  "optional_permissions": ["tabs", "scripting"],
  "host_permissions": ["https://mail.google.com/*"]
}
```

```javascript
// Runtime permission request
const granted = await chrome.permissions.request({
  permissions: ['tabs'],
  origins: ['https://calendar.google.com/*']
});
```

## Content Security Policy

Extension pages (popup, options) default: **no inline scripts**.

- All JS in separate `.js` files
- No `eval`, `new Function` (sandbox page exception)
- Add `'wasm-unsafe-eval'` only when minimally needed

## Message Security

```javascript
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  // Validate sender
  if (!sender.id || sender.id !== chrome.runtime.id) {
    // External — runtime.onMessageExternal + whitelist
    return;
  }
  // Validate input
  if (typeof message?.type !== 'string') return;
  // ...
});
```

`externally_connectable` — trusted domains only.

## Network & Data

- API calls over **HTTPS** only
- Avoid long-term plaintext storage of sensitive data in extension storage
- When sending to servers, state purpose and retention in privacy policy
- Minimize `web_accessible_resources` — sites can detect extension resources

## Privacy (Chrome Policy)

When collecting or transmitting data:
- [ ] Privacy policy URL (required for store when data is accessed)
- [ ] Collected items, purpose, retention, third-party sharing
- [ ] No pre-requesting permissions for future features — request at feature launch

## High-Risk Permissions

| Permission | Risk | Mitigation |
|------------|------|------------|
| `<all_urls>` host | very high | domain scope + store description |
| `webRequest` (non-blocking) | high | prefer DNR |
| `cookies` | high | required domains only |
| `history` | very high | consider alternative design |
| `debugger` | very high | dev builds only |

## Code Quality (Review)

- Avoid obfuscated code — review rejection and delays
- Submitted ZIP matches source
- Remove unused permission/manifest keys

## Checklist (reviewer integration)

- [ ] manifest permissions = only APIs actually used
- [ ] host_permissions on specific domains
- [ ] progressive disclosure via optional_permissions
- [ ] no CSP violations (no inline)
- [ ] onMessage input validation
- [ ] privacy policy (when data is accessed)
