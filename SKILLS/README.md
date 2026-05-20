# Distractors Generation & Audit Skills

Three complementary skills for generating, auditing, and optimizing quiz distractors following B6 rules and FACTORY_REGISTRY_CORE architecture.

## Overview

**Four complementary skills:**

### FACTORY-Specific (B3 Distractor Pipeline)
Three-pass funnel for producing 831 high-quality distractors from 277 quiz questions:

```
PASS 1: distractors-generator
  ↓ (831 raw distractors)
PASS 2: distractor-audit-statistics
  ↓ (audit report + flags)
PASS 3: distractor-optimizer
  ↓
LAB READY
```

### Universal (All Claude Contexts)
```
token-optimization (ANY task/context)
  → Compress context (-30-50% tokens)
  → Batch processing
  → ID-based references
  → Narrative → tables
  → Applicable: Code, Cowork, FACTORY, web
```

## Skills (11 Total)

### PHASE A — Élaboration

#### 1. a2-bib-construction (A2)
Build raw source items from research → A2_BIB structuré par sections thématiques.

#### 2. a3-bib-processing (A3)
Normalize A2_BIB → A3_BIPREGEN (items codés) + A3_ANGIPREGEN (angles/quotas).

#### 3. a4-pools-definition (A4)
Define 20 pools architecture (IF-SF/IF-ROT/QV) avec assignations angles.

### PHASE B — Production

#### 4. b2-questions-generator (B2)
Generate 277 raw questions (Q+R+TYPE+Difficulty) pool by pool from BIPREGEN.

#### 5. distractors-generator (PASS 1 — B3)

Generate 3 plausible distractors per question (PASS 1 light rules, coherence + pertinence).

**What it does:**
- Reads question type (1-5), correct answer, difficulty level
- Loads rules from REGISTRY_RULES_DISTRACTORS
- Generates 10-15 candidates from real CDM sources
- Filters by coherence (shared properties with answer)
- Applies difficulty scaling (N1/N2/N3)
- Validates format
- Outputs 3 best candidates with rationale

**Input:** Question metadata + FACTORY_REGISTRY

**Output:** 3 distractors per question, 831 total (raw)

**Focus:** Plausibility, not collision-checking

---

### 2. distractor-audit-statistics (PASS 2)

Comprehensive audit of all 831 distractors to detect problems.

**What it does:**
- Checks for hard collisions (distractor = answer)
- Checks for soft collisions (same entity, different context)
- Measures format consistency
- Analyzes difficulty distribution (N1/N2/N3 %)
- Analyzes type distribution (TYPE 1-5 %)
- Detects source concentration (bias)
- Detects era clustering
- Detects nationality bias
- Flags all issues with severity
- Makes GO/NO-GO decision

**Input:** 831 distractors + 277 correct answers + FACTORY_REGISTRY_VALIDATIONS

**Output:** Detailed audit report + list of flagged questions for PASS 3

**Metrics:**
- Hard collisions: 0 (critical)
- Format homogeneity: ≥99%
- Difficulty distribution: N1/N2/N3 within ±5%
- Reuse rate: <5%
- No critical biases

---

### 3. distractor-optimizer (PASS 3)

Intelligently fix ONLY the problems flagged by PASS 2.

**What it does:**
- Reads audit flags with specific issue types
- Understands root cause of each flag
- Loads context-specific rules
- Generates 3-5 replacement candidates
- Selects best replacement (solves problem, maintains quality)
- Verifies no new issues created
- Outputs change with justification

**Input:** Audit flags + flagged questions + FACTORY_REGISTRY_RULES

**Output:** Optimized 831 distractors ready for LAB

**Philosophy:** Fix ONLY what's broken; preserve non-flagged distractors

#### 6. b4-spreadsheet-implantation (B4)
Implant B2 questions + B3 distractors into A5_TABLEUR → B4_TABLEUR vN.xlsx formatted.

#### 7. b5-audit-validator (B5)
Audit questions one-by-one, validate format/content, trace decisions → B5 logs + QA_STATUS assignment.

#### 8. b6-rules-extractor (B6)
Extract generalizable rules from cobaye audit → promote to glossaire FACTORY.

### UNIVERSAL

#### 9. token-optimization (ALL CONTEXTS)

Compress context and reduce token usage by 30-50% in ANY Claude context (Code, Cowork, FACTORY, web projects).

