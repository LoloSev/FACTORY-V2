---
name: distractors-generator
description: "Use when generating distractors for quiz questions - applies B6 rules to produce 3 plausible incorrect answers matching the question type and difficulty level."
---

# Distractors Generator

## Overview

**Core Principle:** Generate maximally plausible incorrect answers by reading rules from FACTORY_REGISTRY and applying them with focus on coherence and relevance, deferring strict collision checks to PASS 2.

**Announce at start:** "Using distractors-generator to create [TYPE] distractors for [QUESTION_ID]"

This skill reads rules from FACTORY_REGISTRY_CORE, not hardcoded logic. Modify registry → skill adapts automatically.

---

## When to Use

This skill applies when you are generating 3 incorrect answers (distractors) for a single quiz question.

**Preconditions:**
- Question text available
- Correct answer known
- Question type identified (TYPE 1-5)
- Difficulty level specified (N1, N2, N3)
- FACTORY_REGISTRY_CORE accessible (REGISTRY_RULES_DISTRACTORS at minimum)

**You should NOT use this skill when:**
- Validating distractors (use distractor-audit-statistics instead)
- Fixing specific collision problems (use distractor-optimizer instead)
- Batch-modifying rules (update FACTORY_REGISTRY instead)

---

## The Process

### STEP 1: Identify Question Type

Read the question and determine which TYPE (1-5) it belongs to:

| TYPE | Pattern | Example |
|------|---------|---------|
| 1 | "Quel joueur / stade / équipe..." → réponse = nom propre | "Quel joueur portugais a terminé meilleur buteur en 1966?" → "Eusebio" |
| 2 | "Combien de buts / de fois / d'éditions..." → réponse = nombre | "Combien de buts Ronaldo a-t-il marqué en CDM?" → "15" |
| 3 | "En quelle année / édition..." → réponse = année | "En quelle année la France a-t-elle remporté sa première CDM?" → "1998" |
| 4 | "Dans quelle ville / quel pays..." → réponse = lieu | "Dans quel pays s'est déroulée la CDM 2010?" → "Afrique du Sud" |
| 5 | Multi-critères "Quel joueur X a [fait Y] lors de [édition Z]?" | "Quel joueur argentin a remporté Ballon d'Or en 2022?" → "Lionel Messi" |

---

### STEP 2: Load Type-Specific Rules

Load `REGISTRY_RULES_DISTRACTORS.md` and extract rules for your TYPE:

**TYPE 1 (IDENTIFICATION):**
- RULE-DIST-1-1: Selection (real, same category)
- RULE-DIST-1-2: Coherence (shared properties)
- RULE-DIST-1-3: Exclusion (vs 277 answers — soft check)
- RULE-DIST-1-4: Plausibility (recognizable)
- RULE-DIST-1-5: Difficulty scaling (N1/N2/N3)
- RULE-DIST-1-6: Format (case, accents)

**TYPE 2 (NUMBERS):**
- RULE-DIST-2-1: Selection (neighbors, real CDM values)
- RULE-DIST-2-2: Coherence (same magnitude range)
- RULE-DIST-2-3: Exclusion (vs 277 answers — soft check)
- RULE-DIST-2-4: Plausibility (seems possible)
- RULE-DIST-2-5: Difficulty scaling (N1: ±4+, N2: ±2-3, N3: ±1)
- RULE-DIST-2-6: Format (Arabic numerals, no units unless answer has them)

**TYPE 3 (YEARS/EDITIONS):**
- RULE-DIST-3-1: Selection (only real CDM years)
- RULE-DIST-3-2: Coherence (event could logically happen then)
- RULE-DIST-3-3: Exclusion (vs 277 answers — soft check)
- RULE-DIST-3-4: Plausibility (contextually appropriate era)
- RULE-DIST-3-5: Difficulty scaling (N1: far apart, N2: same decade, N3: adjacent)
- RULE-DIST-3-6: Format (1998 vs "édition 1998" — consistent)

**TYPE 4 (LOCATION):**
- RULE-DIST-4-1: Selection (real host countries, real cities)
- RULE-DIST-4-2: Coherence (country stays country, city stays city; same region if relevant)
- RULE-DIST-4-3: Exclusion (vs 277 answers — soft check)
- RULE-DIST-4-4: Plausibility (recognizable location)
- RULE-DIST-4-5: Difficulty scaling (N1: different continent, N2: other hosts, N3: same region)
- RULE-DIST-4-6: Format (French spelling, "Afrique du Sud" not "South Africa")

