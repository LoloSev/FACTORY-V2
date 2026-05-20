---
name: factory-conductor
description: Chef d'orchestre FACTORY — reprend le projet en main à chaque session. Lit l'état réel du projet, identifie le blocage critique, propose et exécute la prochaine action. Invoquer en début de session ou quand le projet est à l'arrêt.
version: 1.0
status: ACTIVE
---

# FACTORY CONDUCTOR

**Rôle:** Lire → Évaluer → Décider → Agir
**Quand invoquer:** Début de session, reprise après pause, blocage non résolu

---

## PHASE 0 — BOOT (obligatoire, automatique)

À chaque invocation, lire dans l'ordre:

```
1. _FACTORY/_DOCS/MASTER_ARCHITECTURE.md         → contexte projet + phases
2. _FACTORY/_STANDARDS/SCHEMA_LEGISLATIF_FACTORY_v1.md  → règles actives
3. _FACTORY/_DOCS/MASTER_ARCHITECTURE.md §PRIORITÉ ABSOLUE    → directives en cours
4. Pour chaque _LIGNE active: lister fichiers existants → état réel
```

**Lignes actives à scanner:**
```
_FACTORY/_LIGNES/_CDM/
_FACTORY/_LIGNES/_MAYENNE/
_FACTORY/_LIGNES/_CINEMA/
_FACTORY/_LIGNES/_ROCK/      (si démarré)
_FACTORY/_LIGNES/_RAP/       (si démarré)
```

**Mapping phase → preuve d'existence:**
```
A1 = A1_THEME/ non vide
A2 = A2_APPRO/A2_BIB_[THEME]_01.txt
A3 = A3_TRAITEMENT/A3_BIPREGEN_[THEME].txt
A4 = A4_POOLS/A4_POOLS_[THEME].txt
A5 = A5_TABLEUR/A5_TABLEUR_[THEME]_INIT.xlsx
B2 = B2_GENERATION/ non vide
B3 = B3_DISTRACTEURS/PASS_2_AUDIT/ non vide (PASS1+2 complets)
B4 = B4_IMPLANTATION/B4_TABLEUR_[THEME]_v1.xlsx
B5 = B5_AUDIT/B5_TABLEUR_[THEME]_WIP.xlsx
B6 = B6_REGLES/B6_01_RULES_EXTRACTED.md
EXPORT = EXPORT/EXPORT_[THEME]_FINAL.xlsx
```

---

## PHASE 1 — DIAGNOSTIC

Après scan, produire ce tableau:

```
ÉTAT PROJET — [DATE]
═══════════════════════════════════════════════
QUIZ     │ A1 A2 A3 A4 A5 B2 B3 B4 B5 B6 EXP
─────────┼──────────────────────────────────────
CDM      │ ✅ ✅ ✅ ✅ ✅ ✅ ⛔  ❌  ❌  ❌  ❌
MAYENNE  │ ❌  ✅ ❌  ❌  ❌  ✅ ❌  ❌  ⚠️  ❌  ❌
CINEMA   │ ❌  ✅ ❌  ❌  ❌  ❌  ❌  ❌  ❌  ❌  ❌
ROCK     │ ❌  ❌  ❌  ❌  ❌  ❌  ❌  ❌  ❌  ❌  ❌
RAP      │ ❌  ❌  ❌  ❌  ❌  ❌  ❌  ❌  ❌  ❌  ❌
═══════════════════════════════════════════════
Légende: ✅ FAIT │ ⚠️ EN COURS │ ⛔ BLOQUÉ │ ❌ PAS DÉMARRÉ
```

Puis lister BLOCAGES ACTIFS:
```
BLOCAGES
─────────────────────────────────────────────
[B01] CDM B3 PASS3 — 4 trous systémiques (voir MASTER_ARCHITECTURE §ALERTE)
[B02] FACTORY — STD_B2_generation_rules.md absent (R03/R07 non formalisés)
[B03] FACTORY — STD_B2_recevabilite_pedagogique.md absent (LACUNE L01)
[B04] MAYENNE — phases A3/A4/A5 manquantes entre A2 et B2
```

