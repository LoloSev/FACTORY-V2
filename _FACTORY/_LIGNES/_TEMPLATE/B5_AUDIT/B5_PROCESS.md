# B5_PROCESS — TEMPLATE

STATUS: ACTIVE
MODE: MACHINE_FIRST

PURPOSE:
QA audit question by question. Populate QA sheet. Gate export.

---

INPUT:
- QUIZ_[THEME].xlsx complet
- QUESTIONS validated
- DISTRACTEURS validated (DECISION_GATE = GO)
- FACTORY_QA_RULES.md

---

PROCESS:
1. present one question at a time
2. apply calculable QA validations
3. write DECISION + QA_STATUS immediately
4. block export if FAIL exists
5. produce FICHE_VEILLE from VEILLE flags

---

OUTPUT:
- QA sheet populated
- FICHE_VEILLE produced
- export authorized only if BLOCK_EXPORT = FALSE

---

ACCEPTANCE_CRITERIA:
- QA_ROW_PER_Q_RATE = 100%
- QA_STATUS ∈ {PASS, WARNING, FAIL}
- DECISION ∈ {CONSERVER, MODIFIER, REJETER, DÉPLACER}
- FAIL_COUNT = 0 before export
- NOTES_WORD_COUNT_MAX = 20
- BLOCK_EXPORT = TRUE if FAIL_COUNT >= 1
- VEILLE_MARKERS_LISTED_RATE = 100%

---

FAILURE_CASES:
- missing QA row
- invalid QA_STATUS or DECISION
- FAIL present at export
- VEILLE marker not listed in FICHE_VEILLE
