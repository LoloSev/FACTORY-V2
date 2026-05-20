IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE


# MDE A4 — CONSTITUTION DES POOLS → FEUILLE POOLS

Version : 2.0 (PIPELINE V2)
Date : 2026-05-18
Remplace : MDE_A4 v1.2 (pipeline V1 — POOLS_[THEME].txt + A5 tableur séparé)

DEPENDENCY:
- PIPELINE_V2.md
- MDE_A3_traitement.md (v3.0)
- STD_GLOBAL_quiz_architecture_rules.md
- STD_GLOBAL_pool_collision_rules.md

---

## MACHINE-FIRST EXECUTION CONTRACT

INPUT:
- QUIZ_[THEME].xlsx
- feuilles ITEMS et ANGLES validées
- 20 positions quiz disponibles

PROCESS:
1. lire sections, items, angles et RICHESSE
2. affecter exactement 20 pools
3. calculer CIBLE_NIVEAU depuis POSITION_QUIZ
4. affecter les angles aux pools
5. VALIDER stocks et collisions

OUTPUT:
- feuille POOLS peuplée
- feuille ANGLES mise à jour avec POOL_CIBLE / STATUT
- feuille SOMMAIRE calculée

ACCEPTANCE_CRITERIA:
- POOL_COUNT = 20
- IF_SF_COUNT = 2
- IF_ROT_COUNT = 3
- QV_COUNT = 15
- POSITION_QUIZ_UNIQUE_RATE = 100%
- CIBLE_NIVEAU_POSITION_MATCH_RATE = 100%
- STOCK_CIBLE ∈ {8,12,15}
- POOLS_WITH_ASSIGNED_ITEMS_RATE = 100%
- POOLS_WITH_ASSIGNED_ANGLES_RATE = 100%
- HARD_COLLISION_COUNT = 0
- EXPORT_BLOCKER_COUNT = 0

FAILURE_CASES:
- pool count != 20
- duplicate POSITION_QUIZ
- CIBLE_NIVEAU not derived from POSITION_QUIZ
- pool without item or angle
- hard collision detected

---
# PRINCIPE GÉNÉRAL

A4 constitue les 20 pools du quiz et peuple la feuille POOLS du xlsx.
C'est à cette étape que la difficulté est assignée — top-down, par position dans le quiz.

**Entrée :** QUIZ_[THEME].xlsx avec feuilles ITEMS + ANGLES validées (gate A3)
**Sortie :** feuille POOLS peuplée, prête pour B2

A4 produit aussi une feuille SOMMAIRE dans le xlsx pour le suivi d'avancement.

---

# ÉTAPE 1 — LECTURE DES ANGLES ET RICHESSE

Avant de constituer les pools :
- Lister toutes les sections depuis feuille ITEMS (par CATÉGORIE)
- Identifier les sections DENSE, STANDARD, LIGHT
- Repérer les sections signalées candidats AGRÉGÉ par A3
- Estimer le potentiel de questions par section (QUOTA × angles)

---

# ÉTAPE 2 — CONSTITUTION ÉDITORIALE DES 20 POOLS

DECISION_MODE: HUMAN_GATE_AFTER_MACHINE_PROPOSAL.

MACHINE_PROPOSAL:
- proposer 20 pools à partir des counts ITEMS/ANGLES/RICHESSE
- exposer tout écart aux seuils ACCEPTANCE_CRITERIA
HUMAN_GATE:
- autoriser uniquement APPROVE / RECONFIGURE / REJECT avec motif codé

## Règles de constitution

**Pools IF-SF (2 pools) :**
- Réservés aux incontournables absolus du thème
- Angles exclusifs — interdits dans QV (RULE-IFS-001)
- Stock cible : 8 questions chacun

**Pools IF-ROT (3 pools) :**
- Incontournables rotatifs — figures ou événements majeurs mais renouvelables
- Angles interdits dans QV (RULE-IFR-001)
- Stock cible : 12 questions chacun

**Pools QV (15 pools) :**
- Questions variables — SUBTHEME_DISTINCT_COUNT >= 12 sur QV (RULE-QV-001)
- ≥12 sous-thèmes distincts sur l'ensemble des QV (DEF-VAR-001)
- Stock cible : 15 questions chacun

## Règle de fusion AGRÉGÉ (RULE-ARCH-005)

Si une section LIGHT ou STANDARD ne peut pas atteindre seule le stock cible d'un pool :
- VALIDER si elle partage ≥2 critères avec une section de <5 items
- Si oui → fusionner en pool MODE=AGRÉGÉ
- Le pool AGRÉGÉ reste une unité de tirage unique pour le joueur
- Les questions des sous-thèmes agrégés doivent partager un registre commun
- Les distracteurs doivent rester valides à travers tous les sous-thèmes

---

# ÉTAPE 3 — ASSIGNATION CIBLE_NIVEAU (TOP-DOWN)

La difficulté est assignée par la position du pool dans le quiz.
Elle n'est pas négociable — elle découle de RULE-ARCH-004.

