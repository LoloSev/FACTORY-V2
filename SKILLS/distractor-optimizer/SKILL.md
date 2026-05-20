---
name: distractor-optimizer
description: "Use when fixing flagged distractors - intelligently regenerates only the problematic distractors identified by audit, using specific issue context to ensure fixes actually solve problems."
---

# Distractor Optimizer

## Overview

**Core Principle:** Intelligently fix ONLY the distractors flagged by PASS 2 audit, using specific problem context to ensure each replacement addresses the root cause.

**Announce at start:** "Using distractor-optimizer to fix [N] flagged distractors from [POOL_NAME]"

Key difference from PASS 1: PASS 1 = "Generate 3 options"; PASS 3 = "Fix THIS specific option because it has PROBLEM X".

---

## When to Use

This skill applies **after PASS 2 audit completes** with a list of flagged questions.

**Preconditions:**
- PASS 2 audit report available
- List of flagged distractors with specific issues
- Original question context available
- FACTORY_REGISTRY_RULES_DISTRACTORS accessible
- Correct answers preserved

**You should NOT use this skill when:**
- Still in PASS 1/2 (use those skills first)
- Making global strategy changes (update rules in REGISTRY instead)
- Fixing more than the audited flags (wait for next full audit)

---

## The Process

### STEP 1: Read Audit Flag

Understand the SPECIFIC problem for this distractor:

```
Flag example from PASS 2 audit:
{
  "question_id": "Q042",
  "distractor_index": 1,
  "issue": "HARD_COLLISION",
  "severity": "CRITICAL",
  "root_cause": "Distractor 'Ronaldo' matches correct answer in Q156",
  "recommendation": "Replace with different player"
}

Your job: Fix ONLY distractor at index 1 of Q042.
```

Common issue types:

| Issue Type | Meaning | Root Cause | Fix Strategy |
|---|---|---|---|
| HARD_COLLISION | Distractor = correct answer elsewhere | Same name, different context | Replace with entirely different entity |
| SOFT_COLLISION | Same entity, similar context | Reused without reason | Replace with different entity if TYPE 1/5 |
| FORMAT_MISMATCH | "édition 1998" mixed with "1998" | Inconsistent format | Reformat to match answer |
| OUT_OF_RANGE | Number too far from answer | Bad difficulty spacing | Adjust number to correct range |
| SOURCE_CONCENTRATION | Overused source (e.g., Ronaldo 14x) | Bias detected | Replace with different source |
| PLAUSIBILITY_LOW | Distractor too obscure or implausible | Weak candidate | Replace with more recognizable option |
| ERA_CLUSTERING | Too many from same era | Historical bias | Replace with different era |
| IMPLAUSIBLE_NUMBER | Chiffre way out of plausible range | Generation error | Recalculate with correct bounds |

---

### STEP 2: Understand Original Question Context

Retrieve and analyze:

```
Question_ID: Q042
Question_Text: "Quel joueur portugais a terminé meilleur buteur en 1966?"
Correct_Answer: "Eusebio"
Question_Type: 1 (IDENTIFICATION)
Difficulty: N2

Original_Distractors:
├── D1: "Pauleta" (Portuguese, contemporary attacker) ✓ Good
├── D2: "Ronaldo" (FLAGGED: Hard collision with Q156 answer)
└── D3: "Rui Costa" (Portuguese midfielder, 1990s) ✓ Good

Context from registry:
├── Answer era: 1966
├── Answer position: Attacker
├── Answer nationality: Portuguese
├── Difficulty N2 means: Same nationality, different era/role
```

---

### STEP 3: Load Problem-Specific Rules

Based on issue type, load rules from REGISTRY:

**For HARD_COLLISION:** Load RULE-DIST-[TYPE]-3 (EXCLUSION)
```
RULE-DIST-1-3: "Vérifier contre la liste complète des 277 réponses"
→ Must ensure replacement NOT in 277 correct answers
```

**For SOFT_COLLISION (TYPE 1/5):** Load context rules
```
For TYPE 1: Different nationality or era preferred to avoid confusion
```

**For FORMAT_MISMATCH:** Load RULE-[TYPE]-6 (FORMAT)
```
RULE-DIST-3-6: "If answer '1998', distractors must '1994', '2002'"
→ Standardize to matching format
```

