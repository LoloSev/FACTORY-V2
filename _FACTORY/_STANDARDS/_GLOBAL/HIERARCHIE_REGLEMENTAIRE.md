# HIÉRARCHIE RÉGLEMENTAIRE — QUIZZZ FACTORY

VERSION: 1.1
DATE: 2026-05-24
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

[C-010]
**IA Compatibility**
The factory is designed to be executed by any AI without implicit human context.
All rules, acceptance criteria, and execution contracts must be machine-interpretable without supplementary explanation.
A rule that requires human interpretation to be applied is not a valid factory rule.

[C-011]
**Machine First**
Runtime execution contracts use closed taxonomies, measurable thresholds, and machine states.
Prose judgment inside execution contracts is forbidden.
Every decision point must map to a closed value set or a calculable threshold.
Source : FACTORY_RUNTIME_LEXICON.md / TOKEN_ECONOMY_RUNTIME_PROTOCOL.md

[C-012]
**Token Economy**
No concept is defined in more than one location.
No column is stored if computable from existing data.
No file carries more than one runtime responsibility.
Load the minimum tokens sufficient to execute the active task.
Source : TOKEN_ECONOMY_RUNTIME_PROTOCOL.md

[C-013]
**Runtime Language**
Runtime execution uses canonical English labels (RULE, INPUT, OUTPUT, PROCESS, CONDITION, VALIDATION, FAILURE_CASE, ACCEPTED, REJECTED).
Player-visible quiz content is native French, generated directly — never translated from English.
Deprecated French execution synonyms are forbidden in runtime fields.
Source : RUNTIME_EN_FR_OUTPUT_POLICY.md

---

# NIVEAU 2 — LOIS ORGANIQUES

> Modifiables par décision explicite et documentée.
> Chaque loi cite sa règle constitutionnelle parente.

[L-001] **Architecture des 20 pools** → C-002
5 IF (Q1-Q5 : 2×IF stock=8, 3×IF stock=12) + 15 QV (Q6-Q20, stock=15).
Table de dérivation positionnelle — voir STD_GLOBAL_quiz_architecture_rules.md RULE-ARCH-006
NOTE_STOCKS (D-15): Les valeurs 8, 12 et 15 sont un contrat applicatif (hors pipeline).
Dérivation : STOCK_CIBLE = 277 = (2×8) + (3×12) + (15×15). La valeur 15 garantit la rejouabilité
sur QV (pool tiré 1×/partie — 15 questions = 15 parties sans répétition). Les IF ont des stocks
réduits (8/12) car leur rôle est ancré (Q1-Q5 fixes) et leur volumétrie nécessaire est moindre.

[L-002] **Crescendo N1/N2/N3** → C-005
Q1-Q5 = N1 / Q6-Q15 = N2 / Q16-Q20 = N3. Ordre immuable.
Source : STD_GLOBAL_quiz_architecture_rules.md RULE-ARCH-006
NOTE: référence corrigée — RULE-ARCH-004 concerne la fusion de pools, pas le crescendo.

[L-003] **Difficulté par angle → question → moteur** → C-005 + C-006 + C-010 + C-011
La difficulté est évaluée à l'angle (A3 — NIVEAU_ANGLE), assignée à la question (B2 — NIVEAU_QUESTION), filtrée par le moteur à l'assemblage (runtime).
Le pool est une unité thématique. Il n'est pas le porteur du niveau.
Source : STD_GLOBAL_quiz_architecture_rules.md RULE-ARCH-008
REMPLACE : "La difficulté descend du pool vers la question" (PIPELINE_V2.md — invalidé par RULE-ARCH-008)

[L-004] **Pool agrégé possible** → C-002 + C-003
Un pool peut regrouper plusieurs sous-thèmes faibles pour atteindre son stock cible.
Un pool = une unité de tirage, pas une unité thématique unique.
Source : STD_GLOBAL_quiz_architecture_rules.md RULE-ARCH-005

