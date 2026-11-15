# Séance 7 — expérience : un modèle plus gros rédige-t-il mieux ?

Question posée : les erreurs restantes de la configuration v4 (relectures v0 = 8 justes / 2 partielles / 0 fausses / 2 dangereuses, v1 = 9 / 3 / 4 / 4) viennent-elles de la taille du modèle local `qwen3:4b-instruct` ?

**Seul le modèle qui rédige et qui juge change.** La recherche (`bge-m3` sur CPU, lexique, 5 passages, 2 par article au plus, 1er paragraphe), les passages (calculés pour un contexte de 8 192 tokens comme en local), le prompt, les contrôles du code, la température (0,1) et la limite de 2 000 tokens restent ceux de la v4.

**Aucun verdict de justesse ici** : il viendra de la relecture de l'auteur (grille `eval/rubric.md`). Ce document compare seulement ce que le code mesure.

## 1. Modèles et conditions

Le modèle prévu, `llama-3.3-70b-versatile`, a été retiré par Groq le 16/08/2026 pour les plans gratuit et développeur (annonce du 17/06/2026) ; il n'est pas dans la liste des modèles ouverts à la clé. Deux modèles ont été essayés, dans cet ordre, le 15/11/2026, par le niveau gratuit de Groq (API compatible OpenAI, `LLM_BACKEND=openai`) :

| Série | Modèle | Taille | Raisonnement | Statut chez Groq | Fichiers |
|---|---|---|---|---|---|
| `v4` (référence locale) | `qwen3:4b-instruct` (Q4_K_M, Ollama) | 4 milliards | aucun | — | `answers_v4.md`, `answers_heldout_v4.md` (26/10/2026) |
| `qwen27b` | `qwen/qwen3.8-27b` | 27 milliards, dense, même famille que le modèle local | `reasoning_effort=none` (désactivé) | **preview** le 15/11/2026 : peut changer ou disparaître | `answers_v4_big_qwen27b.md`, `answers_heldout_v4_big_qwen27b.md` |
| `gptoss` | `openai/gpt-oss-120b` | 120 milliards au total, **MoE avec 5,1 milliards de paramètres actifs** par token | `reasoning_effort=low` (le minimum : ce modèle raisonne toujours) | production | `answers_v4_big_gptoss.md`, `answers_heldout_v4_big_gptoss.md` |

Questions : `questions_v0.jsonl` (10) + `questions_offtopic_v0.jsonl` (2 hors sujet) + `questions_v1.jsonl` (17 + 3 hors sujet), soit 32 par modèle. `questions_v2.jsonl` et les questions de l'auteur n'ont été ni lues ni utilisées.

**Données** (page « Your Data in GroqCloud », relue le 14/11/2026) : pas de conservation des requêtes par défaut ; journaux de fiabilité et d'abus jusqu'à 30 jours, désactivables ; option Zero Data Retention ouverte à tous, activée par l'auteur ; stockage aux États-Unis. Seules les questions de test et les extraits de loi ont été envoyés : aucune donnée personnelle.

