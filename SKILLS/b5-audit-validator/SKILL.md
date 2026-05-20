---
name: b5-audit-validator
description: Audit humain + IA questions, validation détaillée, traçabilité décisions
version: 1.0
status: ACTIVE
---

# B5 — AUDIT VALIDATOR

**Input:** B4_TABLEUR vN.xlsx  
**Output:** B5_TABLEUR_WIP.xlsx (avec audit), B5_AUDIT_LOG.md, B5_QA_REPORT.md

## PROCESS (One Question At A Time)

| Étape | Action | Decision |
|-------|--------|----------|
| 1 | Présenter Q seul | — |
| 2 | Valider énoncé (10w max, lisible) | Evaluate |
| 3 | Valider réponse (incontestable) | Evaluate |
| 4 | Valider distractors (crédibles, pas fictif) | Evaluate |
| 5 | Valider format cohérent | Evaluate |
| 6 | Décider | CONSERVER / MODIFIER / REJETER |
| 7 | Tracer decision + raison | Log |

## DECISION OPTIONS

| Decision | Action | Log |
|----------|--------|-----|
| CONSERVER | Keep as-is | Raison conservation |
| MODIFIER | Fix specific issue | Version orig + modifiée + raison |
| REJETER | Remove Q | Raison rejet |
| DÉPLACER | Move to autre pool | Pool destination |

## KEY RULES

- [RULE-B5-001] Une question à la fois (jamais batch)
- [RULE-B5-002] Attendre validation humaine avant suivant
- [RULE-B5-003] Faux distractor = validation humaine obligatoire
- [RULE-B5-004] Tracer AVANT/APRÈS/RAISON obligatoire
- [RULE-B5-005] QA_STATUS assigné (PASS/WARNING/FAIL)

## QA_STATUS VALUES

- PASS = Prêt B6
- WARNING = Audit flagged, review avant export
- FAIL = Bloque export

---

*v1.0 — 2026-05-17*
