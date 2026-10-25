# Relecture des réponses v2

Relecture humaine de `eval/answers_v2.md` (séance 5 bis : `qwen3:4b-instruct`, recherche par vecteurs + lexique, au plus 2 passages par article, prompt au « vous » avec exemple fictif, contrôles du code). C'est la référence pour la séance 5 ter.

## Bilan

| Verdict | Nombre | Questions |
|---|---|---|
| Justes | 6 | q03, q04, q05, q09, h01, h02 |
| Partielles | 5 | q01, q02, q06, q07, q10 |
| Fausses | 1 | q08 |

Par rapport à v1 (9 justes, 2 partielles, 1 fausse) : la v2 recule, même si q10 cite désormais l'art. 4.

## Réponse fausse

- **q08 (chatbot)** : l'exception est inversée (« sauf si cela NE ressort PAS clairement ») alors que l'art. 50, § 1 dit « sauf si cela ressort clairement ». Reformuler une exception a inversé son sens.

## Réponses partielles

- **q07 (AIPD)** : mélange l'AIPD du RGPD (art. 35) avec l'analyse d'impact sur les droits fondamentaux de l'AI Act (art. 27), deux obligations différentes.
- **q01 (DPO)** : ne donne plus qu'un des 3 cas obligatoires de l'art. 37, § 1.
- **q06 (fuite de données)** : oublie toujours l'information des personnes en cas de risque élevé (art. 34).
- **q02 (registre)** : oublie la condition « non occasionnel » de l'exception de l'art. 30, § 5.
- **q10 (IA générative au travail)** : l'art. 4 est bien cité, mais l'obligation d'informer les personnes qui interagissent avec une IA (art. 50, § 1) vise le fournisseur, pas l'organisation qui utilise l'outil.

## Autre remarque

- **q09** : faute de frappe « Cependi ».

## Défauts à corriger de façon générale (séance 5 ter)

1. Exceptions et conditions (« sauf si », « à moins que », « lorsque », « sous réserve de ») recopiées mot pour mot entre « » depuis un extrait vérifié, jamais reformulées. Le code vérifie que le texte entre guillemets existe dans un extrait et signale une négation ajoutée ou supprimée. La phrase fausse de q08 v2 devient un test de non-régression.
2. Ne pas mélanger les textes : chaque obligation nomme son règlement (RGPD ou AI Act) et son article ; deux obligations de textes différents ne sont jamais fusionnées sous un même nom ; préciser qui est visé (responsable du traitement, fournisseur, déployeur).
3. Listes complètes : quand un extrait énumère des cas (a, b, c…), la réponse reprend tous les cas, ou dit explicitement qu'elle n'en cite qu'une partie.
4. Questions en plusieurs parties : vérifier si le passage manquant (art. 34 pour q06) est dans les 5 passages ; s'il manque, corriger la recherche de façon générale ; s'il est présent, renforcer la règle « répondre à chaque partie ».
5. README : section « Limites connues ».
