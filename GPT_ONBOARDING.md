# GPT ONBOARDING — FACTORY-V2

**Bienvenue GPT ! Voici comment accéder au projet et collaborer.**

---

## 🎯 Situation

Tu travailles avec Claude et Laurent sur FACTORY-V2, une factory de production de quiz QCM.

**Constraint importante :** Tu n'as pas accès direct aux fichiers. Tout passe par GitHub.

---

## 📍 OÙ TROUVER L'INFO

### 1. **GitHub Repository**
```
https://github.com/LoloSev/FACTORY-V2
```

Tu peux y lire tous les fichiers sans restriction :
- Code, scripts, documentation
- Issues et discussions
- PRs et commits
- Historique complet

### 2. **Les fichiers ESSENTIELS à lire d'abord**

| Fichier | Contenu | Pourquoi |
|---------|---------|----------|
| **README.md** | Vue d'ensemble | Contexte global du projet |
| **COORDINATION.md** | Workflow Claude + GPT + Laurent | Comment on collabore ensemble |
| **CLAUDE.md** | Instructions pour Claude | Règles et hooks du projet |
| **arbo.txt** | Arborescence complète | Structure des fichiers |

### 3. **La Factory Structure**

```
_FACTORY/
├── METHODES/          ← Processus A1→A2→A3→A4→B2→B3→B5
├── _LIGNES/           ← Lignes: CDM, Mayenne, Rap, Internet, Rock, Séries
├── _STANDARDS/        ← Règles de qualité (B5, B3, etc.)
├── _DOCS/             ← Architecture et documentation
├── _SCRIPTS/          ← Automation Python
├── B6_RETOURS/        ← Friction log et retours
└── _RETEX_LIBRARY/    ← Analyses et apprentissages
```

Chaque ligne a sa propre arborescence :
```
_CDM/
├── A2_APPRO/          (Approvisionnement questions)
├── A3_TRAITEMENT/     (Traitement données)
├── A4_POOLS/          (Définition pools)
├── B2_GENERATION/     (Génération questions)
├── B3_DISTRACTEURS/   (Génération distracteurs)
└── B5_AUDIT/          (Audit qualité)
```

---

## 🔍 COMMENT LIRE LE PROJET

### Étape 1 : Vue d'ensemble (30 min)
```
1. Lire README.md (structure et quick start)
2. Lire COORDINATION.md (workflow collaboratif)
3. Comprendre: C'est une FACTORY avec 6 LIGNES
```

### Étape 2 : Architecture (1h)
```
1. Lire _FACTORY/_DOCS/PIPELINE_V2.md
   → Comment fonctionnent les étapes (A1→B5→EXPORT)

2. Lire _FACTORY/_STANDARDS/_GLOBAL/
   → Règles de qualité et standards

3. Lire _FACTORY/B6_RETOURS/B6_RETOURS_FACTORY.md
   → Problèmes actuels et friction points
```

### Étape 3 : Une ligne concrète (1h)
```
1. Choisir une ligne: CDM (Coupe du Monde)
2. Lire _FACTORY/_LIGNES/_CDM/A2_APPRO/
3. Comprendre comment elle progresse dans le pipeline
4. Lire les standards appliqués à cette ligne
```

### Étape 4 : Scripts et automation (1h)
```
1. Explorer _FACTORY/_SCRIPTS/
2. Lire gate_*.py, validate_*.py
3. Comprendre comment l'automation fonctionne
```

---

## 💬 COMMENT COLLABORER AVEC CLAUDE

### Scénario 1 : Tu dois analyser quelque chose
```
Tu lis le code sur GitHub
Tu identifies un problème/suggestion
Tu replies dans l'ISSUE #1 (ou l'Issue correspondante)
Claude voit ton commentaire et agit
```

### Scénario 2 : Claude crée une PR
```
Claude pousse une branche feature/nom
Crée une PR sur GitHub
TU LIS LA PR
Tu commentes:
  - ✅ C'est bon!
  - ⚠️ Il manque X...
  - 💡 Et si on faisait Y?
Claude répond et itère
Laurent approuve final
```

