# MDE B5 — AUDIT QA

VERSION: 2.0 (PIPELINE V2)
DATE: 2026-05-18
STATUS: ACTIVE_REFERENCE
PIPELINE_SCOPE: B5
IA_COMPATIBLE: TRUE
IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE

DEPENDENCY:
- PIPELINE_V2.md
- QUIZ_[THEME].xlsx (feuilles QUESTIONS + DISTRACTEURS validées)
- STD_B2_recevabilite_pedagogique.md
- STD_OBSOLESCENCE_WATCH_RULES.md
- STD_B3_distractor_rules.md

---

## MACHINE-FIRST EXECUTION CONTRACT

INPUT:
- QUIZ_[THEME].xlsx complet
- QUESTIONS validées
- DISTRACTEURS validés avec DECISION_GATE = GO

PROCESS:
1. présenter une question à la fois
2. appliquer VALIDATIONS QA calculables
3. écrire décision et QA_STATUS immédiatement
4. bloquer export si FAIL existe
5. produire FICHE_MONITORING depuis flags VEILLE

OUTPUT:
- feuille QA peuplée
- FICHE_MONITORING produite
- export autorisé uniquement si BLOCK_EXPORT = FALSE

ACCEPTANCE_CRITERIA:
- QA_ROW_PER_Q_RATE = 100%
- QA_STATUS ∈ {PASS, WARNING, FAIL}
- DECISION ∈ {CONSERVER, MODIFIER, REJETER, DÉPLACER}
- FAIL_COUNT = 0 before export
- QUESTIONS_WITH_VEILLE_MARKER_LISTED_RATE = 100%
- ECART_CIBLE_NOT_OK_FLAGGED_RATE = 100%
- NOTES_WORD_COUNT_MAX = 20
- BLOCK_EXPORT = TRUE if FAIL_COUNT >= 1

FAILURE_CASES:
- missing QA row
- invalid QA_STATUS or DECISION
- FAIL present at export
- VEILLE marker not listed
- untracked modification

---
## OBJECTIF

Audit HUMAN_GATE final question par question.
Peupler la feuille QA du xlsx.
Produire la FICHE_MONITORING avant export.

---

## ENTRÉE / SORTIE

| | |
|---|---|
| FROM | B3 — feuille DISTRACTEURS validée (DECISION_GATE = GO) |
| INPUT | QUIZ_[THEME].xlsx complet (CONFIG + ITEMS + ANGLES + POOLS + QUESTIONS + DISTRACTEURS) |
| OUTPUT | feuille QA peuplée + FICHE_MONITORING |
| HUMAN_VALIDATION | required; one QA row per question |
| BLOCK_EXPORT | QA_STATUS = FAIL sur ≥1 question |

---

## PRINCIPE

Une question à la fois. Décision humaine avant de passer à la suivante.
Mise à jour feuille QA immédiate à chaque décision.

---

## FORMAT DE PRÉSENTATION (obligatoire)

```
Q_ID      : [identifiant]
Pool      : [POOL_ID] — [THEME_LABEL]
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

---

## LES 4 DÉCISIONS

### CONSERVER
- QA_STATUS = PASS
- Passer à la question suivante

### MODIFIER
- Préciser : formulation / distracteur / niveau
- Appliquer correction
- Repasser checklist 8 filtres (RULE-B2-HB-002) si formulation modifiée
- QA_STATUS = PASS après correction validée

### REJETER
- QA_STATUS = FAIL
RETEX_REF: RETEX_MDE_B5_AUDIT_001
- Bloque l'export si non remplacée

### DÉPLACER
- Préciser le pool cible
- Mettre à jour POOL_ID dans feuille QUESTIONS
- QA_STATUS = PASS dans nouveau pool (si compatible)
- Note dans feuille QA : "DÉPLACÉ depuis [pool source]"

---

## COLONNES FEUILLE QA À REMPLIR

| Colonne | Valeur |
|---------|--------|
| Q_ID | référence |
| QA_STATUS | PASS / WARNING / FAIL |
| FLAGS | liste : VEILLE / IRRECEVABLE / COLLISION / FORMAT / ÉCART_CIBLE |
| DÉCISION | CONSERVER / MODIFIER / REJETER / DÉPLACER |
| NOTES | commentaire auditeur (bref) |

---

## CRITÈRES D'ÉVALUATION

- LIBELLE_WORD_COUNT <= 10 sauf JUSTIFICATION_FLAG
- Absence d'ambiguïté de réponse
- DISTRACTOR_COUNT_PER_Q = 3 ; DUPLICATE_WITHIN_Q_COUNT = 0 ; FORMAT_MATCH_RATE >= 99%
- CIBLE_NIVEAU respecté (ÉCART_CIBLE = OK)
- Recevabilité pédagogique (4 types — STD_B2_recevabilite_pedagogique.md)
- Absence de collision avec les autres questions du pool
- CIBLE_NIVEAU_POSITION_MATCH = TRUE

---

## CONTRÔLES SPÉCIFIQUES B5

### Recevabilité pédagogique
Pour chaque question, VALIDER les 4 types :
- TYPE-PED-1 : réponse révélée dans le libellé ?
- TYPE-PED-2 : déductible sans connaissance ?
- TYPE-PED-3 : connaissance triviale ?
- TYPE-PED-4 : ambiguïté de réponse ?

Si OUI → FLAG IRRECEVABLE + TYPE-PED-[N] dans feuille QA → MODIFIER ou REJETER

### Veille obsolescence
Détecter les marqueurs de risque (RULE-OBS-008) :
"dernier", "jamais", "seul", "record", "plus grand/récent/de X", tout superlatif absolu

Si détecté → FLAG VEILLE + TYPE-[1/2/3/4/5] dans feuille QA → QA_STATUS = WARNING (pas bloquant)

---

## PRODUCTION FICHE_MONITORING

En fin d'audit B5, produire la FICHE_MONITORING (RULE-OBS-010) :

```
QUIZ_ID: [identifiant]
DATE_PRODUCTION: [date]
DATE_VALIDITE: [date ou "indéfinie"]
THEME: [thème]

QUESTIONS_A_RISQUE:
  - Q_ID / POOL / RISQUE TYPE-[N] / MARQUEUR / NOTE

DECLENCHEURS_SURVEILLES:
  - [événements à monitorer]

RESPONSABLE_MAJ: [à définir]
```

La FICHE_MONITORING est conservée avec le quiz. Elle ne bloque pas l'export.

---

## BLOCAGES EXPORT

Export impossible si :
- [ ] QA_STATUS = FAIL sur ≥1 question non remplacée
- [ ] ÉCART_CIBLE ≠ OK non résolu sur ≥1 question
- [ ] FICHE_MONITORING absente
- [ ] STOCK_ACTUEL < STOCK_CIBLE sur ≥1 pool (feuille SOMMAIRE)

---

## WORKFLOW RÉSUMÉ

```
Question présentée (format standardisé)
    ↓
VALIDATIONS : recevabilité pédagogique + veille + distracteurs + niveau
    ↓
Décision humaine : CONSERVER / MODIFIER / REJETER / DÉPLACER
    ↓
Mise à jour feuille QA immédiate
    ↓
Question suivante
    ↓ (fin du stock)
Production FICHE_MONITORING
    ↓
Vérification blocages export
    ↓
EXPORT
```

---

*MDE_B5_audit.md*
*Version 2.0 — 2026-05-18 — Pipeline V2*
*Remplace : v1.0 (CSV + [POOL]_LISIBLE.md)*


