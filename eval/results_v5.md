# Examen final — questions_v2 et questions de l'auteur

L'examen final mesure la configuration retenue sur des questions qui n'ont servi à aucun réglage : `eval/questions_v2.jsonl` (20 questions, figées au commit `65ee0c4`, ni lues ni utilisées avant cet examen) et `eval/questions_author.jsonl` (6 questions). **Lancé le 17/11/2026 en une seule passe (sections 2 à 5) ; relecture de l'auteur à venir : aucun verdict ici.**

## 0. Configuration figée (écrite le 17/11/2026, avant tout lancement)

**Règle de l'examen** (décision de l'auteur) : **une seule passe**. Aucun changement du code, du prompt ou du lexique après avoir vu une réponse ou un résultat. Un problème remarqué est noté ici « observé, non corrigé », sans être corrigé.

**Code** : `main` au commit `029e543` (fusion de la PR #15). La branche `eval/questions-author` (commit `93bf498` au moment du lancement) n'y ajoute que `eval/` et `CLAUDE.md` : aucune différence dans `src/` ni `scripts/` (`git diff main..HEAD` hors `eval/` et `CLAUDE.md` : vide).

| Élément | Valeur |
|---|---|
| Recherche | `bge-m3` (Ollama, digest `790764642607`, F16) sur CPU ; mode « vector » ; lexique « all » (19 entrées, empreinte `f38616b38e27`) ; 5 passages ; 2 au plus par article ; 1er paragraphe d'un article découpé ajouté ; **reranker désactivé** (`SEARCH_RERANK=off`) |
| Index | Chroma 1.5.9, 763 morceaux, construit le 24/10/2026 avec `bge-m3` |
| Modèle local | `qwen3:4b-instruct` (Ollama 0.40.16, digest `0edcdef34593`, Q4_K_M), `LLM_NUM_CTX=8192`, `LLM_NUM_GPU=99`, température 0,1, 2 000 tokens au plus |
| Modèle distant | `qwen/qwen3.8-27b` (Groq, niveau gratuit, `reasoning_effort=none` par défaut), mêmes passages, même prompt, mêmes contrôles |
| Prompt | `SYSTEM_PROMPT` de `rag.py`, 4 339 caractères, empreinte `dba634523517` (règles 1 à 12, dont la règle 12 sur les décisions d'adéquation) |
| Juge | `ANSWER_JUDGE=on`, `JUDGE_PROMPT` empreinte `d40a5ebc2131` |
| Contrôles du code | vérification mot pour mot des extraits, alertes de la v4, note fixe d'adéquation (art. 44 à 49 du RGPD cités) et retrait des phrases sur l'adéquation d'un pays, avec sa phrase de conséquence |
| Machine | Python 3.13.2 ; sur secteur à la préparation (`BatteryStatus` = 2), à revérifier avant et après chaque lot |

**Déroulé prévu** : (1) recherche, `evaluate_retrieval.py --questions` sur `questions_v2.jsonl` puis `questions_author.jsonl` (hit@1, hit@5, niveaux article et paragraphe) ; (2) réponses locales, `answer_questions.py --questions … --version final_local_v2` et `final_local_author` ; (3) réponses distantes, `--backend openai`, versions `final_remote_v2` et `final_remote_author` ; (4) mesures du code (`compare_answers.py`), sans verdict.

## 1. Questions de l'auteur (`eval/questions_author.jsonl`)

**Provenance : questions écrites par Claude Code à la demande de l'auteur, qui l'a choisi ; Claude Code connaissait le projet (lexique, points faibles q16 et q24) : biais possible.**

Écrites le 17/11/2026, dans la persona d'un responsable de petite entreprise ou d'association, avec des mots simples et sans citer d'article. Sujets choisis pour ne pas reprendre ceux de v0 et v1 ; le recouvrement avec `questions_v2.jsonl` n'a pas pu être vérifié par Claude, qui ne lit pas ce fichier (le test `test_author_questions_are_well_formed_if_present` vérifie seulement que les identifiants diffèrent de ceux de tous les autres fichiers).

Articles attendus fixés en **lisant le texte du corpus** (`data/processed/chunks.jsonl`), jamais avec la recherche ni le modèle. **Validés par l'auteur**, avec deux voisins ajoutés à sa demande : AI Act art. 113 pour a03 (vérifié dans le texte consolidé du corpus : art. 113, c), i), obligations des systèmes à haut risque de l'annexe III à partir du 2 décembre 2027) et RGPD art. 28 pour a04 (l'éditeur de l'outil est sous-traitant : garanties, § 1, et contrat, § 3).

| Id | Question | Articles attendus | Voisins utiles | Couverture |
|---|---|---|---|---|
| a01 | J'ai 12 salariés et je voudrais remplacer la badgeuse par une pointeuse à empreinte digitale. J'ai le droit ? | RGPD art. 9, § 1 et § 2 | art. 4, point 14 ; art. 9, § 4 | partiel |
| a02 | Un partenaire commercial me propose de racheter notre fichier clients. Est-ce que je peux le lui vendre ? | RGPD art. 6, § 1 et art. 5 | art. 6, § 4 ; art. 13 ; art. 14, § 1 ; art. 21 | partiel |
| a03 | Je pense acheter un logiciel d'IA qui note les résultats de mes commerciaux et propose qui mérite une prime. Qu'est-ce que je dois savoir avant de l'utiliser ? | AI Act annexe III, point 4 ; art. 26, § 7 | art. 26, § 1 et § 2 ; art. 6, § 3 ; art. 4 ; art. 86 ; **art. 113** ; RGPD art. 22 | complet |
| a04 | Pendant nos réunions, un outil d'IA enregistre la discussion et rédige le compte rendu tout seul. Est-ce que je dois prévenir les participants ? | RGPD art. 13 et art. 6, § 1 | art. 5 ; art. 21 ; **art. 28, § 1 et § 3** ; AI Act art. 4 | partiel |
| a05 | On veut publier sur notre site et sur Facebook les photos de la fête de l'association, où l'on voit des adhérents et leurs enfants. Faut-il leur demander la permission ? | RGPD art. 6, § 1 et art. 7 | art. 4, point 1 ; art. 8 ; art. 13 ; art. 17 ; art. 21 | partiel |
| ha01 | Combien de jours de congés payés a un salarié à temps partiel ? | aucun (hors sujet) | — | hors corpus |

Les justifications détaillées (points et paragraphes, ce qui manque au corpus) sont dans le champ `note` de chaque question.

## 2. Recherche (`evaluate_retrieval.py`, 17/11/2026, sur secteur)

Configuration figée (section 0), une seule mesure. Rang cherché parmi les 20 premiers passages ; les questions hors sujet (h06, h07, h08, ha01) ne sont pas comptées.

| Jeu | Questions | hit@1 article | hit@5 article | hit@8 article | hit@1 paragraphe | hit@5 paragraphe | hit@8 paragraphe |
|---|---|---|---|---|---|---|---|
| `questions_v2` | 17 (+ 3 hors sujet) | 8/17 | **10/17** | 12/17 | 8/17 | **10/17** | 12/17 |
| `questions_author` | 5 (+ 1 hors sujet) | 0/5 | **0/5** | 0/5 | 0/5 | **0/5** | 0/5 |

(Une seule question de v2, q39, précise un paragraphe : article au rang 2, définition 5 au rang 3. Le hit@1 au niveau du paragraphe est lu sur les rangs question par question.)

Pour mémoire, sur les questions qui ont servi au réglage : v0 hit@5 10/10, v1 hit@5 16/17 (article) et 15/17 (paragraphe).

Rang de l'article attendu, question par question :

| Question | Article attendu | Rang |
|---|---|---|
| q28 rectification d'une adresse | RGPD art. 16 | 1 |
| q29 exactitude contestée, utilisation pendant la vérification | RGPD art. 18 | 20 |
| q30 refus automatique par un score | RGPD art. 22 | 1 |
| q31 application mobile dès la conception | RGPD art. 25 | 1 |
| q32 fichier géré à deux associations | RGPD art. 26 | 1 |
| q33 fichier de prospects acheté | RGPD art. 14 | 2 |
| q34 caméras dans l'atelier | RGPD art. 88 | non trouvé |
| q35 guide de bonnes pratiques d'une fédération | RGPD art. 40 | 1 |
| q36 plainte à la CNIL et recours | RGPD art. 77 | 6 |
| q37 réparation après une fuite | RGPD art. 82 | 6 |
| q38 extrait de casier judiciaire des bénévoles | RGPD art. 10 | 13 |
| q39 noms remplacés par des numéros | RGPD art. 4, définition 5 | 2 (déf. 5 au rang 3) |
| q40 IA à haut risque qui attribue les tâches | AI Act art. 26 | 1 |
| q41 IA qui note les examens | AI Act annexe III, point 3 | 1 |
| q42 candidat refusé qui demande pourquoi | AI Act art. 86 | 18 |
| q43 mesures pour les PME | AI Act art. 62 | 1 |
| q44 date des obligations à haut risque | AI Act art. 113 | non trouvé |
| a01 pointeuse à empreinte digitale | RGPD art. 9, § 1 ou § 2 | non trouvé |
| a02 vente du fichier clients | RGPD art. 6, § 1 ou art. 5 | 12 |
| a03 IA qui note les commerciaux | AI Act annexe III, point 4 ou art. 26, § 7 | 9 |
| a04 IA qui enregistre les réunions | RGPD art. 13 ou art. 6, § 1 | non trouvé |
| a05 photos de la fête | RGPD art. 6, § 1 ou art. 7 | 10 |

**Observé, non corrigé** (règle de l'examen) :

- **Questions de l'auteur : 0 sur 5.** La recherche part vers des passages qui partagent les mots de la question sans y répondre : pour a01, AI Act art. 48 et RGPD art. 20 et 22 (aucune entrée de lexique ne traduit « empreinte digitale » ou « pointeuse » en « données biométriques ») ; pour a04, AI Act art. 12 (« enregistrement ») et art. 75 ; pour a03, AI Act art. 50, § 1 et art. 6 avant l'annexe III, point 4 (rang 9) ; pour a02 et a05, des passages voisins (annexe VIII de l'AI Act, RGPD art. 35 et 8) avant les articles de base 5, 6 et 7. Ce sont des questions de « principe » (base légale, consentement, information) dont les articles généraux sont peu ressemblants aux mots de la question.
- **q34** (caméras) et **q38** (casier judiciaire) partent vers l'AI Act (art. 75 bis, art. 5, art. 60 et 61) ; **q44** (date d'application) ne trouve pas l'art. 113 dans les 20 premiers passages, la question ressemblant davantage à l'annexe III et à l'art. 2 ; **q42** trouve l'art. 86 au rang 18, après l'annexe III.
- Les deux jeux d'examen sont nettement moins bien servis que v0 et v1, sur lesquels la recherche a été réglée : c'est le sur-apprentissage annoncé (CLAUDE.md, README).

### 2.1 Vérification demandée par l'auteur : le 0/5 des questions de l'auteur n'est pas un bug de mesure

Calcul refait pas à pas (script temporaire, mêmes fonctions que `evaluate_retrieval.py` : `load_questions`, `article_level`, `matches`, `first_hit_rank`, et même recherche avec les réglages de `.env`), en cherchant cette fois jusqu'au rang 60. Cinq recherches lancées pendant les réponses locales.

- **Lecture du fichier correcte** : les articles attendus sont lus comme des listes, identiques au fichier ; chacun correspond à des morceaux existants du corpus (par exemple `gdpr:art_9:par_2` → `gdpr:art_9:par_2_a-i` et `gdpr:art_9:par_2_j`).
- **Rangs confirmés** : aucun outil de mesure à corriger.

| Question | Article attendu (niveau article) | 10 premiers passages | Rang (20 premiers) | Rang jusqu'à 60 |
|---|---|---|---|---|
| a01 | RGPD art. 9 | AI Act art. 48 ; RGPD art. 20, 22, 47 § 2, 42 ; AI Act art. 63 ; AI Act art. 5 § 2 et § 1 a-e ; RGPD art. 15, 17 | non trouvé | **non trouvé** |
| a02 | RGPD art. 6 ou art. 5 | AI Act annexe VIII ×2 ; RGPD art. 48 ; AI Act art. 72 ; RGPD art. 47 § 2 et § 1, 30 ; AI Act art. 4 bis ; RGPD art. 15 ; AI Act art. 78 § 3 | 12 | 12 |
| a03 | AI Act annexe III, point 4 ou art. 26 | AI Act art. 50 § 1 ; art. 6 point d, § 4, § 1 ; annexe III point 8 ; art. 50 § 2 ; art. 75 ×2 ; **annexe III point 4 (rang 9)** ; art. 72 | 9 | 9 |
| a04 | RGPD art. 13 ou art. 6 | AI Act art. 12 ; art. 75 ×2 ; art. 50 § 1 et § 2 ; art. 9 § 2 et § 1 ; art. 75 quater ×2 ; art. 56 § 5 | non trouvé | **non trouvé** |
| a05 | RGPD art. 6 ou art. 7 | RGPD art. 35 § 9 et § 1 ; art. 8 ; art. 12 § 1 ; art. 40 § 2 et § 1 ; art. 91 ; art. 64 § 2 ; art. 12 § 5 ; **art. 7 (rang 10)** | 10 | 10 |

**0/5 est réel.**

**Observé, non corrigé** (règle de l'examen) :

- **Faux ami du lexique** : pour a04, l'entrée `registre` (sans limite de mot) se déclenche sur « en**registre** » et ajoute « registre des activités de traitement » à la question ; la recherche part vers l'art. 12 de l'AI Act (enregistrement des journaux) et l'art. 30 du RGPD n'aide pas non plus.
- Pour a01, aucune entrée ne traduit « empreinte digitale » ou « pointeuse » ; seule « salariés » → « personne concernée » s'ajoute, ce qui n'oriente pas vers les données biométriques (art. 9 absent des 60 premiers).
- Pour a03, aucune entrée ne se déclenche (« commerciaux », « prime » et « note » ne sont pas dans le lexique).

## 3. Réponses locales (`qwen3:4b-instruct`), sans retouche

`eval/answers_final_local_v2.md` (20 questions) et `eval/answers_final_local_author.md` (6 questions), produites le 17/11/2026 entre 23:09 et 23:37 par `answer_questions.py --questions … --version final_local_v2` puis `final_local_author`.

**Alimentation** : `BatteryStatus` = 2 (secteur) au lancement à 23:09, puis **1 (batterie)** entre les deux fichiers (23:27) et à la fin (23:37). D'après la vitesse de génération question par question, le passage sur batterie a eu lieu **vers q34** : 32 à 35 tokens/s de q28 à q33, puis 15 à 26 tokens/s de q34 à h08, et 5,5 à 18 tokens/s pour les questions de l'auteur (a03 : 228 s de génération).

**Observé, non corrigé** (règle de l'examen : une seule passe, rien n'est régénéré) : le **contenu** des réponses ne dépend pas de la vitesse (mêmes passages, même modèle, température 0,1) ; les **temps** de q34 à h08 et de toutes les questions de l'auteur ne sont pas représentatifs. Les 5 recherches de vérification de la section 2.1 ont tourné pendant ce lot, vers q41-q42, après la baisse de vitesse : elles n'en sont pas la cause.

## 4. Réponses distantes (`qwen/qwen3.8-27b`, Groq), sans retouche

`eval/answers_final_remote_v2.md` (20 questions) et `eval/answers_final_remote_author.md` (6 questions), produites le 17/11/2026 entre 23:41 et 23:51 par `answer_questions.py --backend openai --questions … --version final_remote_v2` puis `final_remote_author` (modèle `LLM_API_MODEL` par défaut, `reasoning_effort=none`). **Sur secteur du début à la fin** (`BatteryStatus` = 2 avant, entre les deux fichiers et après ; l'attente a démarré sur batterie et le lot n'a été lancé qu'une fois le secteur détecté). Aucun arrêt par quota. Seules les questions d'examen et des extraits de loi ont été envoyés à l'API.

## 5. Mesures du code (`compare_answers.py`), sans verdict

| Série | Questions | Réponses données | Abstentions du juge | Refus (aucun extrait vérifié) | Hors sujet refusés | Extraits vérifiés / recopiés | Réponses avec alerte | Mots (médiane) | Total par question : médian · max |
|---|---|---|---|---|---|---|---|---|---|
| local, v2 | 17 + 3 hors sujet | 9 / 17 | 8 | 0 | 3 / 3 | 49 / 50 | 11 / 20 | 101 | 47 s · 111 s (*) |
| distant, v2 | 17 + 3 hors sujet | 11 / 17 | 2 | 4 | 3 / 3 | 52 / 54 | 4 / 20 | 138 | 4 s · 5 s (+ 411 s d'attente des limites sur 15 questions, non comptée) |
| local, auteur | 5 + 1 hors sujet | 2 / 5 | 3 | 0 | 1 / 1 | 18 / 19 | 4 / 6 | 130 | 100 s · 248 s (*) |
| distant, auteur | 5 + 1 hors sujet | 0 / 5 | 4 | 1 | 1 / 1 | 14 / 14 | 4 / 6 | — | 4 s · 4 s (+ 135 s d'attente sur 4 questions) |

(*) Temps faussés à partir de q34 et pour toutes les questions de l'auteur (passage sur batterie, section 3).

Aucune réponse coupée. **Note fixe d'adéquation : 0** (aucune réponse ne cite les art. 44 à 49 du RGPD) ; **phrase retirée : 0**.

Alertes du code, par type (nombre de réponses) :

| Alerte | local v2 | distant v2 | local auteur | distant auteur |
|---|---|---|---|---|
| Contrôle de pertinence (abstention du juge) | 8 | 2 | 3 | 4 |
| Texte entre « » introuvable dans les extraits vérifiés | 1 | 2 | 0 | 0 |
| Absence ou impossibilité affirmée sans extrait | 1 | 0 | 0 | 0 |
| Citation [n] sans extrait vérifié | 1 | 0 | 0 | 0 |
| Obligation d'un autre acteur | 0 | 0 | 1 | 0 |
| Extrait introuvable mot pour mot | 0 | 1 | 0 | 0 |

**Ce que la réponse affichée a fait, selon que l'article attendu était ou non parmi les 5 passages** (lecture des fichiers, pas un verdict) :

| | Article attendu dans les passages | Article attendu absent des passages |
|---|---|---|
| local, v2 | 10 questions : 7 réponses (q28, q31, q32, q35, q39, q40, q43), **3 abstentions** (q30, q33, q41) | 7 questions : 5 abstentions (q29, q34, q37, q38, q42), **2 réponses** (q36, q44) |
| distant, v2 | 10 questions : **10 réponses** | 7 questions : 2 abstentions (q29, q42), 4 refus (q34, q37, q38, q44), **1 réponse** (q36) |
| local, auteur | 0 question | 5 questions : 3 abstentions, **2 réponses** (a04, a05) |
| distant, auteur | 0 question | 5 questions : 4 abstentions, 1 refus |

**Observé, non corrigé** (règle de l'examen) :

- **Le juge local s'abstient alors que l'article attendu est dans les passages** pour q30 (art. 22, passage [1]), q33 (art. 14, passage [2]) et q41 (annexe III, point 3, passage [1]) ; le modèle distant répond à ces trois questions. Même limite que celle vue à la séance 7 bis (juge local instable, `results_v4.md`, section 2.3).
- **Réponses données sans l'article attendu** : en local q36, q44, a04 et a05 ; en distant q36. Ce sont les cas à risque à regarder en premier dans la relecture.
- Le modèle distant ne répond à aucune des 5 questions de l'auteur (4 abstentions, 1 refus) : la recherche ne lui a fourni l'article attendu pour aucune (section 2).
