# Réponses du copilote — v6_local_author

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 18/11/2026 à 16:48 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen3:4b-instruct` via Ollama 0.40.16 — température 0.1, contexte 8192 tokens, couches sur la carte graphique : toutes, 2000 tokens au plus par réponse
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu, reranker `BAAI/bge-reranker-v2-m3` sur CPU (20 candidats reclassés avant la limite par article), reformulation de la question par le modèle avant la recherche (termes juridiques ajoutés, sans conclusion)
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_author.jsonl` (5 + 1 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| a01 | J'ai 12 salariés et je voudrais remplacer la badgeuse par une pointeuse à empreinte digitale. J'ai le droit ? | 5/5 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 100 s |
| a02 | Un partenaire commercial me propose de racheter notre fichier clients. Est-ce que je peux le lui vendre ? | 4/5 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 81 s |
| a03 | Je pense acheter un logiciel d'IA qui note les résultats de mes commerciaux et propose qui mérite une prime. Qu'est-ce que je dois savoir avant de l'utiliser ? | 3/3 | non | 1 passage(s) retiré(s) faute de place dans le contexte du modèle (LLM_NUM_CTX = 8192). | 146 s |
| a04 | Pendant nos réunions, un outil d'IA enregistre la discussion et rédige le compte rendu tout seul. Est-ce que je dois prévenir les participants ? | 4/4 | non | La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Cette obligation exige que les personnes physiques concernées soient informées qu’elles interagissent avec un système … ». Vérifiez qui est concerné. | 78 s |
| a05 | On veut publier sur notre site et sur Facebook les photos de la fête de l'association, où l'on voit des adhérents et leurs enfants. Faut-il leur demander la permission ? | 2/2 | non | — | 52 s |
| ha01 | Combien de jours de congés payés a un salarié à temps partiel ? | 0/0 | oui | — | 59 s |

## a01 — J'ai 12 salariés et je voudrais remplacer la badgeuse par une pointeuse à empreinte digitale. J'ai le droit ?

Article attendu : RGPD art. 9, paragraphe 1 ou RGPD art. 9, paragraphe 2 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [2] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [3] RGPD — règlement (UE) 2016/679, article 21 : Droit d'opposition
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_21
  [4] RGPD — règlement (UE) 2016/679, article 16 : Droit de rectification
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_16
  [5] RGPD — règlement (UE) 2016/679, article 20 : Droit à la portabilité des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_20
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: … »  
- [2] « Les États membres peuvent prévoir, par la loi ou au moyen de conventions collectives, des règles plus spécifiques pour assurer la protection des droits et libertés en ce qui concerne le traitement des données à caractère personnel des employés dans le cadre des relations de travail, aux fins, notamment, du recrutement, de l'exécution du contrat de travail, y compris le respect des obligations fixées par la loi ou par des conventions collectives, de la gestion, de la planification et de l'organisation du travail, de l'égalité et de la diversité sur le lieu de travail, de la santé et de la sécurité au travail, de la protection des biens appartenant à l'employeur ou au client, aux fins de l'exercice et de la jouissance des droits et des avantages liés à l'emploi, individuellement ou collectivement, ainsi qu'aux fins de la résiliation de la relation de travail. »  
- [3] « La personne concernée a le droit de s'opposer à tout moment, pour des raisons tenant à sa situation particulière, à un traitement des données à caractère personnel la concernant fondé sur l'article 6, paragraphe 1, point e) ou f), y compris un profilage fondé sur ces dispositions. »  
- [4] « La personne concernée a le droit d'obtenir du responsable du traitement, dans les meilleurs délais, la rectification des données à caractère personnel la concernant qui sont inexactes. Compte tenu des finalités du traitement, la personne concernée a le droit d'obtenir que les données à caractère personnel incomplètes soient complétées, y compris en fournissant une déclaration complémentaire. »  
- [5] « Les personnes concernées ont le droit de recevoir les données à caractère personnel les concernant qu'elles ont fournies à un responsable du traitement, dans un format structuré, couramment utilisé et lisible par machine, et ont le droit de transmettre ces données à un autre responsable du traitement sans que le responsable du traitement auquel les données à caractère personnel ont été communiquées y fasse obstacle, lorsque: a) le traitement est fondé sur le consentement en application de l'article 6, paragraphe 1, point a), ou de l'article 9, paragraphe 2, point a), ou sur un contrat en application de l'article 6, paragraphe 1, point b); et b) le traitement est effectué à l'aide de procédés automatisés. »  

