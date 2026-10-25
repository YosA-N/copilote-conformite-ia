# Résultats des séances 5 et 5 bis — avant / après

Séance 5 : sections 1 à 6. Séance 5 bis (corrections après la relecture `eval/review_v1.md`) : section 7, et colonne « séance 5 bis » de la section 5.

Toutes les mesures sont produites par les scripts du dépôt. Les questions `eval/questions_v1.jsonl` ont été écrites et commitées (`c57bc66`) **avant** toute amélioration : elles servent seulement à mesurer, on ne règle rien dessus. Les questions v0 servent, elles, à diagnostiquer et à régler.

## 1. Mesure de départ (recherche par vecteurs seuls, avant toute amélioration)

Commande : `scripts/evaluate_retrieval.py --questions …` (rang cherché parmi les 20 premiers passages ; les questions hors sujet ne sont pas comptées).

| Jeu de questions | hit@1 | hit@5 |
|---|---|---|
| v0 (10 questions) | 6/10 | 7/10 |
| v1 (17 questions + 3 hors sujet) | 9/17 | 11/17 |

Échecs de départ sur v1 (rang du premier article attendu) : q14 prospection (non trouvé), q15 sous-traitant (6), q16 hébergeur aux États-Unis (6), q18 données de santé (non trouvé), q21 sécurité (non trouvé), q24 émotions au travail (9).

**Variabilité constatée ensuite** : les vecteurs des questions, calculés par Ollama sur le processeur, varient très légèrement d'un lancement à l'autre. Pour q16, l'article attendu (art. 46, similarité 0,4746) et l'art. 49 de l'AI Act (0,4794) peuvent s'échanger : le hit@5 de départ sur v1 vaut **11 ou 12/17** selon le lancement (11, 12, 11 sur trois lancements séparés). La configuration retenue (section 2) a donné le même résultat sur trois lancements séparés.

## 2. Recherche

Commande : `scripts/compare_retrieval.py --repeat 3` (même lancement, trois mesures identiques).

| Configuration | v0 hit@1 | v0 hit@5 | v1 hit@1 | v1 hit@5 |
|---|---|---|---|---|
| vecteurs seuls (départ) | 6/10 | 7/10 | 9/17 | 12/17 (11–12 selon le lancement) |
| **vecteurs + lexique (retenu)** | **7/10** | **9/10** | **10/17** | **13/17** |
| hybride (vecteurs + BM25, fusion RRF) | 5/10 | 5/10 | 7/17 | 10/17 |
| hybride + lexique (mots-clés seulement) | 8/10 | 9/10 | 8/17 | 9/17 |
| hybride + lexique (partout) | 8/10 | 10/10 | 8/17 | 8/17 |

**Règle fixée avant la mesure** : garder un changement seulement si, sur v0 comme sur v1, le hit@5 ne baisse pas et au moins une mesure monte.

