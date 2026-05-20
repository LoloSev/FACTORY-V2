# HIÉRARCHIE RÉGLEMENTAIRE — QUIZZZ FACTORY

VERSION: 1.0
DATE: 2026-05-18
STATUS: ACTIVE_REFERENCE
PIPELINE_SCOPE: GLOBAL
IA_COMPATIBLE: TRUE
IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE

DEPENDENCY:
- MASTER_ARCHITECTURE.md
- PIPELINE_V2.md

---

# PRINCIPE FONDATEUR

Toute règle de la FACTORY doit répondre à une règle hiérarchiquement supérieure.
Une règle sans parent est invalide et ne peut pas être intégrée à un STD.
Plus on descend dans le détail du process, plus on descend dans la hiérarchie.

**5 niveaux :**
```
N1 — CONSTITUTION        → axiomes immuables du projet
N2 — LOIS ORGANIQUES     → architecture et gouvernance
N3 — STANDARDS (STD)     → règles opérationnelles
N4 — MÉTHODES (MDE)      → procédures d'exécution
N5 — ANNEXES THÉMATIQUES → règles spécifiques à un quiz
```

**Règle méta :**
Modifier une règle N[k] peut invalider des règles N[k+1] qui en dépendent.
Toute modification d'une règle de niveau ≤ N2 déclenche une revue des niveaux inférieurs.

---

# NIVEAU 1 — CONSTITUTION

> Immuable sauf décision de refonte globale du projet.
> Changer une règle constitutionnelle = remettre en cause l'identité du projet.

[C-001]
**Expérience de jeu**
Le quiz est une expérience de 90 secondes pour 20 questions, mobile, rejouable.

[C-002]
**Structure de tirage**
Exactement 20 pools. Une question tirée par pool par partie. Toujours.

[C-003]
**Stock cible**
Le stock cible standard est de 277 questions par quiz.

[C-004]
**Format QCM**
4 choix par question. 1 seule bonne réponse. Pas d'ambiguïté possible.

[C-005]
**Progression de difficulté**
La difficulté augmente du début à la fin d'une partie. Cet ordre est immuable.

[C-006]
**Autorité éditoriale humaine**
L'humain est l'architecte éditorial final. La machine prépare, propose, signale.
Elle ne décide jamais seule d'une règle, d'un contenu, ou d'une validation finale.

[C-007]
**Vérifiabilité factuelle**
Tout contenu du quiz — réponses, distracteurs, angles — doit être factuellement vérifiable.
Zéro invention non signalée.

[C-008]
**Rejouabilité**
La variété est une contrainte structurelle. Un quiz est répétitif si une même entité correcte apparaît >3 fois ou si une même catégorie dépasse 45 %.

[C-009]
**Recevabilité universelle des questions**
Aucune question n'est recevable sans avoir passé l'intégralité des BLOCKERs mécaniques, quelle que soit son origine, son statut ou l'étape du pipeline.
S'applique sans exception à toute question générée, importée, récupérée, copiée, reformulée ou déplacée.
Source : SKILL.md RULE-UNIV-Q-001

---

# NIVEAU 2 — LOIS ORGANIQUES

> Modifiables par décision explicite et documentée.
> Chaque loi cite sa règle constitutionnelle parente.

[L-001] **Architecture des 20 pools** → C-002
2 IF-SF + 3 IF-ROT + 15 QV.
Source : STD_GLOBAL_quiz_architecture_rules.md RULE-ARCH-001/002

[L-002] **Crescendo N1/N2/N3** → C-005
Q1-Q5 = N1 / Q6-Q15 = N2 / Q16-Q20 = N3. Ordre immuable.
Source : STD_GLOBAL_quiz_architecture_rules.md RULE-ARCH-004

[L-003] **Difficulté top-down** → C-005 + C-006
La difficulté descend du pool vers la question et les distracteurs.
Elle n'est jamais assignée bottom-up depuis l'item.
Source : PIPELINE_V2.md

[L-004] **Pool agrégé possible** → C-002 + C-003
Un pool peut regrouper plusieurs sous-thèmes faibles pour atteindre son stock cible.
Un pool = une unité de tirage, pas une unité thématique unique.
Source : STD_GLOBAL_quiz_architecture_rules.md RULE-ARCH-005

