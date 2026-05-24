# STANDARD — QUIZ ARCHITECTURE RULES

VERSION: 1.1
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

# SECTION — STRUCTURE_UNIVERSELLE

[RULE-ARCH-001]
Un quiz final est piloté par des positions gameplay, pas par le nombre de pools physiques.

[RULE-ARCH-002]
Distinction obligatoire :

```txt
POOL_PHYSIQUE ≠ SLOT_RUNTIME ≠ QUOTA_ASSEMBLY
```

Définitions :
- `POOL_PHYSIQUE` = réservoir de contenu exploitable
- `SLOT_RUNTIME` = position gameplay dans l’assemblage final
- `QUOTA_ASSEMBLY` = volume cible dérivé du contrat d’assemblage actif

[RULE-ARCH-003]
Les quotas runtime sont pilotés par l’assembly contract actif.

Interdit :
- recalculer un quota runtime depuis le seul nombre de pools physiques
- modifier un stock cible par fusion structurelle implicite

[RULE-ARCH-004]
Une fusion de pools physiques :
- réduit la fragmentation structurelle
- ne modifie jamais automatiquement les quotas runtime
- doit transférer coverage, angles, collisions et densité vers la structure active

[RULE-ARCH-005]
Le stock cible d’une ligne est dérivé de son assembly contract.

Contrôle minimal :
```txt
SUM(QUOTA_ASSEMBLY_BY_FAMILY) = TARGET_STOCK_LINE
```

Si le total ne correspond pas au contrat actif :
```txt
QA_STATUS=FAIL
```

[RULE-ARCH-006]
**Difficulty distribution — canonical runtime rule**

For a 20-question player-facing quiz:

```yaml
DIFFICULTY_DISTRIBUTION:
  N1: 5
  N2: 10
  N3: 5
```

Runtime roles:
- N1: onboarding_and_confidence
- N2: discovery_core
- N3: stimulating_final_elevation

Position mapping:
- Q1 to Q5 -> N1
- Q6 to Q15 -> N2
- Q16 to Q20 -> N3

This order is fixed and does not vary between runs.
This rule overrides any legacy 40/40/20 distribution.
RETEX_REF: RETEX_STD_GLOBAL_QUIZ_ARCHITECTURE_RULES_001
RETEX_ROLE: JUSTIFICATION

Application layer (updated v1.2):
The engine applies this position mapping by filtering NIVEAU_QUESTION on questions.
NIVEAU_QUESTION is a property of each question (assigned in B2), not of the pool.
A pool is a thematic unit. It does not carry a fixed level.
See RULE-ARCH-008.

Do not confuse this with distractor distribution rules.

[RULE-ARCH-007]
**Agrégation de sous-thèmes dans un pool**

Un pool peut regrouper plusieurs sous-thèmes faibles pour atteindre son stock cible,
dès lors que les questions restent CONSISTENCY_VALIDATED entre elles et que les distracteurs
restent valides à travers les sous-thèmes agrégés.

Un pool = unité de tirage runtime, pas nécessairement unité thématique unique.
RETEX_REF: RETEX_STD_GLOBAL_QUIZ_ARCHITECTURE_RULES_002
RETEX_ROLE: JUSTIFICATION

[RULE-ARCH-008]
**Décorrélation thème / niveau**

```txt
POOL_PHYSIQUE   = thematic unit
NIVEAU_QUESTION = property of each question (assigned B2 via NIVEAU_ANGLE)
```

Constraints:
- A pool has no fixed CIBLE_NIVEAU
- A pool has a NIVEAU_REQUIS computed from POSITION_QUIZ (for validation only, not stored)
- A pool must satisfy COUVERTURE_NIVEAU = OK for its NIVEAU_REQUIS before B2
- The engine filters by (POOL_ID, NIVEAU_QUESTION) at assembly runtime

COUVERTURE_NIVEAU thresholds:
```txt
OK   : items with NIVEAU_POTENTIEL = NIVEAU_REQUIS or MULTI ≥ 30% of pool's items
WARN : same condition, 1–29%
FAIL : same condition, 0% → human gate required before B2
```

NOTE: 30% threshold = initial calibration value. To be confirmed on MAYENNE prototype (RULE-GOV-002).
Parent: HIERARCHIE_REGLEMENTAIRE.md L-003 + C-010 + C-011
