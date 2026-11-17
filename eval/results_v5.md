# Examen final — questions_v2 et questions de l'auteur

L'examen final mesure la configuration retenue sur des questions qui n'ont servi à aucun réglage : `eval/questions_v2.jsonl` (20 questions, figées au commit `65ee0c4`, ni lues ni utilisées avant cet examen) et `eval/questions_author.jsonl` (6 questions). **Il n'est pas encore lancé.**

## 1. Questions de l'auteur (`eval/questions_author.jsonl`)

**Provenance : questions écrites par Claude Code à la demande de l'auteur, qui l'a choisi ; Claude Code connaissait le projet (lexique, points faibles q16 et q24) : biais possible.**

Écrites le 17/11/2026, dans la persona d'un responsable de petite entreprise ou d'association, avec des mots simples et sans citer d'article. Sujets choisis pour ne pas reprendre ceux de v0 et v1 ; le recouvrement avec `questions_v2.jsonl` n'a pas pu être vérifié par Claude, qui ne lit pas ce fichier (le test `test_author_questions_are_well_formed_if_present` vérifie seulement que les identifiants diffèrent de ceux de tous les autres fichiers).

Articles attendus fixés en **lisant le texte du corpus** (`data/processed/chunks.jsonl`), jamais avec la recherche ni le modèle. **À vérifier par l'auteur avant l'examen.**

| Id | Question | Articles attendus | Voisins utiles | Couverture |
|---|---|---|---|---|
| a01 | J'ai 12 salariés et je voudrais remplacer la badgeuse par une pointeuse à empreinte digitale. J'ai le droit ? | RGPD art. 9, § 1 et § 2 | art. 4, point 14 ; art. 9, § 4 | partiel |
| a02 | Un partenaire commercial me propose de racheter notre fichier clients. Est-ce que je peux le lui vendre ? | RGPD art. 6, § 1 et art. 5 | art. 6, § 4 ; art. 13 ; art. 14, § 1 ; art. 21 | partiel |
| a03 | Je pense acheter un logiciel d'IA qui note les résultats de mes commerciaux et propose qui mérite une prime. Qu'est-ce que je dois savoir avant de l'utiliser ? | AI Act annexe III, point 4 ; art. 26, § 7 | art. 26, § 1 et § 2 ; art. 6, § 3 ; art. 4 ; art. 86 ; RGPD art. 22 | complet |
| a04 | Pendant nos réunions, un outil d'IA enregistre la discussion et rédige le compte rendu tout seul. Est-ce que je dois prévenir les participants ? | RGPD art. 13 et art. 6, § 1 | art. 5 ; art. 21 ; AI Act art. 4 | partiel |
| a05 | On veut publier sur notre site et sur Facebook les photos de la fête de l'association, où l'on voit des adhérents et leurs enfants. Faut-il leur demander la permission ? | RGPD art. 6, § 1 et art. 7 | art. 4, point 1 ; art. 8 ; art. 13 ; art. 17 ; art. 21 | partiel |
| ha01 | Combien de jours de congés payés a un salarié à temps partiel ? | aucun (hors sujet) | — | hors corpus |

Les justifications détaillées (points et paragraphes, ce qui manque au corpus) sont dans le champ `note` de chaque question.
