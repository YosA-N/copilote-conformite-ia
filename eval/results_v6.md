# Séance 7 ter — améliorer la recherche avec des méthodes générales

**Contexte** (`eval/results_v5.md`) : à l'examen final, l'article attendu n'était dans les 5 passages que pour 10 questions sur 22. Causes observées : mots de la question différents de ceux de la loi (a01, a04, q34), article juste après le rang 5 (a02, a03, a05, q36, q37), et un faux ami du lexique (« enregistre » déclenchait « registre »).

**Jeu de réglage** : toutes les questions existantes sont désormais connues ; v0, v1, v2 et les questions de l'auteur servent toutes au réglage (49 questions avec article attendu : v0 10, v1 17, v2 17, auteur 5). Un examen 2 sur des questions neuves, écrites par l'auteur hors du dépôt, viendra après cette séance.

**Règle de décision** (auteur) : une configuration n'est retenue que si elle améliore le hit@5 sur l'ensemble des 4 jeux sans recul sur aucun ; puis les réponses des questions dont les passages changent sont régénérées pour la relecture de l'auteur : aucune réponse dangereuse créée. Aucune règle n'est écrite pour une seule question.

**Contrôle des dates : non fait** (décision de l'auteur). Rejoué hors ligne avant la séance : une seule date est écrite dans toutes les réponses enregistrées, celle de q44 en local (« le 2 août 2027 »), et elle figure mot pour mot dans un extrait vérifié (échéance des actes délégués, art. 2, présentée à tort comme date d'application). Un contrôle « date présente dans un extrait vérifié » n'aurait donc retiré aucune phrase, ni arrêté q44.

## 1. Lexique en mots entiers

Une entrée du lexique ne se déclenche plus que sur des **mots entiers** (`WHOLE_WORDS` dans `lexicon.py`) : « enregistre » ne déclenche plus « registre ». Les entrées écrites comme des débuts de mot sont devenues des familles de mots (pluriel, féminin, dérivés) : `publicit(e|es|aire|aires)`, `securi(te|taire|ser|sation…)`, `candidat(e|es|s|ure|ures)?`, `client(e|es|s)?`, `salarie(e|es|s)?`, `emotions?|emotionnel(le|les|s)?`, `medica(l|le|les|ux)`… Sans le féminin, « Une **cliente** conteste… » (q29) aurait perdu son ajout.

**Effet sur les 59 questions des 4 jeux** (comparaison des ajouts avec l'ancien lexique) : **une seule question change, a04**, qui ne reçoit plus « registre des activités de traitement ». Le hit@5 ne bouge pas (a04 reste hors des 20 premiers : section 2). Effet de bord voulu : « amendement » ne déclenche plus « amendes administratives ». Test : `test_lexicon_matches_whole_words_only_and_keeps_word_families`.

## 2. Mesures de la recherche (`compare_retrieval.py --repeat 3`, 4 jeux)

18/11/2026, sur secteur (`BatteryStatus` = 2 avant et après, 13:17 à 15:30). « a–b » : résultat variable d'une mesure à l'autre. Référence avec l'**ancien** lexique (même jour) : identique à la ligne « actuelle » ci-dessous (36/49 au niveau article, 35/49 au niveau paragraphe).

**Niveau article**

| Configuration | v0 hit@5 | v1 hit@5 | v2 hit@5 | auteur hit@5 | **total hit@5** | total hit@1 |
|---|---|---|---|---|---|---|
| a) actuelle (lexique en mots entiers + 2 par article + 1er paragraphe) | 10/10 | 16/17 | 10/17 | 0/5 | **36/49** | 28/49 |
| b) sans lexique | 7/10 | 11/17 | 9/17 | 0/5 | 27/49 | 22/49 |
| c) + reranker (20 → 5) | 10/10 | 17/17 | 12/17 | 1/5 | **40/49** | 31/49 |
| d) + reformulation locale (`qwen3:4b-instruct`) | **8–9/10** | 17/17 | 13–14/17 | 2/5 | 40–41/49 | 28/49 |
| d') + reformulation distante (`qwen/qwen3.8-27b`) | **9/10** | **15–16/17** | 14–15/17 | 2/5 | 40–42/49 | 30–32/49 |
| e) + reformulation locale + reranker | 10/10 | 17/17 | 14/17 | 1–2/5 | **42–43/49** | 33–35/49 |
| e') + reformulation distante + reranker | 10/10 | 17/17 | 15/17 | 0/5 | **42/49** | 38–40/49 |