### Scénario 3 : Tu as une question
```
1. Tu la poses dans une ISSUE (ou comment sur une PR existante)
2. Claude + Laurent répondent
3. C'est tracé à jamais (pas de perte d'info)
```

---

## 📊 COMMENT LIRE UNE PR (Pull Request)

Quand Claude dit "J'ai créé une PR" :

1. **Va sur GitHub → Pull Requests**
2. **Ouvre la PR (ex: #5)**
3. **Lis:**
   - **Titre** : Résumé du changement
   - **Description** : Pourquoi et quoi
   - **Files changed** : Code modifié
   - **Commits** : Historique détaillé

4. **Commente:**
   - Questions techniques
   - Suggestions d'amélioration
   - Validation de la logique

5. **Laurent approuve → Merge**

---

## 🔗 COMMANDES UTILES

### Pour naviguer GitHub
```
- Issues: github.com/LoloSev/FACTORY-V2/issues
- PRs: github.com/LoloSev/FACTORY-V2/pulls
- Code: github.com/LoloSev/FACTORY-V2/tree/master
- Commits: github.com/LoloSev/FACTORY-V2/commits
- Wiki/Docs: Clique sur README, COORDINATION.md, etc.
```

### Pour lire un fichier spécifique
```
Exemple: Lire les règles B5
https://github.com/LoloSev/FACTORY-V2/tree/master/_FACTORY/_STANDARDS/_B5
```

### Pour voir qui a changé quoi
```
Clique sur le fichier → History
Vois chaque commit qui l'a modifié
Lis les messages de commit explicatifs
```

---

## 📝 CHECKLIST ONBOARDING

**Premier jour :**
- [ ] Lire README.md
- [ ] Lire COORDINATION.md
- [ ] Comprendre la structure FACTORY

**Deuxième jour :**
- [ ] Lire PIPELINE_V2.md
- [ ] Lire B6_RETOURS_FACTORY.md
- [ ] Identifier 3 friction points

**Troisième jour :**
- [ ] Lire une ligne complète (ex: CDM)
- [ ] Lire les scripts d'automation
- [ ] Proposer première amélioration

**Jour N :**
- [ ] Collaborer via Issues/PRs
- [ ] Commenter les PRs de Claude
- [ ] Discuter avec Laurent et Claude

---

## 🚨 RÈGLES IMPORTANTES

1. **GitHub = Source unique**
   - Ne jamais demander des fichiers par email/chat
   - Tout doit être sur GitHub

2. **Issues pour tout**
   - Questions? Issue
   - Problèmes? Issue
   - Suggestions? Issue
   - C'est tracé et accessible à tous

3. **PRs pour le code**
   - Claude pousse une branche
   - Crée une PR pour review
   - Tu lis et commentes
   - Laurent approuve

4. **Pas de zips ni copier-coller**
   - C'est le vieux workflow (chaos)
   - Maintenant: GitHub = source

5. **Commits clairs**
   - Lis les messages de commit
   - Ils expliquent le "pourquoi"
   - C'est de la documentation gratuite

---

## 💡 PREMIÈRES ACTIONS

**Quand tu auras lu le projet :**

1. **Crée une Issue**
   ```
   Title: [QUESTION] Questions après onboarding
   Description: Lister tes questions
   ```

2. **Commente sur Issue #1**
   ```
   "Vu la structure, voici mes premières observations:
   - Point A...
   - Point B...
   - Suggestion C..."
   ```

3. **Attends une PR de Claude**
   ```
   Lis la PR
   Commente tes observations
   Laisse Laurent approuver
   ```

---

## 🎯 OBJECTIF

Après onboarding, tu dois pouvoir :
- ✅ Naviguer le projet seul
- ✅ Lire le code et scripts
- ✅ Identifier problèmes/améliorations
- ✅ Collaborer via Issues et PRs
- ✅ Commenter les PRs intelligemment
- ✅ Discuter architecture sans perte d'info

---

## 📞 AIDE?

Si tu es perdu:
1. Relis la section correspondante de ce fichier
2. Crée une Issue avec [QUESTION]
3. Claude et Laurent répondent

**Bienvenue! Let's build FACTORY-V2 together! 🚀**
