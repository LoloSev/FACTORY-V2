# MDE B2 — GÉNÉRATION DES QUESTIONS

VERSION: 2.1 (PIPELINE V2.1)
DATE: 2026-05-25
STATUS: ACTIVE_REFERENCE
PIPELINE_SCOPE: B2
IA_COMPATIBLE: TRUE
IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE

DEPENDENCY:
- PIPELINE_V2.md
- POOLS.tsv validé (gate A4)
- ANGLES.tsv validé (gate A3)
- STD_B2_generation_rules.md
- STD_B2_recevabilite_pedagogique.md
- STD_GLOBAL_pool_collision_rules.md
- STD_GLOBAL_quiz_architecture_rules.md

---

## MACHINE-FIRST EXECUTION CONTRACT

INPUT:
- POOLS.tsv validé
- ANGLES.tsv avec POOL_CIBLE renseigné
- STD_B2_generation_rules.md
- STD_B2_recevabilite_pedagogique.md

PROCESS:
1. traiter un pool à la fois
2. sélectionner angles DISPONIBLE du pool
3. appliquer hard blockers avant écriture
4. générer la question au NIVEAU_ANGLE de l'angle
5. écrire uniquement les questions PASS

OUTPUT:
- QUESTIONS.tsv peuplé
- STATUT_B2 renseigné pour chaque question
- flags bloquants explicités

ACCEPTANCE_CRITERIA:
- QUESTIONS_WITH_Q_ID_RATE = 100%
- QUESTIONS_WITH_POOL_ID_RATE = 100%
- QUESTIONS_WITH_ANGLE_ID_RATE = 100%
- QUESTIONS_WITH_NIVEAU_QUESTION_RATE = 100%
- NIVEAU_QUESTION_FROM_ANGLE_RATE = 100%
- LIBELLE_WORD_COUNT_MAX = 15 (RULE-B2-HB-000 — STD_B2_generation_rules.md)
- ANSWER_UNIQUE_RATE = 100%
- PED_BLOCKER_COUNT = 0
- HARD_COLLISION_COUNT = 0
- FILLER_COUNT = 0

FAILURE_CASES:
- missing NIVEAU_QUESTION
- question without ANGLE_ID
- NIVEAU_QUESTION not derived from NIVEAU_ANGLE
- answer ambiguous or revealed
- filler or hard collision detected

---
## OBJECTIF

Peupler QUESTIONS.tsv, pool par pool, en ciblant le NIVEAU_ANGLE de chaque angle.
Produire des questions propres, recevables, non-fillers, prêtes pour B3.

---

## ENTRÉE / SORTIE

| | |
|---|---|
| FROM | A4 — POOLS.tsv validé |
| INPUT | POOLS.tsv + ANGLES.tsv |
| OUTPUT | QUESTIONS.tsv peuplé (Q_ID / POOL_ID / ANGLE_ID / LIBELLE / REPONSE / NIVEAU_QUESTION / TYPE_Q / STATUT_B2) |
| HUMAN_VALIDATION | required per pool; allowed statuses: APPROVE / REJECT / REWORK |
| BLOCK_IF | filler, collision, angle sans signal GAME_VALUE_FLAG = TRUE, question irrecevable |

---

## PRINCIPE FONDAMENTAL V2.1

**La difficulté est évaluée à l'angle (NIVEAU_ANGLE en A3) et assignée à la question (NIVEAU_QUESTION en B2).**

RETEX_REF: RETEX_MDE_B2_GENERATION_001

Le pool ne porte plus de niveau fixe. NIVEAU_QUESTION = NIVEAU_ANGLE de l'angle source — assigné par l'IA, non hérité du pool.

---

## SÉQUENCE DE TRAVAIL (PAR POOL)

1. Lire le pool dans POOLS.tsv (THEME_LABEL / MODE / SOUS_THEMES / COUVERTURE_NIVEAU / ITEMS_ASSIGNES)
2. Lire les angles disponibles dans ANGLES.tsv (POOL_CIBLE = ce pool / STATUT = DISPONIBLE)
3. VALIDER si une passe de cadrage pré-génération est nécessaire (RULE-B2-SW-001)
4. Proposer la répartition calculée du pool (angles × questions)
5. Pour chaque question candidate :
   a. Triple filtre angle (RULE-B2-HB-004) : disponibilité → anti-collision → signal GAME_VALUE_FLAG = TRUE
   b. Checklist 8 filtres rédaction (RULE-B2-HB-002)
   c. VALIDATION recevabilité pédagogique (STD_B2_recevabilite_pedagogique.md)
