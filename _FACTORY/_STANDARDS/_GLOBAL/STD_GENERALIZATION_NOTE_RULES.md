# STANDARD - GENERALIZATION NOTE RULES

VERSION: 1.0
STATUS: ACTIVE_REFERENCE
PIPELINE_SCOPE: B6_GLOBAL
IA_COMPATIBLE: TRUE
IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE

DEPENDENCY:
- MASTER_ARCHITECTURE.md
- glossaire_documentaire_factory.md
---

# SECTION - GENERALIZATION_NOTES

[DEF-GNOTE-001]
Une `GENERALIZATION_NOTE` capture un apprentissage issu d'un cas reel de production avant toute generalisation large.

[RULE-GNOTE-001]
Une observation locale ne devient pas automatiquement une regle Factory.

[RULE-GNOTE-002]
Statuts autorises :
- `CANDIDATE`
- `CONFIRMED_THEME`
- `CROSS_THEME_VALIDATED`
- `REJECTED`

[RULE-GNOTE-003]
Une note peut passer en standard Factory seulement si :
- elle resout un probleme reel observe
- elle ne duplique pas un standard existant
- elle reste exploitable operationnellement
- elle est confirmee au minimum sur un autre contexte ou justifiee comme principe transversal evident

[RULE-GNOTE-004]
Les notes rejetees ou fragiles doivent etre conservees tant qu'elles documentent un failed pattern utile.

[RULE-GNOTE-005]
Le B6 extrait, trie et propose.
La validation humaine decide ce qui devient :
- hard blocker
- soft warning
- optimizer
- simple observation
