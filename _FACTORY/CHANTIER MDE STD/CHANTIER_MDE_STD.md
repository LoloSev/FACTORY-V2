# CHANTIER MDE STD — AUDIT ET PLANIFICATION

VERSION: 1.1
DATE: 2026-05-22
STATUS: ACTIVE
SCOPE: METHODES + STANDARDS uniquement — MAYENNE et autres lignes exclus

---

## PRINCIPES INTANGIBLES (non négociables)

- POOL_COUNT = 20
- STOCK_CIBLE = 277 (constante contractuelle — justification applicative, hors pipeline)
- CIBLE_NIVEAU top-down par POSITION_QUIZ :
  - Q1–Q5 = N1
  - Q6–Q15 = N2
  - Q16–Q20 = N3
- QCM : 4 choix, 1 seule bonne réponse
- 1 question tirée par pool par partie

## ARCHITECTURE POOLS — TABLE DE DÉRIVATION (validée)

Deux types uniquement : **IF** (Incontournables) et **QV** (Questions Variables).
TYPE, STOCK_CIBLE et CIBLE_NIVEAU sont dérivés automatiquement depuis POSITION_QUIZ.

| POSITION_QUIZ | TYPE | STOCK_CIBLE | CIBLE_NIVEAU |
|---------------|------|-------------|--------------|
| Q1–Q2 | IF | 8 | N1 |
| Q3–Q5 | IF | 12 | N1 |
| Q6–Q15 | QV | 15 | N2 |
| Q16–Q20 | QV | 15 | N3 |

Vérification : (2×8) + (3×12) + (10×15) + (5×15) = 16 + 36 + 150 + 75 = **277 ✓**

Règle d'exclusivité : les angles IF ne peuvent pas être assignés à un pool QV.

> Remplace la nomenclature IF-SF / IF-ROT / QV. Les anciens identifiants IF-SF et IF-ROT
> sont abandonnés — leur signification n'était pas documentée et leur distinction
> est purement applicative (hors pipeline).

---

## PARTIE 1 — INVENTAIRE DES DIFFICULTÉS

---

### D-01 — CONFLIT V1 / V2 : arborescence obsolète
**Fichiers concernés :** `STD_GLOBAL_factory_arborescence_rules.md`, `STD_A4_pool_format_rules.md`, `STD_A4_pool_workflow_rules.md`
**Nature :** Ces 3 fichiers décrivent encore la structure V1 (BIPREGEN.txt, ANGIPREGEN.txt, POOLS_[THEME].txt, A5_TABLEUR/, B4_IMPLANTATION/, B6_REGLES/). MDE_A3 v3.0 et STD_NAMING_CONVENTIONS les ont explicitement supprimés en V2.
**Sévérité :** 🔴 Critique — conflit direct avec V2

---

### D-02 — CONFLIT : seuil longueur question (3 valeurs)
**Fichiers concernés :** `A1_LIGNES_TEMPLATE.md`, `MDE_B2_generation.md`, `SKILL.md`
**Nature :**
| Document | Seuil déclaré |
|----------|--------------|
| A1_LIGNES_TEMPLATE.md | FAIL > 14 mots |
| MDE_B2_generation.md (ACCEPTANCE_CRITERIA) | max = 10 mots |
| SKILL.md RULE-UNIV-Q-001 | FAIL > 15 mots |

Trois seuils incompatibles pour la même contrainte.
**Sévérité :** 🔴 Critique — ambiguïté d'exécution directe

---

### D-03 — VIOLATION LINE_DEPENDENCY : contenu football dans STD génériques
**Fichiers concernés :** `STD_B3_distractor_rules.md`, `STD_B3_distractor_metrics.md`, `QUIZ_ASSEMBLY_RULES.md`, `STD_B5_density_rules.md`, `STD_B2_generation_rules.md`
**Nature :** Ces fichiers déclarent `LINE_DEPENDENCY: FORBIDDEN` mais contiennent du contenu spécifique à la ligne "cas source" (football) traité comme règle universelle :
- RULE-T3-001 : "23 années maximum" (hardcodé cas source)
- RULE-T4-001 : "Pays hôtes cas source réels SEULEMENT"
- RULE-T1-001 : "base cas source : joueurs/équipes célèbres, multi-éditions"
- STD_B3_distractor_metrics.md : "831 distractors" (277×3, hardcodé cas source)
- QUIZ_ASSEMBLY_RULES.md : sections Joueurs / Finales / Nations (100% football)
- STD_B5_density_rules.md : "surreprésentations joueur / nation / édition"
- RULE-B2-OPT-003 : "Calcio, Seleção, Albiceleste"
- RULE-B2-OPT-004 : "Numéros de maillot"

