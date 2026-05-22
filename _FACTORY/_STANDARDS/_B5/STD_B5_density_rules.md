# STANDARD — DENSITY RULES

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
# SECTION — CHECK_REPEAT_DENSITY

[RULE-DENS-001]
Détecter les surreprésentations [ENTITE_PRIMAIRE].

[RULE-DENS-002]
Détecter les surreprésentations [CATEGORIE_GEOGRAPHIQUE].

[RULE-DENS-003]
Détecter les surreprésentations [PERIODE].

[RULE-DENS-004]
Détecter les surreprésentations [CONTEXTE_EDITION].

[EXEMPLE-DENS-001 — cas source]
Application sur la ligne cas source (football) :
→ ENTITE_PRIMAIRE = joueur
→ CATEGORIE_GEOGRAPHIQUE = nation
→ PERIODE = époque
→ CONTEXTE_EDITION = édition (Coupe du Monde)
