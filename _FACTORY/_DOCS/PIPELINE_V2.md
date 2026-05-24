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
— Un seul artefact vivant (le xlsx) enrichi progressivement
— La difficulté est évaluée à l'angle (A3), assignée à la question (B2), filtrée par le moteur (runtime)
— Le pool est une unité thématique — il ne porte plus de niveau fixe
— Chaque étape a une entrée claire et une sortie claire

---

# CHANGEMENTS FONDAMENTAUX VS V1

| Concept V1 | Concept V2 |
|------------|------------|
| Items classés N1/N2/N3 en A3 | Items classés par RICHESSE + NIVEAU_POTENTIEL dérivé des angles |
| Difficulté montante (item → question) | Difficulté évaluée à l'angle (NIVEAU_ANGLE), assignée à la question (NIVEAU_QUESTION) |
| Pool = thème + niveau fixe (CIBLE_NIVEAU) | Pool = thème pur — niveau porté par chaque question |
| BIPREGEN.txt + ANGIPREGEN.txt + POOLS.txt | Feuilles du xlsx unique |
| A5 = étape autonome (TABLEUR_INIT) | xlsx créé en A3, enrichi à chaque étape |
| B4 = étape autonome (implantation) | Disparaît — le xlsx EST l'artefact en continu |
| Difficulté confirmée en B3 après coup | Difficulté ciblée dès A4, servie par B2 et B3 |

---

# ARTEFACTS V2.1

```
_LIGNES/[THEME]/
├── BIB_[THEME].txt          → source immuable A2 (jamais modifiée)
├── CONFIG.yaml              → métadonnées du quiz (THEME, DATE, STATUT...)
├── ITEMS.tsv                → source de vérité A3 — items
├── ANGLES.tsv               → source de vérité A3 — angles
├── POOLS.tsv                → source de vérité A4
├── QUESTIONS.tsv            → source de vérité B2
├── DISTRACTEURS.tsv         → source de vérité B3
├── QA.tsv                   → source de vérité B5
├── PROCESS_[THEME].md       → log minimal des décisions humaines uniquement
└── FICHE_VEILLE_[THEME].md  → produit en B5
```

TSV = source de vérité machine (C-010 / C-012 / TOKEN_ECONOMY RÈGLE 01).
VIEW xlsx générée à la demande : `python generate_xlsx_view.py _LIGNES/[THEME]`
SOMMAIRE calculé à la demande : `python generate_sommaire.py _LIGNES/[THEME]`

---

# STRUCTURE DU XLSX — QUIZ_[THEME].xlsx

## Feuille 1 : CONFIG

Métadonnées du quiz.

| Champ | Valeur |
|-------|--------|
| THEME | — |
| DATE_INIT | — |
| STOCK_CIBLE | 277 |
| VERSION | — |
| STATUT | INIT / EN_COURS / VALIDÉ / EXPORTÉ |

---

## Feuille 2 : ITEMS

Remplace BIPREGEN.txt.

| Colonne | Description |
|---------|-------------|
| ITEM_ID | [THEME]-[CAT]-[N°] |
| LIBELLE | Texte de l'item (ligne unique) |
| CLUSTER | Section / catégorie thématique d'origine |
| RICHESSE | DENSE / STANDARD / LIGHT |
| NIVEAU_POTENTIEL | N1 / N2 / N3 / MULTI — dérivé des NIVEAU_ANGLE de l'item |
| SIGNAL_RUNTIME | tag runtime optionnel (KNOWN_NAME / HIDDEN_ORIGIN / etc.) |
| SOURCE_BIB | Référence ligne BIB originale |

**RICHESSE** = combien de questions l'item peut générer.
**NIVEAU_POTENTIEL** = à quel public — dérivé de l'agrégation des NIVEAU_ANGLE (voir FACTORY_RUNTIME_LEXICON.md).
**CLUSTER** = section/catégorie thématique — remplace CATÉGORIE (C-013 : labels runtime en anglais).
**SIGNAL_RUNTIME** = tag fermé depuis FACTORY_RUNTIME_LEXICON.md (RUNTIME_SIGNAL section).

