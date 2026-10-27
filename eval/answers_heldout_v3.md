# Réponses du copilote — heldout_v3

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 25/10/2026 à 19:09 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen3:4b-instruct` via Ollama 0.40.11 — température 0.1, contexte 8192 tokens, couches sur la carte graphique : toutes, 1500 tokens au plus par réponse
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_v1.jsonl` (17 + 3 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q11 | Un client me demande d'effacer toutes ses données : suis-je obligé de le faire ? | 3/3 | non | La réponse change le sens d'une condition ou d'une exception (négation ajoutée ou retirée par rapport à l'extrait) : « lorsque l'un des motifs suivants s'applique : les données ne sont plus nécessaires ». Vérifiez ce point. | 73 s |
| q12 | Un salarié demande une copie de toutes les données que nous avons sur lui : que dois-je lui donner ? | 2/2 | non | — | 41 s |
| q13 | Un adhérent veut récupérer ses données pour les donner à une autre association : est-ce un droit ? | 1/1 | non | — | 29 s |
| q14 | Puis-je envoyer une lettre d'information par e-mail à mes adhérents, et peuvent-ils refuser ? | 6/6 | non | Réponse coupée : le modèle a atteint la limite de 1500 tokens (LLM_MAX_TOKENS), la fin de la réponse manque. Posez une question plus précise ou augmentez LLM_MAX_TOKENS dans .env. | 66 s |
| q15 | Mon prestataire informatique a accès à nos fichiers : faut-il signer un contrat particulier ? | 3/3 | non | La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui: si votre prestataire informatique a accès à vos fichiers et qu’il fournit un système d’IA à haut risque ou un … » (et 6 autre(s)). Vérifiez qui est concerné. | 46 s |
| q16 | Puis-je stocker les fichiers de mon association chez un hébergeur situé aux États-Unis ? | 3/3 | non | La réponse s'appuie sur le RGPD et l'AI Act sans dire de quel règlement vient chaque obligation : « Ces garanties doivent permettre aux personnes concernées de disposer de droits opposables et de voies de droit … » (et 2 autre(s)). | 44 s |
| q17 | Quelles sanctions risque une petite entreprise qui ne respecte pas le RGPD ? | 2/3 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([5]) : ignoré(s).; La réponse cite [5] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations. | 41 s |
| q18 | Notre association peut-elle collecter des informations sur la santé de ses bénévoles ? | 1/1 | non | — | 31 s |
| q19 | Qu'est-ce qu'une donnée personnelle ? | 2/2 | non | La réponse s'appuie sur le RGPD et l'AI Act sans dire de quel règlement vient chaque obligation : « Une donnée personnelle est toute information se rapportant à une personne physique identifiée ou identifiable. » (et 1 autre(s)). | 20 s |
| q20 | À partir de quel âge un enfant peut-il s'inscrire seul à notre service en ligne ? | 1/1 | non | — | 37 s |
| q21 | Comment dois-je protéger les données personnelles que nous conservons ? | 3/5 | non | 2 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1], [1]) : ignoré(s). | 38 s |
| q22 | Le consentement d'une personne doit-il être donné par écrit ? | 3/3 | non | La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Non, le consentement n’est pas obligatoirement donné par écrit, car le RGPD (article 4, point 11) définit le … ». Vérifiez ce point.; La réponse met entre « » un texte introuvable dans les extraits vérifiés : « toute manifestation de volonté, libre, spécifique, éclairée et univoque par laquelle la personne concernée accepte, par … ».; La réponse formule une exception qui ne reprend pas les extraits vérifiés : « sauf dans les cas où une déclaration écrite est exigée, comme dans le cas ». Vérifiez-la dans les textes.; La réponse s'appuie sur le RGPD et l'AI Act sans dire de quel règlement vient chaque obligation : « Cela inclut des formes orales ou autres actes positifs clairs, sauf dans les cas où une déclaration écrite est exigée, … » (et 3 autre(s)). | 29 s |
| q23 | Quelles utilisations de l'intelligence artificielle sont interdites en Europe ? | 8/8 | non | Réponse coupée : le modèle a atteint la limite de 1500 tokens (LLM_MAX_TOKENS), la fin de la réponse manque. Posez une question plus précise ou augmentez LLM_MAX_TOKENS dans .env.; La réponse formule une exception qui ne reprend pas les extraits vérifiés : « sauf dans les cas précisément autorisés : la recherche de victimes d’enlèvement, de traite ». Vérifiez-la dans les textes. | 77 s |
| q24 | Ai-je le droit d'utiliser une IA qui analyse les émotions de mes salariés ? | 2/2 | non | La réponse cite [5] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations. | 49 s |
| q25 | Mon logiciel est-il un « système d'IA » au sens de la loi européenne ? | 1/1 | non | — | 24 s |
| q26 | Dois-je indiquer qu'une image publiée sur notre site a été créée par une IA ? | 1/2 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([2]) : ignoré(s).; La réponse cite [2] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations. | 36 s |
| q27 | Quelles amendes prévoit le règlement européen sur l'intelligence artificielle ? | 5/5 | non | — | 57 s |
| h03 | Comment déclarer la création d'une association en préfecture ? | 0/0 | oui | — | 31 s |
| h04 | Quel est le montant du SMIC cette année ? | 0/0 | oui | — | 22 s |
| h05 | Comment rédiger les statuts d'une association ? | 5/5 | non | — | 42 s |

## q11 — Un client me demande d'effacer toutes ses données : suis-je obligé de le faire ?

Article attendu : RGPD art. 17 — passage [1].

### Réponse du copilote

> Oui : vous êtes obligé d'effacer les données à caractère personnel du client dans les meilleurs délais, lorsque l'un des motifs suivants s'applique : les données ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées, le client a retiré son consentement sans autre fondement juridique, il s'oppose au traitement sans motif légitime impérieux, les données ont fait l'objet d'un traitement illicite, ou elles doivent être effacées pour respecter une obligation légale [1]. Cependant, cette obligation ne s'applique pas si le traitement est nécessaire à l'exercice du droit à la liberté d'expression et d'information, pour respecter une obligation légale, pour une mission d'intérêt public, à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques, ou pour la constatation, l'exercice ou la défense de droits en justice [1]. Si l'un de ces cas s'applique, l'effacement n'est pas obligatoire. En outre, si les données ont été rendues publiques, vous devez prendre des mesures raisonnables pour informer les autres responsables du traitement de l'effacement demandé [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit d'obtenir du responsable du traitement l'effacement, dans les meilleurs délais, de données à caractère personnel la concernant et le responsable du traitement a l'obligation d'effacer ces données à caractère personnel dans les meilleurs délais, lorsque l'un des motifs suivants s'applique: »
  [1] « Lorsqu'il a rendu publiques les données à caractère personnel et qu'il est tenu de les effacer en vertu du paragraphe 1, le responsable du traitement, compte tenu des technologies disponibles et des coûts de mise en œuvre, prend des mesures raisonnables, y compris d'ordre technique, pour informer les responsables du traitement qui traitent ces données à caractère personnel que la personne concernée a demandé l'effacement par ces responsables du traitement de tout lien vers ces données à caractère personnel, ou de toute copie ou reproduction de celles-ci. »
  [1] « Les paragraphes 1 et 2 ne s'appliquent pas dans la mesure où ce traitement est nécessaire: … à l'exercice du droit à la liberté d'expression et d'information; … pour respecter une obligation légale qui requiert le traitement prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis, ou pour exécuter une mission d'intérêt public ou relevant de l'exercice de l'autorité publique dont est investi le responsable du traitement; … à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, dans la mesure où le droit visé au paragraphe 1 est susceptible de rendre impossible ou de compromettre gravement la réalisation des objectifs dudit traitement; ou … à la constatation, à l'exercice ou à la défense de droits en justice. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 17 : Droit à l'effacement («droit à l'oubli») (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_17
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 19 : Obligation de notification en ce qui concerne la rectification ou l'effacement de données à caractère personnel ou la limitation du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_19
  [3] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
  [4] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [5] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
Attention : La réponse change le sens d'une condition ou d'une exception (négation ajoutée ou retirée par rapport à l'extrait) : « lorsque l'un des motifs suivants s'applique : les données ne sont plus nécessaires ». Vérifiez ce point.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « La personne concernée a le droit d'obtenir du responsable du traitement l'effacement, dans les meilleurs délais, de données à caractère personnel la concernant et le responsable du traitement a l'obligation d'effacer ces données à caractère personnel dans les meilleurs délais, lorsque l'un des motifs suivants s'applique: »  
- [1] « Lorsqu'il a rendu publiques les données à caractère personnel et qu'il est tenu de les effacer en vertu du paragraphe 1, le responsable du traitement, compte tenu des technologies disponibles et des coûts de mise en œuvre, prend des mesures raisonnables, y compris d'ordre technique, pour informer les responsables du traitement qui traitent ces données à caractère personnel que la personne concernée a demandé l'effacement par ces responsables du traitement de tout lien vers ces données à caractère personnel, ou de toute copie ou reproduction de celles-ci. »  
- [1] « Les paragraphes 1 et 2 ne s'appliquent pas dans la mesure où ce traitement est nécessaire: … à l'exercice du droit à la liberté d'expression et d'information; … pour respecter une obligation légale qui requiert le traitement prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis, ou pour exécuter une mission d'intérêt public ou relevant de l'exercice de l'autorité publique dont est investi le responsable du traitement; … à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, dans la mesure où le droit visé au paragraphe 1 est susceptible de rendre impossible ou de compromettre gravement la réalisation des objectifs dudit traitement; ou … à la constatation, à l'exercice ou à la défense de droits en justice. »  

RÉPONSE :  
Oui : vous êtes obligé d'effacer les données à caractère personnel du client dans les meilleurs délais, lorsque l'un des motifs suivants s'applique : les données ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées, le client a retiré son consentement sans autre fondement juridique, il s'oppose au traitement sans motif légitime impérieux, les données ont fait l'objet d'un traitement illicite, ou elles doivent être effacées pour respecter une obligation légale [1]. Cependant, cette obligation ne s'applique pas si le traitement est nécessaire à l'exercice du droit à la liberté d'expression et d'information, pour respecter une obligation légale, pour une mission d'intérêt public, à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques, ou pour la constatation, l'exercice ou la défense de droits en justice [1]. Si l'un de ces cas s'applique, l'effacement n'est pas obligatoire. En outre, si les données ont été rendues publiques, vous devez prendre des mesures raisonnables pour informer les autres responsables du traitement de l'effacement demandé [1].
```

</details>

Temps : recherche 5.7 s · génération 67.4 s (4069 tokens lus, 754 écrits, 32.2 tokens/s)

## q12 — Un salarié demande une copie de toutes les données que nous avons sur lui : que dois-je lui donner ?

Article attendu : RGPD art. 15 — passage [2].

### Réponse du copilote

> Vous devez lui fournir une copie des données à caractère personnel qui vous concernent, conformément à l’article 15, paragraphe 3 du RGPD [2]. Cette copie peut être fournie sous une forme électronique d’usage courant, à moins qu’il ne demande autrement [2]. En outre, vous devez lui indiquer la source des données à caractère personnel, ainsi que si elles proviennent de sources accessibles au public [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « Le responsable du traitement fournit une copie des données à caractère personnel faisant l'objet d'un traitement. Le responsable du traitement peut exiger le paiement de frais raisonnables basés sur les coûts administratifs pour toute copie supplémentaire demandée par la personne concernée. Lorsque la personne concernée présente sa demande par voie électronique, les informations sont fournies sous une forme électronique d'usage courant, à moins que la personne concernée ne demande qu'il en soit autrement. »
  [4] « la source d'où proviennent les données à caractère personnel et, le cas échéant, une mention indiquant qu'elles sont issues ou non de sources accessibles au public; »

Sources citées :
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [4] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [3] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [5] AI Act — règlement (UE) 2024/1689, article 91 : Pouvoir de demander de la documentation et des informations
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_91

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [2] « Le responsable du traitement fournit une copie des données à caractère personnel faisant l'objet d'un traitement. Le responsable du traitement peut exiger le paiement de frais raisonnables basés sur les coûts administratifs pour toute copie supplémentaire demandée par la personne concernée. Lorsque la personne concernée présente sa demande par voie électronique, les informations sont fournies sous une forme électronique d'usage courant, à moins que la personne concernée ne demande qu'il en soit autrement. »  
- [4] « la source d'où proviennent les données à caractère personnel et, le cas échéant, une mention indiquant qu'elles sont issues ou non de sources accessibles au public; »  

RÉPONSE :  
Vous devez lui fournir une copie des données à caractère personnel qui vous concernent, conformément à l’article 15, paragraphe 3 du RGPD [2]. Cette copie peut être fournie sous une forme électronique d’usage courant, à moins qu’il ne demande autrement [2]. En outre, vous devez lui indiquer la source des données à caractère personnel, ainsi que si elles proviennent de sources accessibles au public [4].
```

</details>

Temps : recherche 4.0 s · génération 36.8 s (4001 tokens lus, 282 écrits, 32.7 tokens/s)

## q13 — Un adhérent veut récupérer ses données pour les donner à une autre association : est-ce un droit ?

Article attendu : RGPD art. 20 — passage [1].

### Réponse du copilote

> Oui, c’est un droit : l’adhérent a le droit de recevoir ses données à caractère personnel fournies à un responsable du traitement, dans un format structuré, couramment utilisé et lisible par machine, et de les transmettre à un autre responsable du traitement sans que le responsable du traitement auquel les données ont été communiquées y fasse obstacle, lorsque le traitement est fondé sur le consentement ou un contrat et que le traitement est effectué à l’aide de procédés automatisés [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les personnes concernées ont le droit de recevoir les données à caractère personnel les concernant qu'elles ont fournies à un responsable du traitement, dans un format structuré, couramment utilisé et lisible par machine, et ont le droit de transmettre ces données à un autre responsable du traitement sans que le responsable du traitement auquel les données à caractère personnel ont été communiquées y fasse obstacle, lorsque: a) le traitement est fondé sur le consentement en application de l'article 6, paragraphe 1, point a), ou de l'article 9, paragraphe 2, point a), ou sur un contrat en application de l'article 6, paragraphe 1, point b); et b) le traitement est effectué à l'aide de procédés automatisés. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 20 : Droit à la portabilité des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_20
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [3] RGPD — règlement (UE) 2016/679, article 16 : Droit de rectification
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_16
  [4] RGPD — règlement (UE) 2016/679, article 6, paragraphe 4 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
  [5] RGPD — règlement (UE) 2016/679, article 80 : Représentation des personnes concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_80

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les personnes concernées ont le droit de recevoir les données à caractère personnel les concernant qu'elles ont fournies à un responsable du traitement, dans un format structuré, couramment utilisé et lisible par machine, et ont le droit de transmettre ces données à un autre responsable du traitement sans que le responsable du traitement auquel les données à caractère personnel ont été communiquées y fasse obstacle, lorsque: a) le traitement est fondé sur le consentement en application de l'article 6, paragraphe 1, point a), ou de l'article 9, paragraphe 2, point a), ou sur un contrat en application de l'article 6, paragraphe 1, point b); et b) le traitement est effectué à l'aide de procédés automatisés. »

