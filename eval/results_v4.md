# Séance 7 bis — q24 : abstention avec les trois modèles, recherche ou juge ?

Question q24 de `eval/questions_v1.jsonl` : « Ai-je le droit d'utiliser une IA qui analyse les émotions de mes salariés ? ». Article attendu : AI Act, art. 5, § 1, f) (interdit sur le lieu de travail, sauf raisons médicales ou de sécurité ; morceau `ai_act:art_5:par_1_f-h`).

Avec la configuration v4, les trois modèles de la séance 7 s'abstiennent (`answers_heldout_v4.md`, `answers_heldout_v4_big_qwen27b.md`, `answers_heldout_v4_big_gptoss.md`) : verdict « faux » dans les trois relectures (« abstention alors que l'art. 5, § 1, f répond ; sans danger, mais sans réponse »).

## 0. Avertissement de méthode : q24 est une question v1

q24 fait partie de `questions_v1.jsonl`. Depuis la séance 6, partie 2, les questions v1 ont été relues par l'auteur et servent au réglage avec v0 ; elles ne sont plus « jamais vues ». **Diagnostiquer et corriger en regardant q24 confirme cet état** : toute mesure sur v1 après cette séance est optimiste, puisque l'une des entrées aura été choisie pour q24. **Le seul examen propre qui reste est `eval/questions_v2.jsonl` (figé au commit `65ee0c4`) plus les questions personnelles de l'auteur (`eval/questions_author.jsonl`)** : ni l'un ni l'autre n'a été lu ni utilisé ici.

Règle de décision inchangée : une correction est gardée si elle ne fait baisser le hit@5 ni sur v0 ni sur v1, et fait monter au moins une mesure.

## 1. La recherche : l'art. 5 n'est pas dans les 5 passages

Mesures du 16/11/2026, sur secteur, `bge-m3` sur CPU, configuration v4 (lexique `all`, 5 passages, 2 par article au plus, 1er paragraphe), `scripts/search.py -k 20` puis `scripts/compare_retrieval.py --repeat 3` (3 mesures identiques pour q24).

| Question envoyée à la recherche | Rang de `art_5:par_1_f-h` | 5 premiers passages (score) |
|---|---|---|
| question seule, sans lexique | 10 | art. 50 § 3 (0,650), art. 27, annexe III pt 4, art. 7 § 2, art. 92 |
| **lexique actuel** : + « personne concernée ; systèmes de reconnaissance des émotions » | **10 à 11** | art. 50 § 3 (0,702), art. 3 déf. 39 (0,684), annexe III pt 4 (0,664), art. 86 (0,656), annexe III pt 5 (0,653) |

Les 5 passages donnés aux trois modèles sont bien ceux-là (même liste dans les trois fichiers). Score de l'art. 5, § 1, f-h : 0,631, derrière 10 passages qui parlent de « système de reconnaissance des émotions » (art. 50, § 3 et la définition 39, où l'expression figure mot pour mot), de « salariés » (annexe III, point 4 : emploi) ou de « droit » (art. 86 : droit à l'explication).

**Pourquoi** : le texte de l'art. 5, § 1, f) ne dit ni « reconnaissance des émotions » ni « salariés » ; il dit « inférer les émotions d'une personne physique sur le lieu de travail », sous le titre « Pratiques interdites ». Et la question ne dit pas « interdit » : elle dit « ai-je le droit ». Le modèle de vecteurs ne fait pas le pont entre « ai-je le droit de… » et « … sont interdites ». L'entrée de lexique retirée à la séance 6 (« pratiques interdites en matière d'IA ») faisait ce pont, mais en donnant la conclusion : elle a été rendue neutre (`results_v2.md`, section 10.1), et q24 est retombée au rang 10.

### 1.1 Hypothèse « le morceau f-h est trop long », réfutée

Le morceau `par_1_f-h` fait 2 418 caractères : le point f) (émotions, 1 phrase) y est noyé dans g) (catégorisation biométrique) et h) (identification biométrique à distance, 5 alinéas). Hypothèse : un morceau par point remonterait f).

