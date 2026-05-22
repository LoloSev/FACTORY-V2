# STANDARD — B2 GENERATION RULES

VERSION: 1.0
DATE: 2026-05-18
STATUS: ACTIVE_REFERENCE
PIPELINE_SCOPE: B2
IA_COMPATIBLE: TRUE
IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE

DEPENDENCY:
- MASTER_ARCHITECTURE.md
- STD_GLOBAL_pool_collision_rules.md
- STD_GLOBAL_quiz_architecture_rules.md
- glossaire_documentaire_factory.md

RETEX_REF: RETEX_STD_B2_GENERATION_RULES_001
RETEX_ROLE: JUSTIFICATION
DATE_CONSOLIDATION: 2026-05-18

---

# SECTION — HARD_BLOCKERS (ABSOLU)

[RULE-B2-HB-000]
**Longueur libellé — seuil unique**
FAIL si libellé > 15 mots.
SOURCE_DE_VERITE: ce fichier — MDE_B2 et SKILL.md pointent vers cette règle.
TARGET_EDITORIAL: 6–9 mots. ACCEPTABLE: 10–14 mots. FAIL: ≥16 mots.

[RULE-B2-HB-001]
**Zéro filler**
Si un pool ne peut pas atteindre son TARGET avec des angles valides :
- Signaler le déficit explicitement
- Arrêter la génération du pool
- Attendre décision humaine
Une question de remplissage est invalide même si elle passe tous les autres VALIDATIONS.
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_002
RETEX_ROLE: JUSTIFICATION

[RULE-B2-HB-002]
**Checklist de rédaction — 8 filtres obligatoires**
Toute question candidate doit passer les 8 filtres suivants avant soumission :
1. Court et direct (pas de phrase complexe ou subordonnée inutile)
2. Une seule information centrale (pas de double question déguisée)
3. Pas de contexte inutile (supprimer tout ce qui ne conditionne pas la réponse)
4. Pas Wikipédique (pas de formulation encyclopédique ou narrative)
5. Pas de qualificatif éditorial (pas de "célèbre", "légendaire", "fameux")
6. Pas d'anglicisme invalide (utiliser les termes français officiels)
7. Réponse univoque (une seule réponse possible, sans ambiguïté)
8. Cadre du quiz omis si contexte implicite (dans un quiz cas source, "en cas source" est superflu)
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_003
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_004
RETEX_ROLE: JUSTIFICATION

[RULE-B2-HB-003]
**Boucle de corrections complète**
Toute correction d'une question repasse TOUS les 8 filtres de RULE-B2-HB-002 comme une proposition initiale.
Une correction validée sans repasser les filtres est invalide de process.
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_005
RETEX_ROLE: JUSTIFICATION

[RULE-B2-HB-004]
**Triple filtre de validation d'angle**
Avant de valider un angle pour génération, 3 VALIDATIONS obligatoires dans cet ordre :
1. **Disponibilité réelle** : l'angle n'est pas déjà réservé, exclu, ou assigné à un autre pool
2. **Absence de collision** : aucune collision directe ou éditoriale avec angles déjà produits
3. **Valeur intrinsèque de jeu** : le fait est saillant, non trivial, mérite d'être posé en question

⚠️ Passer les filtres 1 et 2 ne confère pas automatiquement le mérite. Un angle disponible et non-collisionnel peut rester sans valeur de jeu.
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_006
RETEX_ROLE: JUSTIFICATION

[RULE-B2-HB-005]
**Séquence de VALIDATION avant soumission humaine**
Aucune question candidate ne peut être soumise à l'humain avant :
1. VALIDATION anti-collision sur l'ensemble du lot déjà produit
2. VALIDATION de conformité FACTORY (règles actives)
3. Passage de la checklist 8 filtres (RULE-B2-HB-002)

Ordre obligatoire : angle candidat → anti-collision → conformité → proposition humaine.
Une question proposée avant ces vérifications est invalide de process, même si son angle est défendable.
SOURCE: MDE_B2 RULE-B2-002A

[RULE-B2-HB-006]
**Réponse univoque**
Un angle est invalide si sa réponse s'applique à plusieurs entités dans le contexte de la question.
La réponse doit pointer un fait factuel unique et non partagé.
Exemple invalide : "premier joueur de l'équipe à marquer" si plusieurs joueurs ont marqué au même moment.
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_007
RETEX_ROLE: JUSTIFICATION

[RULE-B2-HB-007]
**Désambiguïsation des homonymes**
Tout homonyme célèbre doit être désigné par son nom complet ou son surnom distinctif.
Jamais un nom seul ambigu dans une question ou une réponse.
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_008
RETEX_ROLE: JUSTIFICATION

---

# SECTION — SOFT_RULES (IMPORTANT)

[RULE-B2-SW-001]
**Passe de cadrage pré-génération**
Déclencher une passe de cadrage avant génération si le pool présente l'un des critères suivants :
- Pool éditorial pur (pas de mapping direct depuis feuille ANGLES)
- Densité d'angles structurés < 1,2 angle valide par question cible
- Part d'angles nécessitant mémoire collective/culture du domaine > 40 % du pool
- Risque d'oubli majeur probable sans revue spécifique
- Casting discutable ou composition ouverte

La fiche de cadrage produit (sans générer de questions) :
- Objets incontournables du pool
- Absents majeurs possibles
- Trajectoires transversales tombant entre plusieurs pools
- Angles culturels et narratifs non couverts par la feuille ANGLES
- Micro-faits à haut rendement de jeu
- Risques liés à la cible audience
- Arbitrages humains identifiés (3-5 max)
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_009
RETEX_ROLE: JUSTIFICATION

