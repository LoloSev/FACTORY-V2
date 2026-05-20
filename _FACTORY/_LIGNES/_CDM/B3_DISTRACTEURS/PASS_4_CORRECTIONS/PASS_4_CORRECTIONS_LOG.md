# CDM B3 — PASS 4 CORRECTIONS LOG

**Date:** 2026-05-18  
**Statut:** EN COURS  
**Source:** CDM_B2_AUDIT_RETROACTIF_REGLES_FINALES.md  
**Contexte:** Nombreuses corrections B2 déjà intégrées lors de la création des fichiers B3. Ce log documente les corrections résiduelles à appliquer dans les fichiers B3 existants.

---

## CONSTAT PRÉLIMINAIRE

Après lecture de tous les fichiers B3 :
- La majorité des corrections de l'audit B2 (31 non-conformités) ont **déjà été intégrées** lors de la création des fichiers B3
- Corrections déjà appliquées en B3 : QV03-Q002/Q004/Q009 (supprimés), QV08-Q009/Q010 (restent — à supprimer), QV10-Q005/Q006/Q008/Q011 (reformulés), QV12-Q005 (reformulé), QV13-Q003 (reformulé), QV14-Q009 (reformulé), QV01-Q006/Q009/Q013 (remplacés), IF-SF01-Q005 (remplacé), IF-ROT01-Q002/Q003 (supprimés)
- **Corrections résiduelles à appliquer : 16 actions**

---

## CORRECTIONS RÉSIDUELLES À APPLIQUER

### TYPE A — SUPPRESSIONS (pool réduit, R01 conforme)

| # | Pool | Q_ID | Raison | Action |
|---|------|------|--------|--------|
| A1 | QV08 | Q009 | Collision finale 2018 (IF-SF-02 couvre déjà cette finale) | SUPPRIMER |
| A2 | QV08 | Q010 | Collision finale 2018 (même famille REC-07) | SUPPRIMER |
| A3 | QV13 | Q010 | Nationalité Helmut Rahn sans valeur (R07/R20) | SUPPRIMER |

### TYPE B — REFORMULATIONS (question text only)

| # | Pool | Q_ID | Formulation actuelle | Formulation cible | Règle |
|---|------|------|---------------------|-------------------|-------|
| B1 | QV02 | Q002 | "En 1986, les tenants du titre italiens sont éliminés par un joueur évoluant dans le Calcio. Qui est-il ?" | "Quel joueur a éliminé l'Italie tenante du titre en 1986 ?" | R03 |
| B2 | QV02 | Q008 | "Quel numéro de maillot est devenu mythique grâce à Johan Cruyff ?" | "Quel numéro de maillot portait Johan Cruyff ?" | R03 |
| B3 | QV04 | Q005 | "Quelle finale est restée célèbre pour le but fantôme de Geoff Hurst ?" | "Dans quelle finale Geoff Hurst a-t-il inscrit son 'but fantôme' ?" | R03 |
| B4 | QV06 | Q002 | "Quel stade a accueilli deux finales avant 2026 ?" | "Quel stade a accueilli deux finales ?" | R05 |
| B5 | QV11 | Q001 | "En quelle ville espagnole s'est joué le match surnommé la Disgrace de Gijon ?" | "Dans quelle ville espagnole s'est joué le match controversé entre l'Allemagne de l'Ouest et l'Autriche en 1982 ?" | RECEVABILITE L01 |
| B6 | QV12 | Q006 | "…avant de devenir le héros du Mondial 1982 ?" | "Quelle sanction Paolo Rossi avait-il subie avant le Mondial 1982 ?" | R03 |

**Note B4 (QV06-Q002) :** Après reformulation, la question "Quel stade a accueilli deux finales ?" reste ambigu car le Maracana a aussi accueilli 2 finales (1950, 2014). La question Q001 et Q002 pointent toutes deux vers L'Azteca. Risque de redondance — à surveiller en B5.

### TYPE C — FLAGS VEILLE (annotation sans modification question)

| # | Pool | Q_ID | Question | Motif |
|---|------|------|----------|-------|
| C1 | IF-ROT-01 | Q005 | "Quelle est la nation la plus titrée en CDM ?" → Le Brésil | Palmarès peut changer (CDM 2026) |
| C2 | QV01 | Q007 | "Combien de fois Lionel Messi a-t-il participé au tournoi ?" → 5 fois | Participations Messi (CDM 2026) |
| C3 | QV01 | Q010 | "Combien de fois Cristiano Ronaldo a-t-il participé au tournoi ?" → 5 fois | Participations Ronaldo (CDM 2026) |
| C4 | QV08 | Q001 | "Quel joueur détient le record du but le plus rapide ?" → Hakan Şükür | Record battable (CDM 2026) |
| C5 | QV08 | Q013 | "Quel gardien est devenu le plus âgé à disputer un match ?" → Essam El-Hadary | Record battable (CDM 2026) |
| C6 | QV08 | Q014 | "Quel joueur est devenu le plus jeune à disputer un match ?" → Norman Whiteside | Record battable (CDM 2026) |
| C7 | QV13 | Q012 | "Quel joueur a disputé le plus de matches en CDM ?" → Lothar Matthäus | Record battable (CDM 2026) |
| C8 | QV13 | Q014 | "Quel joueur détient le record de matches gagnés en CDM ?" → Miroslav Klose | Record battable (CDM 2026) |

### TYPE D — NETTOYAGE TECHNIQUE

| # | Pool | Q_ID | Action |
|---|------|------|--------|
| D1 | QV01 | Q011 + Q011_corr | Supprimer ligne Q011 (avec collision D3) — garder uniquement Q011_corr comme version définitive |

---

## IMPACT SUR LA DISTRIBUTION (après corrections)

| Suppressions | Questions supprimées | Nouveau total |
|---|---|---|
| QV08: -2 (Q009, Q010) | 2 | 275 |
| QV13: -1 (Q010) | 1 | 274 |

**Note :** Réduction à 274 questions conforme à R01. Pas de question de remplissage. Le gap N3 (task #9) pourra compenser partiellement si de nouvelles questions N3 sont identifiées.

---

## STATUT CORRECTIONS

- [x] Log créé
- [ ] TYPE A — Suppressions appliquées
- [ ] TYPE B — Reformulations appliquées
- [ ] TYPE C — Flags VEILLE appliqués
- [ ] TYPE D — Nettoyage technique appliqué

---

*PASS 4 LOG — CDM B3 — 2026-05-18*
