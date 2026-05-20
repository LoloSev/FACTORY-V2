# TRAITEMENT DE LA BASE CDM — DOCUMENTATION PRÉCISE

**Fichier traité :** `BIPREGEN_CDM.txt`
**Fichier original conservé :** `BIB_CDM.txt` (01_APPRO)
**Fichier angles :** `ANGIPREGEN_CDM.txt`
**Date :** 13/05/2026

---

## 1. État initial

Le fichier `BIB_CDM.txt` était une base de connaissances brute sur la Coupe du Monde FIFA, organisée en 9 sections thématiques :

1. Joueurs (20 items)
2. Stades (7 items)
3. Matchs (15 items)
4. Buteurs toutes éditions (10 items)
5. Meilleurs buteurs par édition (10 items)
6. Finalistes (10 items)
7. Participations (15 items)
8. Anecdotes / Polémiques (15 items)
9. Autres records (9 items)

**Problèmes identifiés :**
- Indicateurs de difficulté en fin de ligne codés `F` / `I` / `D` — format non standard
- Sections 3 (Matchs) et 4 (Buteurs) : items sur plusieurs lignes — inexploitable tel quel
- Aucun identifiant unique par item
- Aucune statistique de répartition
- Aucune définition des angles interrogeables

---

## 2. Transformations appliquées (dans l'ordre)

### 2.1 Correction des indicateurs de difficulté
- `— F` → `— Niveau 1`
- `— I` → `— Niveau 2`
- `— D` → `— Niveau 3`

⚠️ Les `(V)` et `(D)` dans la section Finalistes (Victoire/Défaite) ont été laissés intacts.

### 2.2 Mise en ligne unique
**Section 3 — Matchs (Type A) :** fusion titre + description avec séparateur `—`
**Section 4 — Buteurs (Type B) :** fusion avec séparateur `/` pour les détails par édition

### 2.3 Système de codage
Attribution d'un identifiant unique `CDM-[CAT]-[N°]-[NIV]` sur chaque ligne.

| Code | Section |
|------|---------|
| `JOU` | Joueurs |
| `STA` | Stades |
| `MAT` | Matchs |
| `BUT` | Buteurs toutes éditions |
| `BUE` | Meilleurs buteurs par édition |
| `FIN` | Finalistes |
| `PAR` | Participations |
| `ANE` | Anecdotes / Polémiques |
| `REC` | Records |

### 2.4 Tableau de statistiques + proportions
Comptage par section × niveau, % réel vs % cible FACTORY (40/40/20).

### 2.5 Reclassement de 4 items N1 → N2

| Code | Item | Motif |
|------|------|-------|
| CDM-JOU-18 | Manuel Neuer | Gardien, moins visible du grand public |
| CDM-JOU-20 | Luka Modrić | Pas champion du monde, moins emblématique |
| CDM-MAT-12 | Finale 2010 | Moins mémorable que 1998, 2018, 2022 |
| CDM-FIN-10 | Angleterre | 1 seule finale (1966), moins évidente |

Résultat : N1=40% / N2=40% / N3=20% — parfaitement conforme.

### 2.6 Index par niveau
Liste des codes regroupés par niveau (N1 / N2 / N3) avec quotas.

### 2.7 Légende + Historique
Ajoutés en tête de document.

---

## 3. Création du fichier ANGIPREGEN_CDM.txt

### Calibrage des quotas

Quotas naturels :
- N1 : 124 (cible 120, surplus +4)
- N2 : 120 (cible 120, parfait)
- N3 : 65 (cible 60, surplus +5)

**9 angles supprimés** pour atteindre exactement 120 / 120 / 60.

Suppressions N1 (-4) :
- CDM-JOU-08 : suppression A4 "Nombre de participations"
- CDM-JOU-19 : suppression A4 "Nombre de participations"
- CDM-MAT-07 : suppression A4 "Phase de compétition"
- CDM-MAT-15 : suppression A4 "Hat-trick Mbappé" → déplacé en exclusion

Suppressions N3 (-5) :
- CDM-JOU-13 : suppression A4 "Nombre de participations"
- CDM-JOU-15 : suppression A4 "Nombre de participations"
- CDM-BUE-05 : suppression A3 "Année"
- CDM-BUE-06 : suppression A3 "Année"
- CDM-REC-03 : suppression A4 "Année"

---

## 4. Résultats finals

| Niveau | Items | Questions à générer |
|--------|-------|---------------------|
| N1 | 44 | 120 |
| N2 | 44 | 120 |
| N3 | 23 | 60 |
| **Total** | **111** | **300** |

---

## 5. Prochaine étape

Générer les 300 questions en suivant `ANGIPREGEN_CDM.txt` :
- item par item
- angle par angle
- sans jamais dépasser le quota défini
- en respectant les exclusions inter-items notées par ⚠️
