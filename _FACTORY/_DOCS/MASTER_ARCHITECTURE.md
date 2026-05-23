# QUIZZZ FACTORY — MASTER ARCHITECTURE

VERSION: 6.0
DATE: 2026-05-22
STATUS: ACTIVE_REFERENCE — point d'entrée runtime

> Pipeline V2 actif depuis 2026-05-18. Référence : `_FACTORY/_DOCS/PIPELINE_V2.md`

---

## CONTEXTE PROJET

**Les Quizzzz de Lolo** — quiz culture générale thématique, mobile-friendly, rejouable. 90 secondes / 20 questions / mélange aléatoire.

| Paramètre | Valeur |
|---|---|
| Auteur | Laurent (Lolo) — ouathealth@gmail.com |
| URL live | quizzzz-de-lolo.netlify.app |
| Durée partie | 90 secondes |
| Questions/partie | 20 |
| Stock cible/quiz | 277 questions |
| Format | QCM 4 choix, 1 bonne réponse |
| Déploiement | `netlify deploy --prod` — compte laurent-baudouin |

---

## QUI FAIT QUOI

| Outil | Rôle |
|---|---|
| Claude (Cowork) | Documentation, règles, workflow, génération questions, audit, distracteurs, HTML/CSS/JS/xlsx, déploiement Netlify |
| ChatGPT | Génération avatars/images (DALL-E) |

---

## CATALOGUE DES QUIZ

| Quiz | Thème |
|---|---|
| Rock | Légendes, albums, riffs, mouvements |
| Rap | Rap français + game international |
| CDM | Histoire de la Coupe du Monde |
| Mayenne | Histoire, géo, traditions du 53 |
| Internet | Memes, plateformes, culture web |
| Séries | Séries TV françaises et internationales |
| Cinéma | Films, acteurs, réalisateurs |

---

## PHILOSOPHIE

L'objectif est de produire un système capable de générer des quiz CONSISTENCY_VALIDATED sur n'importe quel thème.

Rôle humain : architecte éditorial, valideur final, superviseur QA. Pas opérateur de saisie.

Stratégie technique : Excel → Export JSON → Site.

---

## CONSTANTES ARCHITECTURE

POOL_COUNT = 20 / STOCK_CIBLE = 277 / QCM 4 choix / 1 question tirée par pool par partie.

Distribution canonique :
```yaml
DIFFICULTY_DISTRIBUTION: { N1: 5, N2: 10, N3: 5 }
```
Source de vérité : ce fichier. Applications : STD_GLOBAL_quiz_architecture_rules.md / QUIZ_ASSEMBLY_RULES.md.

Table de dérivation pools → voir HIERARCHIE_REGLEMENTAIRE.md L-001.

---

## GOUVERNANCE

[RULE-GOV-001]
Le projet apprend à chaque quiz. L'intervention humaine (AVANT/APRÈS) est incontournable. Aucune automatisation ne substitue ce retour. Les STD sont des photographies du savoir courant, pas des lois figées.

[RULE-GOV-002]
Avant toute nouvelle règle dans un STD, 4 filtres dans l'ordre :
1. Déjà couverte ? → enrichir l'existante.
2. Généralisable multi-thèmes ? → si non, reste dans le document thématique.
3. Remplace une règle plus faible ? → substituer, ne pas empiler.
4. Observée sur ≥2 cobayes ? → si non, statut GEN_NOTE candidat, pas STD actif.

[RULE-LAB-001]
Le LAB expérimente au-dessus du socle FACTORY, jamais en dessous. Toute règle FACTORY active s'applique dans le LAB tant qu'elle n'a pas été remplacée par décision explicite.

---

## POINTEURS AUTORITATIFS

| Sujet | Fichier |
|---|---|
| Pipeline V2 | `_DOCS/PIPELINE_V2.md` |
| Arborescence V2 | `_STANDARDS/_GLOBAL/STD_GLOBAL_factory_arborescence_rules.md` |
| Nommage fichiers | `_STANDARDS/_GLOBAL/STD_NAMING_CONVENTIONS.md` |
| Hiérarchie réglementaire | `_STANDARDS/_GLOBAL/HIERARCHIE_REGLEMENTAIRE.md` |
| Architecture pools + stocks | `_STANDARDS/_GLOBAL/STD_GLOBAL_quiz_architecture_rules.md` |
| Anti-collision | `_STANDARDS/_GLOBAL/STD_GLOBAL_pool_collision_rules.md` |
| QA rules | `_STANDARDS/_GLOBAL/FACTORY_QA_RULES.md` |
| Assemblage quiz | `_STANDARDS/_GLOBAL/QUIZ_ASSEMBLY_RULES.md` |
| Glossaire | `_STANDARDS/_GLOBAL/glossaire_documentaire_factory.md` |
| Retours d'expérience | `_RETEX_LIBRARY/RETEX_INDEX.md` |
| État site / déploiement | `_DOCS/DDT.md` |

---

*MASTER_ARCHITECTURE.md — v6.0 — 2026-05-22*
*Remplace v5.3 (637 lignes → allégé, duplications supprimées)*
