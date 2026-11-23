# Réponses du copilote — v6b_remote_author

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 23/11/2026 à 15:14 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen/qwen3.8-27b` via l'API compatible OpenAI https://api.groq.com/openai/v1 (expérience de la séance 7, questions de test seulement ; modèle tel que servi par l'API à la date ci-dessus) — température 0.1, raisonnement : réglage par défaut du modèle, passages calculés pour un contexte de 8192 tokens comme en local, 2000 tokens au plus par réponse (raisonnement compris) ; le juge est le même modèle
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu, reranker `BAAI/bge-reranker-v2-m3` sur CPU (20 candidats reclassés avant la limite par article), reformulation de la question par le modèle avant la recherche (termes juridiques ajoutés, sans conclusion)
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_author.jsonl` (3 + 1 hors sujet)
- Sélection : seules les questions choisies avec --ids ont été posées (les autres ne figurent pas dans ce fichier)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| a02 | Un partenaire commercial me propose de racheter notre fichier clients. Est-ce que je peux le lui vendre ? | 4/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 42 s |
| a03 | Je pense acheter un logiciel d'IA qui note les résultats de mes commerciaux et propose qui mérite une prime. Qu'est-ce que je dois savoir avant de l'utiliser ? | 6/6 | non | La réponse met entre « » un texte introuvable dans les extraits vérifiés : « en notifie[r] les résultats à l’autorité de surveillance du marché » (et 1 autre(s)). | 30 s |
| a05 | On veut publier sur notre site et sur Facebook les photos de la fête de l'association, où l'on voit des adhérents et leurs enfants. Faut-il leur demander la permission ? | 6/6 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 26 s |
| ha01 | Combien de jours de congés payés a un salarié à temps partiel ? | 0/0 | oui | — | 27 s |

## a02 — Un partenaire commercial me propose de racheter notre fichier clients. Est-ce que je peux le lui vendre ?

Article attendu : RGPD art. 6, paragraphe 1 ou RGPD art. 5 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 47, paragraphe 2, points a) à k) : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
  [2] RGPD — règlement (UE) 2016/679, article 47, paragraphe 1 : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
  [3] RGPD — règlement (UE) 2016/679, article 21 : Droit d'opposition
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_21
  [4] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [5] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [4] « les destinataires ou les catégories de destinataires des données à caractère personnel, s'ils existent; »
- [4] « le responsable du traitement fournit au préalable à la personne concernée des informations au sujet de cette autre finalité et toute autre information pertinente visée au paragraphe 2. »
- [3] « La personne concernée a le droit de s'opposer à tout moment, pour des raisons tenant à sa situation particulière, à un traitement des données à caractère personnel la concernant fondé sur l'article 6, paragraphe 1, point e) ou f), y compris un profilage fondé sur ces dispositions. »
- [3] « Le responsable du traitement ne traite plus les données à caractère personnel, à moins qu'il ne démontre qu'il existe des motifs légitimes et impérieux pour le traitement qui prévalent sur les intérêts et les droits et libertés de la personne concernée, ou pour la constatation, l'exercice ou la défense de droits en justice. »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question concernant la licéité spécifique de la vente d'un fichier clients à un partenaire commercial. Ils précisent toutefois que vous devez informer les personnes concernées des destinataires de leurs données [4]. Si la vente constitue un traitement ultérieur pour une finalité autre que celle de la collecte initiale, vous devez fournir au préalable des informations au sujet de cette autre finalité [4]. De plus, les personnes concernées disposent du droit de s'opposer à un traitement fondé sur des intérêts légitimes, auquel cas vous ne pouvez plus traiter les données sauf si vous démontrez des motifs légitimes et impérieux qui prévalent sur leurs intérêts [3].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données à caractère personnel ; cession de données ; consentement ; transfert de données ; droits des personnes concernées

Temps : recherche 40.0 s · génération 1.3 s (4105 tokens lus, 381 écrits, 569.0 tokens/s) · contrôle de pertinence 0.1 s · reformulation 0.6 s

## a03 — Je pense acheter un logiciel d'IA qui note les résultats de mes commerciaux et propose qui mérite une prime. Qu'est-ce que je dois savoir avant de l'utiliser ?

