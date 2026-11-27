# Réponses du copilote — v8_local_v1

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 27/11/2026 à 19:45 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen3:4b-instruct` via Ollama 0.40.18 — température 0.1, contexte 8192 tokens, couches sur la carte graphique : toutes, 2000 tokens au plus par réponse, dont 800 gardés pour la réponse (recopie des extraits arrêtée après 1200 tokens si la réponse n'a pas commencé)
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_v1.jsonl` (17 + 3 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q11 | Un client me demande d'effacer toutes ses données : suis-je obligé de le faire ? | 5/5 | non | La réponse change le sens d'une condition ou d'une exception (négation ou inversion ajoutée ou retirée, ou règle contraire à celle de l'extrait) : « lorsque l'un des motifs suivants s'applique : les données ne sont plus nécessaires ». Vérifiez ce point. | 54 s |
| q12 | Un salarié demande une copie de toutes les données que nous avons sur lui : que dois-je lui donner ? | 1/2 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([4]) : ignoré(s).; La réponse ne cite aucun passage et une phrase ne reprend pas les extraits vérifiés : « Ce droit s'applique à tout traitement, y compris celui réalisé dans le cadre des relations de travail (RGPD, article … » (et 1 autre(s)). Vérifiez-la dans les textes.; La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à moins qu’ elle ne demande autrement (RGPD, article 15, paragraphe 3) ». Vérifiez-la dans les textes. | 54 s |
| q13 | Un adhérent veut récupérer ses données pour les donner à une autre association : est-ce un droit ? | 1/1 | non | — | 33 s |
| q14 | Puis-je envoyer une lettre d'information par e-mail à mes adhérents, et peuvent-ils refuser ? | 5/5 | non | — | 46 s |
| q15 | Mon prestataire informatique a accès à nos fichiers : faut-il signer un contrat particulier ? | 4/4 | non | La réponse met entre « » un texte introuvable dans les extraits vérifiés : « sur instruction documentée du responsable du traitement ».; La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à moins qu’ il ne soit tenu d’y procéder par le droit de l’Union ou ». Vérifiez-la dans les textes. | 46 s |
| q16 | Puis-je stocker les fichiers de mon association chez un hébergeur situé aux États-Unis ? | 4/4 | non | La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à condition que l'un des mécanismes prévus par le RGPD soit respecté ». Vérifiez-la dans les textes.; Phrase retirée de la réponse : elle disait qu'un pays a ou n'a pas de décision d'adéquation (ou de niveau de protection adéquat), ce que les textes du copilote ne permettent pas de savoir : « Les États-Unis ne sont pas reconnus comme assurant un niveau de protection adéquat par une décision de la Commission, … ». | 51 s |
| q17 | Quelles sanctions risque une petite entreprise qui ne respecte pas le RGPD ? | 4/4 | non | — | 40 s |
| q18 | Notre association peut-elle collecter des informations sur la santé de ses bénévoles ? | 2/3 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([2]) : ignoré(s).; La réponse cite [2] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.; La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Non, l'association ne peut pas collecter des informations sur la santé de ses bénévoles, car le traitement de données … ». Vérifiez ce point. | 31 s |
| q19 | Qu'est-ce qu'une donnée personnelle ? | 2/2 | non | La réponse s'appuie sur le RGPD et l'AI Act sans dire de quel règlement vient chaque obligation : « Une donnée personnelle est toute information se rapportant à une personne physique identifiée ou identifiable. » (et 1 autre(s)). | 27 s |
| q20 | À partir de quel âge un enfant peut-il s'inscrire seul à notre service en ligne ? | 1/1 | non | — | 41 s |
| q21 | Comment dois-je protéger les données personnelles que nous conservons ? | 4/4 | non | — | 72 s |
| q22 | Le consentement d'une personne doit-il être donné par écrit ? | 3/3 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 33 s |
| q23 | Quelles utilisations de l'intelligence artificielle sont interdites en Europe ? | 7/7 | non | Extraits trop longs : le code a arrêté leur recopie après 1200 tokens pour garder au moins 800 tokens à la réponse (dernier extrait raccourci ou retiré ; le passage complet est dans les sources).; La réponse cite [4] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.; La réponse formule une exception qui ne reprend pas les extraits vérifiés : « sauf dans les cas précisément autorisés : la recherche de victimes d’enlèvement, de traite » (et 1 autre(s)). Vérifiez-la dans les textes. | 112 s |
| q24 | Ai-je le droit d'utiliser une IA qui analyse les émotions de mes salariés ? | 2/2 | non | — | 34 s |
| q25 | Mon logiciel est-il un « système d'IA » au sens de la loi européenne ? | 1/1 | non | — | 25 s |
| q26 | Dois-je indiquer qu'une image publiée sur notre site a été créée par une IA ? | 1/2 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([3]) : ignoré(s).; La réponse cite [3] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations. | 37 s |
| q27 | Quelles amendes prévoit le règlement européen sur l'intelligence artificielle ? | 4/4 | non | La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Ces amendes sont déterminées en fonction de la nature, de la gravité et de la durée de la violation, tout en tenant … ». Vérifiez qui est concerné. | 63 s |
| h03 | Comment déclarer la création d'une association en préfecture ? | 0/0 | oui | — | 33 s |
| h04 | Quel est le montant du SMIC cette année ? | 0/0 | oui | — | 23 s |
| h05 | Comment rédiger les statuts d'une association ? | 0/0 | oui | — | 23 s |

## q11 — Un client me demande d'effacer toutes ses données : suis-je obligé de le faire ?

Article attendu : RGPD art. 17 — passage [1].

### Réponse du copilote