**TYPE 5 (CORRESPONDENCE):**
- RULE-DIST-5-1: Selection (satisfies some criteria, not all)
- RULE-DIST-5-2: Coherence (shares ≥1 criterion with answer)
- RULE-DIST-5-3: Exclusion (vs 277 answers — soft check, HIGH RISK)
- RULE-DIST-5-4: Plausibility (celebrity-level credible)
- RULE-DIST-5-5: Difficulty scaling (N1: one minor criterion, N2: one strong criterion, N3: all but one)
- RULE-DIST-5-6: Format (full name if answer is full name)

---

### STEP 3: Extract Question Context

From the question text and correct answer, identify:

**For TYPE 1 (Identification):**
- Category: Player? Team? Stadium? Coach?
- If player: Position? Nationality? Era?
- If team: Continent? Decades active?

**For TYPE 2 (Numbers):**
- Range: Goals? Editions? Appearances?
- Context: Is this from famous achiever or mid-tier?

**For TYPE 3 (Years):**
- Type of event: Victory? First appearance? Hosting?
- Teams involved: Narrows context era

**For TYPE 4 (Location):**
- City or country? Same country required (if city)?
- Geographic region relevant?

**For TYPE 5 (Correspondence):**
- Criteria in question: Nationality? Era? Achievement? Team?
- How many criteria define the answer?

Load `REGISTRY_DEFINITIONS_CDM.md` to understand:
- Positions available (Gardien, Défenseur, Milieu, Attaquant)
- Eras (Pionnière, Classique, Moderne, Contemporaine 1, Contemporaine 2)
- Continents and their footballing traditions
- Era definitions for context matching

---

### STEP 4: Generate Candidate Pool

Create 10-15 candidate distractors using rule-based selection:

**TYPE 1 Example:**
```
Question: "Quel joueur portugais a terminé meilleur buteur en 1966?"
Correct Answer: "Eusebio"
Context from registry: Portuguese attacker, 1966 era

RULE-DIST-1-1 (Selection): Pool of famous Portuguese attackers
Candidates: Pauleta, Figo, Rui Costa, Simão Sabrosa, Cristiano Ronaldo, Conceição
(Avoid: modern-era players like Ronaldo too young for 1966)

Filter for 1966-plausible era: Pauleta, Figo, Rui Costa (too young?), ...
```

**TYPE 2 Example:**
```
Question: "Combien de buts Ronaldo (Brésil) a-t-il marqué en CDM?"
Correct Answer: "15"
Difficulty: N2 (±2 to ±3 range)

RULE-DIST-2-1 (Selection): Real goal totals from CDM history
Candidates nearby: 12, 13, 14, 16, 17, 18
(From actual players: Müller 14, Fontaine 13, Gerd Müller records, etc.)

Filter for plausible range (1-16): 12, 13, 14, 16, 17, 18
```

---

### STEP 5: Apply RÈGLE X.2 (Coherence)

Filter candidates to keep only those sharing ≥1 property with correct answer:

**TYPE 1:**
- Same position if role-specific (attacker shares with attacker, not goalkeeper)
- Same continent or nearby era
- Same type of entity (player, not manager)

**TYPE 2:**
- Plausible range for context (1-16 for goals, 1-6 for editions)
- Real CDM numbers if possible

**TYPE 3:**
- Real CDM years only
- Era contextually possible

**TYPE 4:**
- Country stays country (not mix with cities)
- Same region if geography-dependent

**TYPE 5:**
- Shares ≥1 criterion (nationality, era, achievement, etc.)
- Not completely unrelated

After coherence filter: 6-10 candidates remain.

---

### STEP 6: Filter by Difficulty (RULE X.5)

Select 3 candidates matching the difficulty level:

**N1 (Easy):**
- Large spacing (±4+ for numbers, different continent for countries, different era entirely)
- Eliminable by general knowledge
- Example: If answer is Portuguese 1966, choose Belgian 2010, Swedish 1950, Brazilian 1998

**N2 (Medium):**
- Moderate spacing (±2-3 for numbers, same decade for years, same continent for countries)
- Requires specific knowledge to eliminate
- Example: If answer is Portuguese 1966 attacker, choose Portuguese 1970 defender, Spanish 1970 attacker