RÉPONSE :  
Oui, vous avez le droit de remplacer la badgeuse par une pointeuse à empreinte digitale, car le traitement des données à caractère personnel des salariés dans le cadre des relations de travail est autorisé par le RGPD, article 88, qui permet aux États membres de prévoir des règles spécifiques pour protéger les droits des employés, notamment en matière de gestion du travail, de santé et de sécurité. Cela inclut des dispositifs comme l'identification des salariés, à condition que le traitement soit justifié par des finalités légitimes telles que la gestion du personnel ou la sécurité au travail. Aucune obligation de consentement spécifique n’est requise ici, car le traitement est fondé sur des finalités licites et nécessaires au fonctionnement de l’entreprise. Les données recueillies par la pointeuse (empreintes digitales) sont considérées comme des données à caractère personnel, et vous devez respecter les droits des salariés, notamment le droit d’opposition (article 21), le droit de rectification (article 16) et le droit d’accès (article 15), mais ces droits ne vous empêchent pas de mettre en place un système de gestion des accès. Le RGPD ne bloque pas la mise en œuvre d’un tel dispositif, à condition que les données soient traitées de manière transparente, sécurisée et conforme aux finalités du traitement. [2]
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données biométriques ; traitement des données personnelles ; consentement explicite ; finalité du traitement ; obligation de transparence ; risque de violation

Temps : recherche 39.7 s · génération 49.5 s (3324 tokens lus, 968 écrits, 32.8 tokens/s) · contrôle de pertinence 7.0 s · reformulation 3.5 s

## a02 — Un partenaire commercial me propose de racheter notre fichier clients. Est-ce que je peux le lui vendre ?

Article attendu : RGPD art. 6, paragraphe 1 ou RGPD art. 5 — passage [5].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [2] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 7 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [4] RGPD — règlement (UE) 2016/679, article 6, paragraphe 3 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
  [5] RGPD — règlement (UE) 2016/679, article 6, paragraphe 1 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: … »  
- [2] « Lorsque des données à caractère personnel relatives à une personne concernée sont collectées auprès de cette personne, le responsable du traitement lui fournit, au moment où les données en question sont obtenues, toutes les informations suivantes: … »  
- [3] « responsabile du traitement, la personne physique ou morale, l'autorité publique, le service ou un autre organisme qui, seul ou conjointement avec d'autres, détermine les finalités et les moyens du traitement; »  
- [4] « Les finalités du traitement sont définies dans cette base juridique ou, en ce qui concerne le traitement visé au paragraphe 1, point e), sont nécessaires à l'exécution d'une mission d'intérêt public ou relevant de l'exercice de l'autorité publique dont est investi le responsable du traitement. »  
- [5] « Le traitement n'est licite que si, et dans la mesure où, au moins une des conditions suivantes est remplie: … f) le traitement est nécessaire aux fins des intérêts légitimes poursuivis par le responsable du traitement ou par un tiers, à moins que ne prévalent les intérêts ou les libertés et droits fondamentaux de la personne concernée qui exigent une protection des données à caractère personnel, notamment lorsque la personne concernée est un enfant. »

