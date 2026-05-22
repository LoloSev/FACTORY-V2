# ACTIVE_CONTEXT_MANIFEST

DEPENDENCY:
- FACTORY_RUNTIME_LEXICON.md
- TOKEN_ECONOMY_RUNTIME_PROTOCOL.md
- MASTER_ARCHITECTURE.md
- PIPELINE_V2.md
- glossaire_documentaire_factory.md
## Chargement par défaut

Charger uniquement :
- STD/MDE nécessaires à la phase en cours
- règles globales minimales
- dépendances explicitement citées

Ne pas charger par défaut :
- RETEX_INDEX
- archives
- retours historiques
- fichiers de laboratoire

## Règle

Le RETEX est consulté uniquement en contexte :
- audit
- amélioration
- anti-régression
- résolution d'ambiguïté


---

# PHASE_3_COMPRESSION_RULES

STATUS: ACTIVE

RUNTIME_LOAD_POLICY:
- LOAD: target MDE/STD
- LOAD: direct DEPENDENCY only
- DO_NOT_LOAD_DEFAULT: RETEX_LIBRARY
- DO_NOT_LOAD_DEFAULT: ARCHIVES_TESTS
- DO_NOT_LOAD_DEFAULT: _LIGNES production outputs
- DO_NOT_LOAD_DEFAULT: historical reports

ACTIVE_CONTEXT_COST_RULE:
- duplicate validation block must resolve to referenced DEPENDENCY
- repeated glossary term must resolve to glossaire_documentaire_factory.md
- repeated QA status definition must resolve to STD_QA_status_rules.md
- repeated B5 QA validation must resolve to STD_B5_factory_quality_rules.md
- BIB positioning must resolve to STD_BIB_USAGE.md (do not redefine inline)
- BIB operational usage must resolve to MDE_BIB_USAGE.md (do not redefine inline)

ACCEPTANCE_CRITERIA:
- each active STD/MDE/DOC has explicit DEPENDENCY block
- RETEX loading remains ON_DEMAND_ONLY
- no active file deletion during compression
- ZIP file count >= Phase 2 file count

## TOKEN_ECONOMY_LOAD_POLICY

LOAD FIRST:
- `_FACTORY/_STANDARDS/_GLOBAL/FACTORY_RUNTIME_LEXICON.md`

LOAD WHEN STRUCTURING/MIGRATING:
- `_FACTORY/_STANDARDS/_GLOBAL/TOKEN_ECONOMY_RUNTIME_PROTOCOL.md`

DO_NOT_DUPLICATE:
- taxonomies runtime
- statuts machine
- concepts gameplay transversaux

MAYENNE_STATUS:
- prototype de refonte FACTORY
- ne pas généraliser aux autres lignes avant validation
