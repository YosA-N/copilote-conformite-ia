# Résultats de la séance 6 — le vrai examen

Toutes les mesures sont produites par les scripts du dépôt, ordinateur sur secteur. Depuis la partie 2, les questions v1 ont été relues et servent aussi au réglage. **La mesure finale se fera uniquement sur `eval/questions_v2.jsonl`** (figé au commit `65ee0c4`, jamais lu ni utilisé) **et sur les questions personnelles de l'auteur**.

## 1. Relectures (grille `eval/rubric.md`)

Commande : `scripts/review_summary.py --check`.

| Version | Questions | Juste | Partiel | Faux | Dangereux |
|---|---|---|---|---|---|
| v0 (séance 4) | 12 | 5 | 1 | 3 | 3 |
| v1 (séance 5) | 12 | 9 | 2 | 0 | 1 |
| v2 (séance 5 bis) | 12 | 6 | 5 | 0 | 1 |
| v3 (séance 5 ter), questions v0 | 12 | **10** | 2 | 0 | 0 |
| **heldout_v3** : même configuration, questions v1 | 20 | **6** | 5 | 5 | **4** |

La v3 paraît bonne sur les questions qui ont servi à la régler (v0), mais pas sur les questions v1 : c'est du **sur-apprentissage** (**overfitting**).

## 2. Diagnostic de heldout_v3 (avant tout changement)

Cause principale de chaque réponse non juste :
- (a) recherche : l'article ou le paragraphe utile n'est pas dans les 5 passages ;
- (b) rédaction : il y est, mais le modèle se trompe ;
- (c) longueur : réponse coupée ;
- (d) hors sujet non refusé.

| Question | Verdict | Cause | Détail |
|---|---|---|---|
| q14 | faux | (a) | art. 21 au rang 16 ; réponse aussi coupée (c) |
| q15 | dangereux | (a) | art. 28 au rang 6 |
| q16 | partiel | (a) | art. 46 trouvé, art. 45 absent ; plus un paragraphe sans rapport (b) |
| q18 | dangereux | (a) | seul l'art. 9, § 3 est trouvé ; le § 1 (l'interdiction) est au-delà du rang 30. « santé » attire le § 3 (« professionnel de la santé ») |
| q21 | partiel | (a) | art. 32 au rang 25 |
| q24 | dangereux | (a) | art. 5 au rang 8 ; le point f) (émotions) au rang 10 ou 11 |
| q12 | partiel | (b) | art. 15 présent, mais son § 1 est oublié |
| q20 | faux | (b) | « 13 ans » figure dans l'extrait mais est omis |
| q22 | partiel | (b) | art. 7 présent ; le § 1 est oublié et le § 2 mal lu |
| q25 | faux | (b) | « peut faire preuve » devient un critère obligatoire |
| q26 | dangereux | (b) | art. 50, § 4 présent ; la condition (hypertrucage) et l'acteur sont perdus |
| q27 | faux | (b) | le modèle prend l'art. 100 ; le § 4 de l'art. 99 est exclu par la limite de 2 par article ((a) secondaire) |
| q23 | partiel | (c) | réponse coupée |
| h05 | faux | (d) | statuts d'association traités avec 5 passages sans rapport |

**Bilan** : 6 réponses relèvent de la recherche (dont 3 des 4 dangereuses), 6 de la rédaction (dont 1 dangereuse), 1 de la longueur et 1 est un hors sujet traité. **Quand le bon article manque, le modèle répond quand même, avec assurance.**

**Un seuil sur le score de la recherche ne permet pas de s'abstenir** :

| Groupe (32 questions v0 et v1) | Score du 1er passage : moyenne (min – max) |
|---|---|
| Article attendu dans les 5 passages (23) | 0,653 (0,553 – 0,742) |
| Article attendu absent (4) | 0,599 (0,527 – 0,673) |
| Hors sujet (5) | 0,473 (0,398 – 0,570) |

q24, dangereuse, a 0,673 ; h05, hors sujet, a 0,570, soit plus que q16, une question bien couverte (0,553).

## 3. Mesure au niveau du paragraphe