> Oui : vous êtes obligé d'effacer les données à caractère personnel du client dans les meilleurs délais, lorsque l'un des motifs suivants s'applique : les données ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées, le client a retiré son consentement sans autre fondement juridique, il s'oppose au traitement sans motif légitime impérieux, les données ont fait l'objet d'un traitement illicite, ou elles doivent être effacées pour respecter une obligation légale [1]. Cependant, cette obligation ne s'applique pas si le traitement est nécessaire à l'exercice du droit à la liberté d'expression, à l'exécution d'une mission d'intérêt public, à des fins archivistiques, de recherche scientifique ou historique, ou à la constatation, à l'exercice ou à la défense de droits en justice [1]. Vous devez également informer les responsables du traitement qui traitent ces données que la personne a demandé l'effacement, à moins que cela ne soit impossible ou exige des efforts disproportionnés [2]. Les données doivent être conservées uniquement pendant une durée nécessaire aux finalités initiales, sauf pour des fins archivistiques, scientifiques ou statistiques, dans la mesure où des mesures appropriées sont mises en œuvre [3]. Le client a le droit de demander l'effacement, la rectification ou une limitation du traitement [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit d'obtenir du responsable du traitement l'effacement, dans les meilleurs délais, de données à caractère personnel la concernant et le responsable du traitement a l'obligation d'effacer ces données à caractère personnel dans les meilleurs délais, lorsque l'un des motifs suivants s'applique: … »
  [1] « Les paragraphes 1 et 2 ne s'appliquent pas dans la mesure où ce traitement est nécessaire: … »
  [2] « Le responsable du traitement notifie à chaque destinataire auquel les données à caractère personnel ont été communiquées toute rectification ou tout effacement de données à caractère personnel ou toute limitation du traitement effectué conformément à l'article 16, à l'article 17, paragraphe 1, et à l'article 18, à moins qu'une telle communication se révèle impossible ou exige des efforts disproportionnés. »
  [3] « Les données à caractère personnel doivent être: … adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités pour lesquelles elles sont traitées (minimisation des données); … conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées; … »
  [4] « l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ainsi que du droit de s'opposer au traitement et du droit à la portabilité des données; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 17 : Droit à l'effacement («droit à l'oubli») (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_17
  [2] RGPD — règlement (UE) 2016/679, article 19 : Obligation de notification en ce qui concerne la rectification ou l'effacement de données à caractère personnel ou la limitation du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_19
  [3] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
  [4] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
Passages consultés mais non cités :
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
Attention : La réponse change le sens d'une condition ou d'une exception (négation ou inversion ajoutée ou retirée, ou règle contraire à celle de l'extrait) : « lorsque l'un des motifs suivants s'applique : les données ne sont plus nécessaires ». Vérifiez ce point.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « La personne concernée a le droit d'obtenir du responsable du traitement l'effacement, dans les meilleurs délais, de données à caractère personnel la concernant et le responsable du traitement a l'obligation d'effacer ces données à caractère personnel dans les meilleurs délais, lorsque l'un des motifs suivants s'applique: … »
- [1] « Les paragraphes 1 et 2 ne s'appliquent pas dans la mesure où ce traitement est nécessaire: … »
- [2] « Le responsable du traitement notifie à chaque destinataire auquel les données à caractère personnel ont été communiquées toute rectification ou tout effacement de données à caractère personnel ou toute limitation du traitement effectué conformément à l'article 16, à l'article 17, paragraphe 1, et à l'article 18, à moins qu'une telle communication se révèle impossible ou exige des efforts disproportionnés. »
- [3] « Les données à caractère personnel doivent être: … adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités pour lesquelles elles sont traitées (minimisation des données); … conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées; … »
- [4] « l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ainsi que du droit de s'opposer au traitement et du droit à la portabilité des données; »

RÉPONSE :
Oui : vous êtes obligé d'effacer les données à caractère personnel du client dans les meilleurs délais, lorsque l'un des motifs suivants s'applique : les données ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées, le client a retiré son consentement sans autre fondement juridique, il s'oppose au traitement sans motif légitime impérieux, les données ont fait l'objet d'un traitement illicite, ou elles doivent être effacées pour respecter une obligation légale [1]. Cependant, cette obligation ne s'applique pas si le traitement est nécessaire à l'exercice du droit à la liberté d'expression, à l'exécution d'une mission d'intérêt public, à des fins archivistiques, de recherche scientifique ou historique, ou à la constatation, à l'exercice ou à la défense de droits en justice [1]. Vous devez également informer les responsables du traitement qui traitent ces données que la personne a demandé l'effacement, à moins que cela ne soit impossible ou exige des efforts disproportionnés [2]. Les données doivent être conservées uniquement pendant une durée nécessaire aux finalités initiales, sauf pour des fins archivistiques, scientifiques ou statistiques, dans la mesure où des mesures appropriées sont mises en œuvre [3]. Le client a le droit de demander l'effacement, la rectification ou une limitation du traitement [4].
```

</details>

Temps : recherche 2.5 s · génération 45.7 s (3664 tokens lus, 717 écrits, 32.5 tokens/s) · contrôle de pertinence 5.8 s

## q12 — Un salarié demande une copie de toutes les données que nous avons sur lui : que dois-je lui donner ?

Article attendu : RGPD art. 15 — passage [2].

### Réponse du copilote

> Vous devez lui fournir une copie des données à caractère personnel qui vous concernent (RGPD, article 15, paragraphe 3). Ce droit s'applique à tout traitement, y compris celui réalisé dans le cadre des relations de travail (RGPD, article 88, paragraphe 1). Vous pouvez exiger un paiement de frais raisonnables basés sur les coûts administratifs pour une copie supplémentaire (RGPD, article 15, paragraphe 3). Si la demande est faite par voie électronique, les informations doivent être fournies sous une forme électronique d'usage courant, à moins qu’elle ne demande autrement (RGPD, article 15, paragraphe 3). Vous devez également lui fournir les informations suivantes : les finalités du traitement, les catégories de données concernées, les destinataires ou catégories de destinataires, la durée de conservation des données ou les critères utilisés pour déterminer cette durée, le droit de rectification, d’effacement, de limitation du traitement, de s’opposer au traitement ou de porter une réclamation auprès d’une autorité de contrôle, ainsi que l’existence d’une prise de décision automatisée, y compris un profilage, avec les informations utiles sur la logique sous-jacente et les conséquences prévues pour lui (RGPD, article 15, paragraphes 1 à 4).

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « Le responsable du traitement fournit une copie des données à caractère personnel faisant l'objet d'un traitement. Le responsable du traitement peut exiger le paiement de frais raisonnables basés sur les coûts administratifs pour toute copie supplémentaire demandée par la personne concernée. Lorsque la personne concernée présente sa demande par voie électronique, les informations sont fournies sous une forme électronique d'usage courant, à moins que la personne concernée ne demande qu'il en soit autrement. »

Sources citées :
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [3] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [4] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([4]) : ignoré(s).
Attention : La réponse ne cite aucun passage et une phrase ne reprend pas les extraits vérifiés : « Ce droit s'applique à tout traitement, y compris celui réalisé dans le cadre des relations de travail (RGPD, article … » (et 1 autre(s)). Vérifiez-la dans les textes.
Attention : La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à moins qu’ elle ne demande autrement (RGPD, article 15, paragraphe 3) ». Vérifiez-la dans les textes.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [2] « Le responsable du traitement fournit une copie des données à caractère personnel faisant l'objet d'un traitement. Le responsable du traitement peut exiger le paiement de frais raisonnables basés sur les coûts administratifs pour toute copie supplémentaire demandée par la personne concernée. Lorsque la personne concernée présente sa demande par voie électronique, les informations sont fournies sous une forme électronique d'usage courant, à moins que la personne concernée ne demande qu'il en soit autrement. »
- [4] « Lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée, le responsable du traitement fournit à celle-ci toutes les informations suivantes: … c) l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ainsi que du droit de s'opposer au traitement et du droit à la portabilité des données; … g) l'existence d'une prise de décision automatisée, y compris un profilage, visée à l'article 22, paragraphes 1 et 4, et, au moins en pareils cas, des informations utiles concernant la logique sous-jacente, ainsi que l'importance et les conséquences prévues de ce traitement pour la personne concernée. »

RÉPONSE :
Vous devez lui fournir une copie des données à caractère personnel qui vous concernent (RGPD, article 15, paragraphe 3). Ce droit s'applique à tout traitement, y compris celui réalisé dans le cadre des relations de travail (RGPD, article 88, paragraphe 1). Vous pouvez exiger un paiement de frais raisonnables basés sur les coûts administratifs pour une copie supplémentaire (RGPD, article 15, paragraphe 3). Si la demande est faite par voie électronique, les informations doivent être fournies sous une forme électronique d'usage courant, à moins qu’elle ne demande autrement (RGPD, article 15, paragraphe 3). Vous devez également lui fournir les informations suivantes : les finalités du traitement, les catégories de données concernées, les destinataires ou catégories de destinataires, la durée de conservation des données ou les critères utilisés pour déterminer cette durée, le droit de rectification, d’effacement, de limitation du traitement, de s’opposer au traitement ou de porter une réclamation auprès d’une autorité de contrôle, ainsi que l’existence d’une prise de décision automatisée, y compris un profilage, avec les informations utiles sur la logique sous-jacente et les conséquences prévues pour lui (RGPD, article 15, paragraphes 1 à 4).
```

</details>

Temps : recherche 2.2 s · génération 47.4 s (4058 tokens lus, 652 écrits, 31.7 tokens/s) · contrôle de pertinence 4.3 s

## q13 — Un adhérent veut récupérer ses données pour les donner à une autre association : est-ce un droit ?

Article attendu : RGPD art. 20 — passage [1].

### Réponse du copilote

> Oui, c’est un droit : l’adhérent a le droit de recevoir ses données à caractère personnel dans un format structuré, couramment utilisé et lisible par machine, et de les transmettre à un autre responsable du traitement, sans que le responsable du traitement auquel les données ont été communiquées y fasse obstacle, lorsque le traitement est fondé sur le consentement ou sur un contrat et qu’il est effectué à l’aide de procédés automatisés [1].

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
  [5] RGPD — règlement (UE) 2016/679, article 6, paragraphe 1 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les personnes concernées ont le droit de recevoir les données à caractère personnel les concernant qu'elles ont fournies à un responsable du traitement, dans un format structuré, couramment utilisé et lisible par machine, et ont le droit de transmettre ces données à un autre responsable du traitement sans que le responsable du traitement auquel les données à caractère personnel ont été communiquées y fasse obstacle, lorsque: a) le traitement est fondé sur le consentement en application de l'article 6, paragraphe 1, point a), ou de l'article 9, paragraphe 2, point a), ou sur un contrat en application de l'article 6, paragraphe 1, point b); et b) le traitement est effectué à l'aide de procédés automatisés. »

RÉPONSE :  
Oui, c’est un droit : l’adhérent a le droit de recevoir ses données à caractère personnel dans un format structuré, couramment utilisé et lisible par machine, et de les transmettre à un autre responsable du traitement, sans que le responsable du traitement auquel les données ont été communiquées y fasse obstacle, lorsque le traitement est fondé sur le consentement ou sur un contrat et qu’il est effectué à l’aide de procédés automatisés [1].
```

</details>

Temps : recherche 2.2 s · génération 26.7 s (3086 tokens lus, 300 écrits, 34.4 tokens/s) · contrôle de pertinence 3.8 s

## q14 — Puis-je envoyer une lettre d'information par e-mail à mes adhérents, et peuvent-ils refuser ?

Article attendu : RGPD art. 21 ou RGPD art. 6, paragraphe 1 — passage [1].

### Réponse du copilote

> Oui, vous pouvez envoyer une lettre d'information par e-mail à vos adhérents, car cela relève de la prospection, et donc du traitement des données à caractère personnel à des fins de prospection (RGPD, article 1, paragraphe 1, point e) ou f), et du profilage lié à cette prospection (RGPD, article 1, paragraphe 1, point e) ou f), [1]). Cependant, chaque adhérent a le droit de s'opposer à ce traitement à tout moment, pour des raisons tenant à sa situation particulière (RGPD, article 21, paragraphe 1, [1]). Lorsqu’un adhérent s’oppose à ce traitement, les données ne sont plus traitées à ces fins (RGPD, article 21, paragraphe 3, [1]). Ce droit doit être explicitement porté à l’attention de la personne concernée au plus tard au moment de la première communication (RGPD, article 21, paragraphe 4, [1]). Ainsi, les adhérents peuvent refuser le traitement de leurs données à caractère personnel à des fins de prospection, et ce droit leur est offert par le RGPD (article 21, [1]).

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit de s'opposer à tout moment, pour des raisons tenant à sa situation particulière, à un traitement des données à caractère personnel la concernant fondé sur l'article 6, paragraphe 1, point e) ou f), y compris un profilage fondé sur ces dispositions. »
  [1] « Lorsque les données à caractère personnel sont traitées à des fins de prospection, la personne concernée a le droit de s'opposer à tout moment au traitement des données à caractère personnel la concernant à de telles fins de prospection, y compris au profilage dans la mesure où il est lié à une telle prospection. »
  [1] « Lorsque la personne concernée s'oppose au traitement à des fins de prospection, les données à caractère personnel ne sont plus traitées à ces fins. »
  [2] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: … »
  [4] « La personne concernée a le droit de mandater un organisme, une organisation ou une association à but non lucratif, qui a été valablement constitué conformément au droit d'un État membre, dont les objectifs statutaires sont d'intérêt public et est actif dans le domaine de la protection des droits et libertés des personnes concernées dans le cadre de la protection des données à caractère personnel les concernant, pour qu'il introduise une réclamation en son nom, exerce en son nom les droits visés aux articles 77, 78 et 79 et exerce en son nom le droit d'obtenir réparation visé à l'article 82 lorsque le droit d'un État membre le prévoit. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 21 : Droit d'opposition (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_21
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [4] RGPD — règlement (UE) 2016/679, article 80 : Représentation des personnes concernées (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_80
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 24 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [5] RGPD — règlement (UE) 2016/679, article 35, paragraphe 9 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « La personne concernée a le droit de s'opposer à tout moment, pour des raisons tenant à sa situation particulière, à un traitement des données à caractère personnel la concernant fondé sur l'article 6, paragraphe 1, point e) ou f), y compris un profilage fondé sur ces dispositions. »  
- [1] « Lorsque les données à caractère personnel sont traitées à des fins de prospection, la personne concernée a le droit de s'opposer à tout moment au traitement des données à caractère personnel la concernant à de telles fins de prospection, y compris au profilage dans la mesure où il est lié à une telle prospection. »  
- [1] « Lorsque la personne concernée s'oppose au traitement à des fins de prospection, les données à caractère personnel ne sont plus traitées à ces fins. »  
- [2] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: … »  
- [4] « La personne concernée a le droit de mandater un organisme, une organisation ou une association à but non lucratif, qui a été valablement constitué conformément au droit d'un État membre, dont les objectifs statutaires sont d'intérêt public et est actif dans le domaine de la protection des droits et libertés des personnes concernées dans le cadre de la protection des données à caractère personnel les concernant, pour qu'il introduise une réclamation en son nom, exerce en son nom les droits visés aux articles 77, 78 et 79 et exerce en son nom le droit d'obtenir réparation visé à l'article 82 lorsque le droit d'un État membre le prévoit. »

RÉPONSE :  
Oui, vous pouvez envoyer une lettre d'information par e-mail à vos adhérents, car cela relève de la prospection, et donc du traitement des données à caractère personnel à des fins de prospection (RGPD, article 1, paragraphe 1, point e) ou f), et du profilage lié à cette prospection (RGPD, article 1, paragraphe 1, point e) ou f), [1]). Cependant, chaque adhérent a le droit de s'opposer à ce traitement à tout moment, pour des raisons tenant à sa situation particulière (RGPD, article 21, paragraphe 1, [1]). Lorsqu’un adhérent s’oppose à ce traitement, les données ne sont plus traitées à ces fins (RGPD, article 21, paragraphe 3, [1]). Ce droit doit être explicitement porté à l’attention de la personne concernée au plus tard au moment de la première communication (RGPD, article 21, paragraphe 4, [1]). Ainsi, les adhérents peuvent refuser le traitement de leurs données à caractère personnel à des fins de prospection, et ce droit leur est offert par le RGPD (article 21, [1]).
```