| Position quiz | CIBLE_NIVEAU |
|---------------|--------------|
| Q1 à Q5 | N1 |
| Q6 à Q15 | N2 |
| Q16 à Q20 | N3 |

L'IA assigne automatiquement CIBLE_NIVEAU selon la POSITION_QUIZ.
HUMAN_GATE: POSITION_QUIZ peut être validée ou modifiée ; CIBLE_NIVEAU reste calculé automatiquement.

⚠️ Conséquence descriptife : un pool en position Q16-Q20 devra générer des questions N3.
Si le pool contient <3 angles N3-valides, revoir la position du pool, pas le niveau.

---

# ÉTAPE 4 — PEUPLEMENT FEUILLE POOLS

RETEX_REF: RETEX_MDE_A4_TABLEUR_POOLS_001

| Colonne | Valeur |
|---------|--------|
| POOL_ID | QV-01 à QV-15 / IF-SF-01/02 / IF-ROT-01/02/03 |
| TYPE | IF-SF / IF-ROT / QV |
| POSITION_QUIZ | Q1 à Q20 |
| CIBLE_NIVEAU | N1 / N2 / N3 (automatique via position) |
| THEME_LABEL | label contrôlé du pool |
| MODE | SIMPLE / AGRÉGÉ |
| SOUS_THÈMES | liste des sous-thèmes (si AGRÉGÉ) |
| ITEMS_ASSIGNÉS | liste des ITEM_ID assignés à ce pool |
| STOCK_CIBLE | 8 (IF-SF) / 12 (IF-ROT) / 15 (QV) |
| STOCK_ACTUEL | formule =COUNTIF(QUESTIONS[POOL_ID], POOL_ID) |

---

# ÉTAPE 5 — ASSIGNATION ANGLES AUX POOLS

Mettre à jour la feuille ANGLES :
- Pour chaque angle, remplir POOL_CIBLE avec le POOL_ID correspondant
- Mettre STATUT = RÉSERVÉ pour les angles déjà assignés
- VALIDER que chaque pool a assez d'angles pour atteindre STOCK_CIBLE

Si un pool ne peut pas atteindre STOCK_CIBLE avec les angles disponibles :
- Signaler le déficit explicitement (RULE-B2-HB-001)
- Ne pas passer à B2 sans décision humaine
- Options : enrichir le BIB (ajouter matière culturelle — gate humaine requise) / fusionner avec un autre pool / réduire le stock cible

---

# ÉTAPE 6 — CONTRÔLE ANTI-COLLISION INTER-POOLS

Avant validation :
- VALIDER qu'aucun angle n'est assigné à deux pools différents
- VALIDER qu'aucun item majeur n'appartient à deux pools
- VALIDER conformité EXCLUDED_POOLS dans feuille ANGLES
- VALIDER par critère mesurable que les angles IF-SF ne sont pas dans les QV, idem IF-ROT

---

# ÉTAPE 7 — CRÉATION FEUILLE SOMMAIRE

Créer une feuille SOMMAIRE dans le xlsx :

| Colonne | Contenu |
|---------|---------|
| POOL_ID | identifiant |
| TYPE | IF-SF / IF-ROT / QV |
| POSITION | Q1 à Q20 |
| CIBLE_NIVEAU | N1 / N2 / N3 |
| THÈME | intitulé |
| MODE | SIMPLE / AGRÉGÉ |
| STOCK_CIBLE | cible |
| STOCK_ACTUEL | =COUNTIF dynamique |
| Q_PASS | =COUNTIF(QA[QA_STATUS]="PASS", QA[POOL_ID]=...) |
| Q_WARNING | idem WARNING |
| Q_FAIL | idem FAIL |
| Q_DRAFT | idem DRAFT |
| % COMPLET | =STOCK_ACTUEL/STOCK_CIBLE |

Le SOMMAIRE est le cockpit de pilotage du quiz. Il se met à jour automatiquement à chaque ajout de question ou changement de QA_STATUS.

---

# ÉTAPE 8 — HUMAN_GATE (GATE A4→B2)

Avant de passer à B2 :

- [ ] 20 pools constitués
- [ ] CIBLE_NIVEAU correct pour chaque position
- [ ] Pools AGRÉGÉ validés (conformité sous-thèmes confirmée)
- [ ] Angles assignés pour chaque pool
- [ ] Stocks cibles atteignables
- [ ] Anti-collision inter-pools vérifié
- [ ] SOMMAIRE opérationnel

Décisions humaines attendues :
- Validation des 20 pools (ou reconfiguration)
- Validation des pools AGRÉGÉ
- Confirmation des positions (qui détermine CIBLE_NIVEAU)

---

# METRICS

A4 est valide si :
- exactement 20 pools définis
- CIBLE_NIVEAU conforme à RULE-ARCH-004 pour chaque position
- chaque pool a assez d'angles pour atteindre son stock cible
- aucun angle assigné à deux pools
- les pools AGRÉGÉ ont une conformité documentaire vérifiée

---

*MDE_A4_tableur_pools.md*
*Version 2.0 — 2026-05-18 — Pipeline V2*
*Remplace : v1.2 (POOLS_[THEME].txt + A5 tableur séparé)*