Les exemples concrets sont utiles à l'IA — mais ils doivent être tagués `[EXEMPLE]` et les valeurs hardcodées doivent être paramétriques.
**Sévérité :** 🔴 Critique — l'IA applique du football à tous les thèmes

---

### D-04 — REDITE : usage du BIB défini deux fois
**Fichiers concernés :** `METHODES/_A2/MDE_BIB_USAGE.md`, `STANDARDS/_GLOBAL/STD_BIB_USAGE.md`
**Nature :** Contenu quasi-identique dans les deux fichiers. STD_BIB_USAGE est plus complet.
**Sévérité :** 🟠 Important — double maintenance

---

### D-05 — REDITE : 8 filtres rédaction en 3 endroits
**Fichiers concernés :** `STD_B2_generation_rules.md`, `MDE_B2_generation.md`, `SKILL.md`
**Nature :** RULE-B2-HB-002 définie complètement dans STD, résumée dans MDE et SKILL. Toute modification doit être appliquée à 3 fichiers simultanément.
**Sévérité :** 🟠 Important — risque de dérive entre copies

---

### D-06 — REDITE : distribution difficulté quiz répétée 3 fois
**Fichiers concernés :** `STD_GLOBAL_quiz_architecture_rules.md`, `QUIZ_ASSEMBLY_RULES.md`, `MDE_A2.md`
**Nature :** N1=5 / N2=10 / N3=5 déclaré 3 fois dans 3 documents distincts.
**Sévérité :** 🟠 Important — source de vérité non unique

---

### D-07 — REDITE : anti-collision définie 5 fois
**Fichiers concernés :** `STD_GLOBAL_pool_collision_rules.md`, `STD_B5_pool_collision_rules.md`, `STD_B3_distractor_rules.md`, `FACTORY_QA_RULES.md`, `MDE_B2_generation.md`
**Nature :** Même concept répété sous 5 formes dans 5 documents différents.
**Sévérité :** 🟠 Important — fragmentation, risque d'incohérence progressive

---

### D-08 — INCOHÉRENCE : distribution distracteurs vs distribution pools
**Fichiers concernés :** `STD_GLOBAL_quiz_architecture_rules.md`, `STD_B3_distractor_metrics.md`, `STD_B3_distractor_rules.md`
**Nature :** Distribution pools : N1=25% / N2=50% / N3=25%. Distribution distracteurs cible : N1=30% / N2=40% / N3=30%. La logique reliant ces deux distributions n'est pas documentée. STD_B3_distractor_rules contient une note d'explication mais elle est insuffisante.
**Sévérité :** 🟠 Important — incohérence non expliquée

---

### D-09 — FICHIERS STUBS : règles sans seuils mesurables
**Fichiers concernés :** `STD_B5_density_rules.md`, `STD_B5_difficulty_curve_rules.md`, `STD_B5_distractor_quality_rules.md`, `STD_B5_factory_quality_rules.md`, `STD_B6_hard_blockers_rules.md`, `STD_B6_soft_warnings_rules.md`, `STD_B6_optional_optimizer_rules.md`
**Nature :** 7 fichiers avec des règles vides de critères mesurables (pas de seuil, pas d'action, pas d'enum). FACTORY_QA_RULES.md couvre la même matière avec des seuils réels.
**Sévérité :** 🟠 Important — règles non exécutables par l'IA

---

### D-10 — RÉFÉRENCE MORTE : STD_ASM_quiz_assembly_rules.md
**Fichiers concernés :** `glossaire_documentaire_factory.md` (DEF-AGR-001)
**Nature :** Le glossaire cite `STD_ASM_quiz_assembly_rules.md` qui n'existe pas. Le fichier existant s'appelle `QUIZ_ASSEMBLY_RULES.md`.
**Sévérité :** 🟠 Important — lien mort

---

