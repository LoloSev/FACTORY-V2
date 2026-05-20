# GLOSSAIRE DOCUMENTAIRE — QUIZZZ FACTORY

VERSION: 4.6
DATE_UPDATE: 2026-05-19
STATUS: ACTIVE_REFERENCE
DOC_ROLE: NORMATIVE_MACHINE_LEXICON
IA_COMPATIBLE: TRUE
IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE

DEPENDENCY:
- MASTER_ARCHITECTURE.md
- _STANDARDS/_GLOBAL/STD_GLOBAL_quiz_architecture_rules.md
- _STANDARDS/_GLOBAL/STD_GLOBAL_pool_collision_rules.md
- _STANDARDS/_GLOBAL/STD_GLOBAL_factory_arborescence_rules.md
- _STANDARDS/_B5/STD_B5_factory_quality_rules.md
- _STANDARDS/_GLOBAL/STD_QA_status_rules.md
- _STANDARDS/STD_ASM_quiz_assembly_rules.md

---

# SECTION — MACHINE_INTERPRETATION_RULES

[RULE-META-001]
Chaque définition doit être interprétable sans contexte implicite.

[RULE-META-002]
Les synonymes métier doivent être limités.

[RULE-META-003]
Les objets documentaires doivent utiliser une structure stable.

FORMAT_OBJET:
```txt
OBJET:
INPUT:
OUTPUT:
CONTRAINTES:
ERREURS:
```

[RULE-META-004]
Les références croisées doivent utiliser DEPENDENCY.

[RULE-META-005]
Les IDs documentaires doivent rester stables.

[RULE-META-006]
Les emojis sont interdits dans les documents de production.

[RULE-META-007]
Les définitions narratives doivent être réduites au minimum opérationnel.

---

# SECTION — STATUS_STANDARD

[DEF-STATUS-001]
STATUS_STANDARD:
Liste officielle des statuts documentaires autorisés.

VALEURS_AUTORISEES:
- [OK]
- [EN_COURS]
- [A_CREER]
- [BLOQUE]

[RULE-STATUS-001]
Tout autre format de statut est interdit.

---

# SECTION — RULE_ID

[DEF-RULE-001]
RULE_ID:
Identifiant stable permettant le référencement d'une règle documentaire.

FORMAT_AUTORISE:
```txt
[RULE-CAT-001]
```

UTILISATIONS:
- audit IA
- validation automatique
- réduction tokens
- traçabilité

---

# SECTION — DEF_ID

[DEF-RULE-002]
DEF_ID:
Identifiant stable d'une définition documentaire.

FORMAT_AUTORISE:
```txt
[DEF-CAT-001]
```

---

# SECTION — ERROR_ID

[DEF-RULE-003]
ERR_ID:
Identifiant stable d'une FAILURE_CASE documentaire.

FORMAT_AUTORISE:
```txt
[ERR-001]
```

---

# SECTION — OPTIMIZATION_ID

[DEF-RULE-004]
OPT_ID:
Identifiant stable d'une règle d'optimisation.

FORMAT_AUTORISE:
```txt
[OPT-001]
```

---

# SECTION — MACHINE_READABLE

[DEF-MACHINE-001]
MACHINE_READABLE:
Bloc structuré destiné à être interprété directement par une IA.

FORMATS_RECOMMANDES:
- YAML
- JSON
- structure clé/valeur

OBJECTIF:
Réduire l'ambiguïté documentaire.

[RULE-MACHINE-001]
Les données structurelles critiques doivent exister en version MACHINE_READABLE.

---

# SECTION — DEPENDENCY

[DEF-DEP-001]
DEPENDENCY:
Liste explicite des documents nécessaires à l'interprétation correcte d'un document.

FORMAT_AUTORISE:
```txt
DEPENDENCY:
- chemin/document.md
```

[RULE-DEP-001]
Les références implicites sont interdites.

INTERDIT:
```txt
voir MDE_A3
```

AUTORISE:
```txt
DEPENDENCY:
- METHODES/_A3/MDE_A3_traitement.md
```

---

# SECTION — OBJET_DOCUMENTAIRE

[DEF-OBJ-001]
OBJET_DOCUMENTAIRE:
Bloc documentaire normalisé représentant une unité opérationnelle de la FACTORY.

STRUCTURE_STANDARD:
```txt
OBJET:
INPUT:
OUTPUT:
CONTRAINTES:
ERREURS:
```

[RULE-OBJ-001]
Les objets documentaires critiques doivent utiliser cette structure.

---

# SECTION — ROTATION_LENTE

[DEF-ROT-001]
ROTATION_LENTE:
Renouvellement inférieur à 10 % des questions par export.

---

# SECTION — ROTATION_RAPIDE

[DEF-ROT-002]
ROTATION_RAPIDE:
Renouvellement supérieur à 40 % des questions par export.

---

# SECTION — FORTE_VARIETE