Mesure (même question avec le lexique actuel, mêmes vecteurs `bge-m3`, similarité cosinus calculée à la main) :

| Texte comparé à la question | Similarité |
|---|---|
| morceau entier f-h (2 418 car.) | 0,631 |
| point f) seul, avec l'en-tête de l'article (505 car.) | 0,601 |
| point g) seul | 0,562 |
| point h) seul | 0,569 |
| 5e passage retenu aujourd'hui (seuil d'entrée) | 0,653 |

Le point f) seul fait **moins** bien que le morceau entier : découper plus finement ne ferait pas entrer l'art. 5 dans les passages. Hypothèse écartée, sans changer le découpage.

### 1.2 Ce que donneraient des entrées de lexique, pour q24 seulement

Mesure exploratoire (lexique appliqué à la main, `k=40`), avant toute décision ; l'effet sur v0 et v1 n'est pas mesuré ici.

| Ajout à la question | Rang de l'art. 5, § 1, f-h |
|---|---|
| « inférer les émotions » (l'expression du texte, piste notée en séance 6) | 7 |
| salariés → « sur le lieu de travail » au lieu de « personne concernée » | 8 |
| les deux | 7 |
| **ai-je le droit → « pratique interdite ou autorisée »** (forme de la question, les deux issues) | **3** (art. 5 a-e au rang 1, art. 50 § 3 au rang 2) |
| ancienne entrée de la séance 6 « pratiques interdites en matière d'IA » (pour mémoire, non neutre) | 1 |

Le vocabulaire du texte ne suffit pas (rang 7-8). Ce qui fait entrer l'art. 5, c'est le mot « interdit ». Une entrée qui traduit la **forme** de la question (« ai-je le droit », « est-ce permis / autorisé / interdit », « est-ce légal ») par « pratique interdite ou autorisée » ne contient pas la réponse : elle dit que la question porte sur une permission, sans dire laquelle. Elle n'est pas liée aux émotions.

Limite de la mesure : dans v0 et v1, **seule q24** a la forme « ai-je le droit ». Une entrée aussi étroite ne serait testée que sur q24 ; une entrée plus large (« puis-je utiliser », « peut-on utiliser ») toucherait aussi q09 (« Puis-je utiliser une IA pour trier des CV ? », attendus annexe III pt 4 et art. 26), où « interdite » pourrait faire entrer l'art. 5 et sortir l'art. 26. C'est ce que `compare_retrieval.py --repeat 3` devra dire.

## 2. Le juge : rejoué sur les mêmes passages, en local et en mode distant

Rejeu de `judge_extracts` (même consigne, même question), sans régénérer les fichiers de réponses, le 16/11/2026, 3 appels par cas. Modèle local `qwen3:4b-instruct` (Ollama) et modèle distant `qwen/qwen3.8-27b` (Groq, `reasoning_effort=none`) ; seuls la question de test et des extraits de loi ont été envoyés.

### 2.1 Sur les extraits des fichiers (sans l'art. 5) : NON, cohérent

| Extraits soumis au juge | Juge local | Juge distant |
|---|---|---|
| les 5 extraits vérifiés du fichier local v4 (art. 50 § 3, déf. 39, annexe III pt 4, art. 86, annexe III pt 5) | NON, NON, NON | NON, NON, NON |
| les 6 extraits du fichier qwen27b | NON, NON, NON | NON, NON, NON |

Les deux juges disent NON, trois fois sur trois, et ils ont raison : aucun de ces extraits ne dit si l'usage est permis. **L'abstention des trois fichiers est la bonne décision pour ces passages-là : la cause première est la recherche.**

### 2.2 Avec l'extrait de l'art. 5, § 1, f) ajouté : les deux juges divergent

| Extraits soumis au juge | Juge local | Juge distant |
|---|---|---|
| art. 50 § 3 + déf. 39 + **point f)** | **NON, NON, NON** | **OUI, OUI, OUI** |

Chaîne complète (`answer_from_passages` + juge) avec le morceau de l'art. 5 mis en 5e passage à la place de l'annexe III, point 5, 2 essais par modèle :

