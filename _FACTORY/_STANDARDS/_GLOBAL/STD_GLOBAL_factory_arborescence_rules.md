# STANDARD — FACTORY ARBORESCENCE RULES

VERSION: 1.1
DATE: 2026-05-14
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

---

RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_002

```txt
RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_003
│
├── _TEMPLATE/
│   │
│   ├── A1_THEME/
│   │   └── A1_01_THEME_CONTEXT.md
│   │
│   ├── A2_APPRO/
│   │   ├── A2_BIB_[THEME]_01.txt
│   │   ├── A2_01_APPRO_LOG.md
│   │   └── A2_02_APPRO_STATS.md
│   │
│   ├── A3_TRAITEMENT/
│   │   ├── A3_BIPREGEN_[THEME].txt
│   │   ├── A3_ANGIPREGEN_[THEME].txt
│   │   └── A3_01_PROCESS_BIB_[THEME].md
│   │
│   ├── A4_POOLS/
│   │   └── A4_POOLS_[THEME].txt
│   │
│   ├── A5_TABLEUR/
│   │   └── A5_TABLEUR_[THEME]_INIT.xlsx
│   │
│   ├── B2_GENERATION/
│   │   ├── IF_SF/
│   │   ├── IF_ROT/
│   │   ├── QV/
│   │   └── B2_01_GENERATION_LOG.md
│   │
│   ├── B3_DISTRACTEURS/
│   │   ├── IF_SF/
│   │   ├── IF_ROT/
│   │   ├── QV/
│   │   └── B3_01_DISTRACTEUR_LOG.md
│   │
│   ├── B4_IMPLANTATION/
│   │   ├── B4_TABLEUR_[THEME]_v1.xlsx
│   │   ├── B4_TABLEUR_[THEME]_v2.xlsx
│   │   ├── B4_01_IMPORT_LOG.md
│   │   └── B4_02_EXPORT_CHECK.md
│   │
│   ├── B5_AUDIT/
│   │   ├── B5_TABLEUR_[THEME]_WIP.xlsx
│   │   ├── B5_01_AUDIT_LOG.md
│   │   ├── B5_02_FIX_LOG.md
│   │   └── B5_03_QA_REPORT.md
│   │
│   ├── B6_REGLES/
│   │   ├── B6_01_RULES_EXTRACTED.md
│   │   ├── B6_02_EDGE_CASES.md
│   │   └── B6_03_THEME_RULES_[THEME].md
│   │
│   └── EXPORT/
│       └── EXPORT_[THEME]_FINAL.xlsx
│
├── _MAYENNE/                        ← process en cours : B5
│   ├── A1_THEME/
│   ├── A2_APPRO/
│   │   ├── A2_BIB_MAYENNE_01.txt
│   │   ├── A2_01_APPRO_LOG.md
│   │   └── A2_02_APPRO_STATS.md
│   ├── A3_TRAITEMENT/
│   ├── A4_POOLS/
│   ├── A5_TABLEUR/
│   ├── B2_GENERATION/
│   ├── B3_DISTRACTEURS/
│   ├── B4_IMPLANTATION/
│   ├── B5_AUDIT/
│   │   ├── B5_TABLEUR_MAYENNE_WIP.xlsx
│   │   ├── B5_01_AUDIT_LOG.md
│   │   ├── B5_02_FIX_LOG.md
│   │   └── B5_03_QA_REPORT.md
│   ├── B6_REGLES/
│   └── EXPORT/
│
RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_004
│   ├── A1_THEME/
│   ├── A2_APPRO/
RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_005
│   ├── A3_TRAITEMENT/
RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_006
RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_007
RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_008
│   ├── A4_POOLS/
RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_009
│   ├── A5_TABLEUR/
RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_010
│   ├── B2_GENERATION/
│   ├── B3_DISTRACTEURS/
│   ├── B4_IMPLANTATION/
│   ├── B5_AUDIT/
│   ├── B6_REGLES/
│   └── EXPORT/
│
├── _CINEMA/                         ← process en cours : A2
│   ├── A1_THEME/
│   ├── A2_APPRO/
│   │   ├── A2_BIB_CINEMA_01.txt
│   │   ├── A2_BIB_CINEMA_02.txt
│   │   ├── A2_BIB_CINEMA_03.txt
│   │   ├── A2_01_APPRO_LOG.md
│   │   └── A2_02_APPRO_STATS.md
│   ├── A3_TRAITEMENT/
│   ├── A4_POOLS/
│   ├── A5_TABLEUR/
│   ├── B2_GENERATION/
│   ├── B3_DISTRACTEURS/
│   ├── B4_IMPLANTATION/
│   ├── B5_AUDIT/
│   ├── B6_REGLES/
│   └── EXPORT/
│
├── _ROCK/
├── _RAP/
├── _INTERNET/
└── _SERIES/
```

