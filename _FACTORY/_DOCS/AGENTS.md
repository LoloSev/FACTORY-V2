\# AGENTS — QUIZZZ FACTORY

DEPENDENCY:
- MASTER_ARCHITECTURE.md
- PIPELINE_V2.md
- glossaire_documentaire_factory.md


\## MISSION

Appliquer uniquement la refonte définie dans :

\- refonte\_arbo\_v1\_1.txt



\## RÈGLES ABSOLUES



\- ne jamais supprimer un fichier sans validation

\- ne jamais modifier les IDs documentaires

\- ne jamais renommer librement

\- respecter strictement les phases A\*/B\*

\- respecter les suffixes INIT/WIP/FINAL

\- migration thème par thème

\- ne jamais déplacer plusieurs thèmes simultanément

\- ne jamais modifier MASTER sans validation

\- ne jamais modifier glossaire sans validation

\- appliquer intÃ©gralement les rÃ¨gles FACTORY actives dans tout LAB conformÃ©ment Ã  `RULE-LAB-001` de `MASTER_ARCHITECTURE.md`



\## INTERDICTIONS



\- aucune refactorisation supplémentaire

\- aucune création de nouveaux standards

\- aucun changement de naming hors document officiel

\- aucun merge automatique



\## MÉTHODE



1\. créer nouveaux dossiers

2\. déplacer fichiers

3\. renommer fichiers

4\. VALIDER CONSISTENCY

5\. VALIDER chemins

6\. commit git



\## QA OBLIGATOIRE



VALIDER :

\- chemins morts

\- collisions naming

\- doublons

\- locks résiduels

\- fichiers hors phase

\- CONSISTENCY_FAILURE MASTER/glossaire