[L-005] **TSV source de vérité — xlsx vue humaine** → C-006 + C-010 + C-012
Un dossier par ligne, enrichi progressivement via fichiers TSV (source de vérité machine).
Le xlsx est une vue générée à la demande par script — jamais la source de vérité.
Structure : CONFIG.yaml / ITEMS.tsv / ANGLES.tsv / POOLS.tsv / QUESTIONS.tsv / DISTRACTEURS.tsv / QA.tsv
Scripts : generate_xlsx_view.py / generate_sommaire.py
Source : PIPELINE_V2.md v2.1

[L-006] **Richesse et niveau potentiel des items** → L-003 + C-011
Les items ont une RICHESSE documentaire (DENSE/STANDARD/LIGHT) = combien de questions.
Les items ont un NIVEAU_POTENTIEL (N1/N2/N3/MULTI) = dérivé de l'agrégation de leurs NIVEAU_ANGLE.
La difficulté appartient à la question (NIVEAU_QUESTION), pas au pool.
Source : MDE_A3_traitement.md v4.0

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

[L-011] **Lexique central — anti-duplication** → C-012
Toute taxonomie partagée entre ≥2 fichiers vit exclusivement dans FACTORY_RUNTIME_LEXICON.md.
Les autres fichiers référencent sans redéfinir. Toute colonne partagée entre ≥2 xlsx est listée dans COLUMN_CONTRACT.
Source : TOKEN_ECONOMY_RUNTIME_PROTOCOL.md RÈGLE 05

[L-012] **Labels runtime en anglais** → C-013
Les champs d'exécution utilisent l'anglais canonique machine-first.
Le contenu joueur est produit en français natif sans étape de traduction intermédiaire.
Source : RUNTIME_EN_FR_OUTPUT_POLICY.md

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
| RULE-ARCH-006 | 5 IF (table dérivation positionnelle) + 15 QV + crescendo N1/N2/N3 | L-001 + L-002 |
| RULE-ARCH-003 | Stock cible 277 questions | C-003 |
| RULE-ARCH-004 | Fusion pools physiques — transfert coverage/angles/collisions | L-004 |
| RULE-ARCH-005 | Pool peut agréger sous-thèmes faibles | L-004 |

## STD_GLOBAL_pool_collision_rules.md

| Règle | Énoncé condensé | Parent N2 |
|-------|-----------------|-----------|
| RULE-PCOLL-001 | Item majeur = 1 seul pool | L-009 |
| RULE-PCOLL-002 | IF ≠ QV (exclusivité angles) | L-009 + L-001 |
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

## TOKEN_ECONOMY_RUNTIME_PROTOCOL.md

| Règle | Énoncé condensé | Parent N2 |
|-------|-----------------|-----------|
| RÈGLE 01 | Responsabilité unique par fichier | L-011 |
| RÈGLE 02 | XLSX = runtime tables uniquement | C-011 + C-012 |
| RÈGLE 03 | Markdown = règles et arbitrages uniquement | C-011 |
| RÈGLE 04 | Taxonomies fermées — tags/IDs/états machine | C-011 |
| RÈGLE 05 | Lexique central — pas de redéfinition externe | L-011 |
| RÈGLE 06 | Migration progressive — ne pas casser les lignes existantes | L-008 |
| L0–L4 | Couches de chargement runtime — minimum suffisant | C-012 |

## RUNTIME_EN_FR_OUTPUT_POLICY.md

| Règle | Énoncé condensé | Parent N2 |
|-------|-----------------|-----------|
| RULE | Runtime EN / output joueur FR natif | L-012 |
| SCOPE_RUNTIME_EN | Champs d'exécution en anglais canonique | L-012 + C-013 |
| SCOPE_OUTPUT_FR | Contenu joueur en français natif | C-013 |
| FORBIDDEN_PATTERN | Pas de génération EN puis traduction FR | C-013 |

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
*Version 1.1 — 2026-05-24*
*Ajouts : C-010/C-011/C-012/C-013 (IA Compatibility, Machine First, Token Economy, Runtime Language) + L-011/L-012*
*Corrections : L-002 source RULE-ARCH-004→RULE-ARCH-006 / RULE-ARCH-004 libellé corrigé dans N3*
*Principe : toute règle répond à une règle hiérarchiquement supérieure*


