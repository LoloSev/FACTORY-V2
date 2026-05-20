# FACTORY PIPELINE — VERSION 2

DEPENDENCY:
- MASTER_ARCHITECTURE.md
- glossaire_documentaire_factory.md
VERSION: 2.0
DATE: 2026-05-18
STATUS: ACTIVE_REFERENCE
REMPLACE: pipeline implicite dans MASTER_ARCHITECTURE.md (A1→B6)
IA_COMPATIBLE: TRUE

PRINCIPE: Légèreté + Discipline
— Un seul artefact vivant (le xlsx) enrichi progressivement
— La difficulté descend du pool, elle ne remonte pas de l'item
— Chaque étape a une entrée claire et une sortie claire

---

# CHANGEMENTS FONDAMENTAUX VS V1

| Concept V1 | Concept V2 |
|------------|------------|
| Items classés N1/N2/N3 en A3 | Items classés par RICHESSE (Dense/Standard/Light) |
| Difficulté montante (item → question) | Difficulté descendante (pool → question → distracteurs) |
| BIPREGEN.txt + ANGIPREGEN.txt + POOLS.txt | Feuilles du xlsx unique |
| A5 = étape autonome (TABLEUR_INIT) | xlsx créé en A3, enrichi à chaque étape |
| B4 = étape autonome (implantation) | Disparaît — le xlsx EST l'artefact en continu |
| Difficulté confirmée en B3 après coup | Difficulté ciblée dès A4, servie par B2 et B3 |

---

# ARTEFACTS V2

```
BIB_[THEME].txt           → source immuable (jamais modifiée)
QUIZ_[THEME].xlsx         → colonne vertébrale unique, progressivement enrichie
PROCESS_[THEME].md        → log minimal des décisions humaines uniquement
```

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
| LIBELLÉ | Texte de l'item (ligne unique) |
| CATÉGORIE | Section thématique |
| RICHESSE | DENSE / STANDARD / LIGHT |
| SOURCE_BIB | Référence ligne BIB originale |

**RICHESSE** — définitions :
- **DENSE** : item à plusieurs angles exploitables, fort potentiel de questions distinctes
- **STANDARD** : item à 1-3 angles, potentiel normal
- **LIGHT** : item faiblement interrogeable, 1 angle au maximum

⚠️ RICHESSE ≠ difficulté. Un item DENSE peut générer des questions N1 comme N3 selon l'angle.

---

## Feuille 3 : ANGLES

Remplace ANGIPREGEN.txt.

| Colonne | Description |
|---------|-------------|
| ANGLE_ID | [ITEM_ID]-[A/B/C...] |
| ITEM_ID | Référence feuille ITEMS |
| ANGLE | Description de l'angle interrogeable |
| POOL_CIBLE | Pool auquel cet angle est assigné |
| EXCLUSIONS | Angles incompatibles (anti-collision) |
| QUOTA | Nombre de questions cibles depuis cet angle |
| STATUT | DISPONIBLE / RÉSERVÉ / UTILISÉ / EXCLU |

---

## Feuille 4 : POOLS

Remplace POOLS.txt. Structure les 20 pools avec difficulté top-down.

| Colonne | Description |
|---------|-------------|
| POOL_ID | QV-01 à QV-15 / IF-SF-01/02 / IF-ROT-01/02/03 |
| TYPE | IF-SF / IF-ROT / QV |
| POSITION_QUIZ | Q1 à Q20 |
| CIBLE_NIVEAU | N1 (Q1-5) / N2 (Q6-15) / N3 (Q16-20) |
| THÈME_ÉDITORIAL | Intitulé du pool (peut être composite) |
| MODE | SIMPLE / AGRÉGÉ |
| SOUS_THÈMES | Liste des sous-thèmes fusionnés (si MODE=AGRÉGÉ) |
| ITEMS_ASSIGNÉS | Liste ITEM_ID (tous sous-thèmes confondus) |
| STOCK_CIBLE | Nombre questions cibles |
| STOCK_ACTUEL | Calculé automatiquement depuis QUESTIONS |

**CIBLE_NIVEAU est immuable** — défini par RULE-ARCH-004, non modifiable par l'éditeur.

**MODE AGRÉGÉ** (RULE-ARCH-005) : un pool peut regrouper plusieurs sous-thèmes dont aucun n'atteint seul le stock cible. Les questions restent CONSISTENCY_VALIDATED entre elles et les distracteurs valides à travers les sous-thèmes. Un pool agrégé = une seule unité de tirage au sort — le joueur ne voit pas la distinction.

---

## Feuille 5 : QUESTIONS

Remplace les fichiers B2_GENERATION/.

