# STANDARD — RECEVABILITÉ PÉDAGOGIQUE (B2)

VERSION: 1.0
DATE_UPDATE: 2026-05-18
STATUS: ACTIVE_REFERENCE
PIPELINE_SCOPE: B2 + B5_AUDIT
IA_COMPATIBLE: TRUE
IA_COMPATIBILITY_SCOPE: GENERALIZED
NORMATIVE_SCOPE: UNIVERSAL_PIPELINE
LINE_DEPENDENCY: FORBIDDEN
RETEX_LOADING: ON_DEMAND_ONLY
RETEX_NORMATIVE_STATUS: NON_NORMATIVE

DEPENDENCY:
- STD_B2_generation_rules.md
- STD_GLOBAL_quiz_architecture_rules.md
- MASTER_ARCHITECTURE.md

RETEX_REF: RETEX_STD_B2_RECEVABILITE_PEDAGOGIQUE_001
RETEX_ROLE: JUSTIFICATION

---

# SECTION — PRINCIPE GÉNÉRAL

[RULE-PED-001]
**Définition : question irrecevable**
Une question est pédagogiquement irrecevable si un joueur peut trouver la bonne réponse
sans posséder la connaissance que la question est censée évaluer.

Ce standard est complémentaire à la checklist 8 filtres (RULE-B2-HB-002).
Les 8 filtres couvrent le style et la forme.
Ce standard couvre la validité cognitive.

[RULE-PED-002]
Une question irrecevable doit être rejetée ou reformulée avant B4.
Elle ne peut pas être compensée par des distracteurs de QA_STATUS.

---

# SECTION — TAXONOMIE DES IRRECEVABILITÉS

## TYPE-PED-1 : Réponse révélée dans le libellé

[RULE-PED-T1-001]
La question contient un mot, un nom, ou un élément qui désigne directement la réponse
ou la rend évidente par simple lecture.

EXEMPLES INVALIDES :
- "Quel joueur surnommé 'O Rei' a remporté 3 Coupes du monde ?" → "O Rei" = Pelé, notoire
- "Dans quel pays se trouvait le Stade de France lors du mondial 1998 ?" → France dans la question

DÉTECTION :
- La réponse est contenue littéralement dans la question
- Un synonyme ou surnom très connu de la réponse est dans la question
- Le contexte géographique/temporel exclut toutes les options sauf une sans connaissance

---

## TYPE-PED-2 : Réponse déductible par élimination logique

[RULE-PED-T2-001]
Un joueur sans connaissance du domaine peut éliminer les distracteurs par raisonnement
et identifier la bonne réponse sans savoir.

EXEMPLES INVALIDES :
- Question sur un buteur N3 avec 3 distracteurs de nationalités différentes
  → si la question cite une nationalité implicitement, l'élimination est triviale
- Question "Quel pays a organisé la finale en 2006 ?" avec distracteurs USA, Brésil, Argentine, Allemagne
  → Allemagne est la seule option "logique" même sans connaissance cas source
RETEX_REF: RETEX_STD_B2_RECEVABILITE_PEDAGOGIQUE_002

DÉTECTION :
- Les distracteurs sont CONSISTENCY_FAIL avec un indice dans la question
- Un seul distracteur partage le contexte de la question
- La réponse est la seule "crédible" par déduction culturelle générale

---

## TYPE-PED-3 : Connaissance triviale / réponse évidente

[RULE-PED-T3-001]
La réponse est connue de toute personne, même sans intérêt pour le sujet du quiz.
La question ne teste aucune connaissance spécifique au thème.

EXEMPLES INVALIDES :
- "Dans quel pays se situe Buenos Aires ?" (dans un quiz cas source)
RETEX_REF: RETEX_STD_B2_RECEVABILITE_PEDAGOGIQUE_003
- "Quelle est la couleur du maillot traditionnel du Brésil ?" (N1 extrême — réponse déductible par indice unique)

SEUIL :
- Si >90% d'un public non-spécialiste peut répondre sans hésiter → TYPE-PED-3
- À distinguer des questions N1 légitimes (faciles mais requérant un minimum de mémoire du domaine)

---

## TYPE-PED-4 : Double sens / ambiguïté de réponse

[RULE-PED-T4-001]
La question admet plusieurs réponses correctes défendables.
Distinct de RULE-B2-HB-006 (univocité factuelle) :
TYPE-PED-4 couvre les cas où l'ambiguïté vient de la formulation, pas du fait.

EXEMPLES INVALIDES :
- "Quel joueur a été le plus décisif lors du mondial 1998 ?" → subjectif, plusieurs réponses valides
- "Quelle équipe a dominé les années 2000 ?" → "dominé" est interprétatif

DÉTECTION :
- La question contient des termes qualitatifs non définis ("le meilleur", "le plus important")
- Deux réponses différentes pourraient être défendues par deux personnes bien informées

---

# SECTION — PROCESSUS DE CONTRÔLE

[RULE-PED-005]
**Moment de VALIDATION**
Le VALIDATION de recevabilité pédagogique s'effectue :
1. En B2 — avant soumission humaine (RULE-B2-HB-005 complété par ce filtre)
2. En B5 — audit systématique de l'ensemble du pool

[RULE-PED-006]
**Séquence de VALIDATION en B2**
Pour chaque question candidate, poser les 4 questions suivantes :
1. La réponse est-elle révélée ou fortement suggérée dans le libellé ? → TYPE-PED-1
2. La bonne réponse est-elle déductible sans connaissance par élimination ? → TYPE-PED-2
3. La réponse est-elle connue de toute personne sans rapport au thème ? → TYPE-PED-3
4. La question admet-elle plusieurs réponses également défendables ? → TYPE-PED-4

Si OUI à l'une de ces 4 questions → la question est irrecevable.

[RULE-PED-007]
**Correction avant rejet**
Avant de rejeter une question irrecevable, tenter une reformulation.
Si la reformulation résout le FAILURE_CASE sans créer de collision → soumettre la version corrigée.
Si la reformulation est impossible → signaler le déficit d'angle et attendre décision humaine (RULE-B2-HB-001).

---

# SECTION — RELATION AVEC LES 8 FILTRES B2

[RULE-PED-008]
Les 4 VALIDATIONS TYPE-PED complètent la checklist 8 filtres (RULE-B2-HB-002) sans la remplacer.
Ordre d'application obligatoire :
1. Checklist 8 filtres (style, format, univocité factuelle)
2. VALIDATION recevabilité pédagogique (validité cognitive)

Une question passant les 8 filtres peut rester irrecevable pédagogiquement.

---

# SECTION — VALIDATION_CHECKLIST B5

[RULE-PED-009]
En B5_AUDIT, pour chaque question du pool :
- [ ] TYPE-PED-1 vérifié (pas de révélation dans le libellé)
- [ ] TYPE-PED-2 vérifié (pas de déduction par élimination)
- [ ] TYPE-PED-3 vérifié (connaissance non triviale requise)
- [ ] TYPE-PED-4 vérifié (réponse univoque et non subjective)

Toute question échouant un VALIDATION → FLAG_IRRECEVABLE + motif TYPE-PED-[N]

---

*STD_B2_recevabilite_pedagogique.md*
*Version 1.0 — 2026-05-18*
*Status: ACTIVE_REFERENCE*
*Source: RETEX source trou systémique #1 (lacune L01)*
RETEX_REF: RETEX_STD_B2_RECEVABILITE_PEDAGOGIQUE_004


