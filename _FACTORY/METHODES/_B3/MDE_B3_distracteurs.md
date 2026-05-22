# MDE B3 — GÉNÉRATION DES DISTRACTEURS

VERSION: 2.0 (PIPELINE V2)
DATE: 2026-05-18
STATUS: ACTIVE_REFERENCE
PIPELINE_SCOPE: B3
IA_COMPATIBLE: TRUE
IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE

DEPENDENCY:
- PIPELINE_V2.md
- QUIZ_[THEME].xlsx (feuille QUESTIONS validée)
- STD_B3_distractor_rules.md
- STD_GLOBAL_pool_collision_rules.md

---

## MACHINE-FIRST EXECUTION CONTRACT

INPUT:
- QUIZ_[THEME].xlsx
- feuille QUESTIONS validée
- STD_B3_distractor_rules.md
- CIBLE_NIVEAU hérité par question

PROCESS:
1. générer candidats distracteurs par TYPE_Q
2. filtrer format, collisions et distance cible
3. sélectionner exactement 3 distracteurs
4. calculer NIVEAU_CONFIRMÉ et ÉCART_CIBLE
5. auditer le lot avant gate

OUTPUT:
- feuille DISTRACTEURS peuplée
- PASS 2 audit calculé
- flags par question

ACCEPTANCE_CRITERIA:
- DISTRACTOR_COUNT_PER_Q = 3
- EMPTY_DISTRACTOR_COUNT = 0
- DUPLICATE_WITHIN_Q_COUNT = 0
- HARD_COLLISION_COUNT = 0
- FORMAT_MATCH_RATE >= 99%
- REUSE_RATE < 5%
- SOURCE_CONCENTRATION_MAX <= 3%
- ECART_CIBLE_OK_RATE = 100% before GO
- STATUT_B3 ∈ {PASS, WARNING, FAIL}

FAILURE_CASES:
- fewer or more than 3 distractors
- distractor equals correct answer
- duplicate distractor in same question
- format mismatch above threshold
- ÉCART_CIBLE not resolved before GO

---
## OBJECTIF

Peupler la feuille DISTRACTEURS du xlsx : 3 distracteurs par question, calibrés pour confirmer le CIBLE_NIVEAU hérité du pool.

---

## ENTRÉE / SORTIE

| | |
|---|---|
| FROM | B2 — feuille QUESTIONS validée |
| INPUT | QUIZ_[THEME].xlsx (QUESTIONS avec Q_ID / RÉPONSE / CIBLE_NIVEAU / TYPE_Q) |
| OUTPUT | feuille DISTRACTEURS peuplée (D1 / D2 / D3 / NIVEAU_CONFIRMÉ / ÉCART_CIBLE / STATUT_B3) |
| HUMAN_VALIDATION | required after PASS 2; allowed statuses: GO / CONDITIONAL_GO / NO_GO |
| BLOCK_IF | hard collision / format inconsistant / QA_STATUS=FAIL |

---

## PRINCIPE FONDAMENTAL V2

Les distracteurs **servent** le CIBLE_NIVEAU — ils ne le définissent pas.

- CIBLE_NIVEAU est fixé par le pool (hérité depuis A4)
- PASS 1 génère des distracteurs calibrés pour atteindre ce niveau
- PASS 2 confirme si le NIVEAU_CONFIRMÉ correspond au CIBLE_NIVEAU
- Tout ÉCART_CIBLE ≠ OK est signalé → décision humaine

---

## COLONNES FEUILLE DISTRACTEURS À REMPLIR

| Colonne | Règle |
|---------|-------|
| Q_ID | référence feuille QUESTIONS |
| D1 | distracteur 1 |
| D2 | distracteur 2 |
| D3 | distracteur 3 |
| NIVEAU_CONFIRMÉ | N1 / N2 / N3 — niveau réel constaté après distracteurs |
| ÉCART_CIBLE | OK / SURQUALIFIÉ / SOUS-QUALIFIÉ |
| STATUT_B3 | PASS / WARNING / FAIL |

**ÉCART_CIBLE :**
- **OK** : NIVEAU_CONFIRMÉ = CIBLE_NIVEAU
- **SURQUALIFIÉ** : `NIVEAU_CONFIRMÉ` inférieur au `CIBLE_NIVEAU` ou distance distracteurs au-dessus de la plage cible
- **SOUS-QUALIFIÉ** : `NIVEAU_CONFIRMÉ` supérieur au `CIBLE_NIVEAU` ou distance distracteurs sous la plage cible

Tout ÉCART_CIBLE ≠ OK → tenter correction distracteurs avant de signaler à le HUMAN_GATE.

---

## ENTONNOIR 3-PASSES

### PASS 1 — GÉNÉRATION

**Objectif :** 3 distracteurs conformes au seuil de plausibilité du TYPE_Q par question, calibrés sur CIBLE_NIVEAU.

