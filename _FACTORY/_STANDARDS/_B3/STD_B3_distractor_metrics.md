---
name: STD_B3_distractor_metrics
version: 1.0
status: ACTIVE_REFERENCE
IA_COMPATIBLE: TRUE
IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE
PIPELINE_SCOPE: B3
DEPENDENCY:
  - STD_B3_distractor_rules.md
  - STD_B6_rule_priority_matrix.md
---

# STANDARD — DISTRACTOR METRICS (B3)

Thresholds de QA_STATUS et métriques pour audit PASS 2.

---

## HARD_BLOCKERS (PASS 2 Detection)

| Métrique | Condition | Action | Severity |
|----------|-----------|--------|----------|
| Hard collisions | count > 0 | BLOCKER immédiat | CRITICAL |
| QA_STATUS | = FAIL | Bloque B4 | CRITICAL |
| Distracteur fictif | Non signalé | BLOCKER immédiat | CRITICAL |
| Format inconsistent | Dans même Q | Reformatter | HIGH |

---

## SOFT_WARNINGS (PASS 2 Detection)

| Métrique | Green | Yellow | Red | Action |
|----------|-------|--------|-----|--------|
| Format homogeneity | ≥99% | 95-99% | <95% | Flag + PASS 3 fix |
| Hard collisions | 0 | 0 | >0 | BLOCKER |
| Soft collisions | <5% | 5-10% | >10% | Flag for review |
| Difficulty distribution | ±5% | ±10% | ±15%+ | Flag + PASS 3 |

---

## DIFFICULTY DISTRIBUTION

**Target :** 25% N1 / 50% N2 / 25% N3

### Global (all [STOCK_CIBLE × 3] distractors)

| Level | Target | Green | Yellow | Red |
|-------|--------|-------|--------|-----|
| N1 | 30% | 25-35% | 20-40% | <20% or >40% |
| N2 | 40% | 35-45% | 30-50% | <30% or >50% |
| N3 | 30% | 25-35% | 20-40% | <20% or >40% |

**Calculation :**
```
TOTAL_DISTRACTORS = STOCK_CIBLE × 3
N1_COUNT = count(distractors where difficulty == N1)
N1_PERCENT = (N1_COUNT / TOTAL_DISTRACTORS) * 100
```

[EXEMPLE-METRICS-001 — cas source]
Application sur la ligne cas source (STOCK_CIBLE = 277) :
→ TOTAL_DISTRACTORS = 831 (277 × 3)

**Green decision :** All three levels within ±5%  
**Yellow decision :** At least one level ±5-10%  
**Red decision :** Any level outside ±10%

### Per TYPE (TYPE 1-5)

**Expected :** Each TYPE should mirror global distribution (±10% tolerance)

| TYPE | Distribution | Status | Action |
|------|--------------|--------|--------|
| TYPE 1 | N1: 25%, N2: 50%, N3: 25% | Target | If off ±10%, flag |
| TYPE 2 | N1: 25%, N2: 50%, N3: 25% | Target | If off ±10%, flag |
| TYPE 3 | N1: 25%, N2: 50%, N3: 25% | Target | If off ±10%, flag |
| TYPE 4 | N1: 25%, N2: 50%, N3: 25% | Target | If off ±10%, flag |
| TYPE 5 | N1: 25%, N2: 50%, N3: 25% | Target | If off ±10%, flag |

**Example :**
- TYPE 4 has N1: 20%, N2: 55%, N3: 25%
- Deviation: N1 is -5% (vs global 25%), N2 is +5%
- Status: YELLOW (at boundary, monitor)
- Action: Flag for PASS 3 if many similar

---

## TYPE DISTRIBUTION

**Target :** Each TYPE 15-25% of total (all types represented)

| TYPE | Count | % | Green (>10%) | Status |
|------|-------|---|---|---|
| TYPE 1 (Identification) | ~240 | 29% | ✓ | OK |
| TYPE 2 (Numbers) | ~240 | 29% | ✓ | OK |
| TYPE 3 (Years) | ~200 | 24% | ✓ | OK |
| TYPE 4 (Location) | ~100 | 12% | ✓ | OK |
| TYPE 5 (Correspondence) | ~50 | 6% | ✗ WARN | Under-represented |

**Threshold :** All types >10%  
**Red:** Any type <10% → indicates pool imbalance

---

## FORMAT CONSISTENCY

**Metric :** QUESTIONS_WITH_CONSISTENT_FORMAT / 277 * 100

| Consistency | Green | Yellow | Red |
|-------------|-------|--------|-----|
| Threshold | ≥99% | 95-99% | <95% |
| Action | OK | Flag for review | HIGH priority |

**What to check :**
```
For each question:
  - CASE(answer) == CASE(distractor_1/2/3)
  - ACCENTS(answer) == ACCENTS(distractors)
  - TYPE_FORMAT (for TYPE 3: "1998" vs "édition 1998")
  - UNITS (if answer has units, distractors must too)
```

**Example RED :**
```
Answer: "1998" (plain year)
D1: "1994" ✓
D2: "édition 2002" ✗ MISMATCH
D3: "2006" ✓
→ Format inconsistent, flag Q203 for PASS 3
```

---

## COLLISION METRICS

| Type | Count Target | Green | Yellow | Red | Action |
|------|---|---|---|---|---|
| Hard collisions | 0 | 0 | 0 | >0 | BLOCKER |
| Soft collisions | <5% | <5% | 5-10% | >10% | Flag + review |
| Reuse rate | <5% | <5% | 5-10% | >10% | Flag for diversity |

**Hard collision definition :**
```
distractor == any of 277 correct answers
```

**Soft collision definition :**
```
same entity (player, country, etc.) 
appears as answer in Q1 AND distractor in Q2
with different or similar context
```

