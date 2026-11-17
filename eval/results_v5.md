# Examen final — questions_v2 et questions de l'auteur

L'examen final mesure la configuration retenue sur des questions qui n'ont servi à aucun réglage : `eval/questions_v2.jsonl` (20 questions, figées au commit `65ee0c4`, ni lues ni utilisées avant cet examen) et `eval/questions_author.jsonl` (6 questions). **Il n'est pas encore lancé.**

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
