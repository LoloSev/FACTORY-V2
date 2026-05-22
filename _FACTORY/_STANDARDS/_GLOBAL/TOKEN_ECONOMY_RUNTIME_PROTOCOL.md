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
POOL_ID | TYPE | POSITION_QUIZ | CIBLE_NIVEAU | SIGNAL_RUNTIME | MODE | STOCK_CIBLE | STOCK_ACTUEL | FAISABILITE
```

### B2 QUESTIONS
```txt
Q_ID | POOL_ID | ANGLE_ID | LIBELLE | REPONSE | CIBLE_NIVEAU | TYPE_Q | WORD_COUNT | LENGTH_STATUS | REQUIRED_FEELING | STATUT_B2
```

### B3 FLAGS
```txt
Q_ID | FLAG_TYPE | SEVERITY | FIX_ACTION | STATUT_CORRECTION
```

### B5 FINAL
```txt
Q_ID | POOL_ID | CIBLE_NIVEAU | LIBELLE_Q | REPONSE | D1 | D2 | D3 | QA_STATUS | FLAGS | NOTES_COURTES | DECISION_RUNTIME
```

### EXPORT
```txt
Q_ID | POOL_ID | POSITION_QUIZ | CIBLE_NIVEAU | LIBELLE | REPONSE | D1 | D2 | D3 | TYPE_Q | QA_STATUS | FLAG_VEILLE
```
