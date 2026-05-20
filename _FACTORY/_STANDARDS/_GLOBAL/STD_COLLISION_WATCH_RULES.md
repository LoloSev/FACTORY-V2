# STANDARD - COLLISION WATCH RULES

VERSION: 1.0
STATUS: ACTIVE_REFERENCE
PIPELINE_SCOPE: A4_B5
IA_COMPATIBLE: TRUE
IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE

DEPENDENCY:
- MASTER_ARCHITECTURE.md
- glossaire_documentaire_factory.md
---

# SECTION - COLLISION_WATCH

[DEF-CWATCH-001]
`COLLISION_WATCH` signale une collision potentielle ou une surexposition à monitorer sans bloquer automatiquement la production.

[RULE-CWATCH-001]
Utiliser `COLLISION_WATCH` quand :
- deux angles sont factuellement distincts mais editorialement proches
- une meme figure apparait dans plusieurs pools avec un risque de fatigue
- un arbitrage humain futur reste necessaire

[RULE-CWATCH-002]
`COLLISION_WATCH` n'est pas un hard blocker.
Il doit rester distinct de :
- collision averee
- doublon direct
- violation de reservation

[RULE-CWATCH-003]
Chaque `COLLISION_WATCH` doit documenter :
- les pools concernes
- l'objet ou le fait surveille
- la raison du risque
- la decision finale si elle existe

[RULE-CWATCH-004]
Cycle de traitement recommande :
`WATCH -> DECISION HUMAINE -> CONSERVE / DEPLACE / SUPPRIME`

[EXEMPLE-CWATCH-001]
cas source : Mbappe apparait dans plusieurs pools distincts.
RETEX_REF: RETEX_STD_COLLISION_WATCH_RULES_001
Le suivi porte sur la surexposition globale, pas sur un doublon automatique.