Article attendu : AI Act annexe III, point 4 ou AI Act art. 26, paragraphe 7 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question, car ils ne précisent pas si un logiciel notant des commerciaux est classé comme « système d’IA à haut risque » ni s’il relève des catégories visées par l’obligation d’analyse d’impact.
>
> Cependant, si ce logiciel est bien un système d’IA à haut risque et que vous en êtes le déployeur, vous devez savoir que vous devez effectuer une analyse de l’impact sur les droits fondamentaux avant le déploiement, « à l’exception des systèmes d’IA à haut risque destinés à être utilisés dans le domaine visé à l’annexe III, point 2 » [2]. Cette obligation s’applique « à la première utilisation du système d’IA à haut risque » [2]. Une fois cette analyse effectuée, vous devez « en notifie[r] les résultats à l’autorité de surveillance du marché » [2].
>
> Par ailleurs, vous devez vous assurer que le système est « accompagné d’une notice d’utilisation » contenant des informations « concises, complètes, exactes et claires » [1]. Cette notice doit notamment indiquer « l’identité et les coordonnées du fournisseur » ainsi que « les caractéristiques, les capacités et les limites de performance du système d’IA à haut risque, notamment: i) sa destination » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « Avant le déploiement d’un système d’IA à haut risque visé à l’article 6, paragraphe 2, à l’exception des systèmes d’IA à haut risque destinés à être utilisés dans le domaine visé à l’annexe III, point 2, les déployeurs qui sont des organismes de droit public ou des entités privées fournissant des services publics et les déployeurs de systèmes d’IA à haut risque visés à l’annexe III, points 5), b) et c), effectuent une analyse de l’impact sur les droits fondamentaux que l’utilisation de ce système peut produire. »
  [2] « L’obligation établie au paragraphe 1 s’applique à la première utilisation du système d’IA à haut risque. »
  [2] « Une fois l’analyse visée au paragraphe 1 du présent article effectuée, le déployeur en notifie les résultats à l’autorité de surveillance du marché, et soumet le modèle visé au paragraphe 5 du présent article, rempli, dans le cadre de la notification. »
  [1] « Les systèmes d’IA à haut risque sont accompagnés d’une notice d’utilisation dans un format numérique approprié ou autre, contenant des informations concises, complètes, exactes et claires, qui soient pertinentes, accessibles et compréhensibles pour les déployeurs. »
  [1] « La notice d’utilisation contient au moins les informations suivantes: a) l’identité et les coordonnées du fournisseur et, le cas échéant, de son mandataire; »
  [1] « b) les caractéristiques, les capacités et les limites de performance du système d’IA à haut risque, notamment: i) sa destination; »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 13 : Transparence et fourniture d’informations aux déployeurs (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_13
  [2] AI Act — règlement (UE) 2024/1689, article 27 : Analyse d’impact des systèmes d’IA à haut risque sur les droits fondamentaux (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_27
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, article 9, paragraphe 8 : Système de gestion des risques
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_9
  [4] AI Act — règlement (UE) 2024/1689, article 9, paragraphe 1 : Système de gestion des risques
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_9
  [5] AI Act — règlement (UE) 2024/1689, article 9, point c : Système de gestion des risques
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_9
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « en notifie[r] les résultats à l’autorité de surveillance du marché » (et 1 autre(s)).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [2] « Avant le déploiement d’un système d’IA à haut risque visé à l’article 6, paragraphe 2, à l’exception des systèmes d’IA à haut risque destinés à être utilisés dans le domaine visé à l’annexe III, point 2, les déployeurs qui sont des organismes de droit public ou des entités privées fournissant des services publics et les déployeurs de systèmes d’IA à haut risque visés à l’annexe III, points 5), b) et c), effectuent une analyse de l’impact sur les droits fondamentaux que l’utilisation de ce système peut produire. »
- [2] « L’obligation établie au paragraphe 1 s’applique à la première utilisation du système d’IA à haut risque. »
- [2] « Une fois l’analyse visée au paragraphe 1 du présent article effectuée, le déployeur en notifie les résultats à l’autorité de surveillance du marché, et soumet le modèle visé au paragraphe 5 du présent article, rempli, dans le cadre de la notification. »
- [1] « Les systèmes d’IA à haut risque sont accompagnés d’une notice d’utilisation dans un format numérique approprié ou autre, contenant des informations concises, complètes, exactes et claires, qui soient pertinentes, accessibles et compréhensibles pour les déployeurs. »
- [1] « La notice d’utilisation contient au moins les informations suivantes: a) l’identité et les coordonnées du fournisseur et, le cas échéant, de son mandataire; »
- [1] « b) les caractéristiques, les capacités et les limites de performance du système d’IA à haut risque, notamment: i) sa destination; »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question, car ils ne précisent pas si un logiciel notant des commerciaux est classé comme « système d’IA à haut risque » ni s’il relève des catégories visées par l’obligation d’analyse d’impact.