**What it does:**
- Audits current context for waste (repetitions, narratives, redundancy)
- Applies 8 compression patterns:
  1. ID-BASED_REFERENCE (replace descriptions with [RULE-X-NNN])
  2. STRUCTURE-TO-TABLE (narratives → tableaus)
  3. YAML-FOR-STRUCTURE (compact data encoding)
  4. HIERARCHY-COMPRESSION (implicit structures)
  5. BATCH-CONSOLIDATION (group requests)
  6. CONTEXT-LAYERING (incremental loading)
  7. SYNONYMS-UNIFICATION (glossaire enforcement)
  8. DEEP-LINKING (references not repetition)
- Quantifies token savings
- Documents token strategy
- Monitors ongoing compression

**Input:** Current context + task scope + conversation history

**Output:** Optimized context + compression strategy + token savings report

**Philosophy:** Tokens = scarce resource. Optimization is MANDATORY, not optional.

**Applicable to:**
- Large codebases (Code projects)
- Long conversations (Cowork)
- FACTORY documentation (quiz production)
- API-heavy projects (web)
- Any multi-file context

---

## How to Use

### Quick Start

```
1. Use distractors-generator
   Input: 277 questions with type/difficulty
   Output: 831 raw distractors

2. Use distractor-audit-statistics
   Input: 831 distractors + audit criteria
   Output: Audit report with flags

3. Use distractor-optimizer
   Input: Flags from audit
   Output: 831 optimized distractors

4. Optional: Re-run audit to confirm
```

### Full Workflow

#### Step 1: Generate Distractors

```
For each of 277 questions:
  /distractors-generator
  → Question: "Quel joueur portugais a terminé meilleur buteur en 1966?"
  → Type: 1, Difficulty: N2
  → Generates: ["Pauleta", "Figo", "Rui Costa"]

Output: 831 raw distractors
```

#### Step 2: Audit All Distractors

```
/distractor-audit-statistics
→ Input: 831 distractors + 277 answers
→ Measures:
   - Collisions
   - Format consistency
   - Difficulty distribution
   - Bias patterns
→ Output: Report + 23 flagged questions
```

#### Step 3: Fix Flagged Items

```
For each flagged question:
  /distractor-optimizer
  → Flag: "Q042 D2: Hard collision with Q156"
  → Replaces: "Ronaldo" → "Figo"
  → Verifies: No new issues introduced

Output: 831 optimized distractors
```

#### Step 4: Optional Re-audit

```
/distractor-audit-statistics (again)
→ Verify all fixes worked
→ Confirm no new issues
→ Green light for deployment
```

---

## Registry Integration

All three skills read from **FACTORY_REGISTRY_CORE**, not hardcoded rules.

### Registry Files

