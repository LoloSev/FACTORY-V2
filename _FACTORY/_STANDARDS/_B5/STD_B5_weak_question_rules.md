# STANDARD — WEAK QUESTION RULES

VERSION: 1.0
STATUS: ACTIVE_REFERENCE
PIPELINE_SCOPE: B5
IA_COMPATIBLE: TRUE
IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE

DEPENDENCY:
- FACTORY_QA_RULES.md
- STD_QA_status_rules.md
- glossaire_documentaire_factory.md
# SECTION — CHECK_WEAK_QUESTIONS

[RULE-WQ-001]
**Question générique**
FAIL si la question ne contient aucun ancrage détectable parmi :
- entité nommée
- date/période
- lieu
- catégorie contrôlée
- relation explicite entre deux champs source

[RULE-WQ-002]
**Question longue**
- WARNING si longueur > 120 caractères
- FAIL si longueur > 160 caractères
Comptage : caractères Unicode, espaces inclus.

[RULE-WQ-003]
**Question encyclopédique**
WARNING si la formulation contient au moins un marqueur narratif non nécessaire :
- "connu pour"
- "célèbre pour"
- "notamment"
- "au cours de"
- "dans le cadre de"
- "qui a marqué"
FAIL si ≥ 2 marqueurs sont présents dans la même question.

[RULE-WQ-004]
**Tournure IA typique**
WARNING si présence d'une formule méta ou scolaire :
- "quel est le nom de"
- "parmi les propositions suivantes"
- "selon les données disponibles"
- "il est important de noter"
FAIL si la tournure ajoute > 20 caractères sans modifier la condition de réponse.

[RULE-WQ-005]
**Phrase verbeuse**
WARNING si :
- ≥ 2 propositions subordonnées
- ou ≥ 2 incises entre virgules
- ou ratio mots-outils / mots totaux > 0,45

[RULE-WQ-006]
**Unicité interrogeable**
FAIL si la question teste plus d'une information centrale.
Test : la réponse exige deux faits indépendants pour être justifiée.

[RULE-WQ-007]
**Sortie attendue**
Chaque VALIDATION retourne :
- `PASS`
- `WARNING:<RULE_ID>`
- `FAIL:<RULE_ID>`