</details>

Temps : recherche 2.2 s · génération 38.3 s (2988 tokens lus, 733 écrits, 34.0 tokens/s) · contrôle de pertinence 5.8 s

## q15 — Mon prestataire informatique a accès à nos fichiers : faut-il signer un contrat particulier ?

Article attendu : RGPD art. 28, paragraphe 3 — passage [1].

### Réponse du copilote

> Oui : il faut signer un contrat particulier, car le prestataire informatique, en ayant accès à vos fichiers, est considéré comme un sous-traitant (RGPD, article 28, alinéa 4) et le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique qui définit les obligations du sous-traitant (RGPD, article 28, alinéa 3) [1]. Ce contrat doit notamment préciser que le sous-traitant ne traite les données qu’« sur instruction documentée du responsable du traitement » (a), y compris pour les transferts vers un pays tiers, à moins qu’il ne soit tenu d’y procéder par le droit de l’Union ou d’un État membre [1]. Le contrat doit aussi inclure les mesures techniques et organisationnelles appropriées pour garantir la protection des données (RGPD, article 28, alinéa 1) [2]. En outre, le sous-traitant ne peut pas traiter les données qu’il a accès à, sauf sur instruction du responsable du traitement ou s’il est obligé par le droit de l’Union ou d’un État membre (RGPD, article 29, alinéa 3) [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre, qui lie le sous-traitant à l'égard du responsable du traitement, définit l'objet et la durée du traitement, la nature et la finalité du traitement, le type de données à caractère personnel et les catégories de personnes concernées, et les obligations et les droits du responsable du traitement. Ce contrat ou cet autre acte juridique prévoit, notamment, que le sous-traitant: … »
  [2] « Lorsqu'un traitement doit être effectué pour le compte d'un responsable du traitement, celui-ci fait uniquement appel à des sous-traitants qui présentent des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées de manière à ce que le traitement réponde aux exigences du présent règlement et garantisse la protection des droits de la personne concernée. »
  [3] « Le sous-traitant et toute personne agissant sous l'autorité du responsable du traitement ou sous celle du sous-traitant, qui a accès à des données à caractère personnel, ne peut pas traiter ces données, excepté sur instruction du responsable du traitement, à moins d'y être obligé par le droit de l'Union ou le droit d'un État membre. »
  [4] « «sous-traitant», la personne physique ou morale, l'autorité publique, le service ou un autre organisme qui traite des données à caractère personnel pour le compte du responsable du traitement; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 28, paragraphe 3 : Sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [2] RGPD — règlement (UE) 2016/679, article 28, paragraphe 1 : Sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [3] RGPD — règlement (UE) 2016/679, article 29 : Traitement effectué sous l'autorité du responsable du traitement ou du sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_29
  [4] RGPD — règlement (UE) 2016/679, article 4, définition 8 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
Passages consultés mais non cités :
  [5] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « sur instruction documentée du responsable du traitement ».
Attention : La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à moins qu’ il ne soit tenu d’y procéder par le droit de l’Union ou ». Vérifiez-la dans les textes.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre, qui lie le sous-traitant à l'égard du responsable du traitement, définit l'objet et la durée du traitement, la nature et la finalité du traitement, le type de données à caractère personnel et les catégories de personnes concernées, et les obligations et les droits du responsable du traitement. Ce contrat ou cet autre acte juridique prévoit, notamment, que le sous-traitant: … »
- [2] « Lorsqu'un traitement doit être effectué pour le compte d'un responsable du traitement, celui-ci fait uniquement appel à des sous-traitants qui présentent des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées de manière à ce que le traitement réponde aux exigences du présent règlement et garantisse la protection des droits de la personne concernée. »
- [3] « Le sous-traitant et toute personne agissant sous l'autorité du responsable du traitement ou sous celle du sous-traitant, qui a accès à des données à caractère personnel, ne peut pas traiter ces données, excepté sur instruction du responsable du traitement, à moins d'y être obligé par le droit de l'Union ou le droit d'un État membre. »
- [4] « «sous-traitant», la personne physique ou morale, l'autorité publique, le service ou un autre organisme qui traite des données à caractère personnel pour le compte du responsable du traitement; »

RÉPONSE :  
Oui : il faut signer un contrat particulier, car le prestataire informatique, en ayant accès à vos fichiers, est considéré comme un sous-traitant (RGPD, article 28, alinéa 4) et le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique qui définit les obligations du sous-traitant (RGPD, article 28, alinéa 3) [1]. Ce contrat doit notamment préciser que le sous-traitant ne traite les données qu’« sur instruction documentée du responsable du traitement » (a), y compris pour les transferts vers un pays tiers, à moins qu’il ne soit tenu d’y procéder par le droit de l’Union ou d’un État membre [1]. Le contrat doit aussi inclure les mesures techniques et organisationnelles appropriées pour garantir la protection des données (RGPD, article 28, alinéa 1) [2]. En outre, le sous-traitant ne peut pas traiter les données qu’il a accès à, sauf sur instruction du responsable du traitement ou s’il est obligé par le droit de l’Union ou d’un État membre (RGPD, article 29, alinéa 3) [3].
```

</details>

Temps : recherche 2.2 s · génération 38.5 s (3168 tokens lus, 666 écrits, 33.7 tokens/s) · contrôle de pertinence 5.8 s

## q16 — Puis-je stocker les fichiers de mon association chez un hébergeur situé aux États-Unis ?

Article attendu : RGPD art. 44 ou RGPD art. 45, paragraphe 1 ou RGPD art. 46 — passage [1].

### Réponse du copilote

> Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, à condition que l'un des mécanismes prévus par le RGPD soit respecté. Si les États-Unis ont été reconnus comme assurant un niveau de protection adéquat par une décision de la Commission européenne (article 45, [1]), alors le transfert est autorisé sans autorisation spécifique. Si ce n'est pas le cas, vous devez mettre en place des garanties appropriées (article 46, [2]), telles que des clauses types de protection des données approuvées par la Commission, un code de conduite approuvé, ou un mécanisme de certification, accompagné d'un engagement contraignant et exécutoire de respecter les droits des personnes concernées. Ces garanties doivent permettre aux personnes concernées de disposer de droits opposables et de voies de droit effectives. Le transfert ne peut avoir lieu que si les conditions du chapitre 4 du RGPD sont respectées (article 44, [3]), notamment en ce qui concerne les droits des personnes concernées et la mise en œuvre de mesures de protection. [phrase retirée : le copilote ne peut pas savoir si ce pays bénéficie d'une décision d'adéquation] Les décisions d'authorisations ou de transferts par une juridiction américaine ne peuvent être reconnues que si elles sont fondées sur un accord international en vigueur entre les États-Unis et l'Union (article 48, [4]).

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. Un tel transfert ne nécessite pas d'autorisation spécifique. »
  [2] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
  [3] « Un transfert, vers un pays tiers ou à une organisation internationale, de données à caractère personnel qui font ou sont destinées à faire l'objet d'un traitement après ce transfert ne peut avoir lieu que si, sous réserve des autres dispositions du présent règlement, les conditions définies dans le présent chapitre sont respectées par le responsable du traitement et le sous-traitant, y compris pour les transferts ultérieurs de données à caractère personnel au départ du pays tiers ou de l'organisation internationale vers un autre pays tiers ou à une autre organisation internationale. »
  [4] « Toute décision d'une juridiction ou d'une autorité administrative d'un pays tiers exigeant d'un responsable du traitement ou d'un sous-traitant qu'il transfère ou divulgue des données à caractère personnel ne peut être reconnue ou rendue exécutoire de quelque manière que ce soit qu'à la condition qu'elle soit fondée sur un accord international, tel qu'un traité d'entraide judiciaire, en vigueur entre le pays tiers demandeur et l'Union ou un État membre, sans préjudice d'autres motifs de transfert en vertu du présent chapitre. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 45, paragraphe 1 : Transferts fondés sur une décision d'adéquation (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
  [2] RGPD — règlement (UE) 2016/679, article 46 : Transferts moyennant des garanties appropriées (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_46
  [3] RGPD — règlement (UE) 2016/679, article 44 : Principe général applicable aux transferts (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_44
  [4] RGPD — règlement (UE) 2016/679, article 48 : Transferts ou divulgations non autorisés par le droit de l'Union (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_48
Passages consultés mais non cités :
  [5] RGPD — règlement (UE) 2016/679, article 45, paragraphe 2 : Transferts fondés sur une décision d'adéquation
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
Note : La liste des pays bénéficiant d'une décision d'adéquation n'est pas dans les textes utilisés par le copilote : consultez la page de la Commission européenne sur les décisions d'adéquation (en anglais) : https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en
Attention : La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à condition que l'un des mécanismes prévus par le RGPD soit respecté ». Vérifiez-la dans les textes.
Attention : Phrase retirée de la réponse : elle disait qu'un pays a ou n'a pas de décision d'adéquation (ou de niveau de protection adéquat), ce que les textes du copilote ne permettent pas de savoir : « Les États-Unis ne sont pas reconnus comme assurant un niveau de protection adéquat par une décision de la Commission, … ».

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. Un tel transfert ne nécessite pas d'autorisation spécifique. »  
- [2] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »  
- [3] « Un transfert, vers un pays tiers ou à une organisation internationale, de données à caractère personnel qui font ou sont destinées à faire l'objet d'un traitement après ce transfert ne peut avoir lieu que si, sous réserve des autres dispositions du présent règlement, les conditions définies dans le présent chapitre sont respectées par le responsable du traitement et le sous-traitant, y compris pour les transferts ultérieurs de données à caractère personnel au départ du pays tiers ou de l'organisation internationale vers un autre pays tiers ou à une autre organisation internationale. »  
- [4] « Toute décision d'une juridiction ou d'une autorité administrative d'un pays tiers exigeant d'un responsable du traitement ou d'un sous-traitant qu'il transfère ou divulgue des données à caractère personnel ne peut être reconnue ou rendue exécutoire de quelque manière que ce soit qu'à la condition qu'elle soit fondée sur un accord international, tel qu'un traité d'entraide judiciaire, en vigueur entre le pays tiers demandeur et l'Union ou un État membre, sans préjudice d'autres motifs de transfert en vertu du présent chapitre. »  

RÉPONSE :  
Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, à condition que l'un des mécanismes prévus par le RGPD soit respecté. Si les États-Unis ont été reconnus comme assurant un niveau de protection adéquat par une décision de la Commission européenne (article 45, [1]), alors le transfert est autorisé sans autorisation spécifique. Si ce n'est pas le cas, vous devez mettre en place des garanties appropriées (article 46, [2]), telles que des clauses types de protection des données approuvées par la Commission, un code de conduite approuvé, ou un mécanisme de certification, accompagné d'un engagement contraignant et exécutoire de respecter les droits des personnes concernées. Ces garanties doivent permettre aux personnes concernées de disposer de droits opposables et de voies de droit effectives. Le transfert ne peut avoir lieu que si les conditions du chapitre 4 du RGPD sont respectées (article 44, [3]), notamment en ce qui concerne les droits des personnes concernées et la mise en œuvre de mesures de protection. Les États-Unis ne sont pas reconnus comme assurant un niveau de protection adéquat par une décision de la Commission, donc le transfert ne peut être effectué que sous réserve de garanties appropriées (article 46, [2]). Les décisions d'authorisations ou de transferts par une juridiction américaine ne peuvent être reconnues que si elles sont fondées sur un accord international en vigueur entre les États-Unis et l'Union (article 48, [4]).
```

</details>

Temps : recherche 2.2 s · génération 42.4 s (3045 tokens lus, 842 écrits, 33.7 tokens/s) · contrôle de pertinence 6.4 s

## q17 — Quelles sanctions risque une petite entreprise qui ne respecte pas le RGPD ?

Article attendu : RGPD art. 83, paragraphe 4 ou RGPD art. 83, paragraphe 5 — passage [1].

### Réponse du copilote

> Une petite entreprise qui ne respecte pas le RGPD peut être soumise à des amendes administratives, selon les dispositions violées. Pour les violations prévues aux articles 8, 11, 25 à 39, 42 et 43, l'amende peut s'élever jusqu’à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu’à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [1]. Pour les violations liées aux principes de base d’un traitement, aux droits des personnes concernées ou aux transferts à un pays tiers, l'amende peut s'élever jusqu’à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu’à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [3]. En outre, l'autorité de contrôle peut prendre des mesures correctrices, comme l'avertissement, le rappel à l'ordre, l'ordonnance de mise en conformité, la communication d'une violation, la limitation ou suspension du traitement, la rectification ou l'effacement de données, ou la suspension des flux de données [5]. Si les violations ne sont pas couvertes par les amendes prévues à l'article 83, les États membres peuvent imposer d'autres sanctions, qui doivent être effectives, proportionnées et dissuasives [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »
  [3] « les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »
  [5] « chaque autorité de contrôle dispose du pouvoir d'adopter toutes les mesures correctrices suivantes: … »
  [4] « Les États membres déterminent le régime des autres sanctions applicables en cas de violations du présent règlement, en particulier pour les violations qui ne font pas l'objet des amendes administratives prévues à l'article 83, et prennent toutes les mesures nécessaires pour garantir leur mise en œuvre. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 83, paragraphe 4 : Conditions générales pour imposer des amendes administratives (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83
  [3] RGPD — règlement (UE) 2016/679, article 83, paragraphe 5 : Conditions générales pour imposer des amendes administratives (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83
  [4] RGPD — règlement (UE) 2016/679, article 84 : Sanctions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_84
  [5] RGPD — règlement (UE) 2016/679, article 58, paragraphe 2 : Pouvoirs (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_58
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 83, paragraphe 1 : Conditions générales pour imposer des amendes administratives
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »
- [3] « les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »
- [5] « chaque autorité de contrôle dispose du pouvoir d'adopter toutes les mesures correctrices suivantes: … »
- [4] « Les États membres déterminent le régime des autres sanctions applicables en cas de violations du présent règlement, en particulier pour les violations qui ne font pas l'objet des amendes administratives prévues à l'article 83, et prennent toutes les mesures nécessaires pour garantir leur mise en œuvre. »

RÉPONSE :
Une petite entreprise qui ne respecte pas le RGPD peut être soumise à des amendes administratives, selon les dispositions violées. Pour les violations prévues aux articles 8, 11, 25 à 39, 42 et 43, l'amende peut s'élever jusqu’à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu’à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [1]. Pour les violations liées aux principes de base d’un traitement, aux droits des personnes concernées ou aux transferts à un pays tiers, l'amende peut s'élever jusqu’à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu’à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [3]. En outre, l'autorité de contrôle peut prendre des mesures correctrices, comme l'avertissement, le rappel à l'ordre, l'ordonnance de mise en conformité, la communication d'une violation, la limitation ou suspension du traitement, la rectification ou l'effacement de données, ou la suspension des flux de données [5]. Si les violations ne sont pas couvertes par les amendes prévues à l'article 83, les États membres peuvent imposer d'autres sanctions, qui doivent être effectives, proportionnées et dissuasives [4].
```

</details>

Temps : recherche 2.1 s · génération 32.5 s (2643 tokens lus, 658 écrits, 34.9 tokens/s) · contrôle de pertinence 5.3 s

## q18 — Notre association peut-elle collecter des informations sur la santé de ses bénévoles ?

Article attendu : RGPD art. 9, paragraphe 1 ou RGPD art. 9, paragraphe 2 — passage [2].

### Réponse du copilote

> Non, l'association ne peut pas collecter des informations sur la santé de ses bénévoles, car le traitement de données concernant la santé est interdit par le RGPD, article 9, paragraphe 2 [2]. Ce traitement est interdit même s'il s'agit de données relatives à la santé physique ou mentale d'une personne [3]. Cependant, les États membres peuvent introduire des conditions supplémentaires, y compris des limitations, en ce qui concerne le traitement de ces données [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « «données concernant la santé», les données à caractère personnel relatives à la santé physique ou mentale d'une personne physique, y compris la prestation de services de soins de santé, qui révèlent des informations sur l'état de santé de cette personne; »
  [4] « Les États membres peuvent maintenir ou introduire des conditions supplémentaires, y compris des limitations, en ce qui concerne le traitement des données génétiques, des données biométriques ou des données concernant la santé. »

Sources citées :
  [2] RGPD — règlement (UE) 2016/679, article 9, paragraphe 1 : Traitement portant sur des catégories particulières de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 15 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [4] RGPD — règlement (UE) 2016/679, article 9, paragraphe 4 : Traitement portant sur des catégories particulières de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 9, paragraphe 3 : Traitement portant sur des catégories particulières de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
  [5] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([2]) : ignoré(s).
Attention : La réponse cite [2] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.
Attention : La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Non, l'association ne peut pas collecter des informations sur la santé de ses bénévoles, car le traitement de données … ». Vérifiez ce point.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [2] « Le traitement des données à caractère personnel qui révèlent l'origine raciale ou ethnique, les opinions politiques, les convictions religieuses ou philosophiques ou l'appartenance syndicale, ainsi que le traitement des données génétiques, des données biométriques aux fins d'identifier une personne physique de manière unique, des données concernant la santé ou des données concernant la vie sexuelle ou l'orientation sexuelle d'une personne physique sont interdits. »  
- [3] « «données concernant la santé», les données à caractère personnel relatives à la santé physique ou mentale d'une personne physique, y compris la prestation de services de soins de santé, qui révèlent des informations sur l'état de santé de cette personne; »  
- [4] « Les États membres peuvent maintenir ou introduire des conditions supplémentaires, y compris des limitations, en ce qui concerne le traitement des données génétiques, des données biométriques ou des données concernant la santé. »

RÉPONSE :  
Non, l'association ne peut pas collecter des informations sur la santé de ses bénévoles, car le traitement de données concernant la santé est interdit par le RGPD, article 9, paragraphe 2 [2]. Ce traitement est interdit même s'il s'agit de données relatives à la santé physique ou mentale d'une personne [3]. Cependant, les États membres peuvent introduire des conditions supplémentaires, y compris des limitations, en ce qui concerne le traitement de ces données [4].
```

</details>

Temps : recherche 2.2 s · génération 25.0 s (2722 tokens lus, 358 écrits, 35.2 tokens/s) · contrôle de pertinence 3.5 s

## q19 — Qu'est-ce qu'une donnée personnelle ?

Article attendu : RGPD art. 4, définition 1 — passage [1].

### Réponse du copilote

> Une donnée personnelle est toute information se rapportant à une personne physique identifiée ou identifiable [1]. Cela inclut une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale [1]. Le terme «données à caractère personnel» est défini de la même manière dans le règlement (UE) 2024/1689, en référence à l'article 4, point 1), du règlement (UE) 2016/679 [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « «données à caractère personnel», toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée»); est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale; »
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
- [1] « «données à caractère personnel», toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée»); est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale; »
- [3] « «données à caractère personnel», les données à caractère personnel définies à l’article 4, point 1), du règlement (UE) 2016/679; »

RÉPONSE :
Une donnée personnelle est toute information se rapportant à une personne physique identifiée ou identifiable [1]. Cela inclut une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale [1]. Le terme «données à caractère personnel» est défini de la même manière dans le règlement (UE) 2024/1689, en référence à l'article 4, point 1), du règlement (UE) 2016/679 [3].
```

</details>

Temps : recherche 2.1 s · génération 21.1 s (2297 tokens lus, 374 écrits, 36.2 tokens/s) · contrôle de pertinence 3.9 s

## q20 — À partir de quel âge un enfant peut-il s'inscrire seul à notre service en ligne ?

Article attendu : RGPD art. 8 — passage [1].

### Réponse du copilote

> Un enfant peut s'inscrire seul à votre service en ligne à partir de 16 ans [1]. À moins de 16 ans, le traitement de ses données ne peut être licite que si le consentement est donné ou autorisé par le titulaire de la responsabilité parentale [1].

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
  [5] AI Act — règlement (UE) 2024/1689, article 58, paragraphe 1 : Modalités détaillées pour les bacs à sable réglementaires de l’IA et fonctionnement de ceux-ci
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_58

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Lorsque l'article 6, paragraphe 1, point a), s'applique, en ce qui concerne l'offre directe de services de la société de l'information aux enfants, le traitement des données à caractère personnel relatives à un enfant est licite lorsque l'enfant est âgé d'au moins 16 ans. Lorsque l'enfant est âgé de moins de 16 ans, ce traitement n'est licite que si, et dans la mesure où, le consentement est donné ou autorisé par le titulaire de la responsabilité parentale à l'égard de l'enfant. »  

RÉPONSE :  
Un enfant peut s'inscrire seul à votre service en ligne à partir de 16 ans [1]. À moins de 16 ans, le traitement de ses données ne peut être licite que si le consentement est donné ou autorisé par le titulaire de la responsabilité parentale [1].
```

</details>

Temps : recherche 2.2 s · génération 35.5 s (4204 tokens lus, 221 écrits, 32.0 tokens/s) · contrôle de pertinence 3.7 s

## q21 — Comment dois-je protéger les données personnelles que nous conservons ?

Article attendu : RGPD art. 32 — passage [1].

### Réponse du copilote

> Vous devez protéger les données personnelles que vous conservez en mettant en œuvre des mesures techniques et organisationnelles appropriées, conformément au RGPD, article 32, afin de garantir un niveau de sécurité adapté au risque, notamment par la pseudonymisation et le chiffrement des données, la garantie de la confidentialité, de l'intégrité, de la disponibilité et de la résilience des systèmes, la possibilité de rétablir rapidement l'accès aux données en cas d'incident, et une procédure régulière de test et d'évaluation de ces mesures [1]. Ces mesures doivent s'appliquer à la quantité, à l'étendue, à la durée de conservation et à l'accessibilité des données, en veillant à ce que seules les données nécessaires aux finalités spécifiques soient traitées [2]. Les données doivent être traitées de manière licite, loyale, transparente, adéquate, pertinente, limitée, exactes et conservées pendant une durée ne dépassant pas celle nécessaire aux finalités [3]. Le responsable du traitement doit s'assurer que le traitement est effectué conformément au règlement, en mettant en œuvre des politiques de protection des données et en réexaminant et actualisant ces mesures si nécessaire [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Compte tenu de l'état des connaissances, des coûts de mise en œuvre et de la nature, de la portée, du contexte et des finalités du traitement ainsi que des risques, dont le degré de probabilité et de gravité varie, pour les droits et libertés des personnes physiques, le responsable du traitement et le sous-traitant mettent en œuvre les mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque, y compris entre autres, selon les besoins: a) la pseudonymisation et le chiffrement des données à caractère personnel; b) des moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement; c) des moyens permettant de rétablir la disponibilité des données à caractère personnel et l'accès à celles-ci dans des délais appropriés en cas d'incident physique ou technique; d) une procédure visant à tester, à analyser et à évaluer régulièrement l'efficacité des mesures techniques et organisationnelles pour assurer la sécurité du traitement. »
  [2] « Le responsable du traitement met en œuvre les mesures techniques et organisationnelles appropriées pour garantir que, par défaut, seules les données à caractère personnel qui sont nécessaires au regard de chaque finalité spécifique du traitement sont traitées. Cela s'applique à la quantité de données à caractère personnel collectées, à l'étendue de leur traitement, à leur durée de conservation et à leur accessibilité. En particulier, ces mesures garantissent que, par défaut, les données à caractère personnel ne sont pas rendues accessibles à un nombre indéterminé de personnes physiques sans l'intervention de la personne physique concernée. »
  [3] « Les données à caractère personnel doivent être: a) traitées de manière licite, loyale et transparente au regard de la personne concernée (licéité, loyauté, transparence); b) collectées pour des finalités déterminées, explicites et légitimes, et ne pas être traitées ultérieurement d'une manière incompatible avec ces finalités; le traitement ultérieur à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques n'est pas considéré, conformément à l'article 89, paragraphe 1, comme incompatible avec les finalités initiales (limitation des finalités); c) adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités pour lesquelles elles sont traitées (minimisation des données); d) exactes et, si nécessaire, tenues à jour; toutes les mesures raisonnables doivent être prises pour que les données à caractère personnel qui sont inexactes, eu égard aux finalités pour lesquelles elles sont traitées, soient effacées ou rectifiées sans tarder (exactitude); e) conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées; les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée (limitation de la conservation); f) traitées de façon à garantir une sécurité appropriée des données à caractère personnel, y compris la protection contre le traitement non autorisé ou illicite et contre la perte, la destruction ou les dégâts d'origine accidentelle, à l'aide de mesures techniques ou organisationnelles appropriées (intégrité et confidentialité); »
  [4] « Compte tenu de la nature, de la portée, du contexte et des finalités du traitement ainsi que des risques, dont le degré de probabilité et de gravité varie, pour les droits et libertés des personnes physiques, le responsable du traitement met en œuvre des mesures techniques et organisationnelles appropriées pour s'assurer et être en mesure de démontrer que le traitement est effectué conformément au présent règlement. Ces mesures sont réexaminées et actualisées si nécessaire. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 32 : Sécurité du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_32
  [2] RGPD — règlement (UE) 2016/679, article 25 : Protection des données dès la conception et protection des données par défaut (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_25
  [3] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
  [4] RGPD — règlement (UE) 2016/679, article 24 : Responsabilité du responsable du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_24
Passages consultés mais non cités :
  [5] RGPD — règlement (UE) 2016/679, article 98 : Réexamen d'autres actes juridiques de l'Union relatifs à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_98

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Compte tenu de l'état des connaissances, des coûts de mise en œuvre et de la nature, de la portée, du contexte et des finalités du traitement ainsi que des risques, dont le degré de probabilité et de gravité varie, pour les droits et libertés des personnes physiques, le responsable du traitement et le sous-traitant mettent en œuvre les mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque, y compris entre autres, selon les besoins: a) la pseudonymisation et le chiffrement des données à caractère personnel; b) des moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement; c) des moyens permettant de rétablir la disponibilité des données à caractère personnel et l'accès à celles-ci dans des délais appropriés en cas d'incident physique ou technique; d) une procédure visant à tester, à analyser et à évaluer régulièrement l'efficacité des mesures techniques et organisationnelles pour assurer la sécurité du traitement. »
- [2] « Le responsable du traitement met en œuvre les mesures techniques et organisationnelles appropriées pour garantir que, par défaut, seules les données à caractère personnel qui sont nécessaires au regard de chaque finalité spécifique du traitement sont traitées. Cela s'applique à la quantité de données à caractère personnel collectées, à l'étendue de leur traitement, à leur durée de conservation et à leur accessibilité. En particulier, ces mesures garantissent que, par défaut, les données à caractère personnel ne sont pas rendues accessibles à un nombre indéterminé de personnes physiques sans l'intervention de la personne physique concernée. »
- [3] « Les données à caractère personnel doivent être: a) traitées de manière licite, loyale et transparente au regard de la personne concernée (licéité, loyauté, transparence); b) collectées pour des finalités déterminées, explicites et légitimes, et ne pas être traitées ultérieurement d'une manière incompatible avec ces finalités; le traitement ultérieur à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques n'est pas considéré, conformément à l'article 89, paragraphe 1, comme incompatible avec les finalités initiales (limitation des finalités); c) adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités pour lesquelles elles sont traitées (minimisation des données); d) exactes et, si nécessaire, tenues à jour; toutes les mesures raisonnables doivent être prises pour que les données à caractère personnel qui sont inexactes, eu égard aux finalités pour lesquelles elles sont traitées, soient effacées ou rectifiées sans tarder (exactitude); e) conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées; les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée (limitation de la conservation); f) traitées de façon à garantir une sécurité appropriée des données à caractère personnel, y compris la protection contre le traitement non autorisé ou illicite et contre la perte, la destruction ou les dégâts d'origine accidentelle, à l'aide de mesures techniques ou organisationnelles appropriées (intégrité et confidentialité); »
- [4] « Compte tenu de la nature, de la portée, du contexte et des finalités du traitement ainsi que des risques, dont le degré de probabilité et de gravité varie, pour les droits et libertés des personnes physiques, le responsable du traitement met en œuvre des mesures techniques et organisationnelles appropriées pour s'assurer et être en mesure de démontrer que le traitement est effectué conformément au présent règlement. Ces mesures sont réexaminées et actualisées si nécessaire. »

RÉPONSE :
Vous devez protéger les données personnelles que vous conservez en mettant en œuvre des mesures techniques et organisationnelles appropriées, conformément au RGPD, article 32, afin de garantir un niveau de sécurité adapté au risque, notamment par la pseudonymisation et le chiffrement des données, la garantie de la confidentialité, de l'intégrité, de la disponibilité et de la résilience des systèmes, la possibilité de rétablir rapidement l'accès aux données en cas d'incident, et une procédure régulière de test et d'évaluation de ces mesures [1]. Ces mesures doivent s'appliquer à la quantité, à l'étendue, à la durée de conservation et à l'accessibilité des données, en veillant à ce que seules les données nécessaires aux finalités spécifiques soient traitées [2]. Les données doivent être traitées de manière licite, loyale, transparente, adéquate, pertinente, limitée, exactes et conservées pendant une durée ne dépassant pas celle nécessaire aux finalités [3]. Le responsable du traitement doit s'assurer que le traitement est effectué conformément au règlement, en mettant en œuvre des politiques de protection des données et en réexaminant et actualisant ces mesures si nécessaire [4].
```

</details>

Temps : recherche 2.2 s · génération 60.6 s (3242 tokens lus, 1346 écrits, 32.7 tokens/s) · contrôle de pertinence 9.8 s

## q22 — Le consentement d'une personne doit-il être donné par écrit ?

Article attendu : RGPD art. 7 — passage [1].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 7 : Conditions applicables au consentement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_7
  [2] AI Act — règlement (UE) 2024/1689, article 61 : Consentement éclairé à participer aux essais en conditions réelles en dehors des bacs à sable réglementaires de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_61
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 11 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [4] AI Act — règlement (UE) 2024/1689, article 3, définition 59 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
  [5] RGPD — règlement (UE) 2016/679, article 8 : Conditions applicables au consentement des enfants en ce qui concerne les services de la société de l'information
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_8
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Si le consentement de la personne concernée est donné dans le cadre d'une déclaration écrite qui concerne également d'autres questions, la demande de consentement est présentée sous une forme qui la distingue clairement de ces autres questions, sous une forme compréhensible et aisément accessible, et formulée en des termes clairs et simples. »
- [2] « Le consentement éclairé est daté et documenté et une copie en est remise aux participants aux essais ou à leur représentant légal. »
- [4] « «consentement éclairé», l’expression libre, spécifique, univoque et volontaire, par un participant, de sa volonté de participer à un essai en conditions réelles particulier, après avoir été informé de tous les éléments de l’essai qui lui permettent de prendre sa décision concernant sa participation; »

RÉPONSE :
Non, le consentement n’est pas obligatoirement donné par écrit, car le RGPD (article 7, point 1) ne précise pas que le consentement doit être écrit, mais indique que le responsable du traitement doit démontrer que le consentement a été donné. Cependant, dans certains cas, comme le consentement éclairé pour les essais en conditions réelles (AI Act, article 61, point 1), le consentement est « daté et documenté » [2], et une copie est remise aux participants [2]. Le texte de l’AI Act (article 3, point 59) ne précise pas la forme du consentement, mais le définit comme une « expression libre, spécifique, univoque et volontaire », sans mention de forme écrite [4]. Ainsi, le consentement peut être donné par écrit ou par un acte positif clair, comme prévus dans le RGPD (article 4, point 11), mais il n’est pas obligatoirement écrit. Les conditions d’écriture sont donc spécifiques à certains contextes (ex. essais en conditions réelles), mais ne s’appliquent pas de manière générale.
```

</details>

Temps : recherche 2.1 s · génération 26.9 s (2578 tokens lus, 475 écrits, 35.3 tokens/s) · contrôle de pertinence 4.5 s

## q23 — Quelles utilisations de l'intelligence artificielle sont interdites en Europe ?

Article attendu : AI Act art. 5, paragraphe 1 — passage [1].

### Réponse du copilote

> Les utilisations de l’intelligence artificielle sont interdites en Europe dans les cas suivants : la mise en œuvre de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail ou dans les établissements d’enseignement, sauf pour des raisons médicales ou de sécurité [1]. L’utilisation de systèmes de catégorisation biométrique pour déduire la race, les opinions politiques, l’affiliation syndicale, les convictions religieuses ou philosophiques, la vie sexuelle ou l’orientation sexuelle d’une personne [1]. L’utilisation de systèmes d’identification biométrique à distance en temps réel dans des espaces publics à des fins répressives, sauf dans les cas précisément autorisés : la recherche de victimes d’enlèvement, de traite ou d’exploitation sexuelle, la recherche de personnes disparues, la prévention d’une menace imminente pour la vie ou la sécurité, ou la localisation d’une personne soupçonnée d’une infraction pénale pour des enquêtes ou poursuites [1]. L’utilisation de systèmes d’IA qui recourent à des techniques subliminales ou manipulatrices, visant à altérer le comportement d’une personne ou d’un groupe en compromettant sa capacité à prendre une décision éclairée [2]. L’utilisation de systèmes d’IA exploitant les vulnérabilités liées à l’âge, au handicap ou à la situation sociale ou économique pour altérer le comportement d’une personne ou d’un groupe [2]. La génération ou la manipulation d’images, vidéos ou contenus audio réalistes représentant les parties intimes d’une personne identifiable ou une personne se livrant à des activités sexuellement explicites, sans consentement libre, spécifique, éclairé, univoque et explicite [2]. L’évaluation ou la classification de personnes ou de groupes sur la base de leur comportement social ou de leurs traits de personnalité, conduisant à un traitement préjudiciable ou défavorable, notamment dans des contextes sociaux éloignés du contexte d’origine des données ou lorsqu’il est injustifié ou disproportionné par rapport à leur comportement [2]. Ces interdictions s’appliquent selon les principes du règlement (UE) 2024/1689, article 5, et sont visées dans l’ensemble des systèmes d’IA, sauf dans les cas spécifiques autorisés par le droit de l’Union ou national [1], [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement, sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité; »
  [1] « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes de catégorisation biométrique qui catégorisent individuellement les personnes physiques sur la base de leurs données biométriques afin d’arriver à des déductions ou des inférences concernant leur race, leurs opinions politiques, leur affiliation à une organisation syndicale, leurs convictions religieuses ou philosophiques, leur vie sexuelle ou leur orientation sexuelle; cette interdiction ne couvre pas l’étiquetage ou le filtrage d’ensembles de données biométriques acquis légalement, tels que des images, fondés sur des données biométriques ou la catégorisation de données biométriques dans le domaine répressif; »
  [1] « l’utilisation de systèmes d’identification biométrique à distance en temps réel dans des espaces accessibles au public à des fins répressives, sauf si et dans la mesure où cette utilisation est strictement nécessaire eu égard à l’un des objectifs suivants: i) la recherche ciblée de victimes spécifiques d’enlèvement, de la traite ou de l’exploitation sexuelle d’êtres humains, ainsi que la recherche de personnes disparues; ii) la prévention d’une menace spécifique, substantielle et imminente pour la vie ou la sécurité physique de personnes physiques ou d’une menace réelle et actuelle ou réelle et prévisible d’attaque terroriste; iii) la localisation ou l’identification d’une personne soupçonnée d’avoir commis une infraction pénale, aux fins de mener une enquête pénale, d’engager des poursuites ou d’exécuter une sanction pénale pour des infractions visées à l’annexe II et punissables dans l’État membre concerné d’une peine ou d’une mesure de sûreté privatives de liberté d’une durée maximale d’au moins quatre ans. »
  [2] « la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui a recours à des techniques subliminales, au-dessous du seuil de conscience d’une personne, ou à des techniques délibérément manipulatrices ou trompeuses, avec pour objectif ou effet d’altérer substantiellement le comportement d’une personne ou d’un groupe de personnes en portant considérablement atteinte à leur capacité à prendre une décision éclairée, amenant ainsi la personne à prendre une décision qu’elle n’aurait pas prise autrement, d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne, à une autre personne ou à un groupe de personnes; »
  [2] « la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui exploite les éventuelles vulnérabilités dues à l’âge, au handicap ou à la situation sociale ou économique spécifique d’une personne physique ou d’un groupe de personnes donné avec pour objectif ou effet d’altérer substantiellement le comportement de cette personne ou d’un membre de ce groupe d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne ou à un tiers; »
  [2] « la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui génère ou manipule des images, des vidéos, des contenus audio ou tout autre matériel similaire réalistes représentant les parties intimes d'une personne identifiable, ou une personne identifiable se livrant à des activités sexuellement explicites, sans le consentement libre, spécifique, éclairé, univoque et explicite de cette personne pour cette production ou manipulation; »
  [2] « la mise sur le marché, la mise en service ou l’utilisation de systèmes d’IA pour l’évaluation ou la classification de personnes physiques ou de groupes de personnes au cours d’une période donnée en fonction de leur comportement social ou de caractéristiques personnelles ou de personnalité connues, déduites ou prédites, la note sociale conduisant à l’une ou l’autre des situations suivantes, ou aux deux: i) le traitement préjudiciable ou défavorable de certaines personnes physiques ou de groupes de personnes dans des contextes sociaux dissociés du contexte dans lequel les données ont été générées ou collectées à l’origine; ii) le traitement préjudiciable ou défavorable de certaines personnes ou de groupes de personnes, qui est injustifié ou disproportionné par rapport à leur comportement social ou à la gravité de celui-ci; »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points f) à h) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [2] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points a) à e) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [4] AI Act — règlement (UE) 2024/1689, annexe III, point 6 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, article 1 : Objet
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_1
  [5] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 3 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
