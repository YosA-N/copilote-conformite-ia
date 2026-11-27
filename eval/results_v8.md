# Résultats v8 : réponses locales coupées (27/11/2026)

Branche `fix/truncated-answers`, partie de `eval/exam-2`, puis mise à jour avec `main` après la fusion de l'examen 2 (PR #18). Question posée après l'examen 2 : pourquoi des réponses du mode local s'arrêtent-elles au milieu d'une phrase ? À l'examen 2, e17 (passe 3) a été relue « partiel » pour cette raison, et e01 (passes 1 et 2) était coupée aussi, mais remplacée par une abstention du juge (`eval/results_v7.md`, section 7).

Mesures faites sur secteur (`BatteryStatus` = 2, vérifié avant et après chaque étape), avec Ollama 0.40.18 et la configuration locale de l'examen 2 (`exam2-config` : sans reformulation ni reranker, `LLM_MAX_TOKENS=2000`).

## 1. Comptage dans tous les fichiers de réponses

Les 35 fichiers `eval/answers_*.md` contiennent 561 réponses. **7 sont coupées** (`done_reason = "length"`, alerte « Réponse coupée »), **toutes du modèle local `qwen3:4b-instruct`** : 7 sur 288 réponses locales, contre 0 sur 261 réponses distantes (`qwen/qwen3.8-27b` et `openai/gpt-oss-120b`).

| Fichier | Question | Limite | Extraits (mots) | Part des extraits dans le texte écrit | Affiché |
|---|---|---|---|---|---|
| `answers_v3.md` | q04 | 1 500 | 4 extraits, 869 mots | 94 % | réponse coupée |
| `answers_heldout_v3.md` | q14 | 1 500 | 6 extraits, 786 mots | 83 % | réponse coupée |
| `answers_heldout_v3.md` | q23 | 1 500 | 8 extraits, 729 mots | 81 % | réponse coupée |
| `answers_v4_rerank.md` | q04 | 2 000 | 5 extraits, 1 182 mots | 96 % | réponse coupée |
| `answers_exam2_local_1.md` | e01 | 2 000 | 5 extraits, 795 mots | 69 % | abstention |
| `answers_exam2_local_2.md` | e01 | 2 000 | 5 extraits, 795 mots | 69 % | abstention |
| `answers_exam2_local_3.md` | e17 | 2 000 | 3 extraits, 1 182 mots | 97 % | réponse coupée |

Le problème est rare (environ 2 % des réponses locales), mais il revient sur les mêmes sujets : les articles à longue liste (RGPD, art. 13 et 14 pour q04 ; AI Act, art. 5 pour q23 et e17, art. 14 pour e17, art. 5 et 50 pour e01).

## 2. Cause

**Le modèle local recopie des paragraphes ou des listes entières comme un seul extrait**, alors que le prompt demande « une seule phrase ou un seul point a), b)…, jamais un paragraphe entier ». Le code ne limite pas la phase « EXTRAITS » : la réponse reçoit ce qui reste des 2 000 tokens.