**Reuse rate definition :**
```
count(distractors appearing > 1 time) / TOTAL_DISTRACTORS * 100
```

---

## BIAS DETECTION METRICS

### SOURCE CONCENTRATION (TYPE 1, 5)

**Threshold :** No single source >2% of total

| Source | Count | % | Threshold | Status |
|--------|-------|---|-----------|--------|
| Ronaldo | 14 | 1.7% | <2% | ✓ OK |
| France | 12 | 1.4% | <2% | ✓ OK |
| Pelé | 8 | 1.0% | <2% | ✓ OK |
| Unknown source | 25 | 3.0% | <2% | ✗ RED |

**Example RED :**
```
Source "Ronaldo" appears 25+ times across distractors
25 / TOTAL_DISTRACTORS = X% (ex: 25/831 = 3.0% pour cas source)
→ Over-representation, flag for PASS 3 diversity fix
```

### ERA CLUSTERING (TYPE 1, 3)

**Threshold :** <10% questions have >50% distractors from same era

| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| Questions with era clustering | <5 | 5-10 | >10 |
| Action | OK | Monitor | Flag for review |

**Example RED :**
```
Q042 (1966 era question):
- D1: Eusebio (1966 era)
- D2: Pauleta (1990s era)
- D3: Figo (1990s era)
→ 33% from 1966, 66% from 1990s
→ NO clustering (diverse eras) ✓

Q087 (1950s era question):
- D1: Fontaine (1950s)
- D2: Zichon (1950s)
- D3: Ademir (1950s)
→ 100% from 1950s era
→ CLUSTERING detected, flag ✗
```

### NATIONALITY BIAS (TYPE 1, 5)

**Threshold :** No single nationality >15% of TYPE 1+5 distractors

| Nationality | Count | % | Threshold | Status |
|-------------|-------|---|-----------|--------|
| Brazil | 85 | 12% | <15% | ✓ OK |
| France | 75 | 10% | <15% | ✓ OK |
| Germany | 70 | 9% | <15% | ✓ OK |
| Unknown | 120 | 16% | <15% | ✗ RED |

**Example RED :**
```
Brazilian players: 150 / 500 TYPE1+5 distractors = 30%
→ Way over 15% threshold
→ Flag for PASS 3: replace many Brazilian with other nationalities
```

---

## PLAUSIBILITY METRICS (TYPE 1, 5)

**Metric :** % distractors rated ≥80% plausible in context

| Rating | Green | Yellow | Red |
|--------|-------|--------|-----|
| Threshold | ≥80% | 75-80% | <75% |
| Action | OK | Flag for review | HIGH priority |

**What to assess :**
- Does distractor "sound possible" for this question?
- Would reasonable player hesitate?
- Is it recognizable in context?
- Is it "celebrity level" (for TYPE 5)?

**Example :**
```
Q042: "Quel joueur portugais a terminé meilleur buteur en 1966?"
D1: "Pauleta" ✓ Portuguese, famous, plausible
D2: "João Couto" ⚠️ Portuguese but obscure (hard to eliminate)
D3: "Figo" ✓ Portuguese, famous, plausible
→ Q042 Plausibility: 66% (one low) → FLAG ⚠️
```

---

## DECISION GATE

### GO Decision (✓ Ready for B4)

- ✓ Hard collisions = 0
- ✓ Format homogeneity ≥99%
- ✓ Difficulty distribution all within ±5%
- ✓ Type coverage all >10%
- ✓ Plausibility ≥80% (TYPE 1/5)
- ✓ No critical biases detected
- ✓ QA_STATUS = PASS

### CONDITIONAL_GO (⚠️ Fix first via PASS 3)

- ⚠️ Hard collisions ≤ few (fixable)
- ⚠️ Format homogeneity 95-99%
- ⚠️ Difficulty distribution ±5-10%
- ⚠️ Plausibility 75-80% (some questions)
- ⚠️ Reuse rate 5-10%
- ⚠️ Actionable flags exist
- Status: Proceed to PASS 3, then re-audit

### NO_GO (❌ Major rework needed)

- ❌ Hard collisions > 0
- ❌ Format homogeneity <95%
- ❌ Difficulty distribution ±15%+
- ❌ Critical biases (>15% nationality, etc.)
- ❌ QA_STATUS = FAIL
- Status: Return to PASS 1, revisit generation rules

---

## EXAMPLE AUDIT REPORT

```
═══════════════════════════════════════════════════
DISTRACTOR AUDIT REPORT
═══════════════════════════════════════════════════

SUMMARY
├── Total Distractors: [STOCK_CIBLE × 3]  ← ex: 831 pour cas source
├── Questions: 277
├── Status: ⚠️ CONDITIONAL_GO

HARD_BLOCKERS
├── Hard collisions: 2 ✗ (Q042, Q156)
├── Format issues: 1 ✗ (Q203)
└── QA_STATUS: [TOTAL_DISTRACTORS] PASS ✓

DISTRIBUTION
├── N1: 252 (30.3%) ✓
├── N2: 329 (39.6%) ✓
├── N3: 250 (30.1%) ✓
└── Type coverage: All >10% ✓

QUALITY
├── Format homogeneity: 99.6% ✓
├── Plausibility (TYPE 1/5): 84.1% ⚠️
└── Reuse rate: 3.2% ✓

BIAS
├── Source concentration: OK ✓
├── Era clustering: None ✓
└── Nationality skew: OK ✓

DECISION: CONDITIONAL_GO
Condition: Fix 2 hard collisions + 1 format issue (PASS 3)
→ Then proceed to B4
```

---

*STD_B3_distractor_metrics.md*  
*Version 1.0 — 2026-05-17*  
*Status: ACTIVE_REFERENCE*


