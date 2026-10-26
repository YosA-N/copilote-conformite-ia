# CLAUDE.md — Copilote IA de conformité

## Le projet

Projet personnel open source (licence MIT, dépôt GitHub public) : un assistant **RAG** (Retrieval-Augmented Generation) qui répond **en français** aux questions des PME et des associations sur le **RGPD** et l'**AI Act**, et qui **cite toujours l'article source**.

L'auteur débute en programmation : Claude écrit le code, l'auteur valide. Tout doit rester **gratuit** et tourner **en local**.

## Machine de l'auteur

- Windows 11, Python 3.13.2, Git 2.48, Ollama 0.40.11 (mis à jour automatiquement par Ollama : 0.40.7 → 0.40.10 pendant la séance 4, → 0.40.11 avant la séance 5 bis)
- 16 Go de RAM, NVIDIA GTX 1650 avec **4 Go de VRAM** → le modèle de génération doit peser au plus ~3 Go (quantifié Q4), contexte limité à ~8K tokens.
- **VRAM** : `bge-m3` (1,2 Go) + `ministral-3:3b` (3,0 Go) dépassent ensemble les 4 Go. Mesuré (séance 3) : sur la carte graphique, `bge-m3` occupe 0,69 Go et traite environ 300 tokens/s ; sur le CPU (option Ollama `num_gpu=0`), il est presque aussi rapide, avec des vecteurs identiques à 0,9999 près. Les questions passent donc par le CPU (`QUERY_EMBEDDING_DEVICE=cpu`) pour laisser la carte graphique au modèle de génération.
- **Mesures de `ministral-3:3b`** (séance 4, Q4_K_M, 3,8 milliards de paramètres, 26 couches, module de vision inclus) :
  - Laissé à Ollama, il n'est placé qu'à 45-55 % sur la carte graphique et génère à 10-15 tokens/s, soit environ 50 s par réponse.
  - Avec toutes les couches forcées (`num_gpu=99`), il tient entièrement en VRAM et génère à **44 tokens/s** : 3,45 Go avec `num_ctx=4096`, 3,66 Go avec 6144, **3,87 Go avec 8192** (sur 4 Go).
  - Choix : `LLM_NUM_CTX=8192` et `LLM_NUM_GPU=99`. Le pire prompt (5 chunks de 4 000 caractères) approche 6 000 tokens, et un prompt type en fait environ 2 000.
  - En cas d'erreur de mémoire : baisser `LLM_NUM_CTX`, puis `LLM_NUM_GPU`.
  - La lecture du prompt reste vers 160 tokens/s. Une question coûte environ 30 s : recherche sur CPU 2 à 4 s, lecture du prompt environ 12 s, rédaction environ 7 s, plus environ 5 s de chargement à la première question.
  - `bge-m3` (CPU, 0 Go de VRAM) et `ministral` (GPU) restent chargés ensemble après la première question.
- **Mesures de `qwen3:4b-instruct`** (séance 5, Q4_K_M, 4 milliards de paramètres, 36 couches, pas de module de vision) :
  - Avec toutes les couches forcées (`num_gpu=99`) : 3,10 Go (`num_ctx=4096`), 3,39 Go (6144), **3,68 Go (8192)** de VRAM. Il tient entièrement sur la carte graphique.
  - Génération : 38 tokens/s avec 4096 ou 6144, 29 à 36 tokens/s avec 8192. Lecture du prompt vers 137 tokens/s.
  - Environ 31 s par question avec le format « extraits puis réponse ».

## Choix techniques

- **Langage** : Python (paquet `src/compliance_copilot/`).
- **Corpus** : RGPD (règlement (UE) 2016/679), AI Act (règlement (UE) 2024/1689) et quelques fiches CNIL. Découpage (**chunking**) **par article**.
  - Versions consolidées figées dans `src/compliance_copilot/sources.py` : RGPD du 04/05/2016 (99 articles), AI Act du 27/07/2026 (intègre 2026/1744 : 119 articles, 14 annexes). Pas de considérants.
  - Téléchargement par **Cellar** (`publications.europa.eu/resource/celex/…`) : EUR-Lex renvoie un défi anti-robot aux scripts, ne pas chercher à le contourner.
  - Mention de source EUR-Lex obligatoire (CC BY 4.0) : voir le README.
  - Taille des chunks : 4 000 caractères au plus (~1 000 tokens, `MAX_CHUNK_CHARS` dans `corpus.py`). C'est un point de départ : des morceaux plus petits seront testés à l'étape d'évaluation.
