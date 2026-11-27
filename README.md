# Copilote IA de conformité

Assistant open source qui répond **en français** aux questions des PME et des associations sur le **RGPD** et l'**AI Act**, en **citant toujours l'article source**. Tout tourne **en local** et gratuitement, grâce à [Ollama](https://ollama.com).

**Statut :** projet en construction. Le copilote répond aux questions en citant ses sources, en ligne de commande. La qualité des réponses est en cours d'évaluation : lisez les [limites connues](#limites-connues) avant de l'utiliser.

> Ce copilote aide à comprendre les textes. Il ne remplace pas un conseil juridique.

## Prérequis

- Python 3.11 ou plus récent
- [Ollama](https://ollama.com) installé et lancé, avec deux modèles :
  - `bge-m3` pour la recherche (`ollama pull bge-m3`, 1,2 Go) ;
  - `qwen3:4b-instruct` pour rédiger les réponses (`ollama pull qwen3:4b-instruct`, 2,5 Go), retenu après comparaison avec `ministral-3:3b` (voir `eval/results_v1.md`).
- Une carte graphique NVIDIA avec 4 Go de mémoire suffit (testé sur une GTX 1650) ; sans elle, tout fonctionne sur le processeur, mais plus lentement.

## Installation (Windows, PowerShell)

```powershell
git clone https://github.com/YosA-N/copilote-conformite-ia.git
cd copilote-conformite-ia
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
copy .env.example .env
```

Le fichier `.env` contient votre configuration locale (adresse d'Ollama, modèles utilisés). Il n'est jamais envoyé sur GitHub.

## Vérifier l'environnement

```powershell
.venv\Scripts\python scripts\check_env.py   # Python et Ollama répondent-ils ?
.venv\Scripts\python -m pytest              # lancer les tests
```

## Préparer le corpus

```powershell
.venv\Scripts\python scripts\download_sources.py   # télécharge les textes dans data\raw\ (une seule fois)
.venv\Scripts\python scripts\build_corpus.py       # découpe les textes dans data\processed\chunks.jsonl
```

Chaque article devient un morceau de texte (**chunk**). Un article trop long (plus de 4 000 caractères) est découpé par paragraphe, par définition ou par point, et chaque morceau rappelle le règlement, l'article et son titre. Chaque chunk garde aussi ses métadonnées : règlement, article ou annexe, titre, chapitre, paragraphe, lien EUR-Lex vers l'article et date de version.

Les textes viennent de [Cellar](https://op.europa.eu/fr/web/cellar), le dépôt de l'Office des publications qui alimente EUR-Lex : EUR-Lex refuse les téléchargements faits par des scripts. Si le téléchargement échoue, le script explique comment enregistrer le fichier à la main depuis EUR-Lex.

## Chercher dans les textes

```powershell
.venv\Scripts\python scripts\build_index.py                          # construit l'index (environ 7 min la première fois)
.venv\Scripts\python scripts\search.py "Dois-je désigner un DPO ?"   # affiche les 5 passages les plus proches
.venv\Scripts\python scripts\evaluate_retrieval.py                   # mesure la qualité sur eval\questions_v0.jsonl
```

Chaque chunk est transformé en vecteur (**embedding**) par le modèle `bge-m3`, via Ollama, puis rangé dans une base [Chroma](https://www.trychroma.com) locale (`data/index/`). Une question est transformée de la même façon : les passages dont le vecteur est le plus proche (similarité cosinus) sont affichés avec leur score et leur lien EUR-Lex. L'index n'est recalculé que si `chunks.jsonl` ou le modèle changent. Le modèle et le matériel utilisé (carte graphique ou processeur) se règlent dans `.env`.

Un petit **lexique** ajoute à la question le vocabulaire juridique des mots courants (« mention d'information » → « informations à fournir à la personne concernée », « DPO » → « délégué à la protection des données »…). Une recherche hybride par mots-clés (BM25) a aussi été testée : moins bonne sur les questions de mesure, elle n'est pas activée (`SEARCH_MODE=vector`, `SEARCH_LEXICON=all` dans `.env`).

Un long article découpé en paragraphes pouvait occuper à lui seul les 5 passages et cacher un autre article utile. La recherche garde donc **au plus 2 passages d'un même article** (`SEARCH_MAX_PER_ARTICLE=2` dans `.env` ; vide = pas de limite).

`evaluate_retrieval.py` pose les 10 questions de `eval/questions_v0.jsonl` et indique, pour chacune, le rang du premier article attendu, puis le **hit@1** (l'article attendu arrive en premier) et le **hit@5** (il est dans les 5 premiers passages).

### Reformulation de la question et reclassement des passages (activés en mode distant seulement)

Deux étapes de recherche supplémentaires, décidées à la séance 7 ter (`eval/results_v6.md`) :

- **la reformulation** : le modèle ajoute à la question quelques termes juridiques avant la recherche (par exemple « marquage CE » pour « logo sur l'emballage d'un appareil »). Le code écarte tout terme qui contient une conclusion (« interdit », « autorisé », « obligatoire »…) ou un chiffre ;
- **le reclassement** : un **reranker** (**cross-encoder**) relit les 20 meilleurs passages trouvés et les reclasse selon leur pertinence par rapport à la question, avant de garder les 5 meilleurs. Le modèle est `BAAI/bge-reranker-v2-m3` (licence Apache-2.0), sur le processeur.

**Par défaut** (`SEARCH_REWRITE=auto` et `SEARCH_RERANK=auto`), les deux sont **activés en mode distant** et **désactivés en mode local**. Vous pouvez forcer `on` ou `off` dans `.env`. La reformulation n'est jamais activée seule par défaut : sans le reclassement, elle fait reculer certaines questions.

**Pourquoi en mode distant** : l'article attendu est trouvé pour 42 à 44 questions de réglage sur 49 au lieu de 36 (mesuré trois fois, sans recul). Sur les 58 questions relues par l'auteur, une première passe a donné 40 justes, 9 partielles, 9 fausses et aucune dangereuse (contre 38, 6, 13 et 1 sans ces étapes), mais une seconde passe sur 29 d'entre elles a donné 4 réponses dangereuses : **ces étapes améliorent la recherche ; rien ne montre qu'elles réduisent les réponses dangereuses**. Coût : environ 30 s par question au lieu de 4 s (le reclassement tourne sur votre ordinateur), et la question part une fois de plus chez Groq pour la reformulation (après le garde-fou des données personnelles).

**Pourquoi pas en mode local** : avec le petit modèle local, la recherche s'améliore aussi, mais **3 réponses deviennent dangereuses** (30 justes, 7 partielles, 16 fausses, 5 dangereuses, contre 26, 7, 18 et 7), et une question passe de 44 s à 74 s.

Le reclassement demande des bibliothèques supplémentaires (environ 1 Go : `torch`, `transformers`) et un modèle d'environ 2,3 Go, téléchargé une seule fois à la première utilisation :

```powershell
.venv\Scripts\python -m pip install -e .[rerank]   # torch et transformers (versions épinglées)
```

Sans ces bibliothèques, le copilote fonctionne normalement : en mode distant, il le signale et revient à la recherche sans reformulation ni reclassement.

## Poser une question

```powershell
.venv\Scripts\python scripts\ask.py "Dois-je désigner un DPO ?"
.venv\Scripts\python scripts\ask.py "Dois-je désigner un DPO ?" --show-passages   # montre aussi les passages lus par le modèle
```

Le copilote cherche les 5 passages les plus proches, numérotés [1] à [5]. Le modèle `qwen3:4b-instruct` recopie d'abord les phrases exactes des passages qui répondent (**extraits**), puis rédige sa réponse à partir de ces seules phrases, en citant les passages.

**Contrôle de pertinence** : un second appel court demande au modèle si les extraits retenus répondent **directement** à la question (OUI ou NON). Si c'est NON, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. », et les passages consultés restent affichés. Ce contrôle évite des réponses assurées alors que le bon article n'a pas été trouvé, mais il est imparfait : il laisse passer certaines erreurs et peut s'abstenir sur une réponse partiellement juste. Il se désactive avec `ANSWER_JUDGE=off` dans `.env`. Avec lui, la réponse s'affiche d'un bloc après le contrôle, et non au fil de l'écriture.

Le code, et non le modèle :
- **vérifie chaque extrait mot pour mot** dans le passage cité (seuls les espaces, le style des apostrophes et des guillemets, les majuscules et les coupures marquées « … » sont tolérés) ;
- **remplace la réponse par « Les textes trouvés ne permettent pas de répondre à cette question. »** si aucun extrait n'est vérifié : une réponse sans appui dans les textes n'est jamais affichée, même en partie ;
- affiche les extraits vérifiés, puis la liste des sources (règlement, article, titre, lien EUR-Lex, date de version), construite à partir des métadonnées ;
- signale un extrait introuvable, une citation sans extrait vérifié, une citation vers un passage inexistant ou une réponse coupée par la limite de longueur ;
- **garde de la place pour la réponse** : si le modèle recopie encore des extraits après 1 200 tokens (sur 2 000), le code arrête la recopie, garde les extraits complets et lui fait écrire sa réponse avec les tokens restants, puis le signale ; une réponse encore coupée se termine par « […] (réponse coupée : la limite de longueur a été atteinte) » ([`eval/results_v8.md`](eval/results_v8.md)) ;
- relit la réponse elle-même et signale :
  - si elle ne cite aucun passage [n], une phrase dont moins de 35 % des mots se retrouvent dans les extraits vérifiés ;
  - une phrase qui affirme une absence ou une impossibilité (« aucune obligation », « ne s'applique pas », « vous ne pouvez pas »…) alors qu'aucun extrait vérifié ne contient de négation ;
  - le tutoiement (« tu », « ton »…) : le copilote doit toujours vouvoyer ;
  - une condition ou une exception (« sauf si », « lorsque »…) dont la négation a été ajoutée ou retirée par rapport à l'extrait ;
  - un texte entre « » qui ne figure dans aucun extrait vérifié, et une exception reformulée sans reprendre les extraits ;
  - une liste de cas a), b), c)… reprise seulement en partie, sans le dire ;
  - une obligation qui vise un fournisseur, un importateur ou un distributeur, présentée sans nommer cet acteur ;
  - une phrase qui ne dit pas de quel règlement elle vient, quand la réponse mêle RGPD et AI Act ;
- ajoute l'avertissement « Information, pas un conseil juridique ».

Limite : vérifier un extrait prouve que la phrase existe dans la loi, pas qu'elle répond bien à la question. Ces contrôles sont de simples signaux, sans compréhension du sens : ils peuvent laisser passer une erreur ou signaler une phrase juste. La relecture humaine reste nécessaire.

Comptez environ 40 secondes par question (jusqu'à 1 min 45 pour les longues listes) avec une carte graphique de 4 Go, ordinateur branché sur secteur (sur batterie, Windows peut brider la carte graphique et une réponse peut prendre plusieurs minutes).

`scripts\answer_questions.py --version v3` pose les 10 questions de test et 2 questions hors sujet, puis enregistre les réponses brutes dans `eval/answers_v3.md` pour relecture (`eval/answers_v0.md` à `eval/answers_v2.md` gardent les versions précédentes). L'option `--questions` pose un autre fichier de questions, par exemple `--questions eval\questions_v1.jsonl --version heldout_v3`. Les mesures avant/après sont dans `eval/results_v1.md`.

### Relecture des réponses

Chaque version est relue par un humain avec la même grille, décrite dans `eval/rubric.md`, qui donne 4 verdicts : **juste**, **partiel**, **faux** ou **dangereux**. Une réponse est dangereuse si elle pourrait faire agir quelqu'un à tort, par exemple en inventant ou en niant une obligation. Les relectures sont enregistrées dans `eval/reviews/<version>.jsonl`, une ligne par question. Le script suivant en fait le tableau :

```powershell
.venv\Scripts\python scripts\review_summary.py --check
```

| Version | Juste | Partiel | Faux | Dangereux |
|---|---|---|---|---|
| v0 (séance 4) | 5 | 1 | 3 | 3 |
| v1 (séance 5) | 9 | 2 | 0 | 1 |
| v2 (séance 5 bis) | 6 | 5 | 0 | 1 |
| v3 (séance 5 ter) | 9 | 3 | 0 | 0 |

Ces chiffres portent sur les 12 questions qui ont servi à régler le système : ils sont donc optimistes. À l'examen final, sur 26 questions jamais vues, le modèle local obtient 9 justes, 2 partielles, 14 fausses et 1 dangereuse (section [Résultats](#résultats)).

## Résultats

Des mesures à lire ensemble : les **questions de réglage** ont servi à régler le copilote (elles sont donc optimistes) ; l'**examen final** (une seule passe) et l'**examen 2** (3 passes par mode, verdicts en moyenne) portent sur des questions qu'il n'avait jamais vues, sans rien changer pendant l'examen. Détail : [`eval/results_v5.md`](eval/results_v5.md) (examen final), [`eval/results_v6.md`](eval/results_v6.md) (séance 7 ter) et [`eval/results_v7.md`](eval/results_v7.md) (examen 2).

| | Recherche : article attendu dans les 5 passages (hit@5) | Verdicts, modèle local (juste / partiel / faux / dangereux) | Verdicts, mode distant (juste / partiel / faux / dangereux) |
|---|---|---|---|
| **Questions de réglage** (v0 et v1, 32 questions) | 26 / 27 | 17 / 5 / 4 / 6 | 25 / 5 / 2 / 0 |
| **Après la séance 7 ter : réglage sur toutes les questions connues** (v0, v1, v2, auteur : 58 questions, dont les 26 de l'examen, vues depuis) — *réglage, pas un examen* | local 36 / 49 · distant 44 / 49 | 26 / 7 / 18 / 7 (¹) | 40 / 9 / 9 / 0 (²) |
| **Examen final** (questions jamais vues, 26 questions) | **10 / 22** | **9 / 2 / 14 / 1** | **13 / 1 / 11 / 1** |
| **Examen 2 (28 questions neuves, 3 passes, moyennes)** | **local 15 / 24 · distant 19–20 / 24** | **6,0 / 2,0 / 13,7 / 6,3** | **13,3 / 2,0 / 11,7 / 1,0** |

(¹) Configuration locale inchangée par la séance 7 ter (reformulation et reclassement désactivés en local) : verdicts des mêmes réponses qu'avant. (²) Mode distant avec reformulation et reclassement, relu avec l'ancien exemple du prompt de reformulation ; le hit@5 de 44 / 49 est mesuré avec le nouvel exemple (42 / 49 avec l'ancien). **Une seconde passe sur 29 de ces questions, avec la même configuration, a donné 4 réponses dangereuses** (contre 0 sur les mêmes questions à la première passe) : les réponses varient d'une passe à l'autre ([`eval/results_v6.md`](eval/results_v6.md), section 6.5).

**Le mode local n'est pas fiable pour de vraies questions** (plusieurs réponses dangereuses par série de 28 : 6,3 en moyenne à l'examen 2). **Le mode distant donne de meilleurs résultats, mais des réponses dangereuses restent possibles** (1 en moyenne) : **vérifiez toujours les articles cités.**

**Seules les lignes « examen final » et « examen 2 » portent sur des questions jamais vues** au moment de l'examen (elles ont été vues depuis, à la relecture). La ligne « après la séance 7 ter » mesure des réglages faits en connaissant les questions de l'examen final : elle est optimiste.

Les 28 questions de l'examen 2 ont été écrites hors du projet, par un assistant qui ne le connaissait pas ; chaque question a été posée 3 fois dans chaque mode, et les cas décisifs ont été vérifiés à l'aveugle par un second relecteur. Presque toutes les réponses fausses sont des refus prudents, souvent alors que le bon article avait été trouvé ; les réponses dangereuses du mode local reviennent d'une passe à l'autre ([`eval/results_v7.md`](eval/results_v7.md), section 7).

À l'examen final, la plupart des réponses fausses sont des refus prudents (« les passages trouvés ne traitent pas directement de votre question ») : le bon article n'avait pas été trouvé. Il reste une réponse dangereuse dans chaque mode : une date d'application inventée (local) et des données pseudonymisées présentées comme sortant du RGPD (distant). Les questions d'examen ont été écrites par Claude, qui connaissait le projet : c'est une mesure honnête, mais pas un test sur de vraies questions d'utilisateurs.

## Limites connues

- **Les réponses varient d'une passe à l'autre ; des réponses dangereuses restent possibles dans les deux modes** (local et distant). La même question, avec la même configuration, peut recevoir une réponse juste puis une réponse dangereuse (`eval/results_v6.md`, section 6.5) : vérifiez toujours les articles cités.
- **Petit modèle local** : `qwen3:4b-instruct` (4 milliards de paramètres) tourne sur une carte de 4 Go, mais il se trompe encore. Les relectures humaines (`eval/review_v*.md`) ont trouvé une exception inversée, des cas oubliés dans une liste, une obligation du fournisseur présentée comme celle de l'utilisateur, deux analyses d'impact confondues et des fautes de frappe.
- **Extraits trop longs** : le modèle local recopie parfois une liste ou un paragraphe entier comme un seul extrait. Le code arrête alors la recopie pour que la réponse ait de la place (`eval/results_v8.md`). Mais le modèle a toujours le passage entier sous les yeux, et il peut encore appliquer une règle d'un autre paragraphe. Exemple à l'examen 2 (e17) : la vérification par deux personnes de l'AI Act, art. 14, § 5, réservée à l'identification biométrique, appliquée au tri de CV.
- **Contrôles automatiques imparfaits** : ils comparent des mots, sans comprendre le sens. Ils laissent passer des erreurs et signalent parfois des phrases justes. Une réponse sans alerte n'est pas une réponse garantie.
- **Extrait vérifié ≠ bonne réponse** : un extrait vérifié prouve que la phrase existe dans la loi, pas qu'elle répond à la question posée ni qu'elle s'applique à votre situation.
- **Relecture humaine nécessaire** : le copilote donne une information, pas un conseil juridique. Vérifiez toujours les articles cités sur EUR-Lex et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
- **Corpus limité** : seulement le RGPD et l'AI Act (articles et annexes, versions consolidées indiquées plus bas). Le corpus ne contient pas :
  - les considérants ;
  - le droit national, comme la loi Informatique et Libertés ;
  - les lignes directrices et la jurisprudence ;
  - les fiches CNIL, prévues mais pas encore intégrées.

  Les durées, montants et modalités concrètes viennent souvent de ces autres textes.
- **Décisions d'adéquation absentes** : le corpus ne contient pas les décisions de la Commission européenne qui reconnaissent qu'un pays hors de l'Union protège suffisamment les données. Le copilote ne peut donc pas dire si un pays donné en bénéficie : il explique la règle (RGPD, articles 45 et 46). Si le modèle affirme quand même qu'un pays nommé a ou n'a pas de décision d'adéquation, le code retire cette phrase de la réponse, ainsi que la phrase suivante si elle en tire la conséquence (« Par conséquent… », « Ainsi… »), les remplace par « [phrase retirée : le copilote ne peut pas savoir si ce pays bénéficie d'une décision d'adéquation] » et le signale. Ce contrôle compare des formes de phrases, sans comprendre le sens : il retire parfois aussi une phrase prudente et juste. Dès qu'une réponse cite les articles 44 à 49, le code ajoute un renvoi vers [la page de la Commission européenne sur les décisions d'adéquation](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en) (en anglais).
- **Recherche imparfaite** : c'est la principale faiblesse. À l'examen final, l'article attendu n'est dans les 5 passages que pour 10 questions sur 22 (contre 26 sur 27 sur les questions de réglage). Le copilote refuse alors le plus souvent de répondre, ce qui est sans danger mais sans réponse.
- **Lenteur** : comptez environ 40 secondes par réponse (contrôle de pertinence compris) avec une carte graphique de 4 Go ; les questions à longue liste dépassent la minute. C'est davantage sans carte graphique.
- **Sur-apprentissage** : le système a été réglé sur les questions de test. À l'examen final, sur des questions jamais vues, il obtient 9 justes sur 26 en local et 13 sur 26 en mode distant, avec 1 réponse dangereuse dans chaque mode (section [Résultats](#résultats), `eval/results_v5.md`).

## Mémoire de la carte graphique

Le modèle de génération se règle dans `.env` :

| Réglage | Valeur par défaut | Rôle |
|---|---|---|
| `LLM_NUM_CTX` | `8192` | Taille du contexte en tokens : passages + question + réponse |
| `LLM_NUM_GPU` | `99` | Couches du modèle placées sur la carte graphique (99 = toutes, le plus rapide) |
| `LLM_TEMPERATURE` | `0.1` | Basse : réponses plus stables et plus fidèles aux passages |
| `LLM_MAX_TOKENS` | `2000` | Longueur maximale (extraits + réponse), dont 800 tokens toujours gardés pour la réponse ; une réponse coupée est signalée et marquée « […] » |

Avec ces valeurs, `qwen3:4b-instruct` occupe 3,68 Go sur une carte de 4 Go (`ministral-3:3b` : 3,87 Go). Si le copilote affiche « Mémoire insuffisante », par exemple parce qu'une autre application utilise la carte graphique, essayez dans cet ordre :
1. baissez `LLM_NUM_CTX` à `6144` (mesuré : 3,39 Go avec qwen, 3,66 Go avec ministral) ou `4096` (3,10 Go avec qwen, 3,45 Go avec ministral) ;
2. baissez `LLM_NUM_GPU`, par exemple à `20` : une partie du modèle passe alors sur le processeur ;
3. laissez `LLM_NUM_GPU` vide : Ollama choisit lui-même, mais la réponse est environ 4 fois plus lente.

## Mode distant (optionnel)

**Le copilote est local par défaut** (`LLM_BACKEND=ollama`) : vos questions ne quittent pas votre ordinateur.

Depuis la séance 7, un **mode distant** est proposé en option : la rédaction et le contrôle de pertinence sont confiés à `qwen/qwen3.8-27b`, servi par le niveau gratuit de [Groq](https://groq.com) (API compatible OpenAI). La recherche dans les textes reste locale.

**Pourquoi ce modèle** (`eval/results_v3.md`, relecture de l'auteur sur les 32 questions de réglage) : 0 réponse dangereuse contre 6 pour le modèle local, 25 justes contre 17, et un temps médian par question de 4 s contre 39 s. À l'examen final, sur 26 questions jamais vues : 13 justes contre 9 et 1 réponse dangereuse dans chaque mode (`eval/results_v5.md`). Le modèle plus gros `openai/gpt-oss-120b` a aussi été essayé et n'a pas été retenu (3 réponses dangereuses, et des extraits non retrouvés mot pour mot).

**Ce qu'il faut savoir avant de l'activer :**
- En mode distant, la recherche ajoute par défaut la **reformulation de la question** et le **reclassement des passages** (voir [ci-dessus](#reformulation-de-la-question-et-reclassement-des-passages-activés-en-mode-distant-seulement)) : environ 30 s par question au lieu de 4 s, et `pip install -e .[rerank]` pour en profiter (sans quoi le copilote le signale et s'en passe).
- `qwen/qwen3.8-27b` est un modèle en **preview** chez Groq : il peut changer ou disparaître sans préavis (`llama-3.3-70b-versatile`, prévu au départ, a été retiré le 16/08/2026). Le copilote le dit alors clairement et propose de revenir au mode local.
- **Votre question et les extraits de loi sont envoyés à Groq.** Avant chaque réponse, une ligne le rappelle, et le modèle qui a rédigé la réponse est nommé sous celle-ci.
- **N'y mettez jamais de données personnelles** (nom, situation d'une personne, données de clients ou d'adhérents…). Un garde-fou, appliqué dans le cœur du copilote (`rag.answer_question`, donc pour toute interface, présente ou future), refuse d'envoyer une question qui contient une adresse e-mail, un numéro de téléphone, un IBAN ou un numéro de sécurité sociale français, par de simples expressions régulières (`src/compliance_copilot/privacy.py`). **Il ne détecte ni les noms ni les situations personnelles : c'est un filet de sécurité, pas une garantie.** En mode local, rien n'est bloqué, puisque rien ne sort de l'ordinateur.

**Ce que dit Groq de ses données** (page *Your Data in GroqCloud*, relue le 14/11/2026) : pas de conservation des requêtes par défaut ; des journaux (entrées et sorties) peuvent être gardés jusqu'à 30 jours pour la fiabilité et la lutte contre les abus, désactivables dans « Data Controls » ; l'option « Zero Data Retention » y est ouverte à tous ; les données conservées le sont aux États-Unis (Google Cloud). La page ne dit rien de l'entraînement des modèles.

**Limites du plan gratuit** (en-têtes de l'API, 15/11/2026) : 1 000 requêtes par jour, 8 000 tokens par minute, et 200 000 tokens par jour d'après la page des limites. Une question prend environ 4 500 tokens : le copilote attend quand la limite par minute est atteinte, et s'arrête proprement quand le quota du jour l'est.

**Activer le mode distant :**
1. créez une clé sur la console Groq et mettez-la dans `.env`, ligne `GROQ_API_KEY=…` (ce fichier est ignoré par Git ; jamais la clé ailleurs) ;
2. pour une question : `.venv\Scripts\python scripts\ask.py --backend openai "Dois-je tenir un registre des traitements ?"` (le modèle distant est `qwen/qwen3.8-27b` par défaut : `LLM_API_MODEL`, ou `--model` pour une seule question) ;
3. pour en faire le mode par défaut : `LLM_BACKEND=openai` dans `.env`, et rien d'autre (`LLM_MODEL` reste le modèle local, `LLM_API_REASONING_EFFORT` vide vaut `none` pour ce modèle).

| Réglage | Valeur | Rôle |
|---|---|---|
| `LLM_BACKEND` ou `--backend` | `ollama` (défaut) ou `openai` | Mode local ou distant |
| `LLM_API_MODEL` ou `--model` (en mode distant) | `qwen/qwen3.8-27b` (défaut) | Modèle distant ; `LLM_MODEL` reste le modèle local |
| `LLM_API_BASE_URL` | `https://api.groq.com/openai/v1` | Adresse de l'API |
| `LLM_API_KEY_ENV` | `GROQ_API_KEY` | **Nom** de la variable de `.env` qui contient la clé |
| `SEARCH_REWRITE` et `SEARCH_RERANK` | `auto` (défaut), `on` ou `off` | Reformulation et reclassement : `auto` = activés en mode distant, désactivés en mode local |
| `LLM_API_REASONING_EFFORT` | vide (`none` pour qwen3.8-27b) | Réglage `reasoning_effort` envoyé à l'API ; l'option `--reasoning-effort` n'existe que dans `answer_questions.py` et `check_api.py`, pas dans `ask.py` |

`scripts\check_api.py` fait un appel d'essai avec `LLM_API_MODEL` (ou `--model`) et affiche les modèles ouverts à votre clé et les limites réelles de votre compte. Avant chaque commit, `scripts\scan_secrets.py` vérifie qu'aucune clé n'est sur le point d'être publiée. Les fichiers de réponses de l'expérience (`eval/answers_*_big_*.md`) et sa comparaison (`scripts\compare_answers.py`) restent dans le dépôt.

## Sources juridiques

| Texte | Version consolidée utilisée | Contenu repris |
|---|---|---|
| [RGPD — règlement (UE) 2016/679](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504) | 4 mai 2016 (rectificatif de 2018 intégré) | 99 articles |
| [AI Act — règlement (UE) 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727) | 27 juillet 2026 (intègre le règlement (UE) 2026/1744, « omnibus numérique sur l'IA ») | 119 articles et 14 annexes |

Les considérants ne sont pas repris. Les fiches pratiques de la [CNIL](https://www.cnil.fr) viendront plus tard.

**Mention de source.** Source : EUR-Lex, https://eur-lex.europa.eu — © Union européenne, 1998-2026. Les textes consolidés sont réutilisés sous licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr), conformément à la [décision 2011/833/UE](https://eur-lex.europa.eu/eli/dec/2011/833/oj). Modifications apportées : découpage en extraits (articles, paragraphes, définitions, points d'annexe) et suppression des marques de consolidation (▼B, ▼M1, ►C1…). Les textes consolidés sont un outil de documentation : seul fait foi le texte publié au *Journal officiel de l'Union européenne*.

## Licence

MIT — voir [LICENSE](LICENSE).
