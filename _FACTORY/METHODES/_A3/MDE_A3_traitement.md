IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE


# MDE A3 — TRAITEMENT BIB → TSV (ITEMS + ANGLES)

Version : 4.1 (PIPELINE V2.1)
Date : 2026-05-25
Remplace : MDE_A3 v3.0 (pipeline V2 — sans NIVEAU_ANGLE)

DEPENDENCY:
- PIPELINE_V2.md
- STD_GLOBAL_quiz_architecture_rules.md
- STD_B2_generation_rules.md
- STD_GLOBAL_pool_collision_rules.md

---

## MACHINE-FIRST EXECUTION CONTRACT

INPUT:
- BIB_[THEME].txt source archivé
- THEME non vide
- pipeline V2 actif

PROCESS:
1. archiver source sans modification
2. extraire sections et items
3. attribuer ITEM_ID unique
4. classer RICHESSE via seuils mesurables
5. produire feuilles CONFIG / ITEMS / ANGLES

OUTPUT:
- CONFIG.yaml initialisé
- ITEMS.tsv peuplé
- ANGLES.tsv peuplé
- FAILURE_CASE listées avec code flag

ACCEPTANCE_CRITERIA:
- SOURCE_ARCHIVE_EXISTS = TRUE
- ITEM_ID_UNIQUE_RATE = 100%
- ITEMS_WITH_CATEGORY_RATE = 100%
- ITEMS_WITH_RICHESSE_RATE = 100%
- RICHESSE ∈ {DENSE, STANDARD, LIGHT}
- ITEMS_WITH_NIVEAU_POTENTIEL_RATE = 100%
- NIVEAU_POTENTIEL ∈ {N1, N2, N3, MULTI}
- ANGLE_ID_UNIQUE_RATE = 100%
- ANGLES_WITH_ITEM_ID_RATE = 100%
- ANGLES_WITH_NIVEAU_ANGLE_RATE = 100%
- NIVEAU_ANGLE ∈ {N1, N2, N3}
- SECTION_ITEM_COUNT computed for 100% sections
- EXPORT_BLOCKER_COUNT = 0

FAILURE_CASES:
- missing source archive
- duplicate ITEM_ID or ANGLE_ID
- item without category
- item without measurable RICHESSE
- item without NIVEAU_POTENTIEL
- angle without linked ITEM_ID
- angle without NIVEAU_ANGLE

---
# PRINCIPE GÉNÉRAL

A3 extrait sélectivement du BIB pour alimenter deux feuilles xlsx opérationnelles :
- **ITEMS** : items codés avec leur richesse documentaire
- **ANGLES** : angles interrogeables par item

A3 initialise CONFIG.yaml et peuple ITEMS.tsv + ANGLES.tsv depuis le template _LIGNES/_TEMPLATE/.

**Changement V2.1 fondamental :**
Les items reçoivent une **RICHESSE** (DENSE / STANDARD / LIGHT) = combien de questions.
Les angles reçoivent un **NIVEAU_ANGLE** (N1 / N2 / N3) = à quel public.
Les items reçoivent un **NIVEAU_POTENTIEL** dérivé de l'agrégation de leurs NIVEAU_ANGLE.
La difficulté est évaluée à l'angle (A3), assignée à la question en B2 (NIVEAU_QUESTION).
Le pool n'est plus le porteur du niveau — voir RULE-ARCH-008.

---

# ÉTAPE 0 — ARCHIVAGE DE L'ORIGINAL

Action :
Dupliquer le fichier brut sous le nom BIB_[THEME].txt.

Règle :
Ce fichier n'est jamais modifié.
Il sert de référence AVANT pour toute vérification ultérieure.

---

# ÉTAPE 1 — AUDIT DU FICHIER BRUT

Avant toute modification, analyser et documenter l'état initial.

## 1.1 Inventaire des sections
- lister les sections thématiques
- compter le nombre d'items par section

## 1.2 Identification des FAILURE_CASE

| FAILURE_CASE fréquent | Action à prévoir |
|---|---|
| Indicateurs de difficulté non standard | Harmonisation |
RETEX_REF: RETEX_MDE_A3_TRAITEMENT_001
| Absence d'identifiant unique | Ajout d'un code |
| Sections sous seuil (<5 items) | Candidats fusion pool AGRÉGÉ |
| Risques de doublons entre sections | Cartographie des angles |

## 1.3 Comptage initial
- nombre total d'items
- répartition par section
- sections avec <5 items → noter candidats AGRÉGÉ

---

RETEX_REF: RETEX_MDE_A3_TRAITEMENT_002

RETEX_REF: RETEX_MDE_A3_TRAITEMENT_003

Détection :
RETEX_REF: RETEX_MDE_A3_TRAITEMENT_004
- un numéro de section
- un titre de section

