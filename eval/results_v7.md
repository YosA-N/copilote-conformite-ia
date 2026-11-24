# Examen 2 : questions neuves

## 1. Provenance des questions

- **`eval/questions_exam2.jsonl`** : 28 questions (ids `e01` à `e25`, et `he01` à `he03` hors sujet), **recopiées mot pour mot**.
- **Écrites par un assistant sans accès au projet**, à la demande de l'auteur, le **18/11/2026**, donc **avant la séance 7 ter**. Elles sont restées **hors du dépôt** jusqu'au 24/11/2026. Claude Code ne les a pas vues avant cette date.
- **Articles attendus** fixés par Claude Code (Claude Opus 5.5) **en lisant le texte du corpus** (`data/processed/chunks.jsonl`), **jamais avec la recherche ni avec le modèle**. Chaque référence a été vérifiée : elle existe dans le corpus. **Validés par l'auteur le 24/11/2026**, avant tout lancement.
- Ces questions n'ont servi à **aucun réglage** : aucune réponse générée, aucune mesure de recherche, aucun réglage changé avant la validation de l'auteur.

## 2. Articles attendus (validés par l'auteur le 24/11/2026)

« Attendu » : l'article qui répond ; la recherche compte un succès si l'un d'eux figure parmi les 5 passages. « Voisins » : utiles, mais pas indispensables. Couverture : complet (le corpus répond), partiel (le corpus ne donne qu'une partie, le reste vient du droit national ou de la CNIL), hors corpus (le corpus ne permet pas de répondre). La note complète de chaque question est dans `questions_exam2.jsonl`.

| Id | Question (abrégée) | Attendus | Voisins | Couverture |
|---|---|---|---|---|
| e01 | Caméras dans le magasin et la salle de pause | RGPD 6 § 1, 13 | 5, 88, 21, 35 § 3 | partiel |
| e02 | Effacer les données d'une ancienne cliente, factures à garder | RGPD 17 | 6 § 1, 12 § 3, 5 | complet |
| e03 | Durée de conservation des CV non retenus | RGPD 5 | 13, 17, 6 § 1 | partiel |
| e04 | Liste des bénévoles dans un Excel sur Google Drive | RGPD 32, 28 § 1 | 5, 28 § 3, 24, 29, 44, 46 | partiel |
| e05 | Bandeau cookies avec Google Analytics seulement | **aucun** | RGPD 95, 4 (11), 7, 44 | **hors corpus** (*) |
| e06 | Boîte mail de l'accueil piratée | RGPD 33, 34 | 4 (12), 32 | complet |
| e07 | Prestataire de paie : contrat spécial ? | RGPD 28 § 3 | 28 § 1, 4 (8), 32 | complet |
| e08 | Newsletter aux anciens clients sans accord | RGPD 6 § 1, 21 | 7, 13, 95 | partiel |
| e09 | Copie de toutes les données d'un salarié, mails compris ; délai | RGPD 15, 12 § 3 | 12 § 5 | complet |
| e10 | Lire la boîte mail d'un salarié parti | RGPD 5, 6 § 1 | 88, 13, 17, 32 | partiel |
| e11 | Numéro de sécurité sociale et handicap des stagiaires | RGPD 9 § 1, 9 § 2, 87 | 4 (15), 5, 6 § 1, 35 § 3 | partiel |
| e12 | Suivre les véhicules des techniciens par GPS | RGPD 6 § 1, 5 | 88, 13, 21, 35 § 1 | partiel (**) |
| e13 | Photos des bénévoles sur Facebook : accord écrit ? | RGPD 6 § 1, 7 | 4 (11), 4 (1), 13, 17, 21 | partiel |
| e14 | 8 salariés : registre et DPO ? | RGPD 30, 37 | — | complet |
| e15 | Logiciel clients hébergé aux États-Unis | RGPD 44, 45 § 1, 46 | 28 § 1, 49 § 1, 13 | partiel |
| e16 | On utilise juste ChatGPT : l'AI Act nous concerne ? | AI Act 3 (4), 2 § 1, 4 | 2 § 10, 50 § 4, 26, 113 | complet |
| e17 | Logiciel qui trie les CV : interdit ? règles ? | AI Act annexe III pt 4, 26 | 6 § 2, 6 § 3, 26 § 7, 26 § 11, 86, 113, RGPD 22, AI Act 5 § 1 | complet |
| e18 | Chatbot : dire qu'on parle à une machine ? | AI Act 50 § 1 | 50 § 5, 3 (3), 3 (4), 113 | complet |
| e19 | IA pour corriger les examens des stagiaires | AI Act annexe III pt 3 | 6 § 2, 6 § 3, 26, 86, 113, RGPD 22 | complet |
| e20 | Former les salariés à l'IA : obligatoire ? | AI Act 4 | 3 (56), 113 | complet |
| e21 | Visuels générés par IA : le dire ? | AI Act 50 § 4 | 3 (60), 50 § 2, 50 § 5 | complet |
| e22 | Outil qui analyse les émotions en visioconférence | AI Act 5 § 1 f-h | 3 (39), 99 § 3, 113, RGPD 9 § 1 | complet |
| e23 | L'outil écarte un candidat à tort : qui est responsable ? | RGPD 82, AI Act 26 | AI Act 16, 25 § 1, 26 § 5, 86, 6 § 2, RGPD 22 | partiel |
| e24 | Quand l'AI Act s'applique-t-il ? Qu'est-ce qui est en vigueur ? | AI Act 113 | 5 § 1, 4, 111 | complet |
| e25 | Données clients copiées dans ChatGPT : problème ? encadrer ? | RGPD 32, 29 | 5, 24, 28 § 1, 44, 33, AI Act 4 | partiel |
| he01 | TVA trimestrielle | — | — | hors corpus |
| he02 | Préavis de démission en CDI | — | — | hors corpus |
| he03 | Idées pour une fête de bénévoles | — | — | hors corpus |

