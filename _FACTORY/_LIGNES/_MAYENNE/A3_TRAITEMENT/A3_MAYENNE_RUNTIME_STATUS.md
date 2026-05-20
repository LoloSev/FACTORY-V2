# A3 MAYENNE RUNTIME STATUS

## RUNTIME STATE

STATUS = STABLE
A3_LOCKED = YES
B2_READY = PENDING_RESTART

---

## STRUCTURE

POOLS_PHYSIQUES_ACTIFS = 17

POOLS_FUSIONNES = 3
- QV-07
- QV-10
- QV-15

IMPORTANT :
Les pools fusionnés :
- restent visibles structurellement
- ne contribuent plus au total runtime actif

---

## ASSEMBLY MAYENNE

QUIZ FORMAT = 20

RUNTIME DISTRIBUTION:
- IF-SF = 2
- IF-ROT = 3
- QV = 15

TARGET STOCK:
- IF-SF = 16
- IF-ROT = 36
- QV = 225

TOTAL_RUNTIME = 277

IMPORTANT :
Le runtime MAYENNE est piloté :
- par les slots gameplay
- pas par le nombre de pools physiques

---

## RUNTIME PATCH

A3_PATCH = APPLIED

Corrections :
- séparation local/global
- clarification fusion runtime
- clarification quotas assembly
- suppression ambiguïté pools/runtime
- verrouillage contrat 277

---

## SATURATION WATCH

SAT_RISK_HIGH:
- QV-06
- QV-09
- QV-11
- IF-ROT-02

Règle :
génération tardive B2 avec forte variété TYPE_Q.

---

## NEXT STEP

NEXT = B2_RESTART

Condition :
A3 stable et verrouillé avant relance générationnelle.
