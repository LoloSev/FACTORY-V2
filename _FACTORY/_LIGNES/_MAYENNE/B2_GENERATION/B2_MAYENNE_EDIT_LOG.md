# B2_MAYENNE_EDIT_LOG

SOURCE: B2_MAYENNE_QUESTIONS.md
ROLE: traçabilité des modifications éditoriales

---

## FORMAT

| DATE | Q_ID | CHAMP | AVANT | APRÈS | RAISON |
|------|------|-------|-------|-------|--------|

## TYPE_MODIF (valeurs fermées)

```txt
REPONSE_NETTOYAGE   : réponse contenant texte explicatif superflu
REPONSE_FACTUELLE   : correction d'une erreur factuelle (source citée)
LIBELLE_REFORMULATION : reformulation du libellé
LIBELLE_FACTUELLE   : correction d'une erreur dans le libellé
SUPPRESSION         : question retirée (raison obligatoire)
AJOUT               : question ajoutée
NIVEAU              : changement de CIBLE_NIVEAU
COLLISION           : suppression ou réécriture pour collision
```

---

## LOG

| DATE | Q_ID | TYPE_MODIF | AVANT | APRÈS | RAISON |
|------|------|------------|-------|-------|--------|
| 2026-05-22 | MAY-006 | REPONSE_NETTOYAGE | NOZ — née à Laval en 1976 | NOZ | Réponse ne doit pas contenir d'explication — incompatible B3 |
| 2026-05-22 | MAY-025 | NIVEAU | N1 | N3 | Connaissance peu évidente hors Mayenne |
| 2026-05-22 | MAY-029 | SUPPRESSION | NOZ a changé de nom à cause de quoi ? | — | Question pas fun — rejetée éditorialement |
| 2026-05-22 | MAY-001 | LIBELLE_REFORMULATION | NOZ vient de quelle ville ? | Dans quelle ville NOZ a-t-il son siège social ? | Collision avec MAY-004 (Laval mentionné) + réorientation vers Saint-Berthevin |
| 2026-05-22 | MAY-001 | REPONSE_FACTUELLE | Laval | Saint-Berthevin | Siège social NOZ = Saint-Berthevin (Wikipedia) |
| 2026-05-22 | MAY-001 | NIVEAU | N3 | N2 | Requalification suite reformulation |
| 2026-05-22 | MAY-004 | LIBELLE_REFORMULATION | En quelle année NOZ a-t-il été fondé à Laval ? | En quelle année NOZ a-t-il été fondé ? | Collision — "à Laval" révèle la réponse de MAY-006 |
| 2026-05-22 | MAY-006 | LIBELLE_REFORMULATION | Quelle enseigne de déstockage vient de Laval ? | Quelle grande enseigne de déstockage est mayennaise ? | Suppression de "Laval" — collision avec MAY-001 |
| 2026-05-22 | MAY-202 | AJOUT | — | Qui a fondé NOZ en 1976 ? / Rémy Adrion / N3 | Stock sans pool — proposition A validée N3 |
| 2026-05-22 | MAY-203 | AJOUT | — | Quel nom porte le siège social de NOZ ? / Campus Univers Noz / N3 | Stock sans pool |
| 2026-05-22 | MAY-024 | LIBELLE_REFORMULATION | Qui a fondé Lactalis à vélo en 1933 ? | Qui livrait son lait à vélo avant de fonder Lactalis ? | Ambiguïté — "à vélo" se rattachait au sujet |
| 2026-05-22 | MAY-030 | LIBELLE_REFORMULATION | Lactalis démarre avec combien de litres de lait ? | Avec combien de litres de lait par jour André Besnier a-t-il lancé Lactalis ? | Question opaque — "démarre avec" sans contexte |
| 2026-05-22 | MAY-032 | LIBELLE_REFORMULATION | Port-Salut a été inventé par qui ? | Qui est à l'origine du Port-Salut ? | Reformulation plus naturelle |
| 2026-05-22 | MAY-034 | NIVEAU | N1 | N3 | Date précise — trop spécifique pour N1 |
| 2026-05-22 | MAY-036 | SUPPRESSION | Chaussée aux Moines est consommé par combien de Français ? | — | Pas fun — stat froide |
| 2026-05-22 | MAY-039 | SUPPRESSION | Combien de fromages du quotidien viennent de Mayenne ? | — | Réponse trop dépendante des habitudes de chaque foyer |
| 2026-05-22 | MAY-040 | NIVEAU | N1 | N3 | Date précise — trop spécifique pour N1 |
| 2026-05-22 | MAY-053 | SUPPRESSION | L'Emmental Président vient de Suisse ? | — | Risque de révéler la réponse d'autres questions |
| 2026-05-22 | MAY-088 | SUPPRESSION | Lactalis démarre avec combien de camemberts fabriqués ? | — | Redondance avec MAY-030 (même anecdote fondation) |
| 2026-05-22 | MAY-002 | SUPPRESSION | Port-Salut vient de quel département ? | — | Réponse évidente dans un quiz sur la Mayenne |
| 2026-05-22 | MAY-204 | AJOUT | — | Quel était le métier d'André Besnier avant de fonder Lactalis ? / Tonnelier / N3 | Stock sans pool — source Wikipedia |
| 2026-05-22 | MAY-205 | AJOUT | — | Comment s'appelait la première marque de Lactalis ? / Le Petit Lavallois / N3 | Stock sans pool — source Wikipedia |
| 2026-05-22 | MAY-206 | SUPPRESSION | Pourquoi Besnier a-t-il changé de nom pour Lactalis ? | — | Rejeté éditorialement |
| 2026-05-22 | MAY-207 | AJOUT | — | Quel musée lavallois est dédié à l'univers laitier ? / Le Lactopôle André Besnier / N2 | Stock sans pool — source Wikipedia |
| 2026-05-22 | MAY-208 | SUPPRESSION | Quel % des camemberts AOP de France vient de Lactalis ? | — | Info datée (~2015) + trop technique |
| 2026-05-22 | MAY-209 | AJOUT | — | Quelle grande marque de lait appartient à Lactalis ? / Lactel / N1 | Stock sans pool |
| 2026-05-22 | MAY-210 | AJOUT | — | Pour quel fromage la marque Président a-t-elle été créée ? / Le camembert / N1 | Stock sans pool |
| 2026-05-22 | MAY-211 | SUPPRESSION | Lactalis appartient à quelle famille mayennaise ? | — | Collision — révèle André Besnier |
| 2026-05-22 | MAY-212 | SUPPRESSION | Quel rang Lactalis occupe-t-il parmi les groupes laitiers mondiaux ? | — | Trop évidente |
| 2026-05-22 | MAY-213 | SUPPRESSION | Combien Lactalis emploie-t-il de collaborateurs dans le monde ? | — | Trop évidente |
| 2026-05-22 | MAY-214 | AJOUT | — | Quelle grande marque italienne de mozzarella appartient à Lactalis ? / Galbani / N1 | Stock sans pool |
| 2026-05-22 | MAY-026 | SUPPRESSION | Rapido a été fondé par quel métier ? / Un ébéniste | — | Rejet éditorial — collision avec MAY-077 (même information) |
| 2026-05-22 | MAY-077 | SUPPRESSION | Constant Rousseau était quel métier avant Rapido ? / Ébéniste | — | Rejet éditorial — collision avec MAY-026 |
| 2026-05-22 | MAY-078 | SUPPRESSION | Rapido a été fondé en quelle année ? / 1948 | — | Rejet éditorial |
| 2026-05-22 | MAY-081 | SUPPRESSION | Rapido a gagné quelle médaille à Paris ? / Médaille d'or de la Ville de Paris | — | Rejet éditorial |
| 2026-05-22 | MAY-084 | SUPPRESSION | Rapido est installé à Mayenne ville depuis quelle année ? / 1975 | — | Rejet éditorial |
| 2026-05-22 | MAY-086 | SUPPRESSION | Rapido a reçu quel prix au Concours Lépine ? / 1er prix | — | Rejet éditorial — collision libellé/réponse avec MAY-028 |
| 2026-05-22 | MAY-021 | LIBELLE_REFORMULATION | Rapido fabrique quoi depuis Mayenne ? | Que fabrique le constructeur mayennais Rapido ? | Formulation bancale — source Wikipedia |
| 2026-05-22 | MAY-091 | LIBELLE_REFORMULATION | Constant Rousseau a fondé Rapido à quel endroit ? | Dans quelle commune Constant Rousseau a-t-il fondé Rapido ? | Reformulation plus naturelle — source Wikipedia |
| 2026-05-22 | MAY-028 | SUPPRESSION | Rapido a eu un prix à quel concours parisien ? / Concours Lépine | — | Abandonné — année du prix Lépine introuvable, non sourceable |
| 2026-05-22 | MAY-027 | SUPPRESSION | V and B compte combien de magasins en 2022 ? / 255 | — | Rejet éditorial |
| 2026-05-22 | MAY-087 | SUPPRESSION | V and B associe cave à bière et quoi ? / Bar à vin | — | Rejet éditorial |
| 2026-05-22 | MAY-090 | SUPPRESSION | V and B comptait quel CA en 2022 ? / 180 millions d'euros | — | Rejet éditorial |
| 2026-05-22 | MAY-019 | LIBELLE_REFORMULATION | Ville mayennaise du V and B Fest' ? | Dans quelle ville mayennaise se tient le V and B Fest' ? | Reformulation plus naturelle |
| 2026-05-22 | MAY-098 | SUPPRESSION | "Pournigauder" veut dire quoi ? / Traîner, flâner sans but | — | Rejet éditorial |
| 2026-05-22 | MAY-101 | SUPPRESSION | "Achevé" en mayennais signifie quoi ? / Épuisé, crevé | — | Rejet éditorial |
| 2026-05-22 | MAY-144 | SUPPRESSION | La goutte est fabriquée comment en Mayenne ? / En contrebande | — | Rejet éditorial |
| 2026-05-22 | MAY-146 | SUPPRESSION | Asteure vient de quelle expression latine ? / In hodie | — | Rejet éditorial |
| 2026-05-22 | MAY-148 | SUPPRESSION | Ieau désigne quoi en mayennais ? / L'eau | — | Rejet éditorial |
| 2026-05-22 | MAY-150 | SUPPRESSION | Cite désigne quelle boisson en mayennais ? / Cidre | — | Rejet éditorial |
| 2026-05-22 | MAY-048 | SUPPRESSION | "Heulâ" est quelle sorte de mot ? / Une interjection de surprise | — | Rejet éditorial |
| 2026-05-22 | MAY-012 | SUPPRESSION | Que signifie "la niche su'l'chien" en patois mayennais ? / C'est fichu / terminé | — | Doublon MAY-092 |
| 2026-05-22 | MAY-047 | SUPPRESSION | "Du soui" désigne quoi ? / Du bazar, de la poussière | — | Collision MAY-099 (même mot soui) |
| 2026-05-22 | MAY-100 | SUPPRESSION | "Mett' le crouillet" signifie quoi ? / Mettre le verrou | — | Collision MAY-147 (crouillet = verrou dans les deux) |
| 2026-05-22 | MAY-210 | SUPPRESSION | Pour quel fromage la marque Président a-t-elle été créée ? / Le camembert | — | Rejet éditorial |
| 2026-05-22 | MAY-164 | SUPPRESSION | V and B Fest : festival de quoi ? / Bières artisanales et vins | — | Bloc V AND B FEST' supprimé |
| 2026-05-22 | MAY-200 | SUPPRESSION | V and B Fest : quels producteurs réunis ? / Brasseurs et vignerons indépendants | — | Bloc V AND B FEST' supprimé |
| 2026-05-22 | MAY-201 | SUPPRESSION | V and B Fest hors musique : c'est quoi ? / Un marché de bières et vins artisanaux | — | Bloc V AND B FEST' supprimé |
| 2026-05-22 | MAY-073 | SUPPRESSION | Gerbault a traversé l'Atlantique seul d'où vers où ? / D'est en ouest | — | Rejet éditorial |
| 2026-05-22 | MAY-015 | SUPPRESSION | Peintre naïf au MoMA né à Laval ? / Henri Rousseau dit le Douanier | — | Rejet éditorial |
| 2026-05-22 | MAY-122 | SUPPRESSION | Alfred Jarry a écrit quelle pièce ? / Ubu Roi | — | Rejet éditorial |
| 2026-05-22 | MAY-125 | SUPPRESSION | Ambroise Paré, Jarry et Gerbault ont quoi en commun ? / Nés à Laval | — | Rejet éditorial |
| 2026-05-22 | MAY-126 | SUPPRESSION | Douanier Rousseau : œuvres dans quels grands musées ? / MoMA, Orsay, Pompidou | — | Rejet éditorial |
| 2026-05-22 | MAY-127 | SUPPRESSION | Henri Rousseau est surnommé comment ? / Le Douanier | — | Donne la réponse d'autres questions |
| 2026-05-22 | MAY-128 | SUPPRESSION | MANAS est installé dans quel bâtiment lavallois ? / Château médiéval | — | Rejet éditorial |
| 2026-05-22 | MAY-072 | LIBELLE_REFORMULATION | Jarry a écrit Ubu Roi. Il vient d'où ? / Laval, Mayenne | Quel auteur lavallois a écrit Ubu Roi ? / Alfred Jarry | Réponse devient Alfred Jarry |
| 2026-05-22 | MAY-069 | SUPPRESSION | Alfred Jarry est un précurseur de quoi ? / Le surréalisme | — | Incohérence avec MAY-123 — rejet éditorial |
| 2026-05-22 | MAY-123 | SUPPRESSION | Jarry est précurseur du théâtre de quoi ? / L'absurde | — | Incohérence avec MAY-069 — rejet éditorial |
| 2026-05-22 | MAY-065, MAY-071, MAY-075, MAY-005 | CLUSTER | PERSONNALITÉS — SCIENCES ET MÉDECINE | FOOTBALL / STADE LAVALLOIS (nouveau cluster) | Mauvaise classification — footballeurs déplacés |
| 2026-05-22 | MAY-066 | SUPPRESSION | Ambroise Paré a remplacé quoi en chirurgie ? / L'huile bouillante par la ligature | — | Rejet éditorial |
| 2026-05-22 | MAY-070 | SUPPRESSION | Ambroise Paré est surnommé le père de quoi ? / La chirurgie moderne | — | Collision MAY-010 |
| 2026-05-22 | BLOC-36 | LIBELLE_REFORMULATION | Libellés fragmentaires (fragments, deux-points isolants) | Questions complètes avec verbe conjugué | MAY-013/102/104/108/109/111/186/187/189/191/192/168/020/170/172/175/176/177/178/158/194/154/156/159/195/112/113/119/120/016/132/139/140/184/173/162/163/166/167/129 |
| 2026-05-22 | MAY-071 | LIBELLE_REFORMULATION | François Omam-Biyik a joué à Laval avant quoi ? / La Coupe du Monde 1990 | Quel joueur du Stade Lavallois a inscrit un but contre l'Argentine de Maradona en 1990 ? / François Omam-Biyik | Collision MAY-005 résolue — réponse devient François Omam-Biyik |
| 2026-05-22 | MAY-005 | SUPPRESSION | Qui a marqué contre l'Argentine en 1990 avant Laval ? / François Omam-Biyik | — | Doublon MAY-071 après reformulation — libellé confus |
| 2026-05-22 | MAY-010 | LIBELLE_REFORMULATION | Père de la chirurgie moderne, né à Laval ? | Quel médecin lavallois est surnommé le père de la chirurgie moderne ? | Fragment → question complète |
| 2026-05-22 | MAY-062 | REPONSE_NETTOYAGE | Peintures paléolithiques | Peintures et gravures rupestres | Réponse incomplète — les Grottes de Saulges contiennent aussi des gravures |
| 2026-05-22 | MAY-016 | LIBELLE_REFORMULATION | Quelle ancienne carrière aux eaux turquoise peut-on visiter en Mayenne ? | Quelle ancienne carrière insolite peut-on visiter en Mayenne ? | Collision ⑦ — "eaux turquoise" révèle la réponse de MAY-136 et MAY-185 |
| 2026-05-22 | MAY-185 | LIBELLE_REFORMULATION | L'eau turquoise d'Echologia vient de quoi ? | D'où vient la couleur surprenante de l'eau d'Echologia ? | Collision ⑦ — "turquoise" dans le libellé révèle la réponse de MAY-136 |
| 2026-05-22 | MAY-133 | SUPPRESSION | Quel matériau caractérise le Musée Tatin ? / Béton monumental | — | Rejet éditorial — collision ⑦ |
| 2026-05-22 | MAY-013 | SUPPRESSION | Quel est le rang de la Mayenne pour l'élevage de trotteurs ? / 3e département français | — | Rejet éditorial |
| 2026-05-22 | MAY-104 | SUPPRESSION | Pour quel style de course Jacky Durand est-il connu ? / Attaques solitaires | — | Rejet éditorial |
| 2026-05-22 | MAY-105 | SUPPRESSION | Combien d'hippodromes en Mayenne ? / 9 | — | Rejet éditorial |
| 2026-05-22 | MAY-107 | SUPPRESSION | Combien d'équidés compte la Mayenne ? / Plus de 25 000 | — | Rejet éditorial |
| 2026-05-22 | MAY-108 | SUPPRESSION | Quel est le rang de la Mayenne au cheptel équin national ? / 6e de France | — | Rejet éditorial |
| 2026-05-22 | MAY-111 | SUPPRESSION | À quelle fréquence se tiennent les courses cyclistes en Mayenne ? / Tous les weekends | — | Rejet éditorial |
| 2026-05-22 | MAY-192 | SUPPRESSION | Quelle est la singularité du Cross-Country de Craon ? / Il franchit une route nationale | — | Rejet éditorial |
| 2026-05-22 | MAY-172 | SUPPRESSION | En quoi le bocage mayennais est-il un atout naturel pour le motocross ? / Terrain vallonné | — | Rejet éditorial |
| 2026-05-22 | MAY-174 | SUPPRESSION | Ernée accueille le MXoN depuis quelle année ? / 2005 | — | Rejet éditorial |
| 2026-05-22 | MAY-176 | SUPPRESSION | Combien d'éditions du MXoN Ernée a-t-il accueillies ? / 4 | — | Rejet éditorial |
| 2026-05-22 | MAY-179 | SUPPRESSION | Quel pays a dominé le MXoN sur 13 ans ? / Les États-Unis | — | Rejet éditorial |
| 2026-05-22 | MAY-181 | SUPPRESSION | Pendant le MXoN, Ernée ressemble à quoi ? / Un campement international | — | Rejet éditorial |
| 2026-05-22 | MAY-018 | SUPPRESSION | Sainte-Suzanne est bâtie sur quel type de relief ? / Un éperon rocheux | — | Rejet éditorial |
| 2026-05-22 | MAY-153 | SUPPRESSION | Pourquoi un assiégeant de Sainte-Suzanne était-il structurellement désavantagé ? | — | Rejet éditorial |
| 2026-05-22 | MAY-155 | SUPPRESSION | Chemin de ronde de Sainte-Suzanne : que permet-il ? | — | Rejet éditorial |
| 2026-05-22 | MAY-156 | SUPPRESSION | De quelle époque date le logis seigneurial de Sainte-Suzanne ? / XVIIe siècle | — | Rejet éditorial |
| 2026-05-22 | MAY-159 | SUPPRESSION | Quelle est la silhouette de Sainte-Suzanne vue depuis la vallée ? | — | Rejet éditorial |
| 2026-05-22 | MAY-193 | SUPPRESSION | Quel musée se trouve dans le logis de Sainte-Suzanne ? / Musée d'Art et d'Archéologie | — | Rejet éditorial |
| 2026-05-22 | MAY-195 | SUPPRESSION | Depuis le chemin de ronde de Sainte-Suzanne, sur quoi a-t-on vue ? | — | Rejet éditorial |
| 2026-05-22 | MAY-196 | SUPPRESSION | Le village de Sainte-Suzanne est-il dans l'enceinte ? | — | Rejet éditorial |
| 2026-05-22 | MAY-197 | SUPPRESSION | Comment pénètre-t-on dans la forteresse de Sainte-Suzanne ? / Par un châtelet | — | Rejet éditorial |
| 2026-05-22 | ALL | NIVEAU | Colonne N (N1/N2/N3) présente sur 119 questions | Colonne supprimée | Niveaux de difficulté retirés du fichier B2 |
| 2026-05-22 | ALL | POOL_REFONTE | Codes QV-xx / IF-xx / — | Codes thématiques : NOZ / LACTALIS / RAPIDO / VandB / PATOIS / PERSO-ARTS / PERSO-SCI / FOOT / SPORT-EQ / MOTO / STE-SUZ / PATRIM / INSOLITE / VR / GEO / IDENTITE | Pools redéfinis par sujet traité |
| 2026-05-22 | ALL | RENUMEROTATION | MAY-006…MAY-214 (non consécutif) | MAY-001…MAY-119 (séquentiel) | Renumérotation complète dans l'ordre d'apparition thématique |
| 2026-05-22 | MAY-054 | SUPPRESSION | Aubameyang est né à Laval en quelle décennie ? / Années 1980 | — | Rejet éditorial |
| 2026-05-22 | MAY-063 | LIBELLE_REFORMULATION | Quelle est la particularité de l'hippodrome de Craon ? | En quelle année l'hippodrome de Craon a-t-il été ouvert ? | Question recentrée sur l'année — réponse épurée à 1848 |
| 2026-05-22 | MAY-049 | LIBELLE_REFORMULATION | Gerbault est connu pour quelle première mondiale ? | Alain Gerbault est connu pour quelle première mondiale ? | Ajout prénom |
| 2026-05-22 | MAY-056 | LIBELLE_REFORMULATION | Quel Tour Jacky Durand a-t-il gagné en 1992 ? | Quelle course Jacky Durand a-t-il gagnée en 1992 ? | Accord gagnée + formulation plus ouverte |
| 2026-05-22 | MAY-059 | LIBELLE_REFORMULATION | Montebrun récupère sa médaille combien d'ans après ? | Combien d'années après les JO de Pékin Manuela Montebrun a-t-elle reçu sa médaille de bronze ? | Ajout prénom + ancrage JO de Pékin |
| 2026-05-22 | MAY-060 | LIBELLE_REFORMULATION | Dans quelle discipline sportive Montebrun s'est-elle illustrée ? | Dans quelle discipline sportive Manuela Montebrun s'est-elle illustrée ? | Ajout prénom |
| 2026-05-22 | MAY-060 | REPONSE_FACTUELLE | Judo | Lancer du marteau | Erreur factuelle — source Wikipedia |
| 2026-05-22 | MAY-061 | LIBELLE_REFORMULATION | En quelle année Montebrun a-t-elle concouru aux JO ? / 2004 — Athènes | Lors de quels JO Manuela Montebrun a-t-elle décroché sa médaille olympique ? / Pékin 2008 | Question invalide (3 JO) — reformulée sur la médaille + ajout prénom + correction réponse (Pékin 2008, pas Athènes) |