**For OUT_OF_RANGE (TYPE 2):** Load RULE-2-5 (DIFFICULTY_SCALING)
```
RULE-DIST-2-5: N2 = ±2 to ±3
→ Recalculate range
```

**For PLAUSIBILITY_LOW:** Load RULE-[TYPE]-4 (PLAUSIBILITY)
```
→ Find more recognizable candidates
```

---

### STEP 4: Generate Replacement Candidates

Create 3-5 replacement options addressing the specific problem:

**Example: HARD_COLLISION in Q042**

```
Original Problem: "Ronaldo" (appears as correct answer in Q156)
Question context: Portuguese attacker, 1966, N2 difficulty
Requirements (RULE-DIST-1-2 + RULE-DIST-1-5):
- Portuguese (same nationality as Eusebio)
- Contemporary era (different from 1966, for N2 scaling)
- Recognizable name

Replacement candidates:
1. "Pauleta" ← ALREADY USED as D1, skip
2. "Figo" ← Portuguese, contemporary, famous, NOT in 277 answers ✓
3. "Simão Sabrosa" ← Portuguese, 1990s-2000s, lesser known but plausible ✓
4. "Nuno Gomes" ← Portuguese, 1990s, strong defender/midfielder ✓
5. "Rui Costa" ← ALREADY USED as D3, skip

Final candidates: Figo, Simão Sabrosa, Nuno Gomes
Select best: "Figo" (most famous, clearest N2 difficulty)
```

**Example: FORMAT_MISMATCH in Q203**

```
Original Problem: Mix of "1998" and "édition 1998"
Question: "En quelle année la France a-t-elle remporté sa première CDM?"
Answer: "1998" (plain year, no prefix)

Original distractors:
- D1: "1994" ✓ Correct format
- D2: "édition 2002" ✗ Wrong format (should be "2002")
- D3: "2006" ✓ Correct format

Fix D2: Replace "édition 2002" with "2002"
(No need to generate new candidate; just reformat)
```

**Example: OUT_OF_RANGE in Q087**

```
Original Problem: "47" is way too high
Question: "Combien de buts Ronaldo (Brésil) a-t-il marqué en CDM?"
Correct Answer: "15"
Difficulty: N2 (±2-3 range expected)

Out of range: "47" is +32, way outside ±3
Range needed: 12-18 (±3 from 15)

Original distractors:
- D1: "12" ✓ In range
- D2: "13" ✓ In range
- D3: "47" ✗ Out of range, must fix

Fix D3: Replace "47" with "17" (within ±3, real CDM achiever)
Rationale: 17 is plausible, differs by 2, matches N2 difficulty
```

---

### STEP 5: Select Best Replacement

Choose replacement that:

1. **Solves the specific problem** (collision fix → different entity)
2. **Maintains difficulty** if possible (N1 → N1, N2 → N2, N3 → N3)
3. **Preserves format** (matches correct answer)
4. **Is verifiable** (real CDM data, not invented)
5. **Doesn't introduce new problems** (check registry before committing)

**Decision criteria:**

```
REPLACEMENT_SCORE = (problem_solved × 100) + (difficulty_maintained × 50) + (format_match × 30) + (not_already_used × 20) - (introduces_new_issue × 100)

Best replacement = highest score
```

---

### STEP 6: Verify Replacement Doesn't Break Other Validations

Before committing, check:

```
For HARD_COLLISION replacement:
☐ Replacement NOT in 277 correct answers
☐ Replacement NOT already a distractor elsewhere
☐ Replacement matches format of original answer

For SOFT_COLLISION replacement:
☐ Different entity from problematic one
☐ Contextually distinct

For FORMAT fix:
☐ All 4 options (answer + 3 distractors) now consistent
☐ No other format issues introduced

For DIFFICULTY fix:
☐ Spacing now matches N1/N2/N3 target
☐ Still recognizable/plausible

For PLAUSIBILITY fix:
☐ Replacement is recognizable in context
☐ Not too obscure or too famous (if N3 intended)

For CONCENTRATION fix:
☐ Replacement uses different source (player, country, era)
☐ Doesn't exacerbate bias elsewhere
```

---

### STEP 7: Output Replacement with Justification