**Niveau paragraphe**

| Configuration | v0 hit@5 | v1 hit@5 | v2 hit@5 | auteur hit@5 | **total hit@5** | total hit@1 |
|---|---|---|---|---|---|---|
| a) actuelle | 10/10 | 15/17 | 10/17 | 0/5 | **35/49** | 27/49 |
| b) sans lexique | 7/10 | 10/17 | 9/17 | 0/5 | 26/49 | 21/49 |
| c) + reranker | 10/10 | 16/17 | 11/17 | 1/5 | 38/49 | 29/49 |
| d) + reformulation locale | 8–9/10 | 16/17 | 13–14/17 | 2/5 | 39–40/49 | 25/49 |
| d') + reformulation distante | 9/10 | 14–15/17 | 14–15/17 | 2/5 | 39–41/49 | 28–30/49 |
| e) + reformulation locale + reranker | 10/10 | 16/17 | 14/17 | 1–2/5 | **41–42/49** | 31–33/49 |
| e') + reformulation distante + reranker | 10/10 | 16/17 | 15/17 | 0/5 | **41/49** | 35–37/49 |

**Application de la règle** (niveau article, par rapport à a) :

- **b) rejetée** (recul partout) : le lexique reste utile.
- **d) et d') rejetées** : la reformulation seule fait reculer v0 (8–9/10 et 9/10) et, en distant, v1 (15–16/17).
- **c), e) et e') passent** : aucun recul sur aucun jeu, aux deux niveaux. **e) et e') sont les meilleures** (42–43/49 et 42/49, contre 36/49) : c'est la configuration **« reformulation + reranker »**, chacune avec le modèle de son mode, qui est retenue pour la régénération des réponses (section 4).

**Ce que les totaux ne montrent pas** (rangs question par question, tableau complet dans le journal de mesure) :

