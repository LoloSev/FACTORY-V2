---
name: STD_B3_distractor_rules
version: 1.0
status: ACTIVE_REFERENCE
IA_COMPATIBLE: TRUE
IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE
PIPELINE_SCOPE: B3
DEPENDENCY:
  - STD_GLOBAL_pool_collision_rules.md
  - FACTORY_QA_RULES.md
  - glossaire_documentaire_factory.md
---

# STANDARD — DISTRACTOR RULES (B3)

Règles pour générer, valider et optimiser les distracteurs selon priorité FACTORY.

---

## PRIORITY_MATRIX (B6 application)

```
HARD_BLOCKERS    → PASS 2 détecte → PASS 3 corrige obligatoire
SOFT_WARNINGS    → PASS 2 flag → PASS 3 fix souhaité
OPTIONAL         → PASS 2 signal → PASS 3 optimize si possible
```

---

# SECTION — HARD_BLOCKERS

[RULE-HB-DIST-001]
**Collision avec réponse correcte**
- Distractor = correct answer ailleurs → BLOCKER immédiat
- Application B3 de RULE-PCOLL-004 (périmètre inter-pool HARD BLOCKER)
- Détection: PASS 2 (anti-collision check)
- Correction: PASS 3 (remplacer par entité différente)

[RULE-HB-DIST-002]
**Distracteur fictif non signalé**
- Toute invention (nom, lieu, chiffre) sans validation → BLOCKER
- Détection: PASS 1 (VALIDER sources réelles)
- Correction: Sourcer depuis données réelles ou signaler explicitement

Sous-règles (migrées depuis MDE_A3 — consolidation 2026-05-18) :
- L'IA ne peut jamais valider seule un distracteur fictif
- Tout nom inventé doit être vérifié avant intégration
- Les distracteurs fictifs doivent rester crédibles sans pouvoir être confondus avec une entité réelle existante
- Tout distracteur fictif doit rester traçable dans le workflow (MODIFICATIONS_LOG)

[RULE-HB-DIST-003]
**Format inconsistent dans question**
- Mix de formats (1998 vs "édition 1998") → BLOCKER
- Détection: PASS 2 (format homogeneity check)
- Correction: PASS 3 (reformatter pour CONSISTENCY)

[RULE-HB-DIST-004]
**QA_STATUS = FAIL**
- Bloque export immédiat
- Résultat: Ne pas passer à B4

---

# SECTION — SOFT_WARNINGS

[RULE-SW-DIST-001]
**Soft collision (même entité, contexte différent)**
- Distractor réutilisé (ex: Ronaldo en answer Q1, distractor Q2 contexte différent)
- Détection: PASS 2 (soft collision analysis)
- Correction: PASS 3 si TYPE 1/5 (recommandé), sinon documenter

[RULE-SW-DIST-002]
**Plausibilité basse (TYPE 1 ou 5)**
- FAIL si `SOURCE_STATUS` ≠ VERIFIED
- WARNING si aucun critère partagé avec la réponse correcte
- WARNING si l'entité n'apparaît dans aucune source de référence du corpus actif
- Détection: PASS 2 (source + criteria check)
- Correction: PASS 3 (remplacer par option vérifiée partageant ≥1 critère)

[RULE-SW-DIST-003]
**Difficulty spacing mal aligné**
- N1 invalide si distance mesurée appartient à la plage N2/N3 du type
- N2 invalide si distance mesurée appartient à la plage N1/N3 du type
- N3 invalide si distance mesurée appartient à la plage N1/N2 du type
- Détection: PASS 2 (`DISTANCE_LEVEL` vs `CIBLE_NIVEAU`)
- Correction: PASS 3 (remplacer par candidat dans plage cible)