**Limites réelles du compte** (appel d'essai `scripts/check_api.py`, en-têtes `x-ratelimit-*`, identiques pour les deux modèles) : 1 000 requêtes par jour, 8 000 tokens par minute. Les tokens par jour ne sont pas dans les en-têtes : 200 000 d'après la page des limites. Les deux séries de 32 questions sont passées le même jour, chacune sous son quota (environ 150 000 tokens par modèle).

## 2. Déroulement

| Série | Début → fin | Attentes imposées par les 8 000 tokens/min (non comptées) | Incidents |
|---|---|---|---|
| `qwen27b` | 16:56 → 17:13 (16 min pour 32 questions) | 778 s sur 25 questions (47 attentes) | 2 réponses HTTP 503 passagères, réessayées après 2 s : q01 (appel du juge) et q18 (génération) |
| `gptoss` | 17:13 → 17:25 (11 min) | 551 s sur 30 questions (54 attentes) | aucun |

Les deux 503 sont revenus après environ 30 s : ce temps d'essai raté est compté dans « contrôle de pertinence » de q01 (30,2 s) et dans « génération » de q18 (31,5 s) de la série `qwen27b`. Depuis (commit `df968b0`), le temps d'un essai raté est compté à part, avec les attentes ; les fichiers de réponses n'ont pas été régénérés. Hors ces deux cas, la génération par l'API prend 1 à 5 s.

## 3. Comparaison (`scripts/compare_answers.py`)

| Série | Réponses données (sur 27) | Abstentions du juge | Hors sujet refusés (sur 5) | Extraits vérifiés / recopiés | Réponses coupées | Réponses avec alerte | Alertes | Mots par réponse (médiane) | Génération : médiane · max | Total : médian · max | Au-delà de 60 s |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `v4` | 25 | 2 (q22, q24) | 5 | 76 / 83 | 0 | 14 / 32 | 20 | 118 | 32 s · 77 s | 39 s · 89 s | 4 |
| `qwen27b` | 26 | 1 (q24) | 5 | **137 / 139** | 0 | **8 / 32** | 8 | 148 | 1 s · 32 s | 4 s · 38 s | 0 |
| `gptoss` | 20 | 4 (q10, q18, q22, q24) | 5 | 59 / 78 | 0 | 20 / 32 | 24 | 101 | 1 s · 5 s | 4 s · 8 s | 0 |

Le « total » est recherche + génération + juge, sans les attentes de l'API. La recherche locale prend 2 à 7 s dans tous les cas.

Alertes du code par type (nombre de réponses) :

| Alerte | `v4` | `qwen27b` | `gptoss` |
|---|---|---|---|
| Extrait(s) introuvable(s) mot pour mot dans le passage cité | 5 | 2 | 7 |
| Contrôle de pertinence (abstention) | 2 | 1 | 4 |
| Citation [n] sans extrait vérifié de ce passage | 3 | 0 | 4 |
| Texte entre « » introuvable dans les extraits | 1 | 2 | 3 |
| Extrait qui vise un fournisseur, sans le nommer | 2 | 1 | 1 |
| Aucun extrait vérifié : réponse remplacée par un refus | 0 | 0 | 3 (q11, q12, q15) |
| Affirmation d'absence sans extrait négatif | 1 | 1 | 1 |
| Exception reformulée | 3 | 0 | 0 |
| Règlement non nommé (RGPD et AI Act mêlés) | 1 | 1 | 1 |
| Négation ou règle inversée | 1 | 0 | 0 |
| Phrase sans citation, éloignée des extraits | 1 | 0 | 0 |

Par question (valeurs dans l'ordre `v4` · `qwen27b` · `gptoss`) :

| # | Extraits vérifiés | Refus | Alertes | Mots | Génération (s) | Total (s) |
|---|---|---|---|---|---|---|
| q01 | 2/2 · 5/5 · 2/2 | non · non · non | 0 · 0 · 0 | 149 · 114 · 99 | 47 · 1 · 2 | 55 · 38 · 4 |
| q02 | 2/2 · 5/6 · 2/2 | non · non · non | 0 · 1 · 0 | 107 · 174 · 62 | 28 · 1 · 1 | 37 · 4 · 4 |
| q03 | 1/1 · 2/2 · 2/2 | non · non · non | 0 · 0 · 0 | 89 · 116 · 84 | 22 · 1 · 1 | 28 · 4 · 4 |
| q04 | 3/4 · 13/13 · 4/6 | non · non · non | 1 · 0 · 1 | 273 · 164 · 95 | 77 · 2 · 2 | 89 · 5 · 5 |
| q05 | 2/2 · 4/4 · 1/2 | non · non · non | 0 · 0 · 2 | 108 · 105 · 96 | 31 · 1 · 1 | 38 · 4 · 4 |
| q06 | 3/6 · 6/6 · 3/3 | non · non · non | 1 · 0 · 0 | 142 · 241 · 83 | 46 · 2 · 2 | 52 · 6 · 4 |
| q07 | 5/5 · 6/6 · 2/2 | non · non · non | 1 · 0 · 0 | 195 · 184 · 131 | 49 · 3 · 2 | 59 · 5 · 5 |
| q08 | 1/1 · 1/1 · 1/1 | non · non · non | 1 · 1 · 1 | 40 · 71 · 41 | 34 · 1 · 2 | 40 · 4 · 4 |
| q09 | 2/2 · 6/6 · 3/3 | non · non · non | 0 · 0 · 1 | 81 · 129 · 159 | 33 · 2 · 2 | 39 · 4 · 5 |
| q10 | 2/3 · 5/5 · 5/5 | non · non · abstention | 3 · 0 · 1 | 164 · 177 · — | 42 · 2 · 2 | 51 · 5 · 5 |
| h01 | 0/0 · 0/0 · 0/0 | oui · oui · oui | 0 · 0 · 0 | — · — · — | 12 · 0 · 1 | 14 · 3 · 3 |
| h02 | 0/0 · 0/0 · 0/0 | oui · oui · oui | 0 · 0 · 0 | — · — · — | 19 · 0 · 1 | 21 · 3 · 3 |
| q11 | 5/5 · 6/6 · 0/2 | non · non · oui | 1 · 0 · 1 | 216 · 145 · — | 45 · 2 · 2 | 53 · 5 · 4 |
| q12 | 2/2 · 5/6 · 0/2 | non · non · oui | 2 · 1 · 1 | 118 · 81 · — | 31 · 1 · 2 | 38 · 4 · 4 |
| q13 | 1/1 · 4/4 · 2/2 | non · non · non | 0 · 0 · 1 | 62 · 97 · 103 | 26 · 1 · 1 | 32 · 4 · 4 |
| q14 | 4/4 · 6/6 · 3/3 | non · non · non | 1 · 0 · 1 | 122 · 246 · 174 | 32 · 2 · 2 | 39 · 4 · 4 |
| q15 | 2/2 · 6/6 · 0/4 | non · non · oui | 1 · 0 · 1 | 79 · 175 · — | 28 · 2 · 2 | 36 · 4 · 4 |
| q16 | 5/5 · 6/6 · 1/2 | non · non · non | 0 · 0 · 2 | 201 · 184 · 130 | 45 · 2 · 1 | 54 · 5 · 4 |
| q17 | 4/4 · 6/6 · 3/3 | non · non · non | 0 · 0 · 0 | 201 · 196 · 170 | 32 · 2 · 2 | 39 · 4 · 5 |
| q18 | 2/3 · 4/4 · 1/2 | non · non · abstention | 3 · 0 · 1 | 74 · 84 · — | 25 · 32 · 1 | 30 · 34 · 3 |
| q19 | 1/1 · 3/3 · 2/2 | non · non · non | 0 · 1 · 1 | 71 · 94 · 45 | 18 · 1 · 1 | 23 · 3 · 3 |
| q20 | 1/1 · 3/3 · 2/3 | non · non · non | 0 · 0 · 1 | 46 · 100 · 77 | 35 · 1 · 1 | 41 · 3 · 4 |
| q21 | 4/4 · 6/6 · 2/4 | non · non · non | 0 · 0 · 2 | 162 · 166 · 148 | 58 · 1 · 2 | 71 · 4 · 4 |
| q22 | 3/3 · 3/3 · 1/1 | abstention · non · abstention | 1 · 1 · 1 | — · 93 · — | 24 · 1 · 1 | 31 · 4 · 4 |
| q23 | 7/7 · 6/6 · 7/9 | non · non · non | 1 · 0 · 1 | 256 · 180 · 478 | 75 · 2 · 5 | 88 · 6 · 8 |
| q24 | 5/5 · 6/6 · 3/3 | abstention · abstention · abstention | 1 · 1 · 1 | — · — · — | 38 · 2 · 1 | 48 · 5 · 4 |
| q25 | 1/1 · 1/1 · 1/1 | non · non · non | 0 · 1 · 1 | 64 · 86 · 123 | 20 · 1 · 1 | 26 · 3 · 3 |
| q26 | 1/2 · 4/4 · 2/2 | non · non · non | 2 · 1 · 0 | 107 · 150 · 91 | 29 · 1 · 1 | 35 · 4 · 4 |
| q27 | 5/5 · 9/9 · 4/5 | non · non · non | 0 · 0 · 2 | 215 · 229 · 216 | 59 · 2 · 2 | 70 · 5 · 4 |
| h03 | 0/0 · 0/0 · 0/0 | oui · oui · oui | 0 · 0 · 0 | — · — · — | 38 · 0 · 0 | 40 · 3 · 2 |
| h04 | 0/0 · 0/0 · 0/0 | oui · oui · oui | 0 · 0 · 0 | — · — · — | 21 · 1 · 1 | 23 · 3 · 3 |
| h05 | 0/0 · 0/0 · 0/0 | oui · oui · oui | 0 · 0 · 0 | — · — · — | 19 · 1 · 0 | 21 · 3 · 3 |

## 4. Ce que le code voit (sans juger le fond)

**`qwen27b`** recopie presque tout mot pour mot (137 extraits vérifiés sur 139, contre 76 sur 83 en local), en recopie beaucoup plus (jusqu'à 13 pour q04, 9 pour q27 ; le prompt en demande 6 au plus) et déclenche deux fois moins d'alertes (8 réponses sur 32, contre 14). Ses réponses sont plus longues (148 mots médians contre 118). Il répond à q22 là où le juge local s'abstenait, et s'abstient comme le local sur q24 (art. 5 hors des passages avec le lexique neutre). Aucune réponse coupée.

**`gptoss`** répond à 20 questions sur 27 : 4 abstentions du juge (q10, q18, q22, q24) et **3 refus par le code** (q11, q12, q15), parce qu'aucun de ses extraits n'a été retrouvé mot pour mot. Ses textes bruts contiennent des caractères typographiques que les textes officiels n'ont pas : 33 traits d'union insécables (U+2011, « sous‑traitant ») et 145 espaces fines insécables (U+202F, devant « ; » et « : ») ; `qwen27b` n'en écrit aucun. En rejouant la vérification avec ces caractères ramenés à l'ASCII, q15 et q21 retrouvent chacune 2 extraits sur 4 ; cette tolérance n'a pas été ajoutée au code pendant l'expérience, pour ne pas changer la mesure en cours. Le raisonnement en réglage `low` reste court : 955 mots en tout sur 32 réponses (30 en moyenne, 91 au plus), toujours renvoyé dans le fichier, et **aucune réponse coupée** par la limite de 2 000 tokens. Ses réponses sont les plus courtes (101 mots médians), sauf q23 (478 mots).

**Vitesse** : par l'API, la rédaction prend 1 à 5 s au lieu de 18 à 77 s en local, mais la limite de 8 000 tokens par minute impose environ 25 s d'attente par question ; au total, 32 questions prennent 11 à 16 min contre environ 25 min en local. Le temps de la recherche locale est le même partout.

**Tokens écrits** (raisonnement compris pour `gptoss`) : 14 922 pour `qwen27b`, 14 111 pour `gptoss`.

## 5. Limites de la mesure

- Les verdicts (juste, partiel, faux, dangereux) ne sont pas ici : relecture de l'auteur à venir, dans `eval/reviews/v4_big_qwen27b.jsonl`, `heldout_v4_big_qwen27b.jsonl`, `v4_big_gptoss.jsonl` et `heldout_v4_big_gptoss.jsonl`.
- Un extrait vérifié prouve que la phrase existe, pas qu'elle répond à la question ; plus d'extraits ne veut pas dire une meilleure réponse.
- Les questions v1 ont servi au réglage du lexique à la séance 6 ; elles ne sont plus « jamais vues » pour la recherche, qui est la même pour les trois séries.
- `qwen/qwen3.8-27b` est un modèle en preview : les réponses datent du 15/11/2026 et pourraient ne pas être reproductibles plus tard.
- La vérification mot pour mot pénalise `gptoss` pour des caractères typographiques, pas pour le sens : à trancher avant toute conclusion sur ce modèle.
- Une seule passe par modèle (température 0,1) : la stabilité n'a pas été mesurée.

## 6. Relecture humaine (grille `eval/rubric.md`)

Verdicts de l'auteur, enregistrés tels quels dans `eval/reviews/v4_big_qwen27b.jsonl`, `heldout_v4_big_qwen27b.jsonl`, `v4_big_gptoss.jsonl` et `heldout_v4_big_gptoss.jsonl` (`scripts/review_summary.py --check` : 11 relectures cohérentes avec les réponses et les questions).

| Série | Questions | Juste | Partiel | Faux | Dangereux |
|---|---|---|---|---|---|
| v4 local, v0 (`v4`) | 12 | 8 | 2 | 0 | 2 |
| v4 local, v1 (`heldout_v4`) | 20 | 9 | 3 | 4 | 4 |
| **v4 local, total** | 32 | 17 | 5 | 4 | **6** |
| qwen3.8-27b, v0 (`v4_big_qwen27b`) | 12 | 12 | 0 | 0 | 0 |
| qwen3.8-27b, v1 (`heldout_v4_big_qwen27b`) | 20 | 13 | 5 | 2 | 0 |
| **qwen3.8-27b, total** | 32 | 25 | 5 | 2 | **0** |
| gpt-oss-120b, v0 (`v4_big_gptoss`) | 12 | 10 | 1 | 1 | 0 |
| gpt-oss-120b, v1 (`heldout_v4_big_gptoss`) | 20 | 8 | 2 | 7 | 3 |
| **gpt-oss-120b, total** | 32 | 18 | 3 | 8 | **3** |

Questions qui ne sont pas justes :
- qwen3.8-27b : partiel q12, q16, q22, q23, q27 · faux q18, q24.
- gpt-oss-120b : partiel q06, q14, q23 · faux q10, q11, q12, q15, q18, q22, q24, q25 · dangereux q16, q26, q27.

**Conclusion.** La taille du modèle aide beaucoup : avec les mêmes passages, le même prompt et les mêmes contrôles, `qwen3.8-27b` ne produit aucune réponse dangereuse, contre 6 pour le modèle local, et 25 réponses justes contre 17. Mais elle ne suffit pas : `gpt-oss-120b`, plus gros encore, produit 3 réponses dangereuses (q16, q26, q27) et 8 fausses, dont 3 refus dus à la vérification mot pour mot et 4 abstentions du juge.

**Trois problèmes de méthode, communs à tous les modèles**, à traiter chacun dans une PR séparée (rien n'est corrigé dans celle-ci) :

a) **La vérification mot pour mot échoue sur les caractères typographiques** (apostrophe ’, trait d'union insécable ‑, espaces insécables) : trois réponses de `gpt-oss-120b` (q11, q12, q15) sont remplacées par un refus alors que l'article répond.

b) **q24 donne une abstention avec les trois modèles** : le problème est dans la recherche des passages (l'art. 5, § 1, f n'est pas dans les 5 passages avec le lexique neutre) ou dans le juge, pas dans le modèle qui rédige.

c) **L'adéquation des États-Unis dépend d'un texte absent du corpus** (décision d'exécution (UE) 2023/1795, Data Privacy Framework) : `qwen3.8-27b` reste partiel sur q16 faute de pouvoir le dire, et `gpt-oss-120b` affirme le contraire (dangereux).
