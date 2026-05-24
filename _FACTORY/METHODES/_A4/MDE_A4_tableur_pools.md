IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE

# MDE A4 — CONSTITUTION DES POOLS → POOLS.tsv

Version : 3.2 (PIPELINE V2.1)
Date : 2026-05-25
Remplace : MDE_A4 v3.1 — alignement dépendances et POOL_ID canoniques

DEPENDENCY:
- PIPELINE_V2.md
- MDE_A3_traitement.md (v4.2)
- STD_GLOBAL_quiz_architecture_rules.md
- STD_GLOBAL_pool_collision_rules.md

---

## MACHINE-FIRST EXECUTION CONTRACT

INPUT:
- ITEMS.tsv validé (gate A3)
- ANGLES.tsv validé (gate A3)
- 20 positions quiz disponibles

PROCESS:
1. lire sections, items, angles, RICHESSE et NIVEAU_POTENTIEL
2. affecter exactement 20 pools (thématique uniquement)
3. calculer COUVERTURE_NIVEAU par pool (RULE-ARCH-008)
4. affecter les angles aux pools
5. VALIDER stocks, couverture et collisions

OUTPUT:
- POOLS.tsv peuplé
- ANGLES.tsv mis à jour (POOL_CIBLE / STATUT)
- SOMMAIRE généré via generate_sommaire.py

ACCEPTANCE_CRITERIA:
- POOL_COUNT = 20
- IF_COUNT = 5
- QV_COUNT = 15
- POSITION_QUIZ_UNIQUE_RATE = 100%
- STOCK_CIBLE ∈ {8,12,15}
- IF_STOCK_Q1Q2 = 8
- IF_STOCK_Q3Q5 = 12
- QV_STOCK = 15
- POOLS_WITH_ASSIGNED_ITEMS_RATE = 100%
- POOLS_WITH_ASSIGNED_ANGLES_RATE = 100%
- NIVEAU_COVERAGE_FAIL_COUNT = 0
- HARD_COLLISION_COUNT = 0
- EXPORT_BLOCKER_COUNT = 0

FAILURE_CASES:
- POOL_COUNT != 20
- duplicate POSITION_QUIZ
- pool without item or angle
- COUVERTURE_NIVEAU = FAIL without human decision
- hard collision detected

---

# PRINCIPE GÉNÉRAL

A4 constitue les 20 pools du quiz et peuple POOLS.tsv.
Les pools sont purement thématiques — la difficulté n'est plus assignée au pool.
A4 valide que chaque pool peut servir le niveau qu'exigera le moteur (COUVERTURE_NIVEAU).

**Entrée :** ITEMS.tsv + ANGLES.tsv validés (gate A3)
**Sortie :** POOLS.tsv peuplé, prêt pour B2

A4 déclenche aussi generate_sommaire.py pour le suivi d'avancement.

---

# ÉTAPE 1 — LECTURE DES ANGLES ET RICHESSE

Avant de constituer les pools :
- Lister toutes les sections depuis ITEMS.tsv (par CLUSTER)
- Identifier les sections DENSE, STANDARD, LIGHT
- Lire NIVEAU_POTENTIEL par item (N1/N2/N3/MULTI)
- Repérer les sections signalées candidats AGRÉGÉ par A3
- Estimer le potentiel de questions par section (QUOTA × angles)

---

# ÉTAPE 2 — CONSTITUTION ÉDITORIALE DES 20 POOLS

DECISION_MODE: HUMAN_GATE_AFTER_MACHINE_PROPOSAL.

## Règles de constitution

**Pools IF — Q1-Q2 (2 pools, stock=8) :**
- Réservés aux incontournables absolus du thème
- Angles exclusifs — interdits dans QV (RULE-IF-001)
- Stock cible : 8 questions chacun
- POOL_ID : IF-01, IF-02

**Pools IF — Q3-Q5 (3 pools, stock=12) :**
- Incontournables rotatifs — figures ou événements majeurs mais renouvelables
- Angles interdits dans QV (RULE-IF-001)
- Stock cible : 12 questions chacun
- POOL_ID : IF-03, IF-04, IF-05

**Pools QV — Q6-Q20 (15 pools, stock=15) :**
- Questions variables — SUBTHEME_DISTINCT_COUNT >= 12 sur QV (RULE-QV-001)
- ≥12 sous-thèmes distincts sur l'ensemble des QV (DEF-VAR-001)
- Stock cible : 15 questions chacun
- POOL_ID : QV-01 à QV-15

---

# ÉTAPE 3 — VÉRIFICATION COUVERTURE NIVEAU

Le pool est purement thématique.
La position dans le quiz définit le niveau que le moteur demandera.

| Position quiz | NIVEAU_REQUIS |
|---------------|----------------|
| Q1 à Q5 | N1 |
| Q6 à Q15 | N2 |
| Q16 à Q20 | N3 |

COUVERTURE_NIVEAU = OK / WARN / FAIL selon le ratio d'items compatibles.
FAIL = HUMAN_GATE obligatoire avant B2.

---

# ÉTAPE 4 — PEUPLEMENT POOLS.tsv

| Colonne | Valeur |
|---------|--------|
| POOL_ID | IF-01 à IF-05 / QV-01 à QV-15 |
| TYPE | IF / QV |
| POSITION_QUIZ | Q1 à Q20 |
| THEME_LABEL | label contrôlé du pool |
| MODE | SIMPLE / AGRÉGÉ |
| SOUS_THEMES | liste des sous-thèmes |
| ITEMS_ASSIGNES | liste ITEM_ID assignés |
| COUVERTURE_NIVEAU | OK / WARN / FAIL |
| STOCK_CIBLE | 8 / 12 / 15 |
| STOCK_ACTUEL | calculé depuis QUESTIONS.tsv |

---

# ÉTAPE 5 — ASSIGNATION ANGLES AUX POOLS

Mettre à jour ANGLES.tsv :
- remplir POOL_CIBLE
- mettre STATUT = RÉSERVÉ
- valider STOCK_CIBLE atteignable

---

# ÉTAPE 6 — CONTRÔLE ANTI-COLLISION

- aucun angle assigné à deux pools
- aucun item majeur dans deux pools
- conformité EXCLUDED_POOLS
- angles IF absents des QV

---

# ÉTAPE 7 — GÉNÉRATION SOMMAIRE

Lancer :
`python _FACTORY/_SCRIPTS/generate_sommaire.py _LIGNES/[THEME]`

---

# ÉTAPE 8 — HUMAN_GATE (A4→B2)

Avant B2 :
- [ ] 20 pools constitués
- [ ] COUVERTURE_NIVEAU ≠ FAIL
- [ ] Pools AGRÉGÉ validés
- [ ] Angles assignés
- [ ] Stocks atteignables
- [ ] Anti-collision validé
- [ ] SOMMAIRE généré

---

# METRICS

A4 est valide si :
- exactement 20 pools définis
- COUVERTURE_NIVEAU ∈ {OK, WARN}
- chaque pool atteint son stock cible
- aucun angle assigné à deux pools
- pools AGRÉGÉ validés

---

*MDE_A4_tableur_pools.md*
*Version 3.2 — 2026-05-25 — Pipeline V2.1*
