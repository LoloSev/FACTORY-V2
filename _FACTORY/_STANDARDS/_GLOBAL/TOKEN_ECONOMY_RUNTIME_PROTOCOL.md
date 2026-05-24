# TOKEN_ECONOMY_RUNTIME_PROTOCOL.md

STATUT: ACTIVE
SOURCE: factory_v_2_token_economy_master_analysis.md
ROLE: protocole d'application machine-first pour FACTORY V2.

## FORMULE CIBLE

```txt
MINIMUM TOKENS
+ MINIMUM AMBIGUITY
+ MAXIMUM GAMEPLAY SIGNAL
+ MAXIMUM RUNTIME STABILITY
```

## RÈGLE 01 — RESPONSABILITÉ UNIQUE

Chaque fichier porte une seule responsabilité runtime.
Interdit:
- méta-document expliquant d'autres documents
- double gouvernance
- prose de justification longue
- concept dupliqué hors lexique

## RÈGLE 02 — XLSX = RUNTIME TABLES ONLY

Les XLSX portent:
- mappings
- pools
- quotas
- coverage
- scoring
- rotations
- assignations
- runtime combinatoire
- production dense

Les XLSX ne portent pas:
- philosophie
- gouvernance
- storytelling
- rationalisations IA
- commentaires longs
- logique éditoriale diffuse

## RÈGLE 03 — MARKDOWN = RÈGLES ET ARBITRAGES

Les markdown portent:
- logique runtime
- anti-patterns
- taxonomies
- policies
- supervision humaine
- arbitrages structurels

## RÈGLE 04 — TAXONOMIES FERMÉES

Les mots flottants doivent devenir:
- tags runtime
- IDs gameplay
- états machine
- listes fermées

## RÈGLE 05 — LEXIQUE CENTRAL

Toute taxonomie partagée vit dans:
`_FACTORY/_STANDARDS/_GLOBAL/FACTORY_RUNTIME_LEXICON.md`

Les autres fichiers référencent le lexique sans redéfinir.

## RÈGLE 06 — MIGRATION PROGRESSIVE

Ne pas casser une ligne existante pour normaliser.
Ordre:
1. normaliser templates
2. normaliser MAYENNE prototype
3. ajuster gates
4. généraliser aux autres lignes

## COUCHES DE CHARGEMENT RUNTIME

Règle fondamentale : charger le minimum suffisant pour exécuter la tâche.
Ne jamais charger par défaut ce qui n'est pas requis par la tâche en cours.

---

### L0 — BOOTSTRAP (obligatoire, toujours, toute session)

```txt
RÔLE        : constantes projet + taxonomies machine + état git
COÛT TOKENS : ~800 tokens
```

CONTENU_AUTORISÉ:
- `MASTER_ARCHITECTURE.md` — constantes (277, 20 pools, catalogue)
- `FACTORY_RUNTIME_LEXICON.md` — machine states, taxonomies fermées
- `git log -1 --stat --oneline` + `git status --short` — état runtime

CONTENU_INTERDIT:
- STD détaillés
- MDE
- RETEX
- contenu lignes

CONDITION_CHARGEMENT: toute session sans exception
CONDITION_NON_CHARGEMENT: aucune — L0 est incompressible

---

### L1 — PHASE RUNTIME (chargé selon phase active)

```txt
RÔLE        : règles et méthode de la phase en cours
COÛT TOKENS : ~2 000–4 000 tokens
HÉRITAGE    : L0 requis
```

CONTENU_AUTORISÉ:
- MDE de la phase active (ex: `MDE_B2_generation.md`)
- STD directs listés dans le bloc DEPENDENCY du MDE
- `SKILL.md` si exécution via skill

CONTENU_INTERDIT:
- MDE des autres phases
- STD non référencés par DEPENDENCY
- glossaire complet
- RETEX

CONDITION_CHARGEMENT: phase identifiée + tâche de production active
CONDITION_NON_CHARGEMENT: tâche documentaire / audit / navigation inter-phases

SIGNAL_CHARGEMENT: "je travaille sur B2 pool X" / "générer les distracteurs de Y"

---

### L2 — RÉFÉRENCE TRANSVERSE (chargé sur signal explicite)

```txt
RÔLE        : résolution d'ambiguïté, conflit de règles, audit
COÛT TOKENS : ~3 000–8 000 tokens selon fichier
HÉRITAGE    : L0 + L1 requis
```

