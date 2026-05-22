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
- FACTORY_QA_RULES.md
- STD_QA_status_rules.md
- glossaire_documentaire_factory.md

SOURCE_DE_VERITE: STD_GLOBAL_pool_collision_rules.md
NOTE: Les règles ci-dessous sont des applications B5 des règles globales. Elles ne redéfinissent pas le concept — elles précisent le périmètre d'audit B5.

# SECTION — CHECK_POOL_COLLISIONS

[RULE-PCOLL-B5-001]
Application B5 de RULE-PCOLL-001 — seuils gradués (DÉCISION INC-01 / 2026-05-22) :
- Fait majeur présent dans 2 pools → WARNING audit B5 (violation RULE-PCOLL-001 documentée, tolérance B5 assumée)
- Fait majeur présent dans ≥ 3 pools → FAIL audit B5