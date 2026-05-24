# CLAUDE.md — quiz-core-lab

## HOOK DE DÉMARRAGE OBLIGATOIRE

À chaque ouverture de session, exécuter dans l'ordre :

```bash
# 0. Git — état runtime
git log -1 --stat --oneline
git branch --show-current
git status --short
```

**Règles de réponse git :**

| Résultat | Action |
|----------|--------|
| Erreur quelconque | Signaler et continuer |
| Fichiers modifiés détectés | Lire les fichiers listés avant toute analyse ou action |
| Commits récents détectés | Signaler le dernier commit et ses fichiers modifiés |

**L0 Bootstrap — charger après git (TOKEN_ECONOMY_RUNTIME_PROTOCOL.md) :**

```
1. Lire : _FACTORY/_DOCS/MASTER_ARCHITECTURE.md
2. Lire : _FACTORY/_STANDARDS/_GLOBAL/FACTORY_RUNTIME_LEXICON.md
3. Si ligne active identifiée → Lire : _FACTORY/_LIGNES/[THEME]/CONFIG.yaml
```

> `sync_glossaire.py` — désactivé. Appel manuel si glossaire modifié.

Ce hook ne bloque jamais le démarrage. Temps estimé : < 10 secondes.

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
Pipeline V2.1 actif depuis 2026-05-24.
Référence : _FACTORY/_DOCS/PIPELINE_V2.md

Artefact par ligne : dossier _LIGNES/[THEME]/ — fichiers TSV source de vérité machine + CONFIG.yaml
Vue humaine xlsx : générée à la demande via `python _FACTORY/_SCRIPTS/generate_xlsx_view.py`
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
- Protocole machine-first + couches L0/L1/L2/L3 : `_FACTORY/_STANDARDS/_GLOBAL/TOKEN_ECONOMY_RUNTIME_PROTOCOL.md`
- Politique langue runtime/joueur : `_FACTORY/_DOCS/RUNTIME_EN_FR_OUTPUT_POLICY.md`
- Audit : `python _FACTORY/_SCRIPTS/audit_token_economy.py`

Règles :
- Ne pas dupliquer les taxonomies runtime hors lexique
- Préférer tags fermés, états machine, colonnes courtes
- Charger uniquement les TSV de la phase active (TSV LOADING RULE — TOKEN_ECONOMY_RUNTIME_PROTOCOL.md)
- Template validé avant toute production ligne
