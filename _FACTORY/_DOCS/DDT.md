# DDT — DÉPLOIEMENT, DÉPENDANCES, TECHNIQUE

DEPENDENCY:
- MASTER_ARCHITECTURE.md
- PIPELINE_V2.md
- glossaire_documentaire_factory.md
**Mis à jour :** 12/05/2026

---

## 🌐 Site live

| Info | Valeur |
|---|---|
| URL | `quizzzz-de-lolo.netlify.app` |
| Hébergement | Netlify |
| Compte Netlify | `laurent-baudouin` (laurent.baudouin@gmail.com) |
| Déploiement | CLI Netlify (`netlify deploy`) |
| Analytics | Google Analytics — ID : `G-GZHLYBP79J` |

---

## 🐙 GitHub

| Info | Valeur |
|---|---|
| Repo | `github.com/LoloSev/quizz-Mayenne` |
| Usage | QUIZZZ FACTORY Mayenne |
| Compte | `LoloSev` |

> ⚠️ Le repo GitHub ne contient PAS le code du site complet. Le site est déployé via CLI depuis le dossier local.

---

## 📁 Source locale

```
C:\Users\Laurent\Desktop\site quiz\
```

Source de vérité du site live. Tout déploiement part de là.

---

## 🚀 Procédure de déploiement

```bash
netlify deploy --prod
```

> Compte : `laurent-baudouin` — PAS `ouathealth`.

---

## 🗂️ État des quiz

| Quiz | HTML | Questions | Stock actuel | Cible |
|---|---|---|---|---|
| 🎸 Rock | ✅ | `QUESTIONS_ROCK.txt` | à auditer | 277 |
| 🎤 Rap | ✅ | `QUESTIONS_RAP.txt` | à auditer | 277 |
| ⚽ CDM | ✅ | `QUESTIONS_CDM.txt` | à auditer | 277 |
| 🏞️ Mayenne | ✅ | `QUESTIONS_MAYENNE.txt` | 4/277 (ODS) | 277 |
| 💻 Internet | ✅ | `QUESTIONS_INTERNET.txt` | à auditer | 277 |
| 📺 Séries | 🔄 | `QUESTIONS_SERIES.txt` | 50 brutes | 277 |

---

## 🏗️ Architecture technique

### Stack

- **Frontend** : HTML / CSS / JavaScript vanilla
- **Styles** : `theme.css` par quiz + styles inline
- **Sons** : MP3 par thème (`sounds/`) + sons feedback partagés
- **Données** : questions dans les fichiers HTML (pas de JSON externe — pour l'instant)

### Structure d'un quiz

```
quiz-[thème]/
├── QUIZ_[THÈME].html    # Tout-en-un : logique + questions + styles
├── theme.css            # Couleurs et identité visuelle
└── avatar-lolo-[thème].png
```

### Google Analytics

Installé sur 6 fichiers HTML :
- `index.html`
- `quiz-cdm/QUIZ_CDM.html`
- `quiz-rap/QUIZ_RAP.html`
- `quiz-rock/QUIZ_ROCK.html`
- `quiz-mayenne/QUIZ_MAYENNE.html`
- `quiz-internet/QUIZ_INTERNET.html`

> ⚠️ À ajouter sur `quiz-series/QUIZ_SERIES.html` lors de l'intégration.

---

## 🏭 QUIZZZ FACTORY

→ Voir `_FACTORY/_DOCS/MASTER_ARCHITECTURE.md`

---

## 🔧 Backlog technique

- [ ] Intégrer quiz Séries (HTML + questions + GA)
- [ ] Étoffer stocks Rock, Rap, CDM, Internet à 277 questions (via FACTORY + xlsx)
- [ ] Auditer stocks existants
- [ ] Compléter pools xlsx Mayenne avec les 300 questions brutes (MDE B5)
- [ ] Créer xlsx pour les autres thèmes (MDE A4→A5)