**N3 (Difficult):**
- Minimal spacing (±1 for numbers, adjacent years, same region)
- Shares almost all criteria except one specific detail
- Example: If answer is "Lionel Messi won 2022 Ballon d'Or", choose "Lautaro Martínez" (same nationality/era, different achievement)

---

### STEP 7: Validate Format (RULE X.6)

Ensure all 3 candidates match format of correct answer:

**Checks:**
- [ ] Case matches: If "Eusebio", not "eusebio" or "EUSEBIO"
- [ ] Accents match FIFA spelling: "Pelé" not "Pele"
- [ ] Numbers: Arabic numerals only ("15" not "quinze")
- [ ] Locations: Same language as answer ("Afrique du Sud" not "South Africa")
- [ ] Names: Full format consistency (if "Lionel Messi", all names should be "FirstName LastName")

---

### STEP 8: Output 3 Distractors

Return structured output:

```
QUESTION_ID: Q042
TYPE: 1 (IDENTIFICATION)
DIFFICULTY: N2
CORRECT_ANSWER: "Eusebio"

DISTRACTOR_1: "Pauleta"
REASON: Portuguese attacker, contemporary era (1990s-2000s), shares nationality with answer. RULE-DIST-1-2 coherence + RULE-DIST-1-5 N2 scaling (same nationality, different era/role).

DISTRACTOR_2: "Figo"
REASON: Portuguese player, famous, plausible era. Not attacker but contemporary. RULE-DIST-1-2 coherence + RULE-DIST-1-5 N2 scaling.

DISTRACTOR_3: "Rui Costa"
REASON: Portuguese midfielder, 1990s-2000s, shares nationality. RULE-DIST-1-2 coherence + RULE-DIST-1-5 N2 scaling (same nationality, different position/era).

RULES_APPLIED: RULE-DIST-1-1, RULE-DIST-1-2, RULE-DIST-1-3, RULE-DIST-1-4, RULE-DIST-1-5, RULE-DIST-1-6
FORMAT_VALIDATED: ✓ (All names: FirstName LastName, Portuguese origin, plausible era)
ANTI_COLLISION_SOFT_CHECK: No obvious matches in known answers
```

---

## Example Walkthroughs

### Example 1: TYPE 2 (Numbers)

```
INPUT:
- Question: "Combien de buts Ronaldo (Brésil) a-t-il marqué en Coupe du monde?"
- Correct Answer: "15"
- Difficulty: N2

STEP 1: TYPE = 2 (NUMBERS)

STEP 2: Load REGISTRY_RULES_DISTRACTORS[TYPE_2]
- RULE-DIST-2-1 Selection (real CDM values, neighbors)
- RULE-DIST-2-5 Difficulty: N2 = ±2 to ±3

STEP 3: Context = "goals by Ronaldo (Brazil)"
- Range: 1-16 typical for top scorers
- Context: Famous attacker, Brazil

STEP 4: Generate candidates
- Real totals from CDM history: 12, 13, 14, 16, 17, 18
- (Based on Fontaine 13, Müller 14, etc.)

STEP 5: Apply coherence
- All in range 1-16 ✓
- All plausible CDM goal counts ✓

STEP 6: Filter by N2 (±2 to ±3)
- For answer 15: ±2-3 = [12, 13, 14, 16, 17, 18]
- Select 3: 12, 13, 17 (varied for better selection)

STEP 7: Format validation
- Arabic numerals: "12", "13", "17" ✓
- No units: correct (answer is "15" not "15 goals") ✓

STEP 8: Output
DISTRACTORS: ["12", "13", "17"]
RULES_APPLIED: RULE-DIST-2-1, RULE-DIST-2-2, RULE-DIST-2-5, RULE-DIST-2-6
```

### Example 2: TYPE 5 (Correspondence)

