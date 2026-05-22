---
name: b4-spreadsheet-implantation
description: Implanter questions + distracteurs dans xlsx (A5 structure + B2 + B3 data)
version: 1.0
status: ARCHIVED
archived_date: 2026-05-22
archived_reason: Étape B4 supprimée en V2 — implantation intégrée dans QUIZ_[THEME].xlsx dès A3.
---

# B4 — SPREADSHEET IMPLANTATION

**Input:** A5_TABLEUR_[THEME]_INIT.xlsx + B2_questions + B3_distractors  
**Output:** B4_TABLEUR_[THEME]_vN.xlsx (semi-final)

## PROCESS

| Étape | Action |
|-------|--------|
| 1 | Load INIT.xlsx (structure vide) |
| 2 | Implanter B2 questions (énoncé) |
| 3 | Implanter réponse correcte |
| 4 | Implanter B3 distractors (A/B/C/D) |
| 5 | Mélanger réponse parmi 4 choix |
| 6 | Valider format cohérent |
| 7 | Output B4_TABLEUR_[THEME]_v1.xlsx |

## COLUMNS

| Col | Data | Source |
|-----|------|--------|
| Q | Question text | B2 |
| R | Correct answer | B2 |
| A/B/C/D | Choices (1 bonne + 3 distractors) | B3 |
| Type | 1-5 | B2 |
| Difficulty | N1/N2/N3 | B2 |
| QA_Status | PASS/WARNING/FAIL | Empty (B5) |

## KEY RULES

- [RULE-B4-001] Format QCM strict: Q/R/A/B/C/D
- [RULE-B4-002] Pas modification contenu (juste implantation)
- [RULE-B4-003] Mélanger réponse position random
- [RULE-B4-004] Version naming: v1, v2... (vN+1 per iteration)

---

*v1.0 — 2026-05-17*