RÉPONSE :  
Oui, c’est un droit : l’adhérent a le droit de recevoir ses données à caractère personnel fournies à un responsable du traitement, dans un format structuré, couramment utilisé et lisible par machine, et de les transmettre à un autre responsable du traitement sans que le responsable du traitement auquel les données ont été communiquées y fasse obstacle, lorsque le traitement est fondé sur le consentement ou un contrat et que le traitement est effectué à l’aide de procédés automatisés [1].
```

</details>

Temps : recherche 2.2 s · génération 26.5 s (2903 tokens lus, 307 écrits, 35.1 tokens/s)

## q14 — Puis-je envoyer une lettre d'information par e-mail à mes adhérents, et peuvent-ils refuser ?

Article attendu : RGPD art. 21 ou RGPD art. 6 — absent des passages donnés au modèle.

### Réponse du copilote

> Oui, vous pouvez envoyer une lettre d'information par e-mail à vos adhérents, car le RGPD permet le traitement des données à caractère personnel pour des finalités de communication, notamment dans le cadre d'informations destinées à des groupes d'adhérents, à condition que les informations soient fournies de manière claire, transparente et compréhensible [4]. Cependant, les adhérents ont le droit de refuser ce traitement, notamment en exercant leur droit de s'opposer à ce traitement, comme prévus à l'article 15, point e) [3]. Cette possibilité de refus est fondée sur le droit de la personne concernée de s'opposer à ce traitement [3]. Le fait que la communication soit par e-mail ne remet pas en cause ce droit, même si les données sont transmises par voie électronique [2]. Les conditions de l'envoi doivent respecter les exigences de transparence et d'accessibilité, notamment en termes de langage clair et simple [4]. Aucun texte ne prévoit une obligation de refus par les adhérents, mais ils peuvent le faire en exercant leur droit de s'opposer [

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Lorsqu'une violation de données à caractère personnel est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement communique la violation de données à caractère personnel à la personne concernée dans les meilleurs délais. »
  [1] « La communication à la personne concernée visée au paragraphe 1 n'est pas nécessaire si l'une ou l'autre des conditions suivantes est remplie: a) le responsable du traitement a mis en œuvre les mesures de protection techniques et organisationnelles appropriées et ces mesures ont été appliquées aux données à caractère personnel affectées par ladite violation, en particulier les mesures qui rendent les données à caractère personnel incompréhensibles pour toute personne qui n'est pas autorisée à y avoir accès, telles que le chiffrement; b) le responsable du traitement a pris des mesures ultérieures qui garantissent que le risque élevé pour les droits et libertés des personnes concernées visé au paragraphe 1 n'est plus susceptible de se matérialiser; c) elle exigerait des efforts disproportionnés. Dans ce cas, il est plutôt procédé à une communication publique ou à une mesure similaire permettant aux personnes concernées d'être informées de manière tout aussi efficace. »
  [2] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. Lorsque la personne concernée présente sa demande sous une forme électronique, les informations sont fournies par voie électronique lorsque cela est possible, à moins que la personne concernée ne demande qu'il en soit autrement. »
  [3] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: a) les finalités du traitement; b) les catégories de données à caractère personnel concernées; c) les destinataires ou catégories de destinataires auxquels les données à caractère personnel ont été ou seront communiquées, en particulier les destinataires qui sont établis dans des pays tiers ou les organisations internationales; d) lorsque cela est possible, la durée de conservation des données à caractère personnel envisagée ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; e) l'existence du droit de demander au responsable du traitement la rectification ou l'effacement de données à caractère personnel, ou une limitation du traitement des données à caractère personnel relatives à la personne concernée, ou du droit de s'opposer à ce traitement; f) le droit d'introduire une réclamation auprès d'une autorité de contrôle; g) lorsque les données à caractère personnel ne sont pas collectées auprès de la personne concernée, toute information disponible quant à leur source; h) l'existence d'une prise de décision automatisée, y compris un profilage, visée à l'article 22, paragraphes 1 et 4, et, au moins en pareils cas, des informations utiles concernant la logique sous-jacente, ainsi que l'importance et les conséquences prévues de ce traitement pour la personne concernée. »
  [4] « Le responsable du traitement prend des mesures appropriées pour fournir toute information visée aux articles 13 et 14 ainsi que pour procéder à toute communication au titre des articles 15 à 22 et de l'article 34 en ce qui concerne le traitement à la personne concernée d'une façon concise, transparente, compréhensible et aisément accessible, en des termes clairs et simples, en particulier pour toute information destinée spécifiquement à un enfant. Les informations sont fournies par écrit ou par d'autres moyens y compris, lorsque c'est approprié, par voie électronique. Lorsque la personne concernée en fait la demande, les informations peuvent être fournies oralement, à condition que l'identité de la personne concernée soit démontrée par d'autres moyens. »
  [5] « Dans le cadre du traitement réalisé à des fins journalistiques ou à des fins d'expression universitaire, artistique ou littéraire, les États membres prévoient des exemptions ou des dérogations au chapitre II (principes), au chapitre III (droits de la personne concernée), au chapitre IV (responsable du traitement et sous-traitant), au chapitre V (transfert de données à caractère personnel vers des pays tiers ou à des organisations internationales), au chapitre VI (autorités de contrôle indépendantes), au chapitre VII (coopération et cohérence) et au chapitre IX (situations particulières de traitement) si celles-ci sont nécessaires pour concilier le droit à la protection des données à caractère personnel et la liberté d'expression et d'information. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 34 : Communication à la personne concernée d'une violation de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_34
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [3] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [4] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [5] RGPD — règlement (UE) 2016/679, article 85 : Traitement et liberté d'expression et d'information (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_85
Attention : Réponse coupée : le modèle a atteint la limite de 1500 tokens (LLM_MAX_TOKENS), la fin de la réponse manque. Posez une question plus précise ou augmentez LLM_MAX_TOKENS dans .env.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Lorsqu'une violation de données à caractère personnel est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement communique la violation de données à caractère personnel à la personne concernée dans les meilleurs délais. »  
- [1] « La communication à la personne concernée visée au paragraphe 1 n'est pas nécessaire si l'une ou l'autre des conditions suivantes est remplie: a) le responsable du traitement a mis en œuvre les mesures de protection techniques et organisationnelles appropriées et ces mesures ont été appliquées aux données à caractère personnel affectées par ladite violation, en particulier les mesures qui rendent les données à caractère personnel incompréhensibles pour toute personne qui n'est pas autorisée à y avoir accès, telles que le chiffrement; b) le responsable du traitement a pris des mesures ultérieures qui garantissent que le risque élevé pour les droits et libertés des personnes concernées visé au paragraphe 1 n'est plus susceptible de se matérialiser; c) elle exigerait des efforts disproportionnés. Dans ce cas, il est plutôt procédé à une communication publique ou à une mesure similaire permettant aux personnes concernées d'être informées de manière tout aussi efficace. »  
- [2] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. Lorsque la personne concernée présente sa demande sous une forme électronique, les informations sont fournies par voie électronique lorsque cela est possible, à moins que la personne concernée ne demande qu'il en soit autrement. »  
- [3] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: a) les finalités du traitement; b) les catégories de données à caractère personnel concernées; c) les destinataires ou catégories de destinataires auxquels les données à caractère personnel ont été ou seront communiquées, en particulier les destinataires qui sont établis dans des pays tiers ou les organisations internationales; d) lorsque cela est possible, la durée de conservation des données à caractère personnel envisagée ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; e) l'existence du droit de demander au responsable du traitement la rectification ou l'effacement de données à caractère personnel, ou une limitation du traitement des données à caractère personnel relatives à la personne concernée, ou du droit de s'opposer à ce traitement; f) le droit d'introduire une réclamation auprès d'une autorité de contrôle; g) lorsque les données à caractère personnel ne sont pas collectées auprès de la personne concernée, toute information disponible quant à leur source; h) l'existence d'une prise de décision automatisée, y compris un profilage, visée à l'article 22, paragraphes 1 et 4, et, au moins en pareils cas, des informations utiles concernant la logique sous-jacente, ainsi que l'importance et les conséquences prévues de ce traitement pour la personne concernée. »  
- [4] « Le responsable du traitement prend des mesures appropriées pour fournir toute information visée aux articles 13 et 14 ainsi que pour procéder à toute communication au titre des articles 15 à 22 et de l'article 34 en ce qui concerne le traitement à la personne concernée d'une façon concise, transparente, compréhensible et aisément accessible, en des termes clairs et simples, en particulier pour toute information destinée spécifiquement à un enfant. Les informations sont fournies par écrit ou par d'autres moyens y compris, lorsque c'est approprié, par voie électronique. Lorsque la personne concernée en fait la demande, les informations peuvent être fournies oralement, à condition que l'identité de la personne concernée soit démontrée par d'autres moyens. »  
- [5] « Dans le cadre du traitement réalisé à des fins journalistiques ou à des fins d'expression universitaire, artistique ou littéraire, les États membres prévoient des exemptions ou des dérogations au chapitre II (principes), au chapitre III (droits de la personne concernée), au chapitre IV (responsable du traitement et sous-traitant), au chapitre V (transfert de données à caractère personnel vers des pays tiers ou à des organisations internationales), au chapitre VI (autorités de contrôle indépendantes), au chapitre VII (coopération et cohérence) et au chapitre IX (situations particulières de traitement) si celles-ci sont nécessaires pour concilier le droit à la protection des données à caractère personnel et la liberté d'expression et d'information. »

RÉPONSE :  
Oui, vous pouvez envoyer une lettre d'information par e-mail à vos adhérents, car le RGPD permet le traitement des données à caractère personnel pour des finalités de communication, notamment dans le cadre d'informations destinées à des groupes d'adhérents, à condition que les informations soient fournies de manière claire, transparente et compréhensible [4]. Cependant, les adhérents ont le droit de refuser ce traitement, notamment en exercant leur droit de s'opposer à ce traitement, comme prévus à l'article 15, point e) [3]. Cette possibilité de refus est fondée sur le droit de la personne concernée de s'opposer à ce traitement [3]. Le fait que la communication soit par e-mail ne remet pas en cause ce droit, même si les données sont transmises par voie électronique [2]. Les conditions de l'envoi doivent respecter les exigences de transparence et d'accessibilité, notamment en termes de langage clair et simple [4]. Aucun texte ne prévoit une obligation de refus par les adhérents, mais ils peuvent le faire en exercant leur droit de s'opposer [
```

