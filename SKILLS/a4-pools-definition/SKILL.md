---
name: a4-pools-definition
description: Définir 20 pools opérationnels (IF-SF, IF-ROT, QV) avec assignations angles/quotas
version: 1.0
status: ACTIVE
---

# A4 — POOLS DEFINITION

**Input:** A3_ANGIPREGEN  
**Output:** A4_POOLS_[THEME].txt (20 pools structurés)

## POOLS ARCHITECTURE

| Bloc | Type | Pools | Questions | Rotation | Role |
|------|------|-------|-----------|----------|------|
| 1 | IF-SF | 2 | 8 total | Très lente | Identité quiz |
| 2 | IF-ROT | 3 | 12 total | Lente | Onboarding fluide |
| 3 | QV | 15 | 15 total | Rapide | Variété maximale |
| **TOTAL** | — | **20** | **20/partie** | — | 1 Q/pool |

## PROCESS

| Étape | Action |
|-------|--------|
| 1 | Décider stratégie bloc (IF-SF vs IF-ROT vs QV) |
| 2 | Assigner angles ANGIPREGEN → pools |
| 3 | Vérifier coverage (tous angles assignés) |
| 4 | Définir quotas (questions/pool) |
| 5 | Output A4_POOLS_[THEME].txt |

## KEY RULES

- [RULE-A4-001] Exactement 20 pools obligatoire
- [RULE-A4-002] Tous angles ANGIPREGEN assignés
- [RULE-A4-003] IF-SF = identité, IF-ROT = transition, QV = variété
- [RULE-A4-004] Collisions inter-pools interdites

---

*v1.0 — 2026-05-17*
