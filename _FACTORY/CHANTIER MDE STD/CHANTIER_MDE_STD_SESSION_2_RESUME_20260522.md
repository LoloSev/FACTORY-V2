# SESSION RESUMPTION — CHANTIER MDE STD
# Session 2 — 2026-05-22

---

## ÉTAT SESSION PRÉCÉDENTE

Chantier documentaire METHODES + STANDARDS (scope strict — MAYENNE et lignes thème exclus).
Référence : `_FACTORY/CHANTIER MDE STD/CHANTIER_MDE_STD.md` (Version 1.1)
Suivi blocages/écarts : `_FACTORY/CHANTIER MDE STD/CHANTIER_BLOCAGES_ET_ECARTS.md`

Phase 1 : ✅ TERMINÉE (D-14, D-01, D-02, D-03)
Phase 2 : ✅ TERMINÉE (D-04, D-05, D-06, D-07, D-08 clos par ANT-01)
Phase 3 : ⏳ EN ATTENTE
Phase 4 : ⏳ EN ATTENTE

---

## DÉCISION HUMAINE REQUISE AVANT PHASE 3

**INC-01** — Seuil anti-collision B5 (voir CHANTIER_BLOCAGES_ET_ECARTS.md) :
- Option A : FAIL dès 2 pools (cohérence stricte RULE-PCOLL-001)
- Option B : 2 pools = WARNING / 3 pools = FAIL (tolérance B5 assumée)

Fichiers concernés : `STD_B5_pool_collision_rules.md` / `STD_GLOBAL_pool_collision_rules.md`

---

## FICHIERS MODIFIÉS (sessions 1+2)

### Phase 1
- `_FACTORY/METHODES/_A4/MDE_A4_tableur_pools.md`
- `_FACTORY/_STANDARDS/_GLOBAL/QUIZ_ASSEMBLY_RULES.md`
- `_FACTORY/_STANDARDS/_GLOBAL/HIERARCHIE_REGLEMENTAIRE.md`
- `_FACTORY/_STANDARDS/_GLOBAL/STD_GLOBAL_pool_collision_rules.md`
- `_FACTORY/_STANDARDS/_B5/STD_B5_pool_collision_rules.md`
- `_FACTORY/_STANDARDS/_GLOBAL/glossaire_documentaire_factory.md`
- `_FACTORY/_STANDARDS/_A4/STD_A4_pool_format_rules.md` (ARCHIVED_V1)
- `_FACTORY/_STANDARDS/_A4/STD_A4_pool_workflow_rules.md` (ARCHIVED_V1)
- `_FACTORY/_STANDARDS/_GLOBAL/STD_GLOBAL_factory_arborescence_rules.md` (V2)
- `_FACTORY/_STANDARDS/_B2/STD_B2_generation_rules.md`
- `_FACTORY/METHODES/_B2/MDE_B2_generation.md`
- `_FACTORY/METHODES/A1/A1_LIGNES_TEMPLATE.md`
- `_FACTORY/METHODES/_GLOBAL/SKILL.md`
- `_FACTORY/_STANDARDS/_B3/STD_B3_distractor_rules.md`
- `_FACTORY/_STANDARDS/_B3/STD_B3_distractor_metrics.md`
- `_FACTORY/_STANDARDS/_B5/STD_B5_density_rules.md`

### Phase 2
- `_FACTORY/METHODES/_A2/MDE_BIB_USAGE.md` (STATUS: ARCHIVED — suppression physique manuelle requise)
- `_FACTORY/METHODES/A2/MDE_A2.md`
- `_FACTORY/METHODES/_B3/MDE_B3_distracteurs.md`
- `_FACTORY/_STANDARDS/_B3/STD_B3_distractor_rules.md` (DEPENDENCY + refs RULE-PCOLL-004)
- `_FACTORY/_STANDARDS/_B5/STD_B5_pool_collision_rules.md` (DEPENDENCY + refs globales)
- `_FACTORY/_STANDARDS/_GLOBAL/FACTORY_QA_RULES.md` (DEPENDENCY)
- `_FACTORY/CHANTIER MDE STD/CHANTIER_BLOCAGES_ET_ECARTS.md`

---

## TRAVAIL RESTANT

### Phase 3
- **D-09** : supprimer 7 fichiers stubs (liste dans CHANTIER_MDE_STD.md)
- **D-10** : corriger référence morte (à identifier dans CHANTIER_MDE_STD.md)
- **D-11** : SOMMAIRE → 8 feuilles xlsx (fichier à identifier)
- **D-12** : FICHE_VEILLE (fichier à identifier)
- **D-16** : supprimer bloc FICHIERS_REFERENCE (fichier à identifier)

### Phase 4
- **D-13** : renommer `METHODES/A2/` → `METHODES/_A2/`
- **D-15** : noter stocks 8/12/15 dans HIERARCHIE_REGLEMENTAIRE.md

### Action manuelle (hors IA)
- Supprimer physiquement : `_FACTORY/METHODES/_A2/MDE_BIB_USAGE.md`

---

## PROMPT COPIE-COLLER

```
Reprise du chantier documentaire METHODES + STANDARDS (quiz-core-lab).

Contexte :
- Phases 1 et 2 terminées.
- Suivi : `_FACTORY/CHANTIER MDE STD/CHANTIER_BLOCAGES_ET_ECARTS.md`
- Plan complet : `_FACTORY/CHANTIER MDE STD/CHANTIER_MDE_STD.md` (Version 1.1)

Avant de démarrer la Phase 3, lire :
1. CHANTIER_BLOCAGES_ET_ECARTS.md (décision INC-01 requise)
2. CHANTIER_MDE_STD.md (liste D-09 à D-16)

Attendre la décision humaine sur INC-01, puis attaquer D-09 action par action.
Signaler toute difficulté dans CHANTIER_BLOCAGES_ET_ECARTS.md.
```

---

*CHANTIER_MDE_STD_SESSION_2_RESUME_20260522.md*
