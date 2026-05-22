# STANDARD — FACTORY QUALITY RULES

VERSION: 1.0
STATUS: ARCHIVED
ARCHIVED_DATE: 2026-05-22
ARCHIVED_REASON: D-09 — stub sans seuil mesurable. Source unique QA : FACTORY_QA_RULES.md. Suppression physique manuelle requise.
PIPELINE_SCOPE: B5
IA_COMPATIBLE: TRUE
IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE

DEPENDENCY:
- MASTER_ARCHITECTURE.md
- STD_GLOBAL_glossaire_documentaire_factory.md

---

# SECTION — OBJECTIF_QA

[RULE-B5QA-001]
La FACTORY doit maintenir une QA_STATUS stable malgré la croissance documentaire.

[RULE-B5QA-002]
Les VALIDATIONS QA doivent détecter les dérives documentaires.

[RULE-B5QA-003]
Le pipeline QA doit rester auditable.

---

# SECTION — PHILOSOPHIE_QA

[RULE-B5QA-004]
La FACTORY ne doit pas dépendre d'un VALIDATION humain constant.

[RULE-B5QA-005]
Le système QA doit privilégier :
- génération auditable
- vérification automatique
- pipeline résilient