```
INPUT:
- Question: "Quel joueur argentin a remporté le Ballon d'Or en 2022?"
- Correct Answer: "Lionel Messi"
- Difficulty: N3

STEP 1: TYPE = 5 (CORRESPONDENCE)

STEP 2: Load REGISTRY_RULES_DISTRACTORS[TYPE_5]
- RULE-DIST-5-1: Selection (satisfies some but not all criteria)
- RULE-DIST-5-5: Difficulty N3 = shares all criteria except one precise detail

STEP 3: Criteria extraction from question:
- Criterion A: Argentinian nationality
- Criterion B: 2022 edition
- Criterion C: Ballon d'Or winner

STEP 4: Generate candidates sharing 2 of 3 criteria:
- Candidate 1: "Lautaro Martínez" (Argentinian ✓, 2022 ✓, but not Ballon d'Or ✗)
- Candidate 2: "Kylian Mbappé" (Not Argentinian ✗, 2022 ✓, finalist/great player ✓ loose)
- Candidate 3: "Antoine Griezmann" (Not Argentinian ✗, 2022 edition ✓, strong player ✓)

STEP 5: Coherence check
- Lautaro: shares nationality + era, loses precision
- Mbappé: shares era + top-level player status
- Griezmann: shares era + competitive level

STEP 6: N3 filtering
- All candidates are famous/plausible
- Each shares 2/3 criteria, forcing precise knowledge
- ✓ N3 difficulty achieved

STEP 7: Format validation
- "Lionel Messi" = FirstName LastName
- All distractors must match: ✓ "Lautaro Martínez", "Kylian Mbappé", "Antoine Griezmann"

STEP 8: Output
DISTRACTORS: ["Lautaro Martínez", "Kylian Mbappé", "Antoine Griezmann"]
RULES_APPLIED: RULE-DIST-5-1, RULE-DIST-5-2, RULE-DIST-5-4, RULE-DIST-5-5, RULE-DIST-5-6
```

---

## Red Flags: What NOT to Do

| Red Flag | Why It's Wrong | Fix |
|----------|---|---|
| "I'll just pick any player who played in CDM" | RULE-DIST-1-2 requires coherence, not random. Breaks plausibility. | Use REGISTRY to extract same position/era. |
| "Format doesn't matter, user will understand" | RULE-DIST-X-6 requires homogeneous format. "Eusebio" vs "EUSEBIO" breaks question. | Match case/accents exactly to correct answer. |
| "N3 means very hard, so I'll use obscure players" | N3 means small spacing, not unknown. "Totally Obscure Brazilian 2010" = too easy to eliminate. | Use N3 = same position/era, different name. |
| "I can invent a country to make questions harder" | RULE-TRANS-3 forbids invention. "Atlantica" fails audit. | Use only real CDM host/participant countries. |
| "Let me apply strict anti-collision here" | PASS 1 focuses on plausibility. PASS 2 handles collisions. | Use soft checks only; let audit catch real collisions. |
| "This rule seems too strict, I'll skip it" | Rules are in REGISTRY for a reason. Skipping breaks auditability. | Apply all rules even if tedious. They scale. |
| "My N1 distractors are almost identical to answer" | Large spacing is what defines N1. This is N3. | Re-read RULE-DIST-X-5 for your TYPE. |
| "One distractor will be reused across 50 questions for consistency" | RULE-TRANS-5 discourages reuse. Creates pattern bias. | Let PASS 2 audit catch reuse; PASS 3 fixes it. |

---

## Process Checklist

- [ ] Question type correctly identified (1-5)
- [ ] Rules loaded from REGISTRY_RULES_DISTRACTORS
- [ ] Context extracted (nationality, position, era, etc.)
- [ ] 10-15 candidates generated from real sources
- [ ] RULE X.2 (Coherence) applied — shared properties verified
- [ ] Difficulty level filters applied (N1/N2/N3 spacing)
- [ ] RULE X.6 (Format) validated — case, accents, units match
- [ ] 3 distractors selected
- [ ] Soft anti-collision check (no obvious matches to known answers)
- [ ] Output structured with rule references
- [ ] All distractors distinct from each other
- [ ] All distractors distinct from correct answer

---

## Output Quality Markers

✓ **Good Output:**
```
DISTRACTOR: "Pauleta"
REASON: Portuguese attacker (matches context). Contemporary era (1990s-2000s) differs from 1966 answer era. Plausible under RULE-DIST-1-2 + N2 difficulty. Format matches "Eusebio".
```

✗ **Poor Output:**
```
DISTRACTOR: "Some Other Midfielder"
REASON: It's a distractor.
```

---

*Skill: distractors-generator*  
*Version: 1.0*  
*Reads from: FACTORY_REGISTRY_CORE*  
*Feeds to: distractor-audit-statistics (PASS 2)*
