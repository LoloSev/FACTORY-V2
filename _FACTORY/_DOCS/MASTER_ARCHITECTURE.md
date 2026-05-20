[ATTENTION] RÈGLE IA — COMPORTEMENT OBLIGATOIRE
• Fais strictement ce qui est demandé
• Pas de suggestions non sollicitées
• Pas de récapitulatifs après chaque action
• Pas de questions si la tâche est claire
• Réponses courtes, action immédiate
• Signaler toute FAILURE_CASE détectée
• Signaler les CONSISTENCY_FAILURE entre fichiers du projet
• Signaler quand une tâche risque de dépasser les capacités techniques de l'IA
• Proposer des pistes pour économiser des tokens et optimiser les processus

# QUIZZZ FACTORY — MASTER ARCHITECTURE

**Version :** 5.3-runtime-clean
**Mis à jour :** 2026-05-20
**Statut :** Point d'entrée runtime — version nettoyée

> ⚠️ **PIPELINE V2 ACTIF**
> Le pipeline de production a été refondu. Voir : `_FACTORY/_DOCS/PIPELINE_V2.md`
> Changements majeurs : xlsx colonne vertébrale unique / difficulté top-down / A5 et B4 supprimés.
> Les MDE et STD existants restent valides dans leur domaine — à migrer progressivement vers V2.

---

# CONTEXTE DU PROJET

**Les Quizzzz de Lolo** est un site de quiz de culture générale thématique, court, mobile-friendly et rejouable. Chaque partie dure 90 secondes pour 20 questions, avec un mélange aléatoire à chaque session.

**Auteur :** Laurent (Lolo)
**URL live :** `quizzzz-de-lolo.netlify.app`
**Hashtag :** `#QuizzzdeLolo`
**Public cible :** 12–20 ans, anciens élèves, passionnés de culture pop. Usage mobile, partage Instagram, défis entre amis.

| Paramètre | Valeur |
|---|---|
| Durée d'une partie | 90 secondes |
| Questions par partie | 20 |
| Incontournables fixes | 5 |
| Questions aléatoires | 15 |
| Stock cible par quiz | 277 questions |
| Format | QCM 4 choix (A/B/C/D), 1 bonne réponse |

## Accès techniques

| Ressource | Détail |
|---|---|
| Dossier local | `C:\Users\Laurent\Desktop\site quiz\` |
| Déploiement | `netlify deploy --prod` — compte **laurent-baudouin** (laurent.baudouin@gmail.com) — PAS le compte ouathealth |
| GitHub | `github.com/LoloSev/quizz-Mayenne` (FACTORY Mayenne uniquement) |

---

# QUI FAIT QUOI

| Outil | Rôle |
|---|---|
| **Claude (Cowork)** | Documentation, organisation, règles, workflow — Génération de questions, audit, distracteurs — Fichiers HTML / CSS / JS / xlsx — Déploiement Netlify |
| **ChatGPT** | Génération d'avatars / images (DALL-E) — voir `_DOCS/WF.md` — Support génération questions / audit |

---

# CATALOGUE DES QUIZ

| Quiz | Thème |
|---|---|
| Rock | Légendes, albums, riffs, mouvements |
| Rap | Rap français + game international |
| CDM | Histoire de la Coupe du Monde |
| Mayenne | Histoire, géo, traditions du 53 |
| Internet | Memes, plateformes, culture web |
| Séries | Séries TV françaises et internationales |
| Cinéma | Films, acteurs, réalisateurs |

# PHILOSOPHIE GÉNÉRALE

L'objectif n'est pas de tout connaître, mais de **créer un système capable de produire des quiz CONSISTENCY_VALIDATED sur n'importe quel thème**.

Le rôle humain : architecte éditorial, valideur final, superviseur QA_STATUS. Pas opérateur de saisie.

Les documents actifs doivent rester IA-compatibles : formulations précises, règles exploitables, faible friction runtime.

---

# STRATÉGIE COBAYES

Chaque workflow est construit et validé sur un thème cobaye avant d'être généralisé. [RULE-LAB-001]
Le LAB experimente au-dessus du socle FACTORY, jamais en dessous.

Toute regle FACTORY active s'applique integralement dans le LAB tant qu'elle n'a pas ete
remplacee, suspendue ou corrigee par decision explicite.

Le LAB peut produire de nouvelles regles, tester des extensions et signaler des limites,
mais il ne peut pas generer de livrables non conformes aux regles FACTORY deja actives.

| Cobaye | Workflow | Statut |
|---|---|---|
| Mayenne | Pipeline V2 pilote — A1→A3 validés / A4 actif | [EN_COURS] A4 pool engine — 2026-05-20 |
| CDM | Génération B2 + distracteurs B3 | [EN_COURS] B3 complété — en attente B4/B5 |
| Cinéma | Approvisionnement BIB (MDE A2) | [EN_COURS] A2 en cours |

---

# RÈGLES D'ÉQUILIBRAGE DOCUMENTAIRE

## CANONICAL_DIFFICULTY_DISTRIBUTION

```yaml
DIFFICULTY_DISTRIBUTION:
  N1: 5
  N2: 10
  N3: 5