CONTENU_AUTORISÉ (charger uniquement le fichier nécessaire, pas l'ensemble):
- `HIERARCHIE_REGLEMENTAIRE.md` — si conflit de règles
- `FACTORY_QA_RULES.md` — si audit QA
- `STD_GLOBAL_pool_collision_rules.md` — si collision détectée
- `QUIZ_ASSEMBLY_RULES.md` — si questions d'assemblage final
- `glossaire_documentaire_factory.md` — si ambiguïté sur un terme
- `PIPELINE_V2.md` — si navigation inter-phases ou reprise de ligne

CONTENU_INTERDIT:
- charger tout L2 simultanément
- RETEX
- contenu lignes production

CONDITION_CHARGEMENT: signal explicite de besoin (terme ambigu, conflit, audit)
CONDITION_NON_CHARGEMENT: production courante sans ambiguïté

SIGNAL_CHARGEMENT: "quelle règle s'applique ?" / "collision détectée" / "terme X = ?"

---

### L3 — DÉCISION / AUDIT (chargé sur demande humaine explicite)

```txt
RÔLE        : retours d'expérience, anti-régression, arbitrages complexes
COÛT TOKENS : ~10 000+ tokens
HÉRITAGE    : L0 + L1 + L2 selon contexte
```

CONTENU_AUTORISÉ:
- `_RETEX_LIBRARY/RETEX_INDEX.md`
- RETEX spécifiques (`_RETEX_LIBRARY/retex_mayenne_v_2_factory.md`, etc.)
- Fichiers SESSION_RESUME

CONTENU_INTERDIT:
- chargement automatique
- chargement sans demande humaine
- chargement en production courante

CONDITION_CHARGEMENT: demande humaine explicite ("reprendre les retours", "anti-régression", "qu'avait-on décidé sur X ?")
CONDITION_NON_CHARGEMENT: par défaut — toujours

---

### L4 — ARCHIVES (jamais en runtime)

```txt
RÔLE        : traçabilité historique uniquement
COÛT TOKENS : ne pas charger
```

CONTENU:
- fichiers `STATUS: ARCHIVED`
- dossiers `_ARCHIVE_PRE_REFONTE/`
- fichiers `_frozen`
- `CHANTIER MDE STD/` (suivi chantier terminé)
- outputs lignes production (`_LIGNES/` sauf gate requise)

CONDITION_CHARGEMENT: aucune — L4 n'est jamais chargé en runtime

---

### RÈGLE DE DÉCISION RAPIDE

```txt
Nouvelle session                → L0
Tâche de production identifiée  → L0 + L1
Ambiguïté / conflit détecté     → L0 + L1 + L2 (fichier ciblé)
Audit / décision complexe       → L0 + L2 + L3 (sur demande)
```

---

## SCHÉMAS CIBLES

### A2 ITEMS
```txt
ITEM_ID | SECTION | ITEM | SIGNAL_RUNTIME | FORCE | SOURCE_BIB
```

### A3 ITEMS
```txt
ITEM_ID | LIBELLE | CLUSTER | RICHESSE | SIGNAL_RUNTIME | SOURCE_BIB
```

### A3 ANGLES
```txt
ANGLE_ID | ITEM_ID | ANGLE_COURT | MECANIQUE | NIVEAU | POOL_CIBLE | COLLISION_WITH | QUOTA | STATUT
```

### A4 POOLS
```txt
POOL_ID | TYPE | POSITION_QUIZ | COUVERTURE_NIVEAU | SIGNAL_RUNTIME | MODE | STOCK_CIBLE | STOCK_ACTUEL | FAISABILITE
```

### B2 QUESTIONS
```txt
Q_ID | POOL_ID | ANGLE_ID | LIBELLE | REPONSE | NIVEAU_QUESTION | TYPE_Q | WORD_COUNT | LENGTH_STATUS | REQUIRED_FEELING | STATUT_B2
```

### B3 FLAGS
```txt
Q_ID | FLAG_TYPE | SEVERITY | FIX_ACTION | STATUT_CORRECTION
```

### B5 FINAL
```txt
Q_ID | POOL_ID | NIVEAU_QUESTION | LIBELLE_Q | REPONSE | D1 | D2 | D3 | QA_STATUS | FLAGS | NOTES_COURTES | DECISION_RUNTIME
```

### EXPORT
```txt
Q_ID | POOL_ID | POSITION_QUIZ | NIVEAU_QUESTION | LIBELLE | REPONSE | D1 | D2 | D3 | TYPE_Q | QA_STATUS | FLAG_VEILLE
```
