---
name: startup-verification
description: Automatic verification at next session start — plugin installed?
---

# STARTUP VERIFICATION — Next Session Checklist

**Claude:** Execute this checklist at EVERY session start.

---

## Step 1 : Verify Plugin Detection

Try invoking a simple skill to confirm plugin is loaded.

**Test command:**
```
/token-optimization
→ If responds with skill description → ✅ INSTALLED
→ If error/unknown → ❌ NOT INSTALLED
```

---

## Step 2 : If ✅ INSTALLED

Continue with user request normally. Skills available implicitly.

All 11 skills ready for implicit invocation:
- A2, A3, A4, B2, B4, B5, B6
- B3 (distractors generator/audit/optimizer)
- token-optimization

Proceed with work.

---

## Step 3 : If ❌ NOT INSTALLED

Display to user:

```
⚠️ PLUGIN NOT DETECTED

Quick setup (2 min):
1. Claude Code → Settings ⚙️
2. Plugins → Add Custom Plugin
3. Paste: C:\Users\Laurent\Desktop\site quiz\TRAVAIL EN COURS\quiz-core-lab\SKILLS
4. Save

After install, I'll verify + continue.

Done ?
```

Wait for user confirmation.

After user installs:
- Re-verify plugin (test token-optimization again)
- Confirm ✅ "Plugin loaded, ready to work"
- Proceed normally

---

## Why This Matters

Once plugin is installed, **NO MORE MANUAL INVOCATION NEEDED.**

I automatically use the right skill based on context + triggers.

---

**Execute this at session start.**
**Ensure user has zero friction on next session.**