RÉPONSE :  
Non, vous ne pouvez pas vendre votre fichier clients à un partenaire commercial sans respecter les obligations du RGPD, car le traitement des données à caractère personnel (comme les données des clients) est soumis à des fondements juridiques précis. Le RGPD (article 6, point f) autorise le traitement pour des intérêts légitimes du responsable du traitement ou d’un tiers, mais ce droit ne s’applique pas à la vente de données à caractère personnel, car il s’agit d’un transfert de données, pas d’un traitement légitime. Le transfert de données à caractère personnel vers un tiers (comme un partenaire commercial) nécessite une base juridique claire, une finalité définie et, dans le cas d’un transfert vers un pays tiers, des garanties appropriées (article 46). Le simple fait de vendre un fichier clients implique un traitement de données à caractère personnel, qui doit être licite, transparent et fondé sur une base juridique valable. Le RGPD ne prévoit pas une autorisation de vente directe de données personnelles, et la vente de données personnelles peut être considérée comme un traitement non licite, sauf si elle est justifiée par une finalité équitable, comme la fourniture d’un service ou la mise en œuvre d’un contrat. Aucun des passages ne permet de conclure que la vente d’un fichier clients est autorisée par le RGPD. Les informations sur les finalités, les destinataires et les garanties doivent être fournies à la personne concernée (article 13), et le responsable du traitement doit garantir que les données ne sont pas utilisées de manière abusive ou sans fondement légal. La vente de données personnelles peut donc être interdite par le RGPD, sauf dans des cas très spécifiques et avec une base juridique claire (comme un contrat ou une mission d’intérêt public).
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données personnelles ; transfert de données ; traitement de données ; consentement ; finalité du traitement ; responsabilité du responsable du traitement

Temps : recherche 27.9 s · génération 44.2 s (3687 tokens lus, 806 écrits, 32.2 tokens/s) · contrôle de pertinence 5.4 s · reformulation 3.3 s

## a03 — Je pense acheter un logiciel d'IA qui note les résultats de mes commerciaux et propose qui mérite une prime. Qu'est-ce que je dois savoir avant de l'utiliser ?

Article attendu : AI Act annexe III, point 4 ou AI Act art. 26, paragraphe 7 — absent des passages donnés au modèle.

### Réponse du copilote