**Méthode :**
1. Lire Q_ID / TYPE_Q / RÉPONSE / CIBLE_NIVEAU depuis feuille QUESTIONS
2. Charger règles TYPE-spécifiques (STD_B3_distractor_rules.md)
3. Générer 10-15 candidats depuis sources réelles
4. Filtrer par conformité (RULE-T[X]-002)
5. Calibrer sur CIBLE_NIVEAU (RULE-T[X]-003 / difficulty scaling)
6. Valider format (RULE-T[X]-004)
7. Sélectionner 3 candidats conformes aux seuils — anti-collision soft check
8. Évaluer NIVEAU_CONFIRMÉ et ÉCART_CIBLE

**Output :** D1/D2/D3 + NIVEAU_CONFIRMÉ + ÉCART_CIBLE par question

---

### PASS 2 — AUDIT

**Objectif :** Détecter tous les FAILURE_CASE sur l'ensemble du lot.

**Métriques à VALIDER :**

| Métrique | Seuil | Niveau |
|----------|-------|--------|
| Hard collisions (distractor = réponse correcte ailleurs) | = 0 | BLOCKER |
| Format homogénéité | ≥ 99% | WARNING |
| Distribution difficulté distracteurs N1/N2/N3 | 25/50/25 ±5% | WARNING |
| Distribution TYPE_Q | chaque TYPE > 10% | WARNING |
| Taux réutilisation inter-questions | < 5% | WARNING |
| Plausibilité TYPE 1 & 5 | ≥ 80% | WARNING |
| Concentration source unique | ≤ 3% | WARNING |
| Era clustering | ≤ 50% même ère | WARNING |
| Nationality skew TYPE 1/5 | ≤ 15% | WARNING |
| ÉCART_CIBLE ≠ OK | 0 idéalement | WARNING |

**Output :** rapport audit + flags par question

**Decision gate :**
- ✅ GO : tous critères verts → procéder à B5
- ⚠️ CONDITIONAL_GO : FAILURE_CASE mineurs → PASS 3 requis
- ❌ NO_GO : FAILURE_CASE critiques → retour PASS 1

**HUMAN_GATE :** après PASS 2, avant PASS 3

---

### PASS 3 — CORRECTION

**Objectif :** Corriger uniquement les items flaggés en PASS 2.

**Méthode par type de flag :**

| Flag | Action |
|------|--------|
| HARD_COLLISION | remplacer par entité différente |
| SOFT_COLLISION | remplacer si TYPE 1/5 |
| FORMAT_MISMATCH | reformatter pour homogénéité |
| ÉCART_CIBLE=SURQUALIFIÉ | resserrer les distracteurs |
| ÉCART_CIBLE=SOUS-QUALIFIÉ | élargir l'écart des distracteurs |
| PLAUSIBILITY_LOW | remplacer par option plus reconnaissable |
| SOURCE_CONCENTRATION | varier les sources |
| ERA_CLUSTERING | diversifier les époques |

**Pour chaque correction :**
1. Générer 3-5 remplaçants ciblés
2. Sélectionner le meilleur (résout + maintient QA)
3. VALIDER pas de nouvelle collision
4. Mettre à jour NIVEAU_CONFIRMÉ et ÉCART_CIBLE
5. Documenter dans PROCESS_[THEME].md si correction non triviale

**Si >20% des questions modifiées :** recommander re-audit partiel.

---

## SÉQUENCE COMPLÈTE

```
Feuille QUESTIONS (B2 validé)
    ↓
PASS 1 : générer D1/D2/D3 calibrés sur CIBLE_NIVEAU
    ↓
PASS 2 : auditer collisions / format / distribution / ÉCART_CIBLE
    ↓
Gate humaine : GO / CONDITIONAL_GO / NO_GO
    ↓ (si CONDITIONAL_GO)
PASS 3 : corriger items flaggés
    ↓
Feuille DISTRACTEURS complète → B5 AUDIT
```

---

## RÈGLES UNIVERSELLES (résumé)

Toutes les règles détaillées sont dans STD_B3_distractor_rules.md.

- Distracteurs crédibles, même univers que la réponse (RULE-B3-001)
- Zéro fictif sans HUMAN_GATE (RULE-B3-002 / RULE-HB-DIST-002)
- Format homogène dans les 4 options (RULE-B3-003 / RULE-HB-DIST-003)
- Aucun distracteur avec 0 critère partagé si TYPE exige proximité (RULE-B3-004)
- `SOURCE_STATUS=VERIFIED` et ≥1 critère partagé pour chaque distracteur (RULE-B3-005)
- Calibration N1/N2/N3 selon CIBLE_NIVEAU du pool (RULE-B3-006)
- 3 distracteurs distincts entre eux (RULE-B3-007 / RULE-TRANS-004)
- Réutilisation inter-questions < 5% (RULE-B3-008 / RULE-TRANS-005)
- Anti-collision global obligatoire (RULE-TRANS-001)

---

## TRAÇABILITÉ

Documenter dans PROCESS_[THEME].md (uniquement) :
- corrections non triviales de PASS 3
- ÉCART_CIBLE persistants soumis à décision humaine
- flags WARNING non résolus avec justification

Pas de fichiers B3_AUDIT_*.md ou B3_LOG_*.txt séparés — tout dans PROCESS_[THEME].md.

---

*MDE_B3_distracteurs.md*
*Version 2.0 — 2026-05-18 — Pipeline V2*
*Remplace : v1.0 (B4 comme étape suivante / fichiers séparés)*