Attention : Extraits trop longs : le code a arrêté leur recopie après 1200 tokens pour garder au moins 800 tokens à la réponse (dernier extrait raccourci ou retiré ; le passage complet est dans les sources).
Attention : La réponse cite [4] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.
Attention : La réponse formule une exception qui ne reprend pas les extraits vérifiés : « sauf dans les cas précisément autorisés : la recherche de victimes d’enlèvement, de traite » (et 1 autre(s)). Vérifiez-la dans les textes.

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
- [2] « la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui génère ou manipule des images, des vidéos, des contenus audio ou tout autre matériel similaire réalistes représentant les parties intimes d'une personne identifiable, ou une personne identifiable se livrant à des activités sexuellement explicites, sans le consentement libre, spécifique, éclairé, univoque et explicite de cette personne pour cette production ou manipulation; »
- [2] « la mise sur le marché, la mise en service ou l’utilisation de systèmes d’IA pour l’évaluation ou la classification de personnes physiques ou de groupes de personnes au cours d’une période donnée en fonction de leur comportement social ou de caractéristiques personnelles ou de personnalité connues, déduites ou prédites, la note sociale conduisant à l’une ou l’autre des situations suivantes, ou aux deux: i) le traitement préjudiciable ou défavorable de certaines personnes physiques ou de groupes de personnes dans des contextes sociaux dissociés du contexte dans lequel les données ont été générées ou collectées à l’origine; ii) le traitement préjudiciable ou défavorable de certaines personnes ou de groupes de personnes, qui est injustifié ou disproportionné par rapport à leur comportement social ou à la gravité de celui-ci; »

