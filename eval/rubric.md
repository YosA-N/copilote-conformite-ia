# Grille de relecture des réponses

Cette grille sert à relire chaque réponse du copilote de la même façon, d'une version à l'autre. On juge la réponse **affichée à l'utilisateur**, par rapport aux textes du corpus (RGPD, AI Act) et à l'article attendu de la question.

## Les 4 verdicts

| Verdict | Définition |
|---|---|
| **juste** | Exact et complet par rapport aux textes. |
| **partiel** | Exact mais incomplet, ou petite imprécision sans risque. |
| **faux** | Erreur sur le fond. |
| **dangereux** | Erreur qui pourrait faire agir quelqu'un à tort : inventer une obligation, une durée ou une interdiction, ou en nier une. |

## Cas limites

Ces règles ont été validées par l'auteur à la séance 6. Elles reprennent les choix de ses relectures précédentes.

1. **En cas de doute** entre deux verdicts, on retient le plus sévère. « Dangereux » l'emporte sur « faux ».
2. **Question hors sujet** :
   - refusée proprement (« Les textes trouvés ne permettent pas de répondre à cette question. ») : **juste** ;
   - traitée quand même : **faux**, ou **dangereux** si la réponse invente une règle.
3. **Refus alors que le corpus contient la réponse** : **faux**, car la personne n'obtient pas l'information.
4. **Contenu juste mais réponse coupée** (limite de longueur atteinte) : **partiel** (exemple : q04 de la v3).
5. **Question à couverture « partielle »** (le corpus ne contient qu'une partie de la réponse) : **juste** si la réponse dit ce que dit le texte **et** signale que le reste dépend d'autres textes (droit national, CNIL…).
6. **Les alertes du code ne changent pas le verdict** : on juge la réponse affichée, pas les contrôles.
7. **Le commentaire est obligatoire** pour tout verdict autre que « juste ». Il dit ce qui manque ou ce qui est faux, avec l'article concerné.

Exemples tirés des relectures :
- **dangereux** :
  - v0 q03 invente une durée de conservation de « 10 ans maximum » ;
  - v0 q01 transforme une possibilité (art. 37, § 4) en obligation ;
  - v2 q08 inverse une exception (« sauf si cela ne ressort pas clairement »).
- **partiel** :
  - v2 q06 oublie l'information des personnes (art. 34) ;
  - v3 q10 attribue à l'utilisateur une obligation du fournisseur (art. 50, § 1).

## Format des relectures

Une relecture par version, dans `eval/reviews/<version>.jsonl` (par exemple `v3.jsonl` relit `eval/answers_v3.md`). Il y a une ligne par question relue :

```json
{"id": "q04", "verdict": "partiel", "comment": "Contenu juste, mais réponse coupée à 1 500 tokens."}
```

- `id` : l'identifiant de la question, comme dans `eval/answers_<version>.md` ;
- `verdict` : `juste`, `partiel`, `faux` ou `dangereux` ;
- `comment` : le commentaire du relecteur (obligatoire, sauf pour « juste »).

Les relectures détaillées des premières versions restent dans `eval/review_v0.md`, `review_v1.md` et `review_v2.md`. Les fichiers JSONL sont la source des chiffres.

## Calculer le tableau des verdicts

```powershell
.venv\Scripts\python scripts\review_summary.py           # tableau des verdicts de toutes les versions relues
.venv\Scripts\python scripts\review_summary.py --check   # vérifie aussi que chaque relecture couvre exactement les questions de eval\answers_<version>.md
```
