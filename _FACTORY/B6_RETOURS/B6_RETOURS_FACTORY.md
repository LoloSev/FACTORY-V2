# B6 — RETOURS FACTORY (CENTRALISÉ)

VERSION: 1.0
DATE_INIT: 2026-05-18
STATUS: ACTIVE
SCOPE: TOUTES LIGNES

PRINCIPE:
Toute difficulté, friction ou anomalie détectée sur une ligne de production
est consignée ici pour analyse et décision de généralisation éventuelle.

---

[B6-001] 2026-05-18 / MAYENNE / B2 / BUG_DETECTION / Faux positifs TYPE-PED-1 par correspondance de chaîne
DESCRIPTION: Le détecteur PED-1 (réponse dans le libellé) utilise une correspondance de chaîne simple. Génère des faux positifs quand le même mot désigne des référents différents : "Mayenne" (département) ≠ "Mayenne" (ville) ; "Laval" (cité) ≠ "Laval" (famille seigneuriale) ; "ducs de Mayenne" (titre) ≠ ville. 3 faux positifs sur 7 détections (43%).
IMPACT: Sur-correction potentielle de questions valides.
DÉCISION: Améliorer le détecteur — exiger que la réponse soit un sous-ensemble syntaxique isolé du libellé (pas simplement une sous-chaîne). Contrôle humain obligatoire avant application.
Ce fichier est la source unique des retours d'expérience FACTORY.

---

# RÈGLE D'ALIMENTATION

- Qui consigne : l'IA à chaque détection, l'humain à chaque validation
- Quand : dès détection, quelle que soit l'étape
- Format : une entrée par observation (voir template ci-dessous)
- Décision de promotion : humaine uniquement (RULE-HIER-003)

---

# TEMPLATE D'ENTRÉE

```
[B6-XXX]
DATE: 
LIGNE: [THEME]
ÉTAPE: A2 / A3 / A4 / B2 / B3 / B5
TYPE: FRICTION / ANOMALIE / PATTERN / RÈGLE_MANQUANTE
DESCRIPTION:
IMPACT:
DÉCISION: EN_ATTENTE / GÉNÉRALISER → STD / CLORE
```

---

# RETOURS

<!-- Les entrées sont ajoutées ci-dessous, les plus récentes en premier -->

---

*B6_RETOURS_FACTORY.md — Version 1.0 — 2026-05-18*
*Alimenté par toutes les lignes — décisions humaines uniquement*
