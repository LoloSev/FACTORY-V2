IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE


DEPENDENCY:
- MASTER_ARCHITECTURE.md
- glossaire_documentaire_factory.md
# FACTORY_QA_RULES

## Objectif

Automatiser le VALIDATION QA_STATUS de la FACTORY afin de:
- détecter les dérives
- stabiliser la QA_STATUS
- empêcher la dégradation progressive
- gérer la croissance massive de contenu

---

## VALIDATIONS obligatoires

### CHECK_DUPLICATES

Mesures :
- `Q_TEXT_NORM` identique → FAIL
- similarité normalisée ≥ 0.90 entre deux questions du même export → FAIL
- même `ANSWER_KEY` + même `ANGLE_ID` → FAIL
- même `ANSWER_KEY` dans ≥ 3 questions d'un même pool → WARNING

---

### CHECK_POOL_COLLISIONS

Mesures :
- même fait majeur présent dans ≥ 3 pools → FAIL
- angle déjà réservé dans `RESERVATIONS` → FAIL
- `POOL_ID` absent ou non conforme → FAIL

---

### CHECK_REPEAT_DENSITY

Mesures par export :
- même entité en réponse correcte > 2 occurrences → WARNING
- même entité en réponse correcte > 3 occurrences → FAIL
- même catégorie dominante > 35 % d'un pool → WARNING
- même catégorie dominante > 45 % d'un pool → FAIL

---

### CHECK_DIFFICULTY_CURVE

Mesures :
- écart local N1/N2/N3 > 15 points vs cible du pool → WARNING
- écart local N1/N2/N3 > 25 points vs cible du pool → FAIL
- séquence de ≥ 4 questions consécutives du même niveau → WARNING

---

### CHECK_WEAK_QUESTIONS

Mesures :
- longueur question > 120 caractères → WARNING
- longueur question > 160 caractères → FAIL
- ≥ 2 subordonnées ou incises → WARNING
- présence d'un marqueur encyclopédique narratif listé dans STD_B5_weak_question_rules.md → WARNING
- absence de contrainte interrogeable unique → FAIL

---

### CHECK_DISTRACTORS

Mesures :
- distracteur égal à la réponse correcte normalisée → FAIL
- distracteur hors type attendu (`PERSON`, `DATE`, `PLACE`, `NUMBER`, `LABEL`) → FAIL
- 0 critère partagé avec la réponse attendue lorsque TYPE exige proximité → WARNING
- écart de distance numérique hors plage du niveau cible → WARNING
- distracteur non sourcé ou non traçable → FAIL

---

### CHECK_FACTORY_FORMAT

Mesures :
- champ obligatoire vide → FAIL
- valeur hors enum autorisée → FAIL
- identifiant non conforme au pattern attendu → FAIL
- feuille attendue absente → FAIL

## Flags qa

```txt
QA_STATUS=PASS
QA_STATUS=WARNING
QA_STATUS=FAIL
QA_SOURCE=AUTOMATIC
```

---

## Principe d'exécution

Une règle QA est valide seulement si elle produit :
- `PASS`
- `WARNING`
- `FAIL`

Toute mention qualitative non mesurable doit être convertie en :
- seuil numérique
- enum fermée
- pattern détectable
- présence/absence d'un champ
- comparaison entre deux valeurs normalisées
