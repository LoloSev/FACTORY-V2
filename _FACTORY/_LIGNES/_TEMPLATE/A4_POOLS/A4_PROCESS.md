# A4_PROCESS — TEMPLATE

STATUS: ACTIVE
MODE: MACHINE_FIRST

PURPOSE:
Assign 20 pools from ITEMS + ANGLES. Populate POOLS sheet.

---

INPUT:
- QUIZ_[THEME].xlsx
- ITEMS + ANGLES sheets validated (A3 gate passed)
- positional derivation table (MDE_A4)

---

PROCESS:
1. read sections, items, angles, RICHESSE
2. assign exactly 20 pools
3. derive CIBLE_NIVEAU from POSITION_QUIZ
4. assign STOCK_CIBLE {8|12|15} by pool type/position
5. link angles to pools (POOL_CIBLE)
6. validate stocks and collisions

---

OUTPUT:
- POOLS sheet populated
- ANGLES sheet updated (POOL_CIBLE + STATUT)
- SOMMAIRE sheet calculated

---

ACCEPTANCE_CRITERIA:
- POOL_COUNT = 20
- IF_COUNT = 5
- QV_COUNT = 15
- POSITION_QUIZ_UNIQUE_RATE = 100%
- CIBLE_NIVEAU_POSITION_MATCH_RATE = 100%
- STOCK_CIBLE ∈ {8, 12, 15}
- POOLS_WITH_ASSIGNED_ANGLES_RATE = 100%
- HARD_COLLISION_COUNT = 0
- EXPORT_BLOCKER_COUNT = 0

---

FAILURE_CASES:
- pool count != 20
- duplicate POSITION_QUIZ
- CIBLE_NIVEAU not derived from POSITION_QUIZ
- pool without assigned angle
- STOCK_CIBLE out of {8, 12, 15}
