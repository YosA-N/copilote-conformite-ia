# Réponses du copilote — final_local_author

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 17/11/2026 à 23:37 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen3:4b-instruct` via Ollama 0.40.16 — température 0.1, contexte 8192 tokens, couches sur la carte graphique : toutes, 2000 tokens au plus par réponse
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_author.jsonl` (5 + 1 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| a01 | J'ai 12 salariés et je voudrais remplacer la badgeuse par une pointeuse à empreinte digitale. J'ai le droit ? | 3/3 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 94 s |
| a02 | Un partenaire commercial me propose de racheter notre fichier clients. Est-ce que je peux le lui vendre ? | 4/5 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 113 s |
| a03 | Je pense acheter un logiciel d'IA qui note les résultats de mes commerciaux et propose qui mérite une prime. Qu'est-ce que je dois savoir avant de l'utiliser ? | 5/5 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 248 s |
| a04 | Pendant nos réunions, un outil d'IA enregistre la discussion et rédige le compte rendu tout seul. Est-ce que je dois prévenir les participants ? | 3/3 | non | La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui, vous devez prévenir les participants, car l’outil d’IA interagit directement avec eux pendant les réunions, ce qui … » (et 3 autre(s)). Vérifiez qui est concerné. | 107 s |
| a05 | On veut publier sur notre site et sur Facebook les photos de la fête de l'association, où l'on voit des adhérents et leurs enfants. Faut-il leur demander la permission ? | 3/3 | non | — | 48 s |
| ha01 | Combien de jours de congés payés a un salarié à temps partiel ? | 0/0 | oui | — | 20 s |

## a01 — J'ai 12 salariés et je voudrais remplacer la badgeuse par une pointeuse à empreinte digitale. J'ai le droit ?

Article attendu : RGPD art. 9, paragraphe 1 ou RGPD art. 9, paragraphe 2 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 48 : Marquage CE
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_48
  [2] RGPD — règlement (UE) 2016/679, article 20 : Droit à la portabilité des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_20
  [3] RGPD — règlement (UE) 2016/679, article 22 : Décision individuelle automatisée, y compris le profilage
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_22
  [4] RGPD — règlement (UE) 2016/679, article 47, paragraphe 2, points a) à k) : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
  [5] RGPD — règlement (UE) 2016/679, article 47, paragraphe 1 : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [2] « Les personnes concernées ont le droit de recevoir les données à caractère personnel les concernant qu'elles ont fournies à un responsable du traitement, dans un format structuré, couramment utilisé et lisible par machine, et ont le droit de transmettre ces données à un autre responsable du traitement sans que le responsable du traitement auquel les données à caractère personnel ont été communiquées y fasse obstacle, lorsque: a) le traitement est fondé sur le consentement en application de l'article 6, paragraphe 1, point a), ou de l'article 9, paragraphe 2, point a), ou sur un contrat en application de l'article 6, paragraphe 1, point b); et b) le traitement est effectué à l'aide de procédés automatisés. »  
- [3] « La personne concernée a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé, y compris le profilage, produisant des effets juridiques la concernant ou l'affectant de manière significative de façon similaire. »  
- [4] « Les règles d'entreprise contraignantes visées au paragraphe 1 précisent au moins: a) la structure et les coordonnées du groupe d'entreprises ou du groupe d'entreprises engagées dans une activité économique conjointe et de chacune de leurs entités; b) les transferts ou l'ensemble des transferts de données, y compris les catégories de données à caractère personnel, le type de traitement et ses finalités, le type de personnes concernées affectées et le nom du ou des pays tiers en question; c) leur nature juridiquement contraignante, tant interne qu'externe; … e) les droits des personnes concernées à l'égard du traitement et les moyens d'exercer ces droits y compris le droit de ne pas faire l'objet de décisions fondées exclusivement sur un traitement automatisé, y compris le profilage, conformément à l'article 22, le droit d'introduire une réclamation auprès de l'autorité de contrôle compétente et devant les juridictions compétentes des États membres conformément à l'article 79 et d'obtenir réparation et, le cas échéant, une indemnisation pour violation des règles d'entreprise contraignantes; … »  