Total : 24 questions avec article attendu (15 sur le RGPD, dont e25 ; 8 sur l'AI Act ; e23 sur les deux textes), 1 question du domaine sans article attendu (e05), 3 hors sujet.

(*) **e05, choix validé par l'auteur avec le tableau** : la règle sur les cookies vient de la directive 2002/58/CE et de la loi française, absentes du corpus (l'art. 95 du RGPD dit seulement que cette directive reste à part). La question est donc traitée comme les hors sujet : aucun article attendu, et la bonne réponse est de dire que le corpus ne permet pas de répondre. Une réponse « vous n'êtes pas obligé » serait dangereuse. Autre choix possible, non retenu : attendus RGPD 4 (11) et 7, couverture partielle.

(**) **e12** : voir la section 3.

## 3. Points à trancher avant l'examen

1. **L'exemple du prompt de reformulation correspond à e12.** Le 19/11/2026, à la séance 7 ter, l'exemple « empreinte digitale → données biométriques » a été remplacé parce qu'il correspondait à la question a01. Il est devenu **« géolocalisation des véhicules → données de localisation »**, choisi sans connaître ces questions (elles étaient hors du dépôt). Or **e12 demande : « Je peux suivre les véhicules de mes techniciens par GPS ? »**. En mode distant, où la reformulation est activée par défaut, e12 serait favorisée par un exemple qui lui correspond. **Décision de l'auteur (24/11/2026) : remplacer l'exemple** (section 3 bis). Choix qui se posait : remplacer l'exemple avant l'examen (par un exemple sans rapport avec les 86 questions connues (58 de réglage et 28 de l'examen 2), puis remesurer la recherche sur les jeux de réglage), ou le garder et signaler e12 comme biaisée.
2. **La plupart des sujets ont déjà servi au réglage.** Les questions sont neuves dans leur formulation, mais environ 19 des 25 reprennent le sujet et l'article attendu d'une question de réglage :

   | Examen 2 | Question de réglage sur le même sujet |
   |---|---|
   | e01 caméras | q34 caméras dans l'atelier (art. 88) |
   | e02 effacement et factures | q11 (art. 17) |
   | e03 durée des CV | q03 durée de conservation (art. 5) |
   | e06 boîte mail piratée | q06 fuite de données (art. 33, 34) |
   | e07 prestataire de paie | q15 prestataire informatique (art. 28, § 3) |
   | e08 newsletter | q14 lettre d'information (art. 21, 6) |
   | e09 copie des données d'un salarié, délai | q12 (art. 15) et q05 (art. 12, § 3) |
   | e11 handicap | q18 santé des bénévoles (art. 9) |
   | e13 photos de la fête | **a05, presque identique** (art. 6, 7) |
   | e14 registre et DPO | q01 (art. 37) et q02 (art. 30) |
   | e15 hébergement aux États-Unis | q16 (art. 44 à 46) |
   | e16 ChatGPT et e20 formation à l'IA | q10 IA générative (art. 4) |
   | e17 tri de CV | q09 (annexe III, point 4 ; art. 26) |
   | e18 chatbot | q08 (art. 50, § 1) |
   | e19 notation des examens | q41 (annexe III, point 3) |
   | e21 visuels générés | q26 image créée par une IA (art. 50, § 4) |
   | e22 émotions des salariés | q24 (art. 5, § 1, f) |
   | e24 dates d'application | q44 (art. 113) |

   Sujets vraiment nouveaux : e04 (Google Drive), e05 (cookies), e10 (boîte mail d'un salarié parti), e12 (GPS), e23 (responsabilité), e25 (ChatGPT et données clients). **Les résultats seront donc optimistes pour les questions qui recoupent le réglage** : il faudra les donner aussi à part (recoupement / sujets nouveaux).

## 3 bis. Remplacement de l'exemple du prompt de reformulation (24/11/2026)

**Nouvel exemple, choisi par l'auteur parmi trois propositions** : « logo sur l'emballage d'un appareil » → « marquage CE ». Vérifié contre le texte des 86 questions connues (58 de réglage, 28 de l'examen 2) : aucune ne parle de logo, d'emballage, d'appareil ni de marquage (les seules correspondances venaient du mot courant « ce »). Modifié dans `rewrite.py` et le README ; tests verts.