> Avant d’utiliser ce logiciel, vous devez savoir que la notice d’utilisation doit inclure les informations suivantes : l’identité et les coordonnées du fournisseur, les caractéristiques du système d’IA, notamment sa destination, son niveau d’exactitude, ses limites de performance, les circonstances pouvant affecter son fonctionnement, les données d’entrée utilisées, les mesures de contrôle humain, les ressources nécessaires et les mises à jour logicielles [1]. Vous devez aussi savoir que le système doit être évalué selon sa destination, la nature des données traitées, le degré d’autonomie du système, la possibilité d’intervention humaine, les risques éventuels sur la santé, la sécurité ou les droits fondamentaux, la portée des préjudices potentiels, la dépendance des personnes aux résultats du système, les déséquilibres de pouvoir, la réversibilité des décisions, les avantages potentiels et les mesures de réparation existantes [2]. En outre, si le logiciel évalue ou classe des commerciaux selon leur comportement ou leurs caractéristiques personnelles, cela pourrait être interdit par l’AI Act, car cela constituerait un traitement préjudiciable ou défavorable de personnes sur la base de caractéristiques sociales ou personnelles, notamment s’il est injustifié ou disproportionné par rapport à leur comportement [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La notice d’utilisation contient au moins les informations suivantes: a) l’identité et les coordonnées du fournisseur et, le cas échéant, de son mandataire; b) les caractéristiques, les capacités et les limites de performance du système d’IA à haut risque, notamment: i) sa destination; ii) le niveau d’exactitude, y compris les indicateurs utilisés, de robustesse et de cybersécurité visé à l’article 15 qui a servi de référence pour les tests et la validation du système d’IA à haut risque et qui peut être attendu, ainsi que toutes circonstances connues et prévisibles susceptibles d’avoir une incidence sur le niveau attendu d’exactitude, de robustesse et de cybersécurité; iii) toutes circonstances connues ou prévisibles liées à l’utilisation du système d’IA à haut risque conformément à sa destination ou dans des conditions de mauvaise utilisation raisonnablement prévisible, susceptibles d’entraîner des risques pour la santé et la sécurité ou pour les droits fondamentaux visés à l’article 9, paragraphe 2; iv) le cas échéant, les capacités et caractéristiques techniques du système d’IA à haut risque à fournir des informations pertinentes pour expliquer ses sorties; v) le cas échéant, sa performance en ce qui concerne des personnes ou groupes de personnes spécifiques à l’égard desquels le système est destiné à être utilisé; vi) le cas échéant, les spécifications relatives aux données d’entrée, ou toute autre information pertinente concernant les jeux de données d’entraînement, de validation et de test utilisés, compte tenu de la destination du système d’IA à haut risque; vii) le cas échéant, les informations permettant aux déployeurs d’interpréter les sorties du système d’IA à haut risque et de les utiliser de manière appropriée; c) les modifications du système d’IA à haut risque et de sa performance qui ont été prédéterminées par le fournisseur au moment de l’évaluation initiale de la conformité, le cas échéant; d) les mesures de contrôle humain visées à l’article 14, notamment les mesures techniques mises en place pour faciliter l’interprétation des sorties des systèmes d’IA à haut risque par les déployeurs; e) les ressources informatiques et matérielles nécessaires, la durée de vie attendue du système d’IA à haut risque et toutes les mesures de maintenance et de suivi, y compris leur fréquence, nécessaires pour assurer le bon fonctionnement de ce système d’IA, notamment en ce qui concerne les mises à jour logicielles; f) le cas échéant, une description des mécanismes compris dans le système d’IA à haut risque qui permet aux déployeurs de collecter, stocker et interpréter correctement les journaux, conformément à l’article 12. »
  [2] « Lorsqu’elle évalue les conditions visées au paragraphe 1, point b), la Commission tient compte des critères suivants: a) la destination du système d’IA; b) la mesure dans laquelle un système d’IA a été utilisé ou est susceptible de l’être; c) la nature et la quantité des données traitées et utilisées par le système d’IA, en particulier le traitement ou l’absence de traitement des catégories particulières de données à caractère personnel; d) la mesure dans laquelle le système d’IA agit de manière autonome et la mesure dans laquelle l’homme peut intervenir pour annuler une décision ou des recommandations susceptibles de causer un préjudice potentiel; e) la mesure dans laquelle l’utilisation d’un système d’IA a déjà causé un préjudice à la santé et à la sécurité, a eu une incidence négative sur les droits fondamentaux ou a suscité de graves préoccupations quant à la probabilité de ce préjudice ou de cette incidence négative, tel que cela ressort, par exemple, des rapports ou allégations documentées soumis aux autorités nationales compétentes ou d’autres rapports, le cas échéant; f) l’ampleur potentielle d’un tel préjudice ou d’une telle incidence négative, notamment en ce qui concerne son intensité et sa capacité d’affecter plusieurs personnes ou d’affecter un groupe particulier de personnes de manière disproportionnée; g) la mesure dans laquelle les personnes ayant potentiellement subi un préjudice ou une incidence négative dépendent des résultats obtenus au moyen d’un système d’IA, notamment parce qu’il n’est pas raisonnablement possible, pour des raisons pratiques ou juridiques, de s’affranchir de ces résultats; h) la mesure dans laquelle il existe un déséquilibre de pouvoir, ou les personnes ayant potentiellement subi un préjudice ou une incidence négative se trouvent dans une situation vulnérable par rapport au déployeur d’un système d’IA, notamment en raison du statut, de l’autorité, de connaissances, de circonstances économiques ou sociales ou de l’âge; i) la mesure dans laquelle les résultats obtenus en utilisant un système d’IA sont facilement corrigibles ou réversibles, compte tenu des solutions techniques disponibles pour les corriger ou les inverser, les résultats qui ont une incidence négative sur la santé, la sécurité ou les droits fondamentaux ne devant pas être considérés comme facilement corrigibles ou réversibles; j) la probabilité que le déploiement du système d’IA présente des avantages pour certaines personnes, certains groupes de personnes ou la société dans son ensemble et la portée de ces avantages, y compris les améliorations éventuelles quant à la sécurité des produits; k) la mesure dans laquelle le droit existant de l’Union prévoit: i) des mesures de réparation efficaces en ce qui concerne les risques posés par un système d’IA, à l’exclusion des réclamations en dommages-intérêts; ii) des mesures efficaces destinées à prévenir ou à réduire substantiellement ces risques. »
  [4] « La mise sur le marché, la mise en service ou l’utilisation de systèmes d’IA pour l’évaluation ou la classification de personnes physiques ou de groupes de personnes au cours d’une période donnée en fonction de leur comportement social ou de caractéristiques personnelles ou de personnalité connues, déduites ou prédites, la note sociale conduisant à l’une ou l’autre des situations suivantes, ou aux deux: i) le traitement préjudiciable ou défavorable de certaines personnes physiques ou de groupes de personnes dans des contextes sociaux dissociés du contexte dans lequel les données ont été générées ou collectées à l’origine; ii) le traitement préjudiciable ou défavorable de certaines personnes ou de groupes de personnes, qui est injustifié ou disproportionné par rapport à leur comportement social ou à la gravité de celui-ci; »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 13 : Transparence et fourniture d’informations aux déployeurs (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_13
  [2] AI Act — règlement (UE) 2024/1689, article 7, paragraphe 2 : Modifications de l’annexe III (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_7
  [4] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points a) à e) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, article 7, paragraphe 1 : Modifications de l’annexe III
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_7
Attention : 1 passage(s) retiré(s) faute de place dans le contexte du modèle (LLM_NUM_CTX = 8192).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « La notice d’utilisation contient au moins les informations suivantes: a) l’identité et les coordonnées du fournisseur et, le cas échéant, de son mandataire; b) les caractéristiques, les capacités et les limites de performance du système d’IA à haut risque, notamment: i) sa destination; ii) le niveau d’exactitude, y compris les indicateurs utilisés, de robustesse et de cybersécurité visé à l’article 15 qui a servi de référence pour les tests et la validation du système d’IA à haut risque et qui peut être attendu, ainsi que toutes circonstances connues et prévisibles susceptibles d’avoir une incidence sur le niveau attendu d’exactitude, de robustesse et de cybersécurité; iii) toutes circonstances connues ou prévisibles liées à l’utilisation du système d’IA à haut risque conformément à sa destination ou dans des conditions de mauvaise utilisation raisonnablement prévisible, susceptibles d’entraîner des risques pour la santé et la sécurité ou pour les droits fondamentaux visés à l’article 9, paragraphe 2; iv) le cas échéant, les capacités et caractéristiques techniques du système d’IA à haut risque à fournir des informations pertinentes pour expliquer ses sorties; v) le cas échéant, sa performance en ce qui concerne des personnes ou groupes de personnes spécifiques à l’égard desquels le système est destiné à être utilisé; vi) le cas échéant, les spécifications relatives aux données d’entrée, ou toute autre information pertinente concernant les jeux de données d’entraînement, de validation et de test utilisés, compte tenu de la destination du système d’IA à haut risque; vii) le cas échéant, les informations permettant aux déployeurs d’interpréter les sorties du système d’IA à haut risque et de les utiliser de manière appropriée; c) les modifications du système d’IA à haut risque et de sa performance qui ont été prédéterminées par le fournisseur au moment de l’évaluation initiale de la conformité, le cas échéant; d) les mesures de contrôle humain visées à l’article 14, notamment les mesures techniques mises en place pour faciliter l’interprétation des sorties des systèmes d’IA à haut risque par les déployeurs; e) les ressources informatiques et matérielles nécessaires, la durée de vie attendue du système d’IA à haut risque et toutes les mesures de maintenance et de suivi, y compris leur fréquence, nécessaires pour assurer le bon fonctionnement de ce système d’IA, notamment en ce qui concerne les mises à jour logicielles; f) le cas échéant, une description des mécanismes compris dans le système d’IA à haut risque qui permet aux déployeurs de collecter, stocker et interpréter correctement les journaux, conformément à l’article 12. »
- [2] « Lorsqu’elle évalue les conditions visées au paragraphe 1, point b), la Commission tient compte des critères suivants: a) la destination du système d’IA; b) la mesure dans laquelle un système d’IA a été utilisé ou est susceptible de l’être; c) la nature et la quantité des données traitées et utilisées par le système d’IA, en particulier le traitement ou l’absence de traitement des catégories particulières de données à caractère personnel; d) la mesure dans laquelle le système d’IA agit de manière autonome et la mesure dans laquelle l’homme peut intervenir pour annuler une décision ou des recommandations susceptibles de causer un préjudice potentiel; e) la mesure dans laquelle l’utilisation d’un système d’IA a déjà causé un préjudice à la santé et à la sécurité, a eu une incidence négative sur les droits fondamentaux ou a suscité de graves préoccupations quant à la probabilité de ce préjudice ou de cette incidence négative, tel que cela ressort, par exemple, des rapports ou allégations documentées soumis aux autorités nationales compétentes ou d’autres rapports, le cas échéant; f) l’ampleur potentielle d’un tel préjudice ou d’une telle incidence négative, notamment en ce qui concerne son intensité et sa capacité d’affecter plusieurs personnes ou d’affecter un groupe particulier de personnes de manière disproportionnée; g) la mesure dans laquelle les personnes ayant potentiellement subi un préjudice ou une incidence négative dépendent des résultats obtenus au moyen d’un système d’IA, notamment parce qu’il n’est pas raisonnablement possible, pour des raisons pratiques ou juridiques, de s’affranchir de ces résultats; h) la mesure dans laquelle il existe un déséquilibre de pouvoir, ou les personnes ayant potentiellement subi un préjudice ou une incidence négative se trouvent dans une situation vulnérable par rapport au déployeur d’un système d’IA, notamment en raison du statut, de l’autorité, de connaissances, de circonstances économiques ou sociales ou de l’âge; i) la mesure dans laquelle les résultats obtenus en utilisant un système d’IA sont facilement corrigibles ou réversibles, compte tenu des solutions techniques disponibles pour les corriger ou les inverser, les résultats qui ont une incidence négative sur la santé, la sécurité ou les droits fondamentaux ne devant pas être considérés comme facilement corrigibles ou réversibles; j) la probabilité que le déploiement du système d’IA présente des avantages pour certaines personnes, certains groupes de personnes ou la société dans son ensemble et la portée de ces avantages, y compris les améliorations éventuelles quant à la sécurité des produits; k) la mesure dans laquelle le droit existant de l’Union prévoit: i) des mesures de réparation efficaces en ce qui concerne les risques posés par un système d’IA, à l’exclusion des réclamations en dommages-intérêts; ii) des mesures efficaces destinées à prévenir ou à réduire substantiellement ces risques. »
- [4] « La mise sur le marché, la mise en service ou l’utilisation de systèmes d’IA pour l’évaluation ou la classification de personnes physiques ou de groupes de personnes au cours d’une période donnée en fonction de leur comportement social ou de caractéristiques personnelles ou de personnalité connues, déduites ou prédites, la note sociale conduisant à l’une ou l’autre des situations suivantes, ou aux deux: i) le traitement préjudiciable ou défavorable de certaines personnes physiques ou de groupes de personnes dans des contextes sociaux dissociés du contexte dans lequel les données ont été générées ou collectées à l’origine; ii) le traitement préjudiciable ou défavorable de certaines personnes ou de groupes de personnes, qui est injustifié ou disproportionné par rapport à leur comportement social ou à la gravité de celui-ci; »

