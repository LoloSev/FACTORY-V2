# STANDARD — FACTORY ARBORESCENCE RULES

VERSION: 2.0
DATE: 2026-05-22
STATUS: ACTIVE_REFERENCE
DOC_ROLE:
RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_001
- NAMING_CONVENTION
- MIGRATION_REFERENCE
IA_COMPATIBLE: TRUE
IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE

DEPENDENCY:
- MASTER_ARCHITECTURE.md
- _STANDARDS/_GLOBAL/glossaire_documentaire_factory.md

REPLACES: v1.1 (2026-05-14) — structure V1 avec A5_TABLEUR, B4_IMPLANTATION, B6_REGLES

---

## ARBORESCENCE V2

Artefact central par ligne : **QUIZ_[THEME].xlsx** — enrichi progressivement à chaque étape.

```txt
_FACTORY/_LIGNES/
│
├── _TEMPLATE/
│   │
│   ├── A2_APPRO/
│   │   ├── A2_BIB_[THEME]_01.txt
│   │   ├── A2_01_APPRO_LOG.md
│   │   └── A2_02_APPRO_STATS.md
│   │
│   ├── A3_TRAITEMENT/
│   │   └── A3_01_PROCESS_BIB_[THEME].md
│   │
│   ├── A4_POOLS/
│   │   └── (feuille POOLS dans QUIZ_[THEME].xlsx — pas de fichier .txt séparé)
│   │
│   ├── B2_GENERATION/
│   │   └── (feuille QUESTIONS dans QUIZ_[THEME].xlsx)
│   │
│   ├── B3_DISTRACTEURS/
│   │   └── (feuille DISTRACTEURS dans QUIZ_[THEME].xlsx)
│   │
│   ├── B5_AUDIT/
│   │   └── (feuille QA dans QUIZ_[THEME].xlsx)
│   │
│   └── EXPORT/
│       └── QUIZ_[THEME]_EXPORT.xlsx
│
├── _[LIGNE]/
│   ├── A2_APPRO/
│   ├── A3_TRAITEMENT/
│   ├── A4_POOLS/
│   ├── B2_GENERATION/
│   ├── B3_DISTRACTEURS/
│   ├── B5_AUDIT/
│   └── EXPORT/
```

---

## SECTION — DOSSIERS_PHASES

Arborescence officielle des dossiers de phase (V2).

DOSSIERS:
```txt
A2_APPRO/
A3_TRAITEMENT/
A4_POOLS/
B2_GENERATION/
B3_DISTRACTEURS/
B5_AUDIT/
EXPORT/
```

Phases supprimées en V2 (V1 uniquement) :
```txt
A1_THEME/        ← optionnel, non normé
A5_TABLEUR/      ← supprimé — xlsx créé dès A3
B4_IMPLANTATION/ ← supprimé — intégration directe dans xlsx
B6_REGLES/       ← supprimé — règles dans STD_GLOBAL
```

---

## SECTION — ARTEFACT_CENTRAL

[DEF-XLSX-001]
QUIZ_[THEME].xlsx :
Artefact unique et progressif par ligne. Produit en A3, enrichi jusqu'à EXPORT.

FEUILLES (8 au total) :
```txt
CONFIG
ITEMS
ANGLES
POOLS
QUESTIONS
DISTRACTEURS
QA
SOMMAIRE
```

[RULE-XLSX-001]
Un seul xlsx par ligne. Pas de fichiers intermédiaires .txt pour les pools ou questions.
Exception : BIB (A2) reste en .txt pour volumétrie et lisibilité.

---

## SECTION — NAMING_CONVENTION

## RULE_NAMING_PATTERN

[RULE-NAM-001]
Tout fichier doit porter le préfixe de sa phase en position 1.

FORMAT:
```txt
[PHASE]_...
```

PHASES_AUTORISEES (V2) :
- A2
- A3
- B2
- B3
- B5
- EXPORT

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
- A2_01_APPRO_LOG.md

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
- A2_BIB_[THEME]_01.txt
- A2_BIB_[THEME]_02.txt
- QUIZ_[THEME]_EXPORT.xlsx

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
WIP     ← sous audit B5
EXPORT  ← livrable validé — immuable
```

[RULE-NAM-004]
Le suffixe EXPORT interdit toute modification ultérieure du fichier.

[RULE-NAM-005]
Le suffixe WIP indique un fichier en cours de validation humaine.

---

## CHRONOLOGIE_XLSX (V2)

```txt
QUIZ_[THEME].xlsx créé en A3 (structure initiale)
        ↓
A4 : feuilles POOLS + ANGLES peuplées
        ↓
B2 : feuille QUESTIONS peuplée
        ↓
B3 : feuille DISTRACTEURS peuplée
        ↓
B5 : feuille QA peuplée + SOMMAIRE calculé
        ↓
EXPORT : QUIZ_[THEME]_EXPORT.xlsx — livrable immuable
```

---

*STD_GLOBAL_factory_arborescence_rules.md*
*Version 2.0 — 2026-05-22 — Pipeline V2*
*Remplace : v1.1 (arborescence V1 avec A5/B4/B6/IF_SF/IF_ROT subdirs)*