</details>

Temps : recherche 2.2 s · génération 64.0 s (3006 tokens lus, 1500 écrits, 33.1 tokens/s)

## q15 — Mon prestataire informatique a accès à nos fichiers : faut-il signer un contrat particulier ?

Article attendu : RGPD art. 28 — absent des passages donnés au modèle.

### Réponse du copilote

> Oui : si votre prestataire informatique a accès à vos fichiers et qu’il fournit un système d’IA à haut risque ou un outil, service ou composant intégré dans un tel système, il est obligé de préciser, par accord écrit, les informations, les capacités, l’accès technique et toute autre assistance nécessaires [2]. Cette obligation s’applique notamment pour permettre à votre organisation de se conformer aux obligations du règlement [2]. Cette exigence de contrat écrit s’inscrit dans le cadre des responsabilités de la chaîne de valeur de l’IA [2]. Les passages trouvés ne mentionnent pas de règle spécifique pour les prestataires informatiques en général, sauf dans le cas d’un système d’IA à haut risque [2]. Ainsi, la nécessité d’un contrat particulier dépend du type d’outil ou de service fourni. Si le prestataire utilise un modèle d’IA à usage général, il doit fournir une documentation technique et un résumé du contenu d’entraînement [1]. Dans ce cas, un contrat particulier peut être nécessaire pour définir les obligations de confidentialité et d’information [1]. Les obligations de confidentialité s’appliquent à toute information ou documentation obtenue en vertu du présent article [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les fournisseurs de modèles d’IA à usage général: … élaborent et tiennent à jour la documentation technique du modèle, y compris son processus d’entraînement et d’essai et les résultats de son évaluation, qui contient, au minimum, les informations énoncées à l’annexe XI aux fins de la fournir, sur demande, au Bureau de l’IA et aux autorités nationales compétentes; »
  [2] « Le fournisseur d'un système d'IA à haut risque et le tiers qui fournit un système d'IA, un modèle d'IA, des outils, services, composants ou processus qui sont utilisés ou intégrés dans un système d'IA à haut risque précisent, par accord écrit, les informations, les capacités, l'accès technique et toute autre assistance nécessaires, sur la base de l'état de la technique généralement reconnu, pour permettre au fournisseur du système d'IA à haut risque de se conformer pleinement aux obligations prévues dans le présent règlement. »
  [4] « À la demande motivée d’une autorité compétente, les fournisseurs de systèmes d’IA à haut risque fournissent à ladite autorité toutes les informations et tous les documents nécessaires pour démontrer la conformité du système d’IA à haut risque avec les exigences énoncées à la section 2, dans une langue aisément compréhensible par l’autorité dans l’une des langues officielles des institutions de l’Union, telle qu’indiquée par l’État membre concerné. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 53 : Obligations incombant aux fournisseurs de modèles d’IA à usage général (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_53
  [2] AI Act — règlement (UE) 2024/1689, article 25, paragraphe 4 : Responsabilités tout au long de la chaîne de valeur de l’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_25
  [4] AI Act — règlement (UE) 2024/1689, article 21 : Coopération avec les autorités compétentes (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_21
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 8 : Conditions applicables au consentement des enfants en ce qui concerne les services de la société de l'information
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_8
  [5] AI Act — règlement (UE) 2024/1689, article 18 : Conservation des documents
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_18
Attention : La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui: si votre prestataire informatique a accès à vos fichiers et qu’il fournit un système d’IA à haut risque ou un … » (et 6 autre(s)). Vérifiez qui est concerné.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les fournisseurs de modèles d’IA à usage général: … élaborent et tiennent à jour la documentation technique du modèle, y compris son processus d’entraînement et d’essai et les résultats de son évaluation, qui contient, au minimum, les informations énoncées à l’annexe XI aux fins de la fournir, sur demande, au Bureau de l’IA et aux autorités nationales compétentes; »  
- [2] « Le fournisseur d'un système d'IA à haut risque et le tiers qui fournit un système d'IA, un modèle d'IA, des outils, services, composants ou processus qui sont utilisés ou intégrés dans un système d'IA à haut risque précisent, par accord écrit, les informations, les capacités, l'accès technique et toute autre assistance nécessaires, sur la base de l'état de la technique généralement reconnu, pour permettre au fournisseur du système d'IA à haut risque de se conformer pleinement aux obligations prévues dans le présent règlement. »  
- [4] « À la demande motivée d’une autorité compétente, les fournisseurs de systèmes d’IA à haut risque fournissent à ladite autorité toutes les informations et tous les documents nécessaires pour démontrer la conformité du système d’IA à haut risque avec les exigences énoncées à la section 2, dans une langue aisément compréhensible par l’autorité dans l’une des langues officielles des institutions de l’Union, telle qu’indiquée par l’État membre concerné. »  

RÉPONSE :  
Oui : si votre prestataire informatique a accès à vos fichiers et qu’il fournit un système d’IA à haut risque ou un outil, service ou composant intégré dans un tel système, il est obligé de préciser, par accord écrit, les informations, les capacités, l’accès technique et toute autre assistance nécessaires [2]. Cette obligation s’applique notamment pour permettre à votre organisation de se conformer aux obligations du règlement [2]. Cette exigence de contrat écrit s’inscrit dans le cadre des responsabilités de la chaîne de valeur de l’IA [2]. Les passages trouvés ne mentionnent pas de règle spécifique pour les prestataires informatiques en général, sauf dans le cas d’un système d’IA à haut risque [2]. Ainsi, la nécessité d’un contrat particulier dépend du type d’outil ou de service fourni. Si le prestataire utilise un modèle d’IA à usage général, il doit fournir une documentation technique et un résumé du contenu d’entraînement [1]. Dans ce cas, un contrat particulier peut être nécessaire pour définir les obligations de confidentialité et d’information [1]. Les obligations de confidentialité s’appliquent à toute information ou documentation obtenue en vertu du présent article [1].
```

</details>

Temps : recherche 2.2 s · génération 44.3 s (3512 tokens lus, 672 écrits, 32.8 tokens/s)

## q16 — Puis-je stocker les fichiers de mon association chez un hébergeur situé aux États-Unis ?

Article attendu : RGPD art. 44 ou RGPD art. 45 ou RGPD art. 46 — passage [5].

### Réponse du copilote

> Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, à condition que vous prévoyiez des garanties appropriées pour la protection des données à caractère personnel, telles que définies dans le RGPD, article 46, paragraphe 1 [5]. Ces garanties doivent permettre aux personnes concernées de disposer de droits opposables et de voies de droit effectives [5]. Si votre association compte moins de 250 employés, les obligations du registre des activités de traitement ne s'appliquent pas, sauf si le traitement comporte un risque pour les droits et libertés des personnes concernées, notamment sur des données particulières ou relatives à des condamnations pénales [2]. Cependant, les textes trouvés ne précisent pas les conditions spécifiques pour le stockage de fichiers dans un pays tiers comme les États-Unis, ni les modalités d'application des garanties appropriées dans ce contexte. Les règles concrètes (durée, type de garantie, validation) peuvent venir d'autres textes, comme les recommandations de la CNIL ou des décisions d'autorités nationales [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « Les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10. »
  [4] « Pendant une période prenant fin 10 ans après la mise sur le marché ou la mise en service du système d’IA à haut risque, le fournisseur tient à la disposition des autorités nationales compétentes: … »
  [5] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »

Sources citées :
  [2] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30
  [4] AI Act — règlement (UE) 2024/1689, article 18 : Conservation des documents (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_18
  [5] RGPD — règlement (UE) 2016/679, article 46 : Transferts moyennant des garanties appropriées (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_46
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 4, définition 16 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [3] RGPD — règlement (UE) 2016/679, article 91 : Règles existantes des églises et associations religieuses en matière de protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_91
Attention : La réponse s'appuie sur le RGPD et l'AI Act sans dire de quel règlement vient chaque obligation : « Ces garanties doivent permettre aux personnes concernées de disposer de droits opposables et de voies de droit … » (et 2 autre(s)).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [2] « Les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10. »  
- [4] « Pendant une période prenant fin 10 ans après la mise sur le marché ou la mise en service du système d’IA à haut risque, le fournisseur tient à la disposition des autorités nationales compétentes: … »  
- [5] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »  

RÉPONSE :  
Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, à condition que vous prévoyiez des garanties appropriées pour la protection des données à caractère personnel, telles que définies dans le RGPD, article 46, paragraphe 1 [5]. Ces garanties doivent permettre aux personnes concernées de disposer de droits opposables et de voies de droit effectives [5]. Si votre association compte moins de 250 employés, les obligations du registre des activités de traitement ne s'appliquent pas, sauf si le traitement comporte un risque pour les droits et libertés des personnes concernées, notamment sur des données particulières ou relatives à des condamnations pénales [2]. Cependant, les textes trouvés ne précisent pas les conditions spécifiques pour le stockage de fichiers dans un pays tiers comme les États-Unis, ni les modalités d'application des garanties appropriées dans ce contexte. Les règles concrètes (durée, type de garantie, validation) peuvent venir d'autres textes, comme les recommandations de la CNIL ou des décisions d'autorités nationales [2].
```

</details>

Temps : recherche 2.2 s · génération 42.1 s (3596 tokens lus, 576 écrits, 32.6 tokens/s)

## q17 — Quelles sanctions risque une petite entreprise qui ne respecte pas le RGPD ?

Article attendu : RGPD art. 83 — passage [1].

### Réponse du copilote

> Une petite entreprise qui ne respecte pas le RGPD peut être sanctionnée par des amendes administratives, selon les dispositions violées. Si la violation concerne des obligations comme celles des articles 8, 11, 25 à 39, 42 et 43, l'amende peut s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [1]. Si la violation concerne d'autres dispositions, comme les principes de base du traitement ou les droits des personnes concernées, l'amende peut atteindre jusqu'à 20 000 000 EUR ou jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [2]. En outre, l'autorité de contrôle peut ordonner une limitation temporaire ou définitive du traitement, la rectification ou l'effacement de données, ou la suspension des flux de données [5]. Ces mesures sont applicables même si l'entreprise est petite, car le RGPD s'applique à toutes les entreprises, y compris les petites entreprises, sans exception [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »
  [2] « les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 83, paragraphe 4 : Conditions générales pour imposer des amendes administratives (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83
  [2] RGPD — règlement (UE) 2016/679, article 83, paragraphe 5 : Conditions générales pour imposer des amendes administratives (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83
  [5] RGPD — règlement (UE) 2016/679, article 58, paragraphe 2 : Pouvoirs (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_58
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 24 : Responsabilité du responsable du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_24
  [4] RGPD — règlement (UE) 2016/679, article 42 : Certification
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_42
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([5]) : ignoré(s).
Attention : La réponse cite [5] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »  
- [2] « les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »  
- [5] « chaque autorité de contrôle dispose du pouvoir d'adopter toutes les mesures correctrices suivantes: … f) ordonner une limitation temporaire ou définitive, y compris une interdiction, du traitement; … g) ordonner la rectification ou l'effacement de données à caractère personnel ou la limitation du traitement en application des articles 16, 17 et 18 … »  

RÉPONSE :  
Une petite entreprise qui ne respecte pas le RGPD peut être sanctionnée par des amendes administratives, selon les dispositions violées. Si la violation concerne des obligations comme celles des articles 8, 11, 25 à 39, 42 et 43, l'amende peut s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [1]. Si la violation concerne d'autres dispositions, comme les principes de base du traitement ou les droits des personnes concernées, l'amende peut atteindre jusqu'à 20 000 000 EUR ou jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [2]. En outre, l'autorité de contrôle peut ordonner une limitation temporaire ou définitive du traitement, la rectification ou l'effacement de données, ou la suspension des flux de données [5]. Ces mesures sont applicables même si l'entreprise est petite, car le RGPD s'applique à toutes les entreprises, y compris les petites entreprises, sans exception [1].
```

</details>

Temps : recherche 2.2 s · génération 39.0 s (3267 tokens lus, 596 écrits, 33.3 tokens/s)

## q18 — Notre association peut-elle collecter des informations sur la santé de ses bénévoles ?

Article attendu : RGPD art. 9 — passage [1].

### Réponse du copilote

> Oui, notre association peut collecter des informations sur la santé de ses bénévoles, à condition que ce traitement soit effectué par un professionnel de la santé soumis à une obligation de secret professionnel conformément au droit de l'Union, au droit d'un État membre ou aux règles arrêtées par les organismes nationaux compétents, ou sous sa responsabilité [1]. Sinon, ce traitement relève d'une catégorie particulière de données à caractère personnel et n'est pas autorisé sans une base juridique appropriée, comme le consentement éclairé ou une obligation légale, ce qui n'est pas explicitement mentionné dans les extraits.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les données à caractère personnel visées au paragraphe 1 peuvent faire l'objet d'un traitement aux fins prévues au paragraphe 2, point h), si ces données sont traitées par un professionnel de la santé soumis à une obligation de secret professionnel conformément au droit de l'Union, au droit d'un État membre ou aux règles arrêtées par les organismes nationaux compétents, ou sous sa responsabilité, ou par une autre personne également soumise à une obligation de secret conformément au droit de l'Union ou au droit d'un État membre ou aux règles arrêtées par les organismes nationaux compétents. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 9, paragraphe 3 : Traitement portant sur des catégories particulières de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [3] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [4] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [5] RGPD — règlement (UE) 2016/679, article 26 : Responsables conjoints du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_26

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les données à caractère personnel visées au paragraphe 1 peuvent faire l'objet d'un traitement aux fins prévues au paragraphe 2, point h), si ces données sont traitées par un professionnel de la santé soumis à une obligation de secret professionnel conformément au droit de l'Union, au droit d'un État membre ou aux règles arrêtées par les organismes nationaux compétents, ou sous sa responsabilité, ou par une autre personne également soumise à une obligation de secret conformément au droit de l'Union ou au droit d'un État membre ou aux règles arrêtées par les organismes nationaux compétents. »

RÉPONSE :  
Oui, notre association peut collecter des informations sur la santé de ses bénévoles, à condition que ce traitement soit effectué par un professionnel de la santé soumis à une obligation de secret professionnel conformément au droit de l'Union, au droit d'un État membre ou aux règles arrêtées par les organismes nationaux compétents, ou sous sa responsabilité [1]. Sinon, ce traitement relève d'une catégorie particulière de données à caractère personnel et n'est pas autorisé sans une base juridique appropriée, comme le consentement éclairé ou une obligation légale, ce qui n'est pas explicitement mentionné dans les extraits.
```

</details>

Temps : recherche 2.2 s · génération 29.0 s (3172 tokens lus, 301 écrits, 34.0 tokens/s)

## q19 — Qu'est-ce qu'une donnée personnelle ?

Article attendu : RGPD art. 4, définition 1 — passage [1].

### Réponse du copilote

> Une donnée personnelle est toute information se rapportant à une personne physique identifiée ou identifiable [1]. Cela inclut notamment des données telles que des noms, des numéros d’identification, des données de localisation, des identifiants en ligne ou des éléments spécifiques propres à l’identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale de cette personne [1]. Le terme est également utilisé dans le contexte de l’AI Act, où il est défini comme les données à caractère personnel définies à l’article 4, point 1), du règlement (UE) 2016/679 [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « «données à caractère personnel», toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée»); »
  [3] « «données à caractère personnel», les données à caractère personnel définies à l’article 4, point 1), du règlement (UE) 2016/679; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 4, définition 1 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [3] AI Act — règlement (UE) 2024/1689, article 3, définition 50 : Définitions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
  [4] RGPD — règlement (UE) 2016/679, article 4, définition 14 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [5] AI Act — règlement (UE) 2024/1689, article 3, définition 34 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
Attention : La réponse s'appuie sur le RGPD et l'AI Act sans dire de quel règlement vient chaque obligation : « Une donnée personnelle est toute information se rapportant à une personne physique identifiée ou identifiable. » (et 1 autre(s)).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « «données à caractère personnel», toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée»); »
- [3] « «données à caractère personnel», les données à caractère personnel définies à l’article 4, point 1), du règlement (UE) 2016/679; »

RÉPONSE :
Une donnée personnelle est toute information se rapportant à une personne physique identifiée ou identifiable [1]. Cela inclut notamment des données telles que des noms, des numéros d’identification, des données de localisation, des identifiants en ligne ou des éléments spécifiques propres à l’identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale de cette personne [1]. Le terme est également utilisé dans le contexte de l’AI Act, où il est défini comme les données à caractère personnel définies à l’article 4, point 1), du règlement (UE) 2016/679 [3].
```

</details>

Temps : recherche 2.2 s · génération 17.7 s (2117 tokens lus, 255 écrits, 36.4 tokens/s)

## q20 — À partir de quel âge un enfant peut-il s'inscrire seul à notre service en ligne ?

Article attendu : RGPD art. 8 — passage [1].

### Réponse du copilote

> Un enfant peut s'inscrire seul à notre service en ligne à partir de 16 ans [1]. À moins de 16 ans, le traitement de ses données ne peut être licite que si le consentement est donné ou autorisé par le titulaire de la responsabilité parentale [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Lorsque l'article 6, paragraphe 1, point a), s'applique, en ce qui concerne l'offre directe de services de la société de l'information aux enfants, le traitement des données à caractère personnel relatives à un enfant est licite lorsque l'enfant est âgé d'au moins 16 ans. Lorsque l'enfant est âgé de moins de 16 ans, ce traitement n'est licite que si, et dans la mesure où, le consentement est donné ou autorisé par le titulaire de la responsabilité parentale à l'égard de l'enfant. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 8 : Conditions applicables au consentement des enfants en ce qui concerne les services de la société de l'information (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_8
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [3] RGPD — règlement (UE) 2016/679, article 57, paragraphe 1, points a) à t) : Missions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_57
  [4] AI Act — règlement (UE) 2024/1689, article 58, paragraphe 2 : Modalités détaillées pour les bacs à sable réglementaires de l’IA et fonctionnement de ceux-ci
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_58
  [5] AI Act — règlement (UE) 2024/1689, article 63 : Dérogations pour des opérateurs spécifiques
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_63

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Lorsque l'article 6, paragraphe 1, point a), s'applique, en ce qui concerne l'offre directe de services de la société de l'information aux enfants, le traitement des données à caractère personnel relatives à un enfant est licite lorsque l'enfant est âgé d'au moins 16 ans. Lorsque l'enfant est âgé de moins de 16 ans, ce traitement n'est licite que si, et dans la mesure où, le consentement est donné ou autorisé par le titulaire de la responsabilité parentale à l'égard de l'enfant. »

RÉPONSE :  
Un enfant peut s'inscrire seul à notre service en ligne à partir de 16 ans [1]. À moins de 16 ans, le traitement de ses données ne peut être licite que si le consentement est donné ou autorisé par le titulaire de la responsabilité parentale [1].
```

</details>

Temps : recherche 2.2 s · génération 34.5 s (3942 tokens lus, 220 écrits, 32.3 tokens/s)

## q21 — Comment dois-je protéger les données personnelles que nous conservons ?

Article attendu : RGPD art. 32 — absent des passages donnés au modèle.

### Réponse du copilote

> Vous devez protéger les données personnelles en les limitant à ce qui est nécessaire aux finalités du traitement (minimisation des données) [1]. Les données doivent être exactes et, en cas d’inexactitude, rectifiées ou effacées sans tarder [1]. Leur conservation ne doit pas dépasser la durée nécessaire aux finalités initiales, sauf pour des fins archivistiques, scientifiques ou statistiques, à condition que des mesures techniques et organisationnelles appropriées soient mises en œuvre [1]. Le responsable du traitement doit mettre en œuvre des mesures techniques et organisationnelles pour que, par défaut, seules les données nécessaires soient traitées, notamment en ce qui concerne la quantité, l’étendue, la durée de conservation et l’accessibilité [2]. Ces mesures doivent garantir que les données ne sont pas accessibles à un nombre indéterminé de personnes sans l’intervention de la personne concernée [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée (limitation de la conservation); »
  [2] « le responsable du traitement met en œuvre les mesures techniques et organisationnelles appropriées pour garantir que, par défaut, seules les données à caractère personnel qui sont nécessaires au regard de chaque finalité spécifique du traitement sont traitées. Cela s'applique à la quantité de données à caractère personnel collectées, à l'étendue de leur traitement, à leur durée de conservation et à leur accessibilité. »
  [2] « En particulier, ces mesures garantissent que, par défaut, les données à caractère personnel ne sont pas rendues accessibles à un nombre indéterminé de personnes physiques sans l'intervention de la personne physique concernée. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
  [2] RGPD — règlement (UE) 2016/679, article 25 : Protection des données dès la conception et protection des données par défaut (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_25
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 1 : Objet et objectifs
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_1
  [4] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [5] RGPD — règlement (UE) 2016/679, article 98 : Réexamen d'autres actes juridiques de l'Union relatifs à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_98
Attention : 2 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1], [1]) : ignoré(s).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « les données à caractère personnel doivent être adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités pour lesquelles elles sont traitées (minimisation des données); »
- [1] « les données à caractère personnel doivent être exactes et, si nécessaire, tenues à jour; toutes les mesures raisonnables doivent être prises pour que les données à caractère personnel qui sont inexactes, eu égard aux finalités pour lesquelles elles sont traitées, soient effacées ou rectifiées sans tarder (exactitude); »
- [1] « les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée (limitation de la conservation); »
- [2] « le responsable du traitement met en œuvre les mesures techniques et organisationnelles appropriées pour garantir que, par défaut, seules les données à caractère personnel qui sont nécessaires au regard de chaque finalité spécifique du traitement sont traitées. Cela s'applique à la quantité de données à caractère personnel collectées, à l'étendue de leur traitement, à leur durée de conservation et à leur accessibilité. »
- [2] « En particulier, ces mesures garantissent que, par défaut, les données à caractère personnel ne sont pas rendues accessibles à un nombre indéterminé de personnes physiques sans l'intervention de la personne physique concernée. »

RÉPONSE :
Vous devez protéger les données personnelles en les limitant à ce qui est nécessaire aux finalités du traitement (minimisation des données) [1]. Les données doivent être exactes et, en cas d’inexactitude, rectifiées ou effacées sans tarder [1]. Leur conservation ne doit pas dépasser la durée nécessaire aux finalités initiales, sauf pour des fins archivistiques, scientifiques ou statistiques, à condition que des mesures techniques et organisationnelles appropriées soient mises en œuvre [1]. Le responsable du traitement doit mettre en œuvre des mesures techniques et organisationnelles pour que, par défaut, seules les données nécessaires soient traitées, notamment en ce qui concerne la quantité, l’étendue, la durée de conservation et l’accessibilité [2]. Ces mesures doivent garantir que les données ne sont pas accessibles à un nombre indéterminé de personnes sans l’intervention de la personne concernée [2].
```

</details>

Temps : recherche 2.1 s · génération 35.6 s (2802 tokens lus, 636 écrits, 34.2 tokens/s)

## q22 — Le consentement d'une personne doit-il être donné par écrit ?

Article attendu : RGPD art. 7 — passage [1].

### Réponse du copilote

> Non, le consentement n’est pas obligatoirement donné par écrit, car le RGPD (article 4, point 11) définit le consentement comme « toute manifestation de volonté, libre, spécifique, éclairée et univoque par laquelle la personne concernée accepte, par une déclaration ou par un acte positif clair, que des données à caractère personnel la concernant fassent l'objet d'un traitement ». Cela inclut des formes orales ou autres actes positifs clairs, sauf dans les cas où une déclaration écrite est exigée, comme dans le cas d'une déclaration qui concerne d'autres questions [1]. Le consentement éclairé dans les essais en conditions réelles doit être « daté et documenté » [2], ce qui implique une forme écrite, mais ce point est spécifique aux essais en conditions réelles, pas à tous les cas de traitement. Le texte ne précise pas que le consentement doit être écrit dans tous les cas, donc il peut être donné par un acte positif clair, oralement ou autrement, à condition qu’il soit libre, spécifique, éclairé et univoque [4]. Les passages trouvés ne permettent pas de conclure qu’il doit être écrit dans tous les cas, seulement que certaines formes (comme une déclaration écrite) peuvent être utilisées dans des contextes précis [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Si le consentement de la personne concernée est donné dans le cadre d'une déclaration écrite qui concerne également d'autres questions, la demande de consentement est présentée sous une forme qui la distingue clairement de ces autres questions… »
  [2] « Le consentement éclairé est daté et documenté et une copie en est remise aux participants aux essais ou à leur représentant légal. »
  [4] « «consentement éclairé», l’expression libre, spécifique, univoque et volontaire, par un participant, de sa volonté de participer à un essai en conditions réelles particulier, après avoir été informé de tous les éléments de l’essai qui lui permettent de prendre sa décision concernant sa participation ; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 7 : Conditions applicables au consentement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_7
  [2] AI Act — règlement (UE) 2024/1689, article 61 : Consentement éclairé à participer aux essais en conditions réelles en dehors des bacs à sable réglementaires de l’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_61
  [4] AI Act — règlement (UE) 2024/1689, article 3, définition 59 : Définitions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 11 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [5] RGPD — règlement (UE) 2016/679, article 8 : Conditions applicables au consentement des enfants en ce qui concerne les services de la société de l'information
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_8
Attention : La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Non, le consentement n’est pas obligatoirement donné par écrit, car le RGPD (article 4, point 11) définit le … ». Vérifiez ce point.
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « toute manifestation de volonté, libre, spécifique, éclairée et univoque par laquelle la personne concernée accepte, par … ».
Attention : La réponse formule une exception qui ne reprend pas les extraits vérifiés : « sauf dans les cas où une déclaration écrite est exigée, comme dans le cas ». Vérifiez-la dans les textes.
Attention : La réponse s'appuie sur le RGPD et l'AI Act sans dire de quel règlement vient chaque obligation : « Cela inclut des formes orales ou autres actes positifs clairs, sauf dans les cas où une déclaration écrite est exigée, … » (et 3 autre(s)).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Si le consentement de la personne concernée est donné dans le cadre d'une déclaration écrite qui concerne également d'autres questions, la demande de consentement est présentée sous une forme qui la distingue clairement de ces autres questions… »  
- [2] « Le consentement éclairé est daté et documenté et une copie en est remise aux participants aux essais ou à leur représentant légal. »  
- [4] « «consentement éclairé», l’expression libre, spécifique, univoque et volontaire, par un participant, de sa volonté de participer à un essai en conditions réelles particulier, après avoir été informé de tous les éléments de l’essai qui lui permettent de prendre sa décision concernant sa participation ; »  

RÉPONSE :  
Non, le consentement n’est pas obligatoirement donné par écrit, car le RGPD (article 4, point 11) définit le consentement comme « toute manifestation de volonté, libre, spécifique, éclairée et univoque par laquelle la personne concernée accepte, par une déclaration ou par un acte positif clair, que des données à caractère personnel la concernant fassent l'objet d'un traitement ». Cela inclut des formes orales ou autres actes positifs clairs, sauf dans les cas où une déclaration écrite est exigée, comme dans le cas d'une déclaration qui concerne d'autres questions [1]. Le consentement éclairé dans les essais en conditions réelles doit être « daté et documenté » [2], ce qui implique une forme écrite, mais ce point est spécifique aux essais en conditions réelles, pas à tous les cas de traitement. Le texte ne précise pas que le consentement doit être écrit dans tous les cas, donc il peut être donné par un acte positif clair, oralement ou autrement, à condition qu’il soit libre, spécifique, éclairé et univoque [4]. Les passages trouvés ne permettent pas de conclure qu’il doit être écrit dans tous les cas, seulement que certaines formes (comme une déclaration écrite) peuvent être utilisées dans des contextes précis [1].
```

</details>

Temps : recherche 2.2 s · génération 27.3 s (2398 tokens lus, 497 écrits, 35.2 tokens/s)

## q23 — Quelles utilisations de l'intelligence artificielle sont interdites en Europe ?

Article attendu : AI Act art. 5 — passage [1].

### Réponse du copilote

> Les utilisations de l’intelligence artificielle sont interdites en Europe lorsque :  
> - on infère les émotions d’une personne physique sur le lieu de travail ou dans les établissements d’enseignement, sauf pour des raisons médicales ou de sécurité [1] ;  
> - on catégorise individuellement une personne sur la base de ses données biométriques pour déduire sa race, ses opinions politiques, son affiliation syndicale, ses convictions religieuses ou philosophiques, sa vie sexuelle ou son orientation sexuelle, sauf dans le domaine répressif [1] ;  
> - on utilise des systèmes d’identification biométrique à distance en temps réel dans des espaces accessibles au public à des fins répressives, sauf dans les cas précisément autorisés : la recherche de victimes d’enlèvement, de traite ou d’exploitation sexuelle, la prévention d’une menace imminente pour la vie ou la sécurité, ou la localisation d’une personne soupçonnée d’infraction pénale pour une enquête ou une sanction [1] ;  
> - on utilise des techniques subliminales ou manipulatrices visant à altérer le comportement d’une personne ou d’un groupe, causant un préjudice

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement, sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité; »
  [1] « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes de catégorisation biométrique qui catégorisent individuellement les personnes physiques sur la base de leurs données biométriques afin d’arriver à des déductions ou des inférences concernant leur race, leurs opinions politiques, leur affiliation à une organisation syndicale, leurs convictions religieuses ou philosophiques, leur vie sexuelle ou leur orientation sexuelle; cette interdiction ne couvre pas l’étiquetage ou le filtrage d’ensembles de données biométriques acquis légalement, tels que des images, fondés sur des données biométriques ou la catégorisation de données biométriques dans le domaine répressif; »
  [1] « l’utilisation de systèmes d’identification biométrique à distance en temps réel dans des espaces accessibles au public à des fins répressives, sauf si et dans la mesure où cette utilisation est strictement nécessaire eu égard à l’un des objectifs suivants: i) la recherche ciblée de victimes spécifiques d’enlèvement, de la traite ou de l’exploitation sexuelle d’êtres humains, ainsi que la recherche de personnes disparues; ii) la prévention d’une menace spécifique, substantielle et imminente pour la vie ou la sécurité physique de personnes physiques ou d’une menace réelle et actuelle ou réelle et prévisible d’attaque terroriste; iii) la localisation ou l’identification d’une personne soupçonnée d’avoir commis une infraction pénale, aux fins de mener une enquête pénale, d’engager des poursuites ou d’exécuter une sanction pénale pour des infractions visées à l’annexe II et punissables dans l’État membre concerné d’une peine ou d’une mesure de sûreté privatives de liberté d’une durée maximale d’au moins quatre ans. »
  [2] « la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui a recours à des techniques subliminales, au-dessous du seuil de conscience d’une personne, ou à des techniques délibérément manipulatrices ou trompeuses, avec pour objectif ou effet d’altérer substantiellement le comportement d’une personne ou d’un groupe de personnes en portant considérablement atteinte à leur capacité à prendre une décision éclairée, amenant ainsi la personne à prendre une décision qu’elle n’aurait pas prise autrement, d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne, à une autre personne ou à un groupe de personnes; »
  [2] « la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui exploite les éventuelles vulnérabilités dues à l’âge, au handicap ou à la situation sociale ou économique spécifique d’une personne physique ou d’un groupe de personnes donné avec pour objectif ou effet d’altérer substantiellement le comportement de cette personne ou d’un membre de ce groupe d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne ou à un tiers; »
  [2] « la mise sur le marché, la mise en service ou l’utilisation d'un système d'IA qui génère ou manipule des images, des vidéos, des contenus audio ou tout autre matériel similaire réalistes représentant les parties intimes d'une personne identifiable, ou une personne identifiable se livrant à des activités sexuellement explicites, sans le consentement libre, spécifique, éclairé, univoque et explicite de cette personne pour cette production ou manipulation; »
  [2] « la mise sur le marché, la mise en service ou l’utilisation de systèmes d’IA pour l’évaluation ou la classification de personnes physiques ou de groupes de personnes au cours d’une période donnée en fonction de leur comportement social ou de caractéristiques personnelles ou de personnalité connues, déduites ou prédites, la note sociale conduisant à l’une ou l’autre des situations suivantes, ou aux deux: i) le traitement préjudiciable ou défavorable de certaines personnes physiques ou de groupes de personnes dans des contextes sociaux dissociés du contexte dans lequel les données ont été générées ou collectées à l’origine; ii) le traitement préjudiciable ou défavorable de certaines personnes ou de groupes de personnes, qui est injustifié ou disproportionné par rapport à leur comportement social ou à la gravité de celui-ci; »
  [2] « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA qui créent ou développent des bases de données de reconnaissance faciale par le moissonnage non ciblé d’images faciales provenant de l’internet ou de la vidéosurveillance; »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points f) à h) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [2] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points a) à e) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, article 1 : Objet
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_1
  [4] AI Act — règlement (UE) 2024/1689, annexe III, point 6 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [5] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 3 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
