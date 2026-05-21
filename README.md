# FACTORY-V2 — Quiz QCM Advanced Refactor

Factory de production de quiz QCM mobile (20 questions, 90s, rejouable).

**Travail collaboratif : Claude + GPT + Laurent via GitHub**

---

## 📌 IMPORTANT

- **Source unique** : GitHub
- **Pas de zips, pas de copier-coller**
- **Tout passe par Issues → PR → Merge**
- **Lire [COORDINATION.md](./COORDINATION.md) d'abord**

---

## 🎯 Quick Start

### Pour Laurent (Coordination)
```bash
# 1. Voir les nouvelles issues
github.com/LoloSev/FACTORY-V2/issues

# 2. Valider une PR
github.com/LoloSev/FACTORY-V2/pulls

# 3. Synchroniser localement (GitHub Desktop)
Pull origin → Voir les changements
```

### Pour Claude (Implémentation)
```bash
# 1. Voir les issues assignées
git log --oneline

# 2. Créer une branche
git checkout -b feature/nom

# 3. Développer et pousser
git push -u origin feature/nom

# 4. Créer une PR sur GitHub
```

### Pour GPT (Validation)
```
1. Lire l'Issue sur GitHub
   → Comprendre l'objectif

2. Lire la PR quand elle arrive
   → Commenter si doutes

3. Valider le merge
   → Approuver ou suggérer changements
```

---

## 📂 Structure du Projet

```
FACTORY-V2/
├── CLAUDE.md              ← Instructions pour Claude (hooks, règles)
├── COORDINATION.md        ← Workflow collaboratif (À LIRE!)
├── README.md              ← Ce fichier
│
├── SKILLS/                ← Custom skills pour Claude Code
│   └── [skill-1, skill-2, ...]
│
├── _FACTORY/              ← Cœur de la factory
│   ├── METHODES/          ← Processus (A1, A2, A3, A4, B2, B3, B5)
│   ├── _LIGNES/           ← Lignes (CDM, Mayenne, Rap, Internet, Rock, Séries)
│   ├── _STANDARDS/        ← Standards de qualité
│   ├── _DOCS/             ← Documentation
│   ├── _SCRIPTS/          ← Scripts Python pour l'automation
│   ├── B6_RETOURS/        ← Retours d'expérience
│   ├── _RETEX_LIBRARY/    ← Analyses rétrospectives
│   └── _STATE/            ← État/dashboards
│
└── arbo.txt               ← Arborescence complète
```

---

## 🔄 Workflow Collaboratif

```
Laurent crée Issue
      ↓
Claude + GPT analysent
      ↓
Laurent valide approche
      ↓
Claude crée branche & développe
      ↓
GPT commente la PR
      ↓
Laurent approuve PR
      ↓
Claude merge sur master
      ↓
Laurent pull localement (GitHub Desktop)
```

**Chaque étape = Traçabilité complète sur GitHub**

---

## 🚀 Phases du Projet

### Phase 1 : RESTRUCTURATION (En cours)
- [ ] Refonte architecture pipeline
- [ ] Standardisation scripts
- [ ] Documentation complète
- [ ] Dashboards améliorés

### Phase 2 : OPTIMISATION
- [ ] Performance des scripts
- [ ] Token economy (Claude + GPT)
- [ ] Automation avancée

### Phase 3 : DÉPLOIEMENT
- [ ] Intégration quiz UI
- [ ] Sync avec site-quiz
- [ ] Production ready

---

## 📋 ISSUES & DISCUSSIONS

### Pour créer une Issue
```
1. Titre: [TYPE] Brève description
   Types: BUG, FEATURE, REFACTOR, QUESTION

2. Labels: 
   - bug / feature / refactoring / question
   - priority-high / priority-medium / priority-low
   - phase-restructuration / phase-optimisation

3. Description complète avec contexte
```

### Pour commenter une PR
```
1. Claude → Laurent : "Prêt à merger"
2. GPT → PR : Commentaires techniques
3. Laurent → PR : ✅ Approve or ❌ Request Changes
```

---

## 🔗 Ressources

| Fichier | Contenu |
|---------|---------|
| [COORDINATION.md](./COORDINATION.md) | Workflow complet (Claude + GPT + Laurent) |
| [CLAUDE.md](./CLAUDE.md) | Instructions pour Claude (hooks, règles) |
| [_FACTORY/_DOCS/PIPELINE_V2.md](./FACTORY/_DOCS/PIPELINE_V2.md) | Architecture du pipeline |
| [_FACTORY/_RETEX_LIBRARY/](./FACTORY/_RETEX_LIBRARY/) | Analyses et apprentissages |
| [_FACTORY/B6_RETOURS/](./FACTORY/B6_RETOURS/) | Friction log & retours |

---

## 💬 Communication

- **Issues** = Décisions, specs, problèmes
- **PRs** = Code review et validation
- **Commits** = Historique détaillé des changements
- **Discussions** = Questions architecturales

**Rien en dehors de GitHub. Tout est tracé.**

---

## ✅ Checklist Démarrage

- [ ] Lire COORDINATION.md
- [ ] Créer première Issue de refonte
- [ ] Claude prend la branche feature
- [ ] GPT valide l'approche
- [ ] Laurent approuve PR
- [ ] Merge et sync locale

**GO FACTORY-V2! 🚀**