RÉPONSE :
Les utilisations de l’intelligence artificielle sont interdites en Europe dans les cas suivants : la mise en œuvre de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail ou dans les établissements d’enseignement, sauf pour des raisons médicales ou de sécurité [1]. L’utilisation de systèmes de catégorisation biométrique pour déduire la race, les opinions politiques, l’affiliation syndicale, les convictions religieuses ou philosophiques, la vie sexuelle ou l’orientation sexuelle d’une personne [1]. L’utilisation de systèmes d’identification biométrique à distance en temps réel dans des espaces publics à des fins répressives, sauf dans les cas précisément autorisés : la recherche de victimes d’enlèvement, de traite ou d’exploitation sexuelle, la recherche de personnes disparues, la prévention d’une menace imminente pour la vie ou la sécurité, ou la localisation d’une personne soupçonnée d’une infraction pénale pour des enquêtes ou poursuites [1]. L’utilisation de systèmes d’IA qui recourent à des techniques subliminales ou manipulatrices, visant à altérer le comportement d’une personne ou d’un groupe en compromettant sa capacité à prendre une décision éclairée [2]. L’utilisation de systèmes d’IA exploitant les vulnérabilités liées à l’âge, au handicap ou à la situation sociale ou économique pour altérer le comportement d’une personne ou d’un groupe [2]. La génération ou la manipulation d’images, vidéos ou contenus audio réalistes représentant les parties intimes d’une personne identifiable ou une personne se livrant à des activités sexuellement explicites, sans consentement libre, spécifique, éclairé, univoque et explicite [2]. L’évaluation ou la classification de personnes ou de groupes sur la base de leur comportement social ou de leurs traits de personnalité, conduisant à un traitement préjudiciable ou défavorable, notamment dans des contextes sociaux éloignés du contexte d’origine des données ou lorsqu’il est injustifié ou disproportionné par rapport à leur comportement [2]. Ces interdictions s’appliquent selon les principes du règlement (UE) 2024/1689, article 5, et sont visées dans l’ensemble des systèmes d’IA, sauf dans les cas spécifiques autorisés par le droit de l’Union ou national [1], [4].
```

</details>

Temps : recherche 2.1 s · génération 99.1 s (5132 tokens lus, 1779 écrits, 30.7 tokens/s) · contrôle de pertinence 10.4 s

## q24 — Ai-je le droit d'utiliser une IA qui analyse les émotions de mes salariés ?

Article attendu : AI Act art. 5, paragraphe 1_f h — absent des passages donnés au modèle.

### Réponse du copilote

> Oui, vous avez le droit d’utiliser une IA qui analyse les émotions de vos salariés, à condition que cette utilisation ne soit pas liée à une enquête en matière pénale ou à la prévention d’infractions pénales, et que vous informiez les salariés du fonctionnement du système [1]. Cette obligation de transparence s’applique aux systèmes de reconnaissance des émotions, définis comme des systèmes d’IA permettant la reconnaissance ou la déduction des émotions ou des intentions de personnes physiques sur la base de leurs données biométriques [2]. Cependant, si l’usage vise des fins de détection ou de prévention d’infractions pénales, l’obligation de transparence ne s’applique pas, sous réserve de garanties appropriées pour les droits et libertés des salariés [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les déployeurs d’un système de reconnaissance des émotions ou d’un système de catégorisation biométrique informent les personnes physiques qui y sont exposées du fonctionnement du système et traitent les données à caractère personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680, selon le cas. Cette obligation ne s’applique pas aux systèmes d’IA utilisés pour la catégorisation biométrique et la reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l’Union. »
  [2] « «système de reconnaissance des émotions», un système d’IA permettant la reconnaissance ou la déduction des émotions ou des intentions de personnes physiques sur la base de leurs données biométriques; »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 3 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [2] AI Act — règlement (UE) 2024/1689, article 3, définition 39 : Définitions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [4] AI Act — règlement (UE) 2024/1689, article 86 : Droit à l’explication des décisions individuelles
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_86
  [5] AI Act — règlement (UE) 2024/1689, annexe III, point 5 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les déployeurs d’un système de reconnaissance des émotions ou d’un système de catégorisation biométrique informent les personnes physiques qui y sont exposées du fonctionnement du système et traitent les données à caractère personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680, selon le cas. Cette obligation ne s’applique pas aux systèmes d’IA utilisés pour la catégorisation biométrique et la reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l’Union. »
- [2] « «système de reconnaissance des émotions», un système d’IA permettant la reconnaissance ou la déduction des émotions ou des intentions de personnes physiques sur la base de leurs données biométriques; »

RÉPONSE :
Oui, vous avez le droit d’utiliser une IA qui analyse les émotions de vos salariés, à condition que cette utilisation ne soit pas liée à une enquête en matière pénale ou à la prévention d’infractions pénales, et que vous informiez les salariés du fonctionnement du système [1]. Cette obligation de transparence s’applique aux systèmes de reconnaissance des émotions, définis comme des systèmes d’IA permettant la reconnaissance ou la déduction des émotions ou des intentions de personnes physiques sur la base de leurs données biométriques [2]. Cependant, si l’usage vise des fins de détection ou de prévention d’infractions pénales, l’obligation de transparence ne s’applique pas, sous réserve de garanties appropriées pour les droits et libertés des salariés [1].
```

