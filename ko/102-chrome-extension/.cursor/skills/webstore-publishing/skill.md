---
name: webstore-publishing
description: "Chrome Web Store 출시·심사·거절 대응·CHROMEWEBSTORE.md·권한 정당화·개인정보 처리방침 가이드. '웹스토어 출시', '익스텐션 심사', 'review rejection' 요청에 사용한다."
---

# Web Store Publishing

스토어 제출은 **코드 ZIP + 대시보드 메타 + 정책 준수** 세 축이다. `CHROMEWEBSTORE.md`에 복붙용 내용을 모아 마감 시 스크램블을 방지한다.

## CHROMEWEBSTORE.md 템플릿

프로젝트 루트 또는 `_workspace/CHROMEWEBSTORE.md`:

```markdown
# Chrome Web Store Listing

## 기본 정보
- **이름** (45자 이내):
- **짧은 설명** (132자):
- **상세 설명**:
- **카테고리**:
- **언어**:

## 그래픽
- 아이콘 128×128
- 스크린샷 1280×800 (최소 1, 권장 3~5)
- 프로모 타일 (선택)

## 개인정보
- **개인정보 처리방침 URL** (필수 — 데이터 접근 시):
- 수집 데이터:
- 사용 목적:
- 제3자 전송:

## 권한 정당화 (Permission justification)
| 권한 | 사용 이유 (영문 권장) |
|------|----------------------|
| storage | Save user preferences locally |
| activeTab | Read page content when user clicks the extension icon |

## 심사용 메모 (비공개)
- 테스트 계정:
- 재현 단계 1,2,3:

## 버전
- version: 1.0.0
- 변경 로그:
```

## 심사 프로세스 요약

1. 개발자 계정 등록 (일회성 등록비)
2. ZIP 업로드 (manifest 루트, 불필요 파일 제외)
3. 스토어 listing + privacy policy
4. 자동 + 수동 리뷰 (broad host·민감 권한은 수동 심사 길어짐)
5. 거절 시 정책 위반 항목 수정 후 재제출

## 거절 빈도 높은 원인

| 원인 | 대응 |
|------|------|
| 과도한 host_permissions | 도메인 축소, activeTab |
| 권한 미사용 | manifest 정리 |
| 난독화 코드 | readable source 제출 |
| 개인정보 처리방침 누락 | URL 추가, 수집 항목 명시 |
| 단일 목적 불명확 | 설명·스크린샷으로 기능 명확화 |
| 원격 코드 | 모든 로직 번들 내 포함 |

## 권한 정당화 작성 팁

- **사용자 관점**으로 "왜 필요한지" 한 문장
- broad access는 **구체적 사용 사례** + 대안 검토 설명
- optional permission은 "사용자가 기능 활성화 시에만 요청" 명시

## 제출 ZIP 체크리스트

- [ ] `manifest_version: 3`
- [ ] node_modules 제외 (빌드 산출물만)
- [ ] .map 파일 정책 확인 (소스맵 제출 여부)
- [ ] 아이콘 파일 실존 또는 생략
- [ ] 버전号 증가 (`version` in manifest)

## 업데이트 전략

- **Patch**: 버그 수정
- **Minor**: 기능 추가 — 새 권한 시 justification 업데이트
- 거절 이력 권한은 재심사 트리거 — changelog에 명시

## 단일 목적 (Single Purpose)

익스텐션이 하는 일이 listing·UI·권한과 **하나의 명확한 목적**으로 읽혀야 한다. 부가 기능은 optional로 분리.

## reviewer 핸드오프

extension-reviewer가 `05_extension_review.md`에서 Go 판단 후:
- CHROMEWEBSTORE.md 초안 완성
- justification 영문 초안
- 스크린샷 촬영 시나리오 목록
