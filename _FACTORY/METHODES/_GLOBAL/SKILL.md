IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE


---
name: quizz-factory
description: Skill pour la production de quiz selon la méthode QUIZZZ FACTORY — Pipeline V2. Déclencher pour : générer des questions (B2), ajouter des distracteurs (B3), auditer un pool (B5), ou toute étape du workflow A/B. S'applique à tous les quiz (Mayenne, Rock, Rap, cas source, Internet, Séries...).
RETEX_REF: RETEX_SKILL_001
---

# QUIZZZ FACTORY — Skill de production (Pipeline V2)

VERSION: 2.0 (PIPELINE V2)
DATE: 2026-05-18
DEPENDENCY: PIPELINE_V2.md / HIERARCHIE_REGLEMENTAIRE.md

## Règles comportementales (toujours actives)
- Fais strictement ce qui est demandé
- Pas de suggestions non sollicitées
- Pas de récapitulatifs après chaque action
- Réponses courtes, action immédiate
- Signaler toute FAILURE_CASE ou CONSISTENCY_FAILURE détectée

## RÈGLE UNIVERSELLE — RECEVABILITÉ DES QUESTIONS

[RULE-UNIV-Q-001]
**Aucune question n'est recevable sans avoir passé l'intégralité des BLOCKERs mécaniques, quelle que soit son origine, son statut ou l'étape du pipeline.**

S'applique à : toute question générée, importée, récupérée, copiée, reformulée ou déplacée.
Sans exception : statut RECUPEREE, RETRO, DRAFT, WIP, ou tout autre ne crée aucune exemption.

BLOCKERs mécaniques (vérification automatique, sans jugement) :
- Réponse absente → FAIL
- Réponse présente dans le libellé → FAIL (règle absolue, sans nuance sémantique)
- Libellé > 15 mots → FAIL
- Formulation négative complexe → FAIL
- TYPE_Q non classifié → FAIL

Une question FAIL n'est jamais proposée, jamais comptée, jamais intégrée au stock.
Elle est signalée et traitée avant toute autre action.

---

## Principe fondamental V2

**La difficulté est top-down, jamais bottom-up.**
- Le CIBLE_NIVEAU (N1/N2/N3) est fixé par la position du pool dans le quiz (RULE-ARCH-004)
- Il descend : pool → question → distracteurs
- L'IA génère POUR atteindre ce niveau — elle ne l'assigne pas depuis l'item
- Les items ont une RICHESSE (DENSE/STANDARD/LIGHT), pas un niveau

**Artefact unique : QUIZ_[THEME].xlsx** — 7 feuilles enrichies progressivement :
CONFIG / ITEMS / ANGLES / POOLS / QUESTIONS / DISTRACTEURS / QA

---

## Règles universelles (tous quiz)

- Questions courtes : 10 mots max, lisibles sur mobile
- Format QCM : 4 choix (A/B/C/D), 1 seule bonne réponse incontestable
- Jamais de formulation négative complexe
- Jamais de réponse dans l'énoncé
- Jamais de connaissance ultra-spécialisée
- Équilibre bonnes réponses : ≈25% par lettre sur le stock
- Travailler pool par pool, jamais globalement

---

## Étape B2 — Générer des questions

**Référence :** `MDE_B2_generation.md` v2.0

**Principe :** Chaque question hérite automatiquement du CIBLE_NIVEAU de son pool (défini en A4).

**Séquence par pool :**
1. Lire POOL_ID / THÈME_ÉDITORIAL / CIBLE_NIVEAU / ITEMS_ASSIGNÉS depuis feuille POOLS
2. Lire les angles disponibles depuis feuille ANGLES (POOL_CIBLE = ce pool)
3. Triple filtre angle (RULE-B2-HB-004) : disponibilité → anti-collision → valeur de jeu
4. Checklist 8 filtres rédaction (RULE-B2-HB-002)
5. VALIDATION recevabilité pédagogique (4 types — voir ci-dessous)
6. Remplir feuille QUESTIONS — STATUT_B2 = SOUMIS
7. Attendre validation humaine avant pool suivant

