# STANDARD — OBSOLESCENCE WATCH RULES

VERSION: 2.0
DATE_UPDATE: 2026-05-18
STATUS: ACTIVE_REFERENCE
PIPELINE_SCOPE: GLOBAL (B5_AUDIT + EXPORT + VEILLE)
IA_COMPATIBLE: TRUE
IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE

DEPENDENCY:
- MASTER_ARCHITECTURE.md
- STD_B2_generation_rules.md
- STD_GLOBAL_quiz_architecture_rules.md

RETEX_REF: RETEX_STD_OBSOLESCENCE_WATCH_RULES_001
RETEX_ROLE: JUSTIFICATION

---

# SECTION — PRINCIPE GÉNÉRAL

[RULE-OBS-001]
RETEX_REF: RETEX_STD_OBSOLESCENCE_WATCH_RULES_002
La déclaration est obligatoire, même si aucun signal d'obsolescence n'est détecté.

[RULE-OBS-002]
La veille est un processus continu post-export, pas une vérification ponctuelle.
RETEX_REF: RETEX_STD_OBSOLESCENCE_WATCH_RULES_003

---

# SECTION — 5 TYPES DE DÉCLENCHEURS

[RULE-OBS-003]
**TYPE-1 : Décès**
Une personnalité citée dans une question (réponse ou distracteur) décède.
Déclencheurs : annonce officielle, mention presse fiable.
Actions :
- VALIDER si la question reste valide (formulation au présent → invalide)
- Signaler si le distracteur est devenu sensible
- Suspendre si formulation irrespectueuse possible

[RULE-OBS-004]
**TYPE-2 : Nouvelle édition / Nouveau palmarès**
Une nouvelle compétition, édition, ou saison modifie un record, un classement, ou un superlatif.
Déclencheurs : résultats officiels d'une édition, fin de saison, cérémonie palmarès.
Actions :
- Revoir toutes les questions contenant superlatifs liés à cette compétition
RETEX_REF: RETEX_STD_OBSOLESCENCE_WATCH_RULES_004

[RULE-OBS-005]
**TYPE-3 : Polémique / Révision historique**
Un fait jugé établi est remis en cause (dopage, falsification, réattribution de record).
Déclencheurs : décision officielle, sanction sportive, révision institutionnelle.
Actions :
- Suspendre immédiatement la question concernée
- Ne pas modifier sans validation humaine

[RULE-OBS-006]
**TYPE-4 : Record battu**
Un record cité en réponse ou dans la question est dépassé.
Déclencheurs : performance officielle homologuée.
Actions :
- Invalider la question si elle porte sur "le record de..."
- Réévaluer si l'angle reste valide avec reformulation

[RULE-OBS-007]
**TYPE-5 : Nouvelle sortie / Nouvelle publication**
Un film, album, livre, jeu cité comme "dernier" ou "plus récent" est dépassé par une nouvelle parution.
Déclencheurs : sortie officielle, date de publication confirmée.
Actions :
- Revoir les questions contenant "dernier", "plus récent", "sorti en [année]"

---

# SECTION — DÉTECTION AUTOMATIQUE

[RULE-OBS-008]
**Marqueurs de risque obligatoires à détecter en B5**
Toute question contenant l'un des mots ou expressions suivants doit recevoir un FLAG_VEILLE :
- "dernier", "dernière"
- "premier", "première" (si relatif à une série en cours)
- "jamais", "encore jamais"
- "seul", "unique"
- "record", "recordman"
- "plus grand", "plus petit", "plus rapide", "plus de X"
- "meilleur", "pire"
- "à ce jour", "en [année]" si l'année est récente
- tout superlatif absolu lié à une compétition en cours

[RULE-OBS-009]
Un FLAG_VEILLE n'invalide pas la question — il la place sous surveillance.
La décision de modifier ou désactiver est humaine.

---

# SECTION — FORMAT FICHE VEILLE

[RULE-OBS-010]
Chaque quiz exporté doit produire une FICHE_VEILLE minimale au format suivant :

```
QUIZ_ID: [identifiant unique du quiz]
DATE_PRODUCTION: [YYYY-MM-DD]
DATE_VALIDITE: [YYYY-MM-DD ou "indéfinie"]
THEME: [thème du quiz]

QUESTIONS_A_RISQUE:
  - Q_ID: [identifiant question]
    POOL: [pool d'origine]
    RISQUE: TYPE-[1|2|3|4|5]
    MARQUEUR: [mot déclencheur identifié]
    NOTE: [contexte court]

DECLENCHEURS_SURVEILLES:
  - [liste des événements à monitorer — ex: cas source 2026, décès, sortie album]
RETEX_REF: RETEX_STD_OBSOLESCENCE_WATCH_RULES_005

RESPONSABLE_MAJ: [humain désigné ou "à définir"]
```

[RULE-OBS-011]
La FICHE_VEILLE est produite à la fin de B5_AUDIT, avant export.
Elle est conservée dans le dossier du quiz et mise à jour à chaque révision.

---

# SECTION — PROCESSUS DE MISE À JOUR

[RULE-OBS-012]
**Séquence de traitement lors d'un déclencheur :**
1. Identifier le type (TYPE-1 à 5)
2. Lister les questions affectées via FICHE_VEILLE
3. Évaluer : invalide / reformulable / inchangée
4. Corriger ou désactiver avec validation humaine
5. Mettre à jour FICHE_VEILLE + MODIFICATIONS_LOG du quiz
6. Re-exporter si nécessaire

[RULE-OBS-013]
Aucune correction d'obsolescence ne peut être appliquée sans validation humaine explicite,
même si la correction semble évidente.

---

# SECTION — ANNEXE THÉMATIQUE : cas source
RETEX_REF: RETEX_STD_OBSOLESCENCE_WATCH_RULES_006

[RULE-OBS-cas source-001]
RETEX_REF: RETEX_STD_OBSOLESCENCE_WATCH_RULES_007
**cas source 2026 — Vérifications obligatoires avant mise en ligne post-édition**
RETEX_REF: RETEX_STD_OBSOLESCENCE_WATCH_RULES_008
Avant toute mise en ligne ou réactivation d'un quiz cas source après le tournoi de juin 2026 :
RETEX_REF: RETEX_STD_OBSOLESCENCE_WATCH_RULES_009
- VALIDER toutes les questions contenant "dernier titre" (pays)
- VALIDER "nombre de titres" (pays, joueur)
- VALIDER records de buts all-time (individus, équipes)
- VALIDER tout superlatif : "le plus...", "jamais...", "seul pays à..."
- VALIDER palmarès buteurs de tournoi
RETEX_REF: RETEX_STD_OBSOLESCENCE_WATCH_RULES_010
RETEX_ROLE: JUSTIFICATION

[RULE-OBS-cas source-002]
RETEX_REF: RETEX_STD_OBSOLESCENCE_WATCH_RULES_011
Les questions cas source produites avant juin 2026 sont toutes potentiellement à risque TYPE-2 et TYPE-4.
RETEX_REF: RETEX_STD_OBSOLESCENCE_WATCH_RULES_012
Elles doivent toutes être listées dans la FICHE_VEILLE avec statut "à réviser post-cas source 2026".
RETEX_REF: RETEX_STD_OBSOLESCENCE_WATCH_RULES_013

---

*STD_OBSOLESCENCE_WATCH_RULES.md*
*Version 2.0 — 2026-05-18*
*Status: ACTIVE_REFERENCE*
*Consolidé depuis: RETEX source R32 + R34 + STD v1.0 original*
RETEX_REF: RETEX_STD_OBSOLESCENCE_WATCH_RULES_014