[DEF-VAR-001]
FORTE_VARIETE:
Présence d'au moins 12 sous-thèmes distincts dans les pools QV.

---

# SECTION — ONBOARDING_FLUIDE

[DEF-ONB-001]
ONBOARDING_FLUIDE:
Présence d'au moins 3 questions N1 dans les 5 premières questions d'une partie.

---

# SECTION — COHERENCE_CULTURELLE

[DEF-COH-001]
COHERENCE_CULTURELLE:
Absence de contradiction chronologique, thématique ou factuelle dans un même quiz.

[RULE-COH-001]
La CONSISTENCY culturelle prime sur les quotas.

---

# SECTION — ACCESSIBILITE_GRAND_PUBLIC

[DEF-AGP-001]
ACCESSIBILITE_GRAND_PUBLIC:
Capacité d'une référence à être reconnue rapidement par le public cible.

CRITERES:
- reconnaissance rapide
- compréhension immédiate
- besoin de spécialisation < 2 règles spécifiques
- présence culturelle forte

[RULE-AGP-001]
Les pools structurants doivent privilégier une forte accessibilité.

---

# SECTION — ANGLE_DOCUMENTAIRE

[DEF-ANGLE-001]
ANGLE_DOCUMENTAIRE:
Aspect précis et exploitable d'un item pouvant produire une question distincte.

CRITERES:
- une seule réponse correcte
- absence d'ambiguïté majeure
- distinction claire avec les autres angles

[RULE-ANGLE-001]
Les micro-variantes artificielles doivent être évitées.

---

# SECTION — ANGLE_ASSIGNMENT

[DEF-ANGLE-002]
ANGLE_ASSIGNMENT:
Assignation explicite d'un angle à un pool unique.

[RULE-ANGLE-002]
Un angle assigné à un pool est interdit dans les autres pools.

DEPENDENCY:
- POOLS_[THEME].txt

---

# SECTION — BIB

[DEF-BIB-001]
BIB:
Réservoir de matière culturelle exploitable.

OBJET:
Source de matière culturelle brute — non normative, non procédurale, non runtime.
Consulté par A2_PROCESS via extraction ciblée uniquement.

INPUT:
- recherche documentaire
- saisie humaine

OUTPUT:
- fragments culturels exploitables
- matière filtrée par la FACTORY

CONTRAINTES:
- archivage obligatoire
- non modifiable après archivage
- ne contient aucune règle runtime
- ne pilote jamais l'exécution FACTORY

[RULE-BIB-001]
Le BIB original ne doit jamais être modifié après archivage.

[RULE-BIB-002]
Le BIB est une source, jamais un contrôleur.
La FACTORY transforme, filtre et valide — le BIB fournit la matière brute.

---

# SECTION — BIPREGEN

[DEF-BIPREGEN-001]
BIPREGEN:
Version harmonisée du BIB.

OBJET:
Source propre de génération.

INPUT:
- BIB

OUTPUT:
- items codés
- niveaux harmonisés
- structure normalisée

CONTRAINTES:
RETEX_REF: RETEX_GLOSSAIRE_DOCUMENTAIRE_FACTORY_001
- code obligatoire
- format stable

ERREURS:
- code invalide
RETEX_REF: RETEX_GLOSSAIRE_DOCUMENTAIRE_FACTORY_002
- niveau incohérent

---

# SECTION — ANGIPREGEN

[DEF-ANGI-001]
ANGIPREGEN:
Carte documentaire des angles exploitables.

OBJET:
Pilotage génération documentaire.

INPUT:
- BIPREGEN

OUTPUT:
- angles
- exclusions
- quotas

CONTRAINTES:
- quota obligatoire
- exclusions explicites

ERREURS:
- angle ambigu
- quota absent
- collision potentielle

---

# SECTION — POOL

[DEF-POOL-001]
POOL:
Unité opérationnelle contenant un stock de questions CONSISTENCY_VALIDATED.

PARAMETRES_FIXES:
  TOTAL_POOLS: 20
  QUESTIONS_PER_GAME: 20
  DRAW_PER_POOL: 1

POOL_TYPES:
  IF_SF: 2
  IF_ROT: 3
  QV: 15

→ Règles opérationnelles : voir `STD_GLOBAL_quiz_architecture_rules.md`

---

# SECTION — IF_SF

[DEF-IFS-001]
IF_SF:
Pool d'incontournables semi-fixes.

PARAMETRES:
- 2 pools
- 8 questions par pool
- rotation lente

[RULE-IFS-001]
Les angles IF-SF ne peuvent pas être réutilisés dans les QV.

---

# SECTION — IF_ROT

[DEF-IFR-001]
IF_ROT:
Pool d'incontournables rotatifs.

PARAMETRES:
- 3 pools
- 12 questions par pool
- ROTATION: MEDIUM

[RULE-IFR-001]
Les angles IF-ROT sont interdits dans les QV.

---

# SECTION — QV

[DEF-QV-001]
QV:
Questions Variables.