| Colonne | Description |
|---------|-------------|
| Q_ID | [POOL_ID]-Q[NNN] |
| POOL_ID | Référence feuille POOLS |
| ANGLE_ID | Référence feuille ANGLES |
| LIBELLÉ | Texte de la question |
| RÉPONSE | Réponse correcte |
| CIBLE_NIVEAU | Hérité du pool (N1/N2/N3) |
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
| NIVEAU_CONFIRMÉ | N1 / N2 / N3 — niveau réel après distracteurs |
| ÉCART_CIBLE | OK / SURQUALIFIÉ / SOUS-QUALIFIÉ |
| STATUT_B3 | EN_COURS / PASS / WARNING / FAIL |

**NIVEAU_CONFIRMÉ vs CIBLE_NIVEAU :** si écart → signaler, corriger distracteurs ou reformuler question. Ne jamais modifier CIBLE_NIVEAU du pool.

---

## Feuille 7 : QA

Audit final B5.

| Colonne | Description |
|---------|-------------|
| Q_ID | Référence |
| QA_STATUS | PASS / WARNING / FAIL |
| FLAGS | VEILLE / IRRECEVABLE / COLLISION / FORMAT |
| NOTES | Commentaire auditeur |
| DÉCISION | CONSERVER / MODIFIER / REJETER / DÉPLACER |

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

## A3 — INIT XLSX + ITEMS + ANGLES
**Entrée :** BIB_[THEME].txt  
**Sortie :** QUIZ_[THEME].xlsx (feuilles CONFIG + ITEMS + ANGLES peuplées)

Actions :
1. Créer QUIZ_[THEME].xlsx
2. Extraire sélectivement du BIB, filtrer, mettre en ligne unique
3. Coder chaque item [THEME]-[CAT]-[N°] → feuille ITEMS
4. Assigner RICHESSE (Dense/Standard/Light) par item → feuille ITEMS
5. Cartographier les angles par item → feuille ANGLES
6. Définir exclusions et quotas indicatifs → feuille ANGLES

**Gate humaine :** validation RICHESSE + angles avant A4

---

## A4 — POOLS
**Entrée :** QUIZ_[THEME].xlsx (ITEMS + ANGLES validés)  
**Sortie :** feuille POOLS peuplée

Actions :
1. Définir les 20 pools (éditorial)
2. Assigner CIBLE_NIVEAU par pool (automatique via RULE-ARCH-004)
3. Identifier les sous-thèmes trop faibles pour tenir un pool seul
4. Fusionner ces sous-thèmes en pool AGRÉGÉ si CONSISTENCY garantie (RULE-ARCH-005)
5. Assigner items/angles aux pools (simples ou agrégés)
6. VALIDER stock cible atteignable pour chaque pool
7. VALIDATION anti-collision inter-pools

**Gate humaine :** validation structure pools avant B2

---

## B2 — GÉNÉRATION QUESTIONS
**Entrée :** QUIZ_[THEME].xlsx (POOLS validés)  
**Sortie :** feuille QUESTIONS peuplée

Actions :
1. Pour chaque pool, générer questions en ciblant CIBLE_NIVEAU du pool
2. Appliquer checklist 8 filtres (RULE-B2-HB-002)
3. Appliquer VALIDATION recevabilité pédagogique (STD_B2_recevabilite_pedagogique.md)
4. Anti-collision avant soumission humaine
5. Remplir Q_ID / POOL_ID / ANGLE_ID / LIBELLÉ / RÉPONSE / CIBLE_NIVEAU / TYPE_Q

**Gate humaine :** validation par pool (pas question par question au stade B2)

---

## B3 — GÉNÉRATION DISTRACTEURS
**Entrée :** QUIZ_[THEME].xlsx (QUESTIONS validées)  
**Sortie :** feuille DISTRACTEURS peuplée

Actions :
1. PASS 1 : générer 3 distracteurs par question en ciblant CIBLE_NIVEAU
2. PASS 2 : audit anti-collision + format + distribution + biais
3. PASS 3 : correction des flags
4. Remplir D1/D2/D3 / NIVEAU_CONFIRMÉ / ÉCART_CIBLE / STATUT_B3
5. Signaler tout ÉCART_CIBLE ≠ OK → décision humaine

**Gate humaine :** validation DECISION_GATE (GO / CONDITIONAL_GO / NO_GO)

---

## B5 — AUDIT QA
**Entrée :** QUIZ_[THEME].xlsx (QUESTIONS + DISTRACTEURS)  
**Sortie :** feuille QA peuplée

Actions :
1. Audit question par question
2. Assigner QA_STATUS + FLAGS
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
**Entrée :** QUIZ_[THEME].xlsx (QA_STATUS = PASS sur toutes questions)  
**Sortie :** livrable quiz prêt à implantation

Blocages export :
- QA_STATUS = FAIL sur ≥1 question
- ÉCART_CIBLE non résolu
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

*PIPELINE_V2.md — Version 2.0 — 2026-05-18*
*Principe : légèreté + discipline — un artefact, une source de vérité*
