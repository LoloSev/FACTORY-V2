# PASS 2 — Infrastructure d'audit

**Date démarrage:** 2026-05-18  
**Phase:** Détection et correction de non-conformités  
**Cible:** Préparer 831 distracteurs pour production

---

## Objectifs PASS 2

### 1. Détection de collisions résiduelles
- Cross-validation triple: chaque distracteur vs 277 réponses
- Flagging immediate de collisions détectées
- Rapport d'anomalies

### 2. Vérification de format
- Cohérence casse/accents/ponctuation
- Pas de guillemets, italiques, caractères parasites
- Longueur/lisibilité consistante

### 3. Distribution de difficulté
- Audit N1/N2/N3 (26.4% / 67.5% / 2.9%)
- Repositionnement si écart vs cible (35% / 60% / 5%)
- Traçabilité par pool

### 4. Audit linguistique
- 100% français vérification
- Accents correctement placés
- Pas d'anglais ou mélanges

---

## Étapes d'audit

### ÉTAPE 1: Anti-collision (validé en PASS 1, double-check ici)
**Fichier de contrôle:** PASS_2_COLLISION_AUDIT.md
- Chaque distracteur scanné vs 277 réponses
- 0 match = ✅ CLEAR
- 1+ match = ❌ FLAGGED

### ÉTAPE 2: Format (nouveau contrôle)
**Fichier de contrôle:** PASS_2_FORMAT_AUDIT.md
- Tables markdown: cohérence vérifiée
- Casse: majuscules initiales vérifiées
- Accents: liste blanche appliquée
- Ponctuation: uniformité vérifiée

### ÉTAPE 3: Distribution difficulté (nouveau contrôle)
**Fichier de contrôle:** PASS_2_DIFFICULTY_AUDIT.md
- Comptage N1/N2/N3 par pool
- Écarts vs cible calculés
- Recommandations repositionnement

### ÉTAPE 4: Linguistique (nouveau contrôle)
**Fichier de contrôle:** PASS_2_LINGUISTIC_AUDIT.md
- Scan français 100%
- Flag si anglais/autre langue détecté
- Accents: vérifiation exhaustive

---

## Fichiers de sortie PASS 2

```
PASS_2_AUDIT/
├── PASS_2_INFRASTRUCTURE.md (ce fichier)
├── PASS_2_COLLISION_AUDIT.md (résultats)
├── PASS_2_FORMAT_AUDIT.md (résultats)
├── PASS_2_DIFFICULTY_AUDIT.md (résultats)
├── PASS_2_LINGUISTIC_AUDIT.md (résultats)
├── PASS_2_FLAGGED_ITEMS.md (consolidé)
└── PASS_2_FINAL_REPORT.md (synthèse)
```

---

## Critères de passage PASS 2 → PASS 3

| Critère | Seuil | Status |
|---------|-------|--------|
| **Collisions résiduelles** | 0 | À vérifier |
| **Format cohérent** | 100% | À auditer |
| **Distribution N1** | 30-40% | À analyser |
| **Distribution N2** | 55-65% | À analyser |
| **Distribution N3** | 3-7% | À analyser |
| **Couverture français** | 100% | À vérifier |

---

## Calendrier PASS 2

- **Étape 1 (Collision):** ~15 min
- **Étape 2 (Format):** ~20 min
- **Étape 3 (Difficulté):** ~15 min
- **Étape 4 (Linguistique):** ~10 min
- **Consolidation:** ~10 min
- **Total:** ~70 min

---

## Statut initial

✅ Infrastructure créée  
⏳ Audits en cours...

---