Quand un article est découpé en plusieurs morceaux et qu'un paragraphe précis compte, `expected` le précise désormais, pour 3 questions v0 et 9 questions v1. Exemple : q18 → art. 9, § 1 et § 2, pas le § 3. Les scripts mesurent deux niveaux :
- **article** : chaque référence est ramenée à son article ou à son point d'annexe, si bien que les chiffres publiés avant ne changent pas ;
- **paragraphe** : il faut trouver le paragraphe précisé.

Un morceau découpé par points (`par_2_a-i`) compte pour son paragraphe. **La mesure par article cachait des échecs** : pour q18, elle comptait l'art. 9 comme trouvé au rang 1 alors que le paragraphe utile manquait.

## 4. Recherche

Commande : `scripts/compare_retrieval.py --repeat 3` (trois mesures identiques).

**Avant le nouveau lexique :**

| Configuration | Niveau | v0 hit@1 | v0 hit@5 | v0 hit@8 | v1 hit@1 | v1 hit@5 | v1 hit@8 |
|---|---|---|---|---|---|---|---|
| vecteurs + lexique + 2 par article (v3) | article | 7/10 | 10/10 | 10/10 | 10/17 | 13/17 | 15/17 |
| | paragraphe | 7/10 | 10/10 | 10/10 | 8/17 | 11/17 | 12/17 |
| vecteurs + lexique + 3 par article | article | 7/10 | **9/10** | 10/10 | 10/17 | 13/17 | 15/17 |
| | paragraphe | 7/10 | 9/10 | 10/10 | 8/17 | 11/17 | 13/17 |

**Après le nouveau lexique** (7 entrées générales tirées des échecs de v1) :

| Configuration | Niveau | v0 hit@1 | v0 hit@5 | v0 hit@8 | v1 hit@1 | v1 hit@5 | v1 hit@8 |
|---|---|---|---|---|---|---|---|
| **vecteurs + lexique + 2 par article (retenu)** | article | 7/10 | **10/10** | 10/10 | 14/17 | **17/17** | 17/17 |
| | paragraphe | 7/10 | 10/10 | 10/10 | 12/17 | **15/17** | 15/17 |
| vecteurs + lexique, sans limite | article | 7/10 | 9/10 | 10/10 | 14/17 | 17/17 | 17/17 |
| | paragraphe | 7/10 | 9/10 | 10/10 | 12/17 | 17/17 | 17/17 |
| vecteurs + lexique + 3 par article | article | 7/10 | 9/10 | 10/10 | 14/17 | 17/17 | 17/17 |
| | paragraphe | 7/10 | 9/10 | 10/10 | 12/17 | 16/17 | 16/17 |

Les 7 nouvelles entrées du lexique associent un mot courant au terme juridique :
- « santé, médical » → « données concernant la santé, catégories particulières » ;
- « lettre d'information, prospection » → « prospection, droit d'opposition » ;
- « protéger les données, sécurité » → « sécurité du traitement » ;
- « prestataire » → « sous-traitant » ;
- « États-Unis, hors de l'UE » → « transfert vers un pays tiers » ;
- « émotions » → « reconnaissance des émotions, pratiques interdites » ;
- « amendes, sanctions » → « amendes administratives ».

**Décisions :**
- **Nouveau lexique : retenu.** Le hit@5 ne baisse sur aucun jeu, et v1 monte (article 13 → 17/17, paragraphe 11 → 15/17). Ces entrées visent les échecs de v1 : **les scores v1 sont donc optimistes**, et seul l'examen final dira si elles généralisent.
- **Limite par article : 2 gardée.** Avec 3 ou sans limite, le niveau paragraphe de v1 serait meilleur (16 ou 17/17 : q18, q27), mais le hit@5 de v0 baisse (9/10, q10 au rang 6 ou 7). La règle l'exclut. C'est un vrai compromis : avec la limite de 2, le § 1 de l'art. 9 (q18) et les § 4 et 6 de l'art. 99 (q27) restent hors des 5 passages.
- **8 passages au lieu de 5 : non retenu.** Avec le nouveau lexique, le hit@8 n'apporte plus rien (égal au hit@5) et il coûtait du temps (section 6).

## 5. Juge d'abstention

Un second appel court au modèle reçoit la question et les extraits vérifiés, et répond OUI ou NON : « Ces extraits répondent-ils DIRECTEMENT à la question posée ? ». Si c'est NON, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. » ; les passages consultés restent affichés, avec une alerte.