Attention : Réponse coupée : le modèle a atteint la limite de 1500 tokens (LLM_MAX_TOKENS), la fin de la réponse manque. Posez une question plus précise ou augmentez LLM_MAX_TOKENS dans .env.
Attention : La réponse formule une exception qui ne reprend pas les extraits vérifiés : « sauf dans les cas précisément autorisés : la recherche de victimes d’enlèvement, de traite ». Vérifiez-la dans les textes.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement, sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité; »
- [1] « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes de catégorisation biométrique qui catégorisent individuellement les personnes physiques sur la base de leurs données biométriques afin d’arriver à des déductions ou des inférences concernant leur race, leurs opinions politiques, leur affiliation à une organisation syndicale, leurs convictions religieuses ou philosophiques, leur vie sexuelle ou leur orientation sexuelle; cette interdiction ne couvre pas l’étiquetage ou le filtrage d’ensembles de données biométriques acquis légalement, tels que des images, fondés sur des données biométriques ou la catégorisation de données biométriques dans le domaine répressif; »
- [1] « l’utilisation de systèmes d’identification biométrique à distance en temps réel dans des espaces accessibles au public à des fins répressives, sauf si et dans la mesure où cette utilisation est strictement nécessaire eu égard à l’un des objectifs suivants: i) la recherche ciblée de victimes spécifiques d’enlèvement, de la traite ou de l’exploitation sexuelle d’êtres humains, ainsi que la recherche de personnes disparues; ii) la prévention d’une menace spécifique, substantielle et imminente pour la vie ou la sécurité physique de personnes physiques ou d’une menace réelle et actuelle ou réelle et prévisible d’attaque terroriste; iii) la localisation ou l’identification d’une personne soupçonnée d’avoir commis une infraction pénale, aux fins de mener une enquête pénale, d’engager des poursuites ou d’exécuter une sanction pénale pour des infractions visées à l’annexe II et punissables dans l’État membre concerné d’une peine ou d’une mesure de sûreté privatives de liberté d’une durée maximale d’au moins quatre ans. »
- [2] « la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui a recours à des techniques subliminales, au-dessous du seuil de conscience d’une personne, ou à des techniques délibérément manipulatrices ou trompeuses, avec pour objectif ou effet d’altérer substantiellement le comportement d’une personne ou d’un groupe de personnes en portant considérablement atteinte à leur capacité à prendre une décision éclairée, amenant ainsi la personne à prendre une décision qu’elle n’aurait pas prise autrement, d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne, à une autre personne ou à un groupe de personnes; »
- [2] « la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui exploite les éventuelles vulnérabilités dues à l’âge, au handicap ou à la situation sociale ou économique spécifique d’une personne physique ou d’un groupe de personnes donné avec pour objectif ou effet d’altérer substantiellement le comportement de cette personne ou d’un membre de ce groupe d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne ou à un tiers; »
- [2] « la mise sur le marché, la mise en service ou l’utilisation d'un système d'IA qui génère ou manipule des images, des vidéos, des contenus audio ou tout autre matériel similaire réalistes représentant les parties intimes d'une personne identifiable, ou une personne identifiable se livrant à des activités sexuellement explicites, sans le consentement libre, spécifique, éclairé, univoque et explicite de cette personne pour cette production ou manipulation; »
- [2] « la mise sur le marché, la mise en service ou l’utilisation de systèmes d’IA pour l’évaluation ou la classification de personnes physiques ou de groupes de personnes au cours d’une période donnée en fonction de leur comportement social ou de caractéristiques personnelles ou de personnalité connues, déduites ou prédites, la note sociale conduisant à l’une ou l’autre des situations suivantes, ou aux deux: i) le traitement préjudiciable ou défavorable de certaines personnes physiques ou de groupes de personnes dans des contextes sociaux dissociés du contexte dans lequel les données ont été générées ou collectées à l’origine; ii) le traitement préjudiciable ou défavorable de certaines personnes ou de groupes de personnes, qui est injustifié ou disproportionné par rapport à leur comportement social ou à la gravité de celui-ci; »
- [2] « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA qui créent ou développent des bases de données de reconnaissance faciale par le moissonnage non ciblé d’images faciales provenant de l’internet ou de la vidéosurveillance; »

