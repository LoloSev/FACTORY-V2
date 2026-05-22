# TOKEN_ECONOMY_IMPLEMENTATION_2026-05-21.md

STATUT: APPLIED_BASELINE
SOURCE: factory_v_2_token_economy_master_analysis.md

## ACTIONS APPLIQUÉES

- ajout du lexique runtime central
- ajout du protocole TOKEN_ECONOMY runtime-first
- ajout d'un audit script machine-first
- verrouillage de MAYENNE comme ligne prototype de refonte
- conservation des fichiers existants sans suppression brutale

## DÉCISION

MAYENNE sert de banc d'essai pour remodeler les étapes FACTORY.
Les autres lignes restent intactes tant que les schemas cibles ne sont pas validés sur MAYENNE.

## PRIORITÉ IMMÉDIATE

1. normaliser les templates XLSX
2. normaliser MAYENNE A2/A3/A4
3. adapter gates
4. seulement ensuite migrer B2/B3/B5/EXPORT

## POINTS DE VIGILANCE

- ne plus multiplier les documents explicatifs
- ne pas dupliquer les taxonomies hors lexique
- éviter les colonnes de prose dans XLSX
- préférer états machine et tags fermés
