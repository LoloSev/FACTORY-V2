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