### D-11 — LACUNE STRUCTURELLE : feuille SOMMAIRE hors canonique
**Fichiers concernés :** `MDE_A4_tableur_pools.md`, toutes les MDE
**Nature :** MDE_A4 impose une feuille SOMMAIRE dans le xlsx. Les 7 feuilles canoniques déclarées partout (CONFIG / ITEMS / ANGLES / POOLS / QUESTIONS / DISTRACTEURS / QA) ne l'incluent pas. Le xlsx a donc 8 feuilles, pas 7.
**Sévérité :** 🟡 Secondaire — incohérence de contrat

---

### D-12 — CONFLIT NOMINAL : FICHE_VEILLE vs FICHE_MONITORING
**Fichiers concernés :** `MDE_B5_audit.md`, `SKILL.md`, `STD_OBSOLESCENCE_WATCH_RULES.md`
**Nature :** MDE_B5 appelle ce document FICHE_MONITORING. SKILL.md et STD_OBSOLESCENCE l'appellent FICHE_VEILLE. Même objet, deux noms.
**Sévérité :** 🟡 Secondaire — ambiguïté nominale

---

### D-13 — INCOHÉRENCE DOSSIER : A2 mal nommé
**Fichiers concernés :** `METHODES/A2/` vs `METHODES/_A2/`
**Nature :** Tous les dossiers METHODES utilisent le préfixe underscore (_A3, _A4, _B2…) sauf A2 qui existe en double : `METHODES/A2/` (MDE_A2.md) et `METHODES/_A2/` (MDE_BIB_USAGE.md).
**Sévérité :** 🟡 Secondaire — convention nommage

---

### D-14 — REFONTE NOMENCLATURE : IF-SF / IF-ROT / QV → IF / QV
**Fichiers concernés :** tous les MDE et STD référençant IF-SF, IF-ROT, QV
**Nature :** La distinction IF-SF / IF-ROT n'est pas documentée (SF = non défini), est purement applicative et crée de l'ambiguïté. Remplacée par une table de dérivation positionnelle (voir ARCHITECTURE POOLS ci-dessus).
**Décision :** VALIDÉE — IF et QV uniquement, tout dérivé depuis POSITION_QUIZ.
**Sévérité :** 🔴 Critique — impacte tous les fichiers MDE/STD

---

### D-15 — LACUNE STRUCTURELLE : rationale stocks 8/12/15 non documentée
**Fichiers concernés :** `HIERARCHIE_REGLEMENTAIRE.md`
**Nature :** Les stocks 8 (IF Q1-Q2), 12 (IF Q3-Q5), 15 (QV) dérivent du contrat applicatif (rotation/tirage/277). La chaîne logique est absente des MDE/STD. Une note explicative suffit — pas besoin de justification technique dans la pipeline.
**Sévérité :** 🟡 Secondaire — traçabilité manquante

---

### D-16 — ARBORESCENCE : état lignes hardcodé dans STD global
**Fichiers concernés :** `STD_GLOBAL_factory_arborescence_rules.md`
**Nature :** La section FICHIERS_REFERENCE liste des fichiers spécifiques à MAYENNE et CINEMA avec leur état d'avancement. Documentation d'état dans un STD normatif.
**Sévérité :** 🟡 Secondaire — pollution documentaire

---

## PARTIE 2 — PLANIFICATION DU CHANTIER

---

### PHASE 1 — Élimination des conflits bloquants
*Prérequis à toute autre modification. Durée estimée : courte.*

| ID | Action | Fichiers touchés |
|----|--------|-----------------|
| D-14 | Remplacer IF-SF / IF-ROT / QV par IF / QV dans tous les MDE et STD. Intégrer la table de dérivation positionnelle. | Tous |
| D-01 | Archiver STD_A4_pool_format_rules.md et STD_A4_pool_workflow_rules.md (V1 obsolètes). Réécrire STD_GLOBAL_factory_arborescence_rules.md en V2. | 3 fichiers |
| D-02 | Définir seuil unique longueur question dans STD_B2_generation_rules.md. MDE_B2 et SKILL.md pointent vers cette règle. | 3 fichiers |
| D-03 | Paramétrer les valeurs hardcodées dans les STD génériques. Tagger les exemples cas source `[EXEMPLE-xx-001]`. | 5 fichiers |

---

### PHASE 2 — Élimination des redites
*Après Phase 1. Durée estimée : moyenne.*

