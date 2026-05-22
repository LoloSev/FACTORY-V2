# ACTIVE_CONTEXT_MANIFEST

STATUT: ACTIVE
ROLE: point d'entrée session — règles de chargement runtime actives

DEPENDENCY:
- FACTORY_RUNTIME_LEXICON.md
- TOKEN_ECONOMY_RUNTIME_PROTOCOL.md
- MASTER_ARCHITECTURE.md

---

## POLITIQUE DE CHARGEMENT

Référence : `TOKEN_ECONOMY_RUNTIME_PROTOCOL.md` — section COUCHES DE CHARGEMENT RUNTIME.

Résumé opérationnel :

```txt
Nouvelle session                → L0 uniquement
Tâche de production identifiée  → L0 + L1 (MDE + STD phase)
Ambiguïté / conflit             → ajouter L2 (fichier ciblé)
Audit / décision complexe       → ajouter L3 (sur demande humaine)
Archives / CHANTIER             → L4 — ne jamais charger
```

---

## RÈGLES DE RÉSOLUTION DE CONTENU

En cas de duplication ou d'ambiguïté, résoudre vers la source unique :

```txt
terme runtime / taxonomie       → FACTORY_RUNTIME_LEXICON.md
QA status                       → STD_QA_status_rules.md
QA validation B5                → FACTORY_QA_RULES.md
collision inter-pools           → STD_GLOBAL_pool_collision_rules.md
terme documentaire              → glossaire_documentaire_factory.md
usage BIB                       → STD_BIB_USAGE.md
```

---

## CONTRAINTES ACTIVES

```txt
DO_NOT_LOAD_DEFAULT: RETEX (tout fichier RETEX_*)
DO_NOT_LOAD_DEFAULT: _LIGNES/ outputs de production
DO_NOT_LOAD_DEFAULT: fichiers STATUS: ARCHIVED
DO_NOT_LOAD_DEFAULT: CHANTIER MDE STD/
DO_NOT_DUPLICATE: taxonomies runtime (→ FACTORY_RUNTIME_LEXICON.md)
DO_NOT_DUPLICATE: machine states (→ FACTORY_RUNTIME_LEXICON.md)
```

---

## ACCEPTANCE_CRITERIA

- chaque STD/MDE actif a un bloc DEPENDENCY explicite
- RETEX_LOADING: ON_DEMAND_ONLY dans tout fichier STD
- aucun concept runtime redéfini hors FACTORY_RUNTIME_LEXICON.md

---

*ACTIVE_CONTEXT_MANIFEST.md — 2026-05-22*