**Remesure de e') en distant** (`compare_retrieval.py --configs current,rw_remote_rerank --repeat 3`), 24/11/2026, 13:20 à 14:13, sur secteur (`BatteryStatus` = 2 avant et après), sur les 4 jeux de réglage seulement (l'examen 2 n'est pas mesuré) :

| Niveau article | v0 hit@5 | v1 hit@5 | v2 hit@5 | auteur hit@5 | **total hit@5** | total hit@1 |
|---|---|---|---|---|---|---|
| a) actuelle (même jour) | 10/10 | 16/17 | 10/17 | 0/5 | 36/49 | 28/49 |
| e') exemple « empreinte digitale » (18/11) | 10/10 | 17/17 | 15/17 | 0/5 | 42/49 | 38–40/49 |
| e') exemple « géolocalisation des véhicules » (19/11) | 10/10 | 17/17 | 16/17 | 1/5 | 44/49 | 38–39/49 |
| **e') exemple « marquage CE » (24/11)** | 10/10 | **16/17** | 14–15/17 | 1–2/5 | **41–42/49** | 38–39/49 |

Au niveau paragraphe : 40–41/49 (actuelle 35/49). **Aucun recul par rapport à la configuration actuelle** : la règle de décision est respectée. Mais c'est un peu moins qu'avec les deux exemples précédents :

- **q24** (émotions des salariés) sort des 20 premiers, dans les 3 passes : la reformulation donne cette fois « analyse des émotions ; système d'IA à haut risque ; employeur ; travailleur ; évaluation d'impact », sans « données biométriques », et l'art. 5 n'est plus trouvé (rang 11 dans la configuration actuelle, 1–2 avec les exemples précédents) ;
- **q38** (casier judiciaire) passe au rang 17 : « données sensibles » au lieu de « données relatives à des condamnations pénales » ;
- q33 reste hors des 5 passages ou de justesse (4–9) ; a05 entre de justesse (4–7).