RÉPONSE :
Avant d’utiliser ce logiciel, vous devez savoir que la notice d’utilisation doit inclure les informations suivantes : l’identité et les coordonnées du fournisseur, les caractéristiques du système d’IA, notamment sa destination, son niveau d’exactitude, ses limites de performance, les circonstances pouvant affecter son fonctionnement, les données d’entrée utilisées, les mesures de contrôle humain, les ressources nécessaires et les mises à jour logicielles [1]. Vous devez aussi savoir que le système doit être évalué selon sa destination, la nature des données traitées, le degré d’autonomie du système, la possibilité d’intervention humaine, les risques éventuels sur la santé, la sécurité ou les droits fondamentaux, la portée des préjudices potentiels, la dépendance des personnes aux résultats du système, les déséquilibres de pouvoir, la réversibilité des décisions, les avantages potentiels et les mesures de réparation existantes [2]. En outre, si le logiciel évalue ou classe des commerciaux selon leur comportement ou leurs caractéristiques personnelles, cela pourrait être interdit par l’AI Act, car cela constituerait un traitement préjudiciable ou défavorable de personnes sur la base de caractéristiques sociales ou personnelles, notamment s’il est injustifié ou disproportionné par rapport à leur comportement [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données personnelles ; traitements automatisés ; finalité du traitement ; données sensibles ; responsabilité du responsable ; transparence du traitement

Temps : recherche 33.4 s · génération 94.2 s (4132 tokens lus, 1977 écrits, 29.9 tokens/s) · contrôle de pertinence 14.9 s · reformulation 3.3 s

## a04 — Pendant nos réunions, un outil d'IA enregistre la discussion et rédige le compte rendu tout seul. Est-ce que je dois prévenir les participants ?

Article attendu : RGPD art. 13 ou RGPD art. 6, paragraphe 1 — absent des passages donnés au modèle.

### Réponse du copilote

> Oui : vous devez prévenir les participants, car l’outil d’IA interagit directement avec eux et enregistre leurs discussions, ce qui relève de l’obligation de transparence prévue à l’article 50, paragraphe 3, du règlement (UE) 2024/1689 (AI Act). Cette obligation exige que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation [3]. Puisque l’enregistrement automatique de la discussion et la rédaction du compte rendu sont effectués par un système d’IA, cela constitue une interaction directe avec des personnes physiques, et donc une situation couverte par cette obligation. Les extraits ne mentionnent pas d’exception pour les discussions ou les réunions, ni de cas où l’information n’est pas nécessaire. Ainsi, la prévention est obligatoire.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les systèmes d’IA à haut risque permettent, techniquement, l’enregistrement automatique des événements (journaux) tout au long de la durée de vie du système. »
  [1] « Pour les systèmes d’IA à haut risque visés à l’annexe III, point 1 a), les fonctionnalités de journalisation fournissent, au minimum: a) l’enregistrement de la période de chaque utilisation du système (date et heure de début et de fin pour chaque utilisation); … »
  [3] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »
  [4] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 12 : Enregistrement (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_12
  [3] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [4] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 4 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 65 : Création et structure du Comité européen de l’intelligence artificielle
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_65
  [5] AI Act — règlement (UE) 2024/1689, article 75 bis, point d : Pouvoirs de surveillance et de contrôle du Bureau de l'IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_75a
Attention : La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Cette obligation exige que les personnes physiques concernées soient informées qu’elles interagissent avec un système … ». Vérifiez qui est concerné.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les systèmes d’IA à haut risque permettent, techniquement, l’enregistrement automatique des événements (journaux) tout au long de la durée de vie du système. »  
- [1] « Pour les systèmes d’IA à haut risque visés à l’annexe III, point 1 a), les fonctionnalités de journalisation fournissent, au minimum: a) l’enregistrement de la période de chaque utilisation du système (date et heure de début et de fin pour chaque utilisation); … »  
- [3] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »  
- [4] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. »  

