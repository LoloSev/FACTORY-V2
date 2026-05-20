---
name: b6-rules-extractor
description: Extraire règles généralisables depuis cobaye, alimenter glossaire FACTORY
version: 1.0
status: ACTIVE
---

# B6 — RULES EXTRACTOR

**Input:** B5_AUDIT complete + PROCESS_BIB + all decisions  
**Output:** B6_RULES_EXTRACTED.md + B6_EDGE_CASES.md + STD_updates

## PROCESS

| Étape | Action | Output |
|-------|--------|--------|
| 1 | Analyser décisions B5 patterns | Patterns identifiés |
| 2 | Extraire règles implicites | [RULE-X-Y] candidates |
| 3 | Identifier edge cases | B6_EDGE_CASES.md |
| 4 | Évaluer généralisabilité | Applicabilité > 1 thème ? |
| 5 | Proposer glossaire updates | [DEF-X-Y] + [RULE-X-Y] |
| 6 | Output B6_RULES_EXTRACTED | Prêt pour promotion |

## OUTPUTS

**B6_RULES_EXTRACTED.md:**
- [RULE-X-Y] extracted from audit decisions
- Contexte: quand applicable
- Rationale: pourquoi

**B6_EDGE_CASES.md:**
- Cas limites rencontrés
- Exceptions à règle générale
- Solutions appliquées

**STD_updates (glossaire):**
- Nouvelles [DEF-] entries
- Nouvelles [RULE-] à ajouter
- Transversal rules si applicable

## KEY RULES

- [RULE-B6-001] Règles = généralisables (multi-thème)
- [RULE-B6-002] Edge cases documentés séparément
- [RULE-B6-003] Patterns validés ≥1 cobaye avant promotion
- [RULE-B6-004] Glossaire centralise vérité (source unique)

---

*v1.0 — 2026-05-17*
