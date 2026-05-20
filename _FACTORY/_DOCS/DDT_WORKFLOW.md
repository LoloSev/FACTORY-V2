# DDT_WORKFLOW — RÈGLES DE TRAVAIL

DEPENDENCY:
- MASTER_ARCHITECTURE.md
- PIPELINE_V2.md
- glossaire_documentaire_factory.md
**Mis à jour :** 12/05/2026

---

## 🚀 Démarrage d'une session

### Instruction de démarrage (à copier-coller)

```
Lis START.txt, DDT.md et MASTER_ARCHITECTURE.md (dans _FACTORY/) puis attends mes instructions.
```

### Pour une tâche spécifique

```
Lis START.txt, DDT.md et MASTER_ARCHITECTURE.md (dans _FACTORY/).
Aujourd'hui : [TÂCHE PRÉCISE]
Confirme ce que tu as compris avant de commencer.
```

---

## 🤝 Répartition Claude / ChatGPT

| Tâche | Outil |
|---|---|
| Documentation, organisation, code site | **Claude (Cowork)** |
| Génération questions, audit, distracteurs | **Claude (Cowork)** |
| Production avatars et visuels | **ChatGPT** |
| Génération questions si tokens Claude épuisés | **ChatGPT** |

---

## 📋 Règles absolues de travail avec l'IA

- Répondre uniquement à la demande exacte
- Produire directement le résultat final attendu
- Format clair, compact et exploitable immédiatement
- Travailler pool par pool, étape par étape — jamais globalement
- Toujours attendre validation humaine avant de passer à l'étape suivante
- Checkpoint tous les 10 actions
- Stop à 85% tokens (signaler avant)
- Sauvegarde avant toute action irréversible

---

## 🏭 Workflow QUIZZZ FACTORY

### Étapes de production (dans l'ordre)

```
1. Construction base connaissances
2. Génération brute ciblée (par pool)
3. Audit individuel des questions
4. Classement par difficulté
5. Audit diversité géographique/thématique
6. Génération distracteurs (question par question)
7. Audit final du stock complet
8. Construction finale du quiz
```

### Règle d'or

```
Ne jamais demander : "Génère 500 questions complètes avec distracteurs."
Toujours travailler : pool par pool, étape par étape.
```

### Calc = vérité maître

Toutes les modifications définitives se font dans le fichier ODS.
L'IA propose, l'humain valide et saisit dans Calc.

---

## 🎯 Exemples de tâches courantes

### Génération questions

```
Génère 20 questions brutes pour le pool QV-03 (nature/tourisme Mayenne) :
- sans distracteurs
- diversité géographique
- lecture mobile rapide
```

### Audit d'un pool

```
Audite le pool QV-03 : trop de Laval ? trop de rivières ?
Propose les ajustements.
```

### Intégration nouveau quiz

```
Crée l'architecture complète pour le quiz SÉRIES :
- HTML depuis QUIZ_TEMPLATE.html
- theme.css
- intégration Google Analytics (ID: G-GZHLYBP79J)
```

### Déploiement

```
Vérifie que tous les liens fonctionnent dans index.html.
Liste les fichiers modifiés prêts pour netlify deploy.
```

---

## ⚠️ Règles critiques

- **Distracteurs fictifs** → validation humaine obligatoire, jamais auto-validés par l'IA
- **Modifications ODS** → toujours tracer AVANT / APRÈS / RAISON
- **Déploiement** → toujours depuis `C:\Users\Laurent\Desktop\site quiz\` via compte `laurent-baudouin`
- **GitHub** → repo `LoloSev/quizz-Mayenne` = FACTORY Mayenne uniquement, pas le site complet

---

## 📂 Localisation projet

```
Local  : C:\Users\Laurent\Desktop\site quiz\
Live   : quizzzz-de-lolo.netlify.app
GitHub : github.com/LoloSev/quizz-Mayenne
```
