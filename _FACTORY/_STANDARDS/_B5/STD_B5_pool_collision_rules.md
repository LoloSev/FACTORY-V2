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
- STD_B5_factory_quality_rules.md
- STD_QA_status_rules.md
- glossaire_documentaire_factory.md
# SECTION — CHECK_POOL_COLLISIONS

[RULE-PCOLL-B5-001]
Un même fait majeur ne doit pas apparaître dans 3 pools.

[RULE-PCOLL-B5-002]
Les finales IF-SF doivent rester protégées.

[RULE-PCOLL-B5-003]
Les réservations doivent être contrôlées.

[RULE-PCOLL-B5-004]
Le VALIDATION anti-collision doit couvrir aussi les réponses identiques et les faits éditorialement redondants, même si les formulations diffèrent.

[RULE-PCOLL-B5-005]
Une collision potentielle non bloquante peut être placée sous `COLLISION_WATCH` au lieu d'être traitée comme doublon immédiat.
