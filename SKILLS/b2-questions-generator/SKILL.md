---
name: b2-questions-generator
description: Générer questions brutes pool par pool depuis feuille POOLS du xlsx
version: 2.0
status: ACTIVE
---

# B2 — QUESTIONS GENERATOR

**Input:** QUIZ_[THEME].xlsx (feuilles POOLS + ANGLES + ITEMS validées — gate A4)
**Output:** QUIZ_[THEME].xlsx feuille QUESTIONS peuplée (STATUT_B2 = SOUMIS)

## PROCESS

| Étape | Action | Vérification |
|-------|--------|--------------|
| 1 | Lire POOL_ID / TYPE / CIBLE_NIVEAU / STOCK_CIBLE depuis feuille POOLS | Gate A4 passée |
| 2 | Lire angles disponibles depuis feuille ANGLES (POOL_CIBLE = ce pool) | Angles assignés |
| 3 | Générer N candidates (3× stock cible) | Sourced feuille ITEMS |
| 4 | Appliquer filtres rédaction RULE-B2-HB-002 | 8 filtres obligatoires |
| 5 | Assigner difficulté CIBLE_NIVEAU (top-down depuis POSITION_QUIZ) | N1/N2/N3 |
| 6 | Remplir feuille QUESTIONS — STATUT_B2 = SOUMIS | Pool terminé |

## TYPES DE QUESTIONS

| TYPE | Description |
|------|-------------|
| 1 | Identification — "Quel [ENTITÉ]..." |
| 2 | Nombres — "Combien de..." |
| 3 | Années — "Quelle [PÉRIODE]..." |
| 4 | Localisation — "Quel [LIEU]..." |
| 5 | Correspondance — association [ENTITÉ A] / [ENTITÉ B] |

## KEY RULES

- [RULE-B2-001] Format strict : énoncé + réponse correcte obligatoires
- [RULE-B2-002] 1 seule bonne réponse incontestable
- [RULE-B2-003] Pas de distracteurs en B2 (ajoutés en B3)
- [RULE-B2-004] Pool par pool — jamais global
- [RULE-B2-005] Longueur : TARGET 6–9 mots / ACCEPTABLE 10–14 mots / FAIL ≥16 mots
- Source règles complètes : STD_B2_generation_rules.md

---

*v2.0 — 2026-05-22 — Pipeline V2 (remplace v1.0 : A4_POOLS.txt / A3_BIPREGEN)*
