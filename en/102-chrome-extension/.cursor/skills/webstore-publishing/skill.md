---
name: webstore-publishing
description: "Chrome Web Store release, review, rejection response, CHROMEWEBSTORE.md, permission justification, and privacy policy guide. Use for 'Web Store release', 'extension review', 'review rejection' requests."
---

# Web Store Publishing

Store submission rests on three pillars: **code ZIP + dashboard metadata + policy compliance**. Collect copy-paste content in `CHROMEWEBSTORE.md` to avoid deadline scrambles.

## CHROMEWEBSTORE.md Template

Project root or `_workspace/CHROMEWEBSTORE.md`:

```markdown
# Chrome Web Store Listing

## Basic Info
- **Name** (max 45 chars):
- **Short description** (132 chars):
- **Detailed description**:
- **Category**:
- **Language**:

## Graphics
- Icon 128×128
- Screenshots 1280×800 (min 1, recommended 3–5)
- Promo tile (optional)

## Privacy
- **Privacy policy URL** (required when data is accessed):
- Data collected:
- Purpose of use:
- Third-party transmission:

## Permission Justification
| Permission | Reason for use (English recommended) |
|------------|--------------------------------------|
| storage | Save user preferences locally |
| activeTab | Read page content when user clicks the extension icon |

## Review Notes (private)
- Test account:
- Repro steps 1, 2, 3:

## Version
- version: 1.0.0
- Changelog:
```

## Review Process Summary

1. Register developer account (one-time fee)
2. Upload ZIP (manifest at root, exclude unnecessary files)
3. Store listing + privacy policy
4. Automated + manual review (broad host / sensitive permissions extend manual review)
5. On rejection, fix policy violations and resubmit

## Frequent Rejection Causes

| Cause | Response |
|-------|----------|
| Excessive host_permissions | narrow domains, activeTab |
| Unused permissions | clean manifest |
| Obfuscated code | submit readable source |
| Missing privacy policy | add URL, list collected items |
| Unclear single purpose | clarify in description and screenshots |
| Remote code | bundle all logic locally |

## Permission Justification Tips

- One sentence from the **user perspective** on why it is needed
- For broad access, **specific use case** + explain alternatives considered
- For optional permissions, state "requested only when user enables the feature"

## Submission ZIP Checklist

- [ ] `manifest_version: 3`
- [ ] exclude node_modules (build output only)
- [ ] .map file policy (whether to submit source maps)
- [ ] icon files exist or field omitted
- [ ] bump version (`version` in manifest)

## Update Strategy

- **Patch**: bug fixes
- **Minor**: new features — update justification when adding permissions
- Previously rejected permissions trigger re-review — note in changelog

## Single Purpose

The extension must read as **one clear purpose** across listing, UI, and permissions. Split ancillary features into optional flows.

## Reviewer Handoff

After extension-reviewer Go in `05_extension_review.md`:
- Finalize CHROMEWEBSTORE.md draft
- English justification draft
- Screenshot capture scenario list
