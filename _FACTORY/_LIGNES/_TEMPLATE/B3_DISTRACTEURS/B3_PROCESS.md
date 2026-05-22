# B3_PROCESS — TEMPLATE

STATUS: ACTIVE
MODE: MACHINE_FIRST

PURPOSE:
Generate exactly 3 distractors per question. Populate DISTRACTEURS sheet.

---

INPUT:
- QUIZ_[THEME].xlsx
- QUESTIONS sheet validated (B2 gate passed)
- STD_B3_distractor_rules.md
- CIBLE_NIVEAU inherited per question

---

PROCESS:
1. generate distractor candidates by TYPE_Q
2. filter format, collisions, distance target
3. select exactly 3 distractors
4. compute NIVEAU_CONFIRMÉ and ÉCART_CIBLE
5. audit batch before gate

---

OUTPUT:
- DISTRACTEURS sheet populated
- STATUT_B3 ∈ {PASS|WARNING|FAIL}
- FLAGS sheet updated

---

ACCEPTANCE_CRITERIA:
- DISTRACTOR_COUNT_PER_Q = 3
- EMPTY_DISTRACTOR_COUNT = 0
- DUPLICATE_WITHIN_Q_COUNT = 0
- HARD_COLLISION_COUNT = 0
- FORMAT_MATCH_RATE >= 99%
- REUSE_RATE < 5%
- ECART_CIBLE_OK_RATE = 100%

---

FAILURE_CASES:
- fewer or more than 3 distractors per question
- distractor equals correct answer
- duplicate distractor within same question
- format mismatch above threshold
- ÉCART_CIBLE not resolved before GO
