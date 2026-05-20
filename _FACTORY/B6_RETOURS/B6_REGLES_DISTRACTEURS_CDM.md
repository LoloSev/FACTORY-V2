# B6 — RÈGLES GÉNÉRATION DISTRACTEURS CDM 2026

**Statut**: Référence validée — 277 questions × 3 distracteurs = 831 à générer  
**Contrainte globale**: Aucun distracteur ne doit figurer dans la liste des 277 réponses correctes du quiz.

---

## TYPE 1 — IDENTIFICATION
*Pattern: "Quel joueur / stade / équipe..." → réponse = nom propre*

**Exemple de question**: "Quel joueur portugais a terminé meilleur buteur en 1966 ?"  
**Réponse correcte**: "Eusebio"

**RÈGLE 1.1 - Sélection**  
Puiser dans la base CDM globale : joueurs célèbres ayant participé à plusieurs éditions, dans la même catégorie (attaquant si la réponse est un attaquant, équipe du même continent si la réponse est une équipe). Ne pas inventer de noms. Priorité aux noms reconnaissables par un amateur moyen.

**RÈGLE 1.2 - Cohérence**  
Les distracteurs doivent partager au moins une propriété contextuelle avec la réponse :
- Même position (attaquant / gardien / défenseur) si la question implique un rôle
- Même continent ou même époque si la question est générale
- Même type d'entité (joueur ≠ entraîneur ≠ stade)

**RÈGLE 1.3 - Exclusion**  
- Vérifier contre la liste complète des 277 réponses : tout nom déjà utilisé comme réponse correcte est interdit.
- Ne pas réutiliser un distracteur déjà assigné à une autre question du même pool si possible.

**RÈGLE 1.4 - Vraisemblance**  
Élevée : le joueur doit être réellement connu et associable au contexte (CDM, période). Un amateur moyen doit pouvoir hésiter. Éviter les noms totalement obscurs ou hors contexte.

**RÈGLE 1.5 - Difficulté N1 vs N3**  
- N1 : distracteurs d'une nationalité clairement différente, ou d'une autre époque (ex: joueur des années 2010 pour une question sur 1966)
- N2 : même nationalité ou même période, mais pas le bon rôle / palmarès
- N3 : même nationalité, même époque, même rôle — seul le détail précis les distingue (ex: Pauleta aussi portugais, aussi attaquant, aussi CDM)

**RÈGLE 1.6 - Format**  
Reproduire exactement la casse de la réponse correcte : si la réponse est "Eusebio", les distracteurs sont "Pepe", "Pauleta", "Simão Sabrosa" (majuscule initiale, pas de guillemets, pas de casse tout-caps).  
Pour les accents : respecter l'orthographe officielle FIFA (ex: "Pelé" et non "Pele" si la réponse correcte utilise l'accent).

**Exemple appliqué**  
Q: "Quel joueur portugais a terminé meilleur buteur en 1966 ?"  
R: "Eusebio"  
Distracteurs: ["Pauleta", "Figo", "Rui Costa"]  
→ Vérification anti-collision 277 réponses : aucune collision ✓

---

## TYPE 2 — CHIFFRES
*Pattern: "Combien de buts / de fois / d'éditions..." → réponse = nombre entier*

**Exemple de question**: "Combien de buts Ronaldo (Brésil) a-t-il marqué en Coupe du monde ?"  
**Réponse correcte**: "15"