- **Embeddings** : modèle open source multilingue, en local (servi par Ollama). Par défaut : `bge-m3`.
  - Interface `Embedder` dans `embeddings.py` (un autre backend n'a besoin que de `model` et `embed()`), envoi par lots de 16, `truncate=false` (erreur plutôt que texte coupé en silence).
- **Base vectorielle** : Chroma 1.5.9, persistante dans `data/index/`, distance cosinus.
  - Télémétrie désactivée et `embedding_function=None` : Chroma ne télécharge jamais son propre modèle.
  - `data/index/manifest.json` garde l'empreinte de `chunks.jsonl` et le nom du modèle : l'index n'est recalculé que s'ils changent. Sous Windows, on supprime la collection, jamais le dossier (fichiers verrouillés).
- **Recherche retenue (séance 5)** : vecteurs `bge-m3` + **lexique** (`lexicon.py`, `SEARCH_LEXICON=all`), qui ajoute à la question le vocabulaire juridique des mots courants. Les entrées viennent de v0 et, depuis la séance 6, partie 2, aussi des échecs de v1 (7 entrées générales : santé, prospection, sécurité, prestataire, pays tiers, émotions, amendes). Jamais de `questions_v2.jsonl`.
  - **5 passages** donnés au modèle (`SEARCH_K=5`). 8 ont été mesurés à la séance 6 : plus lent (48 s médian, 93 s max), 5 questions sur 32 perdaient des passages faute de contexte, et rien de plus n'était trouvé une fois le nouveau lexique en place.
  - Recherche hybride vecteurs + BM25 (`lexical.py`, fusion RRF) testée puis rejetée : moins bonne sur v1 ; disponible avec `SEARCH_MODE=hybrid`.
  - **Au plus 2 passages d'un même article** (séance 5 bis, `SEARCH_MAX_PER_ARTICLE=2`, `limit_per_article` dans `index.py`) : la recherche prend 4 × k candidats, puis écarte le 3e morceau d'un article et les suivants. Cause générale corrigée : un long article découpé en paragraphes occupait tout le top 5 (q10 : art. 50 ×2 et art. 26 ×3, art. 4 au rang 7).
- **Évaluation** : `eval/questions_v0.jsonl` (10 questions types, articles attendus vérifiés dans le texte), mesurée par `evaluate_retrieval.py` (hit@1, hit@5, rang du premier article attendu). On mesure d'abord ; on ne retouche pas les questions pour améliorer le score.
  - **Règle anti-triche, depuis la séance 6, partie 2** : les questions v1 ont été relues par l'auteur (`eval/reviews/heldout_v3.jsonl`) ; elles ne sont plus « jamais vues ». **On règle désormais sur v0 et v1. La mesure finale se fait uniquement sur `eval/questions_v2.jsonl` (figé au commit `65ee0c4`) et sur les questions personnelles de l'auteur (`eval/questions_author.jsonl`)**, jamais lues ni utilisées avant.
  - Ancienne règle (séances 5 à 6, partie 1) : `eval/questions_v1.jsonl` (20 questions, dont 3 hors sujet, figées au commit `c57bc66` avant toute amélioration) servait **seulement à mesurer** ; on réglait sur v0, jamais sur v1. Un changement est gardé s'il ne fait baisser le hit@5 sur **aucun** jeu (v0, v1) et fait monter au moins une mesure (règle assouplie à la séance 5 bis, décision de l'auteur : avant, il fallait une amélioration sur les deux jeux).
  - Relectures humaines de référence : `eval/review_v0.md`, `eval/review_v1.md` (v1 : 9 justes, 2 partielles q02 et q06, 1 fausse et dangereuse q10) et `eval/review_v2.md` (v2 : 6 justes, 5 partielles q01, q02, q06, q07, q10, 1 fausse q08). Mesures des séances 5, 5 bis et 5 ter : `eval/results_v1.md`.
  - **Grille de relecture (séance 6)** : `eval/rubric.md`.
    - 4 verdicts : juste, partiel, faux, dangereux (une erreur qui pourrait faire agir à tort : inventer ou nier une obligation, une durée, une interdiction).
    - Cas limites validés par l'auteur : en cas de doute, le plus sévère ; hors sujet traité = faux ; refus alors que le corpus répond = faux ; réponse coupée = partiel ; on juge la réponse affichée, pas les alertes.
    - Relectures structurées dans `eval/reviews/<version>.jsonl` (`id`, `verdict`, `comment`), comptées par `scripts/review_summary.py` (option `--check` : chaque relecture couvre exactement les questions de `eval/answers_<version>.md`). Les `review_v*.md` restent pour le détail.
    - Reclassement selon la grille, décidé par l'auteur : v0 q01 (obligation inventée) et v2 q08 (exception inversée) deviennent « dangereux ».
    - Verdicts (juste / partiel / faux / dangereux) : v0 5/1/3/3 ; v1 9/2/0/1 ; v2 6/5/0/1 ; **v3 9/3/0/0** (q03 reclassée « partiel » ensuite, même règle que v4) ; v4 8/2/0/2 ; heldout_v3 6/5/5/4 ; heldout_v4 9/3/4/4.
  - **Examen final (séance 6)** : `eval/questions_v2.jsonl`, 20 questions (12 RGPD, 5 AI Act, 3 hors sujet), figées au commit `65ee0c4` avant tout autre changement de la séance 6.
    - Articles attendus vérifiés en lisant le corpus, jamais avec la recherche ni le modèle.
    - **Ni lues ni utilisées avant la toute fin du projet** : aucune réponse générée, aucune mesure ; seul un test de format les ouvre.
    - Écrites par Claude, qui connaît les points faibles du système (risque de biais). L'auteur ajoutera à la fin 5 questions à lui dans `eval/questions_author.jsonl` ; `answer_questions.py --questions` et `review_summary.py --check` acceptent ce fichier.
  - **Réponses de la v3 aux 20 questions v1** : `eval/answers_heldout_v3.md`, relues par l'auteur. Résultat : **6 justes, 5 partiels, 5 faux, 4 dangereux**, contre 9 justes sur 12 (10 avant le reclassement de q03) pour les questions v0 qui avaient servi au réglage (sur-apprentissage).
  - **Séance 6, partie 2** (`eval/results_v2.md`).
    - **Diagnostic de heldout_v3** : 6 erreurs viennent de la recherche (dont 3 des 4 dangereuses), 6 de la rédaction (dont q26, dangereuse), 1 de la longueur, 1 est un hors sujet traité. Quand le bon article manque, le modèle répond avec assurance.
    - Un seuil sur le score de la recherche ne permet pas de s'abstenir : q24, dangereuse, a 0,673.
  - **Mesure au niveau du paragraphe** : dans `expected` des questions v0 et v1, le paragraphe utile est précisé quand l'article est découpé (3 questions v0, 9 questions v1). `article_level()` ramène les références à l'article, si bien que les chiffres anciens ne changent pas. Un morceau découpé par points (`par_2_a-i`) compte pour son paragraphe (`par_2`).
  - **Recherche après le nouveau lexique** (`compare_retrieval.py --repeat 3`) : v0 hit@5 10/10 ; v1 hit@5 **17/17** au niveau article (avant 13/17) et **15/17** au niveau paragraphe (avant 11/17). Ces chiffres sont optimistes sur v1, d'où viennent les entrées.
    - La limite de 2 par article est gardée : avec 3 ou sans limite, v0 tombe à 9/10.
    - Coût connu de cette limite : q18 (art. 9, § 1) et q27 (art. 99, § 4 et § 6) restent hors des 5 passages.
  - **Juge d'abstention** (`judge_extracts`, `ANSWER_JUDGE=on`) : un second appel court répond OUI ou NON (« ces extraits répondent-ils directement à la question ? ») ; si c'est NON, la réponse est remplacée par `ABSTENTION`.
    - Calibrage sur les 32 réponses relues : 0 abstention sur 12 justes, 2 sur 4 dangereuses (q15, q18), h05 (hors sujet) arrêtée, mais 2 réponses partielles (q16, q22) deviennent des abstentions, donc « faux » selon la grille.
    - Le juge n'est pas stable : sur q18, NON sur une réponse, OUI sur une réponse presque identique.
    - Médiane 4,5 s.
  - **Effets séparés sur les réponses dangereuses** : 8 passages corrigent q15 ; le juge seul arrête q15, q18 et h05. Rien ne corrige q24 : le 8e passage est retiré faute de place, et c'est le lexique qui la règle. Rien ne corrige q26 (erreur de rédaction).
  - **Configuration complète v4** :
    - réglages : nouveau lexique, 5 passages, limite de 2, juge, `LLM_MAX_TOKENS=2000` ;
    - prompt : règle « un extrait de chaque passage » retirée, consigne d'abstention ajoutée.
    - Sur 32 questions : 26 réponses sur 27 avec un extrait de l'article attendu (v3 : 22), 5 hors sujet refusés sur 5, aucune réponse coupée, 1 abstention (q22).
    - **Temps : génération et juge médians 40 s, maximum 105 s ; 6 questions sur 32 dépassent 60 s** (longs extraits).
    - Lecture rapide de Claude, pas un verdict : q15 corrigée ; q18 toujours problématique (§ 1 et § 2 absents) ; q26 sans la condition d'hypertrucage ; h05 refusée ; q22 abstention (donc « faux »).
    - q24 n'est **pas stable** : juste en apparence dans `answers_heldout_v4.md`, mais avec l'exception inversée dans la comparaison faite le même jour (l'alerte « négation » l'avait signalée).
    - Les temps des fichiers de réponses sont faussés par des incidents de la machine (veille pendant q20 de heldout_v4 ; q06 de v4 à 6 tokens/s ; q17 de heldout_v4 bloquée environ 3 min). La mesure de référence est celle de `compare_models.py`.
    - **Compromis de temps** (`eval/results_v2.md`, section 8) : variante du prompt `eval/prompts/short_extracts.txt` (extraits de 40 mots au plus).
    - **Décision de l'auteur** : 2 000 tokens, et extraits courts gardés seulement s'ils ne réduisent ni les extraits vérifiés ni la complétude. **Critère non rempli, donc retour aux extraits normaux** : 4 questions perdent des extraits vérifiés, 11 réponses raccourcissent de plus de 40 %, q10 devient une abstention, et q06 a une liste incomplète.
    - **Configuration retenue = v4** ; `answers_v4.md` et `answers_heldout_v4.md` ont été régénérées pour la relecture (temps : `eval/results_v2.md`, section 10).
  - **Trois corrections générales demandées par l'auteur avant les réponses finales** (`eval/results_v2.md`, section 10) :
    - **Lexique neutre** : « émotions » → « systèmes de reconnaissance des émotions », sans « pratiques interdites », car le lexique traduit et ne conclut pas. Coût mesuré : q24 retombe au rang 10, et v1 passe de 17 à 16/17 au niveau article.
    - **1er paragraphe d'un article découpé** (`SEARCH_FIRST_PARAGRAPH=on`, `with_first_paragraphs` dans `index.py`) : il est ajouté quand un paragraphe suivant est retenu, dans la limite de 2 par article ou en 3e position.
      - Retenu : v0 10/10, v1 16/17 au niveau article (inchangés), et v1 de 14 à 15/17 au niveau paragraphe (q18 : § 2 au rang 2).
      - q27 n'en profite pas.
    - **Contrôle de négation étendu** :
      - inversions sans « ne … pas » (« autres que », « hors », « excepté », « à l'exception de ») ;
      - règle contraire (`inverted_rules`) : « vous avez le droit…, sauf… » devant une liste annoncée « … sont interdites : ».
      - Test de non-régression : la phrase inversée de q24 (v4).
      - Aucune nouvelle fausse alerte sur 224 réponses rejouées.
  - **Réponses finales à relire** : `eval/answers_v4.md` et `eval/answers_heldout_v4.md` (configuration finale v4 avec ces trois corrections, sur secteur, sans incident).
    - **Temps sur les 32 questions** (recherche, génération et juge) : **médian 39 s, max 89 s, 4 questions au-delà de 60 s** (q04, q23, q21, q27).
    - Lecture rapide de Claude, pas un verdict : q15 juste ; q18 passe à « Non… interdit », trop restrictive (sans les exceptions de l'art. 9, § 2) ; q24 devient une abstention (art. 5 non trouvé avec le lexique neutre) ; q26 cite l'hypertrucage mais le rattache mal ; h03 à h05 refusées ; abstentions q22 et q24.

      | 32 questions | Médian | Max | Au-delà de 60 s | Coupées |
      |---|---|---|---|---|
      | Extraits courts + 2 000 tokens | 37 s | 90 s | 2 | 0 |
      | Extraits courts + 1 200 tokens | 34 s | 60 s | 1 | 1 (q23, refusée) |

      - Dans les deux cas, le juge s'abstient sur q10, et les réponses passent de 134 à 75 ou 65 mots.
      - La machine était plus rapide pendant ces mesures (34 tokens/s contre 28).
      - Choix de l'auteur : 2 000 tokens, pour ne couper aucune réponse.
    - Réponses à relire : `eval/answers_v4.md` et `eval/answers_heldout_v4.md`.
  - Les vecteurs des questions calculés sur le CPU varient très légèrement d'un lancement à l'autre : ±1 rang possible sur les passages aux scores presque égaux (q16). Répéter les mesures (`compare_retrieval.py --repeat 3`) avant de conclure.
  - Mesure de référence (séance 3, `bge-m3`, chunks de 4 000 caractères au plus) : **hit@1 = 6/10, hit@5 = 7/10**. Échecs : q03 durée de conservation (rang 6, réponse partielle dans le corpus), q04 mention d'information (rang 20), q10 IA générative au travail (art. 4 non trouvé dans les 20 premiers). Les sigles DPO et AIPD passent (rang 1). Pistes à étudier à la séance 5.
  - Séance 5 (meilleure configuration) : v0 **hit@1 = 7/10, hit@5 = 9/10** ; v1 **hit@1 = 10/17, hit@5 = 13/17** (départ v1 : 9/17 et 11–12/17). q10 (art. 4) et q21 (art. 32) restent hors des 5 premiers.
  - Séance 5 bis (+ 2 passages par article au plus, 3 mesures identiques) : v0 **hit@1 = 7/10, hit@5 = 10/10** (q10 au rang 5) ; v1 inchangé, 10/17 et 13/17. Effet de bord : q07 perd des paragraphes de l'art. 35 au profit de l'art. 27 de l'AI Act, et la réponse v2 confond les deux analyses d'impact (le hit@5 ne le voit pas). À trancher.
  - Génération séance 5 bis (`compare_models.py`, 32 questions) : réponses avec [n] 26/26 (avant 5/27), tutoiements 0 (avant 3), réponses avec alerte 7/32 (avant 23/32), extraits vérifiés 75/79, hors sujet refusés 5/5, 1 réponse coupée (q23). Vitesse 21 tokens/s ce jour-là, contre 36 : la machine était plus lente (test A/B, ancien prompt aussi à 25 tokens/s ; Ollama passé tout seul en 0.40.11) ; le nouveau prompt ajoute environ 290 tokens à lire.
  - q10 v2 cite bien l'art. 4, mais présente l'obligation des fournisseurs (art. 50, § 1) comme celle de l'utilisateur, et finit par une phrase sans [n] ni extrait, non signalée. Autres points ouverts (q06, q08, q03) : `eval/results_v1.md`, section 7.6.
- **Génération** : petit modèle via Ollama, derrière une **interface interchangeable** : changer de modèle = modifier une ligne dans `.env`. Par défaut : **`qwen3:4b-instruct`** (séance 5 ; avant : `ministral-3:3b`).
  - Comparaison sur les mêmes passages (`compare_models.py`, 32 questions) : qwen recopie 79 extraits sur 83 mot pour mot (ministral : 45 sur 88), refuse les 5 questions hors sujet (ministral : 2), mais il est environ 5 s plus lent par réponse.
  - Interface `ChatModel` dans `llm.py` (`/api/chat` en streaming). Réglages dans `.env` : `LLM_NUM_CTX`, `LLM_NUM_GPU`, `LLM_TEMPERATURE=0.1`, `LLM_MAX_TOKENS=2000` (place pour les extraits puis la réponse ; 1 500 jusqu'à la séance 6), `ANSWER_JUDGE=on`.
  - **Génération fidèle (séance 5)** : le modèle écrit `EXTRAITS :` (phrases exactes des passages), puis `RÉPONSE :` à partir de ces phrases seulement.
    - Le code vérifie chaque extrait **mot pour mot** dans le passage cité (tolérés : espaces, apostrophes, guillemets, majuscules, coupures « … » ou retour à la ligne ; 6 mots au moins).
    - Sans extrait vérifié, la réponse devient « Les textes trouvés ne permettent pas de répondre à cette question. », sans alerte « aucune citation ». En streaming, la réponse n'apparaît qu'après la vérification de ses extraits.
    - Limite connue : un extrait vérifié prouve que la phrase existe, pas qu'elle répond à la question (q10 dans `eval/results_v1.md`).
    - Défauts connus de qwen : il met rarement des [n] dans la réponse, il dépasse parfois les quatre extraits et il a tutoyé une fois (q04).
  - **Prompt de la séance 5 bis** : écrit entièrement au « vous » (un prompt au « tu » fait tutoyer le modèle), avec un court exemple **fictif** du format et des [n], et des règles générales : ne jamais conclure « aucune obligation » faute de passage (« les passages trouvés ne traitent pas de ce point ») ; répondre à chaque partie de la question ; dire quand le texte ne donne qu'un principe (les règles concrètes peuvent venir du droit national ou de la CNIL) ; toujours vouvoyer.
  - **Contrôles de la réponse par le code** (séance 5 bis, `rag.py`) : de simples signaux, sans compréhension du sens.
    - Si la réponse n'a aucun [n] : alerte sur une phrase dont moins de **35 %** des racines de mots (`tokenize` de `lexical.py`) se retrouvent dans les extraits vérifiés (`SUPPORT_THRESHOLD`, choix de l'auteur ; 60 % alertait sur 19 réponses sur 27). Remplace l'ancienne alerte « aucune citation ».
    - Toujours : alerte sur une affirmation d'absence ou d'impossibilité (« aucune obligation », « ne s'applique pas », « vous ne pouvez pas »…) si aucun extrait vérifié ne contient de négation. Effet connu : signale aussi des déductions justes (q01 « cela n'est pas obligatoire »).
    - Toujours : alerte sur le tutoiement (tu, toi, te, t', ton, ta, tes).
    - Tests de non-régression (`tests/test_rag.py`, `KNOWN_WRONG`) : les phrases fausses de q03 v0 (« 10 ans »), q09 v0 (« vous ne pouvez pas ») et q10 v1 (« aucune obligation… usage interne ») doivent rester signalées, avec leurs vrais extraits.
  - **Prompt de la séance 5 ter (v3)** : règles générales en plus. Exceptions et conditions recopiées mot pour mot entre « » ; chaque obligation nomme son règlement, son article et qui est visé ; jamais deux obligations de textes différents sous un même nom ; listes de cas reprises en entier ou annoncées comme partielles (« parmi d'autres cas ») ; un extrait de chaque passage utile d'abord ; 6 extraits au plus (avant : 4). Exemple du prompt toujours fictif. Longueur : 3 678 caractères (v1 : 1 622, v2 : 2 613).
  - **Contrôles de la séance 5 ter** (`rag.py`, une alerte par type et par réponse au plus) :
    - négation ajoutée ou retirée dans une condition ou une exception par rapport à l'extrait le plus proche (`flipped_negations` : au moins 50 % de mots communs ; 12 mots côté réponse, 12 ou 24 côté extrait) ;
    - texte entre « » d'au moins 3 mots absent des extraits vérifiés (`quotes_not_in_extracts`) ;
    - exception (« sauf si »…) hors « » qui partage moins de 60 % de ses mots avec chaque extrait (`unquoted_exceptions`) ;
    - liste de cas (annonce « lorsque : », « cas suivants », « conditions suivantes »… ; pas les listes de contenu « informations suivantes ») reprise en partie sans « parmi », « entre autres », « liste complète » (`incomplete_case_lists`) ; « notamment » ne compte pas ;
    - obligation dont l'extrait vise un fournisseur, un importateur ou un distributeur (et pas aussi le déployeur ou le responsable du traitement), sans nommer cet acteur (`other_actor_duties`) ;
    - phrase sans nom de règlement, seulement si la réponse s'appuie sur le RGPD et l'AI Act (`unnamed_regulations`).
    - Tests de non-régression avec les vraies phrases fausses de la v2 : q08 (négation inversée), q01 (liste 0 cas sur 3, exception inventée), q10 (obligation du fournisseur), q07 (règlement non nommé).
  - `compare_models.py --prompt-file` compare un autre prompt (par exemple celui d'une séance précédente, tiré de Git) sur les mêmes passages, le même jour.
  - **Mesures séance 5 ter** (`eval/results_v1.md`, section 8), prompt v1 contre prompt v3, le même jour, sur les mêmes passages (32 questions) :

    | | Prompt v1 | Prompt v3 |
    |---|---|---|
    | [n] | 4/26 | 28/28 |
    | Tutoiements | 3 | 0 |
    | Réponses avec alerte | 19/32 | 15/32 |
    | Hors sujet refusés | 5/5 | 4/5 (h05 traitée) |
    | Réponses coupées | 0 | 2 |
    | Mots par réponse | 80 | 131 |
    | Tokens lus | 2 604 | 3 186 |
    | Temps | 30,9 s | 32,8 s |
    | Extraits vérifiés | 70/75 | 78/85 |

  - **Lecture de `answers_v3.md`** : q01 (3 cas), q02 (« non occasionnel »), q06 (art. 34), q07 (deux analyses séparées) et q08 (exception fidèle) progressent par rapport à la v2 et au prompt v1. q08 et q10 présentent encore l'obligation du fournisseur (art. 50, § 1) comme celle de l'utilisateur ; le code le signale. Pas de retour au prompt v1 proposé.
  - **Reculs de la v3** : h05 traitée, 2 réponses coupées, réponses 60 % plus longues. Cause probable : la règle « un extrait de chaque passage utile d'abord » et la limite de 6 extraits. Piste : retirer cette règle, puis remesurer.
  - **Contrôles** :
    - le moins utile est « règlement non nommé », qui donne des alertes sans vraie confusion et ne voit pas q07 v2 ;
    - fausse alerte « négation » sur q11 v3 (le morceau comparé déborde après « : ») : correction proposée, non faite, car vue sur une question v1.
  - Mesures faites **sur secteur** : sur batterie, Windows bride la carte graphique (état P8, 300 MHz, environ 10 min par réponse). Vérifier `BatteryStatus` (2 = sur secteur) avant une mesure.
  - Messages d'erreur clairs prévus : Ollama arrêté, modèle absent, mémoire insuffisante.
  - `rag.py` : prompt système en français et passages numérotés [1]…[5]. Si le prompt risque de dépasser le contexte, les derniers passages sont retirés et un avertissement est affiché.
  - Ce que fait le **code**, et non le modèle :
    - citations normalisées (« [1b] » devient « [1] », y compris pendant le streaming) et vérifiées (passage inexistant, aucune citation) ;
    - sources construites à partir des métadonnées ;
    - réponse coupée signalée (`done_reason = "length"`) ;
    - avertissement « Information, pas un conseil juridique ».
  - Réponses de référence non retouchées : `eval/answers_v0.md` (séance 4), `eval/answers_v1.md` (séance 5), `eval/answers_v2.md` (séance 5 bis) et `eval/answers_v3.md` (séance 5 ter, relue : `eval/reviews/v3.jsonl`), produites par `answer_questions.py --version …` (10 questions et 2 hors sujet).
- **Interface web** : Streamlit, plus tard.
- **Dépendances** : on n'ajoute une bibliothèque qu'à l'étape qui en a besoin, avec une version épinglée (`==`) dans `requirements.txt`.

## Règles

1. **Langues** : code, noms (fichiers, fonctions, variables) et messages de commit en **anglais**. README, interface et réponses du copilote en **français**.
2. **Sources** : chaque réponse du copilote cite sa source (règlement + numéro d'article, ou fiche CNIL). Pas de source trouvée = le dire, ne pas inventer.
3. **Secrets** : jamais de secret dans le dépôt. Le fichier `.env` est ignoré par Git ; seul `.env.example` (valeurs d'exemple) est commité.
4. **Accord préalable** : ne rien télécharger (modèles Ollama, gros fichiers) et ne rien pousser (`git push`) sur GitHub sans l'accord de l'auteur.
5. **Explications** : après chaque étape, expliquer en 3 à 5 phrases simples ce qui a été fait et pourquoi, en donnant les termes techniques anglais (par exemple « environnement virtuel (**virtual environment**) »).
6. **Méthode** : présenter un plan et attendre la validation avant les changements importants. Travailler sur une branche, pas directement sur `main`.
7. **Relecture** : ne jamais fusionner une Pull Request avant que l'auteur confirme l'avoir relue. Après l'ouverture d'une PR, s'arrêter et attendre cette confirmation.

## Structure

```
src/compliance_copilot/   code du paquet (config.py, health.py, …)
scripts/                  scripts lancés à la main (check_env.py, …)
tests/                    tests pytest (hors ligne : ils ne demandent pas Ollama)
data/raw/                 textes sources téléchargés (ignoré par Git)
data/processed/           articles découpés : chunks.jsonl (ignoré par Git)
data/index/               index Chroma et manifest.json (ignoré par Git)
eval/                     questions-tests d'évaluation (versionné, contrairement à data/)
```

## Commandes utiles (PowerShell, depuis la racine du dépôt)

```powershell
python -m venv .venv                                   # créer l'environnement virtuel
.venv\Scripts\python -m pip install -r requirements.txt  # installer les dépendances
copy .env.example .env                                 # créer sa configuration locale
.venv\Scripts\python scripts\check_env.py              # vérifier Python et Ollama
.venv\Scripts\python scripts\download_sources.py       # télécharger les textes (une seule fois)
.venv\Scripts\python scripts\build_corpus.py           # découper les textes en chunks
.venv\Scripts\python scripts\build_index.py            # calculer les embeddings et remplir Chroma
.venv\Scripts\python scripts\search.py "question"      # afficher les 5 passages les plus proches
.venv\Scripts\python scripts\evaluate_retrieval.py     # mesurer hit@1 et hit@5
.venv\Scripts\python scripts\ask.py "question"         # poser une question (réponse + sources)
.venv\Scripts\python scripts\answer_questions.py --version v3   # écrire eval/answers_v3.md (12 questions)
.venv\Scripts\python scripts\answer_questions.py --questions eval\questions_v1.jsonl --version heldout_v3   # poser un autre fichier de questions
.venv\Scripts\python scripts\review_summary.py --check        # tableau des verdicts des relectures (eval\reviews\*.jsonl)
.venv\Scripts\python scripts\compare_retrieval.py --repeat 3    # comparer les configurations de recherche (v0 et v1)
.venv\Scripts\python scripts\compare_models.py ministral-3:3b qwen3:4b-instruct   # comparer les modèles sur les mêmes passages (option --prompt-file : comparer un autre prompt)
.venv\Scripts\python -m pytest                         # lancer les tests
```

Pas besoin d'« activer » le venv : on appelle directement `.venv\Scripts\python`.
