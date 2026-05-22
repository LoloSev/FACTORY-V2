IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE


DEPENDENCY:
- MASTER_ARCHITECTURE.md
- glossaire_documentaire_factory.md
# AUDIT RÈGLES — INTÉGRITÉ & COMPARATIF

**Date:** 2026-05-18
**Statut:** PRIORITÉ ABSOLUE 1 — produit par audit systématique
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_001

---

## SECTION 1 — COMPARATIF COBAYE 78 vs cas source
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_002

### 1.1 Règles Communes (même concept, énoncé équivalent)

| Règle cas source | Équivalent COBAYE 78 | Nuances |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_003
|-----------|---------------------|---------|
| R01 Zéro Filler | RULE-DIST-1-1 (QA_STATUS sources) | cas source = généraliste; COBAYE 78 = B3 spécifique |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_004
| R08 Anti-collision avant répartition | RULE-DIST-TRANS-1 + VAL-COLL-001 | cas source = conception angles; COBAYE 78 = affectation distracteurs |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_005
| R37 Collision par réponse identique | RULE-DIST-TRANS-1 + VAL-COLL-002 | cas source = B2 angles; COBAYE 78 = B3 distracteurs |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_006
| R10 Réponse univoque | RULE-DIST-2-3 / 3-3 | cas source = formulation question; COBAYE 78 = validation distracteur |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_007
| R03 Checklist BIPREGEN (format) | RULE-DIST-TRANS-2 + FORMAT règles | cas source = questions; COBAYE 78 = distracteurs |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_008
| R28 Pas d'invention noms | RULE-DIST-TRANS-3 | cas source = questions; COBAYE 78 = distracteurs — même principe |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_009

**Synthèse:** 6 concepts partagés, énoncés différents car phases différentes (B2 vs B3).

---

### 1.2 Règles Exclusives cas source (absentes de COBAYE 78)
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_010

| Règle | Domaine | Raison absence COBAYE 78 |
|-------|---------|--------------------------|
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_011
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_012
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_013
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_014
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_015
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_016
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_017
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_018
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_019
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_020
| R28/R29/R33 Désambiguïsation noms | B2 — cas source-spécifique | COBAYE 78 thème Cinema — différent |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_021
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_022
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_023
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_024

---

### 1.3 Règles Exclusives COBAYE 78 (absentes de cas source)
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_025

| Règle | Domaine | Raison absence cas source |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_026
|-------|---------|---------------------|
| RULE-DIST-1-x à 5-x (TYPE 1-5) | B3 — distracteurs par type | cas source n'a pas encore produit règles B3 |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_027
| VAL-COLL-001/002 | Métriques QA_STATUS B3 | cas source en phase B2 — B3 non démarré |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_028
| VAL-FMT-001/002/003 | Métriques format B3 | idem |
| VAL-DIFF-001/002 | Distribution difficulté distracteurs | idem |
| VAL-COH-001/002 | CONSISTENCY distracteurs | idem |
| VAL-PLAUS-001 | Plausibilité | idem |
| VAL-BIAS-001 à 004 | Biais sources/ères/nationalités | idem |
| GEN_NOTE_008 promu | B3 global view obligatoire | cas source: décision déjà intégrée en FACTORY |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_029

---

### 1.4 Contradictions Détectées

**Aucune contradiction directe identifiée.** Les deux cobayes couvrent des phases différentes (COBAYE 78 = B3 distracteurs / cas source = B2 génération). Les concepts partagés (anti-collision, no invention, format homogène) sont formulés différemment mais compatibles.
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_030