**Calibrage sans régénérer**, sur les 32 réponses relues (v3 sur v0, heldout_v3 sur v1) :

| Verdict de la relecture | Abstentions du juge |
|---|---|
| juste | **0 / 12** |
| partiel | 2 / 7 (q16, q22) |
| faux | 1 / 5 (h05, le hors sujet) |
| dangereux | **2 / 4** (q15, q18) ; q24 et q26 passent |

Temps du juge : médian 4,5 s, maximal 14,3 s. **Retenu**, car il ne s'abstient sur aucune réponse juste. **Coût** : selon la grille, une abstention alors que le corpus répond est « fausse ». q16 et q22, partielles, deviendraient fausses, tandis que q15 et q18 passeraient de « dangereux » à « faux » et h05 de « faux » à « juste ».

## 6. Effet séparé de chaque changement sur les réponses dangereuses

| Question | Départ (v3, 5 passages) | 8 passages seuls | Juge seul | 8 passages + juge |
|---|---|---|---|---|
| q15 | dangereux ; art. 28 absent | **corrigée en apparence** : art. 28, § 3 au passage 6, « il est obligatoire de signer un contrat » | **abstention** | réponse gardée (juge OUI) |
| q18 | dangereux ; seul l'art. 9, § 3 | inchangé : § 1 et § 2 toujours absents, même réponse dangereuse | **abstention** | réponse dangereuse gardée (juge OUI) |
| q24 | dangereux ; art. 5 absent | **inchangé** : le 8e passage (art. 5) est retiré faute de place, 7 passages seulement ; « Oui, vous avez le droit… » | réponse gardée (juge OUI) | réponse gardée |
| q26 | dangereux (rédaction) | inchangé | réponse gardée | réponse gardée |
| h05 | faux (hors sujet traité) | inchangé | **abstention** | **abstention** |

Ce n'est pas un verdict : c'est ma lecture rapide, et la relecture reste la vôtre. Points à retenir :
- **q24 : l'hypothèse « ce sont les 8 passages qui aident » ne se vérifie pas.** L'art. 5 arrivait au rang 8 par son morceau a) à e), qui n'est pas le bon. Le point f) (émotions) était au rang 10 ou 11, et le 8e passage a été retiré faute de place dans le contexte : 5 questions sur 32 ont reçu moins de 8 passages. C'est **le lexique** qui règle q24 : le point f) arrive au rang 2.
- **Le juge n'est pas stable** : sur q18, il dit NON sur la réponse de départ et OUI sur celle à 8 passages, qui est presque identique.
- **q26 (rédaction)** n'est réglée ni par plus de passages ni par le juge.
- **Temps de « 8 passages seuls »** : génération médiane de 48 s, maximale de 93 s (prompt de 4 345 tokens en moyenne, contre 3 186), au-delà de l'objectif de 60 s.

## 7. Configuration complète (v4)

Changements retenus :
- **recherche** : nouveau lexique, 5 passages, au plus 2 par article ;
- **juge d'abstention** activé (`ANSWER_JUDGE=on`) ;
- **longueur** : `LLM_MAX_TOKENS` porté de 1 500 à 2 000 ;
- **prompt** : la règle « un extrait de chaque passage utile d'abord » est retirée, et une consigne demande « Les passages trouvés ne traitent pas directement de votre question. » quand les passages ne traitent que d'un sujet voisin.

Commande : `compare_models.py qwen3:4b-instruct` (32 questions, mêmes réglages que v3 pour le reste).

| Mesure (32 questions) | v3 (séance 5 ter) | 8 passages seuls | **v4** |
|---|---|---|---|
| Réponses données (sur 27) | 27 | 27 | 26 (1 abstention : q22) |
| Avec un extrait vérifié de l'article attendu | 22 | 23 | **26** |
| Avec un extrait vérifié du paragraphe attendu | — | 21 | **24** |
| Hors sujet refusés (sur 5) | 4 | 4 | **5** |
| Extraits vérifiés / recopiés | 78 / 85 | 92 / 97 | 72 / 79 |
| Réponses coupées | 2 | 2 | **0** |
| Réponses avec au moins une alerte | 15 / 32 | 10 / 32 | 14 / 32 |
| Mots par réponse donnée | 131 | 137 | 134 |
| Prompt lu (tokens, moyenne) | 3 186 | 4 345 | 3 176 |
| Temps médian (génération + juge) | 31 s | 48 s | **40 s** |
| Temps maximal (génération + juge) | 75 s | 93 s | **105 s** |
| Questions au-delà de 60 s | 2 / 32 | 9 / 32 | **6 / 32** (q23, q27, q04, q11, q21, q16) |