RÉPONSE :  
Oui, vous avez le droit de remplacer la badgeuse par une pointeuse à empreinte digitale, car le traitement automatisé de données biométriques (comme les empreintes digitales) est couvert par le droit à la portabilité des données (RGPD, article 20) et par le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé (RGPD, article 22). Cependant, ce droit ne s'applique pas si le traitement est fondé sur un contrat ou sur le consentement explicite, ou si les données sont utilisées pour des décisions juridiquement significatives. En outre, si vous avez 12 salariés, vous devez respecter les obligations de transparence et de droit à l'intervention humaine (RGPD, article 22), notamment en leur assurant le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé. Ces obligations sont précisées dans les règles d'entreprise contraignantes (RGPD, article 47), qui doivent inclure les droits des personnes concernées, notamment le droit de contester une décision automatisée. Aucun passage ne indique que ce type de changement est interdit par le RGPD ou l'AI Act, mais les données biométriques sont soumises à des règles spécifiques en matière de traitement automatisé.
```

</details>

Temps : recherche 5.6 s · génération 79.6 s (3726 tokens lus, 865 écrits, 18.3 tokens/s) · contrôle de pertinence 8.3 s

## a02 — Un partenaire commercial me propose de racheter notre fichier clients. Est-ce que je peux le lui vendre ?

Article attendu : RGPD art. 6, paragraphe 1 ou RGPD art. 5 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, annexe VIII, point 1 : Informations à fournir lors de l'enregistrement d'un système d'IA à haut risque conformément à l'article 49
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_VIII
  [2] AI Act — règlement (UE) 2024/1689, annexe VIII, point 1 : Informations à fournir lors de l'enregistrement d'un système d'IA à haut risque conformément à l'article 49
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_VIII
  [3] RGPD — règlement (UE) 2016/679, article 48 : Transferts ou divulgations non autorisés par le droit de l'Union
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_48
  [4] RGPD — règlement (UE) 2016/679, article 47, paragraphe 2, points a) à k) : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
  [5] RGPD — règlement (UE) 2016/679, article 47, paragraphe 1 : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « les informations ci-après sont fournies et mises à jour par la suite en ce qui concerne les systèmes d'IA à enregistrer conformément à l'article 49, paragraphe 2: 1. le nom, l'adresse et les coordonnées du fournisseur; »  
- [2] « les informations ci-après sont fournies et mises à jour par la suite en ce qui concerne les systèmes d'IA à haut risque à enregistrer conformément à l'article 49, paragraphe 1: 1. le nom, l'adresse et les coordonnées du fournisseur; »  
- [3] « Toute décision d'une juridiction ou d'une autorité administrative d'un pays tiers exigeant d'un responsable du traitement ou d'un sous-traitant qu'il transfère ou divulgue des données à caractère personnel ne peut être reconnue ou rendue exécutoire de quelque manière que ce soit qu'à la condition qu'elle soit fondée sur un accord international, tel qu'un traité d'entraide judiciaire, en vigueur entre le pays tiers demandeur et l'Union ou un État membre, sans préjudice d'autres motifs de transfert en vertu du présent chapitre. »  
- [4] « 2. Les règles d'entreprise contraignantes visées au paragraphe 1 précisent au moins: a) la structure et les coordonnées du groupe d'entreprises ou du groupe d'entreprises engagées dans une activité économique conjointe et de chacune de leurs entités; b) les transferts ou l'ensemble des transferts de données, y compris les catégories de données à caractère personnel, le type de traitement et ses finalités, le type de personnes concernées affectées et le nom du ou des pays tiers en question; … e) les droits des personnes concernées à l'égard du traitement et les moyens d'exercer ces droits y compris le droit de ne pas faire l'objet de décisions fondées exclusivement sur un traitement automatisé, y compris le profilage, conformément à l'article 22, le droit d'introduire une réclamation auprès de l'autorité de contrôle compétente et devant les juridictions compétentes des États membres conformément à l'article 79 et d'obtenir réparation et, le cas échéant, une indemnisation pour violation des règles d'entreprise contraignantes; … h) les missions de tout délégué à la protection des données, désigné conformément à l'article 37, ou de toute autre personne ou entité chargée de la surveillance du respect des règles d'entreprise contraignantes au sein du groupe d'entreprises, ou du groupe d'entreprises engagées dans une activité économique conjointe, ainsi que le suivi de la formation et le traitement des réclamations; … j) les procédures de réclamation; … k) les mécanismes mis en place pour communiquer et consigner les modifications apportées aux règles et pour communiquer ces modifications à l'autorité de contrôle compétente; »  
- [5] « 1. L'autorité de contrôle compétente approuve des règles d'entreprise contraignantes conformément au mécanisme de contrôle de la cohérence prévu à l'article 63, à condition que: a) ces règles soient juridiquement contraignantes, et soient mises en application par toutes les entités concernées du groupe d'entreprises ou du groupe d'entreprises engagées dans une activité économique conjointe, y compris leurs employés; b) elles confèrent expressément aux personnes concernées des droits opposables en ce qui concerne le traitement de leurs données à caractère personnel; et c) elles répondent aux exigences prévues au paragraphe 2. »

RÉPONSE :  
Non, vous ne pouvez pas vendre votre fichier clients à un partenaire commercial sans respecter les règles du RGPD, notamment en ce qui concerne le traitement des données à caractère personnel. Le RGPD, article 47, impose que les règles d'entreprise contraignantes, qui peuvent régir les transferts de données, doivent être juridiquement contraignantes, conférer des droits aux personnes concernées et répondre aux exigences prévues au paragraphe 2 [5]. Ces règles doivent préciser les transferts de données, y compris les catégories de données, les finalités, les personnes concernées et les pays tiers [4]. Si le transfert est effectué à l'extérieur de l'Union, il doit être fondé sur un accord international ou des garanties appropriées [3]. Les données à caractère personnel ne peuvent pas être transférées sans que ces conditions soient remplies, et les personnes concernées doivent être informées de leurs droits, notamment le droit de ne pas faire l'objet de décisions fondées sur un traitement automatisé [4]. Ainsi, la vente d’un fichier clients implique un transfert de données à caractère personnel, qui doit être autorisé conformément au RGPD, notamment par des règles d’entreprise contraignantes validées par l’autorité de contrôle [4][5]. Les passages trouvés ne traitent pas directement de la vente d’un fichier clients, mais ils établissent que tout transfert de données à caractère personnel doit respecter les obligations du RGPD, notamment celles relatives à la finalité, la transparence, les droits des personnes concernées et les conditions de transfert [3][4][5].
```