| Modèle | Extrait de l'art. 5 recopié | Juge | Réponse |
|---|---|---|---|
| local | oui (2/2 essais, 2 extraits vérifiés sur 2) | NON (2/2) | **abstention** |
| distant | oui (2/2, 3 extraits vérifiés sur 3) | OUI (2/2) | « Non, vous n'avez pas le droit…, car l'AI Act interdit « l'utilisation de systèmes d'IA pour inférer les émotions d'une personne physique sur le lieu de travail » [5]. Cette interdiction comporte une exception « sauf lorsque … pour des raisons médicales ou de sécurité » [5]. … » (fidèle ; alertes du code : « absence affirmée » sur « vous n'avez pas le droit », une « » hors extraits sur une phrase de l'art. 50) |

**Pour le modèle distant, corriger la recherche suffit.** Pour le modèle local, non : avec le bon passage, il recopie la bonne phrase, et son propre juge la rejette.

### 2.3 Pourquoi le juge local dit NON, et pourquoi on ne le corrige pas par la consigne

Variantes, juge local, 3 appels chacune :

| Extraits | Verdict |
|---|---|
| point f) seul | NON ×3 |
| point f) + définition 39 | OUI ×3 |
| point f) précédé de sa source (« AI Act, article 5 : Pratiques interdites…, § 1, points f) à h) ») | OUI ×3 |
| point f) avec son amorce (« 1. Les pratiques en matière d'IA suivantes sont interdites: f) … ») | OUI ×3 |
| art. 50 § 3 + point f), bruts, avec sources, avec amorce, ou les deux | NON ×3 à chaque fois |
| art. 50 § 3 + déf. 39 + point f), bruts, avec sources, ou amorce | NON ×3 à chaque fois |
| les 5 extraits du fichier local + point f) | OUI ×3 |
| art. 50 § 3 + déf. 39 **sans** point f) | **OUI ×3** (à tort) |

Le juge local ne juge pas chaque extrait : son verdict dépend du **mélange**. L'extrait de l'art. 50, § 3 (longue obligation de transparence, avec « cette obligation ne s'applique pas… ») le tire vers NON même quand la phrase qui répond est à côté ; et sans cette phrase, il dit OUI à deux extraits qui ne répondent pas. Nommer la source ou garder l'amorce ne change rien quand l'art. 50 est là. Une consigne « OUI si au moins un extrait répond » a été essayée : elle dit OUI à tout, y compris aux 5 extraits d'aujourd'hui (l'abstention disparaît). **À cette taille de modèle, le juge est un signal bruité sur cette question** (déjà noté à la séance 6 : « le juge n'est pas stable »). Le juge distant, lui, est cohérent dans tous les cas mesurés (NON sans l'art. 5, OUI avec).

## 3. Les autres abstentions (q10, q18, q22 de gpt-oss ; q22 en local) : pas la même cause

Dans ces trois cas, **l'article attendu était dans les 5 passages** (« Article attendu : … — passage [n] » dans les fichiers) ; pour q24, il était absent. La recherche n'est donc pas en cause.

| Question | Modèle | Article attendu | Dans les passages | Ce qui s'est passé |
|---|---|---|---|---|
| q10 (IA générative au travail) | gpt-oss | AI Act art. 4 | [5] | le modèle n'a cité **aucun** extrait de [5] : extraits de l'art. 50 (hypertrucages) et de l'art. 26 ; le juge a dit NON à des extraits qui ne répondaient pas. Erreur de **rédaction** (choix des extraits), juge cohérent. Le modèle local (partiel) et qwen27b (juste) ont cité l'art. 4. |
| q18 (santé des bénévoles) | gpt-oss | RGPD art. 9, § 1 et § 2 | [2] | extrait de l'art. 9, § 1 (« … les données concernant la santé … sont interdits ») : il répond directement ; le juge a dit NON. **Fausse abstention du juge**. Les deux autres modèles ont répondu (local : dangereux, qwen27b : faux). |
| q22 (consentement par écrit) | gpt-oss et local | RGPD art. 7 | [1] | extrait de l'art. 7, § 2 (déclaration écrite qui concerne aussi d'autres questions) : il ne dit pas si l'écrit est obligatoire ; répondre demande une déduction (art. 7, § 1 « démontrer », art. 4, point 11 « acte positif clair »). Le juge, strict sur « directement », s'abstient ; qwen27b a répondu (partiel). **Limite du juge sur les réponses par déduction**, pas une erreur de recherche. |

