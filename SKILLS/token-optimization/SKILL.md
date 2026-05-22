---
name: token-optimization
description: Skill général pour optimisation agressive des tokens dans TOUS contextes Claude (Code, Cowork, plateau web). Minimisation contexte, compression structures, batch processing, réduction conversation.
version: 1.0
status: ACTIVE
scope: UNIVERSAL (non-FACTORY-specific)
IA_COMPATIBLE: TRUE
---

# TOKEN OPTIMIZATION — Skill Universal

**Principe fondamental :** Tokens = ressource rare. Optimisation n'est pas optionnel, c'est un **impératif absolu**.

Utilisable dans TOUS les contextes : FACTORY, Claude Code, Claude Cowork, projets web, etc.

---

## QUAND UTILISER

Invoquer `/token-optimization` quand :
- Task est grande ou complexe (risque de dépassement contexte)
- Conversation s'allonge (accumulation contexte)
- Fichiers/structures peuvent être compressés
- Batch processing possible (grouper requêtes)
- Documentation peut être restructurée
- Termes/concepts réutilisables identifiables

**Ne PAS invoquer quand :** Task simple, one-shot, pas de contexte externalisable.

---

## THE PROCESS

### STEP 1 — Audit contexte actuel

**Questions :**
- Combien de fichiers lus jusqu'à présent ?
- Combien de lignes documentaires chargées ?
- Conversation a-t-elle > 10 messages ?
- Y a-t-il des répétitions détectables ?

**Objectif :** Mesurer gaspillage token réel.

---

### STEP 2 — Identifier points de compression

**Chercher :**
1. **Répétitions** : même concept expliqué multiple fois → consolidate
2. **Narratif** : paragraphes longs → convert en tableaux/listes
3. **Synonymes** : "distractor" vs "incorrect answer" vs "wrong option" → unifier
4. **Redondance inter-docs** : même info en B3/B5/B6 → centraliser
5. **Imports inutiles** : fichiers chargés mais non utilisés → supprimer

---

### STEP 3 — Appliquer 8 patterns d'optimisation

#### Pattern 1 : ID-BASED REFERENCE
```
BEFORE (21 tokens):
"Rule about hard collision detection in PASS 2 audit process..."

AFTER (3 tokens):
[RULE-HCOLL-001]
```

**Application :** Utiliser IDs au lieu de descriptions longues.

---

#### Pattern 2 : STRUCTURE-TO-TABLE
```
BEFORE (35 tokens, paragraphes narratifs):
"The process has three steps: first you generate 
candidates, then you filter by coherence, 
finally you apply difficulty rules..."

AFTER (12 tokens, tableau):
| Step | Action |
|------|--------|
| 1 | Generate candidates |
| 2 | Filter coherence |
| 3 | Apply difficulty |
```

**Application :** Tableaux/listes au lieu de prose.

---

#### Pattern 3 : YAML-FOR-STRUCTURE
```
BEFORE (18 tokens, listes avec clés texte):
- Name: Eusebio
- Era: 1966
- Position: Attaquant

AFTER (8 tokens, YAML):
name: Eusebio
era: 1966
pos: Attaquant
```

**Application :** YAML pour structures fixes, clés courtes.

---

#### Pattern 4 : HIERARCHY-COMPRESSION
```
BEFORE (41 tokens, explication narrative):
"The system has a general architecture for all quizzes, 
but each quiz theme (CDM, Rock, Mayenne) has specific rules 
that override the general ones in certain contexts..."

AFTER (7 tokens, hiérarchie implicite):
RULES: THEME-SPECIFIC > GENERAL > DEFAULT
```

**Application :** Hiérarchie explicite au lieu de narration.

---

#### Pattern 5 : BATCH-CONSOLIDATION
```
BEFORE (3 messages séparés):
Q1: "Crée la section A"
Q2: "Crée la section B"
Q3: "Crée la section C"

AFTER (1 message batch):
"Crée sections A/B/C avec [spécifications]"
```

**Application :** Grouper requêtes connexes en une seule.

---