</details>

Temps : recherche 2.5 s · génération 102.1 s (2920 tokens lus, 1247 écrits, 15.6 tokens/s) · contrôle de pertinence 8.5 s

## a03 — Je pense acheter un logiciel d'IA qui note les résultats de mes commerciaux et propose qui mérite une prime. Qu'est-ce que je dois savoir avant de l'utiliser ?

Article attendu : AI Act annexe III, point 4 ou AI Act art. 26, paragraphe 7 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [2] AI Act — règlement (UE) 2024/1689, article 6, point d : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
  [3] AI Act — règlement (UE) 2024/1689, article 6, paragraphe 4 : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
  [4] AI Act — règlement (UE) 2024/1689, article 6, paragraphe 1 : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
  [5] AI Act — règlement (UE) 2024/1689, annexe III, point 8 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. Cette obligation ne s’applique pas aux systèmes d’IA dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers, sauf si ces systèmes sont mis à la disposition du public pour permettre le signalement d’une infraction pénale. »  
- [2] « d) le système d’IA est destiné à exécuter une tâche préparatoire en vue d’une évaluation pertinente aux fins des cas d’utilisation visés à l’annexe III. »  
- [3] « Un fournisseur qui considère qu’un système d’IA visé à l’annexe III n’est pas à haut risque documente son évaluation avant que ce système ne soit mis sur le marché ou mis en service. Ce fournisseur est soumis à l’obligation d’enregistrement visée à l’article 49, paragraphe 2. À la demande des autorités nationales compétentes, le fournisseur fournit la documentation de l’évaluation. »  
- [4] « Un système d’IA mis sur le marché ou mis en service, qu’il soit ou non indépendant des produits visés aux points a) et b), est considéré comme étant à haut risque lorsque les deux conditions suivantes sont remplies: a) le système d’IA est destiné à être utilisé comme composant de sécurité d’un produit couvert par la législation d’harmonisation de l’Union dont la liste figure à l’annexe I, ou le système d’IA constitue lui-même un tel produit; b) le produit dont le composant de sécurité visé au point a) est le système d’IA, ou le système d’IA lui-même en tant que produit, est soumis à une évaluation de conformité par un tiers en vue de la mise sur le marché ou de la mise en service de ce produit conformément à la législation d’harmonisation de l’Union dont la liste figure à l’annexe I. »  
- [5] « Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des domaines suivants: 8. Administration de la justice et processus démocratiques: a) systèmes d'IA destinés à être utilisés par les autorités judiciaires ou en leur nom, pour les aider à rechercher et à interpréter les faits ou la loi, et à appliquer la loi à un ensemble concret de faits, ou à être utilisés de manière similaire lors du règlement extrajudiciaire d'un litige; b) systèmes d'IA destinés à être utilisés pour influencer le résultat d'une élection ou d'un référendum ou le comportement électoral de personnes physiques dans l'exercice de leur vote lors d'élections ou de référendums. Sont exclus les systèmes d'IA aux sorties desquels les personnes physiques ne sont pas directement exposées, tels que les outils utilisés pour organiser, optimiser ou structurer les campagnes politiques sous l'angle administratif ou logistique. »  

