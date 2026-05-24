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

## RÈGLE 02 — TSV = RUNTIME TABLES / XLSX = VUE HUMAINE

Les TSV portent (source de vérité machine) :
- mappings
- pools
- quotas
- coverage
- scoring
- rotations
- assignations
- runtime combinatoire
- production dense

Le xlsx est une vue générée par script (generate_xlsx_view.py) — jamais la source de vérité.

Les TSV et xlsx ne portent pas :
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
- `CONFIG.yaml` de la ligne active — métadonnées THEME / STATUT
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
- TSV fichier(s) de la phase active uniquement (ex: ANGLES.tsv + POOLS.tsv pour B2)
- `SKILL.md` si exécution via skill

CONTENU_INTERDIT:
- MDE des autres phases
- STD non référencés par DEPENDENCY
- TSV des phases non actives
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
Nouvelle session                → L0 (+ CONFIG.yaml ligne active)
Tâche de production identifiée  → L0 + L1 (MDE + TSV de la phase)
Ambiguïté / conflit détecté     → L0 + L1 + L2 (fichier ciblé)
Audit / décision complexe       → L0 + L2 + L3 (sur demande)
```

TSV LOADING RULE:
```txt
Phase A3 → ITEMS.tsv + ANGLES.tsv (écriture)
Phase A4 → ITEMS.tsv + ANGLES.tsv (lecture) + POOLS.tsv (écriture)
Phase B2 → POOLS.tsv + ANGLES.tsv (lecture) + QUESTIONS.tsv (écriture)
Phase B3 → QUESTIONS.tsv (lecture) + DISTRACTEURS.tsv (écriture)
Phase B5 → QUESTIONS.tsv + DISTRACTEURS.tsv (lecture) + QA.tsv (écriture)
```

---

## SCHÉMAS CIBLES — FICHIERS TSV

FORMAT: TSV (tab-separated) — encodage UTF-8 strict
SOURCE_OF_TRUTH: TSV files
HUMAN_VIEW: generate_xlsx_view.py on demand

### CONFIG.yaml
```yaml
THEME: str
DATE_INIT: YYYY-MM-DD
STOCK_CIBLE: int
VERSION: str
STATUT: INIT | EN_COURS | VALIDE | EXPORTE
```

### ITEMS.tsv
```txt
ITEM_ID | LIBELLE | CLUSTER | RICHESSE | NIVEAU_POTENTIEL | SIGNAL_RUNTIME | SOURCE_BIB
```

### ANGLES.tsv
```txt
ANGLE_ID | ITEM_ID | ANGLE_COURT | MECANIQUE | NIVEAU_ANGLE | POOL_CIBLE | COLLISION_WITH | QUOTA | STATUT
```

### POOLS.tsv
```txt
POOL_ID | TYPE | POSITION_QUIZ | THEME_LABEL | MODE | SOUS_THEMES | ITEMS_ASSIGNES | COUVERTURE_NIVEAU | STOCK_CIBLE | STOCK_ACTUEL | SIGNAL_RUNTIME | FAISABILITE
```

### QUESTIONS.tsv
```txt
Q_ID | POOL_ID | ANGLE_ID | LIBELLE | REPONSE | NIVEAU_QUESTION | TYPE_Q | WORD_COUNT | LENGTH_STATUS | REQUIRED_FEELING | STATUT_B2
```

### DISTRACTEURS.tsv
```txt
Q_ID | POOL_ID | NIVEAU_QUESTION | LIBELLE_Q | REPONSE | D1 | D2 | D3 | NIVEAU_CONFIRME | ECART_CIBLE | STATUT_B3
```

### QA.tsv
```txt
Q_ID | POOL_ID | NIVEAU_QUESTION | LIBELLE_Q | REPONSE | D1 | D2 | D3 | QA_STATUS | FLAGS | NOTES_COURTES | DECISION_RUNTIME
```

### SOMMAIRE (derived — not source)
```txt
generated by generate_sommaire.py from POOLS.tsv + QUESTIONS.tsv + QA.tsv
```