**Temps : l'objectif d'environ 60 s au plus n'est pas tenu.** Les réponses lentes sont celles où le modèle recopie de très longs extraits. Par exemple, pour q23, il écrit 1 083 mots, dont 318 de réponse ; pour q04, 1 143 mots, dont 254. La limite de 2 000 tokens supprime les réponses coupées, mais laisse ces écritures s'allonger.

Les fichiers de réponses donnent des temps plus mauvais, à cause d'incidents de la machine. Ils ne sont pas retenus comme mesure :
- q20 de heldout_v4 : l'ordinateur s'est mis en veille pendant la question ;
- q06 de v4 : génération à 6 tokens/s au lieu de 28 ;
- q17 de heldout_v4 : environ 3 minutes bloquée à la lecture du prompt.

| Fichier | Temps total médian | Maximum | Au-delà de 60 s |
|---|---|---|---|
| `answers_v3.md` | 36 s | 70 s | 1 / 12 |
| `answers_heldout_v3.md` | 40 s | 77 s | 3 / 20 |
| `answers_v4.md` | 42 s | 188 s (incident) | 2 / 12 |
| `answers_heldout_v4.md` | 42 s | 216 s (incident ; q20 exclue) | 5 / 20 |

**Compromis proposé (non fait, à valider)** : 60 s correspondent à environ 12 s de lecture du prompt, 5 s de juge et 43 s d'écriture, soit environ 1 200 tokens à 28 tokens/s. Deux leviers :
- demander des **extraits courts**, une phrase ou un point de 40 mots au plus, puisque ce sont les extraits qui allongent l'écriture ;
- ramener `LLM_MAX_TOKENS` à environ 1 200.

Risque : des réponses de nouveau coupées sur les longues listes (q04, q23), donc « partiel » selon la grille. À mesurer sur v0 et v1.

**Ma lecture rapide des réponses surveillées** (le verdict reste le vôtre), dans `answers_heldout_v4.md` :
- **q15** : corrigée en apparence. L'art. 28, § 3 est trouvé : « il faut signer un contrat particulier ».
- **q18** : toujours problématique. La réponse dit « Oui… », sans l'interdiction de principe (§ 1) ni ses exceptions (§ 2), que la limite de 2 par article tient hors des passages (les § 3 et § 4 occupent les deux places).
- **q24** : juste en apparence : « Non, vous n'avez pas le droit…, sauf si … pour des raisons médicales ou de sécurité ». Mais dans la comparaison des 32 questions, faite le même jour avec la même configuration, le modèle avait **inversé** l'exception (« à condition que … pour des raisons autres que médicales ») ; l'alerte « négation » l'avait signalé. **Le modèle n'est pas stable d'un lancement à l'autre.**
- **q26** : la condition d'hypertrucage manque toujours (erreur de rédaction).
- **h05** : refusée par le modèle lui-même (« Les textes trouvés ne permettent pas de répondre… »).
- **q22** : abstention du juge, alors que le corpus contient la réponse (art. 7) : « faux » selon la grille.

## 8. Points ouverts

- **Temps** : compromis à valider (section 7).
- **Limite par article** : avec 2, q18 et q27 perdent le paragraphe utile ; avec 3 ou sans limite, v0 perd q10. Une autre piste générale serait de garder le premier paragraphe d'un article découpé, qui pose souvent la règle, quand un autre de ses paragraphes est retenu.
- **Juge** : utile sur les hors sujet et sur certaines réponses sans bon article (q15, q18 à la calibration), mais instable, et il coûte des réponses partielles (q16, q22).
- **Rédaction** (q20, q25, q26) : aucune correction générale dans cette séance.
- **Optimisme de v1** : les nouvelles entrées du lexique viennent des échecs de v1. Seul l'examen final (`questions_v2.jsonl` et les questions de l'auteur) mesurera la généralisation.
