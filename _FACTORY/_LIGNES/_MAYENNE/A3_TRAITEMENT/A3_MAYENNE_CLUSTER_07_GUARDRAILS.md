# A3_MAYENNE_CLUSTER_07_GUARDRAILS
# LINE_ID: MAYENNE_FACTORY_CORE
# PIPELINE: FACTORY_V2
# CLUSTER: 07 — FRANCE_PARALLELE / QUOTIDIEN
# STATUS: GUARDRAILS_ACTIVE — CLUSTER_LOCKED_UNTIL_HUMAN_VALIDATION

---

# OBJECTIF

Éviter avant ouverture complète du cluster 07 :
- hallucinations IA sur la vie quotidienne rurale
- folklore inventé
- pseudo-France rurale artificielle
- génération culturelle flottante

---

# VALIDATION_HUMAINE_REQUISE

Tout item du cluster 07 doit avoir :
- une source humaine directe (témoignage, usage oral, objet réel)
- ou une source vérifiable publique (presse locale, pratique documentée)

Aucun item ne peut être généré par inférence IA seule.

---

# SEUIL_MINIMUM_PREUVE

ACCEPTABLE :
- "entendu IRL / transmission orale / usage familial documenté"
- "pratique locale attestée par source humaine"
- "objet / lieu physique existant et vérifiable"
- "couverture presse locale ou régionale"

NON ACCEPTABLE :
- "probablement pratiqué en zone rurale"
- "typiquement dans ce type de département"
- "on peut imaginer que..."
- inférence sur "la France rurale en général"

---

# TYPES_AUTORISÉS

- habitudes de courses locales attestées
- expressions entendues dans les familles mayennaises (source humaine)
- objets du quotidien physiquement localisés
- micro-situations sociales réellement observées
- routines locales documentées (marché, foire, hippodrome, etc.)

---

# TYPES_INTERDITS

- stéréotypes ruraux non sourcés
- "vie à la campagne" générique
- folklore inventé ou extrapolé
- traditions non vérifiées
- ambiance "province française" sans ancrage Mayenne réel

---

# ANTI_HALLUCINATION_RULES

Ne jamais générer un item cluster 07 si :
- l'item pourrait s'appliquer à n'importe quel département rural français
- l'item ne contient pas un ancrage Mayenne identifiable
- l'item provient uniquement d'inférence IA sans source humaine
- l'item ressemble à du folklore marketing territorial

---

# EXEMPLES_ACCEPTABLES

✅ phrase orale entendue dans une famille mayennaise (source : transmission directe)
✅ habitude de courses attestée (NOZ + marché de Laval = combo local documenté)
✅ objet ou lieu physique réel avec usage quotidien identifiable
✅ routine hippodrome / foire agricole avec ancrage géographique précis

---

# EXEMPLES_REFUSÉS

❌ "les Mayennais font leur pain eux-mêmes" (stéréotype non sourcé)
❌ "la vie au bocage" sans fait précis
❌ "le dimanche en famille à la campagne" (générique)
❌ tout item généré par inférence IA sans validation humaine explicite

---

# RÈGLE_OUVERTURE_CLUSTER

Cluster 07 reste LOCKED jusqu'à :
- validation humaine d'au moins 3 items sourcés
- ajout dans A2_MAYENNE_CANONICAL_SOURCE.md section 7
- gate humaine explicite avant production A4