⚠️ RICHESSE ≠ NIVEAU_POTENTIEL. Un item DENSE peut être N1, N3 ou MULTI selon ses angles.

---

## Feuille 3 : ANGLES

Remplace ANGIPREGEN.txt.

| Colonne | Description |
|---------|-------------|
| ANGLE_ID | [ITEM_ID]-[A/B/C...] |
| ITEM_ID | Référence feuille ITEMS |
| ANGLE_COURT | Description courte de l'angle interrogeable |
| MECANIQUE | Mécanique de question (IDENTIFY / COMPARE / LOCATE / DATE / CLASSIFY / ELIMINATE / LINK) |
| NIVEAU_ANGLE | N1 / N2 / N3 — niveau de difficulté de cet angle (critères fermés dans FACTORY_RUNTIME_LEXICON.md) |
| POOL_CIBLE | Pool auquel cet angle est assigné |
| COLLISION_WITH | ANGLE_ID incompatibles (anti-collision) |
| QUOTA | Nombre de questions cibles depuis cet angle |
| STATUT | DISPONIBLE / RÉSERVÉ / UTILISÉ / EXCLU |

---

## Feuille 4 : POOLS

Remplace POOLS.txt. Structure les 20 pools avec difficulté top-down.

| Colonne | Description |
|---------|-------------|
| POOL_ID | QV-01 à QV-15 / IF-01 à IF-05 |
| TYPE | IF / QV |
| POSITION_QUIZ | Q1 à Q20 |
| THEME_LABEL | Intitulé contrôlé du pool (peut être composite) |
| MODE | SIMPLE / AGRÉGÉ |
| SOUS_THEMES | Liste des sous-thèmes fusionnés (si MODE=AGRÉGÉ) |
| ITEMS_ASSIGNES | Liste ITEM_ID (tous sous-thèmes confondus) |
| COUVERTURE_NIVEAU | OK / WARN / FAIL — validé en A4 (voir RULE-ARCH-008) |
| SIGNAL_RUNTIME | tag runtime optionnel |
| FAISABILITE | OK / WARN / FAIL — stock cible atteignable |
| STOCK_CIBLE | Nombre questions cibles |
| STOCK_ACTUEL | Calculé automatiquement depuis QUESTIONS |

Le pool n'a plus de CIBLE_NIVEAU fixe. La progression de difficulté est assurée par NIVEAU_QUESTION sur chaque question et filtrée par le moteur à l'assemblage (RULE-ARCH-006 + RULE-ARCH-008).

**MODE AGRÉGÉ** (RULE-ARCH-005) : un pool peut regrouper plusieurs sous-thèmes dont aucun n'atteint seul le stock cible. Les questions restent CONSISTENCY_VALIDATED entre elles et les distracteurs valides à travers les sous-thèmes. Un pool agrégé = une seule unité de tirage au sort — le joueur ne voit pas la distinction.

---

## Feuille 5 : QUESTIONS

Remplace les fichiers B2_GENERATION/.

| Colonne | Description |
|---------|-------------|
| Q_ID | [POOL_ID]-Q[NNN] |
| POOL_ID | Référence feuille POOLS |
| ANGLE_ID | Référence feuille ANGLES |
| LIBELLE | Texte de la question |
| REPONSE | Réponse correcte |
| NIVEAU_QUESTION | N1 / N2 / N3 — assigné en B2 depuis NIVEAU_ANGLE (non hérité du pool) |
| TYPE_Q | 1-Identification / 2-Nombre / 3-Année / 4-Lieu / 5-Correspondance |
| STATUT_B2 | EN_COURS / SOUMIS / VALIDÉ / REJETÉ |

---

## Feuille 6 : DISTRACTEURS

Remplace les fichiers B3/.

| Colonne | Description |
|---------|-------------|
| Q_ID | Référence feuille QUESTIONS |
| D1 | Distracteur 1 |
| D2 | Distracteur 2 |
| D3 | Distracteur 3 |
| NIVEAU_CONFIRME | N1 / N2 / N3 — niveau réel après distracteurs |
| ECART_CIBLE | OK / SURQUALIFIÉ / SOUS-QUALIFIÉ |
| STATUT_B3 | EN_COURS / PASS / WARNING / FAIL |

