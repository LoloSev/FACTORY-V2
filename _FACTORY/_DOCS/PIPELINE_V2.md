# FACTORY PIPELINE — VERSION 2

DEPENDENCY:
- MASTER_ARCHITECTURE.md
- glossaire_documentaire_factory.md
VERSION: 2.1
DATE: 2026-05-25
STATUS: ACTIVE_REFERENCE
REMPLACE: pipeline implicite dans MASTER_ARCHITECTURE.md (A1→B6)
IA_COMPATIBLE: TRUE

PRINCIPE: Légèreté + Discipline
- TSV = source de vérité machine unique
- Le xlsx est une vue générée à la demande
- La difficulté est évaluée à l'angle (A3), assignée à la question (B2), filtrée par le moteur (runtime)
- Le pool est une unité thématique — il ne porte plus de niveau fixe
- Chaque étape a une entrée claire et une sortie claire

---

# CHANGEMENTS FONDAMENTAUX VS V1

| Concept V1 | Concept V2 |
|------------|------------|
| Items classés N1/N2/N3 en A3 | Items classés par RICHESSE + NIVEAU_POTENTIEL dérivé des angles |
| Difficulté montante (item → question) | Difficulté évaluée à l'angle (NIVEAU_ANGLE), assignée à la question (NIVEAU_QUESTION) |
| Pool = thème + niveau fixe (CIBLE_NIVEAU) | Pool = thème pur — niveau porté par chaque question |
| BIPREGEN.txt + ANGIPREGEN.txt + POOLS.txt | TSV spécialisés |
| A5 = étape autonome (TABLEUR_INIT) | TSV initialisés dès A3 |
| B4 = étape autonome (implantation) | Disparaît — TSV = artefact continu |
| Difficulté confirmée en B3 après coup | Difficulté ciblée dès A4, servie par B2 et B3 |

---

# ARTEFACTS V2.1

```txt
_LIGNES/[THEME]/
├── BIB_[THEME].txt
├── CONFIG.yaml
├── ITEMS.tsv
├── ANGLES.tsv
├── POOLS.tsv
├── QUESTIONS.tsv
├── DISTRACTEURS.tsv
├── QA.tsv
├── PROCESS_[THEME].md
└── FICHE_VEILLE_[THEME].md
```

TSV = source de vérité machine.
VIEW xlsx générée à la demande :
`python generate_xlsx_view.py _LIGNES/[THEME]`

SOMMAIRE calculé à la demande :
`python generate_sommaire.py _LIGNES/[THEME]`

---

# STRUCTURE LOGIQUE DES DONNÉES

## CONFIG.yaml

Métadonnées du quiz.

| Champ | Valeur |
|-------|--------|
| THEME | — |
| DATE_INIT | — |
| STOCK_CIBLE | 277 |
| VERSION | — |
| STATUT | INIT / EN_COURS / VALIDÉ / EXPORTÉ |

---

## ITEMS.tsv

| Colonne | Description |
|---------|-------------|
| ITEM_ID | [THEME]-[CAT]-[N°] |
| LIBELLE | Texte de l'item |
| CLUSTER | Section thématique d'origine |
| RICHESSE | DENSE / STANDARD / LIGHT |
| NIVEAU_POTENTIEL | N1 / N2 / N3 / MULTI |
| SIGNAL_RUNTIME | tag runtime optionnel |
| SOURCE_BIB | Référence ligne BIB originale |

---

## ANGLES.tsv

| Colonne | Description |
|---------|-------------|
| ANGLE_ID | [ITEM_ID]-[A/B/C...] |
| ITEM_ID | Référence ITEMS.tsv |
| ANGLE_COURT | Description courte de l'angle |
| MECANIQUE | IDENTIFY / COMPARE / LOCATE / DATE / CLASSIFY / ELIMINATE / LINK |
| NIVEAU_ANGLE | N1 / N2 / N3 |
| POOL_CIBLE | Pool assigné |
| COLLISION_WITH | ANGLE_ID incompatibles |
| QUOTA | Nombre de questions cibles |
| STATUT | DISPONIBLE / RÉSERVÉ / UTILISÉ / EXCLU |

---

## POOLS.tsv

| Colonne | Description |
|---------|-------------|
| POOL_ID | QV-01 à QV-15 / IF-01 à IF-05 |
| TYPE | IF / QV |
| POSITION_QUIZ | Q1 à Q20 |
| THEME_LABEL | Intitulé contrôlé du pool |
| MODE | SIMPLE / AGRÉGÉ |
| SOUS_THEMES | Sous-thèmes fusionnés |
| ITEMS_ASSIGNES | Liste ITEM_ID |
| COUVERTURE_NIVEAU | OK / WARN / FAIL |
| SIGNAL_RUNTIME | tag runtime optionnel |
| FAISABILITE | OK / WARN / FAIL |
| STOCK_CIBLE | Nombre questions cibles |
| STOCK_ACTUEL | Calculé automatiquement depuis QUESTIONS.tsv |

Le pool n'a plus de CIBLE_NIVEAU fixe.
La progression de difficulté est assurée par NIVEAU_QUESTION.

---

## QUESTIONS.tsv

| Colonne | Description |
|---------|-------------|
| Q_ID | [POOL_ID]-Q[NNN] |
| POOL_ID | Référence POOLS.tsv |
| ANGLE_ID | Référence ANGLES.tsv |
| LIBELLE | Texte de la question |
| REPONSE | Réponse correcte |
| NIVEAU_QUESTION | N1 / N2 / N3 |
| TYPE_Q | 1-Identification / 2-Nombre / 3-Année / 4-Lieu / 5-Correspondance |
| STATUT_B2 | EN_COURS / SOUMIS / VALIDÉ / REJETÉ |

---

## DISTRACTEURS.tsv

| Colonne | Description |
|---------|-------------|
| Q_ID | Référence QUESTIONS.tsv |
| D1 | Distracteur 1 |
| D2 | Distracteur 2 |
| D3 | Distracteur 3 |
| NIVEAU_CONFIRME | N1 / N2 / N3 |
| ECART_CIBLE | OK / SURQUALIFIÉ / SOUS-QUALIFIÉ |
| STATUT_B3 | EN_COURS / PASS / WARNING / FAIL |

---

## QA.tsv

| Colonne | Description |
|---------|-------------|
| Q_ID | Référence |
| QA_STATUS | PASS / WARNING / FAIL |
| FLAGS | VEILLE / IRRECEVABLE / COLLISION / FORMAT |
| NOTES | Commentaire auditeur |
| DECISION | CONSERVER / MODIFIER / REJETER / DÉPLACER |

---

# PIPELINE V2 — ÉTAPES

```txt
A1_THEME
  → A2_BIB
    → A3_INIT_TSV
      → A4_POOLS
        → B2_QUESTIONS
          → B3_DISTRACTEURS
            → B5_AUDIT
              → B6_REGLES
                → EXPORT
```

---

## EXPORT

Entrée : QA.tsv validé.
Sortie : livrable quiz prêt à implantation.

VIEW xlsx générée à la demande :
`python generate_xlsx_view.py _LIGNES/[THEME]`

---

*PIPELINE_V2.md — Version 2.1 — 2026-05-25*
*TSV = source de vérité machine / xlsx = vue générée*