Types possibles :
- Type A : titre + description
- Type B : titre + sous-données multiples

Indicateurs de difficulté du BIB source : les conserver comme information brute dans SOURCE_BIB.
Ils ne déterminent pas la RICHESSE — ils sont de la documentation source.

---

# ÉTAPE 3 — INITIALISATION DES TSV ET CONFIG.yaml

Copier le template _LIGNES/_TEMPLATE/ dans _LIGNES/[THEME]/ (TSV + CONFIG.yaml).
TSV initialisés : ITEMS.tsv / ANGLES.tsv / POOLS.tsv / QUESTIONS.tsv / DISTRACTEURS.tsv / QA.tsv

Remplir CONFIG.yaml :

| Champ | Valeur |
|-------|--------|
| THEME | [nom du thème] |
| DATE_INIT | [date] |
| STOCK_CIBLE | 277 |
| VERSION | 1.0 |
| STATUT | INIT |

---

# ÉTAPE 4 — CODAGE ITEMS → FEUILLE ITEMS

## Format du code

```
[THEME]-[CAT]-[N°]
```

Règles :
- chaque code doit être unique
- [CAT] = abréviation de la catégorie/section (3-5 lettres majuscules)
- [N°] = numérotation séquentielle dans la catégorie (001, 002...)
- pas de niveau dans le code (supprimé vs V1)

## Colonnes à remplir

| Colonne | Règle |
|---------|-------|
| ITEM_ID | [THEME]-[CAT]-[N°] |
RETEX_REF: RETEX_MDE_A3_TRAITEMENT_005
| LIBELLE | texte de l'item, ligne unique |
| CLUSTER | section thématique d'origine (C-013 — remplace CATÉGORIE) |
| RICHESSE | DENSE / STANDARD / LIGHT (voir critères ci-dessous) |
RETEX_REF: RETEX_MDE_A3_TRAITEMENT_006
| NIVEAU_POTENTIEL | dérivé en Étape 7b — ne pas remplir manuellement |
| SIGNAL_RUNTIME | tag fermé depuis FACTORY_RUNTIME_LEXICON.md / RUNTIME_SIGNAL |
| SOURCE_BIB | référence ligne BIB originale |

## Critères RICHESSE

**DENSE** :
- item à 3 angles ou plus exploitables distinctement
- ≥3 angles distincts possibles parmi identité, mesure, contexte, comparaison, chronologie, exception
- exemple : une finale de Coupe du Monde (score, buteurs, pays, année, anecdote)

**STANDARD** :
- item à 1-3 angles exploitables
- potentiel normal
- exemple : un buteur avec quelques statistiques mémorables

**LIGHT** :
- item avec <2 angles distincts
- ≤1 angle, ou similarité entre angles ≥0,85
- souvent candidat à un pool AGRÉGÉ
- exemple : un joueur n'ayant qu'une seule donnée factuelle notable

⚠️ RICHESSE ≠ NIVEAU_POTENTIEL. Un item DENSE peut être N1, N3 ou MULTI selon ses angles.
La difficulté est évaluée à l'angle (NIVEAU_ANGLE), assignée à la question en B2 (NIVEAU_QUESTION). Le pool ne porte plus de niveau fixe.

---

# ÉTAPE 5 — STATISTIQUES DE RICHESSE

Tableau de bord documentaire :

| Catégorie | Nb items | DENSE | STANDARD | LIGHT | Observation |
|-----------|----------|-------|----------|-------|-------------|
| [CAT-1] | | | | | |
| [CAT-2] | | | | | |
| TOTAL | | | | | |

Objectif : identifier les sections LIGHT candidates à fusion AGRÉGÉ avant A4.

---

# ÉTAPE 6 — RÉÉQUILIBRAGE DOCUMENTAIRE

Si une catégorie dépasse un seuil de déséquilibre en RICHESSE :
- WARNING si une valeur RICHESSE > 60 % des items de la catégorie
- FAIL si une valeur RICHESSE > 75 % des items de la catégorie
- proposer des reclassements LIGHT → STANDARD si sous-estimé
- proposer des réductions (doublons cachés)
- proposer des enrichissements documentaires

HUMAN_GATE obligatoire avant application.

---

# ÉTAPE 7 — ANGLES → FEUILLE ANGLES

Un angle = un aspect précis et non ambigu d'un item = une seule question possible.

## Colonnes à remplir