**NIVEAU_CONFIRME vs NIVEAU_QUESTION :** si écart → signaler, corriger distracteurs ou reformuler question. NIVEAU_QUESTION peut être ajusté sur décision humaine (contrairement à l'ancien CIBLE_NIVEAU de pool qui était immuable).

---

## Feuille 7 : QA

Audit final B5.

| Colonne | Description |
|---------|-------------|
| Q_ID | Référence |
| QA_STATUS | PASS / WARNING / FAIL |
| FLAGS | VEILLE / IRRECEVABLE / COLLISION / FORMAT |
| NOTES | Commentaire auditeur |
| DECISION | CONSERVER / MODIFIER / REJETER / DÉPLACER |

---

# PIPELINE V2 — ÉTAPES

```
A1_THEME
  → A2_BIB
    → A3_INIT_XLSX
      → A4_POOLS
        → B2_QUESTIONS
          → B3_DISTRACTEURS
            → B5_AUDIT
              → B6_RÈGLES
                → EXPORT
```

---

## A1 — CADRAGE THÈME
**Entrée :** décision humaine  
**Sortie :** contexte thématique documenté (léger)  
**Pas de xlsx encore**

---

## A2 — APPROVISIONNEMENT BIB
**Entrée :** recherche documentaire  
**Sortie :** BIB_[THEME].txt (immuable après archivage)  
**Pas de xlsx encore**

---

## A3 — INIT TSV + ITEMS + ANGLES
**Entrée :** BIB_[THEME].txt  
**Sortie :** CONFIG.yaml + ITEMS.tsv + ANGLES.tsv peuplés

Actions :
1. Initialiser TSV depuis template _LIGNES/_TEMPLATE/ + remplir CONFIG.yaml
2. Extraire sélectivement du BIB, filtrer, mettre en ligne unique
3. Coder chaque item [THEME]-[CAT]-[N°] → ITEMS.tsv
4. Assigner RICHESSE (Dense/Standard/Light) par item → ITEMS.tsv
5. Cartographier les angles par item → ANGLES.tsv
6. Assigner NIVEAU_ANGLE (N1/N2/N3) par angle → ANGLES.tsv (critères fermés — FACTORY_RUNTIME_LEXICON.md)
7. Dériver NIVEAU_POTENTIEL par item depuis agrégation NIVEAU_ANGLE → ITEMS.tsv
8. Définir exclusions et quotas indicatifs → ANGLES.tsv

**Gate humaine :** validation RICHESSE + NIVEAU_ANGLE + angles avant A4

---

## A4 — POOLS
**Entrée :** ITEMS.tsv + ANGLES.tsv validés (gate A3)  
**Sortie :** POOLS.tsv peuplé + ANGLES.tsv mis à jour

Actions :
1. Définir les 20 pools (éditorial — thématique uniquement)
2. Identifier les sous-thèmes trop faibles pour tenir un pool seul
3. Fusionner ces sous-thèmes en pool AGRÉGÉ si CONSISTENCY garantie (RULE-ARCH-005)
4. Assigner items/angles aux pools (simples ou agrégés)
5. Calculer COUVERTURE_NIVEAU par pool (RULE-ARCH-008) — FAIL bloque B2
6. VALIDER stock cible atteignable pour chaque pool
7. VALIDATION anti-collision inter-pools

**Gate humaine :** validation structure pools + COUVERTURE_NIVEAU avant B2
**Vue :** `python generate_sommaire.py _LIGNES/[THEME]`

---

## B2 — GÉNÉRATION QUESTIONS
**Entrée :** POOLS.tsv + ANGLES.tsv validés (gate A4)  
**Sortie :** QUESTIONS.tsv peuplé

Actions :
1. Pour chaque angle assigné au pool, lire NIVEAU_ANGLE et générer la question à ce niveau
2. Appliquer checklist 8 filtres (RULE-B2-HB-002)
3. Appliquer VALIDATION recevabilité pédagogique (STD_B2_recevabilite_pedagogique.md)
4. Anti-collision avant soumission humaine
5. Remplir Q_ID / POOL_ID / ANGLE_ID / LIBELLE / REPONSE / NIVEAU_QUESTION / TYPE_Q dans QUESTIONS.tsv
6. Vérifier distribution NIVEAU_QUESTION par pool — WARNING si stock N_REQUIS < 5 questions

**Gate humaine :** validation par pool (pas question par question au stade B2)

---

## B3 — GÉNÉRATION DISTRACTEURS
**Entrée :** QUESTIONS.tsv validé (gate B2)  
**Sortie :** DISTRACTEURS.tsv peuplé

Actions :
1. PASS 1 : générer 3 distracteurs par question en ciblant NIVEAU_QUESTION
2. PASS 2 : audit anti-collision + format + distribution + biais
3. PASS 3 : correction des flags
4. Remplir D1/D2/D3 / NIVEAU_CONFIRME / ECART_CIBLE / STATUT_B3 dans DISTRACTEURS.tsv
5. Signaler tout ECART_CIBLE ≠ OK → décision humaine

**Gate humaine :** validation DECISION_GATE (GO / CONDITIONAL_GO / NO_GO)

---

## B5 — AUDIT QA
**Entrée :** QUESTIONS.tsv + DISTRACTEURS.tsv validés (gate B3)  
**Sortie :** QA.tsv peuplé + FICHE_VEILLE

Actions :
1. Audit question par question
2. Assigner QA_STATUS + FLAGS dans QA.tsv
3. Appliquer VALIDATION VEILLE (STD_OBSOLESCENCE_WATCH_RULES.md)
4. Décisions CONSERVER / MODIFIER / REJETER / DÉPLACER
5. Produire FICHE_VEILLE

**Gate humaine :** validation finale avant export

---

## B6 — EXTRACTION RÈGLES
**Entrée :** retour d'expérience session  
**Sortie :** GEN_NOTES candidats, enrichissements STD  
**Légère — seulement si pattern généralisable détecté**

---

## EXPORT
**Entrée :** QA.tsv (QA_STATUS = PASS sur toutes questions)  
**Sortie :** livrable quiz prêt à implantation
**Vue :** `python generate_xlsx_view.py _LIGNES/[THEME]`

Blocages export :
- QA_STATUS = FAIL sur ≥1 question
- ECART_CIBLE non résolu
- FICHE_VEILLE absente

---

# ÉTAPES SUPPRIMÉES

| Étape V1 | Raison suppression |
|----------|--------------------|
| A5 — TABLEUR_INIT | Absorbé par A3 — xlsx créé dès A3 |
| B4 — IMPLANTATION | Disparaît — le xlsx est l'artefact continu, pas un livrable de fin |

---

# DOCUMENTS SUPPRIMÉS

| Document V1 | Remplacé par |
|-------------|--------------|
| BIPREGEN_[THEME].txt | Feuille ITEMS du xlsx |
| ANGIPREGEN_[THEME].txt | Feuille ANGLES du xlsx |
| POOLS_[THEME].txt | Feuille POOLS du xlsx |
| Fichiers B2_GENERATION/ | Feuille QUESTIONS du xlsx |
| Fichiers B3/ | Feuille DISTRACTEURS du xlsx |

---

# DOCUMENTS CONSERVÉS

| Document | Rôle |
|----------|------|
| BIB_[THEME].txt | Source immuable |
| PROCESS_[THEME].md | Log décisions humaines (léger) |
| QUIZ_[THEME].xlsx | Artefact unique |
| FICHE_VEILLE | Produite en B5, conservée avec le quiz |

---

*PIPELINE_V2.md — Version 2.1 — 2026-05-24*
*Évolution : décorrélation thème/niveau — CIBLE_NIVEAU pool → NIVEAU_QUESTION par question*
*Principe : légèreté + discipline — un artefact, une source de vérité*