RÉPONSE :  
Avant d’utiliser ce logiciel d’IA, vous devez savoir que, selon l’AI Act, un système d’IA qui évalue les performances de vos commerciaux et propose des primes peut être considéré comme un système à haut risque, car il implique une évaluation de personnes physiques (les commerciaux) et une décision influençant leur récompense. Cela signifie que le fournisseur doit justifier que ce système n’est pas classé comme à haut risque, en documentant son évaluation avant la mise en service [3]. Cette obligation s’applique si le système est utilisé comme composant de sécurité d’un produit ou s’il est lui-même un produit soumis à une évaluation de conformité [4]. Cependant, ce type de système ne relève pas des domaines de l’administration de la justice ou de l’influence sur les élections, donc il n’est pas inclus dans les systèmes à haut risque visés à l’annexe III [5]. En revanche, l’obligation de transparence s’applique : les utilisateurs doivent être clairement informés qu’ils interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation [1].
```

</details>

Temps : recherche 2.5 s · génération 228.4 s (2383 tokens lus, 1168 écrits, 5.5 tokens/s) · contrôle de pertinence 17.1 s

## a04 — Pendant nos réunions, un outil d'IA enregistre la discussion et rédige le compte rendu tout seul. Est-ce que je dois prévenir les participants ?

Article attendu : RGPD art. 13 ou RGPD art. 6, paragraphe 1 — absent des passages donnés au modèle.

### Réponse du copilote

> Oui, vous devez prévenir les participants, car l’outil d’IA interagit directement avec eux pendant les réunions, ce qui relève de l’obligation de transparence prévue à l’article 50 de l’AI Act [4]. Cette obligation exige que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation [4]. Comme l’outil rédige un compte rendu automatique à partir de la discussion, il s’agit d’un système d’IA destiné à interagir directement avec des personnes physiques, et donc de l’application de l’obligation de transparence [4]. Cette obligation ne s’applique pas dans des cas spécifiques comme la prévention ou la détection d’infractions pénales, mais ici, il n’y a pas de mention de tel usage, donc la condition d’exemption ne s’applique pas [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les systèmes d’IA à haut risque permettent, techniquement, l’enregistrement automatique des événements (journaux) tout au long de la durée de vie du système. »
  [1] « Pour les systèmes d’IA à haut risque visés à l’annexe III, point 1 a), les fonctionnalités de journalisation fournissent, au minimum: a) l’enregistrement de la période de chaque utilisation du système (date et heure de début et de fin pour chaque utilisation); b) la base de données de référence utilisée par le système pour vérifier les données d’entrée; c) les données d’entrée pour lesquelles la recherche a abouti à une correspondance; d) l’identification des personnes physiques participant à la vérification des résultats, visées à l’article 14, paragraphe 5. »
  [4] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. Cette obligation ne s’applique pas aux systèmes d’IA dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers, sauf si ces systèmes sont mis à la disposition du public pour permettre le signalement d’une infraction pénale. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 12 : Enregistrement (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_12
  [4] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 75, paragraphe 1 quinquies : Surveillance du marché et contrôle des systèmes d'IA et assistance mutuelle
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_75
  [3] AI Act — règlement (UE) 2024/1689, article 75, paragraphe 1 : Surveillance du marché et contrôle des systèmes d'IA et assistance mutuelle
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_75
  [5] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 2 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
Attention : La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui, vous devez prévenir les participants, car l’outil d’IA interagit directement avec eux pendant les réunions, ce qui … » (et 3 autre(s)). Vérifiez qui est concerné.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les systèmes d’IA à haut risque permettent, techniquement, l’enregistrement automatique des événements (journaux) tout au long de la durée de vie du système. »
- [1] « Pour les systèmes d’IA à haut risque visés à l’annexe III, point 1 a), les fonctionnalités de journalisation fournissent, au minimum: a) l’enregistrement de la période de chaque utilisation du système (date et heure de début et de fin pour chaque utilisation); b) la base de données de référence utilisée par le système pour vérifier les données d’entrée; c) les données d’entrée pour lesquelles la recherche a abouti à une correspondance; d) l’identification des personnes physiques participant à la vérification des résultats, visées à l’article 14, paragraphe 5. »
- [4] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. Cette obligation ne s’applique pas aux systèmes d’IA dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers, sauf si ces systèmes sont mis à la disposition du public pour permettre le signalement d’une infraction pénale. »

RÉPONSE :
Oui, vous devez prévenir les participants, car l’outil d’IA interagit directement avec eux pendant les réunions, ce qui relève de l’obligation de transparence prévue à l’article 50 de l’AI Act [4]. Cette obligation exige que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation [4]. Comme l’outil rédige un compte rendu automatique à partir de la discussion, il s’agit d’un système d’IA destiné à interagir directement avec des personnes physiques, et donc de l’application de l’obligation de transparence [4]. Cette obligation ne s’applique pas dans des cas spécifiques comme la prévention ou la détection d’infractions pénales, mais ici, il n’y a pas de mention de tel usage, donc la condition d’exemption ne s’applique pas [4].
```

