# B2_PROCESS — TEMPLATE

STATUS: ACTIVE
MODE: MACHINE_FIRST

PURPOSE:
Generate questions pool by pool from ANGLES. Populate QUESTIONS sheet.

---

INPUT:
- QUIZ_[THEME].xlsx
- POOLS sheet validated (A4 gate passed)
- ANGLES sheet (POOL_CIBLE renseigné)
- STD_B2_generation_rules.md
- STD_B2_recevabilite_pedagogique.md

---

PROCESS:
1. process one pool at a time
2. select DISPONIBLE angles for pool
3. apply hard blockers before writing
4. generate questions at inherited CIBLE_NIVEAU
5. write only PASS questions

---

OUTPUT:
- QUESTIONS sheet populated
- STATUT_B2 ∈ {DRAFT|READY_B3|REWRITE}
- blocking flags explicit

---

ACCEPTANCE_CRITERIA:
- QUESTIONS_WITH_Q_ID_RATE = 100%
- QUESTIONS_WITH_POOL_ID_RATE = 100%
- QUESTIONS_WITH_ANGLE_ID_RATE = 100%
- CIBLE_NIVEAU_POOL_MATCH_RATE = 100%
- LIBELLE_WORD_COUNT_MAX = 15
- ANSWER_UNIQUE_RATE = 100%
- PED_BLOCKER_COUNT = 0
- HARD_COLLISION_COUNT = 0

---

FAILURE_CASES:
- missing CIBLE_NIVEAU
- question without ANGLE_ID
- CIBLE_NIVEAU edited manually
- WORD_COUNT >= 16
