# CLAUDE.md — quiz-core-lab

## HOOK DE DÉMARRAGE OBLIGATOIRE

À chaque ouverture de session, exécuter dans l'ordre :

```bash
# 1. Sync glossaire
python _FACTORY/_SCRIPTS/sync_glossaire.py --lignes

# 2. Check dashboards
python _FACTORY/_SCRIPTS/check_dashboard.py
```

**Règles de réponse :**

| Résultat | Action |
|----------|--------|
| `OK GLOSSAIRE SYNC -- no-op` | Silencieux |
| `SYNC GLOSSAIRE -- glossaire modifié` | Signaler : "Glossaire synchronisé sur N xlsx" |
| `NO_OP` (dashboards) | Silencieux |
| `REFRESH_NEEDED` (dashboards) | Exécuter `python _FACTORY/_SCRIPTS/generate_dashboards.py` puis appeler update_artifact sur factory-dashboard avec le fichier `_FACTORY/_STATE/.dashboard_factory_main.html` |
| Erreur quelconque | Signaler et continuer |

Ce hook ne bloque jamais le démarrage. Temps estimé : < 5 secondes si no-op.

---

## CONTEXTE PROJET

Factory de production de quiz QCM mobile (20 questions, 90 secondes, rejouable).
Pipeline V2 actif depuis 2026-05-18.
Référence : _FACTORY/_DOCS/PIPELINE_V2.md

Artefact central par ligne : xlsx par étape (A2→A3→A4→B2→B3→B5→EXPORT)
Source de vérité glossaire : _FACTORY/_STANDARDS/_GLOBAL/glossaire_documentaire_factory.md
Retours d'expérience : _FACTORY/B6_RETOURS/B6_RETOURS_FACTORY.md

---

## RÈGLES DE COMPORTEMENT

- Ne jamais générer de contenu sans validation humaine explicite
- Signaler toute incohérence entre fichiers du projet
- Toute difficulté ou friction détectée → consigner dans B6_RETOURS_FACTORY.md
- Gate humaine obligatoire entre chaque étape du pipeline
- Planifier avant d'agir si la planification n'est pas fournie