- **Entrent dans les 5 passages avec e)** : q24 (rang 11 → 1), q29 (20 → 1), q34 (absent → 1–2), q36 (6 → 1–2), q42 (18 → 1–2), q10 (5 → 1), q09 (3 → 1) ; a01 (absent → 3–20 selon la passe).
- **Sortent des 5 passages avec e)** : **q33** (rang 2 → 6–13 ; e') : 6–10) et **q38** (absent avant, mais 15 avec e) contre 1 avec e')). q35 passe du rang 1 au rang 4 (encore dans les 5).
- **Toujours hors des 20 premiers** : **q44** (date d'application, art. 113) et **a04** (compte rendu de réunion, art. 13 et 6), dans toutes les configurations.

## 3. La reformulation : termes produits et stabilité

Termes enregistrés pour les 294 appels (49 questions × 3 passes × 2 modèles) : **aucune réponse vide**, et **aucun terme de conclusion** n'a franchi le filtre (« interdit », « autorisé », « obligatoire », « oui », « non », chiffres, plus de 8 mots). Exemples :

| Question | Reformulation locale | Reformulation distante |
|---|---|---|
| a01 pointeuse à empreinte digitale | données biométriques ; traitements de données personnelles ; consentement explicite ; finalité spécifique ; durée limitée | données biométriques ; traitement de données à caractère personnel ; consentement ; protection des données ; sécurité des données |
| q34 caméras dans l'atelier | enregistrement vidéo ; surveillance ; données personnelles ; traitement ; données d'identification ; activité professionnelle | traitement de données à caractère personnel ; vidéosurveillance ; données relatives à l'identité ; consentement ; information des personnes concernées ; finalité du traitement |
| a05 photos de la fête | données personnelles ; traitement ; image ; représentation ; consentement ; finalité | données à caractère personnel ; consentement ; droit à l'image ; responsable du traitement ; sous-traitant ; finalité |
| q44 date des obligations à haut risque | systèmes d'IA à haut risque ; recrutement ; obligation de transparence ; évaluation des risques ; mise en œuvre ; mise en conformité | systèmes d'IA à haut risque ; recrutement ; obligations ; conformité |

**Limites observées** :

- **Instabilité** : les termes ne sont identiques aux 3 passes que pour 17 questions sur 49 en local et 16 sur 49 en distant (température 0,1) ; d'où les résultats « a–b » des configurations avec reformulation.
- **Termes trop généraux en local** : le petit modèle ajoute souvent « données personnelles », « consentement explicite », « données sensibles » quelle que soit la question (q09, q10, a03), ce qui peut tirer la recherche vers des articles voisins.
- **q44** : aucun des deux modèles ne traduit « à partir de quelle date » par « date d'application » ou « entrée en application » ; l'art. 113 reste introuvable.

## 4. Réponses régénérées avec « reformulation + reranker », pour la relecture de l'auteur

**Passages changés** : 56 questions sur 58 (toutes sauf q01 et q17) reçoivent d'autres passages que la configuration actuelle (comparaison avec la recherche actuelle, même jour). Les 58 questions ont donc été régénérées, en local et en mode distant, sans retouche, avec `SEARCH_REWRITE=on` et `SEARCH_RERANK=on` (chaque mode reformule avec son propre modèle). L'en-tête de chaque fichier le dit ; chaque réponse affiche les termes ajoutés par la reformulation.

### 4.1 Local (`qwen3:4b-instruct`)

`eval/answers_v6_local.md` (v0 + 2 hors sujet), `answers_v6_local_v1.md`, `answers_v6_local_v2.md`, `answers_v6_local_author.md` ; 18/11/2026, 15:32 à 16:48, **sur secteur** du début à la fin (`BatteryStatus` = 2 avant, au milieu et après ; génération à 33 à 34 tokens/s).

Mesures du code (`compare_answers.py`), comparées aux réponses de la configuration actuelle (`answers_v4.md` et `answers_heldout_v4.md` pour v0 et v1, `answers_final_local_v2.md` et `answers_final_local_author.md` pour v2 et l'auteur) :

| Local, 58 questions | Configuration actuelle | Reformulation + reranker |
|---|---|---|
| Réponses données (sur 49) | 36 | 38 |
| Abstentions du juge | 13 | 11 |
| Hors sujet refusés | 9 / 9 | 9 / 9 |
| Extraits vérifiés / recopiés | 143 / 152 | 179 / 188 |
| Réponses avec alerte | 29 / 58 | 28 / 58 |
| Temps total par question : médian · max | 44 s · 248 s (*) | **74 s · 146 s** |
| Questions au-delà de 60 s | 12 | **45** |

(*) Les fichiers de l'examen local ont des temps faussés par la batterie à partir de q34 ; les fichiers v4 datent de la séance 6.

Temps de la nouvelle configuration : reformulation locale **3,3 s médian** (max 10,3 s), recherche avec reranker **28,5 s médian** (max 50,2 s).

**Ce qui change dans les réponses affichées** (lecture des fichiers, pas un verdict ; « présent » = l'article attendu est parmi les 5 passages) :

| Question | Configuration actuelle | Reformulation + reranker |
|---|---|---|
| q24 émotions des salariés | abstention, absent | **réponse, présent** |
| q29 exactitude contestée | abstention, absent | **réponse, présent** |
| q36 plainte à la CNIL | réponse (faux à l'examen), absent | réponse, **présent** |
| q37 réparation après une fuite | abstention, absent | **réponse, présent** |
| q42 explication d'un refus par une IA | abstention, absent | **réponse, présent** |
| q44 date des obligations à haut risque | **réponse dangereuse à l'examen**, absent | abstention, absent |
| a05 photos de la fête | réponse (faux à l'examen), absent | réponse, **présent** |
| q34 caméras | abstention, absent | abstention, **présent** |
| a02 vente du fichier clients | abstention, absent | abstention, **présent** |
| q10 IA générative au travail | réponse, présent | **abstention**, présent |
| q18 santé des bénévoles | réponse, présent | **abstention**, présent |
| q33 fichier de prospects acheté | abstention, présent | abstention, **absent** |
| a03 IA qui note les commerciaux | abstention, absent | **réponse, absent** (à regarder en premier) |
| a04 compte rendu de réunion | réponse (faux à l'examen), absent | réponse, absent (inchangé) |

Le juge local s'abstient toujours avec l'article attendu dans les passages (q10, q18, q34, a02).

### 4.2 Distant (`qwen/qwen3.8-27b`) : 58 réponses sur 58, produites sur deux jours

`eval/answers_v6_remote.md` (v0 + 2 hors sujet), `answers_v6_remote_v1.md`, `answers_v6_remote_v2.md`, `answers_v6_remote_author.md`. **51 réponses le 18/11/2026** (à partir de 16:49 ; arrêt par le quota du jour de Groq, 200 000 tokens sur 24 heures glissantes, puis petits lots, arrêt volontaire à 18:05 avec l'accord de l'auteur) et **7 réponses le 19/11/2026** de 10:46 à 10:50 (h08 avec `--resume`, puis les 6 questions de l'auteur) ; **sur secteur** les deux jours (`BatteryStatus` = 2 avant et après). Le modèle étant en preview, il a pu changer entre les deux jours.

Mesures du code (`compare_answers.py`), comparées aux réponses de la configuration actuelle en mode distant (`answers_v4_big_qwen27b.md` et `answers_heldout_v4_big_qwen27b.md` pour v0 et v1, `answers_final_remote_v2.md` et `answers_final_remote_author.md` pour v2 et l'auteur) :

| Distant, 58 questions | Configuration actuelle | Reformulation + reranker |
|---|---|---|
| Réponses données (sur 49) | 37 | **41** |
| Abstentions du juge | 7 | 7 |
| Refus faute d'extrait vérifié | 5 (q34, q37, q38, q44, a02) | 1 (q38) |
| Hors sujet refusés | 9 / 9 | 9 / 9 |
| Extraits vérifiés / recopiés | 203 / 207 | 213 / 225 |
| Réponses avec alerte | 16 / 58 | 22 / 58 |
| Alertes au total | 17 | 27 |
| Temps total par question : médian · max | 4 s · 38 s | **30 s · 50 s** |
| Questions au-delà de 60 s | 0 | 0 |

En mode distant, le reranker tourne toujours sur l'ordinateur : il fait passer une question de 4 s à environ 30 s. Les alertes en plus viennent surtout de textes entre « » introuvables dans les extraits (4 → 7 réponses) et d'extraits non retrouvés mot pour mot (3 → 5).

**Ce qui change dans les réponses affichées** (lecture des fichiers, pas un verdict ; « présent » = l'article attendu est parmi les 5 passages) :

| Question | Configuration actuelle | Reformulation + reranker |
|---|---|---|
| q24 émotions des salariés | abstention, absent | **réponse, présent** |
| q29 exactitude contestée | abstention, absent | **réponse, présent** |
| q34 caméras | refus (aucun extrait vérifié), absent | **réponse, présent** (3 alertes) |
| q36 plainte à la CNIL | réponse, absent | réponse, **présent** |
| q37 réparation après une fuite | refus, absent | **réponse, présent** |
| q42 explication d'un refus par une IA | abstention, absent | **réponse, présent** |
| q38 casier judiciaire des bénévoles | refus, absent | refus, **présent** (*) |
| q33 fichier de prospects acheté | réponse, présent | **abstention, absent** |
| q44 date des obligations à haut risque | refus, absent | abstention, absent |
| a02 vente du fichier clients | refus, absent | abstention, absent |
| a01, a03, a04, a05 | abstention, absent | abstention, absent (inchangé) |

(*) q38 : l'art. 10 est au passage [1], mais le modèle a recopié ses extraits entre crochets chinois « 「 » et avec une faute (« autoriture ») : aucun extrait n'est vérifié, la réponse est remplacée par un refus. Observé, non corrigé (même famille que les caractères ajoutés par gpt-oss à la séance 7).

**Questions de l'auteur en distant** : l'article attendu manque dans les 5 cas, comme dans les mesures de la section 2 (e') : 0/5) ; le juge s'abstient sur les 5, sans danger. La reformulation distante ajoute des termes généraux (« consentement », « responsable du traitement », « sous-traitant ») qui ne mènent pas aux art. 6 et 9 ; en local, a02 et a05 trouvaient l'article.

## 5. Relecture de l'auteur et décision (19/11/2026)

Relecture par l'auteur des 116 réponses (58 locales, 58 distantes) selon `eval/rubric.md`, **vérifiée à l'aveugle par un second relecteur sur les 24 cas décisifs** ; verdicts enregistrés tels quels dans `eval/reviews/v6_local*.jsonl` et `eval/reviews/v6_remote*.jsonl` (`review_summary.py --check` : 25 relectures cohérentes).

| 58 questions (juste / partiel / faux / dangereux) | Configuration actuelle | Reformulation + reranker |
|---|---|---|
| **Local** (`qwen3:4b-instruct`) | 26 / 7 / 18 / 7 | 30 / 7 / 16 / 5 |
| **Distant** (`qwen/qwen3.8-27b`) | 38 / 6 / 13 / 1 | **40 / 9 / 9 / 0** |

« Configuration actuelle » = relectures déjà faites des mêmes questions : en local `v4`, `heldout_v4`, `final_local_v2`, `final_local_author` ; en distant `v4_big_qwen27b`, `heldout_v4_big_qwen27b`, `final_remote_v2`, `final_remote_author`.

| Jeu | Local actuel | Local reformulation + reranker | Distant actuel | Distant reformulation + reranker |
|---|---|---|---|---|
| v0 + 2 hors sujet (12) | 8 / 2 / 0 / 2 | 8 / 1 / 1 / 2 | 12 / 0 / 0 / 0 | 11 / 1 / 0 / 0 |
| v1 (20) | 9 / 3 / 4 / 4 | 12 / 2 / 5 / 1 | 13 / 5 / 2 / 0 | 14 / 5 / 1 / 0 |
| v2 (20) | 8 / 2 / 9 / 1 | 9 / 4 / 6 / 1 | 12 / 1 / 6 / 1 | 14 / 3 / 3 / 0 |
| auteur (6) | 1 / 0 / 5 / 0 | 1 / 0 / 4 / 1 | 1 / 0 / 5 / 0 | 1 / 0 / 5 / 0 |

**Réponses dangereuses** :

- **Local, 3 créées** : **q09** (tri de CV : le haut risque et les obligations du déployeur ne sont pas dits, et l'obligation de détection des biais est niée), **q29** (« Oui, les données peuvent être utilisées » pendant la vérification de leur exactitude, à l'inverse de l'art. 18, avec une exception inventée), **a03** (interdiction au titre de la notation sociale suggérée, alors que l'évaluation des performances au travail relève du haut risque). Toujours dangereuses : q07 et q26. Ne le sont plus : q01, q14, q16, q18 et q44.
- **Distant, aucune créée** : q39 (pseudonymisation présentée comme une sortie du RGPD à l'examen final) devient juste.

**Application de la règle** : la recherche s'améliore sans recul dans les deux modes (section 2) ; **aucune réponse dangereuse créée en distant**, **3 en local**. Le distant passe la règle, le local non.

**Décision de l'auteur** :

- **Mode distant : reformulation + reranker activés par défaut.** `SEARCH_RERANK=auto` et `SEARCH_REWRITE=auto` (valeurs par défaut) : activés en mode distant, désactivés en mode local, toujours modifiables dans `.env` (`on` ou `off`). Si `torch` n'est pas installé en mode distant : message clair et retour à la configuration validée précédente (sans reformulation ni reranker), **jamais la reformulation seule** (elle fait reculer v0 et v1, section 2).
- **Mode local : désactivés** (3 réponses dangereuses créées, et 74 s médian par question au lieu de 44 s).
- Coût accepté en distant : environ 30 s par question au lieu de 4 s (le reranker tourne sur le processeur), une requête de plus chez Groq (la reformulation, après le garde-fou des données personnelles), environ 2,3 Go de modèle et `pip install -e .[rerank]`.

## 6. Après la décision (19/11/2026)

### 6.1 Valeur « auto » dans le code

- `config.py` : `SEARCH_RERANK` et `SEARCH_REWRITE` acceptent `auto`, `on` ou `off` (`1`, `true`, `oui` / `0`, `false`, `non`), `auto` par défaut ; une autre valeur arrête le programme avec un message clair. Le reranker est utilisé si `on`, ou `auto` en mode distant ; la reformulation si `on`, ou `auto` en mode distant **quand le reranker l'est aussi** (jamais seule par défaut).
- `rerank.resolve_search` décide une seule fois par lancement (`ask.py`, `search.py`, `answer_questions.py`). En mode distant avec `auto`, si `torch` ou `transformers` manque (vérifié sans les importer) : ni reranker ni reformulation, et un message (« … recherche sans reformulation ni reranker (configuration validée avant la séance 7 ter). Pour les activer : pip install -e .[rerank]… »). `SEARCH_RERANK=on` écrit dans `.env` reste un choix explicite : le reranker s'arrête alors sur son erreur claire, sans repli silencieux.
- Tests (`tests/test_rerank.py`) : `auto` en local et en distant, jamais la reformulation seule, repli sans `torch`, choix explicites gardés, lecture de `auto`/`on`/`off` ; le test « le copilote marche sans torch » vérifie aussi le repli du mode distant.
- `answer_questions.py --ids q06,q07` : ne pose que les questions choisies (l'en-tête du fichier le dit).

### 6.2 Crochets 「 」 『 』 dans la vérification mot pour mot

Cause de q38 distant (faux) : le modèle a recopié ses extraits entre crochets 「 」, donc aucun n'a été retrouvé mot pour mot et la réponse a été remplacée par un refus. Ces crochets sont désormais ignorés comme les autres guillemets (des deux côtés, et retirés en début et fin d'extrait). Test avec les vrais extraits de q38 et le vrai texte de l'art. 10 : 2 extraits sur 3 vérifiés ; **l'extrait avec la faute « autoriture » reste rejeté**.

Non-régression rejouée sur tous les `eval/answers_*.md`, sans rien régénérer (texte brut du modèle, passages retrouvés par leur étiquette dans `chunks.jsonl`) : **349 réponses rejouées** (15 non rejouables, format ancien), **2 seulement changent**, les deux seules qui contiennent ces crochets : q17 distant v6 (2/5 → 4/5 extraits vérifiés) et q38 distant v6 (0/3 → 2/3 : la réponse ne serait plus remplacée par un refus). Contrôle du rejeu : l'ancien calcul retrouve les chiffres enregistrés pour 338 réponses sur 349 ; les 11 écarts sont dans des fichiers produits avant des tolérances déjà ajoutées (tirets U+2011 de gpt-oss, séance 7 ; v2 q06, séance 5 bis).

### 6.3 Nouvel exemple du prompt de reformulation

L'exemple « empreinte digitale → données biométriques » correspondait exactement à la question a01. Il est remplacé par **« géolocalisation des véhicules → données de localisation »** (aucune des 59 questions ne parle de géolocalisation ni de véhicule).

Remesure de e') en distant (`compare_retrieval.py --configs current,rw_remote_rerank --repeat 3`), 19/11/2026, 11:12 à 12:03, sur secteur (`BatteryStatus` = 2 avant et après) :

| Niveau article | v0 hit@5 | v1 hit@5 | v2 hit@5 | auteur hit@5 | **total hit@5** | total hit@1 |
|---|---|---|---|---|---|---|
| a) actuelle (même jour) | 10/10 | 16/17 | 10/17 | 0/5 | 36/49 | 28/49 |
| e') ancien exemple (18/11, section 2) | 10/10 | 17/17 | 15/17 | 0/5 | 42/49 | 38–40/49 |
| **e') nouvel exemple** | 10/10 | 17/17 | **16/17** | **1/5** | **44/49** | 38–39/49 |

Au niveau paragraphe : 43/49 (ancien exemple 41/49, actuelle 35/49). Aucun recul par rapport à la configuration actuelle. Les deux questions gagnées : **q33** entre de justesse (rang 5 ; ancien exemple 6–10) et **a05** (rang 3 ; ancien exemple hors des 5). q44, a01 et a04 restent hors des 20 premiers.

**Prudence** : la reformulation est instable d'une passe à l'autre (section 3). Pour séparer l'effet de l'exemple de cette instabilité, les 58 questions ont été recherchées une fois avec chaque exemple, le même jour, et comparées aux passages des réponses relues (`answers_v6_remote*.md`) : **29 questions sur 58 changent de passages avec le nouvel exemple, 15 sur 58 avec l'ancien exemple rejoué**. Une partie des changements (et peut-être du +2) vient donc de l'instabilité, pas de l'exemple.
