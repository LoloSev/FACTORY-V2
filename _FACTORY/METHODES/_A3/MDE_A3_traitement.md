IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE


# MDE A3 — TRAITEMENT BIB → XLSX (ITEMS + ANGLES)

Version : 3.0 (PIPELINE V2)
Date : 2026-05-18
Remplace : MDE_A3 v2.0 (pipeline V1 — BIPREGEN.txt + ANGIPREGEN.txt)

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
- QUIZ_[THEME].xlsx initialisé
- feuilles CONFIG / ITEMS / ANGLES peuplées
- FAILURE_CASE listées avec code flag

ACCEPTANCE_CRITERIA:
- SOURCE_ARCHIVE_EXISTS = TRUE
- ITEM_ID_UNIQUE_RATE = 100%
- ITEMS_WITH_CATEGORY_RATE = 100%
- ITEMS_WITH_RICHESSE_RATE = 100%
- RICHESSE ∈ {DENSE, STANDARD, LIGHT}
- ANGLE_ID_UNIQUE_RATE = 100%
- ANGLES_WITH_ITEM_ID_RATE = 100%
- SECTION_ITEM_COUNT computed for 100% sections
- EXPORT_BLOCKER_COUNT = 0

FAILURE_CASES:
- missing source archive
- duplicate ITEM_ID or ANGLE_ID
- item without category
- item without measurable RICHESSE
- angle without linked ITEM_ID

---
# PRINCIPE GÉNÉRAL

A3 extrait sélectivement du BIB pour alimenter deux feuilles xlsx opérationnelles :
- **ITEMS** : items codés avec leur richesse documentaire
- **ANGLES** : angles interrogeables par item

A3 crée également le fichier QUIZ_[THEME].xlsx et le peuple jusqu'à HUMAN_GATE.

**Changement V2 fondamental :**
Les items ne reçoivent plus de niveau de difficulté (N1/N2/N3).
Ils reçoivent une **RICHESSE** (DENSE / STANDARD / LIGHT).
La difficulté des questions sera déterminée en A4 (pool) + B2 (question) + B3 (distracteurs).

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

# ÉTAPE 3 — CRÉATION DU XLSX ET FEUILLE CONFIG

Créer QUIZ_[THEME].xlsx avec les 7 feuilles standards :
CONFIG / ITEMS / ANGLES / POOLS / QUESTIONS / DISTRACTEURS / QA

Peupler la feuille CONFIG :

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
| CATÉGORIE | section thématique d'origine |
| RICHESSE | DENSE / STANDARD / LIGHT (voir critères ci-dessous) |
RETEX_REF: RETEX_MDE_A3_TRAITEMENT_006

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

⚠️ RICHESSE ≠ difficulté. Un item DENSE peut générer des questions N1 comme N3 selon l'angle choisi et les distracteurs. La difficulté sera définie en A4 par le pool.

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
| ITEM_ID | référence feuille ITEMS |
| ANGLE | description courte de l'angle (ex: "année du titre", "nombre de buts en finale") |
| POOL_CIBLE | laisser vide à ce stade — rempli en A4 |
| EXCLUSIONS | angles incompatibles avec celui-ci (anti-collision préventive) |
| QUOTA | nombre de questions cibles depuis cet angle (indicatif) |
| STATUT | DISPONIBLE par défaut |

## Règles de cartographie des angles

- Un angle doit pointer un fait unique et vérifiable
- Éviter les micro-variantes artificielles (reformulations différentes du même fait)
- Signaler les angles à risque de collision inter-items
- Ne pas assigner de niveau de difficulté à l'angle — ce sera fait en B2 selon le pool

## Suppressions d'angles motivées par

- redondance avec un autre angle du même item ou d'un item proche
- <1 relation interrogeable détectable hors description brute
- angle dont la réponse est textuellement contenue dans la question ou déductible par indice unique

---

# ÉTAPE 8 — HUMAN_GATE (GATE A3→A4)

Avant de passer à A4, soumettre à validation :

- [ ] Feuille ITEMS : codes uniques, RICHESSE ∈ {DENSE, STANDARD, LIGHT}, libellés non vides
- [ ] Feuille ANGLES : angles distincts, exclusions documentées, quotas indicatifs
- [ ] Sections LIGHT identifiées et candidates AGRÉGÉ notées
- [ ] Aucun angle fictif ou non vérifiable

Décisions humaines attendues :
- Validation RICHESSE (ou reclassement)
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
3. Créer QUIZ_[THEME].xlsx + CONFIG
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
- la RICHESSE est assignée pour chaque item
- les angles sont distincts et non ambigus
- les sections LIGHT candidates à AGRÉGÉ sont identifiées
- le BIB original reste intact
- les reclassements sont justifiés dans PROCESS_[THEME].md

---

*MDE_A3_traitement.md*
*Version 3.0 — 2026-05-18 — Pipeline V2*
*Remplace : v2.0 (BIPREGEN.txt + ANGIPREGEN.txt)*