PARAMETRES:
- 15 pools
- 15 questions par pool
- rotation rapide

[RULE-QV-001]
Les QV doivent maximiser la diversité documentaire.

---

# SECTION — DISTRACTEUR

[DEF-DIST-001]
DISTRACTEUR:
Réponse incorrecte crédible proposée dans un QCM.

CRITERES:
- même registre que la bonne réponse
- crédible
- non ambigu
- non absurde

→ Règles opérationnelles : voir `STD_B3_distractor_rules.md` [RULE-HB-DIST-002]

---

# SECTION — POOL_COLLISION

[DEF-PCOLL-001]
POOL_COLLISION:
Réutilisation problématique d'un même angle dans plusieurs pools.

NIVEAU_PRIORITE:
HARD_BLOCKER

→ Règles opérationnelles : voir `STD_GLOBAL_pool_collision_rules.md` [RULE-PCOLL-001 à 006]

---

# SECTION — QA_STATUS

[DEF-QA-001]
QA_STATUS:
Résultat final des VALIDATIONS QA_STATUS.

VALEURS_AUTORISEES:
- PASS
- WARNING
- FAIL

[RULE-QA-001]
QA_STATUS=FAIL bloque l'export.

---

# SECTION — PROCESS_BIB

[DEF-PROCESS-001]
PROCESS_BIB:
Document de traçabilité des décisions d'extraction BIB → A3.

OBJET:
Traçabilité des décisions humaines lors du traitement A2/A3.

INPUT:
- BIB
- décisions d'extraction et de rejet

OUTPUT:
- historique des extractions
- décisions documentaires
- reclassements et arbitrages

CONTRAINTES:
- conservation AVANT/APRES si modification nécessaire
- justification obligatoire

ERREURS:
- décision non tracée
- justification absente

IMPORTANT:
PROCESS_BIB est un document parallèle de traçabilité.
Il ne constitue pas une étape autonome du FACTORY_PIPELINE.
Il ne contient aucune règle runtime.

---

# SECTION — POOLS_DOC

[DEF-POOLS-001]
POOLS_DOC:
Document définissant les pools opérationnels du quiz.

OBJET:
Pilotage assemblage et génération.

INPUT:
- ANGIPREGEN
- stratégie éditoriale

OUTPUT:
- structure des 20 pools
- assignations
- exclusions

CONTRAINTES:
- 20 pools obligatoires
- assignations explicites

ERREURS:
- collision de pools
- angle non assigné

---

# SECTION — COBAYE

[DEF-COB-001]
COBAYE:
Thème pilote utilisé pour construire ou valider un workflow avant généralisation.

OBJECTIF:
Tester les règles documentaires sur un cas réel.

EXEMPLES:
- cas source pour A3
RETEX_REF: RETEX_GLOSSAIRE_DOCUMENTAIRE_FACTORY_003
- MAYENNE pour B5
- CINEMA pour A2

---

# SECTION — FACTORY_PIPELINE

[DEF-PIPE-001]
FACTORY_PIPELINE:
Chaîne officielle de traitement documentaire.

PIPELINE_STANDARD_V2:
```txt
A2_APPRO → A3_TRAITEMENT → A4_POOLS → B2_GENERATION → B3_DISTRACTEURS → B5_AUDIT → EXPORT
```

[RULE-PIPE-001]
Aucune étape ne peut être sautée.

[RULE-PIPE-002]
Les validations humaines restent obligatoires.

---

# SECTION — HARD_COLLISION

[DEF-HCOLL-001]
HARD_COLLISION:
Distractor identique à une réponse correcte ailleurs dans le pool.

PRIORITE: HARD_BLOCKER
EFFET_BLOCAGE: Immédiat — PASS 2 détecte, PASS 3 corrige obligatoirement

EXEMPLES:
- Q1: Réponse = "Eusebio", Q42: Distractor = "Eusebio" → HARD_COLLISION

→ Règle opérationnelle : voir `STD_B3_distractor_rules.md` [RULE-HB-DIST-001]

---

# SECTION — SOFT_COLLISION

[DEF-SCOLL-001]
SOFT_COLLISION:
Même entité réutilisée dans contextes différents (réponse Q1, distractor Q2).

PRIORITE: SOFT_WARNING
EFFET: Flag pour review, correction recommandée si TYPE 1/5

EXEMPLE:
- Q1: Réponse = "Ronaldo" (contexte: meilleur buteur 1998)
- Q87: Distractor = "Ronaldo" (contexte: nombre de buts) → SOFT_COLLISION

→ Règle opérationnelle : voir `STD_B3_distractor_rules.md` [RULE-SW-DIST-001]

---

# SECTION — PASS_FUNNEL

[DEF-PASS-001]
PASS_FUNNEL:
Trois étapes séquentielles de l'entonnoir B3 (génération, audit, optimisation).

PASS_1_GENERATION:
- Génère 3 distracteurs/question
- Focus: champs obligatoires présents + valeur documentaire mesurée
- Pas de VALIDATION strict collision
- Output: 831 distracteurs bruts

