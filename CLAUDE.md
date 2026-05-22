# CLAUDE.md — quiz-core-lab

## HOOK DE DÉMARRAGE OBLIGATOIRE

À chaque ouverture de session, exécuter dans l'ordre :

```bash
# 0. Contexte Git — source de vérité runtime minimale
git log -1 --stat --oneline
git branch --show-current
git status --short
```

**Règles de réponse :**

| Résultat | Action |
|----------|--------|
| Erreur quelconque | Signaler et continuer |
| Git : fichiers modifiés détectés | Lire les fichiers listés avant toute analyse ou action |
| Git : commits récents détectés | Signaler le dernier commit et ses fichiers modifiés |

> `sync_glossaire.py` — désactivé du hook. Appel manuel si glossaire modifié.
> `check_dashboard.py` — désactivé du hook. `generate_dashboards.py` en déclenchement manuel uniquement.

Ce hook ne bloque jamais le démarrage. Temps estimé : < 5 secondes si no-op.

## HOOK GIT — TÂCHES SENSIBLES

Avant toute tâche de type : refactor / migration / réparation / synchronisation / génération structure / reprise de session — exécuter :

```bash
git log -1 --stat --oneline
git status --short
```

Contraintes : sortie compacte uniquement. Jamais de log long. Jamais de diff complet.

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

## TOKEN ECONOMY — RÈGLE ACTIVE

- Lexique runtime central : `_FACTORY/_STANDARDS/_GLOBAL/FACTORY_RUNTIME_LEXICON.md`
- Protocole machine-first : `_FACTORY/_STANDARDS/_GLOBAL/TOKEN_ECONOMY_RUNTIME_PROTOCOL.md`
- Audit : `python _FACTORY/_SCRIPTS/audit_token_economy.py`

Règle: ne pas dupliquer les taxonomies runtime hors lexique. Préférer tags fermés, états machine, colonnes courtes.
MAYENNE est la ligne prototype pour remodeler les étapes FACTORY.
