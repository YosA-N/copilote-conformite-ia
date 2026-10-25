# Relecture des réponses v0 — référence

Relecture humaine de `eval/answers_v0.md` (séance 4 : `ministral-3:3b`, recherche par vecteurs seuls). C'est la référence à laquelle les versions suivantes sont comparées.

## Bilan

| Verdict | Nombre | Questions |
|---|---|---|
| Justes | 5 | q06, q07, q08, h01, h02 |
| Partielles | 2 | q01, q02 |
| Fausses | 5 | q03, q04, q05, q09, q10 |

Sur les 10 questions RGPD et AI Act : 3 justes, 2 partielles, 5 fausses. Les 2 questions hors sujet (h01, h02) ont été bien refusées.

## Réponses dangereuses

- **q03 (durée de conservation)** : invente « 10 ans maximum » à partir de l'art. 18 de l'AI Act, qui concerne la conservation de la documentation des systèmes d'IA. Le RGPD ne fixe aucune durée.
- **q09 (tri de CV)** : répond « vous ne pouvez pas trier des CV avec une IA ». C'est faux : c'est permis, mais classé à haut risque (AI Act, annexe III, point 4), avec des obligations pour le déployeur (art. 26).

## Autres erreurs

- **q01 (DPO)** : dit « oui, vous devez » et lit l'art. 37, § 4 comme une obligation pour les associations, alors que c'est une possibilité.
- **q02 (registre)** : formule mal l'exception pour les structures de moins de 250 salariés (art. 30, § 5).
- **q04 (mention d'information)** : hors sujet ; le bon article (RGPD art. 13) n'a pas été trouvé par la recherche.
- **q05 (délai d'accès)** : ignore le bon passage (art. 12, § 3 : un mois), pourtant fourni au modèle.
- **q10 (IA générative au travail)** : hors sujet ; le bon article (AI Act art. 4) n'a pas été trouvé par la recherche.

## Causes retenues pour la séance 5

1. **Recherche** : q04 et q10, le bon article n'est pas dans les passages.
2. **Fidélité aux sources** : q03, q05, q09 et q01, le bon passage est fourni ou une citation existe, mais la réponse ne dit pas ce que dit le texte.
3. **Modèle** : comparer `ministral-3:3b` avec `qwen3:4b-instruct`, avec le même prompt et les mêmes passages.
