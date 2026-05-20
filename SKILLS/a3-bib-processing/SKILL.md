---
name: a3-bib-processing
description: Traiter BIB → BIPREGEN (normalisé) + ANGIPREGEN (angles + quotas)
version: 1.0
status: ACTIVE
---

# A3 — BIB PROCESSING

**Input:** A2_BIB (brut)  
**Output:** A3_BIPREGEN + A3_ANGIPREGEN + A3_PROCESS_BIB (traçabilité)

## PROCESS

| Étape | Input | Output | Rules |
|-------|-------|--------|-------|
| 1 | BIB items | Codage [THEME]-[CAT]-[NNN]-[NIV] | [RULE-A3-001] |
| 2 | Codes items | Normalisation niveaux (1-5 → N1/N2/N3) | [RULE-A3-002] |
| 3 | Normalisé | BIPREGEN + stats + index | [RULE-A3-003] |
| 4 | BIPREGEN | Angles interrogeables + exclusions | [RULE-A3-004] |
| 5 | Angles | ANGIPREGEN + quotas | [RULE-A3-005] |
| 6 | Decisions | PROCESS_BIB (AVANT/APRES/RAISON) | [RULE-A3-006] |

## KEY RULES

- [RULE-A3-001] Codage stable, immutable après création
- [RULE-A3-002] Niveaux: N1 (facile), N2 (moyen), N3 (difficile)
- [RULE-A3-003] BIPREGEN = source data propre pour B2
- [RULE-A3-004] Angles = angles interrogeables per item
- [RULE-A3-005] Quotas = nombre questions/angle cible
- [RULE-A3-006] PROCESS_BIB = traçabilité décisions humaines

---

*v1.0 — 2026-05-17*
