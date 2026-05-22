# STANDARD — POOL COLLISION RULES

VERSION: 1.1
DATE_UPDATE: 2026-05-18
STATUS: ACTIVE_REFERENCE
PIPELINE_SCOPE: GLOBAL
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

# SECTION — ANTI_COLLISION

[RULE-PCOLL-001]
Un item documentaire majeur ne peut appartenir qu'à un seul pool principal.

[RULE-PCOLL-002]
Un angle IF ne peut pas être réassigné à un pool QV (RULE-IF-001).

[RULE-PCOLL-003]
Les pools peuvent définir :
- EXCLUDED_POOLS
- RESERVED_ITEMS
- FORBIDDEN_TAGS

[RULE-PCOLL-004]
Le VALIDATION anti-collision distingue deux périmètres :

**Inter-pool (HARD BLOCKER) :**
Une réponse correcte d'un pool ne peut pas apparaître comme distracteur dans un autre pool.
Couvre :
- le même fait réutilisé sous deux formulations différentes
- des angles de similarité normalisée ≥0,85 entre pools distincts
- deux questions reconduisant à la même réponse, même si leurs formulations ou angles diffèrent

**Intra-pool (BLOCKER limité) :**
Deux questions du même pool ne peuvent pas être effectivement identiques :
même réponse + même angle, quelle que soit la formulation.
La proximité thématique et la redondance partielle sont tolérées en intra-pool,
car une seule question par pool est tirée par partie — les deux n'apparaissent jamais ensemble.

RETEX_REF: RETEX_STD_GLOBAL_POOL_COLLISION_RULES_001
RETEX_ROLE: JUSTIFICATION

[RULE-PCOLL-005]
Une collision detectee apres validation d'un pool impose de rouvrir
au moins une des deux questions concernees avant passage a l'etape suivante.

[RULE-PCOLL-006]
Le controle anti-collision intervient avant toute proposition de question a l'humain,
pas seulement avant validation finale.