RÉPONSE :  
Oui : vous devez prévenir les participants, car l’outil d’IA interagit directement avec eux et enregistre leurs discussions, ce qui relève de l’obligation de transparence prévue à l’article 50, paragraphe 3, du règlement (UE) 2024/1689 (AI Act). Cette obligation exige que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation [3]. Puisque l’enregistrement automatique de la discussion et la rédaction du compte rendu sont effectués par un système d’IA, cela constitue une interaction directe avec des personnes physiques, et donc une situation couverte par cette obligation. Les extraits ne mentionnent pas d’exception pour les discussions ou les réunions, ni de cas où l’information n’est pas nécessaire. Ainsi, la prévention est obligatoire.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : utilisation d’un outil d’intelligence artificielle ; traitement automatisé des données ; enregistrement de données ; production de contenu ; participation à une discussion ; traitements de données

Temps : recherche 32.3 s · génération 36.4 s (3279 tokens lus, 563 écrits, 33.3 tokens/s) · contrôle de pertinence 5.3 s · reformulation 3.7 s

## a05 — On veut publier sur notre site et sur Facebook les photos de la fête de l'association, où l'on voit des adhérents et leurs enfants. Faut-il leur demander la permission ?

Article attendu : RGPD art. 6, paragraphe 1 ou RGPD art. 7 — passage [5].