Preuves :
- **Longueur des extraits** (réponses locales avec une limite de 2 000) : sur 683 extraits locaux, 86 dépassent 120 mots, et **57 de ces 86 sont des listes a), b)… recopiées d'un bloc**. L'extrait le plus long fait 552 mots (art. 14 de l'AI Act en entier, e17).
- **Les réponses elles-mêmes ont une longueur normale** (228 réponses locales complètes, partage extraits/réponse estimé au prorata des caractères) : réponse médiane 225 tokens, 99e centile 481, maximum 712. Extraits : médiane 275 tokens, 95e centile 956, maximum 1 641.
- **Rejeu de e17, 3 fois** (mêmes 5 passages qu'à l'examen) : coupée 2 fois, avec environ 1 923 tokens d'extraits (3 extraits : art. 5, § 1, a) à e), 497 mots ; annexe III, point 4, 133 mots ; art. 14 en entier, 552 mots) et 77 tokens de réponse. Le 3e essai n'est pas coupé : l'extrait de l'art. 14 y fait 295 mots, et la réponse a 337 tokens. **Avec une limite de 3 800 tokens, la réponse s'arrête d'elle-même à 358 tokens** : rien ne s'emballe dans la réponse.
- **Rejeu de e01, 3 fois** : pas coupée (extraits de 837 à 1 383 tokens, réponse de 460 à 576 tokens). Avec 3 800 tokens : 1 574 tokens d'extraits et 711 de réponse, soit 2 286 au total. **e01 cumule des extraits longs et une réponse longue.**
- **Même question, mêmes passages, longueur très variable** : selon l'essai, le modèle recopie l'art. 14 en entier ou à moitié, d'où une réponse coupée ou non.

Cause probable de la recopie des listes : un **conflit entre deux règles du prompt**. La règle 7 demande de recopier chaque cas d'une liste comme un extrait et de les reprendre tous, alors que le prompt limite à six extraits. Pour l'art. 5 de l'AI Act (7 cas de a) à e)), le modèle ne peut pas suivre les deux règles et regroupe la liste en un seul extrait.

**Autre effet des paragraphes recopiés en entier (e17)** : les passes 1 et 2 de l'examen, non coupées, ont été relues « dangereux ». Le modèle applique au tri de CV la vérification par deux personnes de l'art. 14, § 5, qui ne vise que l'identification biométrique (annexe III, point 1 a). Les 2 réponses complètes du rejeu ont la même erreur. **La passe 3 n'était « partielle » que parce qu'elle s'arrêtait avant cette partie.**

## 3. Correction retenue (décision de l'auteur, 27/11/2026)

Options présentées à l'auteur, avec leurs risques :
- **A. Réserve pour la réponse** (code). Si le modèle n'a pas encore écrit « RÉPONSE : » après `LLM_MAX_TOKENS − 800` tokens, soit 1 200, le code arrête la génération (il ferme la connexion, et Ollama s'arrête). Il garde les extraits complets et coupe le dernier après sa dernière phrase ou son dernier point complet, en marquant la coupe par « … ». Il relance ensuite le modèle avec le même prompt et, comme début de réponse du modèle (**prefill**, pré-remplissage), le texte déjà écrit suivi de « RÉPONSE : ». Le modèle continue alors avec les tokens restants.
  - Le total reste dans `LLM_MAX_TOKENS` : le temps maximal ne change pas.
  - La garde ne se déclenche que si la recopie déborde : les autres réponses suivent exactement le même chemin qu'avant.
  - La réserve de 800 tokens couvre la plus longue réponse complète mesurée (712 tokens).
- **B. Marque de coupure visible**. Une réponse encore coupée se termine par « […] (réponse coupée : la limite de longueur a été atteinte) », sans rien retirer : retirer la phrase inachevée de e17 aurait effacé « haut risque », le point essentiel. L'alerte « Réponse coupée » reste.
- **Écartées** :
  - **Augmenter `LLM_MAX_TOKENS`** : `fit_passages` retirerait des passages, car son budget vaut `LLM_NUM_CTX − LLM_MAX_TOKENS − 200`, et chaque réponse serait plus lente.
  - **Extraits courts** (40 mots au plus, `eval/prompts/short_extracts.txt`) : déjà rejetés (`results_v2.md`, section 8).
  - **Réécrire la règle 7 du prompt** : c'est la vraie racine, mais toutes les réponses changeraient, ce qui demanderait une relecture complète. À faire plus tard, dans une PR à part, si l'auteur le souhaite.

**Prototype hors dépôt, avant la décision** (3 essais par question) : e17 complète 3 fois sur 3 (210 à 232 mots). e01 : garde déclenchée 2 fois sur 3, mais encore coupée 1 fois, car la réponse longue épuise la réserve ; d'où B. Ollama accepte le pré-remplissage : le modèle reprend sur « RÉPONSE : » sans réécrire d'extraits. Mais il relit tout le prompt au second appel (environ 5 450 tokens, 15 s), sans réutiliser son cache.

**Risque annoncé avant la décision** : compléter e17 rend visible l'erreur de rédaction de l'art. 14, § 5 (section 2). La garde ne crée pas cette erreur, mais une passe « partielle » parce que coupée peut devenir « dangereuse ».

**Décision de l'auteur : A et B.**

## 4. Mise en œuvre

