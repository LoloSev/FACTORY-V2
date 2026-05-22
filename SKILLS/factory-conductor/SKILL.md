---
name: factory-conductor
description: Chef d'orchestre FACTORY — reprend le projet en main à chaque session. Lit l'état réel du projet, identifie le blocage critique, propose et exécute la prochaine action. Invoquer en début de session ou quand le projet est à l'arrêt.
version: 2.0
status: ACTIVE
---

# FACTORY CONDUCTOR

**Rôle:** Lire → Évaluer → Décider → Agir
**Quand invoquer:** Début de session, reprise après pause, blocage non résolu

---

## PHASE 0 — BOOT (obligatoire, automatique)

À chaque invocation, lire dans l'ordre :

```
1. _FACTORY/_DOCS/MASTER_ARCHITECTURE.md       → contexte + constantes
2. _FACTORY/_DOCS/PIPELINE_V2.md               → pipeline actif
3. _FACTORY/_STATE/DASHBOARD_STATE.json        → état courant par ligne
```

**Lignes à scanner :**
```
_FACTORY/_LIGNES/_CDM/
_FACTORY/_LIGNES/_MAYENNE/
_FACTORY/_LIGNES/_CINEMA/
_FACTORY/_LIGNES/_RAP/      (si démarré)
```

**Mapping phase → preuve d'existence (V2) :**
```
A2 = A2_APPRO/A2_BIB_[THEME]_01.txt
A3 = A3_TRAITEMENT/A3_01_PROCESS_BIB_[THEME].md
A4 = A4_POOLS/ dans QUIZ_[THEME].xlsx (feuille POOLS peuplée)
B2 = B2_GENERATION/ dans QUIZ_[THEME].xlsx (feuille QUESTIONS peuplée)
B3 = B3_DISTRACTEURS/ dans QUIZ_[THEME].xlsx (feuille DISTRACTEURS peuplée)
B5 = B5_AUDIT/ dans QUIZ_[THEME].xlsx (feuille QA peuplée)
EXPORT = EXPORT/QUIZ_[THEME]_EXPORT.xlsx
```

---

## PHASE 1 — DIAGNOSTIC

Après scan, produire ce tableau :

```
ÉTAT PROJET — [DATE]
═══════════════════════════════════════════
QUIZ     │ A2  A3  A4  B2  B3  B5  EXP
─────────┼──────────────────────────────────
CDM      │ ✅  ✅  ✅  ✅  ✅  ❌  ❌
MAYENNE  │ ✅  ✅  ✅  ⚠️  ❌  ❌  ❌
CINEMA   │ ✅  ❌  ❌  ❌  ❌  ❌  ❌
RAP      │ ⚠️  ❌  ❌  ❌  ❌  ❌  ❌
═══════════════════════════════════════════
Légende: ✅ FAIT │ ⚠️ EN COURS │ ⛔ BLOQUÉ │ ❌ PAS DÉMARRÉ
```

Puis lister BLOCAGES ACTIFS :
```
BLOCAGES
──────────────────────────────────────────
[B01] ...
```

---

## PHASE 2 — DÉCISION

### Règle de priorité :

```
SI blocage FACTORY (règle manquante bloque plusieurs lignes)
  → Créer/compléter le STD manquant en premier
SINON
  → Choisir la ligne la plus avancée, prochaine phase non bloquée
  → Préférer : ligne proche de EXPORT > ligne en cours > nouvelle ligne
```

### Output décision :

```
DÉCISION
──────────────────────────────────────────
ACTION PRIORITAIRE : [titre]
LIGNE              : [CDM / MAYENNE / ...]
PHASE              : [B3 / A4 / ...]
RAISON             : [pourquoi cette action avant les autres]
PRÉREQUIS          : [ce dont j'ai besoin pour commencer]
```

---

## PHASE 3 — EXÉCUTION

Avant d'agir :
1. Confirmer avec Laurent si action > 30 min estimée
2. Lire le MDE correspondant (`_FACTORY/METHODES/[PHASE]/MDE_[PHASE]_*.md`)
3. Lire les STD applicables (`_FACTORY/_STANDARDS/[PHASE]/STD_[PHASE]_*.md`)
4. Exécuter pool par pool / étape par étape — jamais globalement
5. Créer les fichiers de log requis

### Checklist pré-action :
```
[ ] MDE de la phase lu
[ ] STD applicables lus
[ ] Fichier output cible identifié (xlsx ou .md)
[ ] Gate précédente passée (DASHBOARD_STATE.json)
[ ] Log de traçabilité ouvert
```

---

## PHASE 4 — CLÔTURE SESSION

```
RÉSUMÉ SESSION [DATE]
──────────────────────────────────────────
FAIT    : [actions complétées]
EN COURS: [où on s'est arrêté, fichier exact]
BLOQUÉ  : [nouveau blocage détecté ?]
PROCHAIN: [première action session suivante]
```

---

## RÈGLES DU CONDUCTOR

```
[COND-001] Pool par pool — jamais global
[COND-002] Validation humaine obligatoire avant changement de phase
[COND-003] Lire MDE + STD avant d'agir
[COND-004] Tout blocage documenté — rien gardé en mémoire implicite
[COND-005] Si doute = documenter comme "À CLARIFIER", pas d'invention
```

---

## SKILLS DISPONIBLES

| Phase | Skill | Invoquer si |
|-------|-------|-------------|
| A2 | `a2-bib-construction` | Nouvelle ligne à démarrer |
| A3 | `a3-bib-processing` | BIB prête → xlsx ITEMS/ANGLES |
| A4 | `a4-pools-definition` | ITEMS/ANGLES prêts → xlsx POOLS |
| B2 | `b2-questions-generator` | POOLS prêts → xlsx QUESTIONS |
| B3 | `distractors-generator` | B2 complet → xlsx DISTRACTEURS |
| B3 | `distractor-audit-statistics` | PASS2 → métriques qualité |
| B3 | `distractor-optimizer` | PASS3 → optimisation |
| B5 | `b5-audit-validator` | xlsx complet → feuille QA |

---

*v2.0 — 2026-05-22 — Pipeline V2 (remplace v1.0 : A5/B4/B6 supprimés, BIPREGEN→xlsx, IF-SF/IF-ROT→IF/QV)*
