# A3_PROCESS — TEMPLATE

STATUS: ACTIVE
MODE: MACHINE_FIRST

PURPOSE:
Transform A2_BIB source into ITEMS + ANGLES sheets (xlsx).

---

INPUT:
- A2_BIB_[THEME].txt (archived, unmodified)
- QUIZ_[THEME].xlsx (CONFIG initialized)
- RICHESSE seuils from MDE_A3_traitement.md

---

PROCESS:
1. archive BIB source without modification
2. extract sections and items
3. assign ITEM_ID (unique, sequential)
4. classify RICHESSE {DENSE|STANDARD|LIGHT}
5. produce ITEMS sheet
6. produce ANGLES sheet with ITEM_ID linkage
7. flag FAILURE_CASES

---

OUTPUT:
- ITEMS sheet populated
- ANGLES sheet populated
- FAILURE_CASE flags explicit

---

ACCEPTANCE_CRITERIA:
- SOURCE_ARCHIVE_EXISTS = TRUE
- ITEM_ID_UNIQUE_RATE = 100%
- ITEMS_WITH_RICHESSE_RATE = 100%
- RICHESSE ∈ {DENSE, STANDARD, LIGHT}
- ANGLE_ID_UNIQUE_RATE = 100%
- ANGLES_WITH_ITEM_ID_RATE = 100%
- EXPORT_BLOCKER_COUNT = 0

---

FAILURE_CASES:
- BIB source missing or modified
- duplicate ITEM_ID or ANGLE_ID
- RICHESSE not classified
- ANGLE without ITEM_ID