PASS_2_AUDIT:
- Détecte TOUS les FAILURE_CASE (collisions, format, distribution, biais)
- Génère audit report + flags
- Decision gate: GO / CONDITIONAL_GO / NO_GO

PASS_3_OPTIMIZER:
- Corrige UNIQUEMENT items flaggés en PASS 2
- Context-aware intelligent replacements
- Verification pas de nouvelle collision

→ Règle opérationnelle : voir `STD_B3_distractor_rules.md` (section PRIORITY_MATRIX)

---

# SECTION — DECISION_GATE

[DEF-DG-001]
DECISION_GATE:
Mécanisme de validation B3 après PASS 2, avant PASS 3 ou export.

VALEURS_AUTORISEES:
- GO: Tous critères verts, hard collisions = 0, ready for B4
- CONDITIONAL_GO: FAILURE_CASE mineurs fixables en PASS 3, proceed with caution
- NO_GO: FAILURE_CASE critiques nécessitant retour à PASS 1

→ Règles opérationnelles : voir `STD_B3_distractor_rules.md` [RULE-HB-DIST-004]

---

# SECTION — PLAUSIBILITY_RATING

[DEF-PLAUS-001]
PLAUSIBILITY_RATING:
Score subjectif (0-100%) ou catégorisé (LOW/MEDIUM/HIGH) de crédibilité d'un distractor.

SEUIL_CRITIQUE: ≥80% pour TYPE 1/5
SEUIL_ACCEPTABLE: ≥75% pour autres types

CRITERE_EVALUATION:
- Distracteur reconnaissable en contexte ?
- Paraît-il possible pour un joueur moyen ?
- Est-il au bon niveau de notoriété ?

→ Règle opérationnelle : voir `STD_B3_distractor_rules.md` [RULE-SW-DIST-002]

---

# SECTION — FORMAT_HOMOGENEITY

[DEF-FH-001]
FORMAT_HOMOGENEITY:
Pourcentage de questions où réponse correcte + 3 distractors ont format identique.

CRITERES_FORMAT:
- Casse (majuscule/minuscule)
- Accents (respect)
- Structure (année pleine vs abrégée, unités, etc.)

SEUIL_CRITIQUE: ≥99%
SEUIL_ACCEPTABLE: ≥95%

→ Règle opérationnelle : voir `STD_B3_distractor_rules.md` [RULE-HB-DIST-003]

---

# SECTION — REUSE_RATE

[DEF-RR-001]
REUSE_RATE:
Pourcentage de distractors utilisés plus d'une fois inter-questions.

CALCUL: (count(distractors appearing >1 time) / total_distractors) * 100

SEUIL_CRITIQUE: <5%
SEUIL_ACCEPTABLE: 5-10%
SEUIL_ALERTE: >10%

→ Règle opérationnelle : voir `STD_B3_distractor_rules.md` [RULE-OPT-DIST-004]

---

# SECTION — BIAS_DETECTION

[DEF-BIAS-001]
BIAS_DETECTION:
Détection de patterns de sur-représentation dans le pool de distracteurs.

TYPES_BIAS:
- SOURCE_CONCENTRATION: Une source (joueur, pays) >2% de total
- ERA_CLUSTERING: >50% distractors d'une question de même époque
- NATIONALITY_SKEW: Une nationalité >15% de TYPE 1/5 distractors

PRIORITE: OPTIONAL_OPTIMIZER (corrigible en PASS 3 si détecté)

→ Règles opérationnelles : voir `STD_B3_distractor_rules.md` [RULE-OPT-DIST-001 à 003]

---

# SECTION — SKILL_CREATION_PROTOCOL

[DEF-SKILL-001]
SKILL:
Module spécialisé (compétence IA) qui exécute une étape du FACTORY_PIPELINE en lisant règles depuis STD/MDE.

CARACTERISTIQUES:
- Thème-agnostique (aucune dépendance à un domaine nommé)
- Rules-as-Data (lit STD, pas codes en dur)
- Automatisation complète d'une étape

CYCLE_VIE: Création → Intégration → Maintenance

[RULE-SKILL-001]
Chaque skill DOIT avoir une MDE (méthodologie) et une STD (règles) associées.

[RULE-SKILL-002]
Chaque skill DOIT référencer ses dépendances STD/MDE dans le manifest.json.

---

[DEF-SKILL-CREATION-001]
SKILL_CREATION_PROTOCOL:
Processus automatisé d'intégration d'un nouveau skill dans la FACTORY.

CHECKLIST_OBLIGATOIRE:

1. **SKILL.md créé/modifié**
   - Écrit la documentation skill avec section When to Use, Process, Examples

2. **Identifier concepts nouveaux**
   - Extraire tous les nouveaux termes/concepts utilisés par le skill
   - Lister: définitions, métriques, seuils, rôles