**Colonnes feuille QUESTIONS :**
`Q_ID / POOL_ID / ANGLE_ID / LIBELLÉ / RÉPONSE / CIBLE_NIVEAU / TYPE_Q / STATUT_B2`

**Classification TYPE_Q :**
- Type 1 : Identification (personne, entité)
- Type 2 : Nombre (stat, quantité)
- Type 3 : Année / Édition
- Type 4 : Lieu / Géographie
- Type 5 : Correspondance (critères multiples)

**Recevabilité pédagogique — 4 types bloquants :**
- TYPE-PED-1 : réponse révélée dans le libellé → BLOCKER
- TYPE-PED-2 : déductible sans connaissance → BLOCKER
- TYPE-PED-3 : connaissance triviale → BLOCKER
- TYPE-PED-4 : ambiguïté de réponse → BLOCKER

Référence : `STD_B2_recevabilite_pedagogique.md`

**Hard blockers B2 :**
- Zéro filler (RULE-B2-HB-001)
- 8 filtres rédaction (RULE-B2-HB-002)
- Réponse univoque (RULE-B2-HB-006)
- Désambiguïsation homonymes (RULE-B2-HB-007)

---

## Étape B3 — Générer et auditer les distracteurs

**Référence :** `MDE_B3_distracteurs.md` v2.0

**Principe :** Les distracteurs servent le CIBLE_NIVEAU — ils ne le définissent pas.

**Colonnes feuille DISTRACTEURS :**
`Q_ID / D1 / D2 / D3 / NIVEAU_CONFIRMÉ / ÉCART_CIBLE / STATUT_B3`

**ÉCART_CIBLE :**
- OK : NIVEAU_CONFIRMÉ = CIBLE_NIVEAU
- SURQUALIFIÉ : `NIVEAU_CONFIRMÉ` inférieur au `CIBLE_NIVEAU` ou distance distracteurs au-dessus de la plage cible → resserrer
- SOUS-QUALIFIÉ : `NIVEAU_CONFIRMÉ` supérieur au `CIBLE_NIVEAU` ou distance distracteurs sous la plage cible → élargir

---

### PASS 1 — Génération

