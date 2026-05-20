IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE


DEPENDENCY:
- MASTER_ARCHITECTURE.md
- glossaire_documentaire_factory.md
# QUIZ ASSEMBLY RULES

## Objectif

Garantir qu'une partie finale de 20 questions soit :
- variée
- fluide
- RATIO_VALIDATED
- rejouable
- sans collisions documentaires

---

## Structure fixe

Chaque quiz final contient :

- 2 IF-SF
- 3 IF-ROT
- 15 QV

Ordre recommandé :

```txt
IF-SF
QV
QV
IF-ROT
QV
QV
QV
IF-SF
QV
QV
IF-ROT
QV
QV
QV
QV
IF-ROT
QV
QV
QV
QV
```

---

## Règles d'équilibrage

### Joueurs

- Maximum 2 occurrences du même joueur majeur par partie
- Aucun joueur dans 2 questions consécutives
- Une question IF-SF sur un joueur interdit un QV immédiat sur le même joueur

---

### Finales / matchs

- Pas de deux finales consécutives
- Maximum 3 questions liées à une même édition cas source
RETEX_REF: RETEX_QUIZ_ASSEMBLY_RULES_001
- Une finale IF-SF interdit sa réutilisation dans les QV

---

### Nations

- Éviter plus de 3 questions d'affilée sur une même nation
- Répartir les grandes nations sur toute la partie

---

### Difficulty

Canonical distribution for 20 player-facing questions:

| Level | Volume | Ratio | Runtime role |
|---|---:|---:|---|
| N1 | 5 | 25% | onboarding_and_confidence |
| N2 | 10 | 50% | discovery_core |
| N3 | 5 | 25% | stimulating_final_elevation |

Rules:
- no more than 2 consecutive N3 questions
- accessible opening sequence
- progressive difficulty curve
- this distribution overrides any legacy 40/40/20 reference

---

## Règles anti-monotonie

Interdits :
- 3 questions biographies d'àffilée
- 3 scores/matchs d'àffilée
- 3 records d'àffilée
- répétition immédiate de formulation

Alterner :
- joueurs
- matchs
- records
- anecdotes
- nations
- époques

---

## Validation finale pipeline

Avant export final :

```txt
CHECK_DUPLICATES
CHECK_PLAYER_DENSITY
CHECK_DIFFICULTY_CURVE
CHECK_THEME_BALANCE
CHECK_POOL_COLLISIONS
CHECK_REPEAT_EDITIONS
```

---

## Philosophie

Une bonne partie ne dépend pas seulement :
- de bonnes questions

Mais surtout :
- d'un bon rythme
- d'une bonne alternance
- d'une variété documentaire maîtrisée


