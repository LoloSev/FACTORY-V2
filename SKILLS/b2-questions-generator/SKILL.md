---
name: b2-questions-generator
description: Générer questions brutes (énoncé + réponse + type + difficulté) par pool
version: 1.0
status: ACTIVE
---

# B2 — QUESTIONS GENERATOR

**Input:** A4_POOLS + A3_BIPREGEN  
**Output:** 277 questions brutes (Q + R + TYPE + Difficulty)

## PROCESS

| Étape | Action | Check |
|-------|--------|-------|
| 1 | Charger pool | Quota clair |
| 2 | Générer N candidates (3× quota) | BIPREGEN sourced |
| 3 | Appliquer règles TYPE | [RULE-TYPE-X] |
| 4 | Filtrer qualité | <10 words, 1 bonne réponse |
| 5 | Assigner difficulté | N1/N2/N3 spacing |
| 6 | Output pool_done | 277 total |

## RULES (par TYPE)

| TYPE | Description | Example |
|------|-------------|---------|
| 1 | Identification | "Quel joueur..." |
| 2 | Nombres | "Combien de..." |
| 3 | Années | "Quelle année..." |
| 4 | Localisation | "Quel pays..." |
| 5 | Correspondance | "Assoc. joueur/feat..." |

## KEY RULES

- [RULE-B2-001] Format strict: Q/R obligatoire
- [RULE-B2-002] 1 bonne réponse incontestable
- [RULE-B2-003] Pas distracteurs (B3 après)
- [RULE-B2-004] Pas narratif complexe
- [RULE-B2-005] Pool par pool (jamais global)

---

*v1.0 — 2026-05-17*