RÉPONSE :
Les utilisations de l’intelligence artificielle sont interdites en Europe lorsque :  
- on infère les émotions d’une personne physique sur le lieu de travail ou dans les établissements d’enseignement, sauf pour des raisons médicales ou de sécurité [1] ;  
- on catégorise individuellement une personne sur la base de ses données biométriques pour déduire sa race, ses opinions politiques, son affiliation syndicale, ses convictions religieuses ou philosophiques, sa vie sexuelle ou son orientation sexuelle, sauf dans le domaine répressif [1] ;  
- on utilise des systèmes d’identification biométrique à distance en temps réel dans des espaces accessibles au public à des fins répressives, sauf dans les cas précisément autorisés : la recherche de victimes d’enlèvement, de traite ou d’exploitation sexuelle, la prévention d’une menace imminente pour la vie ou la sécurité, ou la localisation d’une personne soupçonnée d’infraction pénale pour une enquête ou une sanction [1] ;  
- on utilise des techniques subliminales ou manipulatrices visant à altérer le comportement d’une personne ou d’un groupe, causant un préjudice
```

</details>

Temps : recherche 2.2 s · génération 74.8 s (3802 tokens lus, 1500 écrits, 31.1 tokens/s)

## q24 — Ai-je le droit d'utiliser une IA qui analyse les émotions de mes salariés ?

Article attendu : AI Act art. 5 — absent des passages donnés au modèle.

### Réponse du copilote

> Oui, vous pouvez utiliser une IA qui analyse les émotions de vos salariés, à condition que cette utilisation ne soit pas liée à des fins de prévention ou de détection d’infractions pénales ou d’enquêtes, et que vous respectiez les obligations de transparence prévues par l’article 50 de l’AI Act [1]. Cependant, si l’analyse des émotions est utilisée pour prendre des décisions influant sur les conditions des relations professionnelles, la promotion ou le licenciement, ou pour évaluer les performances ou le comportement des salariés, alors cela relève des systèmes d’IA à haut risque visés à l’annexe III, point 4, b), et vous êtes donc obligé d’effectuer une analyse d’impact sur les droits fondamentaux avant le déploiement [4] et de noter les résultats à l’autorité de surveillance du marché [5]. Cette obligation s’applique à la première utilisation du système [5].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les déployeurs d’un système de reconnaissance des émotions ou d’un système de catégorisation biométrique informent les personnes physiques qui y sont exposées du fonctionnement du système et traitent les données à caractère personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680, selon le cas. Cette obligation ne s’applique pas aux systèmes d’IA utilisés pour la catégorisation biométrique et la reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l’Union. »
  [4] « Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des domaines suivants: 4. Emploi, gestion de la main-d'œuvre et accès à l'emploi indépendant: a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; b) systèmes d'IA destinés à être utilisés pour prendre des décisions influant sur les conditions des relations professionnelles, la promotion ou le licenciement dans le cadre de relations professionnelles contractuelles, pour attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques personnelles ou pour suivre et évaluer les performances et le comportement de personnes dans le cadre de telles relations. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 3 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [4] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [5] AI Act — règlement (UE) 2024/1689, article 27 : Analyse d’impact des systèmes d’IA à haut risque sur les droits fondamentaux (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_27
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 7, paragraphe 2 : Modifications de l’annexe III
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_7
  [3] AI Act — règlement (UE) 2024/1689, article 86 : Droit à l’explication des décisions individuelles
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_86
Attention : La réponse cite [5] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les déployeurs d’un système de reconnaissance des émotions ou d’un système de catégorisation biométrique informent les personnes physiques qui y sont exposées du fonctionnement du système et traitent les données à caractère personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680, selon le cas. Cette obligation ne s’applique pas aux systèmes d’IA utilisés pour la catégorisation biométrique et la reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l’Union. »  
- [4] « Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des domaines suivants: 4. Emploi, gestion de la main-d'œuvre et accès à l'emploi indépendant: a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; b) systèmes d'IA destinés à être utilisés pour prendre des décisions influant sur les conditions des relations professionnelles, la promotion ou le licenciement dans le cadre de relations professionnelles contractuelles, pour attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques personnelles ou pour suivre et évaluer les performances et le comportement de personnes dans le cadre de telles relations. »  

RÉPONSE :  
Oui, vous pouvez utiliser une IA qui analyse les émotions de vos salariés, à condition que cette utilisation ne soit pas liée à des fins de prévention ou de détection d’infractions pénales ou d’enquêtes, et que vous respectiez les obligations de transparence prévues par l’article 50 de l’AI Act [1]. Cependant, si l’analyse des émotions est utilisée pour prendre des décisions influant sur les conditions des relations professionnelles, la promotion ou le licenciement, ou pour évaluer les performances ou le comportement des salariés, alors cela relève des systèmes d’IA à haut risque visés à l’annexe III, point 4, b), et vous êtes donc obligé d’effectuer une analyse d’impact sur les droits fondamentaux avant le déploiement [4] et de noter les résultats à l’autorité de surveillance du marché [5]. Cette obligation s’applique à la première utilisation du système [5].
```

