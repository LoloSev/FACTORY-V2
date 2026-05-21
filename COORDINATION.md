# COORDINATION FACTORY-V2

**Source unique de vérité : GitHub**

GitHub est le point central où Claude, GPT et Laurent travaillent ensemble. Plus de zips, plus de copier-coller.

---

## 🎯 RÔLES

| Acteur | Accès | Tâches |
|--------|-------|--------|
| **Claude** | Direct (git, CLI) | Implémentation, refactoring, automation |
| **GPT** | Lecture (GitHub web) | Analyse, suggestions, validation conceptuelle |
| **Laurent (toi)** | GitHub Desktop + Web | Coordination, validation, décisions |

---

## 📊 WORKFLOW COLLABORATIF

### Phase 1 : DÉFINITION (Discussions/Issues)
```
1. Laurent crée une Issue ou Discussion
   └─ Décrit le problème/feature
   └─ Tag: #question, #refactoring, #feature

2. Claude analyse
   └─ Pose des questions
   └─ Propose une approche

3. GPT lit et commente
   └─ Validation conceptuelle
   └─ Suggestions alternatives

4. Laurent valide
   └─ Approve/Reject
   └─ ✅ Go → Phase 2
```

### Phase 2 : IMPLÉMENTATION (Branches + Commits)
```
1. Claude crée une branche
   └─ Nommage: feature/nom-court ou fix/nom-court
   └─ Ex: feature/pool-optimizer, fix/glossaire-sync

2. Claude développe
   └─ Commits clairs et atomiques
   └─ Références l'Issue (#123)

3. GPT suit via GitHub
   └─ Lit les commits
   └─ Commente si besoin (via Issues)

4. Laurent vérifie (GitHub Desktop)
   └─ Voit les changements en local
   └─ Test si nécessaire

5. Claude fait un Pull Request
   └─ Description claire
   └─ Lien vers l'Issue
   └─ Prêt à merger
```

### Phase 3 : VALIDATION & MERGE
```
1. Laurent revoit la PR
   └─ Approuve sur GitHub

2. Claude merge sur master
   └─ Commit de merge tracé

3. Laurent pull en local
   └─ GitHub Desktop → Pull origin
   └─ Code à jour localement
```

---

## 📝 TYPES D'ISSUES

### 🐛 Bug Report
```
Title: [BUG] Brève description
Labels: bug, priority-high/medium/low

Body:
- Description du problème
- Fichier affecté
- Étape pour reproduire
- Résultat attendu vs actuel
```

### ✨ Feature Request
```
Title: [FEATURE] Brève description
Labels: feature, priority-high/medium/low

Body:
- Objectif
- Bénéfice
- Fichiers/modules impactés
- Approche proposée (optionnel)
```

### 🔧 Refactoring
```
Title: [REFACTOR] Brève description
Labels: refactoring, technical-debt

Body:
- Raison du refactoring
- Scope (fichiers, modules)
- Risques
- Plan de test
```

### ❓ Question/Discussion
```
Title: [QUESTION] Brève description
Labels: question, discussion

Body:
- Contexte
- La question
- Options envisagées
```

---

## 🌿 STRATÉGIE DE BRANCHES

```
master (production)
  ├─ feature/nom-feature (Claude développe)
  ├─ fix/nom-bug (Claude corrige)
  ├─ refactor/nom-refactor (Claude refactorise)
  └─ docs/nom-doc (Documentation)

Règles:
- 1 branche = 1 Issue
- Nommage: type/issue-num-slug (ex: feature/123-pool-optimizer)
- Pull Request obligatoire avant merge
- Pas de push direct sur master
```

---

## 🔄 SYNCHRONISATION

### Claude travaille localement
```bash
# Récupère les derniers changements depuis GitHub
git pull origin master

# Crée une branche pour la feature/fix
git checkout -b feature/nom

# Développe...
git commit -m "message clair"

# Push vers GitHub
git push -u origin feature/nom

# Crée une PR sur GitHub
```

### GPT suit via GitHub
```
- Lit les commits en temps réel
- Commente les PRs
- Suggère des améliorations
- Valide la logique
```

### Laurent synchronise
```
GitHub Desktop:
1. "Fetch origin" (voir les nouveautés)
2. Lire les Issues/PRs
3. Approuver/demander changements
4. "Pull origin" après merge
```

---

## 📋 CHECKLIST ISSUE

Avant de créer une Issue :
- [ ] Le problème est clair
- [ ] C'est dans le scope FACTORY-V2
- [ ] Pas de doublon avec une Issue existante
- [ ] Titre concis avec [TYPE]
- [ ] Description complète (Contexte + Problème + Solution proposée)

Avant de créer une PR :
- [ ] Issue liée (#num)
- [ ] Branche à jour avec master
- [ ] Code conforme aux standards du projet
- [ ] Commits explicites avec références Issues
- [ ] Tests locaux OK (si applicable)
- [ ] Description claire de la PR

Avant de merger :
- [ ] Laurent a approuvé
- [ ] Pas de conflits
- [ ] Branche à jour avec master
- [ ] Status checks OK

---

## 🚨 RÈGLES IMMUABLES

1. **GitHub = Source unique**
   - Jamais de zips, jamais de copier-coller
   - Tout passe par git

2. **Traçabilité complète**
   - Chaque changement → Commit + PR + Issue
   - Historique intégral

3. **Pas de chaos**
   - Issues bien catégorisées
   - Branches nettoyées après merge
   - Master toujours stable

4. **Validation avant merge**
   - Laurent valide toujours
   - GPT commente si doutes
   - Claude implémente

5. **Communication claire**
   - Issues pour les décisions
   - Commits pour le détail technique
   - PRs pour la revue

---

## 📌 EXEMPLE DE CYCLE COMPLET

**Jour 1 : Laurent crée une Issue**
```
Title: [FEATURE] Optimizer de pools CDM

Labels: feature, priority-high

Description:
- Objectif: Améliorer équilibrage Q/R dans pools CDM
- Fichiers: _FACTORY/_LIGNES/_CDM/A4_POOLS/
- Approche: Script Python pour détection collisions
```

**Jour 1 soir : Claude répond**
```
Commentaire:
"J'ai compris l'objectif. Avant de coder, besoin de:
1. Définition précise de 'collision' ?
2. Threshold de similarité ?
3. Fallback si pas de solution ?"
```

**Jour 2 : GPT commente**
```
Commentaire:
"Suggestion: Ajouter scoring de qualité distracteur
pour prioriser les meilleurs replacements"
```

**Jour 2 après-midi : Laurent valide**
```
Commentaire:
"✅ Approuve la spec. Claude go for feature/cdm-pool-optimizer"
```

**Jour 3 : Claude crée la branche et développe**
```
git checkout -b feature/123-cdm-pool-optimizer
# ... coding ...
git push -u origin feature/123-cdm-pool-optimizer
# Crée PR sur GitHub
```

**Jour 4 : PR review**
```
GPT lit la PR et commente
Laurent approuve
Claude merge sur master
Laurent pull en local
```

---

## 📞 QUESTIONS ?

- Claude a une question → Commente dans l'Issue
- GPT a une remarque → Commente dans la PR
- Laurent doit décider → Approuve/Reject avec justification

**Tout sur GitHub. Rien ailleurs.**
