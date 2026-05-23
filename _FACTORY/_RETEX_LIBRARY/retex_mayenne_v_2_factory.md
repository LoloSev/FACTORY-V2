# RETEX — MAYENNE V2 / FACTORY V2

## Contexte

Ce RETEX documente la stabilisation réelle de la ligne MAYENNE dans Factory V2.

Le projet est passé par :
- dérive de contexte IA
- corruption XLSX
- faux pipelines
- collisions inter-pools
- explosion token
- limitations GitHub/connecteurs
- reconstruction depuis mémoire session
- stabilisation incrémentale

Résultat final atteint :

```text
A1 = OK
A2 = OK
A3 = OK
A4_V2 = GO
B2 = GO
PIPELINE = STABLE
TOTAL_STOCK = 132
GATE_B2 = PASS
```

---

# 1. Ce qui a cassé

## 1.1 Pipeline incohérent

Situation initiale détectée :
- A4 cassé/incompatible V2
- B2/B3/B5 placeholders
- exports inutilisables
- dashboard incohérent
- états contradictoires

Conséquence :
- impossibilité de scaler proprement
- génération massive dangereuse
- dette invisible

---

## 1.2 Génération massive

Tentative implicite :
- produire un gros volume immédiatement
- logique "277 questions d’un coup"

Conséquence :
- explosion token
- collisions massives
- perte de cohérence
- fatigue cognitive
- sessions IA instables

---

## 1.3 Dépendance aux snapshots ZIP

Le travail par ZIP successifs a créé :
- perte de continuité mentale
- versions ambiguës
- difficulté à identifier la version maître
- perte d’état implicite

Constat :
un ZIP n’est pas un environnement vivant.

---

## 1.4 XLSX corrompu

`B2_THEME.xlsx` est devenu inutilisable.

Causes probables :
- locks Windows
- Excel ouvert
- réécritures successives
- environnement Claude local

Conséquence :
- nécessité de reconstruction complète.

---

# 2. Ce qui a marché

## 2.1 Micro-opérations atomiques

Le vrai tournant du projet.

Au lieu de :
- grosses opérations
- refonte complète
- scans globaux

Méthode gagnante :
- une seule tâche
- un seul objectif
- une seule sortie attendue
- arrêt immédiat après succès

Exemple :
- réparer A4
- générer B2 uniquement
- enrichir un seul pool
- relancer gate
- stop

Effets :
- stabilité IA
- baisse token
- collisions détectables
- meilleure cohérence

---

## 2.2 Collision-first

Les collisions sont devenues :
- un outil de différenciation
- un révélateur de dérive éditoriale

Méthode validée :
1. charger collision map
2. identifier overlaps
3. choisir nouveaux angles
4. générer
5. gate

Résultat :
- diversité réelle des pools
- meilleure identité éditoriale
- baisse des faux doublons

---

## 2.3 Séparation structure / production

Découverte importante :

Avant :
- confusion entre stabilisation pipeline et production contenu

Après :
- A4 = structure
- B2 = gameplay/stock
- B3/B5 = validation éditoriale/factuelle

Effet :
- réduction énorme du bruit
- meilleure priorisation

---

## 2.4 Reconstruction depuis mémoire session

Moment critique :
- corruption de `B2_THEME.xlsx`
- impossibilité d’écriture normale

Décision correcte :
- reconstruire le fichier depuis le contexte session Claude
- ne pas tenter réparation binaire

Résultat :
- 132 questions récupérées
- Gate B2 PASS
- continuité sauvée

---

# 3. Ce qui a explosé les tokens

## 3.1 Tâches trop larges

Exemples dangereux :
- refaire le BIB
- générer 277 questions
- refactor global
- audit complet + correction + génération

Conséquence :
- dérive IA
- réponses floues
- perte de contraintes
- ralentissements

---

## 3.2 Mélange architecture + production

Très mauvais pattern :
- réfléchir Factory V2
- corriger pipeline
- produire contenu
- vérifier XLSX

Dans la même session.

---

## 3.3 Scans globaux répétés

Exemples :
- rescanner tout le repo
- relire tous les pools
- régénérer l’ensemble des collisions

Impact :
- coût énorme
- peu de valeur réelle

---

# 4. Ce qui réduit fortement les tokens

## 4.1 Prompts ultra-ciblés

Format validé :
- un pool
- une cible
- une sortie attendue
- contraintes courtes

---

## 4.2 git log minimal

Très utile :

```bash
git log -1 --stat --oneline
git status --short
```

Effets :
- contexte runtime réel
- coût faible
- réduction hallucinations état projet

---

## 4.3 Gates fréquents

Faire un gate après chaque pool.

Effets :
- dette faible
- collisions visibles tôt
- correction locale

---

## 4.4 Snapshot réguliers

Pattern validé :
- gate PASS
- snapshot ZIP immédiat

Permet :
- rollback
- reprise stable
- réduction anxiété projet

---

# 5. Découvertes importantes

## 5.1 Le vrai problème n’était pas le contenu

Le vrai problème était :
- la stabilité du pipeline
- la cohérence runtime
- la dette invisible

---

## 5.2 20 questions stables > 277 questions instables

Découverte psychologiquement difficile mais vraie.

Une petite base stable :
- peut scaler
- peut être enrichie
- peut survivre

Un énorme batch instable :
- casse rapidement
- devient ingérable

---

## 5.3 Les pools doivent devenir éditorialement distincts

La différenciation forte des pools est devenue essentielle.

Sinon :
- collisions
- répétitions
- sensation de quiz cloné

---

# 6. Règles absolues pour futures lignes

## Interdits

- génération massive immédiate
- refonte complète permanente
- scans globaux répétés
- mélange architecture + prod
- suppression de snapshots stables

---

## Obligations

- micro-opérations
- collision-first
- gates fréquents
- snapshots réguliers
- prompts compacts
- séparation structure / production

---

# 7. État final MAYENNE V2

MAYENNE n’est plus :
- un quiz cassé
- un prototype incohérent
- un BIB théorique

MAYENNE est devenu :

```text
LIGNE PILOTE FACTORY V2
```

Rôle :
- tester pipeline
- tester montée charge
- tester collisions
- tester stabilité IA
- définir standards futures lignes

---

# 8. Prochaine étape logique

Pas :
- refaire le système
- produire 277 questions d’un coup

Mais :
- continuer enrichissement incrémental
- maintenir stabilité
- préparer B3/B5 proprement
- transformer les règles MAYENNE en protocole Factory V2 global

