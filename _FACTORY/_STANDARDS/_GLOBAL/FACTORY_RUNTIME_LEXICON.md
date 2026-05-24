# FACTORY_RUNTIME_LEXICON.md

STATUT: ACTIVE
ROLE: lexique runtime central machine-first
OBJECTIF: réduire ambiguïté, prose flottante et duplications sémantiques.

## RÈGLE D'USAGE

Tout document FACTORY doit référencer ces IDs/taxonomies au lieu de réexpliquer les concepts.
Un nouveau concept runtime doit être ajouté ici avant d'être propagé dans A2/A3/A4/B2/B3/B5.

## MACHINE STATE

```txt
A1=OPTIONAL
A2=ACTIVE|PENDING|RESET|LOCKED
A3=ACTIVE|PENDING|RESET|LOCKED
A4=ACTIVE|PENDING|RESET|LOCKED
B2=ACTIVE|PENDING|RESET|LOCKED
B3=ACTIVE|PENDING|RESET|LOCKED
B5=ACTIVE|PENDING|RESET|LOCKED
EXPORT=READY|PENDING|BLOCKED
POOL_ENGINE=READY|PENDING|BLOCKED
QA=PASS|WARN|FAIL
```

## RICHESSE

```txt
DENSE
STANDARD
LIGHT
```

## NIVEAU_POTENTIEL

```txt
N1
N2
N3
MULTI
```

Derivation rule (machine-first):
```
NIVEAU_POTENTIEL = N1    if all NIVEAU_ANGLE of item = N1
NIVEAU_POTENTIEL = N2    if all NIVEAU_ANGLE of item = N2
NIVEAU_POTENTIEL = N3    if all NIVEAU_ANGLE of item = N3
NIVEAU_POTENTIEL = MULTI if NIVEAU_ANGLE spans ≥2 distinct values
```

Source : HIERARCHIE_REGLEMENTAIRE.md L-006 / MDE_A3_traitement.md v4.0

## NIVEAU_ANGLE

```txt
N1
N2
N3
```

Classification criteria (closed, machine-applicable):
```
N1 : answer is the most salient and widely known fact about the item
     (primary record, most cited statistic, headline event)
     recognizable without thematic prerequisite

N2 : answer requires documented thematic knowledge
     (secondary stat, supporting event, non-headline figure)
     accessible to informed audience

N3 : answer is precise, rare, or counter-intuitive
     (exact coefficient, internal detail, non-publicized fact)
     inaccessible without immersion in the subject

DEFAULT_RULE : if N1/N2 ambiguous → N2 / if N2/N3 ambiguous → N2
N1 and N3 are unambiguous positions, not defaults.
```

Source : MDE_A3_traitement.md v4.0 / HIERARCHIE_REGLEMENTAIRE.md L-006

## MODE POOL

```txt
SIMPLE
AGREGE
```

## STATUT_B2

```txt
DRAFT
READY_B3
REWRITE
```

## FLAG_TYPE_B3

```txt
FORMAT
LENGTH
AMBIGUITY
PLAUSIBILITY
COLLISION
SCHOOL_FEELING
TOO_CLOSE
WEAK_PAYOFF
LEVEL_MISMATCH
```

## DECISION_RUNTIME_B5

```txt
READY_EXPORT
REWRITE
DROP
```

## PAYOFF_TYPE

```txt
COLLISION
ORALITE
DISPROPORTION
FAUX_REFLEXE
REVELATION
```

## RUNTIME_SIGNAL

```txt
KNOWN_NAME
HIDDEN_ORIGIN
LOCAL_COLLISION
SCALE_SHIFT
FALSE_OBVIOUS
MEMORY_HOOK
SCHOOL_RISK
PATOIS_MARKER
```

## MECHANIC

```txt
IDENTIFY
COMPARE
LOCATE
DATE
CLASSIFY
ELIMINATE
LINK
```

## DENSITY

```txt
LOW
MEDIUM
HIGH
```

## COLUMN_CONTRACT

Colonnes clés partagées entre xlsx A4/B2/B3/B5. Format exact requis pour jointure IA sans contexte implicite.

```txt
Q_ID              : Q-[THEME_3CHARS]-[POOL_ID]-[NNN]   ex: Q-MAY-IF01-001
POOL_ID           : IF[NN] | QV[NN]                      ex: IF01, QV03
CLUSTER           : section thématique d'origine         — colonne ITEMS (C-013)
SIGNAL_RUNTIME    : tag fermé depuis RUNTIME_SIGNAL      — colonnes ITEMS / POOLS
ANGLE_COURT       : description courte de l'angle        — colonne ANGLES
MECANIQUE         : tag fermé depuis MECHANIC            — colonne ANGLES
COLLISION_WITH    : ANGLE_ID incompatibles               — colonne ANGLES (C-013, remplace EXCLUSIONS)
FAISABILITE       : OK | WARN | FAIL                     — colonne POOLS (stock cible atteignable)
NIVEAU_POTENTIEL  : N1 | N2 | N3 | MULTI                 — colonne ITEMS (dérivé de NIVEAU_ANGLE)
NIVEAU_ANGLE      : N1 | N2 | N3                         — colonne ANGLES (assigné A3)
NIVEAU_QUESTION   : N1 | N2 | N3                         — colonne QUESTIONS (assigné B2)
COUVERTURE_NIVEAU : OK | WARN | FAIL                     — colonne POOLS (validé A4)
QA_STATUS         : PASS | WARN | FAIL
LENGTH_STATUS     : OK | ACCEPTABLE | FAIL
STATUT_B2         : DRAFT | READY_B3 | REWRITE
DECISION_RUNTIME  : READY_EXPORT | REWRITE | DROP
SEVERITY          : HB | SW | OPT
```

DEPRECATED:
```txt
CIBLE_NIVEAU  — remplacé par COUVERTURE_NIVEAU (POOLS) + NIVEAU_QUESTION (QUESTIONS)
CATÉGORIE     — remplacé par CLUSTER (C-013)
ANGLE         — remplacé par ANGLE_COURT (C-013)
EXCLUSIONS    — remplacé par COLLISION_WITH (C-013)
```

RÈGLE: toute colonne partagée entre ≥2 xlsx doit être listée ici avec format exact.

---

## RÈGLES ANTI-PROSE

Remplacer les phrases de pilotage par tags fermés.

Exemples:
```txt
éviter trop de patois trop tôt -> PATOIS_DENSITY=LOW
surprise culturelle -> PAYOFF_TYPE=REVELATION
anti scolaire -> SCHOOL_FEELING=LOW
```