- `llm.py` :
  - `generate()` accepte `should_stop` (vérifié après chaque morceau diffusé ; Ollama diffuse environ un token par morceau) et `max_tokens`, qui remplace la limite pour un seul appel.
  - `Generation.stopped` indique un arrêt par l'appelant.
  - Le backend distant ne diffuse pas sa réponse : il ignore `should_stop`. Aucune réponse distante n'a été coupée.
- `rag.py` :
  - `ANSWER_RESERVE_TOKENS = 800`, `extracts_overrun()`, `complete_extracts()`, `continued_generation()`, `CUT_MARK` ;
  - dans `answer_from_passages`, l'affichage au fil de l'écriture repart de zéro après l'arrêt : rien n'était affiché, puisque les extraits sont retenus jusqu'à leur vérification ;
  - nouvelle alerte « Extraits trop longs : le code a arrêté leur recopie après 1200 tokens… » ;
  - `RagAnswer.extracts_cut` ;
  - la marque de coupure est ajoutée après les contrôles du texte, pour qu'elle ne soit pas lue comme une phrase de la réponse.
- Après un arrêt, « tokens lus » compte la lecture du second appel (prompt + extraits), et « écrits » additionne les deux appels. La partie retirée du dernier extrait n'apparaît pas dans le texte brut.
- `answer_questions.py` : l'en-tête des fichiers de réponses indique la réserve.
- Tests hors ligne : voir la section 5.

## 5. Tests

18 tests hors ligne de plus (243 au total, tous verts) :
- `tests/test_llm.py` :
  - Ollama s'arrête quand `should_stop` le demande : texte et nombre de morceaux, connexion fermée ;
  - `max_tokens` d'un appel est envoyé comme `num_predict` ;
  - un message final de l'assistant (pré-remplissage) est envoyé tel quel ;
  - l'API distante ignore `should_stop` mais prend `max_tokens`.
- `tests/test_rag.py` :
  - dernier extrait coupé après son dernier point complet, jamais sur un numéro de paragraphe (« 3. ») ;
  - extrait trop court retiré, en-tête commencé (« RÉPO ») retiré ;
  - arrêt seulement si la réponse n'a pas commencé ;
  - second appel avec le même prompt, le texte pré-rempli et les tokens restants ;
  - affichage au fil de l'écriture limité à la réponse ;
  - un seul appel quand la réponse commence à temps, ou quand le modèle ne diffuse pas sa réponse (cas du mode distant) ;
  - pas de garde quand la limite ne dépasse pas la réserve ;
  - marque de coupure, avec ou sans affichage au fil de l'écriture et après un arrêt ;
  - pas de marque sur un refus ni sur une abstention ;
  - la marque n'est pas lue comme une phrase de la réponse par le contrôle des phrases sans [n].
- Le faux modèle des tests (`FakeChatModel`) compte un morceau de 3 caractères comme un token et accepte `should_stop`, `max_tokens` et une suite de réponses.

## 6. Mesures (27/11/2026)

### 6.1 Recherche

`compare_retrieval.py --configs current --repeat 3`, avec les jeux de réglage par défaut. Le code de recherche n'a pas changé ; la mesure vérifie la règle de décision.

| Niveau article | v0 hit@5 | v1 hit@5 | v2 hit@5 | auteur hit@5 | total hit@5 | total hit@1 |
|---|---|---|---|---|---|---|
| actuelle, 3 mesures identiques | 10/10 | 16/17 | 10/17 | 0/5 | 36/49 | 28/49 |

Au niveau paragraphe : 35/49. Ce sont les mêmes chiffres que la configuration actuelle de `results_v7.md`, section 3 bis : **aucun recul sur v0 ni v1**.

### 6.2 Une passe locale sur toutes les questions

86 questions (v0 et hors sujet, v1, v2, auteur, examen 2), de 19:20 à 20:26, sur secteur à chaque étape. Fichiers bruts, sans retouche :
- `answers_v8_local.md` (v0 et hors sujet) ;
- `answers_v8_local_v1.md`, `answers_v8_local_v2.md`, `answers_v8_local_author.md` ;
- `answers_v8_local_exam2.md`.