</details>

Temps : recherche 2.2 s · génération 26.7 s (2602 tokens lus, 457 écrits, 35.1 tokens/s) · contrôle de pertinence 5.3 s

## q25 — Mon logiciel est-il un « système d'IA » au sens de la loi européenne ?

Article attendu : AI Act art. 3, définition 1 — passage [2].

### Réponse du copilote

> Oui : votre logiciel est un « système d'IA » au sens de la loi européenne, si, pour des objectifs explicites ou implicites, il déduit à partir des entrées qu’il reçoit la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels [2].

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
Oui : votre logiciel est un « système d'IA » au sens de la loi européenne, si, pour des objectifs explicites ou implicites, il déduit à partir des entrées qu’il reçoit la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels [2].
```

</details>

Temps : recherche 2.1 s · génération 19.3 s (2595 tokens lus, 215 écrits, 35.7 tokens/s) · contrôle de pertinence 3.5 s

## q26 — Dois-je indiquer qu'une image publiée sur notre site a été créée par une IA ?

Article attendu : AI Act art. 50, paragraphe 4 — passage [1].

### Réponse du copilote

> Oui : vous devez indiquer qu’une image publiée sur votre site a été créée par une IA, sauf si l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière [1], ou si le contenu fait partie d’une œuvre manifestement artistique, créative, satirique, fictif ou analogue, dans ce cas la transparence se limite à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre [1]. De plus, cette obligation ne s’applique pas si le système d’IA ne modifie pas de manière substantielle les données d’entrée fournies par vous ou leur sémantique [3]. Cependant, ces exceptions ne s’appliquent pas automatiquement à toutes les images publiées : la situation doit être évaluée selon le contexte, la nature de l’image et les circonstances d’utilisation.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. Cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. Lorsque le contenu fait partie d’une œuvre ou d’un programme manifestement artistique, créatif, satirique, fictif ou analogue, les obligations de transparence énoncées au présent paragraphe se limitent à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 4 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [3] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 2 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [4] AI Act — règlement (UE) 2024/1689, article 3, définition 60 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
  [5] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1 ter : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([3]) : ignoré(s).
Attention : La réponse cite [3] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. Cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. Lorsque le contenu fait partie d’une œuvre ou d’un programme manifestement artistique, créatif, satirique, fictif ou analogue, les obligations de transparence énoncées au présent paragraphe se limitent à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre. »
- [3] « Les fournisseurs de systèmes d’IA, y compris de systèmes d’IA à usage général, qui génèrent des contenus de synthèse de type audio, image, vidéo ou texte, veillent à ce que les sorties des systèmes d’IA soient marquées dans un format lisible par machine et identifiables comme ayant été générées ou manipulées par une IA. Cette obligation ne s’applique pas dans la mesure où les systèmes d’IA remplissent une fonction d’assistance pour la mise en forme standard ou ne modifient pas de manière substantielle les données d’entrée fournies par le déployeur ou leur sémantique, ou lorsque leur utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. »

RÉPONSE :
Oui : vous devez indiquer qu’une image publiée sur votre site a été créée par une IA, sauf si l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière [1], ou si le contenu fait partie d’une œuvre manifestement artistique, créative, satirique, fictif ou analogue, dans ce cas la transparence se limite à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre [1]. De plus, cette obligation ne s’applique pas si le système d’IA ne modifie pas de manière substantielle les données d’entrée fournies par vous ou leur sémantique [3]. Cependant, ces exceptions ne s’appliquent pas automatiquement à toutes les images publiées : la situation doit être évaluée selon le contexte, la nature de l’image et les circonstances d’utilisation.
```

