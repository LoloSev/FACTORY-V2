# CHANTIER MDE STD — BLOCAGES ET ÉCARTS

DATE_CREATION: 2026-05-22
SCOPE: METHODES + STANDARDS uniquement
REFERENCE: CHANTIER_MDE_STD.md (Version 1.1)

---

## ÉTAT DU CHANTIER

DATE_MAJ: 2026-05-22

| Phase | Statut | Difficultés |
|-------|--------|-------------|
| Phase 1 | ✅ TERMINÉE | D-14, D-01, D-02, D-03 |
| Phase 2 | ✅ TERMINÉE | D-04, D-05, D-06, D-07, D-08 (ANT-01) |
| Phase 3 | ⏳ EN ATTENTE | D-09, D-10, D-11, D-12, D-16 |
| Phase 4 | ⏳ EN ATTENTE | D-13, D-15 |

**DÉCISION HUMAINE REQUISE avant Phase 3 :**

> **INC-01 (D-07)** — Seuil anti-collision B5 ambigu :
> - RULE-PCOLL-001 (global) interdit un fait dans plus d'un pool
> - RULE-PCOLL-B5-001 (audit B5) bloque (FAIL) seulement à partir de 3 pools
> - Un fait présent dans 2 pools viole la règle globale mais ne déclenche pas le FAIL B5
>
> **Option A** — Aligner B5 : seuil FAIL = 2 pools (cohérence stricte avec global)
> **Option B** — Documenter intentionnellement : 2 pools = WARNING / 3 pools = FAIL (tolérance B5 assumée)

---

---

## BLOCAGES TECHNIQUES

### BLK-01 — Suppression physique de fichiers impossible

DATE: 2026-05-22
ACTION_DEMANDEE: D-04 — supprimer MDE_BIB_USAGE.md
RAISON: commande `rm` non autorisée sur le dossier workspace par l'environnement IA.
SOLUTION_APPLIQUEE: archivage avec STATUS: ARCHIVED + ARCHIVED_REASON.
ACTION_MANUELLE_REQUISE: supprimer physiquement les fichiers suivants :
- `_FACTORY/METHODES/_A2/MDE_BIB_USAGE.md`

---

## ÉCARTS DE PÉRIMÈTRE

### ECR-01 — MDE_A2.md hors liste D-02 mais contenant seuil obsolète

DATE: 2026-05-22
DETECTE_LORS: D-04 (lecture MDE_A2.md)
NATURE: `RUNTIME_ALIGNMENT` dans MDE_A2.md contenait `fail: >14_words` au lieu de `>15_words`.
ACTION: corrigé immédiatement (hors liste D-02 initiale).
FICHIER: `_FACTORY/METHODES/A2/MDE_A2.md`

---

---

## DÉCISIONS ANTICIPÉES

### ANT-01 — D-08 résolu par alignement (prévu Phase 3)

DATE: 2026-05-22
D_CONCERNE: D-08 (Phase 3 — documenter logique 30/40/30 vs 25/50/25)
DECISION_HUMAINE: aligner distribution distracteurs sur distribution questions.
NOUVELLE_VALEUR: 25% N1 / 50% N2 / 25% N3 (remplace 30/40/30)
FICHIERS_MODIFIES:
- STD_B3_distractor_rules.md (NOTE_DIFFICULTÉ + tableau)
- STD_B3_distractor_metrics.md (Target + 5 lignes par TYPE)
- MDE_B3_distracteurs.md
- SKILL.md
- glossaire_documentaire_factory.md
STATUT_D08: CLOS — plus de divergence à documenter.

---

## INCOHÉRENCES DÉTECTÉES

### INC-01 — Seuil RULE-PCOLL-B5-001 ≠ RULE-PCOLL-001

DATE: 2026-05-22
DETECTE_LORS: D-07
NATURE: RULE-PCOLL-001 (global) dit "un seul pool principal". RULE-PCOLL-B5-001 (B5) dit "≥ 3 pools → FAIL". Un fait présent dans 2 pools viole PCOLL-001 mais ne déclenche pas PCOLL-B5-001.
OPTIONS: (a) aligner PCOLL-B5-001 sur seuil = 2 / (b) documenter intentionnellement que B5 tolère 2 pools (WARNING) et bloque à 3 (FAIL).
ACTION_REQUISE: décision humaine.
FICHIERS: STD_B5_pool_collision_rules.md / STD_GLOBAL_pool_collision_rules.md

---

*CHANTIER_BLOCAGES_ET_ECARTS.md — 2026-05-22*