[L-005] **Xlsx colonne vertébrale** → C-006
Un seul artefact vivant (xlsx) progressivement enrichi.
Les fichiers intermédiaires (.txt) sont éliminés au profit des feuilles xlsx.
Source : PIPELINE_V2.md

[L-006] **Richesse des items, pas difficulté** → L-003
Les items ont une RICHESSE documentaire (DENSE/STANDARD/LIGHT).
La difficulté appartient au pool, pas à l'item.
Source : MDE_A3_traitement.md v3.0

[L-007] **Gouvernance législative — anti-explosion** → C-006
Avant toute nouvelle règle : déjà couverte ? généralisable ? remplace une règle non mesurable ? observée sur ≥2 cobayes ?
Source : MASTER_ARCHITECTURE.md RULE-GOV-002

[L-008] **Apprentissage continu — intervention humaine incontournable** → C-006
Le projet apprend à chaque quiz. L'AVANT/APRÈS humain est non-négociable au niveau de maturité actuel.
Source : MASTER_ARCHITECTURE.md RULE-GOV-001

[L-009] **Anti-collision inter-pools** → C-002 + C-008
Un fait documentaire majeur ne peut appartenir qu'à un seul pool.
Une réponse correcte dans un pool ne peut être distracteur dans un autre.
Source : STD_GLOBAL_pool_collision_rules.md

[L-010] **Zéro filler** → C-003 + C-006
Le stock cible est une cible de QA_STATUS, pas de quantité.
Atteindre le stock par des questions sans valeur de jeu est interdit.
Source : STD_B2_generation_rules.md RULE-B2-HB-001

---

# NIVEAU 3 — STANDARDS (STD)

> Règles opérationnelles dérivées des lois organiques.
> Chaque règle cite sa loi organique parente.

## STD_NAMING_CONVENTIONS.md

| Règle | Énoncé condensé | Parent N2 |
|-------|-----------------|-----------|
| RULE-NAMING-001 | Code THEME en majuscules, sans accents ni espaces | L-005 |
| RULE-NAMING-002 | Préfixe d'étape sur fichiers intermédiaires, absent sur artefacts finaux | L-005 |
| RULE-NAMING-003 | Split NN autorisé uniquement pour BIB volumineux (A2) | L-005 |
RETEX_REF: RETEX_HIERARCHIE_REGLEMENTAIRE_001

## STD_GLOBAL_quiz_architecture_rules.md

| Règle | Énoncé condensé | Parent N2 |
|-------|-----------------|-----------|
| RULE-ARCH-001 | 20 pools obligatoires | L-001 |
| RULE-ARCH-002 | 2 IF-SF + 3 IF-ROT + 15 QV | L-001 |
| RULE-ARCH-003 | Stock cible 277 questions | C-003 |
| RULE-ARCH-004 | Q1-5=N1 / Q6-15=N2 / Q16-20=N3 | L-002 |
| RULE-ARCH-005 | Pool peut agréger sous-thèmes faibles | L-004 |

## STD_GLOBAL_pool_collision_rules.md

| Règle | Énoncé condensé | Parent N2 |
|-------|-----------------|-----------|
| RULE-PCOLL-001 | Item majeur = 1 seul pool | L-009 |
| RULE-PCOLL-002 | Finale IF-SF ≠ QV | L-009 + L-001 |
| RULE-PCOLL-003 | Pools peuvent définir EXCLUDED/RESERVED/FORBIDDEN | L-009 |
| RULE-PCOLL-004 | Anti-collision inter-pool = HARD BLOCKER / intra-pool = limité | L-009 + C-002 |
| RULE-PCOLL-005 | Collision détectée → rouvrir avant de continuer | L-009 |
| RULE-PCOLL-006 | VALIDATION anti-collision avant toute proposition humaine | L-009 + C-006 |

## STD_B2_generation_rules.md