| ID | Action | Fichiers touchés |
|----|--------|-----------------|
| D-04 | Supprimer MDE_BIB_USAGE.md. MDE_A2 pointe vers STD_BIB_USAGE.md. | 1 suppression |
| D-05 | Les 8 filtres rédaction : source unique = STD_B2_generation_rules.md RULE-B2-HB-002. MDE_B2 et SKILL.md pointent, ne recopient plus. | 2 fichiers |
| D-06 | Distribution N1/N2/N3 : source unique = STD_GLOBAL_quiz_architecture_rules.md RULE-ARCH-006. Supprimer des autres. | 2 fichiers |
| D-07 | Anti-collision : consolider en source unique STD_GLOBAL_pool_collision_rules.md. Les autres fichiers pointent ou résument sans redéfinir. | 4 fichiers |

---

### PHASE 3 — Complétion des stubs et corrections structurelles
*Après Phase 2. Durée estimée : longue.*

| ID | Action | Fichiers touchés |
|----|--------|-----------------|
| D-08 | Documenter la logique reliant 30/40/30 (distracteurs) au 25/50/25 (pools). Ajouter dans STD_B3_distractor_rules.md. | 1 fichier |
| D-09 | ✅ **DÉCIDÉ Option B** — Supprimer les 7 stubs B5/B6. FACTORY_QA_RULES.md = source unique QA. Mettre à jour les références. | 7 suppressions |
| D-10 | Corriger référence DEF-AGR-001 : STD_ASM → QUIZ_ASSEMBLY_RULES.md. | 1 fichier |
| D-11 | Ajouter SOMMAIRE aux 7 feuilles canoniques → 8 feuilles officielles. Mettre à jour toutes les MDE. | 5+ fichiers |
| D-12 | Nom unique retenu : **FICHE_VEILLE**. Mettre à jour MDE_B5. | 1 fichier |
| D-16 | Retirer la section FICHIERS_REFERENCE de STD_GLOBAL_factory_arborescence_rules.md. | 1 fichier |

---

### PHASE 4 — Clarifications éditoriales
*Après Phase 3. Durée estimée : courte.*

| ID | Action | Fichiers touchés |
|----|--------|-----------------|
| D-13 | Renommer METHODES/A2/ en METHODES/_A2/. Fusionner si MDE_BIB_USAGE supprimé (Phase 2). | 1 dossier |
| D-15 | Ajouter note dans HIERARCHIE_REGLEMENTAIRE : stocks 8/12/15 = contrat applicatif (277, rotation) — hors pipeline. | 1 fichier |

---

## PARTIE 3 — RÈGLE DE TRAITEMENT DES EXEMPLES

À appliquer systématiquement en Phase 1 sur tout contenu ligne-spécifique maintenu comme illustration :

```
[RULE-XX-001]
Principe universel formulé sans référence à une ligne.
Paramètres : [CORPUS_ACTIF], [ENTITÉ], [PÉRIODE], [CATÉGORIE].

[EXEMPLE-XX-001 — cas source]
Application sur la ligne cas source :
→ [valeur concrète football]
→ Transposer sur autre thème : remplacer [X] par l'équivalent du corpus actif.
```

Les règles contiennent des paramètres. Les exemples contiennent des valeurs. Les deux ne se mélangent pas.

---

## RÉCAPITULATIF SÉVÉRITÉS

| Sévérité | Nombre | IDs |
|----------|--------|-----|
| 🔴 Critique | 4 | D-01, D-02, D-03, D-14 |
| 🟠 Important | 6 | D-04, D-05, D-06, D-07, D-08, D-09, D-10 |
| 🟡 Secondaire | 5 | D-11, D-12, D-13, D-15, D-16 |
| **Total** | **16** | |

---

## DÉCISIONS HUMAINES — TOUTES TRANCHÉES

| ID | Décision |
|----|---------|
| D-09 | ✅ Option B — consolider dans FACTORY_QA_RULES.md, supprimer les 7 stubs |
| D-14 | ✅ Refonte nomenclature — IF / QV uniquement, table de dérivation positionnelle |
| D-03 | ✅ Option A — exemples tagués `[EXEMPLE]` dans les STD existants |

---

*CHANTIER_MDE_STD.md — Version 1.1 — 2026-05-22*
