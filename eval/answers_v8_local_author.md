# Réponses du copilote — v8_local_author

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 27/11/2026 à 20:03 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen3:4b-instruct` via Ollama 0.40.18 — température 0.1, contexte 8192 tokens, couches sur la carte graphique : toutes, 2000 tokens au plus par réponse, dont 800 gardés pour la réponse (recopie des extraits arrêtée après 1200 tokens si la réponse n'a pas commencé)
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_author.jsonl` (5 + 1 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| a01 | J'ai 12 salariés et je voudrais remplacer la badgeuse par une pointeuse à empreinte digitale. J'ai le droit ? | 3/3 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 59 s |
| a02 | Un partenaire commercial me propose de racheter notre fichier clients. Est-ce que je peux le lui vendre ? | 1/2 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 60 s |
| a03 | Je pense acheter un logiciel d'IA qui note les résultats de mes commerciaux et propose qui mérite une prime. Qu'est-ce que je dois savoir avant de l'utiliser ? | 5/5 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 62 s |
| a04 | Pendant nos réunions, un outil d'IA enregistre la discussion et rédige le compte rendu tout seul. Est-ce que je dois prévenir les participants ? | 4/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 45 s |
| a05 | On veut publier sur notre site et sur Facebook les photos de la fête de l'association, où l'on voit des adhérents et leurs enfants. Faut-il leur demander la permission ? | 3/3 | non | — | 30 s |
| ha01 | Combien de jours de congés payés a un salarié à temps partiel ? | 0/0 | oui | — | 15 s |

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
Oui, vous avez le droit de remplacer la badgeuse par une pointeuse à empreinte digitale, car le traitement automatisé de données biométriques (comme les empreintes digitales) est couvert par le droit à la portabilité des données (RGPD, article 20) et par le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé (RGPD, article 22). Cependant, ce droit ne s'applique pas si le traitement est fondé sur un contrat ou sur le consentement explicite, ou si des mesures appropriées sont mises en place pour garantir la protection des droits de la personne concernée. En outre, si vous avez 12 salariés, vous devez respecter les obligations de transparence et de communication des droits des personnes concernées, notamment le droit de ne pas faire l'objet d'une décision fondée sur un traitement automatisé, conformément à l’article 22 du RGPD [3]. Ces droits doivent être clairement communiqués aux salariés, notamment via les règles d’entreprise contraignantes, qui doivent inclure les droits liés au traitement automatisé [4].
```

</details>

Temps : recherche 2.6 s · génération 49.4 s (3726 tokens lus, 817 écrits, 32.2 tokens/s) · contrôle de pertinence 6.6 s

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
  [4] AI Act — règlement (UE) 2024/1689, article 72 : Surveillance après commercialisation par les fournisseurs et plan de surveillance après commercialisation pour les systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_72
  [5] RGPD — règlement (UE) 2016/679, article 47, paragraphe 2, points a) à k) : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [3] « Toute décision d'une juridiction ou d'une autorité administrative d'un pays tiers exigeant d'un responsable du traitement ou d'un sous-traitant qu'il transfère ou divulgue des données à caractère personnel ne peut être reconnue ou rendue exécutoire de quelque manière que ce soit qu'à la condition qu'elle soit fondée sur un accord international, tel qu'un traité d'entraide judiciaire, en vigueur entre le pays tiers demandeur et l'Union ou un État membre, sans préjudice d'autres motifs de transfert en vertu du présent chapitre. »  
- [5] « Les règles d'entreprise contraignantes visées au paragraphe 1 précisent au moins: … b) les transferts ou l'ensemble des transferts de données, y compris les catégories de données à caractère personnel, le type de traitement et ses finalités, le type de personnes concernées affectées et le nom du ou des pays tiers en question; … d) l'application des principes généraux relatifs à la protection des données, notamment la limitation de la finalité, la minimisation des données, la limitation des durées de conservation des données, la qualité des données, la protection des données dès la conception et la protection des données par défaut, la base juridique du traitement, le traitement de catégories particulières de données à caractère personnel, les mesures visant à garantir la sécurité des données, ainsi que les exigences en matière de transferts ultérieurs à des organismes qui ne sont pas liés par les règles d'entreprise contraignantes; … e) les droits des personnes concernées à l'égard du traitement et les moyens d'exercer ces droits y compris le droit de ne pas faire l'objet de décisions fondées exclusivement sur un traitement automatisé, y compris le profilage, conformément à l'article 22, le droit d'introduire une réclamation auprès de l'autorité de contrôle compétente et devant les juridictions compétentes des États membres conformément à l'article 79 et d'obtenir réparation et, le cas échéant, une indemnisation pour violation des règles d'entreprise contraignantes; … g) la manière dont les informations sur les règles d'entreprise contraignantes, notamment en ce qui concerne les éléments mentionnés aux points d), e) et f) du présent paragraphe sont fournies aux personnes concernées, en sus des informations visées aux articles 13 et 14; … h) les missions de tout délégué à la protection des données, désigné conformément à l'article 37, ou de toute autre personne ou entité chargée de la surveillance du respect des règles d'entreprise contraignantes au sein du groupe d'entreprises, ou du groupe d'entreprises engagées dans une activité économique conjointe, ainsi que le suivi de la formation et le traitement des réclamations; … j) les procédures de réclamation; … k) les mécanismes mis en place pour communiquer et consigner les modifications apportées aux règles et pour communiquer ces modifications à l'autorité de contrôle; »  

RÉPONSE :  
Non, vous ne pouvez pas vendre votre fichier clients à un partenaire commercial sans respecter les obligations de protection des données personnelles prévues par le RGPD. Le RGPD, article 47, exige que les transferts de données à caractère personnel soient fondés sur des bases juridiques appropriées, notamment la limitation de la finalité, la minimisation des données, la limitation des durées de conservation, la qualité des données, la protection des données dès la conception, la base juridique du traitement, le traitement de catégories particulières de données, les mesures de sécurité et les exigences en matière de transferts ultérieurs à des organismes non liés par les règles d'entreprise contraignantes [5]. Si le transfert est effectué à un pays tiers, il doit être fondé sur un accord international en vigueur (comme un traité d'entraide judiciaire) ou sur des garanties appropriées [3]. Aucun transfert de données à caractère personnel ne peut être effectué sans que les personnes concernées soient informées des droits qu’elles ont sur leurs données, notamment le droit de ne pas faire l’objet de décisions fondées sur un traitement automatisé [5]. Ces obligations s’appliquent à tout transfert, y compris une vente de fichiers clients. Les règles d'entreprise contraignantes doivent préciser les transferts de données, les finalités, les catégories de données, les personnes concernées et les pays tiers [5]. La vente implique un transfert, donc elle doit être conforme à ces exigences.
```

</details>

Temps : recherche 2.2 s · génération 53.7 s (3366 tokens lus, 1075 écrits, 32.7 tokens/s) · contrôle de pertinence 4.4 s

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
Avant d’utiliser ce logiciel d’IA, vous devez savoir que, selon l’AI Act, un système d’IA qui évalue les performances de vos commerciaux et propose des primes peut être classé comme système à haut risque, car il implique un profilage de personnes physiques (article 6, paragraphe 2, point d), et que ce profilage peut être considéré comme une tâche préparatoire à une évaluation pertinente dans un domaine visé à l’annexe III (article 6, point d). Cela signifie que le fournisseur doit documenter son évaluation de risque avant la mise en service du logiciel (article 6, point 3), et que cette documentation peut être demandée par les autorités nationales (article 6, point 3). De plus, le logiciel doit informer les utilisateurs qu’ils interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation [1]. Ce point s’applique à tous les systèmes d’IA destinés à interagir directement avec des personnes physiques, y compris les outils de gestion des commerciaux. Les systèmes d’IA à haut risque sont répertoriés dans le domaine de l’administration de la justice ou des processus démocratiques (annexe III, point 8), mais ce domaine ne s’applique pas à l’analyse des performances commerciales, donc il est probable que ce logiciel ne relève pas de ce cadre spécifique [5]. Toutefois, le fait qu’il effectue un profilage de personnes physiques (comme les commerciaux) peut le rendre soumis à des obligations de transparence et de documentation, même si ce n’est pas explicitement dans un domaine de l’annexe III. Vous devez donc vérifier que le logiciel est bien classé comme système à haut risque ou non, et que le fournisseur a documenté son évaluation, en particulier en cas de mise en service ou de mise sur le marché [3].
```

</details>

Temps : recherche 2.2 s · génération 51.0 s (2383 tokens lus, 1343 écrits, 34.6 tokens/s) · contrôle de pertinence 8.5 s

## a04 — Pendant nos réunions, un outil d'IA enregistre la discussion et rédige le compte rendu tout seul. Est-ce que je dois prévenir les participants ?

Article attendu : RGPD art. 13 ou RGPD art. 6, paragraphe 1 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 12 : Enregistrement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_12
  [2] AI Act — règlement (UE) 2024/1689, article 90 : Alertes de risques systémiques données par le groupe scientifique
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_90
  [3] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 2 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [4] AI Act — règlement (UE) 2024/1689, article 75, paragraphe 1 quinquies : Surveillance du marché et contrôle des systèmes d'IA et assistance mutuelle
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_75
  [5] AI Act — règlement (UE) 2024/1689, article 75, paragraphe 1 : Surveillance du marché et contrôle des systèmes d'IA et assistance mutuelle
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_75
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les systèmes d’IA à haut risque permettent, techniquement, l’enregistrement automatique des événements (journaux) tout au long de la durée de vie du système. »  
- [1] « Pour les systèmes d’IA à haut risque visés à l’annexe III, point 1 a), les fonctionnalités de journalisation fournissent, au minimum: a) l’enregistrement de la période de chaque utilisation du système (date et heure de début et de fin pour chaque utilisation); … »  
- [3] « Les fournisseurs de systèmes d’IA, y compris de systèmes d’IA à usage général, qui génèrent des contenus de synthèse de type audio, image, vidéo ou texte, veillent à ce que les sorties des systèmes d’IA soient marquées dans un format lisible par machine et identifiables comme ayant été générées ou manipulées par une IA. »  
- [3] « Cette obligation ne s’applique pas dans la mesure où les systèmes d’IA remplissent une fonction d’assistance pour la mise en forme standard ou ne modifient pas de manière substantielle les données d’entrée fournies par le déployeur ou leur sémantique, ou lorsque leur utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. »

RÉPONSE :  
Oui, vous devez prévenir les participants, car l’outil d’IA enregistre automatiquement la discussion et rédige le compte rendu, ce qui constitue une fonction de synthèse de type audio ou texte générée par une IA. Selon l’article 50, les fournisseurs de systèmes d’IA à usage général doivent veiller à ce que les sorties soient marquées comme ayant été générées par une IA [3]. Cette obligation s’applique à l’outil en question, car il génère un contenu de synthèse à partir d’une discussion. Cependant, cette obligation ne s’applique pas si l’outil ne modifie pas de manière substantielle les données d’entrée ou s’il remplit une fonction d’assistance pour la mise en forme standard [3]. Si l’outil ne modifie pas de manière substantielle les données d’entrée ou s’il est utilisé dans un cadre de prévention ou de détection d’infractions pénales, l’obligation de marquage ne s’applique pas. Dans ce cas, la prévention des participants n’est pas obligatoire. Mais comme la question concerne l’enregistrement et la rédaction du compte rendu, et que l’outil génère un contenu de synthèse à partir d’un échange humain, il est probable qu’il modifie de manière substantielle les données d’entrée, donc l’obligation s’applique. Ainsi, pour garantir la transparence, vous devez prévenir les participants que le compte rendu a été généré par un outil d’IA [3].
```

</details>

Temps : recherche 2.2 s · génération 37.1 s (2950 tokens lus, 698 écrits, 34.1 tokens/s) · contrôle de pertinence 5.7 s

## a05 — On veut publier sur notre site et sur Facebook les photos de la fête de l'association, où l'on voit des adhérents et leurs enfants. Faut-il leur demander la permission ?

Article attendu : RGPD art. 6, paragraphe 1 ou RGPD art. 7 — absent des passages donnés au modèle.

### Réponse du copilote

> Oui : vous devez demander la permission des personnes concernées, notamment des enfants, car le traitement de leurs données à caractère personnel (comme les photos) est soumis à des obligations de consentement (RGPD, article 8, paragraphe 1). Si l'enfant est âgé de moins de 16 ans, ce traitement n'est licite que si le consentement est donné ou autorisé par le titulaire de la responsabilité parentale à l'égard de l'enfant [3]. Le responsable du traitement doit, le cas échéant, demander l'avis des personnes concernées ou de leurs représentants [1]. Cette obligation s'applique à la publication de photos sur les réseaux sociaux, y compris Facebook [1].

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
Oui : vous devez demander la permission des personnes concernées, notamment des enfants, car le traitement de leurs données à caractère personnel (comme les photos) est soumis à des obligations de consentement (RGPD, article 8, paragraphe 1). Si l'enfant est âgé de moins de 16 ans, ce traitement n'est licite que si le consentement est donné ou autorisé par le titulaire de la responsabilité parentale à l'égard de l'enfant [3]. Le responsable du traitement doit, le cas échéant, demander l'avis des personnes concernées ou de leurs représentants [1]. Cette obligation s'applique à la publication de photos sur les réseaux sociaux, y compris Facebook [1].
```

</details>

Temps : recherche 2.2 s · génération 23.2 s (2523 tokens lus, 359 écrits, 35.5 tokens/s) · contrôle de pertinence 4.5 s

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

Temps : recherche 2.1 s · génération 12.8 s (2447 tokens lus, 26 écrits, 37.9 tokens/s)