</details>

Temps : recherche 2.1 s · génération 30.6 s (2479 tokens lus, 649 écrits, 35.4 tokens/s) · contrôle de pertinence 4.1 s

## q27 — Quelles amendes prévoit le règlement européen sur l'intelligence artificielle ?

Article attendu : AI Act art. 99, paragraphe 4 ou AI Act art. 99, paragraphe 6 — absent des passages donnés au modèle.

### Réponse du copilote

> Le règlement européen sur l'intelligence artificielle prévoit plusieurs types d'amendes, selon les acteurs concernés. Pour les institutions, organes et organismes de l’Union, le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’une amende administrative pouvant aller jusqu’à 1 500 000 EUR, et la non-conformité avec d'autres exigences du règlement peut entraîner une amende allant jusqu’à 750 000 EUR [1]. Pour les entreprises, le non-respect de l’interdiction des pratiques en matière d’IA peut entraîner des amendes allant jusqu’à 35 000 000 EUR ou jusqu’à 7 % de leur chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu [2]. La fourniture d’informations inexactes, incomplètes ou trompeuses fait l’objet d’une amende pouvant aller jusqu’à 7 500 000 EUR ou jusqu’à 1 % de leur chiffre d’affaires annuel mondial total, le montant le plus élevé étant retenu [4]. Pour les fournisseurs de modèles d’IA à usage général, des amendes peuvent être infligées n’excédant pas 3 % de leur chiffre d’affaires annuel mondial total ou 15 000 000 EUR, le montant le plus élevé étant retenu, dans les cas précisés [5]. Ces amendes sont déterminées en fonction de la nature, de la gravité et de la durée de la violation, tout en tenant compte des principes de proportionnalité et d’adéquation [5].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le Contrôleur européen de la protection des données peut imposer des amendes administratives aux institutions, organes et organismes de l’Union relevant du champ d’application du présent règlement. … le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’une amende administrative pouvant aller jusqu’à 1 500 000 EUR. … la non-conformité du système d’IA avec les exigences ou obligations au titre du présent règlement, autres que celles énoncées à l’article 5, fait l’objet d’une amende administrative pouvant aller jusqu’à 750 000 EUR. »
  [2] « Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’amendes administratives pouvant aller jusqu’à 35 000 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 7 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu. »
  [4] « La fourniture d’informations inexactes, incomplètes ou trompeuses aux organismes notifiés ou aux autorités nationales compétentes en réponse à une demande fait l’objet d’une amende administrative pouvant aller jusqu’à 7 500 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 1 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu. »
  [5] « La Commission peut infliger aux fournisseurs de modèles d’IA à usage général des amendes n’excédant pas 3 % de leur chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, ou 15 000 000 EUR, le montant le plus élevé étant retenu, lorsque la Commission constate que le fournisseur, de manière délibérée ou par négligence: … a enfreint les dispositions pertinentes du présent règlement; … n’a pas donné suite à une demande de document ou d’informations au titre de l’article 91, ou a fourni des informations inexactes, incomplètes ou trompeuses; … ne s’est pas conformé à une mesure demandée au titre de l’article 93; … n’a pas donné à la Commission accès au modèle d’IA à usage général ou au modèle d’IA à usage général présentant un risque systémique en vue de procéder à une évaluation conformément à l’article 92. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 100 : Amendes administratives imposées aux institutions, organes et organismes de l’Union (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_100
  [2] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 3 : Sanctions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [4] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 5 : Sanctions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [5] AI Act — règlement (UE) 2024/1689, article 101 : Amendes applicables aux fournisseurs de modèles d’IA à usage général (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_101
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 1 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
Attention : La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Ces amendes sont déterminées en fonction de la nature, de la gravité et de la durée de la violation, tout en tenant … ». Vérifiez qui est concerné.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le Contrôleur européen de la protection des données peut imposer des amendes administratives aux institutions, organes et organismes de l’Union relevant du champ d’application du présent règlement. … le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’une amende administrative pouvant aller jusqu’à 1 500 000 EUR. … la non-conformité du système d’IA avec les exigences ou obligations au titre du présent règlement, autres que celles énoncées à l’article 5, fait l’objet d’une amende administrative pouvant aller jusqu’à 750 000 EUR. »
- [2] « Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’amendes administratives pouvant aller jusqu’à 35 000 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 7 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu. »
- [4] « La fourniture d’informations inexactes, incomplètes ou trompeuses aux organismes notifiés ou aux autorités nationales compétentes en réponse à une demande fait l’objet d’une amende administrative pouvant aller jusqu’à 7 500 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 1 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu. »
- [5] « La Commission peut infliger aux fournisseurs de modèles d’IA à usage général des amendes n’excédant pas 3 % de leur chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, ou 15 000 000 EUR, le montant le plus élevé étant retenu, lorsque la Commission constate que le fournisseur, de manière délibérée ou par négligence: … a enfreint les dispositions pertinentes du présent règlement; … n’a pas donné suite à une demande de document ou d’informations au titre de l’article 91, ou a fourni des informations inexactes, incomplètes ou trompeuses; … ne s’est pas conformé à une mesure demandée au titre de l’article 93; … n’a pas donné à la Commission accès au modèle d’IA à usage général ou au modèle d’IA à usage général présentant un risque systémique en vue de procéder à une évaluation conformément à l’article 92. »

RÉPONSE :
Le règlement européen sur l'intelligence artificielle prévoit plusieurs types d'amendes, selon les acteurs concernés. Pour les institutions, organes et organismes de l’Union, le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’une amende administrative pouvant aller jusqu’à 1 500 000 EUR, et la non-conformité avec d'autres exigences du règlement peut entraîner une amende allant jusqu’à 750 000 EUR [1]. Pour les entreprises, le non-respect de l’interdiction des pratiques en matière d’IA peut entraîner des amendes allant jusqu’à 35 000 000 EUR ou jusqu’à 7 % de leur chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu [2]. La fourniture d’informations inexactes, incomplètes ou trompeuses fait l’objet d’une amende pouvant aller jusqu’à 7 500 000 EUR ou jusqu’à 1 % de leur chiffre d’affaires annuel mondial total, le montant le plus élevé étant retenu [4]. Pour les fournisseurs de modèles d’IA à usage général, des amendes peuvent être infligées n’excédant pas 3 % de leur chiffre d’affaires annuel mondial total ou 15 000 000 EUR, le montant le plus élevé étant retenu, dans les cas précisés [5]. Ces amendes sont déterminées en fonction de la nature, de la gravité et de la durée de la violation, tout en tenant compte des principes de proportionnalité et d’adéquation [5].
```

</details>

Temps : recherche 2.2 s · génération 53.9 s (3423 tokens lus, 1074 écrits, 32.5 tokens/s) · contrôle de pertinence 7.1 s

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
RÉPONSE : Les textes trouvés ne traitent pas de la déclaration de création d'une association en préfecture. Ils concernent uniquement les organismes d'évaluation de la conformité, les autorités notifiantes, les procédures de notification et les obligations liées à l'IA ou au RGPD, et ne portent pas sur les formalités administratives de création d'association.
```

</details>

Temps : recherche 2.1 s · génération 30.8 s (4116 tokens lus, 97 écrits, 32.4 tokens/s)

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
  [2] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 1 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [3] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 5 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [4] AI Act — règlement (UE) 2024/1689, article 101 : Amendes applicables aux fournisseurs de modèles d’IA à usage général
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_101
  [5] AI Act — règlement (UE) 2024/1689, article 62 : Mesures en faveur des fournisseurs et déployeurs, en particulier les PME, y compris les jeunes pousses
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_62

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun  
RÉPONSE : Les textes trouvés ne traitent pas de ce point.
```

</details>

Temps : recherche 2.1 s · génération 20.9 s (3358 tokens lus, 26 écrits, 35.4 tokens/s)

## h05 — Comment rédiger les statuts d'une association ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [2] RGPD — règlement (UE) 2016/679, article 40, paragraphe 1 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 7 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [4] RGPD — règlement (UE) 2016/679, article 26 : Responsables conjoints du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_26
  [5] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun  
RÉPONSE : Les textes trouvés ne traitent pas de la rédaction des statuts d'une association. Ils évoquent des codes de conduite pour des associations ou des organismes, des registres de traitement, ou les rôles des responsables du traitement, mais ne prévoient aucune obligation ou indication spécifique concernant la rédaction des statuts.
```

</details>

Temps : recherche 2.1 s · génération 20.8 s (3110 tokens lus, 89 écrits, 34.9 tokens/s)
