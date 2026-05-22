# Stabilisation locale — 2026-05-21

## Verdict
Base cohérente, utilisable comme version maître locale, mais MAYENNE n'est pas publiable.

## Corrections appliquées
- `check_dashboard.py` : les lignes `_CDM`, `_MAYENNE`, etc. ne sont plus ignorées.
- `check_dashboard.py` : les scripts `gate_*.py` sont appelés depuis `_FACTORY/_SCRIPTS/`.
- `gate_utils.py` : les chemins stockés dans `pipeline_state.json` sont maintenant relatifs à `_FACTORY`, pas absolus machine.
- Dashboard régénéré : `check_dashboard.py` retourne maintenant `NO_OP`.

## État MAYENNE après gates
- A4 : NO_GO — feuille `POOLS` absente dans `A4_MAYENNE_POOL_ENGINE.xlsx`.
- B2 : NO_GO — bloqué par A4 + `TYPE_Q` invalide `[1-5]`.
- B3 : NO_GO — bloqué par B2.
- B5 : NO_GO — bloqué par B3.
- EXPORT : NO_GO — bloqué par B5 + stock insuffisant `1/277 questions`.

## Conclusion opérationnelle
MAYENNE doit repartir au niveau A4/B2 proprement. Les fichiers B2/B3/B5/EXPORT présents sont des placeholders ou artefacts incomplets, pas une version publiable.
