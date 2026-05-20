---
name: SKILL_CREATION_CHECKLIST
version: 1.0
status: ACTIVE_REFERENCE
IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE
DEPENDENCY:
- MASTER_ARCHITECTURE.md
- glossaire_documentaire_factory.md
purpose: Processus rapide de création/intégration d'un nouveau skill dans la FACTORY
---

# SKILL CREATION CHECKLIST

**À exécuter À CHAQUE création ou modification de skill.**

**Durée estimée :** 15-30 min (dépend complexité)

---

## PHASE 1 : SKILL.MD

- [ ] Skill.md créé dans `_FACTORY/SKILLS/[skill-name]/SKILL.md`
- [ ] Section "When to Use" complétée (triggers, applicabilité)
- [ ] Section "The Process" avec étapes numérotées (min 5-7 étapes)
- [ ] Section "Examples" avec 2-3 walkthroughs concrets
- [ ] Section "Red Flags" : anti-patterns à éviter
- [ ] References to STD/MDE files linked

---

## PHASE 2 : IDENTIFIER CONCEPTS NOUVEAUX

**Extraire TOUS les nouveaux termes/concepts utilisés par le skill :**

### Concepts identifiés :
- [ ] Concept 1 : _______________
- [ ] Concept 2 : _______________
- [ ] Concept 3 : _______________
- [ ] ... (ajouter autant que nécessaire)

### Pour chaque concept, noter :
- **Definition** (1-2 phrases)
- **Type** : Métrique / Rôle / Status / Process / Other
- **Seuils/Valeurs** (si applicable)
- **Rules associées** (comportements obligatoires)

---

## PHASE 3 : GLOSSAIRE

**Ajouter entries dans `glossaire_documentaire_factory.md`**

```
[DEF-CAT-NNN]
CONCEPT_NAME:
Définition courte.

TYPE: [Métrique / Rôle / Status / Process]
[AUTRES CHAMPS SI APPLICABLE]

[RULE-CAT-NNN]
Comportement obligatoire ou seuil critique.
```

- [ ] Entry 1 créée : [DEF-___-___]
- [ ] Entry 2 créée : [DEF-___-___]
- [ ] Rules associées créées : [RULE-___-___]
- [ ] Glossaire sauvegardé

---

## PHASE 4 : MASTER_ARCHITECTURE.MD

- [ ] Workflow table : skill ajouté + statut [OK] ✓
- [ ] Bureau des Méthodes : MDE associée listée
- [ ] Standards : STD associées listées
- [ ] Document links section : skill/MDE/STD documentés
- [ ] References croisées vérifiées (dépendances correctes)

---

## PHASE 5 : MANIFEST.JSON

**Dans `.claude-plugin/manifest.json` :**

```json
{
  "skills": [
    {
      "name": "[skill-name]",
      "path": "[folder]/SKILL.md",
      "triggers": ["trigger1", "trigger2", "trigger3"]
    }
  ]
}
```

- [ ] Skill déclaré dans `manifest.json`
- [ ] Name = kebab-case
- [ ] Path = correct
- [ ] Triggers = 3+ variations naturelles
- [ ] Dependencies listées (STD/MDE)

---

## PHASE 6 : DOCUMENTATION CROISÉE

**Mise à jour des fichiers existants :**

### MDE associée :
- [ ] Section skill créée ou mise à jour
- [ ] Lien vers SKILL.md
- [ ] Lien vers STD associées

### STD associées :
- [ ] Règles que le skill exécute documentées
- [ ] Seuils/thresholds explicites
- [ ] Dépendances glossaire notées

---

## PHASE 7 : VÉRIFICATION FINALE

- [ ] Tous les links fonctionnent (MDE → SKILL.md → STD → glossaire)
- [ ] Zéro concept utilisé sans entry glossaire
- [ ] SKILL.md exécutable sans contexte externe : entrées, sorties, gates, enums et seuils présents
- [ ] Manifest.json valide JSON
- [ ] Pas de doublons avec skills existants
- [ ] Documentation CONSISTENCY_VALIDATED (pas de contradictions)

---

## CRITÈRE D'ACCEPTATION : SKILL READY

✓ Tous les checkboxes ci-dessus = SKILL ready pour usage  
✗ Manque une section = skill incomplet, bloque déploiement

---

**Après cette checklist :**
→ Skill peut être invoqué en production  
→ Intégration FACTORY complète  
→ Prêt pour tous les thèmes (cas source, Jeux olympiques, Rock, etc.)
RETEX_REF: RETEX_SKILL_CREATION_CHECKLIST_001

---

*Version 1.0 — 2026-05-17*
*Status: ACTIVE_REFERENCE*