</details>

Temps : recherche 2.2 s · génération 46.7 s (3707 tokens lus, 677 écrits, 32.0 tokens/s)

## q25 — Mon logiciel est-il un « système d'IA » au sens de la loi européenne ?

Article attendu : AI Act art. 3, définition 1 — passage [2].

### Réponse du copilote

> Oui, votre logiciel est un « système d'IA » au sens de la loi européenne, s’il répond aux critères définis dans l’article 3, paragraphe 1, de l’AI Act : s’il est un système automatisé conçu pour fonctionner à différents niveaux d’autonomie, capable d’adaptation après déploiement, et qui, pour des objectifs explicites ou implicites, déduit à partir des entrées qu’il reçoit la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « «système d’IA», un système automatisé qui est conçu pour fonctionner à différents niveaux d’autonomie et peut faire preuve d’une capacité d’adaptation après son déploiement, et qui, pour des objectifs explicites ou implicites, déduit, à partir des entrées qu’il reçoit, la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels; »

Sources citées :
  [2] AI Act — règlement (UE) 2024/1689, article 3, définition 1 : Définitions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, annexe III, point 8 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [3] AI Act — règlement (UE) 2024/1689, article 6, point d : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
  [4] AI Act — règlement (UE) 2024/1689, annexe III, point 6 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [5] AI Act — règlement (UE) 2024/1689, article 6, point c : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [2] « «système d’IA», un système automatisé qui est conçu pour fonctionner à différents niveaux d’autonomie et peut faire preuve d’une capacité d’adaptation après son déploiement, et qui, pour des objectifs explicites ou implicites, déduit, à partir des entrées qu’il reçoit, la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels; »