[RULE-B2-SW-002]
**Présence dans un autre pool ≠ couverture suffisante mesurable**
La présence d'une figure ou d'un objet dans un autre pool ne suffit pas à le considérer couvert.
VALIDER si son absence du pool courant serait surprenante pour un connaisseur du domaine.
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_010
RETEX_ROLE: JUSTIFICATION

[RULE-B2-SW-003]
**Répartition interne = arbitrage éditorial humain**
La répartition des questions entre entités d'un pool est une décision éditoriale humaine.
L'IA prépare les options et signale les contraintes, mais n'impose pas la répartition.
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_011
RETEX_ROLE: JUSTIFICATION

[RULE-B2-SW-004]
**Arbitrage évident : appliquer sans redemander**
Si une correction répond à un `FAIL:<RULE_ID>` ou `WARNING:<RULE_ID>`, appliquer la préférence validée correspondante
et reste dans le périmètre défini : appliquer la correction et soumettre le résultat final.
Ne pas redemander un arbitrage de principe pour chaque cas évident.
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_012
RETEX_ROLE: JUSTIFICATION

[RULE-B2-SW-005]
**Contexte implicite du quiz**
Dans un quiz borné (ex: quiz cas source), le rappel du cadre est superflu dans chaque question.
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_013
"Toutes éditions confondues" est valide pour les records cumulés.
Exception : si la question mêle contextes différents (carrière club + sélection nationale).
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_014
RETEX_ROLE: JUSTIFICATION

[RULE-B2-SW-006]
**Variété des angles dans un pool**
Un pool valide angle par angle peut rester pauvre si tous les angles appartiennent à la même famille.
VALIDER la diversité : identité / palmarès / statistiques / surnom / contexte culturel / singularités.
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_015
RETEX_ROLE: JUSTIFICATION

[RULE-B2-SW-007]
**Ce qui reste légitimement humain**
Relève de la décision humaine exclusive :
- Validation finale d'un pool complet
- Choix éditoriaux de goût irréductibles
- Cas frontières discutables
- Décisions de lancement ou de publication
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_016
RETEX_ROLE: JUSTIFICATION

---

# SECTION — OPTIONAL

[RULE-B2-OPT-001]
**Ancrage culturel positif**
Adapter certains angles au lien culturel local légitime de la cible audience,
si au moins un ancrage culturel vérifiable est ajouté sans supprimer l'unicité de réponse ni créer de prérequis local non sourcé.
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_017
RETEX_ROLE: JUSTIFICATION

[RULE-B2-OPT-002]
**Dimension extra-sportive**
Les angles extra-sportifs sont légitimes s'ils sont indissociables de la mémoire de l'objet
(impact culturel, résonance sociale, symbole politique).
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_018
RETEX_ROLE: JUSTIFICATION

[RULE-B2-OPT-003]
**Appellations culturelles**
Utiliser une appellation culturelle ([DENOMINATION_CULTURELLE]) seulement si :
- Reconnue par la cible
- Apporte quelque chose à la question
- Ne réduit pas l'accessibilité
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_019
RETEX_ROLE: JUSTIFICATION

[EXEMPLE-B2-OPT-003 — cas source]
Application sur la ligne cas source (football) :
→ DENOMINATION_CULTURELLE = Calcio, Seleção, Albiceleste…

[RULE-B2-OPT-004]
**[IDENTIFIANT_SYMBOLIQUE] emblématique**
Un [IDENTIFIANT_SYMBOLIQUE] est un angle valable uniquement si :
- Stable dans la mémoire collective
- Ajoute au moins une relation interrogeable absente d'une fiche standard : cause, conséquence, comparaison, exception, chronologie ou attribution
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_020
RETEX_ROLE: JUSTIFICATION

[EXEMPLE-B2-OPT-004 — cas source]
Application sur la ligne cas source (football) :
→ IDENTIFIANT_SYMBOLIQUE = numéro de maillot
→ Transposer : numéro de catalogue (musique), numéro de saison (séries), etc.

---

# SECTION — RÈGLES FACTUELLES PAR THÈME

Ces règles ne sont pas globales — elles s'appliquent uniquement au thème concerné.
Elles illustrent l'application de RULE-B2-HB-007 (désambiguïsation).

## Thème cas source
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_021

[RULE-B2-cas source-001]
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_022
Ne pas utiliser le Ballon d'Or comme récompense officielle de la Coupe du monde.
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_023
RETEX_ROLE: JUSTIFICATION

[RULE-B2-cas source-002]
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_024
Ne jamais écrire "Ronaldo" seul — préciser "Ronaldo Nazario" (R9) ou "Cristiano Ronaldo" (CR7).
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_025
RETEX_ROLE: JUSTIFICATION

---

# SECTION — ALERTES DE SIGNAL

[RULE-B2-ALT-001]
**Signalement déficit angles**
Signaler explicitement : angles utilisés / réservés / restants — puis attendre décision humaine.
Ne proposer des alternatives que si la décision humaine le demande.
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_026
RETEX_ROLE: JUSTIFICATION

---

*STD_B2_generation_rules.md*
*Version 1.0 — 2026-05-18*
*Status: ACTIVE_REFERENCE*
*Consolidé depuis: RETEX source (R01-R37) + MDE_B2_generation.md*
RETEX_REF: RETEX_STD_B2_GENERATION_RULES_027