Conclusion : q24 est la seule abstention due à la recherche. q10 vient du choix des extraits par le modèle, q18 d'un NON du juge sur un extrait qui répond, q22 d'une question dont la réponse n'est pas écrite telle quelle dans le texte. Trois causes différentes ; on règle d'abord q24.

## 4. Diagnostic

1. **Recherche (les trois modèles)** : l'art. 5, § 1, f) est au rang 10-11, derrière 10 passages qui partagent les mots de la question (« reconnaissance des émotions », « salariés ») sans y répondre. Il manque le pont entre la forme « ai-je le droit » et le mot « interdites » du texte. Le découpage n'est pas en cause (le point f) seul fait moins bien). Le vocabulaire du texte (« inférer les émotions », « lieu de travail ») ne suffit pas (rang 7-8).
2. **Juge (modèle local seulement)** : même avec la bonne phrase recopiée, le juge local dit NON à cause des extraits voisins ; sa consigne ne le corrige pas sans tout laisser passer. Le juge distant est cohérent.
3. **Les autres abstentions** (section 3) ont chacune une autre cause.

## 5. Plan proposé (aucun changement de code fait avant validation)

**Étape 1, recherche — entrée de lexique générale sur la forme de la question**, mesurée avec `compare_retrieval.py --repeat 3` sur v0 et v1, gardée seulement sans recul du hit@5 (article et paragraphe) sur aucun des deux jeux :

- entrée étroite : `ai-je le droit | a-t-on le droit | avons-nous le droit | est-ce (permis|autorisé|interdit|légal)` → « pratique interdite ou autorisée ». Elle ne nomme ni les émotions ni une conclusion ; dans v0 et v1, seule q24 la déclenche (attendu : q24 au rang 3, v1 de 16 à 17/17 au niveau article) ;
- variante large, mesurée aussi : + `puis-je utiliser | peut-on utiliser | pouvons-nous utiliser` ; elle touche q09 (« Puis-je utiliser une IA pour trier des CV ? »), où l'art. 5 pourrait chasser l'art. 26 ; gardée seulement si q09 ne recule pas.

Puis q24 rejouée de bout en bout (chaîne complète) en local et en mode distant, pour confirmer : réponse attendue en distant ; abstention attendue en local tant que le juge n'a pas changé.

**Étape 2, juge local — séparée, à décider après l'étape 1.** Candidat : un juge **par extrait** (une question courte par extrait vérifié, OUI dès qu'un extrait répond), qui enlève l'effet de mélange. Coût : environ 2 s par extrait en local. À calibrer d'abord sur les 32 réponses relues de la séance 6 (`answers_v4.md`, `answers_heldout_v4.md`, extraits enregistrés, verdicts connus) : il faut garder 0 abstention sur les réponses justes et conserver les arrêts utiles (q15, q18, h05). Si cette calibration recule, le juge reste tel quel et la limite est documentée : en local, q24 restera une abstention « sans danger ».

**Hors plan** : pas de retour à l'entrée « pratiques interdites » liée aux émotions (elle contient la réponse) ; pas de changement du découpage (hypothèse réfutée) ; `questions_v2.jsonl` et les questions de l'auteur ne sont ni lues ni utilisées.

## 6. Étape 1 : entrée de lexique sur la forme de la question — **mesurée, non retenue**

Deux entrées candidates, ajoutées au lexique en mémoire seulement (aucun code changé pendant la mesure), `compare_retrieval.py --repeat 3`, 16/11/2026, sur secteur, 3 mesures identiques à chaque fois. Les deux ajoutent « pratique interdite ou autorisée » ; elles ne nomment ni les émotions ni une conclusion.