</details>

Temps : recherche 2.5 s · génération 96.8 s (2875 tokens lus, 676 écrits, 9.9 tokens/s) · contrôle de pertinence 8.1 s

## a05 — On veut publier sur notre site et sur Facebook les photos de la fête de l'association, où l'on voit des adhérents et leurs enfants. Faut-il leur demander la permission ?

Article attendu : RGPD art. 6, paragraphe 1 ou RGPD art. 7 — absent des passages donnés au modèle.

### Réponse du copilote

> Oui : vous devez demander la permission des personnes concernées, notamment des enfants, car le traitement de leurs données à caractère personnel (comme les photos) est soumis à des obligations de consentement (RGPD, article 35, point 9 et article 8, paragraphe 1). Si l'enfant est âgé de moins de 16 ans, ce traitement n'est licite que si le consentement est donné ou autorisé par le titulaire de la responsabilité parentale à l'égard de l'enfant [3]. Le responsable du traitement doit donc demander l'avis des personnes concernées ou de leurs représentants [1]. Cette obligation s'applique à la publication sur les réseaux sociaux comme Facebook, même si les photos sont prises lors d'une fête d'association [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le cas échéant, le responsable du traitement demande l'avis des personnes concernées ou de leurs représentants au sujet du traitement prévu, sans préjudice de la protection des intérêts généraux ou commerciaux ou de la sécurité des opérations de traitement. »
  [3] « Lorsque l'enfant est âgé de moins de 16 ans, ce traitement n'est licite que si, et dans la mesure où, le consentement est donné ou autorisé par le titulaire de la responsabilité parentale à l'égard de l'enfant. »
  [4] « Lorsque la personne concernée en fait la demande, les informations peuvent être fournies oralement, à condition que l'identité de la personne concernée soit démontrée par d'autres moyens. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 35, paragraphe 9 : Analyse d'impact relative à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [3] RGPD — règlement (UE) 2016/679, article 8 : Conditions applicables au consentement des enfants en ce qui concerne les services de la société de l'information (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_8
  [4] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 35, paragraphe 1 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [5] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Le cas échéant, le responsable du traitement demande l'avis des personnes concernées ou de leurs représentants au sujet du traitement prévu, sans préjudice de la protection des intérêts généraux ou commerciaux ou de la sécurité des opérations de traitement. »  
- [3] « Lorsque l'enfant est âgé de moins de 16 ans, ce traitement n'est licite que si, et dans la mesure où, le consentement est donné ou autorisé par le titulaire de la responsabilité parentale à l'égard de l'enfant. »  
- [4] « Lorsque la personne concernée en fait la demande, les informations peuvent être fournies oralement, à condition que l'identité de la personne concernée soit démontrée par d'autres moyens. »

RÉPONSE :  
Oui : vous devez demander la permission des personnes concernées, notamment des enfants, car le traitement de leurs données à caractère personnel (comme les photos) est soumis à des obligations de consentement (RGPD, article 35, point 9 et article 8, paragraphe 1). Si l'enfant est âgé de moins de 16 ans, ce traitement n'est licite que si le consentement est donné ou autorisé par le titulaire de la responsabilité parentale à l'égard de l'enfant [3]. Le responsable du traitement doit donc demander l'avis des personnes concernées ou de leurs représentants [1]. Cette obligation s'applique à la publication sur les réseaux sociaux comme Facebook, même si les photos sont prises lors d'une fête d'association [1].
```

</details>

Temps : recherche 2.6 s · génération 39.6 s (2523 tokens lus, 372 écrits, 16.4 tokens/s) · contrôle de pertinence 5.6 s

## ha01 — Combien de jours de congés payés a un salarié à temps partiel ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [3] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [4] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 6 bis : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [5] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 1 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun  
RÉPONSE : Les textes trouvés ne traitent pas de ce point.
```

</details>

Temps : recherche 2.3 s · génération 17.4 s (2447 tokens lus, 26 écrits, 17.1 tokens/s)