| Colonne | Règle |
|---------|-------|
| ANGLE_ID | [ITEM_ID]-[A/B/C...] |
| ITEM_ID | référence ITEMS.tsv |
| ANGLE_COURT | description courte de l'angle (ex: "année du titre", "nombre de buts en finale") |
| MECANIQUE | tag fermé : IDENTIFY / COMPARE / LOCATE / DATE / CLASSIFY / ELIMINATE / LINK |
| NIVEAU_ANGLE | N1 / N2 / N3 — critères fermés ci-dessous |
| POOL_CIBLE | laisser vide à ce stade — rempli en A4 |
| COLLISION_WITH | ANGLE_ID incompatibles (anti-collision préventive) |
| QUOTA | nombre de questions cibles depuis cet angle (indicatif) |
| STATUT | DISPONIBLE par défaut |

## Critères NIVEAU_ANGLE (machine-applicable — source : FACTORY_RUNTIME_LEXICON.md)

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
```

## Étape 7b — Dérivation NIVEAU_POTENTIEL par item

Après avoir rempli tous les NIVEAU_ANGLE de ANGLES.tsv, calculer par item :

```
NIVEAU_POTENTIEL = N1    if all NIVEAU_ANGLE of item = N1
NIVEAU_POTENTIEL = N2    if all NIVEAU_ANGLE of item = N2
NIVEAU_POTENTIEL = N3    if all NIVEAU_ANGLE of item = N3
NIVEAU_POTENTIEL = MULTI if NIVEAU_ANGLE spans ≥2 distinct values among {N1, N2, N3}
```

Remplir la colonne NIVEAU_POTENTIEL de ITEMS.tsv depuis ce calcul.
Ne pas remplir NIVEAU_POTENTIEL manuellement — toujours dériver depuis NIVEAU_ANGLE.

## Règles de cartographie des angles

- Un angle doit pointer un fait unique et vérifiable
- Éviter les micro-variantes artificielles (reformulations différentes du même fait)
- Signaler les angles à risque de collision inter-items
- Assigner NIVEAU_ANGLE selon les critères fermés ci-dessus — pas d'estimation prose

## Suppressions d'angles motivées par

- redondance avec un autre angle du même item ou d'un item proche
- <1 relation interrogeable détectable hors description brute
- angle dont la réponse est textuellement contenue dans la question ou déductible par indice unique

---

# ÉTAPE 8 — HUMAN_GATE (GATE A3→A4)

Avant de passer à A4, soumettre à validation :

- [ ] ITEMS.tsv : codes uniques, RICHESSE ∈ {DENSE, STANDARD, LIGHT}, NIVEAU_POTENTIEL dérivé, libellés non vides
- [ ] ANGLES.tsv : angles distincts, NIVEAU_ANGLE ∈ {N1, N2, N3}, exclusions documentées, quotas indicatifs
- [ ] Sections LIGHT identifiées et candidates AGRÉGÉ notées
- [ ] Aucun angle fictif ou non vérifiable

Décisions humaines attendues :
- Validation RICHESSE (ou reclassement)
- Validation NIVEAU_ANGLE (ou reclassement)
- Confirmation des candidats AGRÉGÉ
- Suppression d'angles discutables

---

# ÉTAPE 9 — PROCESS LOG (PROCESS_[THEME].md)

Documenter dans PROCESS_[THEME].md (léger) :
- état initial du BIB (résumé)
- reclassements RICHESSE effectués avec justification
- angles supprimés avec motif
- candidats AGRÉGÉ identifiés
- décisions humaines reçues

Ce document est minimal — traçabilité des arbitrages, pas encyclopédie des transformations.

---

# ORDRE D'EXÉCUTION

0. Archiver BIB original
1. Auditer le fichier brut
RETEX_REF: RETEX_MDE_A3_TRAITEMENT_007
3. Initialiser TSV depuis template + remplir CONFIG.yaml
4. Coder les items → feuille ITEMS avec RICHESSE
5. Construire les statistiques de richesse
6. Rééquilibrer si nécessaire (HUMAN_GATE)
7. Cartographier les angles → feuille ANGLES
8. Gate humaine : validation ITEMS + ANGLES
9. Documenter dans PROCESS_[THEME].md

---

# METRICS

A3 est valide si :
- tous les items sont codés de façon unique
- RICHESSE assignée pour chaque item ∈ {DENSE, STANDARD, LIGHT}
- NIVEAU_ANGLE assigné pour chaque angle ∈ {N1, N2, N3}
- NIVEAU_POTENTIEL dérivé pour chaque item ∈ {N1, N2, N3, MULTI}
- les angles sont distincts et non ambigus
- les sections LIGHT candidates à AGRÉGÉ sont identifiées
- le BIB original reste intact
- les reclassements sont justifiés dans PROCESS_[THEME].md

---

*MDE_A3_traitement.md*
*Version 4.1 — 2026-05-25 — Pipeline V2.1*
*Remplace : v4.0 — OUTPUT TSV (ITEMS.tsv / ANGLES.tsv) au lieu de xlsx*


