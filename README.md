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
| v3 (séance 5 ter) | 10 | 2 | 0 | 0 |

Ces chiffres portent sur les 12 questions qui ont servi à régler le système : ils sont donc optimistes. Un examen final de 20 nouvelles questions (`eval/questions_v2.jsonl`) est mis de côté et ne sera utilisé qu'à la fin du projet.

## Limites connues

- **Petit modèle local** : `qwen3:4b-instruct` (4 milliards de paramètres) tourne sur une carte de 4 Go, mais il se trompe encore. Les relectures humaines (`eval/review_v*.md`) ont trouvé une exception inversée, des cas oubliés dans une liste, une obligation du fournisseur présentée comme celle de l'utilisateur, deux analyses d'impact confondues et des fautes de frappe.
- **Contrôles automatiques imparfaits** : ils comparent des mots, sans comprendre le sens. Ils laissent passer des erreurs et signalent parfois des phrases justes. Une réponse sans alerte n'est pas une réponse garantie.
- **Extrait vérifié ≠ bonne réponse** : un extrait vérifié prouve que la phrase existe dans la loi, pas qu'elle répond à la question posée ni qu'elle s'applique à votre situation.
- **Relecture humaine nécessaire** : le copilote donne une information, pas un conseil juridique. Vérifiez toujours les articles cités sur EUR-Lex et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
- **Corpus limité** : seulement le RGPD et l'AI Act (articles et annexes, versions consolidées indiquées plus bas). Le corpus ne contient pas :
  - les considérants ;
  - le droit national, comme la loi Informatique et Libertés ;
  - les lignes directrices et la jurisprudence ;
  - les fiches CNIL, prévues mais pas encore intégrées.

  Les durées, montants et modalités concrètes viennent souvent de ces autres textes.
- **Recherche imparfaite** : le passage utile n'est pas toujours parmi les 5 retenus. Par exemple, l'art. 32 (sécurité) n'est pas trouvé pour une des questions de test.
- **Lenteur** : comptez environ 40 secondes par réponse (contrôle de pertinence compris) avec une carte graphique de 4 Go ; les questions à longue liste dépassent la minute. C'est davantage sans carte graphique.
- **Sur-apprentissage** : le système a été réglé sur les questions de test. Sur des questions qu'il n'avait jamais vues, la version de la séance 5 ter n'avait que 6 réponses justes sur 20, dont 4 dangereuses (`eval/results_v2.md`). Seul l'examen final, mis de côté, mesurera honnêtement la version actuelle.

## Mémoire de la carte graphique

Le modèle de génération se règle dans `.env` :

| Réglage | Valeur par défaut | Rôle |
|---|---|---|
| `LLM_NUM_CTX` | `8192` | Taille du contexte en tokens : passages + question + réponse |
| `LLM_NUM_GPU` | `99` | Couches du modèle placées sur la carte graphique (99 = toutes, le plus rapide) |
| `LLM_TEMPERATURE` | `0.1` | Basse : réponses plus stables et plus fidèles aux passages |
| `LLM_MAX_TOKENS` | `2000` | Longueur maximale (extraits + réponse) ; une réponse coupée est signalée |

Avec ces valeurs, `qwen3:4b-instruct` occupe 3,68 Go sur une carte de 4 Go (`ministral-3:3b` : 3,87 Go). Si le copilote affiche « Mémoire insuffisante », par exemple parce qu'une autre application utilise la carte graphique, essayez dans cet ordre :
1. baissez `LLM_NUM_CTX` à `6144` (mesuré : 3,39 Go avec qwen, 3,66 Go avec ministral) ou `4096` (3,10 Go avec qwen, 3,45 Go avec ministral) ;
2. baissez `LLM_NUM_GPU`, par exemple à `20` : une partie du modèle passe alors sur le processeur ;
3. laissez `LLM_NUM_GPU` vide : Ollama choisit lui-même, mais la réponse est environ 4 fois plus lente.

## Sources juridiques

| Texte | Version consolidée utilisée | Contenu repris |
|---|---|---|
| [RGPD — règlement (UE) 2016/679](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504) | 4 mai 2016 (rectificatif de 2018 intégré) | 99 articles |
| [AI Act — règlement (UE) 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727) | 27 juillet 2026 (intègre le règlement (UE) 2026/1744, « omnibus numérique sur l'IA ») | 119 articles et 14 annexes |

Les considérants ne sont pas repris. Les fiches pratiques de la [CNIL](https://www.cnil.fr) viendront plus tard.

**Mention de source.** Source : EUR-Lex, https://eur-lex.europa.eu — © Union européenne, 1998-2026. Les textes consolidés sont réutilisés sous licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr), conformément à la [décision 2011/833/UE](https://eur-lex.europa.eu/eli/dec/2011/833/oj). Modifications apportées : découpage en extraits (articles, paragraphes, définitions, points d'annexe) et suppression des marques de consolidation (▼B, ▼M1, ►C1…). Les textes consolidés sont un outil de documentation : seul fait foi le texte publié au *Journal officiel de l'Union européenne*.

## Licence

MIT — voir [LICENSE](LICENSE).
