# SESSION RESUMPTION — CHANTIER MDE STD

DATE: 2026-05-22
STATUT: PRÊT À DÉMARRER — RÉFLEXION HUMAINE EN COURS

---

## CONTEXTE

Audit complet des dossiers METHODES et STANDARDS de la FACTORY quiz.
Les sauvegardes des dossiers originaux STD et MDE sont conservées hors accès IA.
Le chantier n'a pas encore démarré — aucun fichier n'a été modifié.

## DOCUMENT DE RÉFÉRENCE

`_FACTORY/CHANTIER MDE STD/CHANTIER_MDE_STD.md` (Version 1.1)
Contient : inventaire des 16 difficultés, planification en 4 phases, décisions validées.

---

## CE QUI EST DÉCIDÉ ET INTANGIBLE

### Architecture pools (nouvelle — validée)
Deux types uniquement : IF et QV. Tout dérivé depuis POSITION_QUIZ.

| POSITION_QUIZ | TYPE | STOCK_CIBLE | CIBLE_NIVEAU |
|---------------|------|-------------|--------------|
| Q1–Q2 | IF | 8 | N1 |
| Q3–Q5 | IF | 12 | N1 |
| Q6–Q15 | QV | 15 | N2 |
| Q16–Q20 | QV | 15 | N3 |

Total : 277 ✓. Remplace IF-SF / IF-ROT / QV.

### Décisions chantier tranchées
- D-09 : supprimer les 7 stubs B5/B6 → FACTORY_QA_RULES.md = source unique QA
- D-03 : exemples ligne-spécifiques tagués `[EXEMPLE]` dans les STD existants (pas de fichier annexe séparé)
- D-14 : refonte nomenclature IF-SF/IF-ROT/QV → IF/QV intégrée en Phase 1

### Principes intangibles
- POOL_COUNT = 20
- STOCK_CIBLE = 277 (constante applicative, hors pipeline)
- CIBLE_NIVEAU top-down : Q1-Q5=N1 / Q6-Q15=N2 / Q16-Q20=N3
- Difficulté non assignée par l'IA — héritée du pool
- 1 question tirée par pool par partie
- Tirage/rotation = préoccupation applicative, hors pipeline

---

## PLANIFICATION — 4 PHASES

### Phase 1 — Conflits bloquants (démarrer ici)
- D-14 : remplacer IF-SF/IF-ROT/QV → IF/QV dans tous les fichiers
- D-01 : archiver STD_A4_pool_format/workflow (V1). Réécrire STD_GLOBAL_factory_arborescence en V2
- D-02 : unifier seuil longueur question (3 valeurs → 1)
- D-03 : paramétrer valeurs hardcodées, tagger exemples `[EXEMPLE]`

### Phase 2 — Redites
- D-04 : supprimer MDE_BIB_USAGE (doublon STD_BIB_USAGE)
- D-05 : 8 filtres rédaction → source unique STD_B2_generation_rules
- D-06 : distribution N1/N2/N3 → source unique STD_GLOBAL_quiz_architecture_rules
- D-07 : anti-collision → source unique STD_GLOBAL_pool_collision_rules

### Phase 3 — Stubs et corrections structurelles
- D-08 : documenter logique 30/40/30 distracteurs vs 25/50/25 pools
- D-09 : supprimer 7 stubs B5/B6
- D-10 : corriger référence morte STD_ASM → QUIZ_ASSEMBLY_RULES
- D-11 : ajouter SOMMAIRE aux 8 feuilles canoniques
- D-12 : nom unique FICHE_VEILLE (remplace FICHE_MONITORING)
- D-16 : retirer FICHIERS_REFERENCE de STD_GLOBAL_factory_arborescence

### Phase 4 — Clarifications éditoriales
- D-13 : renommer METHODES/A2/ → METHODES/_A2/
- D-15 : note stocks 8/12/15 dans HIERARCHIE_REGLEMENTAIRE

---

## PROMPT DE REPRISE

```
REPRISE CHANTIER MDE STD

Contexte :
- Audit MDE + STD complet réalisé en session précédente
- 16 difficultés identifiées, 4 phases planifiées
- Toutes les décisions humaines sont tranchées
- Sauvegardes STD et MDE originaux conservées hors accès IA
- Aucun fichier modifié à ce stade

Document de référence :
_FACTORY/CHANTIER MDE STD/CHANTIER_MDE_STD.md (Version 1.1)

Lire ce document avant toute action.
Lire ensuite les fichiers concernés par la phase demandée.
Attendre instruction humaine avant de démarrer.

Ne pas lancer la Phase 1 automatiquement.
Ne pas scanner MAYENNE ou les lignes de production.
Scope strict : METHODES + STANDARDS uniquement.
```

---

*SESSION_RESUME_CHANTIER_MDE_STD.md — 2026-05-22*