RÉPONSE :
Oui, votre logiciel est un « système d'IA » au sens de la loi européenne, s’il répond aux critères définis dans l’article 3, paragraphe 1, de l’AI Act : s’il est un système automatisé conçu pour fonctionner à différents niveaux d’autonomie, capable d’adaptation après déploiement, et qui, pour des objectifs explicites ou implicites, déduit à partir des entrées qu’il reçoit la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels [2].
```

</details>

Temps : recherche 2.6 s · génération 21.3 s (2415 tokens lus, 275 écrits, 35.3 tokens/s)

## q26 — Dois-je indiquer qu'une image publiée sur notre site a été créée par une IA ?

Article attendu : AI Act art. 50 — passage [1].

### Réponse du copilote

> Oui, vous devez indiquer que l’image a été créée par une IA, sauf si l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière [1], ou si l’image fait partie d’une œuvre manifestement artistique, créative, satirique, fictif ou analogue, dans ce cas la transparence se limite à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre [1]. De plus, cette obligation ne s’applique pas si le système d’IA ne modifie pas de manière substantielle les données d’entrée fournies par vous ou leur sémantique [2]. Cependant, si l’image est un contenu de synthèse de type image, elle doit être marquée comme ayant été générée par une IA [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. Cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. Lorsque le contenu fait partie d’une œuvre ou d’un programme manifestement artistique, créatif, satirique, fictif ou analogue, les obligations de transparence énoncées au présent paragraphe se limitent à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 4 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 2 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1 ter : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [4] AI Act — règlement (UE) 2024/1689, annexe IV, point 1 : Documentation technique visée à l'article 11, paragraphe 1
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_IV
  [5] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1 bis : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([2]) : ignoré(s).
Attention : La réponse cite [2] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. Cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. Lorsque le contenu fait partie d’une œuvre ou d’un programme manifestement artistique, créatif, satirique, fictif ou analogue, les obligations de transparence énoncées au présent paragraphe se limitent à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre. »
- [2] « Les fournisseurs de systèmes d’IA, y compris de systèmes d’IA à usage général, qui génèrent des contenus de synthèse de type audio, image, vidéo ou texte, veillent à ce que les sorties des systèmes d’IA soient marquées dans un format lisible par machine et identifiables comme ayant été générées ou manipulées par une IA. Cette obligation ne s’applique pas dans la mesure où les systèmes d’IA remplissent une fonction d’assistance pour la mise en forme standard ou ne modifient pas de manière substantielle les données d’entrée fournies par le déployeur ou leur sémantique, ou lorsque leur utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. »

RÉPONSE :
Oui, vous devez indiquer que l’image a été créée par une IA, sauf si l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière [1], ou si l’image fait partie d’une œuvre manifestement artistique, créative, satirique, fictif ou analogue, dans ce cas la transparence se limite à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre [1]. De plus, cette obligation ne s’applique pas si le système d’IA ne modifie pas de manière substantielle les données d’entrée fournies par vous ou leur sémantique [2]. Cependant, si l’image est un contenu de synthèse de type image, elle doit être marquée comme ayant été générée par une IA [2].
```

</details>

Temps : recherche 2.2 s · génération 34.1 s (2670 tokens lus, 633 écrits, 34.3 tokens/s)

## q27 — Quelles amendes prévoit le règlement européen sur l'intelligence artificielle ?

Article attendu : AI Act art. 99 — passage [1].

### Réponse du copilote

