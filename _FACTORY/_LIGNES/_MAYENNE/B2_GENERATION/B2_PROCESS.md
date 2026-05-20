# B2_MAYENNE_RUNTIME_PROCESS
# LINE_ID: MAYENNE_FACTORY_CORE
# PIPELINE: FACTORY_V2
# STATUS: READY_TO_LAUNCH

---

# RÔLE B2

Générer les questions brutes par pool.
Sortie : QUESTIONS peuplées dans B2_THEME.xlsx.
Entrée unique : angles validés de A3_MAYENNE_RUNTIME_TABLES.xlsx.

B2 ne :
- raisonne pas en documentation
- ne réexplique pas le contenu culturel
- n'invente pas d'angles absents de A3

---

# INPUTS

INPUT_PRINCIPAL: A3_MAYENNE_RUNTIME_TABLES.xlsx — feuille ANGLES
INPUT_RÈGLES: A4_MAYENNE_RUNTIME_RULES.md
INPUT_BALANCE: A4_MAYENNE_RUNTIME_BALANCE.md
INPUT_SIGNALS: A3_MAYENNE_RUNTIME_SIGNALS.md

NE PAS utiliser A4_MAYENNE_POOL_ENGINE.xlsx comme source runtime (non aligné).

---

# OUTPUT

OUTPUT: B2_THEME.xlsx — feuille QUESTIONS
FORMAT_CIBLE: Q_ID / POOL_ID / ANGLE_ID / LIBELLÉ / RÉPONSE / CIBLE_NIVEAU / TYPE_Q / PAYOFF_TYPE / FLAG_B2 / STATUT_B2

---

# PIPELINE B2

```
POUR CHAQUE POOL ACTIF (17 pools) :
  1. Lire angles disponibles (STATUT = DISPONIBLE)
  2. Générer questions depuis angles
  3. Vérifier chaque question : GAMEPLAY_GATE
  4. Assigner PAYOFF_TYPE
  5. Assigner FLAG_B2
  6. Écrire dans QUESTIONS
  7. Vérifier SUIVI_POOLS : STOCK_ACTUEL vs STOCK_CIBLE
  8. Si pool COMPLET → passer au suivant
```

---

# ORDRE DE GÉNÉRATION RECOMMANDÉ

PRIORITÉ_HAUTE (angles riches, payoff fort) :
QV-01 / QV-03 / QV-04 / QV-12 / QV-14

PRIORITÉ_MOYENNE :
QV-02 / QV-05 / QV-08 / QV-09 / QV-13

PRIORITÉ_BASSE (angles limités, risque saturation) :
QV-06 / QV-11 / IF-SF-01 / IF-SF-02 / IF-ROT-01 / IF-ROT-02 / IF-ROT-03

---

# GAMEPLAY_GATE — VALIDATION PAR QUESTION

Rejeter si FLAG_B2 = FAIL :

LONGUEUR:
- PASS : 6–9 mots
- WARNING : 10–13 mots
- FAIL : ≥ 14 mots

PAYOFF:
- FAIL : question plate, aucun déclencheur émotionnel identifiable
- FAIL : school_feeling détecté (ton cours, définition académique)
- FAIL : tourism_brochure (valorisation territoriale, patrimoine officiel)
- FAIL : encyclopédie (liste, explication, contexte lourd)

ORALITÉ:
- WARNING : formulation non conversationnelle
- FAIL : phrasing Wikipedia / institutionnel

COLLISION:
- WARNING : même mécanique que question précédente dans le pool
- FAIL : angle déjà utilisé dans le même pool

RÉPONSE:
- FAIL : réponse révélée dans le libellé
- FAIL : réponse devinable sans connaissance

---

# PAYOFF_TYPE (obligatoire par question)

Assigner UN type parmi :
- surprise       → "wait... ça vient de là ?"
- collision      → deux réalités incompatibles
- oralité        → mot / son / phrase mémorisable
- disproportion  → taille lieu vs rayonnement
- faux_reflexe   → réflexe immédiat incorrect

---

# TYPES_Q

1-Identification  → "Quel est... / Qui est... / Lequel..."
2-Nombre          → chiffre, quantité, rang
3-Année           → date, époque
4-Lieu            → géographie, localisation
5-Correspondance  → association item ↔ propriété

---

# GATE B2 → B3

Un pool passe en B3 si :
- STOCK_ACTUEL ≥ STOCK_CIBLE
- zéro FLAG_B2 = FAIL en attente
- variété PAYOFF_TYPE : min 3 types distincts représentés
- pas de série de 3+ questions consécutives de même TYPE_Q

Gate humaine obligatoire avant B3.

---

# RISQUES RUNTIME MAYENNE

SATURATION_WATCH:
- QV-14 (9 angles patois) → risque série patois → alterner avec autres pools
- QV-12 (8 angles agrégés) → risque hétérogénéité → vérifier cohérence thématique
- IF-ROT-03 (connexions joueurs) → risque sport trop dense en fin de quiz

ANGLES_FRAGILES (3 angles seulement) :
- QV-06 / QV-11 / IF-SF-01 / IF-ROT-02
→ générer avec soin — pas de recyclage angle

CLUSTER_07:
- LOCKED — ne pas générer sans validation humaine
- Voir A3_MAYENNE_CLUSTER_07_GUARDRAILS.md