3. **Mettre à jour glossaire**
   - [DEF-X-NNN] pour chaque concept nouveau
   - Format standard: OBJET, INPUT, OUTPUT, CONTRAINTES, ERREURS
   - Ajouter [RULE-...] pour comportements obligatoires

4. **Mettre à jour MASTER_ARCHITECTURE.md**
   - Ajouter skill dans section Workflow correspondante
   - Mettre à jour tableau récapitulatif
   - Ajouter references aux documents liés

5. **Enregistrer dans manifest.json**
   - Déclarer skill avec triggers, dependencies

6. **Documentation croisée**
   - Mettre à jour MDE associée pour référencer skill
   - Mettre à jour STD associée pour définir règles que skill exécute

EXEMPLE: Skills B3 (distractors-generator, distractor-audit-statistics, distractor-optimizer)
- MDE_B3_distracteurs.md
- STD_B3_distractor_rules.md
- STD_B3_distractor_metrics.md
- glossaire_documentaire_factory.md (7 nouvelles entries)
- MASTER_ARCHITECTURE.md (mise à jour workflow + references)
- manifest.json (enregistrement)

[RULE-SKILL-CREATION-001]
À chaque création/modification skill, exécuter SKILL_CREATION_PROTOCOL complètement.

[RULE-SKILL-CREATION-002]
Tout skill sans entries glossaire = incomplet, bloque déploiement.

[RULE-SKILL-CREATION-003]
SKILL_CREATION_PROTOCOL est transversal à TOUS les skills (A2, A3, A4, B2, B4, B5, B6, etc.).

---

# SECTION — BIPREGEN

[DEF-BIPREGEN-001]
BIPREGEN:
Base Items Prégénération — BIB normalisée avec codage stable, niveaux harmonisés, index complète.

FORMAT: [THEME]-[CAT]-[NNN]-[NIV]
EXEMPLE: cas source-LEGENDE-001-N2
RETEX_REF: RETEX_GLOSSAIRE_DOCUMENTAIRE_FACTORY_004

[RULE-BIPREGEN-001]
BIPREGEN = source data propre pour génération B2 (jamais modifié après création).

---

# SECTION — ANGIPREGEN

[DEF-ANGIPREGEN-001]
ANGIPREGEN:
Angles Items Prégénération — angles interrogeables par item + exclusions + quotas.

CONTIENT: Angles exploitables per item, inter-item collision rules, quotas questions cibles.

[RULE-ANGIPREGEN-001]
ANGIPREGEN guide la sélection items pour chaque pool en B2.

---

# SECTION — POOLS_ARCHITECTURE

[DEF-POOLS-ARCH-001]
POOLS_ARCHITECTURE:
Définition des 20 pools opérationnels (IF-SF, IF-ROT, QV) avec assignations angles et quotas.

BLOCS: IF-SF (2 pools, 8Q, rotation très lente) + IF-ROT (3 pools, 12Q, lente) + QV (15 pools, 15Q, rapide).

[RULE-POOLS-ARCH-001]
Exactement 20 pools obligatoire. Tous angles ANGIPREGEN assignés.

---

# SECTION — SPREADSHEET_IMPLANTATION

[DEF-XLSX-IMPL-001]
SPREADSHEET_IMPLANTATION:
Mise en place questions + distracteurs dans tableur xlsx — contenu généré en B2/B3, audité en B5.

COLONNES: Q_ID | LIBELLÉ | RÉPONSE | D1 | D2 | D3 | TYPE_Q | CIBLE_NIVEAU | QA_STATUS | POOL_ID

[RULE-XLSX-IMPL-001]
Format QCM strict. Réponse position mélangée aléatoire. Pas modification contenu après FINAL.

---

# SECTION — AUDIT_VALIDATION

[DEF-AUDIT-VAL-001]
AUDIT_VALIDATION:
Validation humaine une question à la fois (énoncé, réponse, distractors, format).

DECISIONS: CONSERVER / MODIFIER / REJETER / DÉPLACER

[RULE-AUDIT-VAL-001]
Une question à la fois (jamais batch). Attendre validation humaine avant suivant.

[RULE-AUDIT-VAL-002]
QA_STATUS assigné : PASS / WARNING / FAIL.

---

# SECTION — RULES_EXTRACTION

[DEF-RULES-EXT-001]
RULES_EXTRACTION:
Extraction de règles généralisables depuis audit cobaye → promotion glossaire FACTORY.

OUTPUT: [RULE-X-Y] extraites + [DEF-X-Y] nouvelles + B6_EDGE_CASES.md

[RULE-RULES-EXT-001]
Règles = généralisables (multi-thème). Edge cases documentés séparément.

---

# SECTION — TOKEN_OPTIMIZATION_MONITORING

[DEF-TOKEN-001]
TOKEN_OPTIMIZATION_MONITORING:
Comportement obligatoire de signalement des opportunités de réduction de tokens avant chaque action ou tool call.