> Le règlement européen sur l’intelligence artificielle prévoit plusieurs types d’amendes selon les cas. Pour le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5, les amendes peuvent aller jusqu’à 35 000 000 EUR ou, pour une entreprise, jusqu’à 7 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu [1]. Dans le cas des institutions, organes ou organismes de l’Union, le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’une amende administrative pouvant aller jusqu’à 1 500 000 EUR [2]. La non-conformité du système d’IA avec d’autres exigences du règlement, que celles de l’article 5, fait l’objet d’une amende administrative pouvant aller jusqu’à 750 000 EUR [2]. Pour les fournisseurs de modèles d’IA à usage général, les amendes ne dépassent pas 3 % de leur chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, ou 15 000 000 EUR, le montant le plus élevé étant retenu, dans les cas précisés par les points a) à d) [3]. Enfin, la fourniture d’informations inexactes, incomplètes ou trompeuses aux organismes notifiés ou aux autorités nationales compétentes en réponse à une demande fait l’objet d’une amende administrative pouvant aller jusqu’à 7 500 000 EUR ou, pour une entreprise, jusqu’à 1 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’amendes administratives pouvant aller jusqu’à 35 000 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 7 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu. »
  [2] « Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’une amende administrative pouvant aller jusqu’à 1 500 000 EUR. »
  [2] « La non-conformité du système d’IA avec les exigences ou obligations au titre du présent règlement, autres que celles énoncées à l’article 5, fait l’objet d’une amende administrative pouvant aller jusqu’à 750 000 EUR. »
  [3] « La Commission peut infliger aux fournisseurs de modèles d’IA à usage général des amendes n’excédant pas 3 % de leur chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, ou 15 000 000 EUR, le montant le plus élevé étant retenu, lorsque la Commission constate que le fournisseur, de manière délibérée ou par négligence: a) a enfreint les dispositions pertinentes du présent règlement; b) n’a pas donné suite à une demande de document ou d’informations au titre de l’article 91, ou a fourni des informations inexactes, incomplètes ou trompeuses; c) ne s’est pas conformé à une mesure demandée au titre de l’article 93; d) n’a pas donné à la Commission accès au modèle d’IA à usage général ou au modèle d’IA à usage général présentant un risque systémique en vue de procéder à une évaluation conformément à l’article 92. »
  [4] « La fourniture d’informations inexactes, incomplètes ou trompeuses aux organismes notifiés ou aux autorités nationales compétentes en réponse à une demande fait l’objet d’une amende administrative pouvant aller jusqu’à 7 500 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 1 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 3 : Sanctions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [2] AI Act — règlement (UE) 2024/1689, article 100 : Amendes administratives imposées aux institutions, organes et organismes de l’Union (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_100
  [3] AI Act — règlement (UE) 2024/1689, article 101 : Amendes applicables aux fournisseurs de modèles d’IA à usage général (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_101
  [4] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 5 : Sanctions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
Passages consultés mais non cités :
  [5] AI Act — règlement (UE) 2024/1689, article 110 : Modification de la directive (UE) 2020/1828
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_110

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’amendes administratives pouvant aller jusqu’à 35 000 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 7 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu. »
- [2] « Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’une amende administrative pouvant aller jusqu’à 1 500 000 EUR. »
- [2] « La non-conformité du système d’IA avec les exigences ou obligations au titre du présent règlement, autres que celles énoncées à l’article 5, fait l’objet d’une amende administrative pouvant aller jusqu’à 750 000 EUR. »
- [3] « La Commission peut infliger aux fournisseurs de modèles d’IA à usage général des amendes n’excédant pas 3 % de leur chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, ou 15 000 000 EUR, le montant le plus élevé étant retenu, lorsque la Commission constate que le fournisseur, de manière délibérée ou par négligence: a) a enfreint les dispositions pertinentes du présent règlement; b) n’a pas donné suite à une demande de document ou d’informations au titre de l’article 91, ou a fourni des informations inexactes, incomplètes ou trompeuses; c) ne s’est pas conformé à une mesure demandée au titre de l’article 93; d) n’a pas donné à la Commission accès au modèle d’IA à usage général ou au modèle d’IA à usage général présentant un risque systémique en vue de procéder à une évaluation conformément à l’article 92. »
- [4] « La fourniture d’informations inexactes, incomplètes ou trompeuses aux organismes notifiés ou aux autorités nationales compétentes en réponse à une demande fait l’objet d’une amende administrative pouvant aller jusqu’à 7 500 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 1 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu. »

RÉPONSE :
Le règlement européen sur l’intelligence artificielle prévoit plusieurs types d’amendes selon les cas. Pour le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5, les amendes peuvent aller jusqu’à 35 000 000 EUR ou, pour une entreprise, jusqu’à 7 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu [1]. Dans le cas des institutions, organes ou organismes de l’Union, le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’une amende administrative pouvant aller jusqu’à 1 500 000 EUR [2]. La non-conformité du système d’IA avec d’autres exigences du règlement, que celles de l’article 5, fait l’objet d’une amende administrative pouvant aller jusqu’à 750 000 EUR [2]. Pour les fournisseurs de modèles d’IA à usage général, les amendes ne dépassent pas 3 % de leur chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, ou 15 000 000 EUR, le montant le plus élevé étant retenu, dans les cas précisés par les points a) à d) [3]. Enfin, la fourniture d’informations inexactes, incomplètes ou trompeuses aux organismes notifiés ou aux autorités nationales compétentes en réponse à une demande fait l’objet d’une amende administrative pouvant aller jusqu’à 7 500 000 EUR ou, pour une entreprise, jusqu’à 1 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu [4].
```

</details>

Temps : recherche 2.2 s · génération 55.0 s (3352 tokens lus, 1069 écrits, 32.2 tokens/s)

## h03 — Comment déclarer la création d'une association en préfecture ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 28, paragraphe 8 : Autorités notifiantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_28
  [2] AI Act — règlement (UE) 2024/1689, article 29 : Demande de notification d’un organisme d’évaluation de la conformité
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_29
  [3] RGPD — règlement (UE) 2016/679, article 56 : Compétence de l'autorité de contrôle chef de file
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_56
  [4] AI Act — règlement (UE) 2024/1689, article 30 : Procédure de notification
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_30
  [5] AI Act — règlement (UE) 2024/1689, article 33 : Filiales des organismes notifiés et sous-traitance
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_33

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun  
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Temps : recherche 2.2 s · génération 28.7 s (3936 tokens lus, 29 écrits, 33.3 tokens/s)

## h04 — Quel est le montant du SMIC cette année ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 4 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [2] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 5 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [3] AI Act — règlement (UE) 2024/1689, article 101 : Amendes applicables aux fournisseurs de modèles d’IA à usage général
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_101
  [4] AI Act — règlement (UE) 2024/1689, article 62 : Mesures en faveur des fournisseurs et déployeurs, en particulier les PME, y compris les jeunes pousses
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_62
  [5] AI Act — règlement (UE) 2024/1689, article 3, définition 40 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun  
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Temps : recherche 2.1 s · génération 20.1 s (3063 tokens lus, 29 écrits, 35.4 tokens/s)

## h05 — Comment rédiger les statuts d'une association ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les statuts d'une association peuvent inclure des dispositions sur les modalités d'application du RGPD, notamment en définissant les finalités et les moyens du traitement des données à caractère personnel, comme le prévoit l'article 4 du RGPD [2]. Si l'association est responsable du traitement, elle peut élaborer un code de conduite pour préciser les obligations relatives au traitement loyal et transparent, à la collecte des données, à la protection des enfants ou à la notification des violations [1]. Si plusieurs personnes ou organes participent à la décision des finalités du traitement, elles sont considérées comme des responsables conjoints, et doivent définir de manière transparente leurs obligations respectives, notamment en ce qui concerne l'exercice des droits des personnes concernées [3]. Cependant, les statuts ne doivent pas remplacer les obligations légales du RGPD, notamment celles relatives au registre des activités de traitement, qui doit être tenu par le responsable du traitement [4]. Enfin, les États membres peuvent introduire des dispositions spécifiques pour garantir un traitement licite et loyal, notamment dans des cas particuliers comme le traitement des données sensibles [5].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent élaborer des codes de conduite, les modifier ou les proroger, aux fins de préciser les modalités d'application du présent règlement, telles que: »
  [2] « «responsable du traitement», la personne physique ou morale, l'autorité publique, le service ou un autre organisme qui, seul ou conjointement avec d'autres, détermine les finalités et les moyens du traitement; »
  [3] « Lorsque deux responsables du traitement ou plus déterminent conjointement les finalités et les moyens du traitement, ils sont les responsables conjoints du traitement. Les responsables conjoints du traitement définissent de manière transparente leurs obligations respectives aux fins d'assurer le respect des exigences du présent règlement, notamment en ce qui concerne l'exercice des droits de la personne concernée, et leurs obligations respectives quant à la communication des informations visées aux articles 13 et 14, par voie d'accord entre eux, sauf si, et dans la mesure, où leurs obligations respectives sont définies par le droit de l'Union ou par le droit de l'État membre auquel les responsables du traitement sont soumis. »
  [4] « Chaque responsable du traitement et, le cas échéant, le représentant du responsable du traitement tiennent un registre des activités de traitement effectuées sous leur responsabilité. »
  [5] « Les États membres peuvent maintenir ou introduire des dispositions plus spécifiques pour adapter l'application des règles du présent règlement pour ce qui est du traitement dans le but de respecter le paragraphe 1, points c) et e), en déterminant plus précisément les exigences spécifiques applicables au traitement ainsi que d'autres mesures visant à garantir un traitement licite et loyal, y compris dans d'autres situations particulières de traitement comme le prévoit le chapitre IX. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [2] RGPD — règlement (UE) 2016/679, article 4, définition 7 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [3] RGPD — règlement (UE) 2016/679, article 26 : Responsables conjoints du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_26
  [4] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30
  [5] RGPD — règlement (UE) 2016/679, article 6, paragraphe 2 : Licéité du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent élaborer des codes de conduite, les modifier ou les proroger, aux fins de préciser les modalités d'application du présent règlement, telles que: »  
- [2] « «responsable du traitement», la personne physique ou morale, l'autorité publique, le service ou un autre organisme qui, seul ou conjointement avec d'autres, détermine les finalités et les moyens du traitement; »  
- [3] « Lorsque deux responsables du traitement ou plus déterminent conjointement les finalités et les moyens du traitement, ils sont les responsables conjoints du traitement. Les responsables conjoints du traitement définissent de manière transparente leurs obligations respectives aux fins d'assurer le respect des exigences du présent règlement, notamment en ce qui concerne l'exercice des droits de la personne concernée, et leurs obligations respectives quant à la communication des informations visées aux articles 13 et 14, par voie d'accord entre eux, sauf si, et dans la mesure, où leurs obligations respectives sont définies par le droit de l'Union ou par le droit de l'État membre auquel les responsables du traitement sont soumis. »  
- [4] « Chaque responsable du traitement et, le cas échéant, le représentant du responsable du traitement tiennent un registre des activités de traitement effectuées sous leur responsabilité. »  
- [5] « Les États membres peuvent maintenir ou introduire des dispositions plus spécifiques pour adapter l'application des règles du présent règlement pour ce qui est du traitement dans le but de respecter le paragraphe 1, points c) et e), en déterminant plus précisément les exigences spécifiques applicables au traitement ainsi que d'autres mesures visant à garantir un traitement licite et loyal, y compris dans d'autres situations particulières de traitement comme le prévoit le chapitre IX. »

RÉPONSE :  
Les statuts d'une association peuvent inclure des dispositions sur les modalités d'application du RGPD, notamment en définissant les finalités et les moyens du traitement des données à caractère personnel, comme le prévoit l'article 4 du RGPD [2]. Si l'association est responsable du traitement, elle peut élaborer un code de conduite pour préciser les obligations relatives au traitement loyal et transparent, à la collecte des données, à la protection des enfants ou à la notification des violations [1]. Si plusieurs personnes ou organes participent à la décision des finalités du traitement, elles sont considérées comme des responsables conjoints, et doivent définir de manière transparente leurs obligations respectives, notamment en ce qui concerne l'exercice des droits des personnes concernées [3]. Cependant, les statuts ne doivent pas remplacer les obligations légales du RGPD, notamment celles relatives au registre des activités de traitement, qui doit être tenu par le responsable du traitement [4]. Enfin, les États membres peuvent introduire des dispositions spécifiques pour garantir un traitement licite et loyal, notamment dans des cas particuliers comme le traitement des données sensibles [5].
```

</details>

Temps : recherche 2.2 s · génération 40.1 s (2970 tokens lus, 733 écrits, 33.6 tokens/s)
