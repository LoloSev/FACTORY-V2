# STD — CONVENTIONS DE NOMMAGE FACTORY

VERSION: 1.0
DATE: 2026-05-18
STATUS: ACTIVE_REFERENCE
IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE
PIPELINE_SCOPE: V2
RETEX_REF: RETEX_STD_NAMING_CONVENTIONS_001

DEPENDENCY:
- PIPELINE_V2.md
- HIERARCHIE_REGLEMENTAIRE.md

---

# PRINCIPE GÉNÉRAL

```
[ÉTAPE]_[TYPE]_[THEME]_[NN].ext
```

| Segment | Description |
|---------|-------------|
| ÉTAPE | Préfixe d'étape pipeline (A2, A3, B2, B3…) |
| TYPE | Nature du contenu (BIB, PROCESS, APPRO_LOG…) |
| THEME | Code thème en majuscules (cas source, CINEMA, INTERNET, RAP, ROCK, SERIES…) |
RETEX_REF: RETEX_STD_NAMING_CONVENTIONS_002
| NN | Séquence 2 chiffres si fichier splitté (01, 02…) — omis si fichier unique |

---

# CONVENTIONS PAR ÉTAPE

## A2 — APPROVISIONNEMENT BIB

| Fichier | Pattern | Règle |
|---------|---------|-------|
| Source brute | `A2_BIB_[THEME]_NN.txt` | Immuable après archivage (RULE-A2-001). Splitté si volumétrie importante. |
RETEX_REF: RETEX_STD_NAMING_CONVENTIONS_003
RETEX_REF: RETEX_STD_NAMING_CONVENTIONS_004

Exemples :
```
RETEX_REF: RETEX_STD_NAMING_CONVENTIONS_005
A2_BIB_CINEMA_01.txt
A2_BIB_CINEMA_02.txt
A2_APPRO_LOG.md
A2_APPRO_STATS.md
```

---

## A3 — INIT XLSX + ITEMS + ANGLES (V2)

| Fichier | Pattern | Règle |
|---------|---------|-------|
| Artefact unique | `QUIZ_[THEME].xlsx` | Colonne vertébrale — 8 feuilles standards |
| Log décisions | `PROCESS_[THEME].md` | Léger — arbitrages humains uniquement |

Exemples :
```
QUIZ_INTERNET.xlsx
PROCESS_INTERNET.md
```

⚠️ Les fichiers V1 (BIPREGEN, ANGIPREGEN) sont supprimés en V2 — leurs données vivent dans les feuilles ITEMS et ANGLES du xlsx.

---

## A4 — POOLS (V2)

Données dans la feuille POOLS du `QUIZ_[THEME].xlsx`.
Pas de fichier séparé en V2.

---

## B2 — QUESTIONS (V2)

Données dans la feuille QUESTIONS du `QUIZ_[THEME].xlsx`.
Pas de fichier séparé en V2.

---

## B3 — DISTRACTEURS (V2)

Données dans la feuille DISTRACTEURS du `QUIZ_[THEME].xlsx`.
Pas de fichier séparé en V2.

---

## B5 — AUDIT QA (V2)

| Fichier | Pattern | Règle |
|---------|---------|-------|
| Audit | Feuille QA du xlsx | Intégré à l'artefact unique |
| Fiche veille | `FICHE_VEILLE_[THEME].md` | Produite en B5, conservée avec le quiz |

---

## B6 — RÈGLES

| Fichier | Pattern | Règle |
|---------|---------|-------|
| Notes de généralisation | `GEN_NOTE_[THEME]_[SUJET].md` | Si pattern généralisable détecté |

---

# CODES THÈMES AUTORISÉS

| Code | Thème |
|------|-------|
| cas source | Coupe du Monde de Football |
RETEX_REF: RETEX_STD_NAMING_CONVENTIONS_006
| CINEMA | Cinéma |
| INTERNET | Internet |
| RAP | Rap / Hip-Hop |
| ROCK | Rock |
| SERIES | Séries TV |
| MAYENNE | Mayenne |

RETEX_REF: RETEX_STD_NAMING_CONVENTIONS_007

---

# RÈGLES COMPLÉMENTAIRES

[RULE-NAMING-001]
Le code THEME est toujours en MAJUSCULES, sans accents, sans espaces.

[RULE-NAMING-002]
Le préfixe d'étape (A2, A3…) est toujours présent dans les fichiers de travail intermédiaires.
L'artefact final (QUIZ_[THEME].xlsx, PROCESS_[THEME].md) n'a pas de préfixe d'étape.

[RULE-NAMING-003]
Le split en plusieurs fichiers (NN) n'est autorisé que pour les BIB volumineux (A2).
Les logs et stats restent en fichier unique.

[RULE-NAMING-004]
RETEX_REF: RETEX_STD_NAMING_CONVENTIONS_008
Exemple : `_INTERNET`, `_RAP`, `_ROCK`, `_SERIES`

---

*STD_NAMING_CONVENTIONS.md*
*Version 1.0 — 2026-05-18 — Pipeline V2*
RETEX_REF: RETEX_STD_NAMING_CONVENTIONS_009