#### Pattern 6 : CONTEXT-LAYERING
```
BEFORE (full context every time):
Load MASTER_ARCHITECTURE (15KB)
Load SKILL.md (8KB)
Load STD files (25KB)
= 48KB every message

AFTER (incremental):
Message 1: Load MASTER (15KB)
Message 2-5: Reference [key-IDs] only (0.5KB each)
Message 6: Reload if needed (15KB)
= 15.5KB vs 288KB saved
```

**Application :** Loader contexte incrementally, référencer par IDs.

---

#### Pattern 7 : SYNONYMS-UNIFICATION
```
BEFORE (4 synonymes dans docs):
- distractor
- incorrect answer
- wrong option
- fake answer

AFTER (1 terme + alias mapping):
DISTRACTOR (alias: incorrect_answer, wrong_option)
```

**Application :** Glossaire centralise termes, unifier références.

---

#### Pattern 8 : DEEP-LINKING
```
BEFORE (répéter règle):
"La règle dit que hard collision must be 0, 
and soft collision should be <5%..."

AFTER (1 lien):
Voir [RULE-HCOLL-001] et [RULE-SCOLL-001]
```

**Application :** Links au lieu de répétition contenu.

---

### STEP 4 — Quantifier économies

**Calcul :**
```
Token_BEFORE = [somme du contexte actuel]
Token_AFTER = [contexte optimisé]
ECONOMIE = Token_BEFORE - Token_AFTER
RATIO = ECONOMIE / Token_BEFORE * 100%
```

**Objectif :** Minimiser 30-50% des tokens dans la moyenne.

---

### STEP 5 — Appliquer optimisations

**Actions concrètes :**
- [ ] Consolider répétitions → nouveau fichier centralisé
- [ ] Convertir prose → tableaux
- [ ] Créer ID mappings (glossaire ou REFERENCE.md)
- [ ] Réorganiser imports (charger strictement nécessaire)
- [ ] Batch requêtes futures
- [ ] Documenter contexte layering (quand recharger)

---

### STEP 6 — Documenter stratégie tokens

Créer ou mettre à jour `TOKEN_STRATEGY.md` :

```markdown
# TOKEN STRATEGY

## Principles
- ID-based reference always
- Narratives prohibited (tables only)
- Batch > sequential processing
- Incremental loading mandatory

## Context Layers
Layer 0 (always): MASTER_ARCHITECTURE + glossaire
Layer 1 (on-demand): STD files
Layer 2 (on-demand): MDE files
Layer 3 (per-task): Task-specific files

## Compression Rules
- Max 50 chars per definition
- ID aliases for long names
- YAML for repeating structures
- Tableaux for comparisons
- <30 words per explanation

## Monitoring
- Token usage per message
- Context growth rate
- Compression ratio target: 30-50%
```

---

## RED FLAGS (ANTI-PATTERNS)

❌ **Ne jamais :**

1. **Répétition contenus** — même concept 2+ fois = bug
   - Fix: Centraliser, référencer par ID

2. **Narratif long** — paragraphes > 100 mots
   - Fix: Convertir en tableau ou listes compressées

3. **Imports globaux** — charger fichier entier si seulement 5 lignes utiles
   - Fix: Charger minimal, référencer (avec offset/ligne) autres sections

4. **Synonymes multiples** — "difficulteur" vs "difficult level" vs "niveau" vs "étape"
   - Fix: Glossaire force un terme unique

5. **Conversation longue** — >15 messages sans consolidation
   - Fix: Batch, summary, réduction scope

6. **Contexte réaccumulé** — recharger contexte déjà chargé
   - Fix: Layer strategy, référencer [KEY-ID]

7. **Explications répétées** — expliquer même règle multiple fois
   - Fix: [DEF-X-NNN] une seule fois, puis link

8. **Files trop larges** — charger 100KB pour 5KB utiles
   - Fix: Split logique, charger by section

---

## EXAMPLES

### Example 1 : FACTORY Optimization

**Scenario :** MDE_B3 + STD_B3 + STD_B6 + glossaire = 120KB contexte, conversation >20 messages.

**Before optimization :**
- Message 1-5 : Loaded 120KB (MASTER + all files)
- Message 6-10 : Repeated rule explanations (+15KB conversational overhead)
- Message 11-20 : Context reloaded (+120KB)
- **Total tokens :** 120 + 75 + 120 = **315KB**