```

Runtime roles:
- N1: onboarding_and_confidence
- N2: discovery_core
- N3: stimulating_final_elevation

Hierarchy:
- MASTER_ARCHITECTURE defines the canonical distribution.
- STD_GLOBAL_quiz_architecture_rules applies the position mapping.
- QUIZ_ASSEMBLY_RULES applies assembly constraints.
- Legacy 40/40/20 references are REJECTED in active runtime.

- Les quotas de difficulté canonique 5/10/5 sont des contraintes runtime actives.
- La CONSISTENCY culturelle et documentaire prime sur les objectifs chiffrés.
- Des déséquilibres volontaires peuvent être conservés s'ils sont ACCEPTED.
- Les ajustements thématiques ne doivent pas modifier la distribution N1/N2/N3 canonique.

---

# GOUVERNANCE LÉGISLATIVE — MÉTA-RÈGLE

[RULE-GOV-001]
**Apprentissage continu — maturité progressive**
Le projet apprend à chaque quiz produit. L'intervention humaine (AVANT/APRÈS) est incontournable au niveau de maturité actuel. Aucune automatisation ne peut substituer ce retour d'expérience. Les STD sont des photographies du savoir courant, pas des lois figées.
SOURCE: SESSION 2026-05-18

[RULE-GOV-002]
**Anti-explosion législative — 4 filtres avant création de règle**
Avant d'ajouter toute nouvelle règle à un fichier STD, VALIDER dans l'ordre :
1. **Déjà couverte ?** → Enrichir la règle existante, ne pas en créer une nouvelle.
2. **Généralisable multi-thèmes ?** → Si non, la règle reste dans le document thématique (ex: STD_B2 CDM annex), pas dans le STD global.
3. **Remplace une règle plus faible ?** → Substituer, ne pas empiler.
4. **Observée sur ≥2 cobayes ?** → Si non, statut GEN_NOTE candidat, pas STD actif.

⚠️ Une règle qui ne passe pas ces 4 filtres ne doit pas intégrer les fichiers STD.
SOURCE: SESSION 2026-05-18

---

# NOMENCLATURE DES DOCUMENTS

## Documents de la chaîne de production

| Code | Nom complet | Rôle |
|---|---|---|
| **BIB** | Base Items Brute | Document source constitué manuellement. Ensemble des items organisés en sections thématiques, avec indicateurs de difficulté bruts. **Non modifié après archivage.** |
| **BIPREGEN** | Base Items Prégénération | Version traitée et structurée de la BIB. Items codés `[THEME]-[CAT]-[N°]-[NIV]`, ligne unique, niveaux harmonisés, statistiques et index inclus. **Source de données propre pour la génération.** |
| **ANGIPREGEN** | Angles Items Prégénération | Définit pour chaque item : les angles interrogeables, les exclusions inter-items et le quota de questions à générer. **Guide opérationnel de la génération.** |
| **PROCESS_BIB** | Process Traitement BIB | Trace précise de toutes les transformations BIB → BIPREGEN + ANGIPREGEN. État initial, interventions, reclassements, décisions. **Traçabilité AVANT/APRÈS.** |
| **POOLS** | Pools Prégénération | Définit les 20 pools du quiz : identifiant, type (IF-SF / IF-ROT / QV), thème éditorial, stock cible, items ANGIPREGEN associés. **Chaînon entre ANGIPREGEN et génération.** |

## Convention de nommage fichier

## RULE_NAMING_PATTERN

[RULE-NAM-001]
Tout fichier doit porter le préfixe de sa phase en position 1.

FORMAT:
```txt
[PHASE]_...
```

PHASES_AUTORISEES:
- A1
- A2
- A3
- A4
- B2
- B3
- B5
- B6
- EXPORT

NOTE: A5 et B4 supprimés en pipeline V2 (2026-05-18).

---

## DEUX PATTERNS DISTINCTS

[DEF-NAMING-001]
NAMING_PATTERN_PROCESS_DOC:
Document unique par phase, non réitérable.

FORMAT:
```txt
[PHASE]_[INDEX]_[ROLE].md
```

EXEMPLES:
- B5_01_AUDIT_LOG.md
- B5_02_FIX_LOG.md
- B5_03_QA_REPORT.md
- A2_01_APPRO_LOG.md
- B4_01_IMPORT_LOG.md

SIGNAL_IA:
Présence de _[INDEX]_ en position 2.

---

[DEF-NAMING-002]
NAMING_PATTERN_ARTIFACT:
Artefact pouvant exister en plusieurs exemplaires ou versions.

FORMAT:
```txt
[PHASE]_[ROLE]_[THEME]_[N].[ext]
```

EXEMPLES:
- A2_BIB_CINEMA_01.txt
- A2_BIB_CINEMA_02.txt
- A2_BIB_CINEMA_03.txt
- B5_TABLEUR_MAYENNE_WIP.xlsx
- EXPORT_CDM_FINAL.xlsx

SIGNAL_IA:
Absence de _[INDEX]_ en position 2.
Présence d'un suffixe d'état ou d'itération en position finale.

---

[RULE-NAM-002]
La présence de _[INDEX]_ en position 2 identifie un NAMING_PATTERN_PROCESS_DOC.
Son absence identifie un NAMING_PATTERN_ARTIFACT.

[RULE-NAM-003]
Les deux patterns ne doivent pas être mélangés dans un même fichier.

---

## SUFFIXES_ETAT_XLSX

SUFFIXES_AUTORISES:
```txt
INIT    ← structure vide (supprimé en V2 — conservé pour rétrocompatibilité naming)
v[N]    ← version de travail B4 (v1, v2...)
WIP     ← sous audit B5
FINAL   ← livrable validé EXPORT — immuable
```

[RULE-NAM-004]
Le suffixe FINAL interdit toute modification ultérieure du fichier.

[RULE-NAM-005]
Le suffixe WIP indique un fichier en cours de validation humaine.

---

## CHRONOLOGIE_XLSX

```txt
B5_TABLEUR_[THEME]_WIP.xlsx       ← sous audit (V2 : plus d'A5/B4)
        ↓
EXPORT_[THEME]_FINAL.xlsx         ← livrable immuable
```

NOTE: A5_TABLEUR_INIT et B4_TABLEUR supprimés en pipeline V2.

---

---

# ARBORESCENCE — QUIZZZ FACTORY

```
_FACTORY/
│
├── _DOCS/                          ← documents de référence
│   ├── MASTER_ARCHITECTURE.md      ← ce document
│   ├── PIPELINE_V2.md              ← description pipeline V2
│   ├── AGENTS.md                   ← agents IA
│   ├── ARBORESCENCE_LIGNES.txt     ← arborescence générée
│   ├── DDT.md                      ← état du site, technique, déploiement
│   ├── DDT_WORKFLOW.md             ← règles de travail avec l'IA
│
├── _SCRIPTS/                       ← scripts Python factory
│   ├── sync_glossaire.py           ← sync onglets GLOSSAIRE xlsx
│   ├── check_dashboard.py          ← détection REFRESH_NEEDED
│   ├── generate_dashboards.py      ← génération dashboard HTML
│   ├── gate_a4.py                  ← gate A4 → B2
│   ├── gate_b2.py                  ← gate B2 → B3
│   ├── gate_b3.py                  ← gate B3 → B5
│   ├── gate_b5.py                  ← gate B5 → EXPORT
│   ├── gate_export.py              ← gate export final
│   ├── gate_utils.py               ← fonctions communes gates
│   ├── validate_collision.py       ← validation collisions pools
│   ├── validate_compliance.py      ← validation conformité
│   └── validate_qa_metrics.py      ← validation métriques QA
│
├── _STATE/                         ← état pipeline (généré)
│   ├── DASHBOARD_STATE.json        ← état courant par ligne
│   ├── pipeline_state.json         ← état gates
│   ├── .dashboard_factory_main.html← dashboard HTML généré
│   ├── .dashboard_stamp.json       ← stamp dashboard
│   └── .sync_stamp.json            ← stamp sync glossaire
│
├── METHODES/                       ← modes opératoires par étape
│   ├── _A3/
│   │   └── MDE_A3_traitement.md    ← BIB → BIPREGEN + ANGIPREGEN    [OK]
│   ├── _A4/
│   │   └── MDE_A4_tableur_pools.md ← créer le tableur xlsx           [OK]
│   ├── _B2/
│   │   └── MDE_B2_generation.md    ← générer les questions brutes    [OK]
│   ├── _B3/
│   │   └── MDE_B3_distracteurs.md  ← ajouter les distracteurs        [OK] ✓ v1.0
│   ├── _B5/
│   │   └── MDE_B5_audit.md         ← audit humain + traçabilité      [OK]
│   └── _GLOBAL/
│       ├── SKILL.md
│       └── SKILL_CREATION_CHECKLIST.md
│
├── _STANDARDS/                     ← règles et références transversales
│   ├── _GLOBAL/                    ← standards transverses
│   │   ├── HIERARCHIE_REGLEMENTAIRE.md
│   │   ├── AUDIT_REGLES_INTEGRITE.md
│   │   ├── FACTORY_QA_RULES.md
│   │   ├── QUIZ_ASSEMBLY_RULES.md
│   │   ├── STD_NAMING_CONVENTIONS.md
│   │   ├── STD_GLOBAL_quiz_architecture_rules.md
│   │   ├── STD_GLOBAL_pool_collision_rules.md
│   │   ├── STD_GLOBAL_factory_arborescence_rules.md
│   │   ├── STD_NOTORIETE_SEPARATION.md
│   │   ├── STD_COLLISION_WATCH_RULES.md
│   │   ├── STD_GENERALIZATION_NOTE_RULES.md
│   │   ├── STD_OBSOLESCENCE_WATCH_RULES.md
│   │   └── STD_QA_status_rules.md
│   ├── _A4/
│   │   ├── STD_A4_pool_format_rules.md
│   │   └── STD_A4_pool_workflow_rules.md
│   ├── _B2/
│   │   ├── STD_B2_generation_rules.md
│   │   └── STD_B2_recevabilite_pedagogique.md
│   ├── _B3/
│   │   ├── STD_B3_distractor_rules.md
│   │   └── STD_B3_distractor_metrics.md
│   ├── _B5/
│   │   ├── STD_B5_factory_quality_rules.md
│   │   ├── STD_B5_duplicate_detection_rules.md
│   │   ├── STD_B5_pool_collision_rules.md
│   │   ├── STD_B5_density_rules.md
│   │   ├── STD_B5_difficulty_curve_rules.md
│   │   ├── STD_B5_weak_question_rules.md
│   │   ├── STD_B5_distractor_quality_rules.md
│   │   └── STD_B5_factory_format_rules.md
│   └── _B6/
│       ├── STD_B6_rule_priority_matrix.md
│       ├── STD_B6_hard_blockers_rules.md
│       ├── STD_B6_soft_warnings_rules.md
│       └── STD_B6_optional_optimizer_rules.md
│
├── B6_RETOURS/                     ← retours d'expérience
│   └── B6_RETOURS_FACTORY.md
│
└── _LIGNES/
    │
    ├── _TEMPLATE/
    │   │
    │   ├── A1_THEME/
    │   │   └── A1_01_THEME_CONTEXT.md
    │   │
    │   ├── A2_APPRO/
    │   │   ├── A2_BIB_[THEME]_01.txt
    │   │   ├── A2_01_APPRO_LOG.md
    │   │   └── A2_02_APPRO_STATS.md
    │   │
    │   ├── A3_TRAITEMENT/
    │   │   ├── A3_BIPREGEN_[THEME].txt
    │   │   ├── A3_ANGIPREGEN_[THEME].txt
    │   │   └── A3_01_PROCESS_BIB_[THEME].md
    │   │
    │   ├── A4_POOLS/
    │   │   └── A4_POOLS_[THEME].txt
    │   │
    │   ├── B2_GENERATION/
    │   │   ├── IF_SF/
    │   │   ├── IF_ROT/
    │   │   ├── QV/
    │   │   └── B2_01_GENERATION_LOG.md
    │   │
    │   ├── B3_DISTRACTEURS/
    │   │   ├── IF_SF/
    │   │   ├── IF_ROT/
    │   │   ├── QV/
    │   │   └── B3_01_DISTRACTEUR_LOG.md
    │   │
    │   ├── B5_AUDIT/
    │   │   ├── B5_TABLEUR_[THEME]_WIP.xlsx
    │   │   ├── B5_01_AUDIT_LOG.md
    │   │   ├── B5_02_FIX_LOG.md
    │   │   └── B5_03_QA_REPORT.md
    │   │
    │   ├── B6_REGLES/
    │   │   ├── B6_01_RULES_EXTRACTED.md
    │   │   ├── B6_02_EDGE_CASES.md
    │   │   └── B6_03_THEME_RULES_[THEME].md
    │   │
    │   └── EXPORT/
    │       └── EXPORT_[THEME]_FINAL.xlsx
    │
    ├── _MAYENNE/                        ← [EN_COURS] Pipeline V2 pilote — A4 actif 2026-05-20
    │   ├── A2_APPRO/                    ← A1 + A2 validés (naming V2)
    │   ├── A3_TRAITEMENT/               ← A3 complet (runtime map + signals + tables + guardrails)
    │   └── A4_POOLS/                    ← A4 actif (pool engine + rules + balance)
    │
    ├── _CDM/                            ← [EN_COURS] B3 complété — en attente B4/B5
    │   ├── A2_APPRO/
    │   │   └── A2_BIB_CDM_01.txt
    │   ├── A3_TRAITEMENT/
    │   │   ├── A3_BIPREGEN_CDM.txt
    │   │   ├── A3_ANGIPREGEN_CDM.txt
    │   │   └── A3_01_PROCESS_BIB_CDM.md
    │   ├── A4_POOLS/
    │   │   └── A4_POOLS_CDM.txt
    │   └── B3_DISTRACTEURS/
    │       ├── PASS_1_GENERATION/       ← IF-ROT, IF-SF, QV (complètes)
    │       ├── PASS_2_AUDIT/            ← collision + difficulté + format (complets)
    │       ├── PASS_3_OPTIMIZATION/     ← surqualification (complète)
    │       ├── PASS_4_CORRECTIONS/      ← corrections appliquées
    │       └── PASS_1_CONSOLIDATION_FINAL.md
    │
    ├── _CINEMA/                         ← [EN_COURS] A2 en cours
    │   └── A2_APPRO/
    │       ├── A2_BIB_CINEMA_01.txt
    │       ├── A2_BIB_CINEMA_02.txt
    │       ├── A2_BIB_CINEMA_03.txt
    │       ├── A2_APPRO_LOG.md
    │       └── A2_APPRO_STATS.md
    │
    └── _RAP/                            ← [EN_ATTENTE] matière première disponible
        └── A2_APPRO/
            ├── 00_SOURCES_RETRO/
            ├── 01_CONSOLIDATION/
            └── A2_THEME_retro_RECONSTRUIT_RAP.xlsx
```

---

# ARBORESCENCE _LIGNES — ETAT CIBLE

# SECTION — DOSSIERS_PHASES

Chaque theme de `_LIGNES/` utilise uniquement l'arborescence de phases A1 a B6 puis EXPORT.

DOSSIERS:
```txt
A1_THEME/
A2_APPRO/
A3_TRAITEMENT/
A4_POOLS/
B2_GENERATION/
B3_DISTRACTEURS/
B5_AUDIT/
B6_REGLES/
EXPORT/
```

---

# SECTION — FICHIERS_REFERENCE

## _MAYENNE

```txt
A2_APPRO/A1_MAYENNE_EDITORIAL_INTENT.md
A2_APPRO/A2_MAYENNE_CANONICAL_SOURCE.md
A2_APPRO/A2_MAYENNE_RUNTIME_INDEX.xlsx
A3_TRAITEMENT/A3_MAYENNE_RUNTIME_MAP.md
A3_TRAITEMENT/A3_MAYENNE_RUNTIME_SIGNALS.md
A3_TRAITEMENT/A3_MAYENNE_RUNTIME_STATUS.md
A3_TRAITEMENT/A3_MAYENNE_RUNTIME_TABLES.xlsx
A3_TRAITEMENT/A3_MAYENNE_CLUSTER_07_GUARDRAILS.md
A4_POOLS/A4_MAYENNE_POOL_ENGINE.xlsx
A4_POOLS/A4_MAYENNE_RUNTIME_RULES.md
A4_POOLS/A4_MAYENNE_RUNTIME_BALANCE.md
```

---

## _CDM

```txt
A2_APPRO/A2_BIB_CDM_01.txt
A3_TRAITEMENT/A3_BIPREGEN_CDM.txt
A3_TRAITEMENT/A3_ANGIPREGEN_CDM.txt
A3_TRAITEMENT/A3_01_PROCESS_BIB_CDM.md
A4_POOLS/A4_POOLS_CDM.txt
B3_DISTRACTEURS/PASS_1_GENERATION/    ← IF-ROT, IF-SF, QV (complètes)
B3_DISTRACTEURS/PASS_2_AUDIT/         ← complet
B3_DISTRACTEURS/PASS_3_OPTIMIZATION/  ← complet
B3_DISTRACTEURS/PASS_4_CORRECTIONS/   ← corrections appliquées
B3_DISTRACTEURS/PASS_1_CONSOLIDATION_FINAL.md
```

---

## _CINEMA

```txt
A2_APPRO/A2_BIB_CINEMA_01.txt
A2_APPRO/A2_BIB_CINEMA_02.txt
A2_APPRO/A2_BIB_CINEMA_03.txt
A2_APPRO/A2_APPRO_LOG.md
A2_APPRO/A2_APPRO_STATS.md
```

---

## _RAP

```txt
A2_APPRO/00_SOURCES_RETRO/quiz_rap_final.txt
A2_APPRO/01_CONSOLIDATION/CONSOLIDATION_RETRO_RAP.xlsx
A2_APPRO/01_CONSOLIDATION/REVUE_EDITORIALE_RETRO_RAP.xlsx
A2_APPRO/01_CONSOLIDATION/STOCK_MAITRE_RETRO_RAP.xlsx
A2_APPRO/A2_THEME_retro_RECONSTRUIT_RAP.xlsx
```

---

---

# ARCHITECTURE DES QUIZ

Chaque quiz contient 20 questions issues de 20 pools.

## Bloc 1 — Incontournables semi-fixes (IF-SF)
2 pools × 8 questions — identité forte, rotation très lente

## Bloc 2 — Incontournables rotatifs (IF-ROT)
3 pools × 12 questions — rotation lente, onboarding fluide

## Bloc 3 — Questions variables (QV)
15 pools × 15 questions — forte variété, rotation rapide

**Total : 20 pools = 20 questions par partie. Le moteur pioche UNE question par pool.**

---

# DEUX WORKFLOWS

## Workflow A — Élaboration (architecture du quiz)

| Étape | Qui | Action | MDE |
|---|---|---|---|
| A1 | [HUMAIN] Laurent | Choix du thème | — |
| A2 | [IA] → [OK] | Construire la BIB | `MDE_A2_approvisionnement.md` |
| A3 | [IA] → [OK] | Traiter BIB → BIPREGEN + ANGIPREGEN | `MDE_A3_traitement.md` |
| A4 | [IA] → [OK] | Définir les 20 pools → créer POOLS_[THEME].txt | `MDE_A4_tableur_pools.md` |

## Workflow B — Production (génération des questions)

| Étape | Qui | Action | MDE |
|---|---|---|---|
| B2 | [IA] → [OK] | Générer les questions brutes (pool par pool) | `MDE_B2_generation.md` |
| B3 | [IA] → [OK] ✓ | Ajouter les distracteurs — entonnoir 4-passes (PASS 1/2/3/4) | `MDE_B3_distracteurs.md` |
| B5 | [HUMAIN] + [IA] | Audit humain + traçabilité | `MDE_B5_audit.md` |
| B6 | [IA] → [OK] | Extraire les règles généralisables | `MDE_B6_regles.md` |

---

# RÈGLES CRITIQUES

- Pool par pool, étape par étape — **jamais globalement**
- Validation humaine obligatoire avant chaque étape suivante
- Distracteurs fictifs → validation humaine **toujours**
- Traçabilité AVANT/APRÈS/RAISON dans le xlsx
- BIB original jamais modifié après archivage
- Les règles extraites des cobayes alimentent le glossaire documentaire
- `PROCESS_BIB` conserve les arbitrages humains utiles à la mémoire du système, pas seulement les transformations techniques
- Les collisions non bloquantes doivent pouvoir être suivies explicitement avant d'être tranchées

---

# STRATÉGIE TECHNIQUE

Rester le plus longtemps possible sur : **Excel / JSON / GitHub / Netlify**

Architecture cible : `Excel → Export JSON → Site`

---

# DOCUMENTS LIÉS

## Contexte projet

| Document | Rôle |
|---|---|
| `_DOCS/DDT.md` | État du site, technique, déploiement |
| `_DOCS/DDT_WORKFLOW.md` | Règles de travail avec l'IA |



## Méthodes de production (Bureau des Méthodes)

| Document | Rôle | Workflow |
|---|---|---|
| `METHODES/_A3/MDE_A3_traitement.md` | Traitement BIB → BIPREGEN + ANGIPREGEN | A3 |
| `METHODES/_B2/MDE_B2_generation.md` | Génération des questions brutes | B2 |
| `METHODES/_B3/MDE_B3_distracteurs.md` | Génération des distracteurs — entonnoir 3-passes | B3 |
| `METHODES/_B5/MDE_B5_audit.md` | Audit humain des questions générées + traçabilité | B5 |
| `METHODES/_GLOBAL/SKILL.md` | Skills pour chaque phase (B3 intégration complète) | A/B |

## Documents de production CDM (cobaye A3 + A4)

| Document | Rôle |
|---|---|
| `_LIGNES/_CDM/A2_APPRO/A2_BIB_CDM_01.txt` | Base Items Brute CDM |
| `_LIGNES/_CDM/A3_TRAITEMENT/A3_BIPREGEN_CDM.txt` | Items codés + niveaux harmonisés |
| `_LIGNES/_CDM/A3_TRAITEMENT/A3_ANGIPREGEN_CDM.txt` | Angles interrogeables + quotas |
| `_LIGNES/_CDM/A3_TRAITEMENT/A3_01_PROCESS_BIB_CDM.md` | Traçabilité BIB → BIPREGEN |
| `_LIGNES/_CDM/A4_POOLS/A4_POOLS_CDM.txt` | Définition des 20 pools — chaînon vers génération |

## Standards et règles

| Document | Rôle |
|---|---|
| `_STANDARDS/_GLOBAL/STD_GLOBAL_quiz_architecture_rules.md` | Règles de génération applicables à tous les quiz |
| `_STANDARDS/_GLOBAL/STD_GLOBAL_pool_collision_rules.md` | Règles anti-collision globales |
| `_STANDARDS/_B3/STD_B3_distractor_rules.md` | Règles formalisées : HARD_BLOCKERS, SOFT_WARNINGS, OPTIONAL_OPTIMIZERS, TYPE 1-5 |
| `_STANDARDS/_B3/STD_B3_distractor_metrics.md` | Métriques QA_STATUS B3 : seuils Green/Yellow/Red, decision gate, audit report |
| `_STANDARDS/_B5/STD_B5_factory_quality_rules.md` | VALIDATIONS QA_STATUS obligatoires (CHECK codes) + flags QA |
| `_STANDARDS/_B6/STD_B6_rule_priority_matrix.md` | Hiérarchie des règles : HARD_BLOCKER / SOFT_WARNING / OPTIONAL |
| `_STANDARDS/_GLOBAL/QUIZ_ASSEMBLY_RULES.md` | Ordre des 20 questions + règles anti-monotonie + équilibrage |