```
Question_ID: Q042
Distractor_Index: 1

Original: "Ronaldo"
Replacement: "Figo"

Issue_Fixed: HARD_COLLISION
Root_Cause: "Ronaldo" matches correct answer in Q156
Rationale: "Figo" is Portuguese (maintains RULE-DIST-1-2 coherence), contemporary era (N2 difficulty), famous and recognizable (RULE-DIST-1-4 plausibility). Not in 277 correct answers (RULE-DIST-1-3 exclusion).

Rules_Applied: RULE-DIST-1-2, RULE-DIST-1-3, RULE-DIST-1-4, RULE-DIST-1-5, RULE-DIST-1-6
Format_Validated: ✓ (matches "Eusebio" format: FirstName LastName, Portuguese origin)
New_Set: ["Pauleta", "Figo", "Rui Costa"]
Verification: No hard collisions, no format issues, N2 difficulty maintained ✓
```

---

## Example Walkthroughs

### Example 1: Hard Collision Fix

```
INPUT from audit:
{
  "question_id": "Q156",
  "distractor_index": 2,
  "issue": "HARD_COLLISION",
  "severity": "CRITICAL",
  "root_cause": "Distractor 'Eusebio' matches correct answer in Q042",
  "recommendation": "Replace with different Portuguese player"
}

STEP 1: Read flag
→ Q156 distractor_2 is "Eusebio", which is answer to Q042

STEP 2: Original context
Question: "Quel joueur portugais a marqué en Coupe du Monde?"
Answer: "Pauleta" (Portuguese, multi-era attacker)
Type: 1
Difficulty: N2
Original distractors: ["Eusebio", "Figo", "Rui Costa"]
Problem distractor: "Eusebio" (collision)

STEP 3: Load rules
RULE-DIST-1-2 (coherence), RULE-DIST-1-3 (exclusion)

STEP 4: Generate candidates
Portuguese players NOT in 277 answers:
- "Simão Sabrosa" ← Portuguese, 1990s, plausible N2
- "Nuno Gomes" ← Portuguese, 1990s, less famous but valid
- "João Couto" ← Portuguese but obscure (no)

STEP 5: Select best
"Simão Sabrosa" - Famous in CDM 2002, meets N2 (different era from "Pauleta")

STEP 6: Verify
✓ Not in 277 answers
✓ Format matches "Pauleta"
✓ Maintains N2 difficulty
✓ Fixes hard collision

STEP 7: Output
Original: "Eusebio"
Replacement: "Simão Sabrosa"
Rationale: Addresses hard collision. Portuguese (RULE-DIST-1-2), contemporary era (N2 scaling), recognizable (RULE-DIST-1-4), not in correct answers list (RULE-DIST-1-3).
```

### Example 2: Format Mismatch Fix

```
INPUT from audit:
{
  "question_id": "Q203",
  "distractor_index": 2,
  "issue": "FORMAT_MISMATCH",
  "severity": "HIGH",
  "root_cause": "Distractor 'édition 2022' inconsistent with answer '2018'",
  "recommendation": "Remove 'édition' prefix to match answer format"
}

STEP 1: Read flag
→ Q203 distractor_2 has wrong format

STEP 2: Context
Question: "En quelle année s'est déroulée la CDM 2018?"
Answer: "2018" (plain year)
Type: 3
Original distractors: ["2014", "édition 2022", "2010"]
Problem: "édition 2022" doesn't match "2018" format

STEP 3: Load RULE-DIST-3-6 (FORMAT)

STEP 4: Replace
Not generating new candidate; just reformatting
"édition 2022" → "2022"

STEP 5: Verify format consistency
Answer: "2018"
D1: "2014" ✓
D2: "2022" ✓ (fixed)
D3: "2010" ✓
All plain years, consistent ✓

STEP 6: Verify other properties
- All real CDM years ✓
- N2 spacing maintained ✓

STEP 7: Output
Original: "édition 2022"
Replacement: "2022"
Issue_Fixed: FORMAT_MISMATCH
Rationale: RULE-DIST-3-6 requires consistent format. Answer is plain year, so all distractors must be plain years.
```

### Example 3: Plausibility Fix