### Réponse du copilote

> Oui : vous devez obtenir le consentement des titulaires de la responsabilité parentale à l'égard des enfants, conformément à l'article 40, point g) du RGPD [1]. Ce consentement doit être obtenu de manière claire et accessible, comme prévus dans l'article 7, point 2 du RGPD [5]. Le retrait du consentement est possible à tout moment, sans affecter la licéité des données collectées auparavant [5]. La demande de consentement doit être distincte des autres questions dans une déclaration écrite, et formulée de manière simple [5].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « g) les informations communiquées aux enfants et la protection dont bénéficient les enfants et la manière d'obtenir le consentement des titulaires de la responsabilité parentale à l'égard de l'enfant; »
  [5] « 4. Au moment de déterminer si le consentement est donné librement, il y a lieu de tenir le plus grand compte de la question de savoir, entre autres, si l'exécution d'un contrat, y compris la fourniture d'un service, est subordonnée au consentement au traitement de données à caractère personnel qui n'est pas nécessaire à l'exécution dudit contrat. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [5] RGPD — règlement (UE) 2016/679, article 7 : Conditions applicables au consentement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_7
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 40, paragraphe 1 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [3] RGPD — règlement (UE) 2016/679, article 35, paragraphe 9 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [4] RGPD — règlement (UE) 2016/679, article 35, paragraphe 1 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « g) les informations communiquées aux enfants et la protection dont bénéficient les enfants et la manière d'obtenir le consentement des titulaires de la responsabilité parentale à l'égard de l'enfant; »  
- [5] « 4. Au moment de déterminer si le consentement est donné librement, il y a lieu de tenir le plus grand compte de la question de savoir, entre autres, si l'exécution d'un contrat, y compris la fourniture d'un service, est subordonnée au consentement au traitement de données à caractère personnel qui n'est pas nécessaire à l'exécution dudit contrat. »  

RÉPONSE :  
Oui : vous devez obtenir le consentement des titulaires de la responsabilité parentale à l'égard des enfants, conformément à l'article 40, point g) du RGPD [1]. Ce consentement doit être obtenu de manière claire et accessible, comme prévus dans l'article 7, point 2 du RGPD [5]. Le retrait du consentement est possible à tout moment, sans affecter la licéité des données collectées auparavant [5]. La demande de consentement doit être distincte des autres questions dans une déclaration écrite, et formulée de manière simple [5].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données personnelles ; image ; représentation ; personne physique ; traitement ; consentement

Temps : recherche 25.2 s · génération 20.1 s (2395 tokens lus, 297 écrits, 35.8 tokens/s) · contrôle de pertinence 3.6 s · reformulation 3.1 s

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
  [2] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [3] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [4] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [5] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun  
RÉPONSE : Les textes trouvés ne traitent pas de ce point.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : congés payés ; durée ; emploi ; période ; salaire ; temps partiel

Temps : recherche 30.5 s · génération 25.8 s (3869 tokens lus, 26 écrits, 33.6 tokens/s) · reformulation 2.9 s