> ⚠️ **Point de vigilance:** R07 cas source (valeur intrinsèque de l'angle) vs COBAYE 78 RULE-DIST-1-4 (plausibilité distracteur). Ce sont deux VALIDATIONS orthogonaux qui ne se contredisent pas mais doivent s'articuler: un angle de valeur peut produire un distracteur implausible et vice-versa. Documenter comme complémentaires.
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_031

---

### 1.5 Lacunes Identifiées (FAILURE_CASE observé, aucune règle correspondante)

| # | Lacune | Observé dans | Règle manquante |
|---|--------|-------------|-----------------|
| **L01** | Questions révélant réponse dans libellé | cas source PASS 3 — QV-11-Q001 invalide | Audit pédagogique recevabilité (REGLE ABSOLUE manquante) |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_032
| **L02** | Pas de méthodologie surqualification N2→N1 | cas source PASS 3 — 100% manuel | Matrice décision TYPE × écart + seuil validité distracteur post-surqual. |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_033
| **L03** | GAP N3 insoluble (2.9% vs 5% cible) | cas source PASS 3 | Règle "audit irrecevables avant reclassification" |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_034
| **L04** | Veille obsolescence non formalisée dans FACTORY | cas source — 8 questions FLAG requis | STD dédié (STD_OBSOLESCENCE_WATCH_RULES.md existe mais non peuplé des types) |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_035
| **L05** | GEN_NOTES 001-007 COBAYE 78 non promues | COBAYE 78 | Tests multi-thèmes requis avant promotion |

---

## SECTION 2 — COMPARATIF COBAYE 78/cas source vs FACTORY ACTUEL
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_036

### 2.1 Règles COBAYE/cas source PRÉSENTES en FACTORY
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_037

| Règle source | Équivalent FACTORY | Localisation FACTORY | Statut |
|-------------|-------------------|---------------------|--------|
| RULE-DIST (TYPE 1-5) | RULE-T1 à T5 | `STD_B3_distractor_rules.md` | ✅ INTÉGRÉES |
| RULE-DIST-TRANS-1/2/3/4/5 | RULE-HB-DIST-001 à 004 + RULE-SW/OPT-DIST | `STD_B3_distractor_rules.md` | ✅ INTÉGRÉES |
| VAL-COLL/FMT/DIFF | Métriques B3 | `STD_B3_distractor_metrics.md` | ✅ INTÉGRÉES |
| GEN_NOTE_008 (B3 global view) | Décision architecture | `MDE_B3_distracteurs.md` | ✅ INTÉGRÉE |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_038
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_039

---

### 2.2 Règles COBAYE/cas source ABSENTES du FACTORY
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_040

| Règle source | Code | Criticalité | Action requise |
|-------------|------|-------------|----------------|
| R03 Checklist BIPREGEN | cas source BLOC 1 | **ABSOLU** | Ajouter à `FACTORY_QA_RULES.md` ou créer `STD_B2_generation_rules.md` |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_041
| R07 Triple Filtre Validation | cas source BLOC 2 | **ABSOLU** | Ajouter à `FACTORY_QA_RULES.md` ou créer `STD_B2_generation_rules.md` |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_042
| R37 Collision réponse identique (B2) | cas source BLOC 2 | **ABSOLU** | Étendre `STD_GLOBAL_pool_collision_rules.md` — couvre actuellement B3 uniquement |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_043
| R10 Réponse univoque (angle) | cas source BLOC 2 | ABSOLU | Ajouter à standard B2 |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_044
| R01 Zéro Filler (génération) | cas source BLOC 1 | ABSOLU | Ajouter à standard B2 |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_045
| R04 Boucle complète corrections | cas source BLOC 1 | ABSOLU | Ajouter à standard B2 |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_046
| Audit pédagogique recevabilité (L01) | LACUNE | **ABSOLU** | Créer `STD_B2_recevabilite_pedagogique.md` |
| Méthodologie surqualification (L02) | LACUNE | SOFT | Créer `STD_B3_surqualification_methodology.md` |
| Veille obsolescence types 1-5 (R34) | cas source BLOC 9 | ABSOLU | Peupler `STD_OBSOLESCENCE_WATCH_RULES.md` |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_047
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_048
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_049

---

### 2.3 Règles FACTORY non mentionnées dans les COBAYE

| Règle FACTORY | Localisation | Statut dans COBAYE |
|--------------|-------------|-------------------|
| RULE-ARCH-001/002/003 (20 pools, 277 questions) | `STD_GLOBAL_quiz_architecture_rules.md` | Non testé directement — appliqué par construction |
| RULE-HB-001 à 004 (hard blockers pipeline) | `STD_B6_hard_blockers_rules.md` | Non testé en COBAYE 78 (pas de pipeline B5 complet) |
| RULE-B6-001/002 (matrice priorités) | `STD_B6_rule_priority_matrix.md` | Implicitement appliqué en cas source PASS 1/2/3 |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_050
| RULE-B5QA-001 à 005 (philosophie QA) | `FACTORY_QA_RULES.md` | Très minimal — insuffisant |
| CHECK codes (format FACTORY) | `STD_B5_factory_format_rules.md` | Non testé |

---

### 2.4 Doublons / Variantes entre FACTORY et COBAYE

| Concept | COBAYE 78 | RETEX source | FACTORY | Verdict |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_051
|---------|-----------|-----------|---------|---------|
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_052
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_053
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_054
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_055

---

### 2.5 Règles FACTORY Obsolètes ou Insuffisantes

| Règle | FAILURE_CASE |
|-------|---------|
| `FACTORY_QA_RULES.md` | Seulement 5 règles génériques — très insuffisant vs richesse cas source |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_056
| `STD_B6_rule_priority_matrix.md` | Seulement 2 règles + ordre priorité — incomplet |
| `STD_B6_hard_blockers_rules.md` | 4 blockers très généraux — pas de détail procédural |

---

## SECTION 3 — BILAN GLOBAL

### Totaux règles identifiées

| Source | Règles formalisées | Règles ABSOLU | Migré FACTORY |
|--------|-------------------|---------------|---------------|
| COBAYE 78 | 37 (B3) + 14 (QA_STATUS) = 51 | 5 (P0_BLOCKING) | ~85% ✅ |
| RETEX source | 37 (B2) | 14 | ~10% ⚠️ |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_057
| FACTORY (avant audit) | ~30 règles documentées | — | — |

### Priorité d'actions post-audit

| Priorité | Action | Fichier cible |
|----------|--------|---------------|
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_058
| 🔴 P0 | Créer STD_B2_recevabilite_pedagogique.md (LACUNE L01) | `_STANDARDS/_B2/STD_B2_recevabilite_pedagogique.md` (NOUVEAU) |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_059
| 🟡 P1 | Créer STD_B3_surqualification_methodology.md (LACUNE L02) | `_STANDARDS/STD_B3_surqualification_methodology.md` (NOUVEAU) |
| 🟡 P1 | Enrichir FACTORY_QA_RULES.md | `_STANDARDS/_B5/FACTORY_QA_RULES.md` |
RETEX_REF: RETEX_AUDIT_REGLES_INTEGRITE_060
| 🟢 P2 | Tester GEN_NOTES 001-007 sur thèmes variés | COBAYE Rock ou Rap |

---

*Audit rédigé: 2026-05-18 — PRIORITÉ ABSOLUE 1*