| Entrée (motif, accents ignorés) | v0 hit@1 / hit@5 | v1 hit@1 / hit@5 article | v1 hit@5 paragraphe | q24 (article, § f-h) | q09 |
|---|---|---|---|---|---|
| référence (`main`, sans entrée) | 7/10, 10/10 | 13/17, 16/17 | 15/17 | 11 (§ 11) | 3 |
| **étroite** : `ai-je le droit \| a-t-on le droit \| avons-nous le droit \| est-(ce\|il) (permis\|autorisé\|interdit\|légal)` | 7/10, **10/10** | **14/17, 17/17** | **16/17** | **1 (§ 2)** | 3 |
| large : étroite + `(puis-je \| peut-on \| pouvons-nous \| peut-il/elle) utiliser` | 7/10, **9/10** | 14/17, 17/17 | 16/17 | 1 (§ 2) | **7** |

- **Entrée étroite** (gardée un temps, puis retirée : voir 6.1) : aucun recul de la recherche, trois mesures montent. Dans v0 et v1, seule q24 la déclenche : aucune autre ligne du tableau des rangs ne change. q24 : l'art. 5, § 1, a-e passe au rang 1 et le morceau f-h (points f à h, celui qui répond) au rang 2 ; les deux entrent dans les passages (limite de 2 par article).
- **Entrée large rejetée** par la règle de décision : « Puis-je utiliser une IA pour trier des CV ? » (q09) recule du rang 3 au rang 7, et v0 passe de 10 à 9/10 ; « interdite » fait entrer l'art. 5 et sortir l'art. 26 (obligations des déployeurs). La forme « puis-je » est trop générale : elle sert aussi à « combien de temps puis-je garder… » (q03).
- Rappel de méthode (section 0) : cette entrée a été choisie en regardant q24, une question v1. Le 17/17 sur v1 est donc optimiste ; seule `questions_v2.jsonl` (+ questions de l'auteur) dira ce que vaut l'entrée sur des questions jamais vues.

Code pendant la mesure : une ligne dans `src/compliance_copilot/lexicon.py` (commit `da3cd10`), retirée ensuite (section 6.1) ; `tests/test_lexical.py` vérifie désormais que « ai-je le droit » ne déclenche aucune entrée.

### 6.1 q24 rejouée de bout en bout avec l'entrée (recherche réelle, génération, juge), 2 essais par modèle

Passages trouvés (identiques aux 4 essais) : [1] art. 5, § 1, a-e · [2] art. 5, § 1, f-h · [3] art. 50, § 3 · [4] annexe III, point 6 · [5] art. 3, définition 39.

| Modèle | Extraits vérifiés | Extrait de l'art. 5, § 1, f) | Juge | Réponse affichée | Alertes du code |
|---|---|---|---|---|---|
| distant `qwen/qwen3.8-27b` (2/2 identiques) | 4/4 | oui, cité [2] | OUI | « Non, vous n'avez pas le droit…, car l'AI Act interdit « … inférer les émotions d'une personne physique sur le lieu de travail… » [2]. Cette interdiction comporte une exception : … « sauf lorsque … pour des raisons médicales ou de sécurité » [2]. … » | 1 (une « » de l'art. 50 hors des extraits vérifiés) |
| local `qwen3:4b-instruct` (2/2 de même sens) | 1/2 (l'extrait cité [1] n'y est pas retrouvé mot pour mot ; seul celui de l'art. 50, § 3 est vérifié) | non | OUI | **« Oui, vous pouvez utiliser une IA qui analyse les émotions de vos salariés, à condition que l'utilisation ne soit pas destinée à des fins de surveillance ou de contrôle au travail, sauf pour des raisons médicales ou de sécurité… »** | 3 (extrait introuvable, citation [1] sans extrait vérifié, exception qui ne reprend pas les extraits) |

**Lecture, pas un verdict** (relecture de l'auteur à venir) :

- En **mode distant**, l'étape 1 règle q24 : réponse fidèle, condition et exception recopiées entre « », les deux fois.
- En **mode local**, l'étape 1 remplace une abstention « sans danger » par une réponse **inversée**, donc « dangereux » selon la grille (on juge la réponse affichée, pas les alertes). Le modèle local a le bon passage sous les yeux ([2]), ne le recopie pas correctement (extrait attribué à [1], non vérifié) et conclut « Oui, vous pouvez ». C'est l'erreur de rédaction déjà vue à la séance 6 sur cette question (« pour des raisons autres que médicales »), quand l'ancienne entrée de lexique trouvait l'art. 5. Les trois alertes du code la signalent, comme prévu, mais ne la corrigent pas.
- Le juge local dit OUI les deux fois, parce que les extraits vérifiés changent (art. 50, § 3 seul) : nouvelle illustration de son instabilité (section 2.3).

**Décision de l'auteur (16/11/2026), révisée le même jour : l'entrée est RETIRÉE. Statut : « mesurée, non retenue ».** Raisons :

1. en mode local, qui est le mode par défaut, elle transforme une abstention sans danger en réponse inversée (« Oui, vous pouvez… »), donc dangereuse selon `eval/rubric.md` ; le critère principal du projet est zéro réponse dangereuse ;
2. le gain mesuré vient d'une seule question (q24) : aucune autre question de v0 ou v1 ne déclenche l'entrée, donc rien ne prouve qu'elle aide en général ;
3. elle risque d'envoyer vers l'art. 5 de l'AI Act des questions RGPD de forme « ai-je le droit de… », et aucune question de test ne permet de le contrôler.

Règle de décision complétée par l'auteur : aucun recul du hit@5 sur v0 ni v1, **et aucune réponse dangereuse créée en mode local**. Le diagnostic (sections 1 à 4) et les mesures (section 6) restent tels quels.

Les termes du choix initial étaient : garder l'entrée (recherche meilleure sur v0 et v1, q24 juste en mode distant, le modèle retenu de la séance 7 ; en local, réponse fausse mais signalée) ou la retirer (abstention locale sans danger, art. 5 absent en distant aussi). L'étape 2 (juge local) ne changerait rien ici : le problème local est la rédaction, pas le juge. Une piste générale pour la suite, non mesurée : quand un extrait n'est pas retrouvé dans le passage cité mais l'est mot pour mot dans un autre passage du même article, le réattribuer avec une alerte, au lieu de l'ignorer.

## 7. Étape 2 : reranker (cross-encoder) sur les 20 candidats

Accord de l'auteur (option A) : `torch` 2.15.0 (version CPU) et `transformers` 5.23.0 installés **dans le `.venv` seulement**, `requirements.txt` inchangé ; modèle officiel `BAAI/bge-reranker-v2-m3` (Apache-2.0, 568 millions de paramètres, 2,27 Go dans le cache Hugging Face, hors dépôt). Espace libre vérifié avant : 40,6 Go.

**Principe** : la recherche actuelle (vecteurs `bge-m3` + lexique) donne ses 20 meilleurs candidats ; le reranker lit chaque paire (question avec son lexique, passage) en entier, jusqu'à 512 tokens, et note sa pertinence ; les candidats sont reclassés par cette note, **puis** viennent la limite de 2 par article et le 1er paragraphe, comme aujourd'hui. Le score affiché reste la similarité cosinus. Réglage `SEARCH_RERANK=off` par défaut ; le code (`src/compliance_copilot/rerank.py`) n'importe `torch` que s'il est activé, et un test vérifie que le copilote tourne sans `torch`.

### 7.1 Premier essai : temps ajouté par question (3 questions de v0)

16/11/2026 au soir, 6 fils CPU, modèle déjà chargé. Secteur vérifié dans la journée, pas au moment même de l'essai (voir 7.5).

| Question | Recherche sans reranker | Avec reranker (20 candidats) | Temps ajouté |
|---|---|---|---|
| q01 | 2,7 s | 29,1 s | 26,4 s |
| q04 | 2,2 s | 29,0 s | 26,8 s |
| q10 | 2,3 s | 28,6 s | 26,4 s |

Chargement du modèle : 14 s une fois par lancement (155 s au premier, téléchargement compris). **Environ 26,5 s ajoutées par question, sous le seuil de 30 s fixé par l'auteur** : la mesure a continué. Pour mémoire, une question locale coûte aujourd'hui 39 s médian (recherche, génération, juge) : le reranker la porterait vers 65 s.

### 7.2 Recherche : `compare_retrieval.py --rerank --repeat 3` (3 mesures identiques)

| Configuration | v0 hit@1 | v0 hit@5 | v1 hit@1 (art.) | v1 hit@5 (art.) | v1 hit@5 (§) |
|---|---|---|---|---|---|
| actuelle (lexique + 2 par article + 1er §) | 7/10 | 10/10 | 13/17 | 16/17 | 15/17 |
| **+ reranker (20 → 5)** | **10/10** | 10/10 | **14/17** | **17/17** | **16/17** |

Rangs qui changent (article, puis paragraphe précisé) : q03 5 → **1** ; q09 3 → **1** ; q10 5 → **1** ; q12 2 → **1** ; q24 11 → **2** (§ 2) ; q25 2 → **1** ; q18 § 2 → § **1** ; q13 1 → 2 et q15 § 1 → § 3 (reculs de rang, toujours dans les 5 passages) ; q27 inchangée (§ 4 et § 6 hors des 20 premiers). **Aucun recul du hit@5 sur v0 ni v1 : la première partie de la règle est remplie.** Contrairement à l'entrée de lexique (section 6), le gain ne vient pas d'une seule question : 7 questions montent, dont 6 hors q24.

### 7.3 Ce que le hit@5 ne voit pas : les 5 passages changent pour 31 questions sur 32

Seule q01 garde exactement les mêmes passages. Points à surveiller dans les réponses (lecture de Claude, pas un verdict) :

- **Mieux, en apparence** : q18 reçoit l'art. 9, § 2 (les exceptions, dont le consentement et les associations), absent avant ; q10 a l'art. 4 en 1re position ; q03 a l'art. 5 en 1re position ; q24 reçoit l'art. 5, § 1, f-h, en 2e position, mais toujours derrière l'art. 50, § 3 (le mélange que le juge local rejette, section 2.3).
- **Risques** : q09 (« Puis-je utiliser une IA pour trier des CV ? ») reçoit l'art. 5, § 1, f-h (pratiques interdites) en 2e position et perd l'art. 26 et l'art. 14 : risque d'une réponse « c'est interdit ». q08 (chatbot) perd l'art. 50, § 2 et reçoit l'art. 5, § 1, f-h et l'annexe III. q16 (hébergeur aux États-Unis) perd l'art. 44. q07 garde l'art. 35, § 1 et § 3 mais reçoit l'art. 64 et deux paragraphes de l'art. 26 de l'AI Act.
- **Hors sujet** (h01 à h05) : passages différents, toujours sans rapport ; à vérifier que les refus tiennent.

D'où l'étape suivante, demandée par l'auteur : les réponses locales régénérées pour ces questions, à relire selon `eval/rubric.md`, pour la seconde partie de la règle (aucune réponse dangereuse créée en local).

### 7.4 Réponses locales avec le reranker, à relire par l'auteur

Comme 31 questions sur 32 changent de passages, les 32 ont été régénérées le 17/11/2026, sans retouche, avec la configuration v4 + `SEARCH_RERANK=on` (même modèle `qwen3:4b-instruct`, même prompt, même juge) : **`eval/answers_v4_rerank.md`** (v0 + 2 hors sujet) et **`eval/answers_heldout_v4_rerank.md`** (v1). L'en-tête de chaque fichier nomme le reranker. Comparaison avec les fichiers v4 relus (`compare_answers.py`) :

| | v4 | v4 + reranker |
|---|---|---|
| Réponses données (v0 / v1) | 10/10 · 15/17 | 10/10 · 15/17 |
| Abstentions (v1) | 2 (q22, q24) | 2 (q18, q22) |
| Hors sujet refusés | 5/5 | 5/5 |
| Extraits vérifiés / recopiés | 76/83 | 89/97 |
| Réponses avec alerte | 14/32 | 14/32 |
| Réponses coupées | 0 | 1 (q04) |
| Mots par réponse (médiane, v0 · v1) | 125 · 118 | 90 · 162 |

**Lecture rapide de Claude, pas un verdict** (les verdicts viendront de la relecture de l'auteur, dans `eval/reviews/v4_rerank.jsonl` et `heldout_v4_rerank.jsonl`) ; « v4 » rappelle le verdict déjà donné sans reranker :

- **q24** (v4 : faux, abstention) : en local, « Non, vous n'avez pas le droit…, sauf si … pour des raisons médicales ou de sécurité [2] », 5 extraits vérifiés sur 5, juge OUI, aucune alerte. Ajoute que la reconnaissance des émotions figure à l'annexe III (vrai hors travail et enseignement) et mêle une exception de l'art. 50, § 3. En mode distant : juste les deux fois, 5/5 extraits vérifiés, aucune alerte.
- **q18** (v4 : dangereux, « Non, interdit » sans les exceptions) : devient une **abstention** du juge, alors que l'art. 9, § 2 est maintenant dans les passages : sans danger, mais « faux » selon la grille.
- **q09** (v4 : à voir dans `reviews/v4.jsonl`) : le risque d'un « c'est interdit » ne se réalise pas : « Oui : vous pouvez…, annexe III … haut risque », mais sans les obligations de l'art. 26 (perdu des passages).
- **q10** : art. 4 cité en premier ; ajoute l'information des travailleurs (art. 26, § 7, pour les systèmes à haut risque) et **généralise l'obligation de l'art. 50, § 4** (« Si le système génère ou manipule des contenus…, vous devez indiquer… ») au-delà des hypertrucages et des textes publiés pour informer le public.
- **q14** (v4 : dangereux) : « à condition que ce traitement soit fondé sur une finalité licite, comme la communication d'informations pertinentes » : condition qui n'est pas dans les extraits.
- **q26** (v4 : dangereux) : toujours la condition d'hypertrucage mal rattachée ; 3 alertes.
- **q04** : coupée par la limite de 2 000 tokens (liste de l'art. 13 incomplète) : « partiel » selon la grille. **q19** : réponse réduite à la première phrase de la définition (16 mots au lieu de 71).
- **q03, q12, q13, q15, q16** : l'article attendu est cité en premier ; q16 cite aussi l'art. 49.
- Hors sujet h01 à h05 : refusés.

### 7.5 Temps : non fiables ce soir (ordinateur passé sur batterie)

Pendant la régénération, la génération est tombée à **17 à 20 tokens/s** (contre 35 pour les fichiers v4), et le temps total médian à 86-89 s par question. Test A/B dans un même processus, même question, mêmes passages : **19 tokens/s sans `torch` importé**, 19 tokens/s avec le reranker chargé, 20 tokens/s après l'avoir libéré. Le reranker ne ralentit donc pas la génération. Cause trouvée à la fin : l'ordinateur était **sur batterie** (`BatteryStatus` = 1, carte graphique en état P8 à 300 MHz), alors qu'il était sur secteur au lancement. Le reranker lui-même a pris 70 s pour 20 passages dans cet état, contre 26 s la veille.

**Le contenu des réponses n'en dépend pas** (mêmes passages, température 0,1). **Les temps des deux fichiers `*_rerank.md` ne sont pas représentatifs** : à remesurer sur secteur (essai des 3 questions de 7.1 et une question complète) avant la décision.

### 7.6 Décision : en attente de la relecture de l'auteur

- Première partie de la règle (recherche) : **remplie**.
- Seconde partie (aucune réponse dangereuse créée en local) : **à juger par l'auteur** sur les deux fichiers ci-dessus.
- Coût : environ 26 s de plus par question sur secteur (à confirmer), 2,3 Go de modèle et environ 1 Go de bibliothèques.
- Si retenu : dépendance optionnelle `pip install -e .[rerank]` dans `pyproject.toml`, versions épinglées, README. Sinon : désinstallation de `torch` et `transformers`, et statut « mesuré, non retenu » ici. Dans les deux cas, `SEARCH_RERANK=off` reste la valeur par défaut jusqu'à la décision.