Ces écarts sont **un effet de l'exemple, pas seulement du hasard** : les termes de q24 et de q38 sont identiques dans les 3 passes. La stabilité générale ne change pas (termes identiques aux 3 passes pour 17 questions sur 49, comme avec l'exemple précédent). Un exemple tiré de l'AI Act semble pousser le modèle vers le vocabulaire des systèmes à haut risque.

**Ce qu'il ne faut pas faire** : essayer d'autres exemples jusqu'à retrouver 44/49 reviendrait à régler le prompt sur les 49 questions connues, ce que l'examen 2 doit justement contrôler. **Décision de l'auteur (24/11/2026) : « marquage CE » est gardé et la configuration de l'examen est figée** (section 4).

## 4. Configuration figée (24/11/2026) et méthode

**Configuration figée** : le commit de la branche `eval/exam-2` qui ajoute cette section (étiquette Git locale `exam2-config`). Après cette étiquette : **aucun changement de code, de prompt, de lexique ni de réglage** avant la fin de l'examen, même après avoir vu une réponse ou un résultat ; ce qui est observé est noté, pas corrigé.

| | Mode local (défaut) | Mode distant |
|---|---|---|
| Modèle qui rédige et juge | `qwen3:4b-instruct` (Ollama 0.40.18, Q4_K_M) | `qwen/qwen3.8-27b` (Groq, preview, `reasoning_effort` non envoyé) |
| Recherche | `bge-m3` sur CPU, lexique en mots entiers (`SEARCH_LEXICON=all`), 5 passages, 2 au plus par article, 1er paragraphe ajouté | idem, **plus reformulation** (exemple « marquage CE ») **et reranker** `BAAI/bge-reranker-v2-m3` sur CPU (20 candidats) : `SEARCH_REWRITE=auto`, `SEARCH_RERANK=auto` |
| Génération | température 0,1 ; 2 000 tokens au plus ; contexte 8 192 ; extraits vérifiés mot pour mot ; juge d'abstention | idem |
| Contrôles du code | tous ceux de la séance 7 ter (négation, citations, adéquation, crochets 「 」 tolérés…) | idem, plus le garde-fou des données personnelles |

- `.env` : seulement des valeurs égales aux valeurs par défaut (`LLM_BACKEND=ollama`), plus la clé de l'API (jamais affichée) ; `SEARCH_REWRITE` et `SEARCH_RERANK` n'y figurent pas, donc `auto`.
- Corpus et index : RGPD du 04/05/2016 et AI Act du 27/07/2026, 763 morceaux, empreinte `12ea821e…7128`, index `bge-m3` construit le 24/10/2026.
- Bibliothèques du reranker : `torch` 2.15.0, `transformers` 5.23.0.

**Outil de mesure** : `compare_retrieval.py` connaît le jeu `exam2`, mais **ne le mesure que si on le demande** (`--sets exam2`) ; par défaut, il ne mesure que les jeux de réglage (test `test_retrieval_comparison_never_measures_the_exam_by_default`).

**Méthode** (leçon de la séance 7 ter, `eval/results_v6.md`, section 6.5 : une seule passe ne suffit pas pour comparer des réponses générées) :

- Recherche : hit@1 et hit@5, niveaux article et paragraphe, 3 mesures (`compare_retrieval.py --sets exam2 --configs current,rw_remote_rerank --repeat 3`) : configuration locale et configuration distante.
- Réponses : **chaque question posée 3 fois par mode** (`answer_questions.py --questions eval\questions_exam2.jsonl --version exam2_local_1` à `_3`, et `--backend openai --version exam2_remote_1` à `_3`), relues par l'auteur selon `eval/rubric.md` ; verdicts comptés en moyenne, avec le nombre de questions qui ont reçu au moins une réponse dangereuse ; résultats donnés aussi à part pour les 6 sujets nouveaux (e04, e05, e10, e12, e23, e25).
- Sur secteur (`BatteryStatus` = 2 avant et après) ; le quota de Groq (200 000 tokens par jour) impose environ une passe distante par jour, reprise avec `--resume` si besoin.
