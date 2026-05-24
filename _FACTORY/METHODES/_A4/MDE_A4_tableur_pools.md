IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE


# MDE A4 — CONSTITUTION DES POOLS → POOLS.tsv

Version : 3.1 (PIPELINE V2.1)
Date : 2026-05-25
Remplace : MDE_A4 v2.0 (pipeline V2 — CIBLE_NIVEAU fixe par pool)

DEPENDENCY:
- PIPELINE_V2.md
- MDE_A3_traitement.md (v4.1)
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

MACHINE_PROPOSAL:
- proposer 20 pools à partir des counts ITEMS/ANGLES/RICHESSE
- exposer tout écart aux seuils ACCEPTANCE_CRITERIA
HUMAN_GATE:
- autoriser uniquement APPROVE / RECONFIGURE / REJECT avec motif codé

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

## Règle de fusion AGRÉGÉ (RULE-ARCH-005)

Si une section LIGHT ou STANDARD ne peut pas atteindre seule le stock cible d'un pool :
- VALIDER si elle partage ≥2 critères avec une section de <5 items
- Si oui → fusionner en pool MODE=AGRÉGÉ
- Le pool AGRÉGÉ reste une unité de tirage unique pour le joueur
- Les questions des sous-thèmes agrégés doivent partager un registre commun
- Les distracteurs doivent rester valides à travers tous les sous-thèmes

---

# ÉTAPE 3 — VÉRIFICATION COUVERTURE NIVEAU (RULE-ARCH-008)

Le pool est purement thématique. La position dans le quiz définit le niveau que le moteur lui demandera (NIVEAU_REQUIS — calculé, non stocké) :

| Position quiz | NIVEAU_REQUIS (moteur) |
|---------------|------------------------|
| Q1 à Q5 | N1 |
| Q6 à Q15 | N2 |
| Q16 à Q20 | N3 |

Pour chaque pool, calculer COUVERTURE_NIVEAU :

```
NIVEAU_REQUIS = dérivé de POSITION_QUIZ (non stocké dans POOLS)
ITEMS_COMPATIBLES = items du pool avec NIVEAU_POTENTIEL = NIVEAU_REQUIS ou MULTI
RATIO = ITEMS_COMPATIBLES / TOTAL_ITEMS_POOL

COUVERTURE_NIVEAU = OK   si RATIO ≥ 0.30
COUVERTURE_NIVEAU = WARN si RATIO ∈ [0.01, 0.30[
COUVERTURE_NIVEAU = FAIL si RATIO = 0
```

COUVERTURE_NIVEAU = FAIL → HUMAN_GATE obligatoire avant B2.
Options : réassigner des items au pool / modifier POSITION_QUIZ / enrichir le BIB.

NOTE : seuil 0.30 = valeur initiale à calibrer sur MAYENNE (RULE-GOV-002).

---

# ÉTAPE 4 — PEUPLEMENT POOLS.tsv

RETEX_REF: RETEX_MDE_A4_TABLEUR_POOLS_001

| Colonne | Valeur |
|---------|--------|
| POOL_ID | IF-01/IF-02 (Q1-Q2) / IF-03/IF-04/IF-05 (Q3-Q5) / QV-01 à QV-15 (Q6-Q20) |
| TYPE | IF / QV |
| POSITION_QUIZ | Q1 à Q20 |
| THEME_LABEL | label contrôlé du pool |
| MODE | SIMPLE / AGRÉGÉ |
| SOUS_THEMES | liste des sous-thèmes (si AGRÉGÉ) |
| ITEMS_ASSIGNES | liste des ITEM_ID assignés à ce pool |
| COUVERTURE_NIVEAU | OK / WARN / FAIL — calculé en Étape 3 |
| STOCK_CIBLE | 8 (IF Q1-Q2) / 12 (IF Q3-Q5) / 15 (QV) |
| STOCK_ACTUEL | formule =COUNTIF(QUESTIONS[POOL_ID], POOL_ID) |

---

# ÉTAPE 5 — ASSIGNATION ANGLES AUX POOLS

Mettre à jour ANGLES.tsv :
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
- VALIDER par critère mesurable que les angles IF ne sont pas dans les QV (RULE-IF-001)

---

# ÉTAPE 7 — GÉNÉRATION SOMMAIRE

Lancer : `python _FACTORY/_SCRIPTS/generate_sommaire.py _LIGNES/[THEME]`

Calcule depuis les TSV : POOL_ID / TYPE / POSITION_QUIZ / THEME_LABEL / MODE / COUVERTURE_NIVEAU / STOCK_CIBLE / STOCK_ACTUEL / Q_PASS / Q_WARNING / Q_FAIL / PCT_COMPLET.

Le SOMMAIRE est la vue de pilotage du quiz — regénéré à la demande, pas maintenu manuellement.

---

# ÉTAPE 8 — HUMAN_GATE (GATE A4→B2)

Avant de passer à B2 :

- [ ] 20 pools constitués (thématiques)
- [ ] COUVERTURE_NIVEAU ≠ FAIL pour chaque pool
- [ ] Pools AGRÉGÉ validés (conformité sous-thèmes confirmée)
- [ ] Angles assignés pour chaque pool
- [ ] Stocks cibles atteignables
- [ ] Anti-collision inter-pools vérifié
- [ ] SOMMAIRE généré (generate_sommaire.py)

Décisions humaines attendues :
- Validation des 20 pools (ou reconfiguration)
- Validation des pools AGRÉGÉ
- Décision sur tout pool COUVERTURE_NIVEAU = FAIL (réassignation / repositionnement / enrichissement BIB)

---

# METRICS

A4 est valide si :
- exactement 20 pools définis
- COUVERTURE_NIVEAU ∈ {OK, WARN} pour chaque pool (FAIL = bloquant)
- chaque pool a assez d'angles pour atteindre son stock cible
- aucun angle assigné à deux pools
- les pools AGRÉGÉ ont une conformité documentaire vérifiée

---

*MDE_A4_tableur_pools.md*
*Version 3.1 — 2026-05-25 — Pipeline V2.1*
*Remplace : v3.0 — OUTPUT TSV (POOLS.tsv / ANGLES.tsv) / SOMMAIRE via script / dépendance A3 v4.1*