Located in: `C:\Users\Laurent\Desktop\site quiz\TRAVAIL EN COURS\quiz-core-lab\TEST COBAYE 78\00_MASTER_TEST\`

1. **REGISTRY_RULES_DISTRACTORS.md**
   - Rules for TYPE 1-5 (RÈGLE 1.1-5.6)
   - Transverse rules
   - Normative definitions

2. **REGISTRY_DEFINITIONS_CDM.md**
   - Position definitions (Gardien, Défenseur, etc.)
   - Era definitions (Pionnière, Classique, etc.)
   - Continent definitions
   - CDM host countries
   - Famous players pool
   - Plausibility thresholds

3. **REGISTRY_VALIDATIONS_QUALITY.md**
   - Validation rules
   - Collision definitions
   - Format standards
   - Metric thresholds
   - Distribution targets
   - Bias detection rules
   - Decision gate logic

4. **REGISTRY_AGENTS_DISTRACTOR.md**
   - Agent definitions
   - Authorized/forbidden actions
   - Input/output schemas
   - Process steps
   - Constraints

### Updating Rules

To change how skills behave, **modify the Registry files**, not the skill code.

**Example:** To change N2 difficulty range from ±2-3 to ±3-4:

1. Edit: `REGISTRY_RULES_DISTRACTORS.md` → `RULE-DIST-2-5`
2. Change: "N2 : écart ±2 à ±3" → "N2 : écart ±3 à ±4"
3. Save
4. Next time skills run, they automatically use new rule ✓

No code changes needed. No skill redeployment needed.

---

## Success Criteria

### PASS 1 (Generator) Success
- ✓ All 831 distractors generated
- ✓ All follow type-specific rules
- ✓ All plausible in context
- ✓ Format consistent within each question

### PASS 2 (Audit) Success
- ✓ Hard collisions = 0
- ✓ Format homogeneity ≥99%
- ✓ Difficulty distribution N1/N2/N3 within ±5%
- ✓ No critical biases
- ✓ Actionable flags for PASS 3

### PASS 3 (Optimizer) Success
- ✓ All flags addressed
- ✓ No new issues introduced
- ✓ Fixes verified
- ✓ Ready for LAB deployment

---

## Architecture

### Three-Pass Funnel Design

**Why three passes?**

1. **PASS 1 (Generator):** Maximize plausibility by minimizing constraints
2. **PASS 2 (Audit):** Detect ALL problems comprehensively
3. **PASS 3 (Optimizer):** Fix ONLY detected problems intelligently

Benefits:
- Better distractors (higher plausibility in PASS 1)
- Better problem detection (comprehensive audit in PASS 2)
- Better solutions (context-aware fixes in PASS 3)
- Better scalability (modular, each pass independent)

### Rules as Data

Skills read rules from Registry, not hardcoded logic.

Benefits:
- Single source of truth (Registry = authoritative)
- Easy updates (modify Registry, skills adapt)
- Auditability (all rules explicit, tracked)
- Scalability (same rules apply to future quizzes)

---

## Troubleshooting

### "Hard collisions not detected"
→ Verify REGISTRY_VALIDATIONS_QUALITY is accessible
→ Check collision detection logic in PASS 2

### "PASS 3 can't fix this collision"
→ Possible issue type misidentification
→ Review the specific question and collision in detail
→ May require returning to PASS 1 with different candidates

### "Reuse rate too high after PASS 3"
→ PASS 3 is fixing specific flags, not optimizing globally
→ Re-run PASS 2 audit with stricter reuse thresholds if needed
→ Consider running PASS 3 multiple times with different replacement strategies

### "Difficulty distribution still off after PASS 3"
→ PASS 3 fixes specific problems, may not optimize global distribution
→ If many flags, consider re-running full pipeline
→ Or adjust REGISTRY_VALIDATIONS thresholds if acceptable

---

## Files Structure

```
SKILLS/
├── README.md (this file)
├── .claude-plugin/
│   └── manifest.json (11 skills registered, v2.0)
│
├── a2-bib-construction/
│   └── SKILL.md (A2 — build BIB)
├── a3-bib-processing/
│   └── SKILL.md (A3 — normalize → BIPREGEN)
├── a4-pools-definition/
│   └── SKILL.md (A4 — define 20 pools)
├── b2-questions-generator/
│   └── SKILL.md (B2 — generate 277 questions)
├── distractors-generator/
│   └── SKILL.md (B3 PASS 1 — generation)
├── distractor-audit-statistics/
│   └── SKILL.md (B3 PASS 2 — audit)
├── distractor-optimizer/
│   └── SKILL.md (B3 PASS 3 — optimization)
├── b4-spreadsheet-implantation/
│   └── SKILL.md (B4 — implant xlsx)
├── b5-audit-validator/
│   └── SKILL.md (B5 — human audit)
├── b6-rules-extractor/
│   └── SKILL.md (B6 — extract rules)
└── token-optimization/
    └── SKILL.md (UNIVERSAL — token economy)

_FACTORY/_STANDARDS/
├── glossaire_documentaire_factory.md (definitions + SKILL_CREATION_PROTOCOL)
├── STD_B3_distractor_rules.md (rules read by skills)
├── STD_B3_distractor_metrics.md (metrics/thresholds read by skills)

_FACTORY/METHODES/
├── MDE_B3_distracteurs.md (B3 methodology)
├── SKILL.md (integration of all skills)
└── SKILL_CREATION_CHECKLIST.md (process automation)
```

---

## Next Steps

1. **Invoke via Skill tool:**
   ```
   /distractors-generator for question Q001
   /distractor-audit-statistics for all 831 distractors
   /distractor-optimizer for flagged items
   ```

2. **Monitor metrics:** Check audit reports for distribution/bias

3. **Iterate if needed:** PASS 2 → PASS 3 loop until all green

4. **Deploy:** Once audit passes, distractors ready for LAB

---

## Support

- Skill documentation: See individual SKILL.md files
- Registry documentation: See REGISTRY_*.md files
- Plan: See graceful-squishing-hickey.md
- Questions: Review the three SKILL.md files for detailed process steps

---

*Version 1.0*  
*Created: 2026-05-17*  
*Status: ACTIVE*
