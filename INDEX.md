# INDEX FACTORY-V2 — Guide d'accès à l'info

**Navigation rapide pour Claude, GPT et Laurent**

---

## 🎯 JE VEUX COMPRENDRE...

### "Quel est ce projet?"
→ Lire: **README.md** (2 min)

### "Comment on collabore?"
→ Lire: **COORDINATION.md** (10 min)

### "Je suis GPT, par où commencer?"
→ Lire: **GPT_ONBOARDING.md** (30 min)

### "Quel est le pipeline complet?"
→ Lire: **_FACTORY/_DOCS/PIPELINE_V2.md**

### "Quelles sont les étapes A2→B5?"
→ Lire: **_FACTORY/METHODES/** (par étape)

### "Comment fonctionne une ligne (ex: CDM)?"
→ Lire: **_FACTORY/_LIGNES/_CDM/** (arbo complète)

### "Quelles sont les règles de qualité?"
→ Lire: **_FACTORY/_STANDARDS/** (par étape)

### "Y a-t-il des problèmes connus?"
→ Lire: **_FACTORY/B6_RETOURS/B6_RETOURS_FACTORY.md**

### "Comment les scripts automatisent?"
→ Lire: **_FACTORY/_SCRIPTS/README.md** (créer si absent)

### "Que dit l'arborescence complète?"
→ Lire: **arbo.txt**

---

## 📂 ARBORESCENCE COMPLÈTE

```
FACTORY-V2/
│
├─ 📌 COORDINATION.md           (Workflow collaboratif)
├─ 📌 README.md                 (Vue d'ensemble)
├─ 📌 GPT_ONBOARDING.md         (Guide pour GPT)
├─ 📌 INDEX.md                  (Ce fichier)
├─ 📌 CLAUDE.md                 (Instructions pour Claude)
├─ 📌 arbo.txt                  (Arborescence projet)
│
├─ 📁 SKILLS/                   (Custom skills pour Claude Code)
│  ├─ .claude-plugin/
│  ├─ a2-bib-construction/      (Skill: construction biblio)
│  ├─ a3-bib-processing/        (Skill: traitement biblio)
│  ├─ a4-pools-definition/      (Skill: définition pools)
│  ├─ b2-questions-generator/   (Skill: génération Q)
│  ├─ b4-spreadsheet-implantation/ (Skill: implantation XLS)
│  ├─ b5-audit-validator/       (Skill: audit qualité)
│  ├─ b6-rules-extractor/       (Skill: extraction règles)
│  ├─ distractor-audit-statistics/
│  ├─ distractor-optimizer/
│  ├─ distractors-generator/
│  ├─ factory-conductor/
│  └─ token-optimization/
│
└─ 📁 _FACTORY/                 (Cœur de la factory)
   │
   ├─ 📁 METHODES/              (Processus par étape)
   │  ├─ A1/                    (Lignes template)
   │  ├─ A2/                    (Approvisionnement)
   │  ├─ _A2/ (archive)
   │  ├─ _A3/                   (Traitement)
   │  ├─ _A4/                   (Pools définition)
   │  ├─ _B2/                   (Questions génération)
   │  ├─ _B3/                   (Distracteurs génération)
   │  ├─ _B5/                   (Audit)
   │  └─ _GLOBAL/               (Skills globales)
   │
   ├─ 📁 _LIGNES/               (Les 6 lignes)
   │  │
   │  ├─ _CDM/                  (Coupe du Monde)
   │  │  ├─ A2_APPRO/           (Questions base)
   │  │  ├─ A3_TRAITEMENT/      (Traitement)
   │  │  ├─ A4_POOLS/           (Pools CDM)
   │  │  ├─ B2_GENERATION/      (Questions)
   │  │  ├─ B3_DISTRACTEURS/    (Distracteurs)
   │  │  └─ B5_AUDIT/           (Validation)
   │  │
   │  ├─ _MAYENNE/              (Géographie locale)
   │  │  ├─ A2_APPRO/
   │  │  ├─ A3_TRAITEMENT/
   │  │  ├─ A4_POOLS/
   │  │  ├─ B2_GENERATION/
   │  │  └─ [suite...]
   │  │
   │  ├─ _RAP/                  (Musique hip-hop)
   │  ├─ _INTERNET/             (Memes & web culture)
   │  ├─ _ROCK/                 (Musique rock)
   │  ├─ _CINEMA/               (Films et séries)
   │  └─ _TEMPLATE/             (Template de base)
   │
   ├─ 📁 _STANDARDS/            (Règles de qualité)
   │  ├─ _A4/                   (Format pools)
   │  ├─ _B2/                   (Génération Q)
   │  ├─ _B3/                   (Métriques distracteurs)
   │  └─ _B5/                   (Audit & validation)
   │
   ├─ 📁 _DOCS/                 (Documentation)
   │  ├─ PIPELINE_V2.md         (★ Architecture complète)
   │  ├─ DDT.md                 (Design Document)
   │  ├─ DDT_WORKFLOW.md        (Workflow DDT)
   │  ├─ MASTER_ARCHITECTURE.md (Architecture master)
   │  ├─ ARBORESCENCE_LIGNES.txt (Arbo lignes)
   │  ├─ AGENTS.md              (Agents/roles)
   │  └─ [autres docs]
   │
   ├─ 📁 _SCRIPTS/              (Automation Python)
   │  ├─ check_dashboard.py     (Vérifier dashboards)
   │  ├─ generate_dashboards.py (Générer dashboards)
   │  ├─ gate_*.py              (Gates par étape)
   │  ├─ validate_*.py          (Validators)
   │  ├─ sync_glossaire.py      (Sync glossaire)
   │  └─ [autres scripts]
   │
   ├─ 📁 B6_RETOURS/            (Friction log)
   │  ├─ B6_RETOURS_FACTORY.md  (★ Problèmes connus)
   │  └─ B6_REGLES_*.md         (Règles retours)
   │
   ├─ 📁 _RETEX_LIBRARY/        (Analyses)
   │  ├─ RETEX_INDEX.md         (Index analyses)
   │  └─ factory_v_2_token_economy_master_analysis.md
   │
   ├─ 📁 _STATE/                (État/dashboards)
   │  └─ [dashboards HTML]
   │
   └─ 📁 [autres répertoires]
```

---

## ⭐ FICHIERS CRITIQUES (À LIRE D'ABORD)

| Fichier | Lecture | Qui | Importance |
|---------|---------|-----|------------|
| **README.md** | 2 min | Tous | 🔴 MUST |
| **COORDINATION.md** | 10 min | Tous | 🔴 MUST |
| **GPT_ONBOARDING.md** | 30 min | GPT | 🔴 MUST |
| **CLAUDE.md** | 5 min | Claude | 🔴 MUST |
| **_DOCS/PIPELINE_V2.md** | 30 min | Tous | 🔴 MUST |
| **B6_RETOURS/B6_RETOURS_FACTORY.md** | 20 min | Tous | 🟡 IMPORTANT |
| **_STANDARDS/_GLOBAL/** | 20 min | Tous | 🟡 IMPORTANT |
| **arbo.txt** | 10 min | Tous | 🟡 IMPORTANT |

---

## 🔄 WORKFLOW LECTURE (PAR RÔLE)

### Claude (Claude Code)
```
1. CLAUDE.md              → Tes instructions & hooks
2. COORDINATION.md        → Comment collaborer
3. PIPELINE_V2.md         → Architecture pipeline
4. B6_RETOURS.md          → Problèmes actuels
5. Puis: Lire la ligne/étape sur laquelle tu travailles
```

### GPT (Lecture seule)
```
1. GPT_ONBOARDING.md      → Par où commencer
2. README.md              → Vue d'ensemble
3. COORDINATION.md        → Workflow collaboratif
4. PIPELINE_V2.md         → Architecture
5. Puis: Commenter les PRs et Issues
```

### Laurent (Coordination)
```
1. README.md              → Contexte global
2. COORDINATION.md        → Le workflow
3. PIPELINE_V2.md         → Architecture
4. B6_RETOURS.md          → Problèmes
5. Puis: Valider Issues et PRs
```

---

## 🎯 CHERCHER PAR THÈME

### "Je veux comprendre la ligne CDM"
```
1. Lire _FACTORY/_LIGNES/_CDM/A2_APPRO/
2. Puis A3_TRAITEMENT/, A4_POOLS/, etc.
3. Lire les standards appliqués (_STANDARDS/)
4. Lire les retours spécifiques (B6_RETOURS/)
```

### "Je veux optimiser les pools"
```
1. Lire _STANDARDS/_A4/STD_A4_pool_*
2. Lire _FACTORY/_SCRIPTS/gate_a4.py
3. Lire _LIGNES/*/A4_POOLS/
4. Lire B6_RETOURS sur les pools
```

### "Je veux générer des questions"
```
1. Lire METHODES/_B2/
2. Lire _STANDARDS/_B2/
3. Lire _SCRIPTS/gate_b2.py
4. Lire B6_RETOURS sur génération
```

### "Je veux comprendre les distracteurs"
```
1. Lire METHODES/_B3/
2. Lire _STANDARDS/_B3/
3. Lire _SCRIPTS/*distractor*.py
4. Lire B6_RETOURS sur distracteurs
5. Lire _RETEX_LIBRARY/
```

---

## 📋 CHECKLIST NAVIGATION

- [ ] J'ai lu README.md
- [ ] J'ai lu COORDINATION.md
- [ ] J'ai lu mon fichier de rôle (CLAUDE.md, GPT_ONBOARDING.md)
- [ ] Je comprends la structure _FACTORY/
- [ ] Je sais où trouver les standards
- [ ] Je connais les problèmes actuels (B6_RETOURS)
- [ ] Je peux naviguer GitHub seul
- [ ] Je peux lire une PR et commenter

---

## 🔗 LIENS DIRECTS (GitHub)

```
Issues:      https://github.com/LoloSev/FACTORY-V2/issues
PRs:         https://github.com/LoloSev/FACTORY-V2/pulls
Code:        https://github.com/LoloSev/FACTORY-V2/tree/master
_FACTORY:    https://github.com/LoloSev/FACTORY-V2/tree/master/_FACTORY
PIPELINE:    [Repo]/blob/master/_FACTORY/_DOCS/PIPELINE_V2.md
```

---

## 💡 TIPS

- **Commits sont tes amis** : Les messages de commit expliquent le "pourquoi"
- **Issues = traçabilité** : Tout ce qui n'est pas sur GitHub n'existe pas
- **PRs = revue collaborative** : Lis-les, commente-les, approuve-les
- **Glossaire = source de vérité** : Vérifier _STANDARDS/_GLOBAL/glossaire
- **B6_RETOURS = apprentissages** : Lire pour ne pas répéter erreurs

---

**Happy exploring! 🚀**