Cependant, si ce logiciel est bien un système d’IA à haut risque et que vous en êtes le déployeur, vous devez savoir que vous devez effectuer une analyse de l’impact sur les droits fondamentaux avant le déploiement, « à l’exception des systèmes d’IA à haut risque destinés à être utilisés dans le domaine visé à l’annexe III, point 2 » [2]. Cette obligation s’applique « à la première utilisation du système d’IA à haut risque » [2]. Une fois cette analyse effectuée, vous devez « en notifie[r] les résultats à l’autorité de surveillance du marché » [2].

Par ailleurs, vous devez vous assurer que le système est « accompagné d’une notice d’utilisation » contenant des informations « concises, complètes, exactes et claires » [1]. Cette notice doit notamment indiquer « l’identité et les coordonnées du fournisseur » ainsi que « les caractéristiques, les capacités et les limites de performance du système d’IA à haut risque, notamment: i) sa destination » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : système d'IA à haut risque ; évaluation d'impact ; profilage ; décision automatisée ; données à caractère personnel ; transparence

Temps : recherche 26.5 s · génération 2.5 s (3194 tokens lus, 688 écrits, 341.9 tokens/s) · contrôle de pertinence 0.6 s · reformulation 0.2 s · attente des limites de l'API 3 s (non comptée)

## a05 — On veut publier sur notre site et sur Facebook les photos de la fête de l'association, où l'on voit des adhérents et leurs enfants. Faut-il leur demander la permission ?

Article attendu : RGPD art. 6, paragraphe 1 ou RGPD art. 7 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [2] RGPD — règlement (UE) 2016/679, article 40, paragraphe 1 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [3] RGPD — règlement (UE) 2016/679, article 80 : Représentation des personnes concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_80
  [4] RGPD — règlement (UE) 2016/679, article 35, paragraphe 9 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [5] RGPD — règlement (UE) 2016/679, article 35, paragraphe 1 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « a) le traitement loyal et transparent; »
- [1] « e) les informations communiquées au public et aux personnes concernées; »
- [1] « g) les informations communiquées aux enfants et la protection dont bénéficient les enfants et la manière d'obtenir le consentement des titulaires de la responsabilité parentale à l'égard de l'enfant; »
- [1] « f) l'exercice des droits des personnes concernées; »
- [3] « La personne concernée a le droit de mandater un organisme, une organisation ou une association à but non lucratif, qui a été valablement constitué conformément au droit d'un État membre, dont les objectifs statutaires sont d'intérêt public et est actif dans le domaine de la protection des droits et libertés des personnes concernées dans le cadre de la protection des données à caractère personnel les concernant, pour qu'il introduise une réclamation en son nom, exerce en son nom les droits visés aux articles 77, 78 et 79 et exerce en son nom le droit d'obtenir réparation visé à l'article 82 lorsque le droit d'un État membre le prévoit. »
- [4] « Le cas échéant, le responsable du traitement demande l'avis des personnes concernées ou de leurs représentants au sujet du traitement prévu, sans préjudice de la protection des intérêts généraux ou commerciaux ou de la sécurité des opérations de traitement. »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question. Ils indiquent que les codes de conduite peuvent préciser « les informations communiquées au public et aux personnes concernées » [1] et « la manière d'obtenir le consentement des titulaires de la responsabilité parentale à l'égard de l'enfant » [1], ainsi que « le traitement loyal et transparent » [1]. Ils mentionnent également que le responsable du traitement peut « demander l'avis des personnes concernées ou de leurs représentants au sujet du traitement prévu » [4] et que les personnes concernées ont le droit de mandater une association pour exercer leurs droits [3]. Cependant, les extraits fournis ne précisent pas si une permission explicite est obligatoire pour la publication de photos sur un site web ou les réseaux sociaux, ni les conditions exactes de ce consentement.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : consentement ; données à caractère personnel ; image ; droit à l'information ; droit d'accès ; droit à l'effacement

Temps : recherche 23.9 s · génération 1.6 s (2177 tokens lus, 497 écrits, 501.2 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.2 s · attente des limites de l'API 23 s (non comptée)

## ha01 — Combien de jours de congés payés a un salarié à temps partiel ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [3] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [4] RGPD — règlement (UE) 2016/679, article 12, paragraphe 2 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [5] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit aux congés payés ; salarié à temps partiel ; durée du travail ; jours ouvrés ; jours ouvrables ; acquisition des congés

Temps : recherche 25.8 s · génération 0.6 s (3157 tokens lus, 25 écrits, 506.9 tokens/s) · reformulation 0.5 s