| Règle | Énoncé condensé | Parent N2 |
|-------|-----------------|-----------|
| RULE-B2-HB-001 | Zéro filler | L-010 |
| RULE-B2-HB-002 | 8 filtres rédaction obligatoires | C-004 + C-007 |
| RULE-B2-HB-003 | Corrections repassent les 8 filtres | RULE-B2-HB-002 |
| RULE-B2-HB-004 | Triple filtre angle (disponibilité / collision / valeur) | L-009 + L-010 + C-006 |
| RULE-B2-HB-005 | Séquence soumission : angle → anti-collision → conformité → humain | C-006 |
| RULE-B2-HB-006 | Réponse univoque | C-004 |
| RULE-B2-HB-007 | Désambiguïsation homonymes | C-007 |
| RULE-B2-SW-001 | Passe de cadrage si pool éditorial/ouvert | C-006 + L-010 |
| RULE-B2-SW-002 | Présence ailleurs ≠ couverture suffisante | C-008 |
| RULE-B2-SW-003 | Répartition interne = décision humaine | C-006 |
| RULE-B2-SW-004 | Arbitrages évidents : appliquer sans redemander | C-006 |
| RULE-B2-cas source-001 | Ballon d'Or ≠ récompense cas source | C-007 |
RETEX_REF: RETEX_HIERARCHIE_REGLEMENTAIRE_002
| RULE-B2-cas source-002 | "Ronaldo" seul interdit | RULE-B2-HB-007 |
RETEX_REF: RETEX_HIERARCHIE_REGLEMENTAIRE_003

## STD_B2_recevabilite_pedagogique.md

| Règle | Énoncé condensé | Parent N2 |
|-------|-----------------|-----------|
| RULE-PED-001 | Définition question irrecevable | C-004 + C-001 |
| RULE-PED-T1 | Réponse révélée dans le libellé = irrecevable | C-004 |
| RULE-PED-T2 | Déductible par élimination = irrecevable | C-004 |
| RULE-PED-T3 | Connaissance triviale = irrecevable | C-001 + C-004 |
| RULE-PED-T4 | Ambiguïté de réponse = irrecevable | C-004 |
| RULE-PED-005/006 | VALIDATION obligatoire en B2 et B5 | C-006 |
| RULE-PED-008 | Recevabilité complète les 8 filtres, ne les remplace pas | RULE-B2-HB-002 |

## STD_B3_distractor_rules.md

| Règle | Énoncé condensé | Parent N2 |
|-------|-----------------|-----------|
| RULE-HB-DIST-001 | Distractor = réponse correcte ailleurs → BLOCKER | L-009 |
| RULE-HB-DIST-002 | Fictif non signalé → BLOCKER | C-007 |
| RULE-HB-DIST-003 | Format inconsistant → BLOCKER | C-004 |
| RULE-HB-DIST-004 | QA_STATUS=FAIL bloque export | C-006 |
| RULE-SW-DIST-001 | Soft collision → WARNING | L-009 |
| RULE-SW-DIST-002 | Plausibilité basse TYPE 1/5 → WARNING | C-004 + C-008 |
| RULE-SW-DIST-003 | Difficulty spacing mal aligné → WARNING | L-002 + L-003 |
| RULE-SW-DIST-004 | Distribution RATIO_FAIL → WARNING | C-008 |
| RULE-OPT-DIST-001 à 004 | Biais source/ère/nationalité/réutilisation | C-008 |
| RULE-T[1-5]-* | Règles par type de question | C-004 + C-007 |
| RULE-TRANS-001 à 005 | Anti-collision global / format / unicité | L-009 + C-004 + C-007 |

## STD_OBSOLESCENCE_WATCH_RULES.md

| Règle | Énoncé condensé | Parent N2 |
|-------|-----------------|-----------|
RETEX_REF: RETEX_HIERARCHIE_REGLEMENTAIRE_004
| RULE-OBS-003 à 007 | 5 types déclencheurs | C-007 |
| RULE-OBS-008 | Marqueurs de risque à détecter en B5 | C-007 + C-006 |
| RULE-OBS-009 | FLAG_VEILLE ≠ invalide — surveillance | C-006 |
| RULE-OBS-010/011 | Format et moment FICHE_VEILLE | C-006 + C-007 |
| RULE-OBS-cas source-001/002 | Vérifications post-cas source 2026 | RULE-OBS-004 (TYPE-2) |
RETEX_REF: RETEX_HIERARCHIE_REGLEMENTAIRE_005