---

## PHASE 2 — DÉCISION

### Règle de priorité conductor:

```
SI PRIORITÉ ABSOLUE active dans MASTER_ARCHITECTURE
  → Exécuter ses missions dans l'ordre indiqué
SINON SI blocage FACTORY (règle manquante bloque plusieurs lignes)
  → Créer/compléter le STD manquant en premier
SINON
  → Choisir la ligne la plus avancée, prochaine phase non bloquée
  → Préférer: ligne proche de EXPORT > ligne en cours > nouvelle ligne
```

### Output décision:

```
DÉCISION
─────────────────────────────────────────────
ACTION PRIORITAIRE: [titre]
LIGNE: [CDM / MAYENNE / CINEMA / ...]
PHASE: [B3 PASS3 / A3 / ...]
RAISON: [pourquoi cette action avant les autres]
PRÉREQUIS: [ce dont j'ai besoin pour commencer]
DURÉE ESTIMÉE: [X tokens / X interactions]
```

---

## PHASE 3 — EXÉCUTION

Avant d'agir:
1. Confirmer avec Laurent si action > 30 min estimée
2. Lire le MDE correspondant à la phase (`METHODES/MDE_[PHASE].md`)
3. Lire les STD applicables (`_STANDARDS/STD_[PHASE]_*.md`)
4. Exécuter pool par pool / étape par étape — jamais globalement
5. Créer les fichiers de log requis (`B3_01_DISTRACTEUR_LOG.md`, etc.)

### Checklist pré-action:
```
[ ] MDE de la phase lu
[ ] STD applicables lus (dont SCHEMA_LEGISLATIF_FACTORY_v1.md)
[ ] Fichier output cible identifié
[ ] Règles ABSOLU vérifiées (R03/R07 si B2, TRANS-1 si B3)
[ ] Log de traçabilité ouvert
```

---

## PHASE 4 — CLÔTURE SESSION

En fin de session ou à 15 interactions:

```
RÉSUMÉ SESSION [DATE]
─────────────────────────────────────────────
FAIT: [liste actions complétées]
EN COURS: [où on s'est arrêté, fichier exact]
BLOQUÉ: [nouveau blocage détecté?]
PROCHAIN: [première action session suivante]
ALERTE: [risque contexte / token si applicable]
```

Sauvegarder ce résumé dans:
`_FACTORY/_LIGNES/[THEME]/[PHASE]/[PHASE]_01_[TYPE]_LOG.md`

---

## RÈGLES DU CONDUCTOR

```
[COND-001] Pool par pool — jamais global
[COND-002] Validation humaine avant changement de phase
[COND-003] Lire avant d'agir (MDE + STD obligatoires)
[COND-004] Tout blocage documenté, rien gardé en mémoire implicite
[COND-005] Alerter à 15 interactions (R35 économie session)
[COND-006] Aucune règle ABSOLU ignorée même si ça ralentit
[COND-007] Si doute = documenter comme "À CLARIFIER", pas d'invention
```

---

## SKILLS DISPONIBLES (musiciens)

| Phase | Skill | Invoquer si |
|-------|-------|-------------|
| A2 | `a2-bib-construction` | Nouvelle ligne à démarrer |
| A3 | `a3-bib-processing` | BIB prête → BIPREGEN |
| A4 | `a4-pools-definition` | BIPREGEN prête → POOLS |
| B2 | `b2-questions-generator` | POOLS prêts → questions |
| B3 | `distractors-generator` | B2 complet → distracteurs |
| B3 | `distractor-audit-statistics` | PASS2 → métriques qualité |
| B3 | `distractor-optimizer` | PASS3 → optimisation |
| B4 | `b4-spreadsheet-implantation` | B3 validé → xlsx |
| B5 | `b5-audit-validator` | xlsx WIP → audit |
| B6 | `b6-rules-extractor` | B5 validé → règles |

---

*factory-conductor v1.0 — 2026-05-18*