[RULE-TOKEN-MONITOR-001]
CLAUDE SIGNALE CHAQUE OPPORTUNITÉ TOKEN — comportement obligatoire, tous contextes.

SIGNAL_OBLIGATION:
Avant chaque tool call ou réponse, évaluer :
- Peut-on compresser le contexte chargé ?
- Peut-on batch des requêtes ?
- Peut-on remplacer narratif par IDs ?
RETEX_REF: RETEX_GLOSSAIRE_DOCUMENTAIRE_FACTORY_005
- Peut-on réutiliser résultats précédents (caching) ?

FORMAT_SIGNAL:
Insérer avant action si opportunité ≥5% tokens :
```
⚡ OPT: [description] → [économie estimée]
```

EXEMPLES:
- ⚡ OPT: Load section B5_AUDIT only (offset 500-800) → save 12KB
- ⚡ OPT: Batch file reads (A+B+C) in 1 call → save 3 call overhead
- ⚡ OPT: Use [RULE-HCOLL-001] not narrative → save 18 tokens

[RULE-TOKEN-MONITOR-002]
Signal n'est pas bloquant — juste informe des opportunités.

[RULE-TOKEN-MONITOR-003]
Seuil minimum = 5% estimé (ne pas spammer <2%).

---

# SECTION — SESSION_RESUMPTION_PROMPT

[DEF-SRP-001]
SESSION_RESUMPTION_PROMPT:
Document .md auto-généré par Claude quand nouvelle session s'impose (token saturation, context complexity, time checkpoint).

FORMAT_FILENAME: [TASK-CODE]_SESSION_[N]_RESUME_[DATE].md
EXEMPLE: B3_DISTRACTOR_SESSION_02_RESUME_2026-05-17.md

CONTENU_OBLIGATOIRE:
- État session antérieure (complété/en-cours)
- Fichiers modifiés + chemins
- Travail restant (checklist)
- Prompt d'invocation (copie-coller direct)
- Tokens estimés prochaine session

LOCALISATION: Racine TRAVAIL EN COURS (accessible directement)

[RULE-SRP-001]
SESSION_RESUMPTION_PROMPT généré PROACTIVE (avant rupture, pas après).

[RULE-SRP-002]
Naming = [TASK-CODE]_SESSION_[N]_RESUME_[YYYYMMDD].md
- TASK-CODE = A2, B3, B5, etc. (unique par processus)
- SESSION_[N] = numérotation (+1 chaque reprise)
- RESUME = mot-clé pour grep rapide
- DATE = YYYYMMDD pour tri chronologique

[RULE-SRP-003]
Prompt d'invocation = executable directement (copie-coller Laurent → Claude sans édition).

[RULE-SRP-004]
Signal de génération obligatoire : "⚡ SESSION_RESUMPTION_PROMPT créé : [filename]"

[RULE-SRP-005]
DÉTECTION_AUTOMATIQUE : Claude génère SRP quand :
- Context loaded >60KB (saturation)
- Conversation >25 messages (accumulation)
- Task >4 heures estimé (checkpoint)
- Token budget <20% available (proactive)
- Checkpoint intermédiaire explicit (blocage atteint)

ACTION: Générer SRP AVANT limite atteinte (proactive, pas réactive).

---

# SECTION — OPTIMISATION_TOKENS

[OPT-001]
Réduire les synonymes métier.

[OPT-002]
Utiliser YAML pour les structures fixes.

[OPT-003]
Référencer les règles via IDs.

[OPT-004]
Limiter les paragraphes narratifs.

[OPT-005]
Réutiliser les structures documentaires stables.



---

# SECTION — NAMING_CONVENTIONS

# SECTION — NAMING_PATTERN_PROCESS_DOC

[DEF-NAMING-001]
NAMING_PATTERN_PROCESS_DOC:
Document unique produit à une phase donnée, non réitérable.

FORMAT:
```txt
[PHASE]_[INDEX]_[ROLE].md
```

SIGNAL_IA:
_[INDEX]_ en position 2.

CONTRAINTES:
- un seul exemplaire par phase
- index séquentiel obligatoire

---

# SECTION — NAMING_PATTERN_ARTIFACT

[DEF-NAMING-002]
NAMING_PATTERN_ARTIFACT:
Fichier pouvant exister en plusieurs exemplaires ou versions dans une même phase.

FORMAT:
```txt
[PHASE]_[ROLE]_[THEME]_[N].[ext]
```

SIGNAL_IA:
Absence de _[INDEX]_ en position 2.
Suffixe d'état ou d'itération en position finale.

CONTRAINTES:
- suffixe obligatoire (INIT / v[N] / WIP / FINAL)
- pas d'index de phase entre [PHASE] et [ROLE]

---

# SECTION — SUFFIXES_ETAT_XLSX

[DEF-SUFFIX-001]
SUFFIXES_ETAT_XLSX:
Indicateurs d'état du fichier tableur tout au long du pipeline.