## MASTER_ARCHITECTURE.md (lois organiques formalisées)

| Règle | Énoncé condensé | Parent N2 |
|-------|-----------------|-----------|
| RULE-GOV-001 | Apprentissage continu / AVANT-APRÈS incontournable | L-008 = cette règle |
| RULE-GOV-002 | Anti-explosion législative (4 filtres) | L-007 = cette règle |
| RULE-LAB-001 | Le LAB expérimente au-dessus du socle FACTORY | C-006 |

---

# NIVEAU 4 — MÉTHODES (MDE)

> Procédures d'exécution dérivées des STD.
> Chaque MDE cite ses STD parents.

| MDE | Phase | STD parents |
|-----|-------|-------------|
| MDE_A3_traitement.md v3.0 | A3 | STD_GLOBAL_quiz_architecture_rules / STD_B2_generation_rules (angles) |
| MDE_A4_tableur_pools.md v2.0 | A4 | STD_GLOBAL_quiz_architecture_rules / STD_GLOBAL_pool_collision_rules |
| MDE_B2_generation.md v2.0 | B2 | STD_B2_generation_rules / STD_B2_recevabilite_pedagogique |
| MDE_B3_distracteurs.md v2.0 | B3 | STD_B3_distractor_rules |
| MDE_B5_audit.md v2.0 | B5 | STD_B2_recevabilite_pedagogique / STD_OBSOLESCENCE_WATCH_RULES / STD_B3_distractor_rules |

---

# NIVEAU 5 — ANNEXES THÉMATIQUES

> Règles spécifiques à un thème. Non généralisables.
> Chaque règle cite sa règle STD parente (N3).

| Règle | Thème | Parent N3 |
|-------|-------|-----------|
| RULE-B2-cas source-001 (Ballon d'Or) | cas source | C-007 → règle factuelle cas source |
RETEX_REF: RETEX_HIERARCHIE_REGLEMENTAIRE_006
| RULE-B2-cas source-002 (Ronaldo) | cas source | RULE-B2-HB-007 |
RETEX_REF: RETEX_HIERARCHIE_REGLEMENTAIRE_007
| RULE-OBS-cas source-001/002 | cas source | RULE-OBS-004 (TYPE-2 nouvelle édition) |
RETEX_REF: RETEX_HIERARCHIE_REGLEMENTAIRE_008

---

# RÈGLES DE CRÉATION D'UNE NOUVELLE RÈGLE

[RULE-HIER-001]
Toute nouvelle règle doit déclarer son niveau (N1 à N5) et son parent.

[RULE-HIER-002]
Une règle sans parent identifiable ne peut pas être intégrée à un STD.
Elle reste en GEN_NOTE candidat jusqu'à ce qu'un parent soit trouvé.

[RULE-HIER-003]
Une règle N5 (thématique) qui se révèle générale sur ≥2 cobayes
doit être promue N3 (STD) avec citation de son parent N2.

[RULE-HIER-004]
Modifier une règle N1 ou N2 déclenche obligatoirement
une revue de toutes les règles qui en dépendent.

[RULE-HIER-005]
Le glossaire contient des définitions, pas des règles.
Toute règle opérationnelle dans le glossaire est mal placée → migrer vers STD.

---

# RÈGLES ORPHELINES IDENTIFIÉES (à traiter)

> Règles existantes dont le parent hiérarchique n'est pas encore formalisé.
> À résoudre avant intégration définitive.

| Règle | Fichier | Statut |
|-------|---------|--------|
| RULE-B2-OPT-001 à 004 (ancrage culturel, extra-sportif...) | STD_B2_generation_rules | Parent probable : C-001 + C-008 — à confirmer |
| GEN_NOTES 001 à 007 (COBAYE_78) | BILAN_COBAYE_78 | Non promus — en attente parent N3 identifié sur ≥2 cobayes |

---

*HIERARCHIE_REGLEMENTAIRE.md*
*Version 1.0 — 2026-05-18*
*Principe : toute règle répond à une règle hiérarchiquement supérieure*