---

# SECTION — DOSSIERS_PHASES

Arborescence officielle des dossiers de phase.

DOSSIERS:
```txt
A1_THEME/
A2_APPRO/
A3_TRAITEMENT/
A4_POOLS/
A5_TABLEUR/
B2_GENERATION/
B3_DISTRACTEURS/
B4_IMPLANTATION/
B5_AUDIT/
B6_REGLES/
EXPORT/
```

---

# SECTION — FICHIERS_REFERENCE

## _MAYENNE

```txt
A2_APPRO/A2_BIB_MAYENNE_01.txt
B2_GENERATION/B2_QUESTIONS_MAYENNE_BRUTES.txt
B5_AUDIT/B5_TABLEUR_MAYENNE_WIP.xlsx
```

NOTE:
quiz_mayenne_integral.xlsx est represente en B5_AUDIT car le process Mayenne est en cours a cette phase.
Il passera en EXPORT/EXPORT_MAYENNE_FINAL.xlsx a validation complete.

---

RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_011

```txt
RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_012
RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_013
RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_014
RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_015
RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_016
RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_017
```

---

## _CINEMA

```txt
A2_APPRO/A2_BIB_CINEMA_01.txt
A2_APPRO/A2_BIB_CINEMA_02.txt
A2_APPRO/A2_BIB_CINEMA_03.txt
A2_APPRO/A2_01_APPRO_LOG.md
A2_APPRO/A2_02_APPRO_STATS.md
```

---

# SECTION — NAMING_CONVENTION

## RULE_NAMING_PATTERN

[RULE-NAM-001]
Tout fichier doit porter le préfixe de sa phase en position 1.

FORMAT:
```txt
[PHASE]_...
```

PHASES_AUTORISEES:
- A1
- A2
- A3
- A4
- A5
- B2
- B3
- B4
- B5
- B6
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
- B5_02_FIX_LOG.md
- B5_03_QA_REPORT.md
- A2_01_APPRO_LOG.md
- B4_01_IMPORT_LOG.md

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
- A2_BIB_CINEMA_01.txt
- A2_BIB_CINEMA_02.txt
- A2_BIB_CINEMA_03.txt
RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_018
RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_019
- B5_TABLEUR_MAYENNE_WIP.xlsx
RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_020
RETEX_REF: RETEX_STD_GLOBAL_FACTORY_ARBORESCENCE_RULES_021

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
INIT    ← structure vide, produit de A5
v[N]    ← version de travail B4 (v1, v2...)
WIP     ← sous audit B5
FINAL   ← livrable validé EXPORT — immuable
```

[RULE-NAM-004]
Le suffixe FINAL interdit toute modification ultérieure du fichier.

[RULE-NAM-005]
Le suffixe WIP indique un fichier en cours de validation humaine.

---

## CHRONOLOGIE_XLSX

```txt
A5_TABLEUR_[THEME]_INIT.xlsx      ← structure vide
        ↓
B4_TABLEUR_[THEME]_v1.xlsx        ← implantation
B4_TABLEUR_[THEME]_v2.xlsx        ← itération si nécessaire
        ↓
B5_TABLEUR_[THEME]_WIP.xlsx       ← sous audit
        ↓
EXPORT_[THEME]_FINAL.xlsx         ← livrable immuable
```

---

# SECTION — GLOSSAIRE_ADDITIONS

Blocs à ajouter dans :
DEPENDENCY:
- _STANDARDS/_GLOBAL/glossaire_documentaire_factory.md

---

# SECTION — GLOSSAIRE_ADDITIONS — NAMING_PATTERN_PROCESS_DOC

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

# SECTION — GLOSSAIRE_ADDITIONS — NAMING_PATTERN_ARTIFACT

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

# SECTION — GLOSSAIRE_ADDITIONS — SUFFIXES_ETAT_XLSX

[DEF-SUFFIX-001]
SUFFIXES_ETAT_XLSX:
Indicateurs d'état du fichier tableur tout au long du pipeline.

VALEURS:
- INIT  : structure vide, sortie de A5
- v[N]  : version de travail, phase B4
- WIP   : en cours d'audit, phase B5
- FINAL : livrable validé, EXPORT — immuable

[RULE-SUFFIX-001]
Tout fichier xlsx doit porter un suffixe d'état.

[RULE-SUFFIX-002]
FINAL interdit toute modification ultérieure.