**Processus :**
1. Lire Q_ID / TYPE_Q / RÉPONSE / CIBLE_NIVEAU depuis feuille QUESTIONS
2. Charger règles TYPE-spécifiques (STD_B3_distractor_rules.md)
3. Générer 10-15 candidats depuis sources réelles (pas d'invention)
4. Filtrer par CONSISTENCY : partage ≥1 critère avec la bonne réponse
5. Calibrer sur CIBLE_NIVEAU (espacement N1 large / N2 moyen / N3 minimal)
6. Valider format : casse, accents, structure CONSISTENCY_VALIDATED
7. Sélectionner 3 meilleurs + évaluer NIVEAU_CONFIRMÉ et ÉCART_CIBLE

**Format strict :**
```
Q_ID : [identifiant]
CIBLE_NIVEAU : [N1/N2/N3]
D1 : [distracteur]
D2 : [distracteur]
D3 : [distracteur]
NIVEAU_CONFIRMÉ : [N1/N2/N3]
ÉCART_CIBLE : [OK / SURQUALIFIÉ / SOUS-QUALIFIÉ]
TYPE_Q : [1-5]
```

---

### PASS 2 — Audit

**Métriques vérifiées :**
- Hard collisions (distractor = réponse correcte ailleurs) → seuil = 0, BLOCKER
- Format homogénéité → ≥99%, WARNING
- Distribution difficulté N1/N2/N3 → 30/40/30 ±5%, WARNING
- Distribution TYPE_Q → chaque TYPE >10%, WARNING
- Taux réutilisation inter-questions → <5%, WARNING
- Plausibilité TYPE 1/5 → ≥80%, WARNING
- Concentration source unique → ≤3%, WARNING
- Era clustering → ≤50% même ère, WARNING
- ÉCART_CIBLE ≠ OK → 0 idéalement, WARNING

**Decision gate :**
- ✅ GO : tous critères verts → procéder à B5
- ⚠️ CONDITIONAL_GO : FAILURE_CASE mineurs → PASS 3 requis
- ❌ NO_GO : FAILURE_CASE critiques → retour PASS 1

**Validation humaine obligatoire après PASS 2.**

---

### PASS 3 — Correction (si CONDITIONAL_GO)

**Processus par flag :**
- HARD_COLLISION → remplacer par entité différente
- ÉCART_CIBLE=SURQUALIFIÉ → resserrer les distracteurs
- ÉCART_CIBLE=SOUS-QUALIFIÉ → élargir l'écart
- FORMAT_MISMATCH → reformatter pour homogénéité
- PLAUSIBILITY_LOW → remplacer par option plus reconnaissable
- SOURCE_CONCENTRATION → varier les sources
- ERA_CLUSTERING → diversifier les époques

**Traçabilité :** documenter dans PROCESS_[THEME].md uniquement si correction non triviale.

---

### Synthèse : Entonnoir 3-Passes

```
Feuille QUESTIONS (B2 validé)
    ↓
PASS 1 : générer D1/D2/D3 calibrés sur CIBLE_NIVEAU
    ↓
PASS 2 : auditer collisions / format / distribution / ÉCART_CIBLE
    ↓
Gate humaine : GO / CONDITIONAL_GO / NO_GO
    ↓ (si CONDITIONAL_GO)
PASS 3 : corriger items flaggés
    ↓
Feuille DISTRACTEURS complète → B5 AUDIT
```

---

**Contraintes universelles :**
- Anti-collision obligatoire : aucun distracteur ≠ bonne réponse ailleurs (RULE-TRANS-001)
- Format homogène : réponse + 3 distracteurs = même format (RULE-HB-DIST-003)
- Pas d'invention : tous noms, chiffres, lieux, années = réels et vérifiables (RULE-HB-DIST-002)
- Unicité intra-question : 3 distracteurs distincts entre eux (RULE-TRANS-004)
- Unicité inter-questions : réutilisation <5% (RULE-TRANS-005)

---

## Étape B5 — Audit QA_STATUS

**Référence :** `MDE_B5_audit.md` v2.0

**Principe :** Une question à la fois. Décision humaine avant de passer à la suivante.

**Format de présentation obligatoire :**
```
Q_ID      : [identifiant]
Pool      : [POOL_ID] — [THÈME_ÉDITORIAL]
Position  : Q[N] — CIBLE_NIVEAU : N[1/2/3]
Type      : TYPE [1/2/3/4/5]

Question  : [libellé]

A. [D1]
B. [D2]
C. [réponse correcte]
D. [D3]

Bonne réponse : [lettre]. [réponse]
Niveau confirmé : N[1/2/3] — Écart cible : [OK / SURQUALIFIÉ / SOUS-QUALIFIÉ]

Flags B3   : [PASS / WARNING — détail]
Flags PED  : [aucun / TYPE-PED-N — détail]
Flags VEILLE : [aucun / TYPE-[N] — marqueur détecté]

Proposition : CONSERVER / MODIFIER / REJETER / DÉPLACER
```

**VALIDATIONS B5 spécifiques :**

Recevabilité pédagogique (4 types) :
- TYPE-PED-1 : réponse révélée dans le libellé ?
- TYPE-PED-2 : déductible sans connaissance ?
- TYPE-PED-3 : connaissance triviale ?
- TYPE-PED-4 : ambiguïté de réponse ?
Si OUI → FLAG IRRECEVABLE + MODIFIER ou REJETER

Veille obsolescence (RULE-OBS-008) :
Détecter : "dernier", "jamais", "seul", "record", "plus grand/récent/de X", tout superlatif absolu
Si détecté → FLAG VEILLE + QA_STATUS = WARNING (non bloquant)

**Colonnes feuille QA :**
`Q_ID / QA_STATUS / FLAGS / DÉCISION / NOTES`

**Les 4 décisions :**
- CONSERVER → QA_STATUS = PASS
- MODIFIER → corriger, repasser 8 filtres, QA_STATUS = PASS après validation
- REJETER → QA_STATUS = FAIL (bloque export si non remplacée)
- DÉPLACER → mettre à jour POOL_ID dans feuille QUESTIONS

**En fin d'audit B5 :** produire FICHE_VEILLE (RULE-OBS-010) — obligatoire avant export.

**Blocages export :**
- QA_STATUS = FAIL sur ≥1 question non remplacée
- ÉCART_CIBLE ≠ OK non résolu sur ≥1 question
- FICHE_VEILLE absente
- STOCK_ACTUEL < STOCK_CIBLE sur ≥1 pool

---

## Variantes par type de quiz

### Type : Entité géographique (ex: Mayenne)
- Questions strictement dans le territoire concerné
- Diversité géographique : max 5% par ville
RETEX_REF: RETEX_SKILL_002

### Type : Culture populaire (Rock, Rap, cas source, Internet, Séries)
RETEX_REF: RETEX_SKILL_003
- Max 2 questions par artiste/sujet/personnage
- Ne jamais répéter le mot-clé du thème dans les questions (implicite)
- VALIDER les liens croisés : une question ne doit jamais donner la réponse d'une autre
- Validation par blocs, attendre validation humaine avant de continuer

---

## Gestion des tokens et de la session (RULE-TOKEN-MONITOR-001/002/003)

**Comportement obligatoire — tous contextes :**

Avant chaque tool call ou réponse, évaluer :
- Peut-on compresser le contexte chargé ?
- Peut-on batcher des requêtes ?
- Peut-on remplacer narratif par IDs ?
RETEX_REF: RETEX_SKILL_004
- Peut-on réutiliser résultats précédents ?

Si opportunité ≥5% tokens estimés → insérer avant action :
```
⚡ OPT: [description] → [économie estimée]
```
Seuil minimum 5% — ne pas signaler <2%.

**Session Resumption (RULE-SRP-001/002/003/004) :**

Générer proactivement un `SESSION_RESUMPTION_PROMPT` avant saturation de contexte (pas après).

Format fichier : `[TASK-CODE]_SESSION_[N]_RESUME_[YYYYMMDD].md`
Contenu obligatoire : état session antérieure / fichiers modifiés / travail restant / prompt copie-coller / tokens estimés prochaine session.
Localisation : racine `TRAVAIL EN COURS`.

---

## Références documentaires

**Pipeline :**
- `PIPELINE_V2.md` — Vue d'ensemble V2, artefacts, feuilles xlsx, séquence complète
- `HIERARCHIE_REGLEMENTAIRE.md` — 5 niveaux N1→N5, parenté de chaque règle

**MDE :**
- `MDE_A3_traitement.md` v3.0 — Traitement BIB, RICHESSE items, création xlsx
- `MDE_A4_tableur_pools.md` v2.0 — Constitution pools, CIBLE_NIVEAU top-down, SOMMAIRE
- `MDE_B2_generation.md` v2.0 — Génération questions, héritage CIBLE_NIVEAU
- `MDE_B3_distracteurs.md` v2.0 — Entonnoir 3-passes, ÉCART_CIBLE
- `MDE_B5_audit.md` v2.0 — Audit QA, FICHE_VEILLE, blocages export

**STD :**
- `STD_GLOBAL_quiz_architecture_rules.md` — Architecture 20 pools, crescendo N1/N2/N3
- `STD_GLOBAL_pool_collision_rules.md` — Anti-collision inter-pools
- `STD_B2_generation_rules.md` — 8 filtres, triple filtre angle, zéro filler
- `STD_B2_recevabilite_pedagogique.md` — 4 types irrecevabilité pédagogique
- `STD_B3_distractor_rules.md` — Règles TYPE-spécifiques, HARD/SOFT/OPT
- `STD_OBSOLESCENCE_WATCH_RULES.md` — 5 types déclencheurs, FICHE_VEILLE

**Glossaire :**
- `glossaire_documentaire_factory.md` — Définitions RICHESSE, CIBLE_NIVEAU, ÉCART_CIBLE, QA_STATUS…