| Jeu | Questions | Garde déclenchée | Réponses coupées | Temps total médian | Max | Au-delà de 60 s |
|---|---|---|---|---|---|---|
| v0 et hors sujet | 12 | 1 (q04) | 0 | 40 s | 92 s | 2 |
| v1 | 20 | 1 (q23) | 0 | 38 s | 112 s | 3 |
| v2 | 20 | 0 | 0 | 38 s | 64 s | 1 |
| auteur | 6 | 0 | 0 | 52 s | 62 s | 1 |
| examen 2 | 28 | 2 (e01, e17) | 0 | 43 s | 107 s | 4 |
| **Total** | **86** | **4** | **0** | | | |

Pour comparer, les 3 passes locales de l'examen 2, avec la même configuration sans la garde : **1 réponse coupée par passe** (e01, e01, e17), temps médian de 43 à 44 s, maximum de 75 à 196 s.

### 6.3 Trois passes sur les questions concernées

Six questions : celles où la garde s'est déclenchée en 6.2 (q04, q23, e01, e17), plus q14 et a03, qui l'auraient déclenchée d'après l'historique (section 1 et estimation au prorata des caractères). Passes 2 et 3 : `answers_v8_local_reserve_2.md` et `_3.md` (`--ids q04,q14,q23,a03,e01,e17`). **L'ordinateur est passé sur batterie pendant la passe 3, à partir de q23** (`BatteryStatus` = 1 à 20:44 ; 14 à 23 tokens/s au lieu de 30 à 32) : les temps de q23, a03, e01 et e17 de la passe 3 sont faussés. Le contenu des réponses ne dépend pas de la vitesse.

| Question | Garde (3 passes) | Coupées | Extraits vérifiés | Affiché | Temps total (passes 1, 2, 3) | Avant la garde |
|---|---|---|---|---|---|---|
| q04 | 3/3 | 0 | 2/3 à chaque passe | réponse ×3 | 92, 99, 71 s | v4 : 89 s |
| q14 | 0/3 | 0 | 5/5, 4/4, 5/5 | réponse ×3 | 46, 38, 29 s | heldout_v4 : 39 s |
| q23 | 3/3 | 0 | 7/7 à chaque passe | réponse ×3 | 112, 102, (100) s | heldout_v4 : 88 s |
| a03 | 0/3 | 0 | 5/5 | abstention ×3 | 62, 53, (101) s | — |
| e01 | 3/3 | 0 | 4/5 à chaque passe | abstention ×3 | 107, 105, (139) s | examen 2 : 196, 75, 63 s (coupée 2 fois) |
| e17 | 3/3 | 0 | 2/3 à chaque passe | réponse ×3 | 106, 75, (139) s | examen 2 : 98, 69, 83 s (coupée 1 fois) |

Entre parenthèses : temps faussés par la batterie.

