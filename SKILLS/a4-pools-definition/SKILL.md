---
name: a4-pools-definition
description: Définir 20 pools opérationnels (IF/QV) avec assignations angles/quotas dans feuille POOLS du xlsx
version: 2.0
status: ACTIVE
---

# A4 — POOLS DEFINITION

**Input:** QUIZ_[THEME].xlsx (feuilles ITEMS + ANGLES validées — gate A3)
**Output:** feuille POOLS peuplée + feuille SOMMAIRE calculée

## POOLS ARCHITECTURE — TABLE DE DÉRIVATION POSITIONNELLE

| POSITION_QUIZ | TYPE | POOLS | STOCK_CIBLE | CIBLE_NIVEAU |
|---------------|------|-------|-------------|--------------|
| Q1–Q2 | IF | 2 | 8 | N1 |
| Q3–Q5 | IF | 3 | 12 | N1 |
| Q6–Q15 | QV | 10 | 15 | N2 |
| Q16–Q20 | QV | 5 | 15 | N3 |
| **TOTAL** | — | **20** | **277** | — |

Vérification : (2×8) + (3×12) + (10×15) + (5×15) = 277 ✓
Règle : les angles IF ne peuvent pas être assignés à un pool QV.

## PROCESS

| Étape | Action |
|-------|--------|
| 1 | Lire feuille ANGLES (POOL_CIBLE à assigner) |
| 2 | Créer 20 pools selon table de dérivation positionnelle |
| 3 | Assigner angles → pools (POOL_CIBLE + STATUT) |
| 4 | Vérifier coverage (tous angles assignés, pas de collision inter-pools) |
| 5 | Peupler feuille POOLS (POOL_ID, TYPE, POSITION_QUIZ, STOCK_CIBLE, CIBLE_NIVEAU) |
| 6 | Calculer feuille SOMMAIRE |

## KEY RULES

- [RULE-A4-001] Exactement 20 pools obligatoire
- [RULE-A4-002] Tous angles feuille ANGLES assignés à un POOL_CIBLE
- [RULE-A4-003] TYPE et STOCK_CIBLE dérivés automatiquement depuis POSITION_QUIZ — ne pas saisir manuellement
- [RULE-A4-004] Collisions inter-pools interdites (voir STD_GLOBAL_pool_collision_rules.md)
- [RULE-A4-005] Un angle IF ne peut pas être assigné à un pool QV

---

*v2.0 — 2026-05-22 — Pipeline V2 (remplace v1.0 : ANGIPREGEN/.txt/IF-SF/IF-ROT)*
