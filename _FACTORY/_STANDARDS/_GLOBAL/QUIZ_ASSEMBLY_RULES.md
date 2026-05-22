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

Chaque quiz final contient 20 questions dans l'ordre immuable suivant :

```txt
Q1  → IF  — N1
Q2  → IF  — N1
Q3  → IF  — N1
Q4  → IF  — N1
Q5  → IF  — N1
Q6  → QV  — N2
Q7  → QV  — N2
Q8  → QV  — N2
Q9  → QV  — N2
Q10 → QV  — N2
Q11 → QV  — N2
Q12 → QV  — N2
Q13 → QV  — N2
Q14 → QV  — N2
Q15 → QV  — N2
Q16 → QV  — N3
Q17 → QV  — N3
Q18 → QV  — N3
Q19 → QV  — N3
Q20 → QV  — N3
```

TYPE et CIBLE_NIVEAU sont dérivés automatiquement depuis POSITION_QUIZ — immuables.

---

## Règles d'équilibrage

### [ENTITE_PRIMAIRE]

- Maximum 2 occurrences de la même [ENTITE_PRIMAIRE] majeure par partie
- Aucune [ENTITE_PRIMAIRE] dans 2 questions consécutives
- Une question IF sur une [ENTITE_PRIMAIRE] interdit un QV immédiat sur la même [ENTITE_PRIMAIRE]

[EXEMPLE-ASSEMBLY-001 — cas source]
Application sur la ligne cas source (football) :
→ Maximum 2 occurrences du même joueur majeur par partie
→ Aucun joueur dans 2 questions consécutives
→ Une question IF sur un joueur interdit un QV immédiat sur le même joueur

---

### [CONTEXTE_EDITION]

- Pas de deux [CONTEXTE_EDITION] consécutifs
- Maximum 3 questions liées à un même [CONTEXTE_EDITION] du [CORPUS_ACTIF]
RETEX_REF: RETEX_QUIZ_ASSEMBLY_RULES_001
- Une réponse d'un pool IF interdit sa réutilisation dans les QV

[EXEMPLE-ASSEMBLY-002 — cas source]
Application sur la ligne cas source (football) :
→ Pas de deux finales consécutives
→ Maximum 3 questions liées à une même édition
→ Une finale IF interdit sa réutilisation dans les QV

---

### [CATEGORIE_GEOGRAPHIQUE]

- Éviter plus de 3 questions d'affilée sur une même [CATEGORIE_GEOGRAPHIQUE]
- Répartir les [ENTITES_GEOGRAPHIQUES] majeures sur toute la partie

[EXEMPLE-ASSEMBLY-003 — cas source]
Application sur la ligne cas source (football) :
→ Éviter plus de 3 questions d'affilée sur une même nation
→ Répartir les grandes nations sur toute la partie

---

### Difficulty

Distribution : → STD_GLOBAL_quiz_architecture_rules.md RULE-ARCH-006

Règles d'assemblage :
- pas plus de 2 questions N3 consécutives
- ouverture accessible (N1 en premier)
- courbe de difficulté progressive

---

## Règles anti-monotonie

Interdits :
- 3 questions [CATEGORIE_1] d'àffilée
- 3 questions [CATEGORIE_2] d'àffilée
- répétition immédiate de formulation

[EXEMPLE-ASSEMBLY-004 — cas source]
Application sur la ligne cas source (football) :
→ 3 questions biographies d'affilée
→ 3 scores/matchs d'affilée
→ 3 records d'affilée

Alterner les types d'angles disponibles dans le corpus actif.

---

## Validation finale pipeline

Avant export final :

```txt
CHECK_DUPLICATES
CHECK_ENTITY_DENSITY
CHECK_DIFFICULTY_CURVE
CHECK_THEME_BALANCE
CHECK_POOL_COLLISIONS
CHECK_REPEAT_CONTEXTS
```

---

## Philosophie

Une bonne partie ne dépend pas seulement :
- de bonnes questions

Mais surtout :
- d'un bon rythme
- d'une bonne alternance
- d'une variété documentaire maîtrisée

