# PASS 2 — Audit de distribution difficulté

**Date:** 2026-05-18  
**Portée:** 277 questions / 831 distracteurs  
**Cible:** N1: 35%, N2: 60%, N3: 5%

---

## Distribution actuelle

### Résultats bruts

| Difficulté | Comptage | Pourcentage | Cible | Écart |
|------------|----------|-------------|-------|-------|
| **N1** | 73 | 26.4% | 35% | -8.6% ⚠️ |
| **N2** | 187 | 67.5% | 60% | +7.5% ⚠️ |
| **N3** | 8 | 2.9% | 5% | -2.1% ⚠️ |
| **N/D** | 9 | 3.2% | 0% | +3.2% ⚠️ |
| **TOTAL** | **277** | **100%** | **100%** | |

---

## Analyse par pool

### IF-SF (16 questions)

| Difficulté | Comptage | % | Statut |
|------------|----------|---|--------|
| N1 | 6 | 37.5% | ✓ Correct |
| N2 | 10 | 62.5% | ✓ Correct |
| N3 | 0 | 0% | ⚠️ Bas |
| **Total** | **16** | **100%** | ✓ |

### IF-ROT (36 questions)

| Difficulté | Comptage | % | Statut |
|------------|----------|---|--------|
| N1 | 6 | 16.7% | ⚠️ Bas |
| N2 | 30 | 83.3% | ⚠️ Haut |
| N3 | 0 | 0% | ⚠️ Bas |
| **Total** | **36** | **100%** | ⚠️ |

### QV-01-05 (75 questions)

| Difficulté | Comptage | % | Statut |
|------------|----------|---|--------|
| N1 | 22 | 29.3% | ✓ Accepte |
| N2 | 53 | 70.7% | ✓ Accepte |
| N3 | 0 | 0% | ⚠️ Bas |
| **Total** | **75** | **100%** | ✓ |

### QV-06-10 (75 questions)

| Difficulté | Comptage | % | Statut |
|------------|----------|---|--------|
| N1 | 28 | 37.3% | ✓ Correct |
| N2 | 46 | 61.3% | ✓ Correct |
| N3 | 1 | 1.3% | ⚠️ Bas |
| **Total** | **75** | **100%** | ✓ |

### QV-11-15 (75 questions)

| Difficulté | Comptage | % | Statut |
|------------|----------|---|--------|
| N1 | 17 | 22.7% | ⚠️ Bas |
| N2 | 55 | 73.3% | ⚠️ Haut |
| N3 | 3 | 4.0% | ✓ Accepte |
| N/D | 0 | 0% | ✓ |
| **Total** | **75** | **100%** | ⚠️ |

---

## Analyse d'écarts

### Écart N1: -8.6% (26.4% vs 35% cible)

**Pools sous-représentés:**
- IF-ROT: 16.7% (cible: 35%)
- QV-11-15: 22.7% (cible: 35%)

**Recommandation:**
Repositionner ~24 questions IF-ROT et QV-11-15 de N2 vers N1 en PASS 3 pour atteindre +8.6%.

### Écart N2: +7.5% (67.5% vs 60% cible)

**Pools sur-représentés:**
- IF-ROT: 83.3% (cible: 60%)
- QV-11-15: 73.3% (cible: 60%)

**Recommandation:**
Ces questions N2 doivent être reclassées en N1 en PASS 3 (voir écart N1 ci-dessus).

### Écart N3: -2.1% (2.9% vs 5% cible)

**Pools sous-représentés:**
- IF-SF: 0% (cible: 5%)
- IF-ROT: 0% (cible: 5%)
- QV-01-05: 0% (cible: 5%)

**Recommandation:**
Ajouter ~8-10 questions N3 en PASS 3, distribuées entre IF-SF, IF-ROT, et QV pools.

---

## Stratégie de correction (PASS 3)

### Étape 1: Reclassification N2 → N1
**Cibles:** IF-ROT et QV-11-15
**Nombre:** ~24 questions
**Effet:** Ramène N1 de 26.4% à 35%, N2 de 67.5% à 60%

### Étape 2: Enrichissement N3
**Cibles:** IF-SF, IF-ROT, QV-01-05
**Nombre:** ~8-10 questions
**Effet:** Ramène N3 de 2.9% à 5%

### Étape 3: Validation
**Post-correction attendu:**
- N1: ~35% ✓
- N2: ~60% ✓
- N3: ~5% ✓

---

## Distribution de faisabilité

| Action | Faisabilité | Effort | Risk |
|--------|------------|--------|------|
| Reclassifier N2→N1 | ✓ Facile | 30 min | Bas |
| Ajouter N3 | ✓ Moyen | 45 min | Moyen |
| Revalider après correction | ✓ Facile | 20 min | Bas |

---

## Recommandations pour PASS 3

✅ **AUDIT COMPLETE:** Distribution écarts identifiés et corrigibles

**Action requise:**
1. Reclassifier ~24 questions N2 → N1 (IF-ROT: ~12, QV-11-15: ~12)
2. Ajouter ~8-10 questions N3 dans pools équilibrés
3. Revalider post-correction

**Délai estimé:** 90 min (inclus reclassification + validation)

---