**After optimization :**
- Message 1 : Load MASTER_ARCHITECTURE only (15KB)
- Message 2-20 : Use [RULE-X-NNN] / [DEF-X-NNN] IDs (0.2KB per message = 3.8KB)
- Message 21 : Reload if needed (15KB)
- **Total tokens :** 15 + 3.8 + 15 = **33.8KB**
- **Compression :** 89% ✓

---

### Example 2 : Claude Code Project Optimization

**Scenario :** Large codebase, multiple file reads, refactoring task.

**Before :**
- Read file A (25KB)
- Read file B (30KB)
- Read tests (20KB)
- Explain refactoring (5 messages × 5KB overhead)
- **Total :** 75 + 25 = **100KB**

**After :**
- Read ONLY implementation sections of A/B (10KB total)
- Batch refactoring requests (1 message instead of 5)
- Use line-range reads (offset/limit) instead of full files
- **Total :** 10 + 2 = **12KB**
- **Compression :** 88% ✓

---

### Example 3 : Continuous Monitoring

**Setup :** Track token usage per session automatically.

```markdown
## Token Accounting

| Phase | Context | Overhead | Total | Compression |
|-------|---------|----------|-------|-------------|
| Before opt | 50KB | 25KB | 75KB | — |
| After opt | 20KB | 2KB | 22KB | 71% |
```

---

## QUALITY GATES

**Optimization is done when :**

✓ No file loaded >2x unnecessarily  
✓ All long definitions replaced with IDs  
✓ No prose paragraph >50 words  
✓ Batch processing strategy documented  
✓ Context layer strategy clear  
✓ Token-per-message <2KB average  
✓ Compression ratio ≥30%  

---

## IMPLEMENTATION ACROSS CONTEXTS

### Claude Code (local projects)
- Batch file reads (read multiple with one tool call)
- Use line-range (offset/limit) not full files
- Cache READ results (don't re-read same file)
- Minimize terminal output (use line count flags)

### Claude Cowork (docs/wikis)
- Load table-of-contents, not full documents
- Reference sections by ID, not content
- Use API endpoints (if available) instead of full scrapes
- Batch document queries

### FACTORY (quiz production)
- Load MDE/STD by section (offset/limit)
- ID-reference [RULE-X-NNN] instead of rule text
- Consolidated glossaire (single source of truth)
- Batch skill invocations (1 message, multiple skills)

### Web Projects
- Use JSON APIs, not HTML scrapes
- Batch API calls (N operations per request)
- Cache responses (validate before refresh)
- Lazy-load non-critical data

---

## ONGOING GOVERNANCE

[RULE-OPT-TOKEN-001]
Token optimization is MANDATORY, not optional.

[RULE-OPT-TOKEN-002]
Every task >5KB context must assess compression opportunities.

[RULE-OPT-TOKEN-003]
Every tool call must ask : "Could this be batched or compressed ?"

[RULE-OPT-TOKEN-004]
Repeated context loading = bug, not feature.

[RULE-OPT-TOKEN-005]
Narratives > 50 words = refactor to table/list.

---

## CHECKLIST : BEFORE EVERY TOOL CALL

- [ ] Can this batch with previous call ? (reduce count)
- [ ] Is the file/section <5KB needed only ? (reduce size)
- [ ] Can IDs replace narrative ? (reduce tokens)
- [ ] Should context be reloaded or cached ? (avoid redundancy)
- [ ] Is the scope limited to what's needed ? (avoid bloat)

---

*Version 1.0 — 2026-05-17*
*Status: ACTIVE — Universal Skill*
*Applicable to: Code, Cowork, FACTORY, Web, all Claude contexts*


# FACTORY V2 — EXTENSION MACHINE-FIRST

Pour FACTORY, appliquer en priorité:
- lexique central: `_FACTORY/_STANDARDS/_GLOBAL/FACTORY_RUNTIME_LEXICON.md`
- protocole: `_FACTORY/_STANDARDS/_GLOBAL/TOKEN_ECONOMY_RUNTIME_PROTOCOL.md`
- audit: `python _FACTORY/_SCRIPTS/audit_token_economy.py`

Objectif: MINIMUM TOKENS + MINIMUM AMBIGUITY + MAXIMUM RUNTIME STABILITY.
