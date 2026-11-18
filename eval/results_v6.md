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