**Bilan : 0 réponse coupée sur 98 générations locales** (86 + 12), contre 3 sur 84 aux passes locales de l'examen 2. La garde s'est déclenchée 12 fois. Elle ne se déclenche que sur des questions à longue liste, et presque toujours les mêmes (q04, q23, e01, e17). Quand elle se déclenche, la réponse prend de 71 à 112 s sur secteur, contre 63 à 98 s avant pour les mêmes questions (196 s pour e01 à une passe de l'examen) : le second appel relit tout le prompt avec les extraits (environ 4 500 à 5 450 tokens, environ 15 s). Les réponses où la garde ne se déclenche pas (82 sur 86 en 6.2) suivent exactement le même chemin qu'avant, et leur temps médian n'a pas changé.

### 6.4 Lecture rapide de Claude (pas un verdict)

- **e17** : complète aux 3 passes. **Les 3 réponses appliquent au tri de CV la vérification par deux personnes de l'art. 14, § 5**, réservée à l'identification biométrique (annexe III, point 1 a). C'est l'erreur relue « dangereuse » aux passes 1 et 2 de l'examen. Les 3 réponses présentent aussi l'art. 5 (notation sociale, point c) comme interdisant le tri sur des traits de personnalité. À la passe 1, le dernier extrait (art. 14) est coupé après le § 2, mais le modèle lit le § 5 dans le passage complet. **Probablement 3 réponses dangereuses sur 3, contre 2 dangereuses et 1 partielle à l'examen 2.** La garde ne crée pas cette erreur de rédaction, mais elle supprime la coupure qui la cachait (risque annoncé avant la décision, section 3).
- **q04** : liste des informations de l'art. 13 du RGPD, complète à première vue.
- **q23** : liste des pratiques interdites de l'art. 5 ; à la passe 1, la liste est partielle sans « parmi d'autres cas », et la phrase finale reste vague (« sauf dans les cas spécifiques autorisés »).
- **e01** : abstention du juge aux 3 passes, comme à l'examen 2 (les art. 6 et 13 du RGPD manquent dans les passages).

## 7. Relecture de l'auteur (27/11/2026)

Les six questions de la section 6.3, à chacune des 3 passes :
- `answers_v8_local_reserve_1.md` : les réponses de la passe 1, recopiées telles quelles depuis `answers_v8_local*.md`, sans rien régénérer, avec le même en-tête que les passes 2 et 3 ;
- `answers_v8_local_reserve_2.md` et `_3.md`.

Verdicts de l'auteur, mot pour mot, dans `eval/reviews/v8_local_reserve_1.jsonl`, `_2.jsonl` et `_3.jsonl` (`review_summary.py --check` : cohérent).

| Question | Garde | Passe 1 | Passe 2 | Passe 3 | Examen 2, sans la garde (passes 1, 2, 3) |
|---|---|---|---|---|---|
| q04 | 3/3 | juste | juste | juste | — |
| q14 | 0/3 | **dangereux** | partiel | faux | — |
| q23 | 3/3 | partiel | partiel | partiel | — |
| a03 | 0/3 | faux (abstention) | faux (abstention) | faux (abstention) | — |
| e01 | 3/3 | faux (abstention) | faux (abstention) | faux (abstention) | faux, faux, faux (abstentions) |
| e17 | 3/3 | **dangereux** | **dangereux** | **dangereux** | dangereux, dangereux, partiel (coupée) |
| **Total (juste / partiel / faux / dangereux)** | | **1 / 1 / 2 / 2** | **1 / 2 / 2 / 1** | **1 / 1 / 3 / 1** | |

Commentaires de l'auteur, en bref :
- **q23** : interdictions citées justes, mais il manque la police prédictive (art. 5, § 1, d) et le moissonnage d'images faciales (e) ;
- **e17** : haut risque juste, mais la vérification par deux personnes de l'art. 14, § 5 est imposée au tri de CV, et l'art. 5, § 1, c est présenté comme interdisant l'évaluation sur des traits de personnalité ;
- **q14**, sans la garde : à la passe 1, l'opposition à la prospection est rattachée à des « raisons tenant à sa situation particulière » (art. 21, § 1), alors qu'elle est possible à tout moment sans justification ;
- **a03 et e01** : abstentions, car l'article attendu manque dans les passages.

**Décision de l'auteur : A et B gardés.**
- **e17** : la garde ne crée pas l'erreur de rédaction, elle arrête de la cacher. La passe 3 de l'examen n'était « partielle » que parce qu'elle était coupée, et cacher une erreur par une coupure n'est pas une sécurité.
- **Les verdicts de l'examen 2 ne changent pas** : ils jugent les réponses affichées à l'époque.
- **q14**, sans la garde, reçoit 3 verdicts différents en 3 passes : cela confirme que le mode local n'est pas fiable.
- **La règle 7 du prompt**, cause racine, n'est pas modifiée : piste notée pour plus tard (section 8).

## 8. Limites et suite

- **La racine reste** : le modèle local recopie toujours des listes entières. La garde l'empêche de couper la réponse, pas de lire, dans le passage, un paragraphe qui ne s'applique pas. **La règle 7 du prompt n'est pas modifiée (décision de l'auteur) : piste notée pour plus tard.** Il s'agirait de résoudre le conflit entre la règle 7 (tous les cas d'une liste) et la limite de six extraits, par exemple en demandant la phrase qui annonce la liste puis seulement les cas qui concernent la question, avec « parmi d'autres cas ». Toutes les réponses changeraient : il faudrait remesurer et relire en entier.
- **Le second appel relit tout le prompt** : Ollama ne réutilise pas son cache après l'arrêt de la génération (environ 15 s).
- **Une réponse longue peut encore être coupée** (e01 dans le prototype) : la marque « […] » le montre alors dans la réponse elle-même.
- **Le mode distant ne change pas** : sa réponse n'est pas diffusée au fil de l'écriture, et aucune réponse distante n'a été coupée (0 sur 261).
