---
name: leaderboard-strategy
description: "대회 리더보드 운영 전략. public/private split, shake-up 대응, 제출 슬롯 운영, 리스크 분산을 다룬다."
---

# Leaderboard Strategy

## 목적
- public LB 과적합을 방지하고 private LB 리스크를 관리한다.

## 핵심 체크리스트
- public-private score delta 추적
- single best 대신 diversified ensemble 포트폴리오 유지
- 제출 슬롯을 탐색/활용(Explore/Exploit)으로 분리
- 최종 제출 후보 2~3개를 분산 보유