- **Lexique (vecteurs + lexique) : retenu.** Il améliore les deux jeux. Ses entrées viennent uniquement des échecs de v0, des exemples donnés au départ et des sigles courants (voir `src/compliance_copilot/lexicon.py`). Transparence : il a été écrit après avoir vu la mesure de départ de v1, mais aucune entrée ne vient d'une question v1. Deux entrées générales (clients, adhérents, bénévoles, salariés → « personne concernée » ; PME, entreprise, association → « responsable du traitement ») viennent des mots de v0 et touchent aussi v1.
- **Recherche hybride (BM25 + RRF) : rejetée.** Elle fait moins bien sur v1, avec ou sans lexique. La fusion des rangs pénalise un passage trouvé par une seule des deux méthodes (par exemple q19 « donnée personnelle », perdue, ou q27 « amendes de l'AI Act », rang 15). Avec le lexique, elle brille sur v0 (10/10) mais recule sur v1 (8/17) : c'est exactement le sur-réglage que les questions v1 servent à détecter. Elle reste disponible (`SEARCH_MODE=hybrid`) pour de futurs essais.
- La reformulation de la question par le modèle n'a pas été testée (5 à 10 s de plus par question et deux modèles à charger tour à tour) : le lexique teste la même idée à moindre coût.

Rang du premier article attendu (— = pas dans les 20 premiers) :

| Question | vecteurs seuls | vecteurs + lexique | hybride | hybride + lexique (mots-clés) | hybride + lexique (partout) |
|---|---|---|---|---|---|
| q01 | 1 | 1 | 1 | 1 | 1 |
| q02 | 1 | 1 | 1 | 1 | 1 |
| q03 | 6 | 4 | 20 | 1 | 1 |
| q04 | 20 | 1 | — | 3 | 2 |
| q05 | 1 | 1 | 1 | 1 | 1 |
| q06 | 1 | 1 | 1 | 1 | 1 |
| q07 | 1 | 1 | 1 | 1 | 1 |
| q08 | 1 | 1 | 13 | 1 | 1 |
| q09 | 3 | 3 | 6 | 1 | 1 |
| q10 | — | 7 | — | 9 | 2 |
| q11 | 1 | 1 | 1 | 1 | 1 |
| q12 | 3 | 2 | 1 | 1 | 1 |
| q13 | 1 | 1 | 2 | 1 | 1 |
| q14 | — | 20 | — | 15 | 15 |
| q15 | 6 | 6 | 1 | 1 | 1 |
| q16 | 5 (5–6) | 5 | 9 | 12 | — |
| q17 | 1 | 1 | 2 | 7 | 6 |
| q18 | — | 1 | 7 | 13 | 10 |
| q19 | 1 | 1 | — | — | — |
| q20 | 1 | 1 | 1 | 1 | 1 |
| q21 | — | — | — | — | — |
| q22 | 1 | 1 | 1 | 1 | 1 |
| q23 | 1 | 1 | 1 | 1 | 1 |
| q24 | 9 | 8 | 5 | 4 | 6 |
| q25 | 2 | 2 | 13 | 13 | 13 |
| q26 | 1 | 1 | 1 | 1 | 1 |
| q27 | 1 | 1 | 15 | 15 | 15 |

## 3. Génération fidèle

Nouveau format (`src/compliance_copilot/rag.py`) : le modèle écrit d'abord `EXTRAITS :` (les phrases exactes des passages, avec leur numéro), puis `RÉPONSE :`, à partir de ces phrases seulement. Le code :

- vérifie chaque extrait **mot pour mot** dans le passage cité ; sont seulement tolérés les espaces, le style des apostrophes et des guillemets, les majuscules, et les coupures marquées « … » ou par un retour à la ligne (chaque morceau doit alors exister, dans l'ordre) ; un extrait de moins de 6 mots ne prouve rien et n'est pas retenu ;
- remplace la réponse par « Les textes trouvés ne permettent pas de répondre à cette question. » si aucun extrait n'est vérifié ; pendant l'affichage au fil de l'eau, la réponse n'apparaît qu'une fois ses extraits vérifiés ;
- n'affiche pas l'alerte « aucune citation » sur un refus propre (question hors sujet) ;
- signale un extrait introuvable, une citation sans extrait vérifié, une réponse coupée, ou un modèle qui n'a pas rédigé sa réponse.

**Limite** : un extrait vérifié prouve que la phrase existe dans la loi, pas qu'elle répond à la question (voir q10, section 6).

## 4. Modèle : `ministral-3:3b` contre `qwen3:4b-instruct`

Commande : `scripts/compare_models.py ministral-3:3b qwen3:4b-instruct`. Les 32 questions (v0, hors sujet v0, v1) sont cherchées une seule fois ; les deux modèles répondent à partir **des mêmes passages**, avec le même prompt (température 0,1, contexte 8 192 tokens, toutes les couches sur la carte graphique).

Mémoire graphique mesurée (contexte 8 192 tokens, toutes les couches sur la carte graphique) : `qwen3:4b-instruct` 3,68 Go (pas de module de vision), `ministral-3:3b` 3,87 Go.

**1er tour** (prompt initial, 900 tokens au plus) :

| Modèle | Réponses données (sur 27) | Avec un extrait vérifié d'un article attendu | Hors sujet refusés (sur 5) | Extraits vérifiés / recopiés | Réponses coupées | Génération moyenne | tokens/s |
|---|---|---|---|---|---|---|---|
| `ministral-3:3b` | 14 | 11 | 3 | 27 / 64 | 1 | 22,6 s | 43,9 |
| `qwen3:4b-instruct` | 22 | 21 | 5 | 59 / 63 | 3 | 28,1 s | 35,6 |

Corrections entre les deux tours, justifiées par des questions v0 (q01, q04) et appliquées aux deux modèles :
- qwen recopiait des paragraphes entiers, sur plusieurs lignes, en sautant des paragraphes sans le signaler (q01) : chaque ligne d'un extrait est désormais vérifiée séparément, dans l'ordre ; le prompt demande une seule phrase ou un seul point par extrait, quatre au plus ;
- des réponses étaient coupées avant `RÉPONSE :`, faute de place (q04 ; aussi q17 et q23 en v1) : limite portée de 900 à 1 500 tokens ;
- l'alerte affichée dans ce cas donnait une raison fausse (« aucun extrait retrouvé ») : corrigée.

**2e tour** (prompt final, 1 500 tokens au plus) :

| Modèle | Réponses données (sur 27) | Avec un extrait vérifié d'un article attendu | Hors sujet refusés (sur 5) | Extraits vérifiés / recopiés | Réponses coupées | Génération moyenne | tokens/s |
|---|---|---|---|---|---|---|---|
| `ministral-3:3b` | 21 | 15 | 2 | 45 / 88 (51 %) | 0 | 23,4 s | 42,1 |
| **`qwen3:4b-instruct` (retenu)** | **27** | **22** | **5** | **79 / 83 (95 %)** | 0 | 28,9 s | 35,9 |

**Choix : `qwen3:4b-instruct`.** Il recopie fidèlement 95 % de ses extraits (contre 51 %) et refuse toutes les questions hors sujet (ministral en traite 3 sur 5). Il est environ 5 s plus lent par réponse.

Détail du 2e tour (état, extraits vérifiés / recopiés, « attendu » = au moins un extrait vérifié vient d'un article attendu, temps de génération) :

| Question | `ministral-3:3b` | `qwen3:4b-instruct` |
|---|---|---|
| q01 | réponse 2/2 attendu 36 s | réponse 1/1 attendu 42 s |
| q02 | réponse 2/2 attendu 22 s | réponse 3/3 attendu 25 s |
| q03 | réponse 2/2 attendu 23 s | réponse 1/2 attendu 24 s |
| q04 | réponse 4/5 attendu 31 s | réponse 12/12 attendu 43 s |
| q05 | réponse 3/3 attendu 18 s | réponse 1/1 attendu 20 s |
| q06 | réponse 1/3 27 s | réponse 4/4 attendu 34 s |
| q07 | réponse 3/4 attendu 18 s | réponse 4/4 attendu 29 s |
| q08 | réponse 2/2 attendu 22 s | réponse 1/1 attendu 26 s |
| q09 | réponse 3/3 attendu 27 s | réponse 1/1 attendu 28 s |
| q10 | refus 0/2 18 s | réponse 4/4 21 s |
| h01 (hors sujet) | refus 0/0 13 s | refus 0/0 17 s |
| h02 (hors sujet) | réponse 1/2 16 s | refus 0/0 18 s |
| q11 | réponse 3/3 attendu 27 s | réponse 4/4 attendu 47 s |
| q12 | réponse 1/2 attendu 21 s | réponse 1/1 attendu 27 s |
| q13 | refus 0/2 22 s | réponse 1/1 attendu 24 s |
| q14 | réponse 3/4 19 s | réponse 4/4 31 s |
| q15 | refus 0/2 25 s | réponse 2/4 39 s |
| q16 | refus 0/2 23 s | réponse 4/4 attendu 40 s |
| q17 | réponse 2/3 attendu 26 s | réponse 4/4 attendu 32 s |
| q18 | réponse 1/2 attendu 23 s | réponse 1/1 attendu 25 s |
| q19 | réponse 1/3 16 s | réponse 2/2 attendu 16 s |
| q20 | réponse 2/2 attendu 25 s | réponse 1/1 attendu 31 s |
| q21 | réponse 1/2 20 s | réponse 3/4 29 s |
| q22 | réponse 2/3 attendu 14 s | réponse 4/4 attendu 23 s |
| q23 | réponse 1/8 attendu 48 s | réponse 7/7 attendu 66 s |
| q24 | réponse 1/2 31 s | réponse 1/1 33 s |
| q25 | réponse 2/4 23 s | réponse 1/1 attendu 21 s |
| q26 | refus 0/2 17 s | réponse 3/3 attendu 21 s |
| q27 | refus 0/5 38 s | réponse 4/4 attendu 39 s |
| h03 (hors sujet) | réponse 1/3 26 s | refus 0/0 26 s |
| h04 (hors sujet) | réponse 1/2 15 s | refus 0/0 14 s |
| h05 (hors sujet) | refus 0/2 20 s | refus 0/0 18 s |

## 5. Avant / après (meilleure configuration)

Meilleure configuration : recherche par vecteurs `bge-m3` + lexique, 5 passages ; `qwen3:4b-instruct`, extraits vérifiés, 1 500 tokens au plus. Réponses brutes, non relues : `eval/answers_v1.md`.

| Mesure | Avant (séance 4) | Après (séance 5) | Séance 5 bis |
|---|---|---|---|
| Recherche, v0 : hit@1 / hit@5 | 6/10 · 7/10 | 7/10 · 9/10 | 7/10 · **10/10** |
| Recherche, v1 : hit@1 / hit@5 | 9/17 · 11–12/17 | 10/17 · 13/17 | 10/17 · 13/17 |
| Extraits vérifiés mot pour mot, 12 questions (`answers_v1.md`, puis `answers_v2.md`) | non mesurable (pas d'extraits) | 21 / 23 | 39 / 40 |
| Extraits vérifiés mot pour mot, 32 questions (comparaison des modèles) | — | 79 / 83 | 75 / 79 |
| Réponses appuyées sur un extrait vérifié d'un article attendu (27 questions) | — | 22 / 27 | 23 / 27 |
| Questions hors sujet refusées | h01 refusée (avec l'alerte « aucune citation »), h02 hors cadre expliqué par le modèle | 2/2 refus standard, sans alerte ; v1 : 3/3 | 2/2 ; v1 : 3/3 |
| Réponses avec au moins une citation [n] (10 questions v0) | — | 2 / 10 | **10 / 10** |
| Réponses avec au moins une citation [n] (32 questions, réponses données) | — | 5 / 27 | **26 / 26** |
| Tutoiements (32 questions) | — | 3 | **0** |
| Réponses avec au moins une alerte (12 questions) | — | 9 / 12 | **3 / 12** |
| Réponses avec au moins une alerte (32 questions) | — | 23 / 32 (25 alertes) | **7 / 32 (10 alertes)** |
| Réponses coupées (32 questions) | — | 0 | 1 (q23) |
| Temps moyen par question (12 questions) | 18 s (`ministral-3:3b`, sans extraits) | 31 s (`qwen3:4b-instruct`, avec extraits) | 41 s (machine plus lente ce jour-là, voir section 7) |

La justesse des réponses s'établit par relecture humaine : `eval/review_v0.md`, `eval/review_v1.md` ; `eval/answers_v2.md` reste à relire.

## 6. Points ouverts, pour la relecture et la suite

- **q10 reste fausse, et c'est grave** : l'art. 4 (maîtrise de l'IA) n'est toujours pas dans les 5 passages (rang 7 avec le lexique). La réponse, appuyée sur des extraits vérifiés de l'art. 50, affirme qu'il n'y a « aucune obligation pour l'usage interne », ce que contredit l'art. 4. Illustration directe de la limite : extrait vérifié ne veut pas dire réponse juste.
- **q04** : contenu juste (art. 13), mais le modèle tutoie, malgré la règle du prompt.
- **Citations [n] dans la réponse** : qwen en met rarement (8 réponses sur 10 de `answers_v1.md` n'en ont aucune) ; les extraits vérifiés, affichés avec leur numéro de passage, appuient quand même la réponse, et le code le signale.
- **Nombre d'extraits** : qwen dépasse parfois la limite de quatre (12 pour q04 au 2e tour).
- **Variabilité** : ±1 rang possible sur les passages aux scores presque égaux (voir section 1).
- **Questions partiellement couvertes** (q14, q16, q20 ; q03 en v0) : à relire avec le critère « dire ce que dit le texte et signaler que la réponse complète dépend d'autres textes ».

## 7. Séance 5 bis — corrections après la relecture de `answers_v1.md`

Relecture de l'auteur (`eval/review_v1.md`) : 9 réponses justes, 2 partielles (q02 oublie la condition « pas de données sensibles » de l'art. 30, § 5 ; q06 oublie l'information des personnes, art. 34), 1 fausse et dangereuse (q10). Les corrections sont générales : aucune règle n'est écrite pour une seule question. Tout est mesuré sur v0 et v1.

### 7.1 Recherche : au plus 2 passages d'un même article

Diagnostic de q10, avant tout changement :
- sans lexique, l'art. 4 (maîtrise de l'IA) n'est pas dans les 20 premiers (similarité 0,567) ; avec le lexique, il est au rang 7 (0,656) ;
- les 5 passages venaient de **2 articles seulement** (art. 50 ×2, art. 26 ×3). Cause générale : un long article découpé en paragraphes peut occuper tout le top 5.

Correction : la recherche prend 20 candidats, puis écarte le 3e morceau d'un même article et les suivants (`SEARCH_MAX_PER_ARTICLE=2`). Le lexique n'a pas changé : une entrée taillée pour q10 serait une règle pour une seule question.

Commande : `scripts/compare_retrieval.py --repeat 3` (trois mesures identiques).

| Configuration | v0 hit@1 | v0 hit@5 | v1 hit@1 | v1 hit@5 |
|---|---|---|---|---|
| vecteurs seuls (départ) | 6/10 | 7/10 | 9/17 | 11/17 |
| vecteurs + lexique (séance 5) | 7/10 | 9/10 | 10/17 | 13/17 |
| **vecteurs + lexique + 2 par article (retenu)** | 7/10 | **10/10** | 10/17 | 13/17 |

Les configurations hybrides donnent les mêmes hit@1 et hit@5 qu'en section 2. Rangs modifiés par la limite : q10 passe du rang 7 au rang 5, q14 du rang 20 au rang 16 ; les autres ne bougent pas.

Essai exploratoire, avant la décision : avec 1 passage par article au plus, v0 donne aussi 10/10 (q10 au rang 3) et v1 ne change pas ; le nombre moyen d'articles différents dans le top 5 passe de 3,6 (v0) et 4,2 (v1) à 4,1 et 4,4 avec 2 au plus, et 5,0 et 5,0 avec 1 au plus. On garde 2, car certaines réponses ont besoin de plusieurs paragraphes du même article.

**Décision de l'auteur, et changement de règle (transparence)** : v1 ne monte pas, donc l'ancienne règle (« améliorer v0 **et** v1 ») aurait rejeté ce changement. L'auteur l'a adopté et a assoupli la règle **après avoir vu cette mesure** : désormais, un changement est gardé s'il ne fait baisser le hit@5 sur aucun jeu (v0, v1) et fait monter au moins une mesure.

**Effet de bord constaté sur q07** (AIPD) : les 5 passages étaient tous des paragraphes de l'art. 35 du RGPD (§ 3, 11, 1, 7, 4) ; avec la limite, il en reste 2 (§ 3 et 11), et arrivent l'art. 27 de l'AI Act (analyse d'impact sur les **droits fondamentaux**), l'art. 26, § 9 et l'art. 83. Le § 1 de l'art. 35, qui pose la règle générale, n'est plus donné au modèle. La réponse v2 confond alors les deux analyses (« Elle est également obligatoire avant le déploiement d'un système d'IA à haut risque [3] »). Le hit@5 ne voit pas ce recul, car il compte l'article et non le paragraphe. q07 était jugée juste en v1.

### 7.2 Prompt

- Réécrit entièrement au « vous » : un prompt qui tutoie le modèle l'incite à tutoyer l'utilisateur.
- Un court exemple de forme, au contenu **fictif** (« obligation X », « cas Y »), montre où placer les [n] ; rien n'est emprunté aux questions de test.
- Quatre règles générales : ne jamais conclure « aucune obligation » parce que les passages n'en parlent pas (écrire « les passages trouvés ne traitent pas de ce point ») ; répondre à chaque partie de la question ; quand le texte ne donne qu'un principe (par exemple une durée de conservation), le dire et préciser que les règles concrètes peuvent venir d'autres textes (droit national, CNIL) ; toujours vouvoyer.

### 7.3 Contrôles de la réponse par le code

**Alerte « phrase non appuyée »** (remplace « La réponse ne cite aucun passage », seulement quand la réponse n'a aucun [n]) : une phrase est signalée si moins de **35 %** de ses mots significatifs (racines, comme pour BM25) se retrouvent dans les extraits vérifiés. Seuil choisi par l'auteur d'après cette mesure sur les 27 réponses de qwen enregistrées à la séance 5 :

| Seuil | Réponses avec l'alerte (sur 27) | q03 v0 « 10 ans » (31 %) | q09 v0 « vous ne pouvez pas » (30 %) | q10 v1 « aucune obligation » (9 %) |
|---|---|---|---|---|
| 60 % | 19 | signalée | signalée | signalée |
| 50 % | 14 | signalée | signalée | signalée |
| 45 % | 14 | signalée | signalée | signalée |
| 40 % | 12 | signalée | signalée | signalée |
| **35 %** | **12** | signalée | signalée | signalée |
| 30 % | 11 | **non signalée** | signalée | signalée |

Les trois phrases fausses sont des **tests de non-régression** (`KNOWN_WRONG` dans `tests/test_rag.py`), avec les vrais extraits sur lesquels le modèle s'appuyait (AI Act art. 18 ; annexe III, point 4 ; art. 26 et art. 50). La nouvelle alerte les signale toutes : elle remplace donc l'ancienne.

**Règle d'absence** (demandée par l'auteur, toujours active) : une phrase qui affirme une absence ou une impossibilité (« aucune obligation », « n'est pas obligatoire », « ne s'applique pas », « vous ne pouvez pas »…) est signalée si aucun extrait vérifié ne contient lui-même une négation. Les phrases qui parlent des passages (« les passages trouvés ne traitent pas de ce point ») ne sont pas visées : c'est la formulation demandée au modèle. Tests : q09 et q10 signalées. Fausses alertes connues, sur des déductions justes : q01 (séance 5, « cela n'est pas obligatoire »), q22 (« le consentement n'est pas obligatoirement donné par écrit »).

**Tutoiement** : « tu », « toi », « te », « t' », « ton », « ta », « tes » dans la réponse (pas dans les extraits).

Ces contrôles ne comprennent pas le sens : ce sont des signaux pour la relecture, pas des preuves.

### 7.4 Génération (32 questions, mêmes réglages)

Commande : `scripts/compare_models.py qwen3:4b-instruct` (nouvelles colonnes : réponses avec [n], tutoiements, alertes). La colonne « séance 5 » reprend les réponses enregistrées au 2e tour (section 4) ; elles ont aussi été repassées dans les contrôles actuels, pour séparer l'effet des nouvelles règles d'alerte de celui du nouveau prompt.

| Mesure | Séance 5 (2e tour) | Séance 5 bis |
|---|---|---|
| Réponses données (sur 27) | 27 | 26 (q23 coupée, refus par prudence) |
| Avec un extrait vérifié d'un article attendu | 22 | 23 |
| Hors sujet refusés (sur 5) | 5 | 5 |
| Extraits vérifiés / recopiés | 79 / 83 | 75 / 79 |
| Réponses coupées | 0 | 1 |
| Réponses avec au moins une citation [n] | 5 / 27 | **26 / 26** |
| Tutoiements | 3 (q04, q12, q24) | **0** |
| Réponses avec au moins une alerte (sur 32) | 23 (25 alertes) ; 16 (20 alertes) avec les contrôles actuels | **7 (10 alertes)** |
| Génération moyenne | 28,9 s | 42,1 s |
| tokens/s | 35,9 | 21,3 |

**Vitesse** : le recul ne vient pas surtout du changement. Test A/B le même jour, sur les mêmes passages, prompt de la séance 5 contre prompt 5 bis : h01 25–26 contre 23–24 tokens/s, q05 25 contre 24, q08 19–20 contre 19. Le jour des mesures, la machine était plus lente qu'à la séance 5 (h01 : 37,9 tokens/s à la séance 5 avec l'ancien prompt) ; Ollama s'était mis à jour tout seul (0.40.10 → 0.40.11). Sur un prompt court, qwen génère toujours vers 41 tokens/s. Le nouveau prompt ajoute environ 290 tokens à lire (environ 2 s) et coûte 1 à 2 tokens/s. À remesurer un autre jour.

### 7.5 Vérifications demandées par l'auteur

1. **Non-régression** : les trois phrases fausses (q03, q09, q10) sont signalées par la nouvelle alerte. Tests ajoutés, ils passent.
2. **Absence** : une affirmation d'absence sans extrait négatif déclenche une alerte (tests ajoutés), avec les fausses alertes connues ci-dessus.
3. **q10 v2 mentionne l'art. 4** : oui, « vous devez prendre des mesures pour favoriser la maîtrise de l'IA par vos salariés ou bénévoles [5] » (art. 4 au passage [5]). Deux défauts restent, pour la relecture :
   - l'obligation de l'art. 50, § 1 vise les **fournisseurs**, mais la réponse la présente comme la vôtre (« Vous devez informer les personnes concernées… [1] ») ;
   - la dernière phrase n'a ni [n] ni extrait (« Ces obligations s'appliquent à l'usage interne ou externe, tant que l'IA est utilisée par des personnes physiques. »). Elle n'est pas signalée, car l'alerte « phrase non appuyée » ne joue que si la réponse n'a aucun [n].

### 7.6 Points ouverts, pour la relecture de `answers_v2.md`

- **q07** : recul probable, dû à la limite par article (section 7.1). À trancher : garder 2 par article, passer à 3 (q10 ressortirait probablement du top 5) ou chercher une autre façon de garder le paragraphe général d'un article.
- **q06** : l'information des personnes (art. 34) manque toujours, bien que l'art. 34 soit le passage [2] ; la règle de complétude ne suffit pas. La réponse dit aussi que le sous-traitant doit « noter » la violation (le texte dit « notifie »).
- **q08** : exception inversée (« sauf si cela **ne** ressort **pas** clairement »), alors que le texte dit « sauf si cela ressort clairement ». Aucun contrôle ne le voit.
- **q02** : la condition des catégories particulières de données (art. 30, § 5) apparaît désormais. À confirmer par la relecture.
- **q03** : la réponse donne le principe (art. 5) sans dire que les durées concrètes viennent d'autres textes : la règle de complétude n'est pas appliquée.
- **Limite de l'alerte « phrase non appuyée »** : maintenant que presque toutes les réponses ont des [n], elle ne joue presque plus. Une phrase sans [n] dans une réponse qui en a ailleurs n'est pas vérifiée (q10). Piste : vérifier chaque phrase sans [n] (à mesurer : risque de plus d'alertes).
- **Longueur** : q23 coupée (un paragraphe entier recopié comme un seul extrait), q04 avec 19 extraits (limite de quatre ignorée, 92 s).
