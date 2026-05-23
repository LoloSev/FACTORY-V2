# DDT_WORKFLOW — RÈGLES DE TRAVAIL

DEPENDENCY:
- MASTER_ARCHITECTURE.md
- PIPELINE_V2.md
- TOKEN_ECONOMY_RUNTIME_PROTOCOL.md
**Mis à jour :** 2026-05-24

---

## Démarrage d'une session

**Cowork mode (normal) :** le hook CLAUDE.md gère le bootstrap automatiquement.

**Autre outil (Claude.ai web, API) :** copier-coller `START.txt` en ouverture de session.

---

## Répartition Claude / ChatGPT

| Tâche | Outil |
|---|---|
| Documentation, organisation, code site | Claude (Cowork) |
| Génération questions, audit, distracteurs | Claude (Cowork) |
| Production avatars et visuels | ChatGPT |

---

## Règles absolues de travail avec l'IA

- Répondre uniquement à la demande exacte
- Produire directement le résultat final attendu
- Format clair, compact et exploitable immédiatement
- Travailler pool par pool, étape par étape — jamais globalement
- Toujours attendre validation humaine avant de passer à l'étape suivante
- Gate humaine obligatoire entre chaque étape du pipeline

---

## Workflow QUIZZZ FACTORY V2

Pipeline : A1 → A2 → A3 → A4 → B2 → B3 → B5 → EXPORT
Référence complète : PIPELINE_V2.md

Artefact unique par ligne : QUIZ_[THEME].xlsx (8 feuilles enrichies progressivement).

Règle d'or : travailler pool par pool, jamais globalement.

---

## Exemples de tâches courantes

### Génération questions (B2)

```
Phase B2 — pool QV-03 — CIBLE_NIVEAU N2
Ligne : _[THEME]
Générer 15 questions. Feuille QUESTIONS du xlsx.
```

### Audit d'un pool (B5)

```
Phase B5 — auditer pool QV-03
Ligne : _[THEME]
Question par question. Attendre validation avant la suivante.
```

### Intégration nouveau quiz (site)

```
Créer l'architecture pour le quiz [THEME] :
- HTML depuis QUIZ_TEMPLATE.html
- theme.css
- Google Analytics ID: G-GZHLYBP79J
```

### Déploiement

```
Vérifier les liens dans index.html.
Lister les fichiers modifiés pour : netlify deploy --prod
```

---

## Règles critiques

- Distracteurs : validation humaine obligatoire, jamais auto-validés
- Modifications xlsx : toujours tracer dans PROCESS_[THEME].md si non trivial
- Déploiement : depuis `C:\Users\Laurent\Desktop\site quiz\` — compte `laurent-baudouin`
- GitHub : repo `LoloSev/quizz-Mayenne` = archive Mayenne uniquement, pas le site complet

---

## Localisation projet

```
Local  : C:\Users\Laurent\Desktop\site quiz\
Live   : quizzzz-de-lolo.netlify.app
GitHub : github.com/LoloSev/quizz-Mayenne
```

---

*DDT_WORKFLOW.md — 2026-05-24*
*Remplace version 12/05/2026 : START.txt supprimé, ODS/Calc supprimés, workflow V1 remplacé par V2*