**RÈGLE 2.1 - Sélection**  
Générer des nombres voisins de la réponse correcte, en restant dans un ordre de grandeur cohérent. Ne jamais utiliser 0 pour une question de type "meilleur buteur". Utiliser les chiffres réels du CDM si disponibles (ex: vrais totaux de buts d'autres joueurs).

**RÈGLE 2.2 - Cohérence**  
Les distracteurs doivent être plausibles dans le contexte de la question :
- Pour des buts en CDM : fourchette 1–16 (maximum historique réaliste)
- Pour des éditions / participations : fourchette 1–6
- Pour des années : uniquement des années d'éditions CDM réelles

**RÈGLE 2.3 - Exclusion**  
- Vérifier que le nombre n'est pas une réponse correcte à une autre question du quiz (ex: si "8" est déjà une réponse correcte pour une autre question de chiffres dans le même pool).
- Ne jamais utiliser le nombre exact de la réponse correcte comme distracteur (évidence).

**RÈGLE 2.4 - Vraisemblance**  
Moyenne à élevée : les nombres doivent paraître possibles. Pour N1, un écart large est acceptable. Pour N3, l'écart doit être minimal (±1 ou ±2) pour forcer la réflexion.

**RÈGLE 2.5 - Difficulté N1 vs N3**  
- N1 : écart ±4 ou plus (ex: R=15 → distracteurs 8, 11, 20)
- N2 : écart ±2 à ±3 (ex: R=15 → distracteurs 12, 13, 18)
- N3 : écart ±1 (ex: R=15 → distracteurs 13, 14, 16) — attention collision

**RÈGLE 2.6 - Format**  
Chiffres arabes uniquement ("15" et non "quinze"). Pas d'unités sauf si la réponse correcte en contient. Pas de décimales pour des dénombrements entiers.

**Exemple appliqué**  
Q: "Combien de buts Ronaldo (Brésil) a-t-il marqués en CDM ?"  
R: "15"  
Distracteurs N2: ["12", "13", "17"]  
→ Vérification anti-collision 277 réponses ✓

---

## TYPE 3 — ANNÉES / ÉDITIONS
*Pattern: "En quelle année / lors de quelle édition..." → réponse = année (ex: "1998") ou "édition 1998"*

**Exemple de question**: "En quelle année la France a-t-elle remporté sa première Coupe du monde ?"  
**Réponse correcte**: "1998"

**RÈGLE 3.1 - Sélection**  
Utiliser exclusivement les années d'éditions CDM réelles (1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022, 2026). Jamais une année non-CDM.

**RÈGLE 3.2 - Cohérence**  
Les distracteurs doivent être des éditions où l'événement décrit aurait pu logiquement se produire (ex: pour "première victoire de la France" → éditions où la France a participé et était compétitive : 1982, 1986, 2006).

**RÈGLE 3.3 - Exclusion**  
- Vérifier contre les 277 réponses : toute année déjà utilisée comme réponse correcte dans le même pool thématique est à éviter en priorité.
- Ne jamais utiliser une année qui est factuellement liée à la même équipe/joueur pour un événement similaire.

**RÈGLE 3.4 - Vraisemblance**  
Les années choisies doivent être des éditions où le contexte de la question était actif (ex: ne pas proposer 1930 pour une question sur Messi).

**RÈGLE 3.5 - Difficulté N1 vs N3**  
- N1 : années très éloignées ou clairement hors contexte (ex: pour R=1998 → 1966, 1974, 2014)
- N2 : éditions de la même décennie (ex: 1994, 2002, 2006)
- N3 : éditions adjacentes (±4 ans) (ex: 1994, 2002 — une seule édition d'écart)

**RÈGLE 3.6 - Format**  
Si la réponse correcte est "1998" → distracteurs au même format ("1994", "2002").  
Si la réponse est "édition 1998" → distracteurs "édition 1994", "édition 2002".  
Ne jamais mélanger les deux formats dans le même set de 4 options.

**Exemple appliqué**  
Q: "En quelle année la France a-t-elle remporté sa première Coupe du monde ?"  
R: "1998"  
Distracteurs N2: ["1994", "2002", "2006"]  
→ Vérification anti-collision 277 réponses ✓

---

## TYPE 4 — LOCALISATION
*Pattern: "Dans quelle ville / quel pays..." → réponse = ville ou pays*

**Exemple de question**: "Dans quel pays s'est déroulée la CDM 2010 ?"  
**Réponse correcte**: "Afrique du Sud"

**RÈGLE 4.1 - Sélection**  
Puiser dans la liste des pays hôtes CDM réels ou des pays participants notables. Pour les villes : utiliser des villes hôtes de la même édition ou d'éditions proches. Ne jamais inventer un lieu.

**RÈGLE 4.2 - Cohérence**  
- Si la réponse est un pays → distracteurs = pays (pas de villes)
- Si la réponse est une ville → distracteurs = villes du même pays ou de pays hôtes proches
- Respecter le continent si la question est géographiquement contextualisée (ex: CDM Afrique → distracteurs africains ou proches)

**RÈGLE 4.3 - Exclusion**  
- Vérifier anti-collision 277 réponses.
- Ne pas utiliser le pays/ville hôte d'une autre question proche dans le même pool (risque de confusion systémique).

**RÈGLE 4.4 - Vraisemblance**  
Les lieux doivent être reconnaissables par un amateur moyen. Éviter les pays très peu connus du football mondial sauf si la question le justifie.

**RÈGLE 4.5 - Difficulté N1 vs N3**  
- N1 : pays d'un autre continent ou clairement non-hôte (ex: pour R="Afrique du Sud" → "France", "Japon", "Mexique")
- N2 : pays hôtes d'autres éditions connus (ex: "Allemagne", "Brésil", "Argentine")
- N3 : pays hôtes de la même décennie ou région (ex: pour R="Afrique du Sud 2010" → "Maroc", "Nigeria", "Égypte" — pays africains crédibles)

**RÈGLE 4.6 - Format**  
Même langue et orthographe que la réponse correcte (français). "Afrique du Sud" et non "South Africa". Cohérence des accents et majuscules.

**⚠ Signal TYPE 4** : Ce type est potentiellement ambigu quand la question porte sur une ville spécifique d'un grand pays hôte (ex: "Dans quelle ville s'est joué la finale 1998 ?"). Le pool de villes hôtes françaises est petit (10 villes) et plusieurs peuvent apparaître comme réponses dans le quiz → risque de collision élevé. À vérifier systématiquement.

**Exemple appliqué**  
Q: "Dans quel pays s'est déroulée la CDM 2010 ?"  
R: "Afrique du Sud"  
Distracteurs N2: ["Maroc", "Égypte", "Nigeria"]  
→ Vérification anti-collision 277 réponses ✓

---

## TYPE 5 — CORRESPONDANCE (multi-critères)
*Pattern: "Quel joueur X a [fait Y] lors de [l'édition Z] ?" → réponse = entité satisfaisant plusieurs critères simultanément*

**Exemple de question**: "Quel joueur argentin a remporté le Ballon d'Or du meilleur joueur en 2022 ?"  
**Réponse correcte**: "Lionel Messi"

**RÈGLE 5.1 - Sélection**  
Générer des distracteurs qui satisfont certains critères de la question mais pas tous :
- Même nationalité, mauvaise distinction (ex: autre joueur argentin célèbre)
- Bonne distinction, mauvaise nationalité (ex: Ballon d'Or d'une autre édition, autre pays)
- Même édition, même rôle, mauvaise personne

**RÈGLE 5.2 - Cohérence**  
Chaque distracteur doit partager au minimum 1 critère sur les N critères de la question. Un distracteur qui ne partage aucun critère est trop facile à éliminer (équivalent N1). Idéalement : 1 ou 2 critères partagés sur 2-3 total.

**RÈGLE 5.3 - Exclusion**  
- Vérifier anti-collision 277 réponses (particulièrement critique ici : les entités multi-critères apparaissent souvent plusieurs fois dans le quiz).
- Un distracteur d'une question de type 5 peut être la réponse correcte d'une autre question → exclusion obligatoire.

**RÈGLE 5.4 - Vraisemblance**  
Très élevée : le distracteur doit paraître crédible sur au moins un axe important. C'est le type où le joueur peut le plus facilement se tromper. Les distracteurs "célèbres mais faux" sont préférables aux distracteurs "inconnus".

**RÈGLE 5.5 - Difficulté N1 vs N3**  
- N1 : distracteurs ne partageant qu'un critère mineur (ex: même continent mais pas même nationalité)
- N2 : distracteurs partageant 1 critère fort sur 2 (ex: même nationalité, mais pas le bon palmarès)
- N3 : distracteurs partageant tous les critères sauf le plus précis (ex: même nationalité, même édition, même rôle, mais pas le bon joueur)

**RÈGLE 5.6 - Format**  
Même format que la réponse correcte : si la réponse est "Lionel Messi" (prénom + nom), les distracteurs sont "Lautaro Martínez", "Kylian Mbappé", "Antoine Griezmann" — jamais "Messi" seul si la réponse est en forme complète.

**⚠ Signal TYPE 5** : C'est le type avec le risque de collision le plus élevé. Les joueurs très célèbres (Messi, Ronaldo, Mbappé) apparaissent probablement plusieurs fois comme réponses dans le quiz → vérification anti-collision impérative avant assignation.

**Exemple appliqué**  
Q: "Quel joueur argentin a remporté le Ballon d'Or du meilleur joueur en 2022 ?"  
R: "Lionel Messi"  
Distracteurs N3: ["Lautaro Martínez", "Kylian Mbappé", "Antoine Griezmann"]  
→ Lautaro : même nationalité (Argentine) ✓ mais pas le bon palmarès  
→ Mbappé : même édition, finaliste ✓ mais Français  
→ Griezmann : même édition ✓ mais Français, pas Ballon d'Or  
→ Vérification anti-collision 277 réponses : à confirmer ✓

---

## RÉCAPITULATIF — RÈGLES TRANSVERSALES

| Règle | Application |
|---|---|
| Anti-collision | Obligatoire pour les 5 types — vérifier contre les 277 réponses avant chaque assignation |
| Format homogène | Dans un set de 4 options (1 réponse + 3 distracteurs), le format doit être identique |
| Pas d'invention | Tous les noms, chiffres, lieux et années doivent être réels et vérifiables |
| Niveau adapté | N1 = éliminable par connaissance générale / N3 = nécessite connaissance précise |
| Unicité intra-question | Les 3 distracteurs d'une même question doivent être distincts entre eux |
| Unicité inter-questions | Dans un même pool, éviter de réutiliser le même distracteur pour deux questions différentes |

---

*Document de référence — Session B6 — CDM 2026*