[RULE-SW-DIST-004]
**Distribution de difficultés hors seuil**
- WARNING si écart d'un type > 15 points vs cible globale
- FAIL si écart d'un type > 25 points vs cible globale
- Détection: PASS 2 (`TYPE_LEVEL_SHARE` vs `TARGET_LEVEL_SHARE`)
- Correction: PASS 3 (remplacer des distracteurs jusqu'à retour sous seuil)

---

# SECTION — OPTIONAL_OPTIMIZERS

[RULE-OPT-DIST-001]
**Source concentration (bias)**
- Single source >3% (ex: Ronaldo appears 25 times)
- Détection: PASS 2 (concentration analysis)
- Correction: PASS 3 (replace with different player)

[RULE-OPT-DIST-002]
**Era clustering**
- >50% distractors from same era for era-dependent question
- Détection: PASS 2 (era bias analysis)
- Correction: PASS 3 (diversify eras)

[RULE-OPT-DIST-003]
**Nationality skew (TYPE 1/5)**
- Single nationality >15% of distractors pool
- Détection: PASS 2 (nationality analysis)
- Correction: PASS 3 (replace with different nationality)

[RULE-OPT-DIST-004]
**Distractor reuse (inter-questions)**
- Same distractor used >1 time
- Target: <5% reuse rate
- Détection: PASS 2 (reuse pattern analysis)
- Correction: PASS 3 (prefer diverse distractors)

---

# SECTION — NOTE_DIFFICULTÉ

Distribution distracteurs alignée sur distribution questions (décision 2026-05-22) :

| Niveau | Questions (pools) | Distracteurs (B3) |
|--------|------------------|-------------------|
| N1 | 25% (Q1-Q5) | 25% ±5% |
| N2 | 50% (Q6-Q15) | 50% ±5% |
| N3 | 25% (Q16-Q20) | 25% ±5% |

Source pools : STD_GLOBAL_quiz_architecture_rules.md RULE-ARCH-006
RETEX_REF: RETEX_STD_B3_DISTRACTOR_RULES_001
RETEX_ROLE: JUSTIFICATION

---

# SECTION — TYPE-SPECIFIC_RULES

## TYPE 1 — IDENTIFICATION

[RULE-T1-001] **Selection**
- Puiser dans [CORPUS_ACTIF] : [ENTITES] célèbres, multi-[CONTEXTE]
- Même catégorie : [CATEGORIE] → [CATEGORIE], pas mélange
RETEX_REF: RETEX_STD_B3_DISTRACTOR_RULES_002

[EXEMPLE-T1-001 — cas source]
Application sur la ligne cas source (football) :
→ Puiser dans base football : joueurs/équipes célèbres, multi-éditions
→ Même catégorie : attaquant → attaquant, pas mélange

[RULE-T1-002] **CONSISTENCY**
- Partager ≥1 propriété : même nationalité OU même époque OU même rôle

[RULE-T1-003] **Plausibilité**
- `SOURCE_STATUS` = VERIFIED obligatoire
- Partage ≥1 critère contrôlé avec la réponse correcte : nationalité, époque, rôle, compétition, catégorie
- WARNING si 0 critère partagé
- FAIL si entité hors catégorie attendue
RETEX_REF: RETEX_STD_B3_DISTRACTOR_RULES_003

[RULE-T1-004] **Format**
- Majuscule initiale exacte (Eusebio, pas eusebio ou EUSEBIO)
- Accents FIFA respect ("Pelé" pas "Pele")

[RULE-T1-005] **Difficulty scaling**
- N1: nationalité différente OU époque très différente
- N2: même nationalité MAIS époque/rôle différent
- N3: même nationalité/époque, seul rôle/détail précis varie

---

## TYPE 2 — NUMBERS

[RULE-T2-001] **Selection**
- Nombres réels du cas source si possible
RETEX_REF: RETEX_STD_B3_DISTRACTOR_RULES_004
- Plage autorisée = min/max observés dans le corpus actif du champ concerné
- Voisins de réponse correcte

[RULE-T2-002] **Plausibilité**
- FAIL si valeur hors min/max corpus actif du champ concerné
- WARNING si distance numérique incompatible avec `CIBLE_NIVEAU` :
  - N1: distance ≥ 4 unités ou ≥ 30 % de la réponse
  - N2: distance 2-3 unités ou 10-30 %
  - N3: distance 1 unité ou < 10 %

[RULE-T2-003] **Difficulty scaling**
- N1: ±4 ou plus (ex: R=15 → 8, 11, 20)
- N2: ±2-3 (ex: R=15 → 12, 13, 18)
- N3: ±1 (ex: R=15 → 13, 14, 16)

[RULE-T2-004] **Format**
- Chiffres arabes ("15" pas "quinze")
- Pas d'unités sauf si réponse en a
- Pas de décimales pour dénombrements

---

## TYPE 3 — YEARS/EDITIONS

[RULE-T3-001] **Selection**
- SEULEMENT [EDITIONS] réelles du [CORPUS_ACTIF] ([N_EDITIONS] maximum)
- Jamais [EDITION] fictive ou hors-[CORPUS_ACTIF]
RETEX_REF: RETEX_STD_B3_DISTRACTOR_RULES_005
RETEX_REF: RETEX_STD_B3_DISTRACTOR_RULES_006

[EXEMPLE-T3-001 — cas source]
Application sur la ligne cas source (football / Coupe du Monde) :
→ SEULEMENT années réelles CdM (23 éditions maximum, 1930–2022)
→ Transposer : remplacer [N_EDITIONS] et [CORPUS_ACTIF] par l'équivalent du thème actif

[RULE-T3-002] **CONSISTENCY**
- Année autorisée seulement si présente dans le corpus actif
- Si la question contient une contrainte d'entité, l'année doit partager ≥1 relation source avec cette entité
- FAIL si année absente du corpus actif

[RULE-T3-003] **Difficulty scaling**
- N1: distance ≥ 12 ans ou ≥ 3 éditions
- N2: distance 8 à 11 ans ou 2 éditions
- N3: distance 4 ans ou 1 édition
- FAIL si distance = 0

[RULE-T3-004] **Format**
- Format unique par ligne : tous numériques (`YYYY`) ou tous libellés (`édition YYYY`)
- FAIL si formats mixtes dans D1/D2/D3/réponse

---

## TYPE 4 — LOCATION

[RULE-T4-001] **Selection**
- [LIEUX] réels du [CORPUS_ACTIF] SEULEMENT
- Pour sous-localisation : [SOUS_LIEUX] de la même [EDITION] ou proche
- Jamais inventer lieu
RETEX_REF: RETEX_STD_B3_DISTRACTOR_RULES_007

[EXEMPLE-T4-001 — cas source]
Application sur la ligne cas source (football / Coupe du Monde) :
→ Pays hôtes CdM réels SEULEMENT
→ Pour villes : villes hôtes même édition ou proche
→ Transposer : remplacer [LIEUX] par l'équivalent géographique du corpus actif

[RULE-T4-002] **CONSISTENCY**
- Pays → distractors pays (pas villes mélangées)
- Respecter continent si question géographiquement contextualisée

[RULE-T4-003] **Difficulty scaling**
- N1: continent différent ou région différente, source vérifiée
- N2: même catégorie de lieu, édition/période différente
- N3: même région ou même période, mais réponse incorrecte
- FAIL si lieu inventé ou non sourcé

[RULE-T4-004] **Format**
- Langue française (Afrique du Sud pas South Africa)
- Respect orthographe officielle

[RULE-T4-005] **⚠️ Signal: ville ambiguity**
- Villes hôtes = pool limité (10 villes France par ex)
- Risque collision élevé → vérification obligatoire

---

## TYPE 5 — CORRESPONDENCE

[RULE-T5-001] **Selection**
- Satisfaire CERTAINS critères de la question (pas tous)
- Même nationalité/époque/achievement : varier
- N1: 1 critère partagé
- N2: 2 critères partagés
- N3: tous les critères sauf 1
- FAIL si tous les critères sont partagés avec la réponse correcte

[RULE-T5-002] **CONSISTENCY**
- Chaque distracteur doit partager ≥1 critère contrôlé
- WARNING si 0 critère partagé
- FAIL si type/catégorie incompatible avec la réponse correcte

[RULE-T5-003] **Plausibilité**
- `SOURCE_STATUS` = VERIFIED obligatoire
- ≥2 critères partagés requis pour N2/N3
- FAIL si entité absente du corpus actif ou non traçable

[RULE-T5-004] **Format**
- Exacte : si réponse "Lionel Messi" → "Kylian Mbappé", pas "Mbappé" seul

[RULE-T5-005] **⚠️ CRITICAL: High collision risk**
- Joueurs célèbres (Messi, Ronaldo, Mbappé) réutilisés souvent
- Vérification anti-collision OBLIGATOIRE avant assignation

---

# SECTION — TRANSVERSE_RULES

[RULE-TRANS-001] **Anti-collision obligatoire**
- Tous types : VALIDER vs [STOCK_CIBLE] correct answers avant assignation
- Application B3 de RULE-PCOLL-004 — SOURCE_DE_VERITE: STD_GLOBAL_pool_collision_rules.md

[RULE-TRANS-002] **Format homogeneous**
- Dans question : 1 answer + 3 distractors = même format

[RULE-TRANS-003] **No invention**
- Tous noms, chiffres, lieux, années = réels et vérifiables

[RULE-TRANS-004] **Uniqueness intra-question**
- 3 distractors d'une question = distincts entre eux

[RULE-TRANS-005] **Uniqueness inter-questions (recommended)**
- Éviter réutilisation même distractor autre question (si possible)
- Target: <5% reuse

---

# SECTION — VALIDATION_CHECKLIST

## PASS 1 (Generation)
- [ ] Type identifié (1-5)
- [ ] Règles TYPE-spécifiques chargées
- [ ] 10-15 candidats générés (sources réelles cas source)
RETEX_REF: RETEX_STD_B3