VALEURS:
- INIT  : structure vide, créée à l'initialisation de l'étape
- v[N]  : version de travail en cours
- WIP   : en cours d'audit (phase B5)
- FINAL : livrable validé, EXPORT — immuable

[RULE-SUFFIX-001]
Tout fichier xlsx doit porter un suffixe d'état.

[RULE-SUFFIX-002]
FINAL interdit toute modification ultérieure.

---

# SECTION — STOCK_CIBLE

[DEF-STOCK-001]
STOCK_CIBLE:
Nombre de questions validées cibles à atteindre par pool.

CONTEXTE: Colonne STOCK_CIBLE dans feuille SUIVI_POOLS (étape B2).
GATE: gate_b2.py vérifie STOCK_ACTUEL ≥ STOCK_CIBLE → fail si déficit.

[RULE-STOCK-001]
STOCK_ACTUEL < STOCK_CIBLE → NO_GO gate B2 (B2-8).

---

# SECTION — CIBLE_NIVEAU

[DEF-NIV-001]
CIBLE_NIVEAU:
Niveau de difficulté cible assigné à une question lors de la génération B2.

VALEURS_AUTORISEES:
- N1 : facile (grand public)
- N2 : intermédiaire
- N3 : difficile (expert)

CONTEXTE: Colonne obligatoire feuille QUESTIONS (étape B2).
GATE: gate_b2.py — champ obligatoire (B2-2).

---

# SECTION — NIVEAU_CONFIRME

[DEF-NIV-002]
NIVEAU_CONFIRME:
Niveau de difficulté confirmé après audit des distracteurs (étape B3).

VALEURS_AUTORISEES: N1 / N2 / N3

DISTRIBUTION_CIBLE: 30% N1 / 40% N2 / 30% N3 (±10%)
GATE: gate_b3.py — champ obligatoire (B3-2) ; déséquilibre → warning B3-8.

[RULE-NIV-001]
NIVEAU_CONFIRME peut différer de CIBLE_NIVEAU après audit distracteurs.

---

# SECTION — TYPE_Q

[DEF-TYPQ-001]
TYPE_Q:
Classification du type de question selon la taxonomie FACTORY.

VALEURS_AUTORISEES: 1 / 2 / 3 / 4 / 5
CONTEXTE: Colonne obligatoire feuille QUESTIONS (étape B2).
GATE: gate_b2.py — valeur hors [1-5] → NO_GO (B2-6).

---

# SECTION — ECART_CIBLE

[DEF-ECAR-001]
ECART_CIBLE:
Indicateur d'écart entre la difficulté cible d'une question et la difficulté perçue de ses distracteurs.

CONTEXTE: Colonne obligatoire feuille DISTRACTEURS (étape B3).
GATE: gate_b3.py — champ obligatoire (B3-6).

OBJECTIF:
Mesurer si les distracteurs sont calibrés au bon niveau par rapport à la réponse.

---

# SECTION — FLAG_VEILLE

[DEF-VEILLE-001]
FLAG_VEILLE:
Marqueur signalant qu'une question contient un élément potentiellement daté nécessitant une veille documentaire.

MARQUEURS_DETECTES:
dernier, dernière, premier, première, jamais, seul, unique, record,
plus grand, plus petit, plus rapide, meilleur, pire, à ce jour

GATE: gate_b5.py — détection automatique → warning B5-8 (non bloquant).

[RULE-VEILLE-001]
Une question FLAG_VEILLE doit être revue à chaque export.

---

# SECTION — FICHE_VEILLE

[DEF-VEILLE-002]
FICHE_VEILLE:
RETEX_REF: RETEX_GLOSSAIRE_DOCUMENTAIRE_FACTORY_006

RETEX_REF: RETEX_GLOSSAIRE_DOCUMENTAIRE_FACTORY_007
PATTERN_RECHERCHE: *FICHE_VEILLE* / *VEILLE* / *veille*

GATE:
- gate_b5.py — absence → NO_GO (B5-7)
- gate_export.py — absence → NO_GO (EXP-6)

[RULE-VEILLE-002]
FICHE_VEILLE obligatoire avant gate B5 et EXPORT.

---

# SECTION — RICHESSE

[DEF-RICH-001]
RICHESSE:
Classification de la densité documentaire d'un pool.

VALEURS_AUTORISEES:
- DENSE   : pool à forte densité d'angles exploitables
- STANDARD: pool à densité nominale
- LIGHT   : pool avec < 2 angles valides par item, nécessite enrichissement

[RULE-RICH-001]
Un pool LIGHT bloque la génération B2 si STOCK_ACTUEL < STOCK_CIBLE.

---

# SECTION — ITEM_ID_V2

[DEF-IID-001]
ITEM_ID_V2:
Format d'identifiant unique pour une question dans le pipeline V2.

FORMAT: Q_ID tel qu'utilisé dans les feuilles QUESTIONS / QA / EXPORT.
CONVENTION: Stable par question, utilisé pour traçabilité inter-étapes (B2→B3→B5→EXPORT).

