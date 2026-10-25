# Relecture des réponses v1

Relecture humaine de `eval/answers_v1.md` (séance 5 : `qwen3:4b-instruct`, recherche par vecteurs + lexique, extraits vérifiés mot pour mot). C'est la référence pour la séance 5 bis.

## Bilan

| Verdict | Nombre | Questions |
|---|---|---|
| Justes | 9 | q01, q03, q04, q05, q07, q08, q09, h01, h02 |
| Partielles | 2 | q02, q06 |
| Fausses | 1 | q10 (dangereuse) |

Par rapport à v0 (5 justes, 2 partielles, 5 fausses) : les deux réponses dangereuses de v0 (q03 « 10 ans maximum », q09 « vous ne pouvez pas trier des CV ») sont corrigées.

## Réponses partielles

- **q02 (registre)** : oublie la condition « pas de données sensibles » de l'exception de l'art. 30, § 5 (l'exception ne joue pas si le traitement porte sur des catégories particulières de données, art. 9, § 1, ou sur des données relatives à des condamnations pénales, art. 10).
- **q06 (fuite de données)** : oublie l'information des personnes concernées en cas de risque élevé (art. 34).

## Réponse fausse et dangereuse

- **q10 (IA générative au travail)** : l'art. 4 de l'AI Act (maîtrise de l'IA) n'est pas retrouvé par la recherche. La réponse, appuyée sur des extraits vérifiés de l'art. 50, conclut qu'il n'y a « aucune obligation » pour l'usage interne, ce que contredit l'art. 4.

## Défauts à corriger de façon générale (séance 5 bis)

1. Retrouver l'art. 4 pour q10, en corrigeant une cause générale ; ne jamais conclure « aucune obligation » parce que les passages n'en parlent pas.
2. Obtenir des citations [n] dans le texte de la réponse, ou revoir l'alerte « aucune citation » pour qu'elle reste rare.
3. Toujours vouvoyer, avec un contrôle dans le code.
4. Répondre à toutes les parties de la question ; quand les passages ne donnent qu'un principe, le dire et indiquer que les règles concrètes viennent d'autres textes.