6. Remplir QUESTIONS.tsv pour les questions validées
7. Marquer STATUT_B2 = SOUMIS
8. Soumettre le pool à HUMAN_GATE
9. Après validation : STATUT_B2 = VALIDÉ ou REJETÉ

---

## COLONNES FEUILLE QUESTIONS À REMPLIR

| Colonne | Règle |
|---------|-------|
| Q_ID | [POOL_ID]-Q[NNN] — auto-généré séquentiellement |
| POOL_ID | copié depuis POOLS |
| ANGLE_ID | référence ANGLES.tsv |
| LIBELLE | texte de la question (filtres appliqués) |
| REPONSE | réponse correcte |
| NIVEAU_QUESTION | = NIVEAU_ANGLE de l'angle source — ne pas modifier manuellement |
| TYPE_Q | 1 / 2 / 3 / 4 / 5 (voir ci-dessous) |
| STATUT_B2 | SOUMIS (puis VALIDÉ / REJETÉ après gate humaine) |

## Classification TYPE_Q

| Type | Catégorie |
|------|-----------|
| 1 | Identification (personne, entité) |
| 2 | Nombre (stat, quantité) |
| 3 | Année / Édition |
| 4 | Lieu / Géographie |
| 5 | Correspondance (critères multiples) |

---

## RÈGLES CRITIQUES (RÉFÉRENCES)

Toutes les règles détaillées sont dans STD_B2_generation_rules.md.
Résumé opérationnel :

**HARD BLOCKERS — arrêt immédiat si violation :**
- Zéro filler (RULE-B2-HB-001)
- 8 filtres rédaction (RULE-B2-HB-002) → STD_B2_generation_rules.md
- Corrections repassent les 8 filtres (RULE-B2-HB-003)
- Triple filtre angle (RULE-B2-HB-004) : disponibilité → collision → signal GAME_VALUE_FLAG = TRUE
- Séquence soumission (RULE-B2-HB-005) : angle → anti-collision → conformité → HUMAN_GATE
- Réponse univoque (RULE-B2-HB-006)
- Désambiguïsation homonymes (RULE-B2-HB-007)

**Recevabilité pédagogique — arrêt si violation :**
- TYPE-PED-1 : réponse révélée dans le libellé
- TYPE-PED-2 : déductible sans connaissance
- TYPE-PED-3 : connaissance triviale
- TYPE-PED-4 : ambiguïté de réponse
(STD_B2_recevabilite_pedagogique.md)

**SOFT — signaler et documenter :**
- Passe de cadrage si pool descriptif/ouvert (RULE-B2-SW-001)
- VALIDER absents majeurs (RULE-B2-SW-002)
- Répartition interne = décision humaine (RULE-B2-SW-003)
- Arbitrages évidents : appliquer sans redemander (RULE-B2-SW-004)

---

## POOLS AGRÉGÉS

Pour un pool MODE=AGRÉGÉ :
- Traiter les sous-thèmes séquentiellement
- VALIDER conformité des questions entre sous-thèmes
- VALIDER que les distracteurs futurs (B3) resteront valides à travers les sous-thèmes
- Ne pas signaler le mode AGRÉGÉ dans le libellé des questions — transparent pour le joueur

---

## SIGNALEMENT DÉFICIT

Si un pool ne peut pas atteindre STOCK_CIBLE avec des angles THRESHOLD_VALIDATED :
- Signaler : angles utilisés / réservés / restants (RULE-B2-ALT-001)
- Arrêter la génération du pool
- Attendre décision humaine : enrichir BIB (ajouter matière culturelle — gate humaine requise) / fusionner / réduire stock cible
- Ne jamais proposer de filler comme solution

---

## HUMAN_GATE (GATE B2→B3)

Par pool, avant de passer au suivant :
- [ ] Toutes les questions passent les 8 filtres
- [ ] Toutes les questions sont pédagogiquement recevables
- [ ] Anti-collision vérifié
- [ ] STOCK_ACTUEL ≥ STOCK_CIBLE (ou déficit signalé)
RETEX_REF: RETEX_MDE_B2_GENERATION_002

Après HUMAN_GATE :
- [ ] STATUT_B2 = VALIDÉ (ou REJETÉ + remplacement)
- [ ] Passer au pool suivant

---

*MDE_B2_generation.md*
*Version 2.1 — 2026-05-25 — Pipeline V2.1*
*Remplace : v2.0 — CIBLE_NIVEAU pool → NIVEAU_QUESTION par question (alignement C-010/C-011)*