```
INPUT from audit:
{
  "question_id": "Q087",
  "distractor_index": 3,
  "issue": "PLAUSIBILITY_LOW",
  "severity": "MEDIUM",
  "root_cause": "Distractor '47' is implausible (way too many goals)",
  "recommendation": "Use ±2-3 range (N2 difficulty)"
}

STEP 1: Read flag
→ Q087 distractor_3 is implausible

STEP 2: Context
Question: "Combien de buts Ronaldo (Brésil) a-t-il marqué en CDM?"
Answer: "15"
Difficulty: N2
Range needed: 12-18 (±3)
Original distractor_3: "47" (way too high, implausible)

STEP 3: Load RULE-DIST-2-5 (DIFFICULTY_SCALING)
N2 = ±2 to ±3

STEP 4: Generate replacement
Options in 12-18 range:
- "12" ← Already used as D1
- "13" ← Already used as D2
- "14" ← Real (Müller's total)
- "16" ← Real (Cristiano's total)
- "17" ← Real (Neymar attempted)
- "18" ← Plausible

Select: "17" (different from already-used 12, 13; within range; real player data)

STEP 5: Verify
✓ In range 12-18 (±3 from 15)
✓ Real CDM total
✓ Maintains N2 difficulty
✓ Not already used
✓ Plausible

STEP 6: Verify no new issues
All distractors: 12, 13, 17
- Unique ✓
- In range ✓
- Real data ✓

STEP 7: Output
Original: "47"
Replacement: "17"
Issue_Fixed: PLAUSIBILITY_LOW
Rationale: RULE-DIST-2-5 N2 requires ±2-3 range. "47" is +32 (implausible). "17" is +2 (within N2 range, realistic, real CDM data).
```

---

## Red Flags: Optimizer Anti-Patterns

| Red Flag | Problem | Fix |
|----------|---------|-----|
| "I'll just replace with random player" | No problem-solving, likely creates new issues | Understand root cause, select targeted replacement |
| "This collision is hard to fix, skip it" | HARD_COLLISION MUST be fixed | Find any valid replacement, don't skip |
| "I'll change format to 'édition' for all to fix one mismatch" | Breaking 276 other questions | Fix only the one question's format |
| "New replacement introduces soft collision too" | Fixing one problem, creating another | Choose different replacement that solves without introducing new issues |
| "I don't have time for PASS 3, deploy anyway" | Unaudited, unverified questions → failures in LAB | PASS 3 is mandatory before deployment |
| "This flag seems wrong, I'll ignore it" | Trust the audit metrics | Trust audit or re-run it, but don't skip flagged items |
| "All replaced distractors are now from 1998 era" | Creating era clustering bias | Diversify sources across eras |

---

## Optimizer Checklist

- [ ] Flag understood (issue type clear)
- [ ] Root cause analyzed
- [ ] Original question context retrieved
- [ ] Relevant registry rules loaded
- [ ] 3-5 replacement candidates generated
- [ ] Best candidate selected (solves problem + maintains quality)
- [ ] Replacement verified (not in 277 answers, format ok, difficulty ok)
- [ ] No new issues introduced
- [ ] Replacement documented with rationale
- [ ] Output structured and ready for re-audit
- [ ] All flagged items processed

---

## Quality Assurance

After fixing all flagged items, output summary:

```
OPTIMIZATION_SUMMARY
═══════════════════════════════════════════════════

Total Flags Processed: 23
├── Hard Collisions Fixed: 2
├── Soft Collisions Fixed: 5
├── Format Issues Fixed: 1
├── Plausibility Improved: 8
├── Out-of-Range Fixed: 4
├── Source Concentration Reduced: 3
└── Era Clustering Resolved: 0

Changes Made:
├── Q042 D2: "Ronaldo" → "Figo" (hard collision)
├── Q087 D3: "47" → "17" (out of range)
├── Q156 D2: "Eusebio" → "Simão Sabrosa" (hard collision)
├── Q203 D2: "édition 2022" → "2022" (format)
... (total 23 changes)

Recommendation: Re-run PASS 2 audit to confirm all fixes successful.
```

Then, **re-run PASS 2 audit** on optimized distractors to verify fixes work and no new issues introduced.

---

*Skill: distractor-optimizer*  
*Version: 1.0*  
*Reads from: FACTORY_REGISTRY_CORE (RULES_DISTRACTORS)*  
*Consumes: Output of distractor-audit-statistics (PASS 2 flags)*  
*Outputs: Optimized 831 distractors → ready for LAB or re-audit*
