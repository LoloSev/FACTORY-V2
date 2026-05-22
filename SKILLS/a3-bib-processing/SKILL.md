---
name: a3-bib-processing
description: Traiter BIB → feuilles ITEMS + ANGLES du xlsx (Pipeline V2)
version: 2.0
status: ACTIVE
---

# A3 — BIB PROCESSING

**Input:** A2_BIB_[THEME]_[N].txt
**Output:** QUIZ_[THEME].xlsx (feuilles CONFIG + ITEMS + ANGLES peuplées) + A3_01_PROCESS_BIB_[THEME].md

## PROCESS

| Étape | Input | Output | Règle |
|-------|-------|--------|-------|
| 1 | BIB items | Codage [THEME]-[CAT]-[NNN]-[NIV] | [RULE-A3-001] |
| 2 | Codes items | Normalisation niveaux → N1/N2/N3 | [RULE-A3-002] |
| 3 | Items normalisés | Feuille ITEMS du xlsx | [RULE-A3-003] |
| 4 | ITEMS | Angles interrogeables + exclusions inter-items | [RULE-A3-004] |
| 5 | Angles | Feuille ANGLES du xlsx (POOL_CIBLE vide — rempli en A4) | [RULE-A3-005] |
| 6 | Décisions | A3_01_PROCESS_BIB (AVANT/APRÈS/RAISON) | [RULE-A3-006] |

## KEY RULES

- [RULE-A3-001] Codage stable et immutable après création
- [RULE-A3-002] Niveaux : N1 (facile), N2 (moyen), N3 (difficile)
- [RULE-A3-003] Feuille ITEMS = source data propre pour A4 et B2
- [RULE-A3-004] Angles = angles interrogeables par item (dans feuille ANGLES)
- [RULE-A3-005] POOL_CIBLE et STATUT remplis en A4, pas en A3
- [RULE-A3-006] PROCESS_BIB = traçabilité de toutes les décisions humaines

---

*v2.0 — 2026-05-22 — Pipeline V2 (remplace v1.0 : BIPREGEN.txt / ANGIPREGEN.txt)*