[RULE-IID-001]
Q_ID obligatoire dans toutes les feuilles de travail — absence → NO_GO.

---

# SECTION — MODE_AGREGE

[DEF-AGR-001]
MODE_AGREGE:
Mode d'assemblage regroupant les questions de plusieurs pools pour constituer un export livrable.

CONTEXTE: Étape EXPORT — 20 pools × 1 question tirée par pool = 20 questions par partie.
CONTRAINTE: CONSISTENCY thématique et équilibre niveaux vérifiés à l'assemblage.

→ Règles opérationnelles : voir STD_ASM_quiz_assembly_rules.md


---

# SECTION — MACHINE_FIRST_CANONICAL_LEXICON

[DEF-MF-001]
MACHINE_FIRST:
Documentation optimisée pour exécution IA déterministe.

ACCEPTANCE_CRITERIA:
- STRUCTURE_KEY_VALUE_RATE = 100% for execution blocks
- SUBJECTIVE_VALIDATION_COUNT = 0 in active RULE blocks
- IMPLICIT_CONTEXT_DEPENDENCY_COUNT = 0

[RULE-MF-001]
Les documents d’exécution actifs doivent privilégier blocs structurés et validations calculables.

---

# SECTION — EXECUTION_VS_KNOWLEDGE

[DEF-EVK-001]
EXECUTION:
Contenu chargé pendant pipeline actif.

INCLUDES:
- RULE
- INPUT
- PROCESS
- OUTPUT
- CONDITION
- VALIDATION
- FAILURE_CASE
- ACCEPTED
- REJECTED

[DEF-EVK-002]
KNOWLEDGE:
Contenu indexable hors pipeline actif.

INCLUDES:
- RETEX
- EXAMPLE
- ARCHIVE

[RULE-EVK-001]
KNOWLEDGE ne modifie pas EXECUTION sans intégration explicite dans RULE.

[RULE-EVK-002]
RETEX_LOADING = ON_DEMAND_ONLY.

---

# SECTION — CALCULABLE_VALIDATION

[DEF-CV-001]
CALCULABLE_VALIDATION:
Validation exprimée par booléen, enum, seuil, ratio, compteur ou pattern.

AUTHORIZED_FORMS:
- BOOLEAN
- ENUM
- THRESHOLD
- RATIO
- COUNT
- REGEX_PATTERN

FORBIDDEN_FORMS:
- jugement subjectif
- préférence implicite
- formulation narrative
- exception historique non codée

[RULE-CV-001]
Toute validation active doit produire ACCEPTED ou REJECTED.

[RULE-CV-002]
Toute validation active doit avoir au moins une condition observable.

---

# SECTION — CANONICAL_TERMS

[DEF-CANON-001]
CANONICAL_TERMS:
Lexique autorisé pour les blocs d’exécution.

AUTHORIZED_TERMS:
- RULE
- RETEX
- EXAMPLE
- ARCHIVE
- INPUT
- OUTPUT
- PROCESS
- STEP
- ACTION
- CONDITION
- VALIDATION
- FAILURE_CASE
- ACCEPTANCE_CRITERIA
- ACCEPTED
- REJECTED
- BLOCKER
- WARNING
- PASS
- FAIL

[RULE-CANON-001]
Les synonymes documentaires sont interdits dans EXECUTION.

DEPRECATED_TERMS:
- vérifier
- s’assurer
- veiller
- pertinent
- intéressant
- équilibré
- soutenable
- qualitatif
- naturel
- problème
- anomalie
- erreur

REPLACEMENT_MAP:
- vérifier -> VALIDATION
- s’assurer -> VALIDATION
- veiller -> CONDITION
- pertinent -> ACCEPTED
- intéressant -> ACCEPTED
- équilibré -> RATIO_VALIDATED
- soutenable -> THRESHOLD_VALIDATED
- problème -> FAILURE_CASE
- anomalie -> FAILURE_CASE
- erreur -> FAILURE_CASE

---

# SECTION — ACTIVE_CONTEXT_COST

[DEF-ACC-001]
ACTIVE_CONTEXT_COST:
Volume documentaire chargé pendant exécution IA active.

MEASURE:
- active_file_count
- active_token_estimate
- execution_block_count
- redundant_rule_count

[RULE-ACC-001]
Les RETEX, EXAMPLE et ARCHIVE ne sont pas chargés par défaut.

[RULE-ACC-002]
Toute règle dupliquée doit être factorisée ou référencée par DEPENDENCY.

---

# SECTION — GLOSSARY_CHANGELOG

[CHANGE-4.6]
- Ajout MACHINE_FIRST
- Ajout EXECUTION vs KNOWLEDGE
- Ajout CALCULABLE_VALIDATION
- Ajout CANONICAL_TERMS
- Ajout ACTIVE_CONTEXT_COST
- Dépréciation des termes humains-first
- Normalisation ACCEPTED / REJECTED / FAILURE_CASE / VALIDATION

