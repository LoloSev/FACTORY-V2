# STANDARD — POOL COLLISION RULES

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
- STD_GLOBAL_pool_collision_rules.md
- STD_B5_factory_quality_rules.md
- STD_QA_status_rules.md
- glossaire_documentaire_factory.md

SOURCE_DE_VERITE: STD_GLOBAL_pool_collision_rules.md
NOTE: Les règles ci-dessous sont des applications B5 des règles globales. Elles ne redéfinissent pas le concept — elles précisent le périmètre d'audit B5.

# SECTION — CHECK_POOL_COLLISIONS

[RULE-PCOLL-B5-001]
Application B5 de RULE-PCOLL-001 : un même fait majeur présent dans ≥ 3 pools → FAIL audit B5.

[RULE-PCOLL-B5-002]
Application B5 de RULE-PCOLL-002 : les pools IF doivent rester protégés — leurs angles ne peuvent pas apparaître en QV.

[RULE-PCOLL-B5-003]
Application B5 de RULE-PCOLL-003 : les réservations (EXCLUDED_POOLS / RESERVED_ITEMS / FORBIDDEN_TAGS) doivent être contrôlées.

[RULE-PCOLL-B5-004]
Application B5 de RULE-PCOLL-004 : le VALIDATION anti-collision doit couvrir les réponses identiques et les faits éditorialement redondants, même si les formulations diffèrent.

[RULE-PCOLL-B5-005]
Extension B5 (pas d'équivalent global) : une collision potentielle non bloquante peut être placée sous `COLLISION_WATCH` au lieu d'être traitée comme doublon immédiat.
