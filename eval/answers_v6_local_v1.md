# Réponses du copilote — v6_local_v1

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 18/11/2026 à 16:15 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen3:4b-instruct` via Ollama 0.40.16 — température 0.1, contexte 8192 tokens, couches sur la carte graphique : toutes, 2000 tokens au plus par réponse
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu, reranker `BAAI/bge-reranker-v2-m3` sur CPU (20 candidats reclassés avant la limite par article), reformulation de la question par le modèle avant la recherche (termes juridiques ajoutés, sans conclusion)
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_v1.jsonl` (17 + 3 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q11 | Un client me demande d'effacer toutes ses données : suis-je obligé de le faire ? | 3/3 | non | La réponse change le sens d'une condition ou d'une exception (négation ou inversion ajoutée ou retirée, ou règle contraire à celle de l'extrait) : « lorsque l'un des motifs suivants s'applique : les données ne sont plus nécessaires ». Vérifiez ce point. | 87 s |
| q12 | Un salarié demande une copie de toutes les données que nous avons sur lui : que dois-je lui donner ? | 2/2 | non | — | 73 s |
| q13 | Un adhérent veut récupérer ses données pour les donner à une autre association : est-ce un droit ? | 1/1 | non | — | 64 s |
| q14 | Puis-je envoyer une lettre d'information par e-mail à mes adhérents, et peuvent-ils refuser ? | 4/4 | non | La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à condition que ce traitement soit fondé sur un consentement valable ou que les données ». Vérifiez-la dans les textes. | 76 s |
| q15 | Mon prestataire informatique a accès à nos fichiers : faut-il signer un contrat particulier ? | 4/5 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([4]) : ignoré(s).; La réponse cite [4] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations. | 71 s |
| q16 | Puis-je stocker les fichiers de mon association chez un hébergeur situé aux États-Unis ? | 5/5 | non | — | 92 s |
| q17 | Quelles sanctions risque une petite entreprise qui ne respecte pas le RGPD ? | 5/5 | non | — | 105 s |
| q18 | Notre association peut-elle collecter des informations sur la santé de ses bénévoles ? | 2/2 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 79 s |
| q19 | Qu'est-ce qu'une donnée personnelle ? | 1/1 | non | — | 66 s |
| q20 | À partir de quel âge un enfant peut-il s'inscrire seul à notre service en ligne ? | 1/1 | non | — | 66 s |
| q21 | Comment dois-je protéger les données personnelles que nous conservons ? | 4/6 | non | 2 extrait(s) introuvable(s) mot pour mot dans le passage cité ([3], [4]) : ignoré(s).; La réponse cite [3], [4] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations. | 106 s |
| q22 | Le consentement d'une personne doit-il être donné par écrit ? | 4/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 66 s |
| q23 | Quelles utilisations de l'intelligence artificielle sont interdites en Europe ? | 8/9 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([2]) : ignoré(s). | 138 s |
| q24 | Ai-je le droit d'utiliser une IA qui analyse les émotions de mes salariés ? | 4/4 | non | — | 75 s |
| q25 | Mon logiciel est-il un « système d'IA » au sens de la loi européenne ? | 1/1 | non | — | 58 s |
| q26 | Dois-je indiquer qu'une image publiée sur notre site a été créée par une IA ? | 1/2 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([3]) : ignoré(s).; La réponse cite [3] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.; La réponse formule une exception qui ne reprend pas les extraits vérifiés : « sauf dans les cas précisément prévus par la loi ou dans les cas d’œuvres ». Vérifiez-la dans les textes. | 76 s |
| q27 | Quelles amendes prévoit le règlement européen sur l'intelligence artificielle ? | 6/6 | non | — | 83 s |
| h03 | Comment déclarer la création d'une association en préfecture ? | 0/0 | oui | — | 40 s |
| h04 | Quel est le montant du SMIC cette année ? | 0/0 | oui | — | 34 s |
| h05 | Comment rédiger les statuts d'une association ? | 2/2 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 69 s |

## q11 — Un client me demande d'effacer toutes ses données : suis-je obligé de le faire ?

Article attendu : RGPD art. 17 — passage [1].

### Réponse du copilote

> Oui : vous êtes obligé d'effacer les données à caractère personnel du client dans les meilleurs délais, conformément à l'article 17 du RGPD, lorsque l'un des motifs suivants s'applique : les données ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées, le consentement a été retiré sans autre fondement juridique, la personne s'oppose au traitement sans motif légitime impérieux, les données ont fait l'objet d'un traitement illicite, ou elles doivent être effacées pour respecter une obligation légale [1]. Cependant, cette obligation ne s'applique pas si le traitement est nécessaire à l'exercice du droit à la liberté d'expression, à l'exécution d'une mission d'intérêt public, à des fins archivistiques, de recherche scientifique ou historique, ou à la constatation, l'exercice ou la défense de droits en justice [1]. Vous devez également informer les destinataires qui traitent ces données de l'effacement, à moins que cette communication ne soit impossible ou exige des efforts disproportionnés [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit d'obtenir du responsable du traitement l'effacement, dans les meilleurs délais, de données à caractère personnel la concernant et le responsable du traitement a l'obligation d'effacer ces données à caractère personnel dans les meilleurs délais, lorsque l'un des motifs suivants s'applique: … »
  [1] « Les paragraphes 1 et 2 ne s'appliquent pas dans la mesure où ce traitement est nécessaire: … »
  [4] « Le responsable du traitement notifie à chaque destinataire auquel les données à caractère personnel ont été communiquées toute rectification ou tout effacement de données à caractère personnel ou toute limitation du traitement effectué conformément à l'article 16, à l'article 17, paragraphe 1, et à l'article 18, à moins qu'une telle communication se révèle impossible ou exige des efforts disproportionnés. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 17 : Droit à l'effacement («droit à l'oubli») (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_17
  [4] RGPD — règlement (UE) 2016/679, article 19 : Obligation de notification en ce qui concerne la rectification ou l'effacement de données à caractère personnel ou la limitation du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_19
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [3] RGPD — règlement (UE) 2016/679, article 18 : Droit à la limitation du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_18
  [5] RGPD — règlement (UE) 2016/679, article 21 : Droit d'opposition
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_21
Attention : La réponse change le sens d'une condition ou d'une exception (négation ou inversion ajoutée ou retirée, ou règle contraire à celle de l'extrait) : « lorsque l'un des motifs suivants s'applique : les données ne sont plus nécessaires ». Vérifiez ce point.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « La personne concernée a le droit d'obtenir du responsable du traitement l'effacement, dans les meilleurs délais, de données à caractère personnel la concernant et le responsable du traitement a l'obligation d'effacer ces données à caractère personnel dans les meilleurs délais, lorsque l'un des motifs suivants s'applique: … »
- [1] « Les paragraphes 1 et 2 ne s'appliquent pas dans la mesure où ce traitement est nécessaire: … »
- [4] « Le responsable du traitement notifie à chaque destinataire auquel les données à caractère personnel ont été communiquées toute rectification ou tout effacement de données à caractère personnel ou toute limitation du traitement effectué conformément à l'article 16, à l'article 17, paragraphe 1, et à l'article 18, à moins qu'une telle communication se révèle impossible ou exige des efforts disproportionnés. »

RÉPONSE :  
Oui : vous êtes obligé d'effacer les données à caractère personnel du client dans les meilleurs délais, conformément à l'article 17 du RGPD, lorsque l'un des motifs suivants s'applique : les données ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées, le consentement a été retiré sans autre fondement juridique, la personne s'oppose au traitement sans motif légitime impérieux, les données ont fait l'objet d'un traitement illicite, ou elles doivent être effacées pour respecter une obligation légale [1]. Cependant, cette obligation ne s'applique pas si le traitement est nécessaire à l'exercice du droit à la liberté d'expression, à l'exécution d'une mission d'intérêt public, à des fins archivistiques, de recherche scientifique ou historique, ou à la constatation, l'exercice ou la défense de droits en justice [1]. Vous devez également informer les destinataires qui traitent ces données de l'effacement, à moins que cette communication ne soit impossible ou exige des efforts disproportionnés [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit d'accès aux données ; suppression des données ; droit à l'oubli ; traitement des données ; finalité du traitement ; données personnelles

Temps : recherche 38.5 s · génération 39.4 s (3803 tokens lus, 476 écrits, 32.5 tokens/s) · contrôle de pertinence 4.9 s · reformulation 4.0 s

## q12 — Un salarié demande une copie de toutes les données que nous avons sur lui : que dois-je lui donner ?

Article attendu : RGPD art. 15 — passage [1].

### Réponse du copilote

> Vous devez lui fournir une copie des données à caractère personnel qui vous concernent, comme prévus à l’article 15, paragraphe 1, du RGPD [1]. Cette copie inclut les données à caractère personnel ainsi que les informations suivantes : les finalités du traitement, les catégories de données concernées, les destinataires ou catégories de destinataires, la durée de conservation, les droits de rectification ou d’effacement, le droit de s’opposer au traitement, le droit de faire une réclamation auprès d’une autorité de contrôle, et, si applicable, les informations sur les prises de décision automatisées [1]. Vous pouvez exiger un paiement de frais raisonnables basés sur les coûts administratifs pour une copie supplémentaire [1]. Si la demande est faite par voie électronique, les informations doivent être fournies sous une forme électronique d’usage courant, à moins que la personne concernée ne demande autrement [1]. Ce droit ne porte pas atteinte aux droits et libertés d'autrui [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: … 3. Le responsable du traitement fournit une copie des données à caractère personnel faisant l'objet d'un traitement. Le responsable du traitement peut exiger le paiement de frais raisonnables basés sur les coûts administratifs pour toute copie supplémentaire demandée par la personne concernée. Lorsque la personne concernée présente sa demande par voie électronique, les informations sont fournies sous une forme électronique d'usage courant, à moins que la personne concernée ne demande qu'il en soit autrement. »
  [1] « Le droit d'obtenir une copie visé au paragraphe 3 ne porte pas atteinte aux droits et libertés d'autrui. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [3] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [4] RGPD — règlement (UE) 2016/679, article 4, définition 1 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: … 3. Le responsable du traitement fournit une copie des données à caractère personnel faisant l'objet d'un traitement. Le responsable du traitement peut exiger le paiement de frais raisonnables basés sur les coûts administratifs pour toute copie supplémentaire demandée par la personne concernée. Lorsque la personne concernée présente sa demande par voie électronique, les informations sont fournies sous une forme électronique d'usage courant, à moins que la personne concernée ne demande qu'il en soit autrement. »
- [1] « Le droit d'obtenir une copie visé au paragraphe 3 ne porte pas atteinte aux droits et libertés d'autrui. »

RÉPONSE :  
Vous devez lui fournir une copie des données à caractère personnel qui vous concernent, comme prévus à l’article 15, paragraphe 1, du RGPD [1]. Cette copie inclut les données à caractère personnel ainsi que les informations suivantes : les finalités du traitement, les catégories de données concernées, les destinataires ou catégories de destinataires, la durée de conservation, les droits de rectification ou d’effacement, le droit de s’opposer au traitement, le droit de faire une réclamation auprès d’une autorité de contrôle, et, si applicable, les informations sur les prises de décision automatisées [1]. Vous pouvez exiger un paiement de frais raisonnables basés sur les coûts administratifs pour une copie supplémentaire [1]. Si la demande est faite par voie électronique, les informations doivent être fournies sous une forme électronique d’usage courant, à moins que la personne concernée ne demande autrement [1]. Ce droit ne porte pas atteinte aux droits et libertés d'autrui [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données personnelles ; droit d'accès ; copie des données ; information détaillée

Temps : recherche 26.3 s · génération 39.7 s (3818 tokens lus, 477 écrits, 32.5 tokens/s) · contrôle de pertinence 4.2 s · reformulation 3.3 s

## q13 — Un adhérent veut récupérer ses données pour les donner à une autre association : est-ce un droit ?

Article attendu : RGPD art. 20 — passage [1].

### Réponse du copilote

> Oui : un adhérent a le droit de récupérer ses données à caractère personnel pour les transmettre à une autre association, à condition que le traitement soit fondé sur le consentement ou un contrat et que le traitement soit effectué à l'aide de procédés automatisés [1]. Ce droit s'applique sans que le responsable du traitement y fasse obstacle [1].

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
  [3] RGPD — règlement (UE) 2016/679, article 21 : Droit d'opposition
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_21
  [4] RGPD — règlement (UE) 2016/679, article 16 : Droit de rectification
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_16
  [5] RGPD — règlement (UE) 2016/679, article 80 : Représentation des personnes concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_80

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les personnes concernées ont le droit de recevoir les données à caractère personnel les concernant qu'elles ont fournies à un responsable du traitement, dans un format structuré, couramment utilisé et lisible par machine, et ont le droit de transmettre ces données à un autre responsable du traitement sans que le responsable du traitement auquel les données à caractère personnel ont été communiquées y fasse obstacle, lorsque: a) le traitement est fondé sur le consentement en application de l'article 6, paragraphe 1, point a), ou de l'article 9, paragraphe 2, point a), ou sur un contrat en application de l'article 6, paragraphe 1, point b); et b) le traitement est effectué à l'aide de procédés automatisés. »

RÉPONSE :  
Oui : un adhérent a le droit de récupérer ses données à caractère personnel pour les transmettre à une autre association, à condition que le traitement soit fondé sur le consentement ou un contrat et que le traitement soit effectué à l'aide de procédés automatisés [1]. Ce droit s'applique sans que le responsable du traitement y fasse obstacle [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit d'accès ; droit de rectification ; droit de portabilité ; droit d'opposition ; droit de suppression ; données personnelles

Temps : recherche 29.3 s · génération 27.8 s (3233 tokens lus, 275 écrits, 34.2 tokens/s) · contrôle de pertinence 3.8 s · reformulation 3.2 s

## q14 — Puis-je envoyer une lettre d'information par e-mail à mes adhérents, et peuvent-ils refuser ?

Article attendu : RGPD art. 21 ou RGPD art. 6, paragraphe 1 — passage [1].

### Réponse du copilote

> Oui, vous pouvez envoyer une lettre d'information par e-mail à vos adhérents, à condition que ce traitement soit fondé sur un consentement valable ou que les données soient traitées pour des fins de prospection. Les adhérents ont le droit de s'opposer à ce traitement, notamment s'il s'agit d'une prospection, comme le précise l'article 21, paragraphe 1, du RGPD [1]. Si un adhérent s'oppose à ce traitement, les données ne sont plus traitées à ces fins [1]. Ce droit d'opposition est explicitement porté à l'attention de la personne concernée au plus tard au moment de la première communication [1]. Cependant, si le traitement est fondé sur un consentement, il peut être retiré à tout moment [1]. Le retrait du consentement ne compromet pas la licéité des traitements antérieurs [1]. Aucun autre droit de limitation du traitement (article 18) n'est directement lié à une lettre d'information, mais il peut s'appliquer dans des cas spécifiques comme la contestation de l'exactitude des données [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit de s'opposer à tout moment, pour des raisons tenant à sa situation particulière, à un traitement des données à caractère personnel la concernant fondé sur l'article 6, paragraphe 1, point e) ou f), y compris un profilage fondé sur ces dispositions. »
  [1] « Lorsque les données à caractère personnel sont traitées à des fins de prospection, la personne concernée a le droit de s'opposer à tout moment au traitement des données à caractère personnel la concernant à de telles fins de prospection, y compris au profilage dans la mesure où il est lié à une telle prospection. »
  [1] « Lorsque la personne concernée s'oppose au traitement à des fins de prospection, les données à caractère personnel ne sont plus traitées à ces fins. »
  [4] « La personne concernée a le droit d'obtenir du responsable du traitement la limitation du traitement lorsque l'un des éléments suivants s'applique: … b) le traitement est illicite et la personne concernée s'oppose à leur effacement et exige à la place la limitation de leur utilisation; … »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 21 : Droit d'opposition (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_21
  [4] RGPD — règlement (UE) 2016/679, article 18 : Droit à la limitation du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_18
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [3] RGPD — règlement (UE) 2016/679, article 80 : Représentation des personnes concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_80
  [5] RGPD — règlement (UE) 2016/679, article 7 : Conditions applicables au consentement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_7
Attention : La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à condition que ce traitement soit fondé sur un consentement valable ou que les données ». Vérifiez-la dans les textes.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « La personne concernée a le droit de s'opposer à tout moment, pour des raisons tenant à sa situation particulière, à un traitement des données à caractère personnel la concernant fondé sur l'article 6, paragraphe 1, point e) ou f), y compris un profilage fondé sur ces dispositions. »  
- [1] « Lorsque les données à caractère personnel sont traitées à des fins de prospection, la personne concernée a le droit de s'opposer à tout moment au traitement des données à caractère personnel la concernant à de telles fins de prospection, y compris au profilage dans la mesure où il est lié à une telle prospection. »  
- [1] « Lorsque la personne concernée s'oppose au traitement à des fins de prospection, les données à caractère personnel ne sont plus traitées à ces fins. »  
- [4] « La personne concernée a le droit d'obtenir du responsable du traitement la limitation du traitement lorsque l'un des éléments suivants s'applique: … b) le traitement est illicite et la personne concernée s'oppose à leur effacement et exige à la place la limitation de leur utilisation; … »  

RÉPONSE :  
Oui, vous pouvez envoyer une lettre d'information par e-mail à vos adhérents, à condition que ce traitement soit fondé sur un consentement valable ou que les données soient traitées pour des fins de prospection. Les adhérents ont le droit de s'opposer à ce traitement, notamment s'il s'agit d'une prospection, comme le précise l'article 21, paragraphe 1, du RGPD [1]. Si un adhérent s'oppose à ce traitement, les données ne sont plus traitées à ces fins [1]. Ce droit d'opposition est explicitement porté à l'attention de la personne concernée au plus tard au moment de la première communication [1]. Cependant, si le traitement est fondé sur un consentement, il peut être retiré à tout moment [1]. Le retrait du consentement ne compromet pas la licéité des traitements antérieurs [1]. Aucun autre droit de limitation du traitement (article 18) n'est directement lié à une lettre d'information, mais il peut s'appliquer dans des cas spécifiques comme la contestation de l'exactitude des données [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données personnelles ; traitement des données ; consentement explicite ; droit d'opposition ; communication électronique ; droit à la rétraction

Temps : recherche 29.9 s · génération 38.3 s (3484 tokens lus, 549 écrits, 33.1 tokens/s) · contrôle de pertinence 4.6 s · reformulation 3.3 s

## q15 — Mon prestataire informatique a accès à nos fichiers : faut-il signer un contrat particulier ?

Article attendu : RGPD art. 28, paragraphe 3 — passage [1].

### Réponse du copilote

> Oui : il faut signer un contrat particulier ou un autre acte juridique, car le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique qui définit les obligations du sous-traitant, notamment en ce qui concerne le traitement des données à caractère personnel [1]. Ce contrat doit préciser l'objet, la durée, la finalité du traitement, le type de données et les catégories de personnes concernées, ainsi que les obligations du sous-traitant [1]. En outre, le responsable du traitement doit faire appel uniquement à des sous-traitants présentant des garanties suffisantes en matière de mesures techniques et organisationnelles [2]. Si le prestataire recrute un autre sous-traitant, les mêmes obligations sont imposées par contrat ou autre acte juridique [3]. Le fait que le prestataire ait accès à vos fichiers le rend un sous-traitant, selon la définition du règlement [4], et il est donc soumis aux obligations du RGPD [5].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre, qui lie le sous-traitant à l'égard du responsable du traitement, définit l'objet et la durée du traitement, la nature et la finalité du traitement, le type de données à caractère personnel et les catégories de personnes concernées, et les obligations et les droits du responsable du traitement. »
  [2] « Lorsqu'un traitement doit être effectué pour le compte d'un responsable du traitement, celui-ci fait uniquement appel à des sous-traitants qui présentent des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées de manière à ce que le traitement réponde aux exigences du présent règlement et garantisse la protection des droits de la personne concernée. »
  [3] « Lorsqu'un sous-traitant recrute un autre sous-traitant pour mener des activités de traitement spécifiques pour le compte du responsable du traitement, les mêmes obligations en matière de protection de données que celles fixées dans le contrat ou un autre acte juridique entre le responsable du traitement et le sous-traitant conformément au paragraphe 3, sont imposées à cet autre sous-traitant par contrat ou au moyen d'un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre… »
  [5] « Le sous-traitant et toute personne agissant sous l'autorité du responsable du traitement ou sous celle du sous-traitant, qui a accès à des données à caractère personnel, ne peut pas traiter ces données, excepté sur instruction du responsable du traitement, à moins d'y être obligé par le droit de l'Union ou le droit d'un État membre. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 28, paragraphe 3 : Sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [2] RGPD — règlement (UE) 2016/679, article 28, paragraphe 1 : Sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [3] RGPD — règlement (UE) 2016/679, article 28, paragraphe 4 : Sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [4] RGPD — règlement (UE) 2016/679, article 4, définition 8 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [5] RGPD — règlement (UE) 2016/679, article 29 : Traitement effectué sous l'autorité du responsable du traitement ou du sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_29
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([4]) : ignoré(s).
Attention : La réponse cite [4] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre, qui lie le sous-traitant à l'égard du responsable du traitement, définit l'objet et la durée du traitement, la nature et la finalité du traitement, le type de données à caractère personnel et les catégories de personnes concernées, et les obligations et les droits du responsable du traitement. »
- [2] « Lorsqu'un traitement doit être effectué pour le compte d'un responsable du traitement, celui-ci fait uniquement appel à des sous-traitants qui présentent des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées de manière à ce que le traitement réponde aux exigences du présent règlement et garantisse la protection des droits de la personne concernée. »
- [3] « Lorsqu'un sous-traitant recrute un autre sous-traitant pour mener des activités de traitement spécifiques pour le compte du responsable du traitement, les mêmes obligations en matière de protection de données que celles fixées dans le contrat ou un autre acte juridique entre le responsable du traitement et le sous-traitant conformément au paragraphe 3, sont imposées à cet autre sous-traitant par contrat ou au moyen d'un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre… »
- [4] « on entend par: «sous-traitant», la personne physique ou morale, l'autorité publique, le service ou un autre organisme qui traite des données à caractère personnel pour le compte du responsable du traitement; »
- [5] « Le sous-traitant et toute personne agissant sous l'autorité du responsable du traitement ou sous celle du sous-traitant, qui a accès à des données à caractère personnel, ne peut pas traiter ces données, excepté sur instruction du responsable du traitement, à moins d'y être obligé par le droit de l'Union ou le droit d'un État membre. »

RÉPONSE :  
Oui : il faut signer un contrat particulier ou un autre acte juridique, car le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique qui définit les obligations du sous-traitant, notamment en ce qui concerne le traitement des données à caractère personnel [1]. Ce contrat doit préciser l'objet, la durée, la finalité du traitement, le type de données et les catégories de personnes concernées, ainsi que les obligations du sous-traitant [1]. En outre, le responsable du traitement doit faire appel uniquement à des sous-traitants présentant des garanties suffisantes en matière de mesures techniques et organisationnelles [2]. Si le prestataire recrute un autre sous-traitant, les mêmes obligations sont imposées par contrat ou autre acte juridique [3]. Le fait que le prestataire ait accès à vos fichiers le rend un sous-traitant, selon la définition du règlement [4], et il est donc soumis aux obligations du RGPD [5].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données personnelles ; traitement de données ; finalité du traitement ; responsabilité du prestataire ; obligation de confidentialité ; contrat de prestations

Temps : recherche 28.4 s · génération 34.3 s (2587 tokens lus, 721 écrits, 35.0 tokens/s) · contrôle de pertinence 5.5 s · reformulation 3.3 s

## q16 — Puis-je stocker les fichiers de mon association chez un hébergeur situé aux États-Unis ?

Article attendu : RGPD art. 44 ou RGPD art. 45, paragraphe 1 ou RGPD art. 46 — passage [1].

### Réponse du copilote

> Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, mais uniquement si l'un des critères suivants est rempli : soit la Commission européenne a établi une décision d'adéquation pour les États-Unis (selon l'article 45, [5]), soit vous avez mis en place des garanties appropriées (selon l'article 46, [1]), notamment par un mécanisme de certification approuvé, des clauses types de protection des données approuvées par la Commission, ou des règles d'entreprise contraignantes (selon les points a) à f) de l'article 46, [1]). Dans ce cas, les personnes concernées doivent disposer de droits opposables et de voies de droit effectives (article 46, [1]). Si aucun de ces dispositifs n’est en place, le transfert ne peut avoir lieu qu’à l’une des conditions spécifiques prévues à l’article 49, paragraphe 1, [2], par exemple si le transfert est nécessaire à l’exécution d’un contrat ou à la défense de droits en justice. En outre, lorsque les données sont transférées vers les États-Unis, la personne concernée a le droit d’être informée des garanties appropriées (article 15, [4]). La liste des pays ou territoires reconnus comme assurant un niveau de protection adéquat est publiée par la Commission européenne.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
  [2] « En l'absence de décision d'adéquation en vertu de l'article 45, paragraphe 3, ou de garanties appropriées en vertu de l'article 46, y compris des règles d'entreprise contraignantes, un transfert ou un ensemble de transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale ne peut avoir lieu qu'à l'une des conditions suivantes: … »
  [3] « Lorsqu'elle évalue le caractère adéquat du niveau de protection, la Commission tient compte, en particulier, des éléments suivants: … »
  [4] « Lorsque les données à caractère personnel sont transférées vers un pays tiers ou à une organisation internationale, la personne concernée a le droit d'être informée des garanties appropriées, en vertu de l'article 46, en ce qui concerne ce transfert. »
  [5] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. Un tel transfert ne nécessite pas d'autorisation spécifique. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 46 : Transferts moyennant des garanties appropriées (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_46
  [2] RGPD — règlement (UE) 2016/679, article 49, paragraphe 1 : Dérogations pour des situations particulières (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_49
  [3] RGPD — règlement (UE) 2016/679, article 45, paragraphe 2 : Transferts fondés sur une décision d'adéquation (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
  [4] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [5] RGPD — règlement (UE) 2016/679, article 45, paragraphe 1 : Transferts fondés sur une décision d'adéquation (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
Note : La liste des pays bénéficiant d'une décision d'adéquation n'est pas dans les textes utilisés par le copilote : consultez la page de la Commission européenne sur les décisions d'adéquation (en anglais) : https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
- [2] « En l'absence de décision d'adéquation en vertu de l'article 45, paragraphe 3, ou de garanties appropriées en vertu de l'article 46, y compris des règles d'entreprise contraignantes, un transfert ou un ensemble de transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale ne peut avoir lieu qu'à l'une des conditions suivantes: … »
- [3] « Lorsqu'elle évalue le caractère adéquat du niveau de protection, la Commission tient compte, en particulier, des éléments suivants: … »
- [4] « Lorsque les données à caractère personnel sont transférées vers un pays tiers ou à une organisation internationale, la personne concernée a le droit d'être informée des garanties appropriées, en vertu de l'article 46, en ce qui concerne ce transfert. »
- [5] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. Un tel transfert ne nécessite pas d'autorisation spécifique. »

RÉPONSE :
Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, mais uniquement si l'un des critères suivants est rempli : soit la Commission européenne a établi une décision d'adéquation pour les États-Unis (selon l'article 45, [5]), soit vous avez mis en place des garanties appropriées (selon l'article 46, [1]), notamment par un mécanisme de certification approuvé, des clauses types de protection des données approuvées par la Commission, ou des règles d'entreprise contraignantes (selon les points a) à f) de l'article 46, [1]). Dans ce cas, les personnes concernées doivent disposer de droits opposables et de voies de droit effectives (article 46, [1]). Si aucun de ces dispositifs n’est en place, le transfert ne peut avoir lieu qu’à l’une des conditions spécifiques prévues à l’article 49, paragraphe 1, [2], par exemple si le transfert est nécessaire à l’exécution d’un contrat ou à la défense de droits en justice. En outre, lorsque les données sont transférées vers les États-Unis, la personne concernée a le droit d’être informée des garanties appropriées (article 15, [4]). La liste des pays ou territoires reconnus comme assurant un niveau de protection adéquat est publiée par la Commission européenne.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données personnelles ; traitement des données ; transfert de données ; hébergement ; finalité du traitement ; conformité avec le règlement

Temps : recherche 31.2 s · génération 50.7 s (4080 tokens lus, 744 écrits, 31.5 tokens/s) · contrôle de pertinence 6.5 s · reformulation 3.3 s

## q17 — Quelles sanctions risque une petite entreprise qui ne respecte pas le RGPD ?

Article attendu : RGPD art. 83, paragraphe 4 ou RGPD art. 83, paragraphe 5 — passage [1].

### Réponse du copilote

> Une petite entreprise qui ne respecte pas le RGPD peut être soumise à des sanctions administratives, notamment des amendes, selon les dispositions du RGPD, article 83. Si la violation concerne les principes de base du traitement, les droits des personnes concernées, les transferts de données à un pays tiers ou les obligations des États membres, l'amende peut s'élever jusqu'à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [1]. Si la violation concerne les obligations du responsable du traitement ou du sous-traitant (articles 8, 11, 25 à 39, 42 et 43), l'amende peut s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [3]. En outre, l'autorité de contrôle peut prendre des mesures correctrices, comme l'avertissement, le rappel à l'ordre, l'ordre de mise en conformité, la communication d'une violation, la limitation ou suspension du traitement, la rectification ou effacement des données, ou la suspension des flux de données [5]. Ces mesures sont effectives, proportionnées et dissuasives [4]. Les sanctions sont déterminées par les États membres, qui doivent les notifier à la Commission [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: … »
  [1] « … y compris les conditions applicables au consentement en vertu des articles 5, 6, 7 et 9; … les droits dont bénéficient les personnes concernées en vertu des articles 12 à 22 … les transferts de données à caractère personnel à un destinataire situé dans un pays tiers ou à une organisation internationale en vertu des articles 44 à 49; … toutes les obligations découlant du droit des États membres adoptées en vertu du chapitre IX; … le non-respect d'une injonction, d'une limitation temporaire ou définitive du traitement ou de la suspension des flux de données ordonnée par l'autorité de contrôle en vertu de l'article 58, paragraphe 2, ou le fait de ne pas accorder l'accès prévu, en violation de l'article 58, paragraphe 1. »
  [3] « les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: … les obligations incombant au responsable du traitement et au sous-traitant en vertu des articles 8, 11, 25 à 39, 42 et 43; … les obligations incombant à l'organisme de certification en vertu des articles 42 et 43; … les obligations incombant à l'organisme chargé du suivi des codes de conduite en vertu de l'article 41, paragraphe 4. »
  [5] « chaque autorité de contrôle dispose du pouvoir d'adopter toutes les mesures correctrices suivantes: … a) avertir un responsable du traitement ou un sous-traitant du fait que les opérations de traitement envisagées sont susceptibles de violer les dispositions du présent règlement; … b) rappeler à l'ordre un responsable du traitement ou un sous-traitant lorsque les opérations de traitement ont entraîné une violation des dispositions du présent règlement; … c) ordonner au responsable du traitement ou au sous-traitant de satisfaire aux demandes présentées par la personne concernée en vue d'exercer ses droits en application du présent règlement; … d) ordonner au responsable du traitement ou au sous-traitant de mettre les opérations de traitement en conformité avec les dispositions du présent règlement, le cas échéant, de manière spécifique et dans un délai déterminé; … e) ordonner au responsable du traitement de communiquer à la personne concernée une violation de données à caractère personnel; … f) imposer une limitation temporaire ou définitive, y compris une interdiction, du traitement; … g) ordonner la rectification ou l'effacement de données à caractère personnel ou la limitation du traitement en application des articles 16, 17 et 18 et la notification de ces mesures aux destinataires auxquels les données à caractère personnel ont été divulguées en application de l'article 17, paragraphe 2, et de l'article 19; … h) retirer une certification ou ordonner à l'organisme de certification de retirer une certification délivrée en application des articles 42 et 43, ou ordonner à l'organisme de certification de ne pas délivrer de certification si les exigences applicables à la certification ne sont pas ou plus satisfaites; … i) imposer une amende administrative en application de l'article 83, en complément ou à la place des mesures visées au présent paragraphe, en fonction des caractéristiques propres à chaque cas; … j) ordonner la suspension des flux de données adressés à un destinataire situé dans un pays tiers ou à une organisation internationale. »
  [4] « Les États membres déterminent le régime des autres sanctions applicables en cas de violations du présent règlement, en particulier pour les violations qui ne font pas l'objet des amendes administratives prévues à l'article 83, et prennent toutes les mesures nécessaires pour garantir leur mise en œuvre. Ces sanctions sont effectives, proportionnées et dissuasives. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 83, paragraphe 5 : Conditions générales pour imposer des amendes administratives (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83
  [3] RGPD — règlement (UE) 2016/679, article 83, paragraphe 4 : Conditions générales pour imposer des amendes administratives (version du 2016-05-04)
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
- [1] « les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: … »
- [1] « … y compris les conditions applicables au consentement en vertu des articles 5, 6, 7 et 9; … les droits dont bénéficient les personnes concernées en vertu des articles 12 à 22 … les transferts de données à caractère personnel à un destinataire situé dans un pays tiers ou à une organisation internationale en vertu des articles 44 à 49; … toutes les obligations découlant du droit des États membres adoptées en vertu du chapitre IX; … le non-respect d'une injonction, d'une limitation temporaire ou définitive du traitement ou de la suspension des flux de données ordonnée par l'autorité de contrôle en vertu de l'article 58, paragraphe 2, ou le fait de ne pas accorder l'accès prévu, en violation de l'article 58, paragraphe 1. »
- [3] « les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: … les obligations incombant au responsable du traitement et au sous-traitant en vertu des articles 8, 11, 25 à 39, 42 et 43; … les obligations incombant à l'organisme de certification en vertu des articles 42 et 43; … les obligations incombant à l'organisme chargé du suivi des codes de conduite en vertu de l'article 41, paragraphe 4. »
- [5] « chaque autorité de contrôle dispose du pouvoir d'adopter toutes les mesures correctrices suivantes: … a) avertir un responsable du traitement ou un sous-traitant du fait que les opérations de traitement envisagées sont susceptibles de violer les dispositions du présent règlement; … b) rappeler à l'ordre un responsable du traitement ou un sous-traitant lorsque les opérations de traitement ont entraîné une violation des dispositions du présent règlement; … c) ordonner au responsable du traitement ou au sous-traitant de satisfaire aux demandes présentées par la personne concernée en vue d'exercer ses droits en application du présent règlement; … d) ordonner au responsable du traitement ou au sous-traitant de mettre les opérations de traitement en conformité avec les dispositions du présent règlement, le cas échéant, de manière spécifique et dans un délai déterminé; … e) ordonner au responsable du traitement de communiquer à la personne concernée une violation de données à caractère personnel; … f) imposer une limitation temporaire ou définitive, y compris une interdiction, du traitement; … g) ordonner la rectification ou l'effacement de données à caractère personnel ou la limitation du traitement en application des articles 16, 17 et 18 et la notification de ces mesures aux destinataires auxquels les données à caractère personnel ont été divulguées en application de l'article 17, paragraphe 2, et de l'article 19; … h) retirer une certification ou ordonner à l'organisme de certification de retirer une certification délivrée en application des articles 42 et 43, ou ordonner à l'organisme de certification de ne pas délivrer de certification si les exigences applicables à la certification ne sont pas ou plus satisfaites; … i) imposer une amende administrative en application de l'article 83, en complément ou à la place des mesures visées au présent paragraphe, en fonction des caractéristiques propres à chaque cas; … j) ordonner la suspension des flux de données adressés à un destinataire situé dans un pays tiers ou à une organisation internationale. »
- [4] « Les États membres déterminent le régime des autres sanctions applicables en cas de violations du présent règlement, en particulier pour les violations qui ne font pas l'objet des amendes administratives prévues à l'article 83, et prennent toutes les mesures nécessaires pour garantir leur mise en œuvre. Ces sanctions sont effectives, proportionnées et dissuasives. »

RÉPONSE :
Une petite entreprise qui ne respecte pas le RGPD peut être soumise à des sanctions administratives, notamment des amendes, selon les dispositions du RGPD, article 83. Si la violation concerne les principes de base du traitement, les droits des personnes concernées, les transferts de données à un pays tiers ou les obligations des États membres, l'amende peut s'élever jusqu'à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [1]. Si la violation concerne les obligations du responsable du traitement ou du sous-traitant (articles 8, 11, 25 à 39, 42 et 43), l'amende peut s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [3]. En outre, l'autorité de contrôle peut prendre des mesures correctrices, comme l'avertissement, le rappel à l'ordre, l'ordre de mise en conformité, la communication d'une violation, la limitation ou suspension du traitement, la rectification ou effacement des données, ou la suspension des flux de données [5]. Ces mesures sont effectives, proportionnées et dissuasives [4]. Les sanctions sont déterminées par les États membres, qui doivent les notifier à la Commission [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : sanctions financières ; responsabilité civile ; pénalités administratives ; amendes ; contrôles renforcés ; obligations de correction

Temps : recherche 32.9 s · génération 57.9 s (2643 tokens lus, 1484 écrits, 33.6 tokens/s) · contrôle de pertinence 11.1 s · reformulation 3.3 s

## q18 — Notre association peut-elle collecter des informations sur la santé de ses bénévoles ?

Article attendu : RGPD art. 9, paragraphe 1 ou RGPD art. 9, paragraphe 2 — passage [1].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 9, paragraphe 2, points a) à i) : Traitement portant sur des catégories particulières de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
  [2] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [3] RGPD — règlement (UE) 2016/679, article 40, paragraphe 1 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [4] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [5] RGPD — règlement (UE) 2016/679, article 6, paragraphe 4 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « le traitement est nécessaire aux fins de la médecine préventive ou de la médecine du travail, de l'appréciation de la capacité de travail du travailleur, de diagnostics médicaux, de la prise en charge sanitaire ou sociale, ou de la gestion des systèmes et des services de soins de santé ou de protection sociale sur la base du droit de l'Union, du droit d'un État membre ou en vertu d'un contrat conclu avec un professionnel de la santé et soumis aux conditions et garanties visées au paragraphe 3; »
- [1] « le traitement est nécessaire pour des motifs d'intérêt public dans le domaine de la santé publique, tels que la protection contre les menaces transfrontalières graves pesant sur la santé, ou aux fins de garantir des normes élevées de qualité et de sécurité des soins de santé et des médicaments ou des dispositifs médicaux, sur la base du droit de l'Union ou du droit de l'État membre qui prévoit des mesures appropriées et spécifiques pour la sauvegarde des droits et libertés de la personne concernée, notamment le secret professionnel; »

RÉPONSE :
Oui : votre association peut collecter des informations sur la santé de ses bénévoles, car ce traitement est considéré comme nécessaire aux fins de la médecine préventive ou de la médecine du travail, de l'appréciation de la capacité de travail du travailleur, de diagnostics médicaux, de la prise en charge sanitaire ou sociale, ou de la gestion des systèmes et des services de soins de santé ou de protection sociale, selon l'article 9, point h) du RGPD [1]. Ce traitement est autorisé dans la mesure où il est fondé sur le droit de l'Union, du droit d'un État membre ou en vertu d'un contrat conclu avec un professionnel de la santé, et sous réserve de garanties appropriées [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données de santé ; données personnelles ; traitement de données ; finalité du traitement ; consentement ; données sensibles

Temps : recherche 30.9 s · génération 39.9 s (3959 tokens lus, 438 écrits, 31.7 tokens/s) · contrôle de pertinence 5.4 s · reformulation 3.1 s

## q19 — Qu'est-ce qu'une donnée personnelle ?

Article attendu : RGPD art. 4, définition 1 — passage [1].

### Réponse du copilote

> Une donnée personnelle est toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée») ; elle est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « «données à caractère personnel», toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée»); est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 4, définition 1 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 4, définition 14 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [3] AI Act — règlement (UE) 2024/1689, article 3, définition 34 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
  [4] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [5] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « «données à caractère personnel», toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée»); est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale; »

RÉPONSE :
Une donnée personnelle est toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée») ; elle est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données personnelles ; information identifiant une personne ; données à caractère personnel ; données relatives à une personne ; données individuelles ; données spécifiques à une personne

Temps : recherche 32.7 s · génération 26.5 s (3147 tokens lus, 280 écrits, 34.0 tokens/s) · contrôle de pertinence 3.5 s · reformulation 3.2 s

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
  [2] AI Act — règlement (UE) 2024/1689, article 3, définition 59 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
  [3] RGPD — règlement (UE) 2016/679, article 7 : Conditions applicables au consentement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_7
  [4] RGPD — règlement (UE) 2016/679, article 57, paragraphe 1, points a) à t) : Missions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_57
  [5] AI Act — règlement (UE) 2024/1689, article 61 : Consentement éclairé à participer aux essais en conditions réelles en dehors des bacs à sable réglementaires de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_61

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

Reformulation de la question (termes ajoutés avant la recherche) : âge de consentement ; capacité juridique ; autonomie personnelle ; consentement éclairé ; responsabilité civile

Temps : recherche 31.4 s · génération 28.0 s (3491 tokens lus, 218 écrits, 33.3 tokens/s) · contrôle de pertinence 3.7 s · reformulation 3.2 s

## q21 — Comment dois-je protéger les données personnelles que nous conservons ?

Article attendu : RGPD art. 32 — passage [2].

### Réponse du copilote

> Vous devez protéger les données personnelles que vous conservez en mettant en œuvre des mesures techniques et organisationnelles appropriées, telles que la pseudonymisation et le chiffrement des données [2], afin de garantir que seules les données nécessaires au regard des finalités spécifiques soient traitées [1]. Ces mesures doivent s'appliquer à la quantité, à l'étendue, à la durée de conservation et à l'accessibilité des données [1]. La sécurité des données doit être assurée par des moyens garantissant la confidentialité, l'intégrité, la disponibilité et la résilience des systèmes et services de traitement [2]. Vous devez également garantir que les données ne soient pas accessibles à un nombre indéterminé de personnes sans l'intervention de la personne concernée [1]. La conservation des données doit être limitée à la durée nécessaire aux finalités initiales [3], sauf pour des usages archivistiques, scientifiques ou statistiques, dans la mesure où des mesures techniques et organisationnelles appropriées sont mises en œuvre [3]. En cas d'incident, des moyens doivent permettre de rétablir la disponibilité des données et l'accès à celles-ci dans des délais appropriés [2]. Une procédure régulière de test, d'analyse et d'évaluation de l'efficacité des mesures doit être mise en place [2]. De plus, toute personne ayant accès aux données ne doit pas les traiter sans instruction du responsable du traitement, sauf obligation légale [2]. La protection des données doit inclure des garanties appropriées, telles que le chiffrement ou la pseudonymisation [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le responsable du traitement met en œuvre les mesures techniques et organisationnelles appropriées pour garantir que, par défaut, seules les données à caractère personnel qui sont nécessaires au regard de chaque finalité spécifique du traitement sont traitées. Cela s'applique à la quantité de données à caractère personnel collectées, à l'étendue de leur traitement, à leur durée de conservation et à leur accessibilité. En particulier, ces mesures garantissent que, par défaut, les données à caractère personnel ne sont pas rendues accessibles à un nombre indéterminé de personnes physiques sans l'intervention de la personne physique concernée. »
  [1] « Un mécanisme de certification approuvé en vertu de l'article 42 peut servir d'élément pour démontrer le respect des exigences énoncées aux paragraphes 1 et 2 du présent article. »
  [2] « Compte tenu de l'état des connaissances, des coûts de mise en œuvre et de la nature, de la portée, du contexte et des finalités du traitement ainsi que des risques, dont le degré de probabilité et de gravité varie, pour les droits et libertés des personnes physiques, le responsable du traitement et le sous-traitant mettent en œuvre les mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque, y compris entre autres, selon les besoins: a) la pseudonymisation et le chiffrement des données à caractère personnel; b) des moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement; c) des moyens permettant de rétablir la disponibilité des données à caractère personnel et l'accès à celles-ci dans des délais appropriés en cas d'incident physique ou technique; d) une procédure visant à tester, à analyser et à évaluer régulièrement l'efficacité des mesures techniques et organisationnelles pour assurer la sécurité du traitement. »
  [2] « Le responsable du traitement et le sous-traitant prennent des mesures afin de garantir que toute personne physique agissant sous l'autorité du responsable du traitement ou sous celle du sous-traitant, qui a accès à des données à caractère personnel, ne les traite pas, excepté sur instruction du responsable du traitement, à moins d'y être obligée par le droit de l'Union ou le droit d'un État membre. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 25 : Protection des données dès la conception et protection des données par défaut (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_25
  [2] RGPD — règlement (UE) 2016/679, article 32 : Sécurité du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_32
  [3] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
  [4] RGPD — règlement (UE) 2016/679, article 6, paragraphe 4 : Licéité du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
Passages consultés mais non cités :
  [5] RGPD — règlement (UE) 2016/679, article 6, paragraphe 1 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
Attention : 2 extrait(s) introuvable(s) mot pour mot dans le passage cité ([3], [4]) : ignoré(s).
Attention : La réponse cite [3], [4] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le responsable du traitement met en œuvre les mesures techniques et organisationnelles appropriées pour garantir que, par défaut, seules les données à caractère personnel qui sont nécessaires au regard de chaque finalité spécifique du traitement sont traitées. Cela s'applique à la quantité de données à caractère personnel collectées, à l'étendue de leur traitement, à leur durée de conservation et à leur accessibilité. En particulier, ces mesures garantissent que, par défaut, les données à caractère personnel ne sont pas rendues accessibles à un nombre indéterminé de personnes physiques sans l'intervention de la personne physique concernée. »
- [1] « Un mécanisme de certification approuvé en vertu de l'article 42 peut servir d'élément pour démontrer le respect des exigences énoncées aux paragraphes 1 et 2 du présent article. »
- [2] « Compte tenu de l'état des connaissances, des coûts de mise en œuvre et de la nature, de la portée, du contexte et des finalités du traitement ainsi que des risques, dont le degré de probabilité et de gravité varie, pour les droits et libertés des personnes physiques, le responsable du traitement et le sous-traitant mettent en œuvre les mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque, y compris entre autres, selon les besoins: a) la pseudonymisation et le chiffrement des données à caractère personnel; b) des moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement; c) des moyens permettant de rétablir la disponibilité des données à caractère personnel et l'accès à celles-ci dans des délais appropriés en cas d'incident physique ou technique; d) une procédure visant à tester, à analyser et à évaluer régulièrement l'efficacité des mesures techniques et organisationnelles pour assurer la sécurité du traitement. »
- [2] « Le responsable du traitement et le sous-traitant prennent des mesures afin de garantir que toute personne physique agissant sous l'autorité du responsable du traitement ou sous celle du sous-traitant, qui a accès à des données à caractère personnel, ne les traite pas, excepté sur instruction du responsable du traitement, à moins d'y être obligée par le droit de l'Union ou le droit d'un État membre. »
- [3] « Les données à caractère personnel doivent être: c) adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités pour lesquelles elles sont traitées (minimisation des données); e) conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées; les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée (limitation de la conservation); f) traitées de façon à garantir une sécurité appropriée des données à caractère personnel, y compris la protection contre le traitement non autorisé ou illicite et contre la perte, la destruction ou les dégâts d'origine accidentelle, à l'aide de mesures techniques ou organisationnelles appropriées (intégrité et confidentialité). »
- [4] « Lorsque le traitement à une fin autre que celle pour laquelle les données ont été collectées n'est pas fondé sur le consentement de la personne concernée ou sur le droit de l'Union ou le droit d'un État membre qui constitue une mesure nécessaire et proportionnée dans une société démocratique pour garantir les objectifs visés à l'article 23, paragraphe 1, le responsable du traitement, afin de déterminer si le traitement à une autre fin est compatible avec la finalité pour laquelle les données à caractère personnel ont été initialement collectées, tient compte, entre autres: e) de l'existence de garanties appropriées, qui peuvent comprendre le chiffrement ou la pseudonymisation. »

RÉPONSE :
Vous devez protéger les données personnelles que vous conservez en mettant en œuvre des mesures techniques et organisationnelles appropriées, telles que la pseudonymisation et le chiffrement des données [2], afin de garantir que seules les données nécessaires au regard des finalités spécifiques soient traitées [1]. Ces mesures doivent s'appliquer à la quantité, à l'étendue, à la durée de conservation et à l'accessibilité des données [1]. La sécurité des données doit être assurée par des moyens garantissant la confidentialité, l'intégrité, la disponibilité et la résilience des systèmes et services de traitement [2]. Vous devez également garantir que les données ne soient pas accessibles à un nombre indéterminé de personnes sans l'intervention de la personne concernée [1]. La conservation des données doit être limitée à la durée nécessaire aux finalités initiales [3], sauf pour des usages archivistiques, scientifiques ou statistiques, dans la mesure où des mesures techniques et organisationnelles appropriées sont mises en œuvre [3]. En cas d'incident, des moyens doivent permettre de rétablir la disponibilité des données et l'accès à celles-ci dans des délais appropriés [2]. Une procédure régulière de test, d'analyse et d'évaluation de l'efficacité des mesures doit être mise en place [2]. De plus, toute personne ayant accès aux données ne doit pas les traiter sans instruction du responsable du traitement, sauf obligation légale [2]. La protection des données doit inclure des garanties appropriées, telles que le chiffrement ou la pseudonymisation [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données personnelles ; traitement ; confidentialité ; finalité ; conservation ; sécurité

Temps : recherche 30.5 s · génération 66.6 s (3521 tokens lus, 1420 écrits, 31.7 tokens/s) · contrôle de pertinence 6.5 s · reformulation 2.8 s

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
  [2] RGPD — règlement (UE) 2016/679, article 4, définition 11 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [3] AI Act — règlement (UE) 2024/1689, article 61 : Consentement éclairé à participer aux essais en conditions réelles en dehors des bacs à sable réglementaires de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_61
  [4] AI Act — règlement (UE) 2024/1689, article 3, définition 59 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
  [5] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Si le consentement de la personne concernée est donné dans le cadre d'une déclaration écrite qui concerne également d'autres questions, la demande de consentement est présentée sous une forme qui la distingue clairement de ces autres questions, sous une forme compréhensible et aisément accessible, et formulée en des termes clairs et simples. »
- [2] « «consentement» de la personne concernée, toute manifestation de volonté, libre, spécifique, éclairée et univoque par laquelle la personne concernée accepte, par une déclaration ou par un acte positif clair, que des données à caractère personnel la concernant fassent l'objet d'un traitement; »
- [3] « Le consentement éclairé est daté et documenté et une copie en est remise aux participants aux essais ou à leur représentant légal. »
- [4] « «consentement éclairé», l’expression libre, spécifique, univoque et volontaire, par un participant, de sa volonté de participer à un essai en conditions réelles particulier, après avoir été informé de tous les éléments de l’essai qui lui permettent de prendre sa décision concernant sa participation; »

RÉPONSE :
Oui, le consentement peut être donné par écrit, car le RGPD (article 7, point 2) précise que, dans le cas d'une déclaration écrite incluant d'autres questions, le consentement est présenté sous une forme distincte, compréhensible et accessible. Le RGPD (article 2) définit le consentement comme une « manifestation de volonté, libre, spécifique, éclairée et univoque » par une « déclaration ou par un acte positif clair », ce qui inclut les formes écrites. L’AI Act (article 3) précise que le consentement éclairé est une « expression libre, spécifique, univoque et volontaire », et que le consentement éclairé est « daté et documenté », avec une copie remise aux participants. Cependant, les textes ne stipulent pas explicitement que le consentement doit être donné par écrit dans tous les cas, mais permettent une forme claire et positive (« acte positif clair »), qui peut inclure une forme écrite. Ainsi, bien que le consentement puisse être donné par écrit, il peut aussi être exprimé par un acte positif clair, comme une action ou un geste, selon le contexte. Les textes ne précise pas qu’il doit être obligatoirement écrit, mais indiquent que le consentement doit être libre, spécifique, éclairé et univoque, et que le document doit être daté et documenté [3].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : consentement éclairé ; expression claire ; indication explicite ; formulaire écrit ; accord formel ; données personnelles

Temps : recherche 27.7 s · génération 29.9 s (2466 tokens lus, 617 écrits, 35.1 tokens/s) · contrôle de pertinence 5.3 s · reformulation 3.1 s

## q23 — Quelles utilisations de l'intelligence artificielle sont interdites en Europe ?

Article attendu : AI Act art. 5, paragraphe 1 — passage [1].

### Réponse du copilote

> Les utilisations de l’intelligence artificielle sont interdites en Europe lorsque : on infère les émotions d’une personne sur le lieu de travail ou dans les établissements d’enseignement, sauf pour des raisons médicales ou de sécurité [1] ; on catégorise individuellement des personnes sur la base de données biométriques pour déduire leur race, leurs opinions politiques, leur affiliation syndicale, leurs convictions religieuses ou philosophiques, leur vie sexuelle ou leur orientation sexuelle, sauf dans le domaine répressif avec des données acquis légalement [1] ; on utilise des systèmes d’identification biométrique à distance en temps réel dans des espaces publics à des fins répressives, sauf dans des cas strictement nécessaires comme la recherche de victimes d’enlèvement, de traite ou d’exploitation, la prévention d’une menace imminente pour la vie ou la sécurité ou la localisation d’une personne soupçonnée d’infraction pénale [1] ; on utilise des techniques subliminales ou manipulatrices pour altérer le comportement d’une personne ou d’un groupe, causant un préjudice important [2] ; on exploite les vulnérabilités liées à l’âge, au handicap ou à la situation sociale ou économique pour altérer le comportement d’une personne ou d’un groupe, causant un préjudice important [2] ; on génère ou manipule des images ou contenus réalistes représentant les parties intimes d’une personne identifiable ou une personne se livrant à des activités sexuellement explicites sans son consentement libre, spécifique, éclairé, univoque et explicite [2] ; on évalue ou classe des personnes ou groupes selon leur comportement social ou personnalité, conduisant à un traitement préjudiciable ou défavorable, notamment dans un contexte dissocié de celui de collecte des données ou injustifié par rapport à leur comportement [2] ; on évalue les risques de délinquance d’une personne uniquement sur la base de profilages ou d’évaluations de traits de personnalité, sauf pour des cas déjà fondés sur des faits objectifs et vérifiables liés à une activité criminelle [2] ; on crée ou développe des bases de données de reconnaissance faciale par le moissonnage non ciblé d’images faciales sur internet ou en vidéosurveillance [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement, sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité; »
  [1] « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes de catégorisation biométrique qui catégorisent individuellement les personnes physiques sur la base de leurs données biométriques afin d’arriver à des déductions ou des inférences concernant leur race, leurs opinions politiques, leur affiliation à une organisation syndicale, leurs convictions religieuses ou philosophiques, leur vie sexuelle ou leur orientation sexuelle; cette interdiction ne couvre pas l’étiquetage ou le filtrage d’ensembles de données biométriques acquis légalement, tels que des images, fondés sur des données biométriques ou la catégorisation de données biométriques dans le domaine répressif; »
  [1] « l’utilisation de systèmes d’identification biométrique à distance en temps réel dans des espaces accessibles au public à des fins répressives, sauf si et dans la mesure où cette utilisation est strictement nécessaire eu égard à l’un des objectifs suivants: i) la recherche ciblée de victimes spécifiques d’enlèvement, de la traite ou de l’exploitation sexuelle d’êtres humains, ainsi que la recherche de personnes disparues; ii) la prévention d’une menace spécifique, substantielle et imminente pour la vie ou la sécurité physique de personnes physiques ou d’une menace réelle et actuelle ou réelle et prévisible d’attaque terroriste; iii) la localisation ou l’identification d’une personne soupçonnée d’avoir commis une infraction pénale, aux fins de mener une enquête pénale, d’engager des poursuites ou d’exécuter une sanction pénale pour des infractions visées à l’annexe II et punissables dans l’État membre concerné d’une peine ou d’une mesure de sûreté privatives de liberté d’une durée maximale d’au moins quatre ans. »
  [2] « la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui a recours à des techniques subliminales, au-dessous du seuil de conscience d’une personne, ou à des techniques délibérément manipulatrices ou trompeuses, avec pour objectif ou effet d’altérer substantiellement le comportement d’une personne ou d’un groupe de personnes en portant considérablement atteinte à leur capacité à prendre une décision éclairée, amenant ainsi la personne à prendre une décision qu’elle n’aurait pas prise autrement, d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne, à une autre personne ou à un groupe de personnes; »
  [2] « la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui exploite les éventuelles vulnérabilités dues à l’âge, au handicap ou à la situation sociale ou économique spécifique d’une personne physique ou d’un groupe de personnes donné avec pour objectif ou effet d’altérer substantiellement le comportement de cette personne ou d’un membre de ce groupe d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne ou à un tiers; »
  [2] « la mise sur le marché, la mise en service ou l'utilisation d'un système d'IA qui génère ou manipule des images, des vidéos, des contenus audio ou tout autre matériel similaire réalistes représentant les parties intimes d'une personne identifiable, ou une personne identifiable se livrant à des activités sexuellement explicites, sans le consentement libre, spécifique, éclairé, univoque et explicite de cette personne pour cette production ou manipulation; »
  [2] « la mise sur le marché, la mise en service ou l’utilisation de systèmes d’IA pour l’évaluation ou la classification de personnes physiques ou de groupes de personnes au cours d’une période donnée en fonction de leur comportement social ou de caractéristiques personnelles ou de personnalité connues, déduites ou prédites, la note sociale conduisant à l’une ou l’autre des situations suivantes, ou aux deux: i) le traitement préjudiciable ou défavorable de certaines personnes physiques ou de groupes de personnes dans des contextes sociaux dissociés du contexte dans lequel les données ont été générées ou collectées à l’origine; ii) le traitement préjudiciable ou défavorable de certaines personnes ou de groupes de personnes, qui est injustifié ou disproportionné par rapport à leur comportement social ou à la gravité de celui-ci; »
  [2] « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA qui créent ou développent des bases de données de reconnaissance faciale par le moissonnage non ciblé d’images faciales provenant de l’internet ou de la vidéosurveillance; »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points f) à h) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [2] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points a) à e) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, article 74, paragraphe 8 : Surveillance du marché et contrôle des systèmes d’IA sur le marché de l’Union
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_74
  [4] AI Act — règlement (UE) 2024/1689, article 74, paragraphe 1 : Surveillance du marché et contrôle des systèmes d’IA sur le marché de l’Union
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_74
  [5] AI Act — règlement (UE) 2024/1689, article 7, paragraphe 2 : Modifications de l’annexe III
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_7
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([2]) : ignoré(s).

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
- [2] « la mise sur le marché, la mise en service ou l'utilisation d'un système d'IA qui génère ou manipule des images, des vidéos, des contenus audio ou tout autre matériel similaire réalistes représentant les parties intimes d'une personne identifiable, ou une personne identifiable se livrant à des activités sexuellement explicites, sans le consentement libre, spécifique, éclairé, univoque et explicite de cette personne pour cette production ou manipulation; »
- [2] « la mise sur le marché, la mise en service ou l’utilisation de systèmes d’IA pour l’évaluation ou la classification de personnes physiques ou de groupes de personnes au cours d’une période donnée en fonction de leur comportement social ou de caractéristiques personnelles ou de personnalité connues, déduites ou prédites, la note sociale conduisant à l’une ou l’autre des situations suivantes, ou aux deux: i) le traitement préjudiciable ou défavorable de certaines personnes physiques ou de groupes de personnes dans des contextes sociaux dissociés du contexte dans lequel les données ont été générées ou collectées à l’origine; ii) le traitement préjudiciable ou défavorable de certaines personnes ou de groupes de personnes, qui est injustifié ou disproportionné par rapport à leur comportement social ou à la gravité de celui-ci; »
- [2] « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour mener des évaluations des risques des personnes physiques visant à évaluer ou à prédire le risque qu’une personne physique commette une infraction pénale, uniquement sur la base du profilage d’une personne physique ou de l’évaluation de ses traits de personnalité ou caractéristiques; cette interdiction ne s’applique pas aux systèmes d’IA utilisés pour étayer l’évaluation humaine de l’implication d’une personne dans une activité criminelle, qui est déjà fondée sur des faits objectifs et vérifiables, directement liés à une activité criminelle; »
- [2] « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA qui créent ou développent des bases de données de reconnaissance faciale par le moissonnage non ciblé d’images faciales provenant de l’internet ou de la vidéosurveillance; »

RÉPONSE :
Les utilisations de l’intelligence artificielle sont interdites en Europe lorsque : on infère les émotions d’une personne sur le lieu de travail ou dans les établissements d’enseignement, sauf pour des raisons médicales ou de sécurité [1] ; on catégorise individuellement des personnes sur la base de données biométriques pour déduire leur race, leurs opinions politiques, leur affiliation syndicale, leurs convictions religieuses ou philosophiques, leur vie sexuelle ou leur orientation sexuelle, sauf dans le domaine répressif avec des données acquis légalement [1] ; on utilise des systèmes d’identification biométrique à distance en temps réel dans des espaces publics à des fins répressives, sauf dans des cas strictement nécessaires comme la recherche de victimes d’enlèvement, de traite ou d’exploitation, la prévention d’une menace imminente pour la vie ou la sécurité ou la localisation d’une personne soupçonnée d’infraction pénale [1] ; on utilise des techniques subliminales ou manipulatrices pour altérer le comportement d’une personne ou d’un groupe, causant un préjudice important [2] ; on exploite les vulnérabilités liées à l’âge, au handicap ou à la situation sociale ou économique pour altérer le comportement d’une personne ou d’un groupe, causant un préjudice important [2] ; on génère ou manipule des images ou contenus réalistes représentant les parties intimes d’une personne identifiable ou une personne se livrant à des activités sexuellement explicites sans son consentement libre, spécifique, éclairé, univoque et explicite [2] ; on évalue ou classe des personnes ou groupes selon leur comportement social ou personnalité, conduisant à un traitement préjudiciable ou défavorable, notamment dans un contexte dissocié de celui de collecte des données ou injustifié par rapport à leur comportement [2] ; on évalue les risques de délinquance d’une personne uniquement sur la base de profilages ou d’évaluations de traits de personnalité, sauf pour des cas déjà fondés sur des faits objectifs et vérifiables liés à une activité criminelle [2] ; on crée ou développe des bases de données de reconnaissance faciale par le moissonnage non ciblé d’images faciales sur internet ou en vidéosurveillance [2].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : utilisations à finalité de surveillance ; traitements automatisés de données personnelles ; systèmes d'analyse de comportement ; applications de discrimination ; décisions automatisées sur des personnes ; traitements de données sensibles

Temps : recherche 30.2 s · génération 93.0 s (4149 tokens lus, 1933 écrits, 29.8 tokens/s) · contrôle de pertinence 11.1 s · reformulation 3.6 s

## q24 — Ai-je le droit d'utiliser une IA qui analyse les émotions de mes salariés ?

Article attendu : AI Act art. 5, paragraphe 1_f h — passage [1].

### Réponse du copilote

> Non : vous n’avez pas le droit d’utiliser une IA qui analyse les émotions de vos salariés, sauf si l’utilisation est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité [1]. Cette interdiction s’applique à l’analyse des émotions sur le lieu de travail ou dans les établissements d’enseignement, même si le système est conçu pour interagir avec les salariés [4]. L’obligation de transparence (article 50) s’applique aux systèmes de reconnaissance des émotions, sauf si l’utilisation est autorisée par la loi à des fins de prévention ou de détection d’infractions pénales ou d’enquêtes, sous réserve de garanties appropriées pour les droits et libertés des salariés [2] et [3]. Cependant, ces cas spécifiques ne couvrent pas l’analyse des émotions dans un contexte de gestion des salariés. Ainsi, l’usage d’une telle IA dans un cadre de gestion ou de surveillance est interdit, sauf dans des cas médicaux ou de sécurité.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement, sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité; »
  [2] « Les déployeurs d’un système de reconnaissance des émotions ou d’un système de catégorisation biométrique informent les personnes physiques qui y sont exposées du fonctionnement du système et traitent les données à caractère personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680, selon le cas. Cette obligation ne s’applique pas aux systèmes d’IA utilisés pour la catégorisation biométrique et la reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l’Union. »
  [3] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. Cette obligation ne s’applique pas aux systèmes d’IA dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers, sauf si ces systèmes sont mis à la disposition du public pour permettre le signalement d’une infraction pénale. »
  [4] « «système de reconnaissance des émotions», un système d’IA permettant la reconnaissance ou la déduction des émotions ou des intentions de personnes physiques sur la base de leurs données biométriques; »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points f) à h) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 3 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [3] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [4] AI Act — règlement (UE) 2024/1689, article 3, définition 39 : Définitions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
Passages consultés mais non cités :
  [5] AI Act — règlement (UE) 2024/1689, annexe III, point 1 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement, sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité; »
- [2] « Les déployeurs d’un système de reconnaissance des émotions ou d’un système de catégorisation biométrique informent les personnes physiques qui y sont exposées du fonctionnement du système et traitent les données à caractère personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680, selon le cas. Cette obligation ne s’applique pas aux systèmes d’IA utilisés pour la catégorisation biométrique et la reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l’Union. »
- [3] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. Cette obligation ne s’applique pas aux systèmes d’IA dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers, sauf si ces systèmes sont mis à la disposition du public pour permettre le signalement d’une infraction pénale. »
- [4] « «système de reconnaissance des émotions», un système d’IA permettant la reconnaissance ou la déduction des émotions ou des intentions de personnes physiques sur la base de leurs données biométriques; »

RÉPONSE :
Non : vous n’avez pas le droit d’utiliser une IA qui analyse les émotions de vos salariés, sauf si l’utilisation est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité [1]. Cette interdiction s’applique à l’analyse des émotions sur le lieu de travail ou dans les établissements d’enseignement, même si le système est conçu pour interagir avec les salariés [4]. L’obligation de transparence (article 50) s’applique aux systèmes de reconnaissance des émotions, sauf si l’utilisation est autorisée par la loi à des fins de prévention ou de détection d’infractions pénales ou d’enquêtes, sous réserve de garanties appropriées pour les droits et libertés des salariés [2] et [3]. Cependant, ces cas spécifiques ne couvrent pas l’analyse des émotions dans un contexte de gestion des salariés. Ainsi, l’usage d’une telle IA dans un cadre de gestion ou de surveillance est interdit, sauf dans des cas médicaux ou de sécurité.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données biométriques ; traitement automatisé des données ; données personnelles ; finalité du traitement ; consentement explicite

Temps : recherche 30.5 s · génération 34.3 s (2760 tokens lus, 829 écrits, 34.1 tokens/s) · contrôle de pertinence 7.2 s · reformulation 3.4 s

## q25 — Mon logiciel est-il un « système d'IA » au sens de la loi européenne ?

Article attendu : AI Act art. 3, définition 1 — passage [1].

### Réponse du copilote

> Oui : votre logiciel est un « système d’IA » au sens de la loi européenne, s’il répond aux critères définis dans l’article 3, paragraphe 1 du règlement (UE) 2024/1689, à savoir s’il est un système automatisé conçu pour fonctionner à différents niveaux d’autonomie, capable d’adaptation après déploiement, et qui, pour des objectifs explicites ou implicites, déduit à partir des entrées la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « système d’IA», un système automatisé qui est conçu pour fonctionner à différents niveaux d’autonomie et peut faire preuve d’une capacité d’adaptation après son déploiement, et qui, pour des objectifs explicites ou implicites, déduit, à partir des entrées qu’il reçoit, la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels; »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 3, définition 1 : Définitions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, annexe IV, point 2 : Documentation technique visée à l'article 11, paragraphe 1
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_IV
  [3] AI Act — règlement (UE) 2024/1689, article 3, définition 66 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
  [4] AI Act — règlement (UE) 2024/1689, annexe III, point 8 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [5] AI Act — règlement (UE) 2024/1689, article 6, paragraphe 1 bis : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] «système d’IA», un système automatisé qui est conçu pour fonctionner à différents niveaux d’autonomie et peut faire preuve d’une capacité d’adaptation après son déploiement, et qui, pour des objectifs explicites ou implicites, déduit, à partir des entrées qu’il reçoit, la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels; 

RÉPONSE :
Oui : votre logiciel est un « système d’IA » au sens de la loi européenne, s’il répond aux critères définis dans l’article 3, paragraphe 1 du règlement (UE) 2024/1689, à savoir s’il est un système automatisé conçu pour fonctionner à différents niveaux d’autonomie, capable d’adaptation après déploiement, et qui, pour des objectifs explicites ou implicites, déduit à partir des entrées la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : système d'intelligence artificielle ; modèle d'apprentissage automatique ; algorithme d'apprentissage ; processus de traitement de données ; fonctionnalité d'analyse prédictive ; capacité d'adaptation automatique

Temps : recherche 26.0 s · génération 23.8 s (2851 tokens lus, 282 écrits, 34.7 tokens/s) · contrôle de pertinence 4.0 s · reformulation 3.8 s

## q26 — Dois-je indiquer qu'une image publiée sur notre site a été créée par une IA ?

Article attendu : AI Act art. 50, paragraphe 4 — passage [1].

### Réponse du copilote

> Oui : vous devez indiquer qu’une image publiée sur votre site a été créée par une IA, sauf si l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière [1], ou si le contenu fait partie d’une œuvre manifestement artistique, créative, satirique, fictif ou analogue, dans ce cas la transparence se limite à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre [1]. De plus, cette obligation ne s’applique pas si le système d’IA ne modifie pas de manière substantielle les données d’entrée fournies par vous ou leur sémantique [3]. Cependant, ces exceptions ne s’appliquent pas automatiquement à une image publiée sur votre site, sauf dans les cas précisément prévus par la loi ou dans les cas d’œuvres manifestement artistiques ou fictifs [1].

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
  [4] AI Act — règlement (UE) 2024/1689, annexe XII : Informations relatives à la transparence visées à l'article 53, paragraphe 1, point b) – documentation technique pour les fournisseurs de modèles d'IA à usage général aux fournisseurs en aval qui intègrent le modèle dans leur système d'IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_XII
  [5] AI Act — règlement (UE) 2024/1689, annexe VIII, point 4 : Informations à fournir lors de l'enregistrement d'un système d'IA à haut risque conformément à l'article 49
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_VIII
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([3]) : ignoré(s).
Attention : La réponse cite [3] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.
Attention : La réponse formule une exception qui ne reprend pas les extraits vérifiés : « sauf dans les cas précisément prévus par la loi ou dans les cas d’œuvres ». Vérifiez-la dans les textes.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. Cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. Lorsque le contenu fait partie d’une œuvre ou d’un programme manifestement artistique, créatif, satirique, fictif ou analogue, les obligations de transparence énoncées au présent paragraphe se limitent à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre. »
- [3] « Les fournisseurs de systèmes d’IA, y compris de systèmes d’IA à usage général, qui génèrent des contenus de synthèse de type audio, image, vidéo ou texte, veillent à ce que les sorties des systèmes d’IA soient marquées dans un format lisible par machine et identifiables comme ayant été générées ou manipulées par une IA. Cette obligation ne s’applique pas dans la mesure où les systèmes d’IA remplissent une fonction d’assistance pour la mise en forme standard ou ne modifient pas de manière substantielle les données d’entrée fournies par le déployeur ou leur sémantique, ou lorsque leur utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. »

RÉPONSE :
Oui : vous devez indiquer qu’une image publiée sur votre site a été créée par une IA, sauf si l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière [1], ou si le contenu fait partie d’une œuvre manifestement artistique, créative, satirique, fictif ou analogue, dans ce cas la transparence se limite à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre [1]. De plus, cette obligation ne s’applique pas si le système d’IA ne modifie pas de manière substantielle les données d’entrée fournies par vous ou leur sémantique [3]. Cependant, ces exceptions ne s’appliquent pas automatiquement à une image publiée sur votre site, sauf dans les cas précisément prévus par la loi ou dans les cas d’œuvres manifestement artistiques ou fictifs [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : information sur l'origine de la création d'une image ; données d'origine d'une œuvre ; utilisation d'une intelligence artificielle ; source d'une représentation ; indicateur de création par IA ; données générées par une IA

Temps : recherche 32.6 s · génération 35.6 s (2916 tokens lus, 656 écrits, 34.0 tokens/s) · contrôle de pertinence 4.1 s · reformulation 3.7 s

## q27 — Quelles amendes prévoit le règlement européen sur l'intelligence artificielle ?

Article attendu : AI Act art. 99, paragraphe 4 ou AI Act art. 99, paragraphe 6 — absent des passages donnés au modèle.

### Réponse du copilote

> Le règlement européen sur l'intelligence artificielle prévoit plusieurs types d'amendes. Pour le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5, les amendes peuvent aller jusqu’à 35 000 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 7 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu [2]. Pour les institutions, organes ou organismes de l’Union, le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’une amende administrative pouvant aller jusqu’à 1 500 000 EUR [3], tandis que la non-conformité du système d’IA avec d'autres exigences du règlement (hors article 5) fait l’objet d’une amende administrative pouvant aller jusqu’à 750 000 EUR [3]. Ces sanctions s’appliquent mutatis mutandis au Bureau de l’IA dans l’exécution de ses tâches de surveillance et de contrôle [4]. Les amendes sont imposées selon des critères précis, notamment la nature, la gravité et la durée de la violation, le degré de responsabilité, la coopération avec le Contrôleur européen de la protection des données, et le budget annuel de l’organisme concerné [3]. Les droits de la défense des parties concernées sont pleinement respectés [3]. Les fonds collectés contribuent au budget général de l’Union [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Ces sanctions doivent être effectives, proportionnées et dissuasives. Lorsqu'ils imposent des sanctions, les États membres tiennent compte des intérêts des PME, y compris les jeunes pousses, et des petites entreprises à moyenne capitalisation, ainsi que de leur viabilité économique. »
  [2] « Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’amendes administratives pouvant aller jusqu’à 35 000 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 7 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu. »
  [3] « Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’une amende administrative pouvant aller jusqu’à 1 500 000 EUR. »
  [3] « La non-conformité du système d’IA avec les exigences ou obligations au titre du présent règlement, autres que celles énoncées à l’article 5, fait l’objet d’une amende administrative pouvant aller jusqu’à 750 000 EUR. »
  [4] « Une décision adoptée en vertu du paragraphe 1 du présent article peut s'accompagner de l'imposition de sanctions conformément à l'article 99, paragraphes 3 à 7, dont les dispositions s'appliquent mutatis mutandis au Bureau de l'IA dans l'exécution de ses tâches de surveillance et de contrôle visées à l’article 75, paragraphe 1. En particulier, fait l'objet d'une amende administrative visée à l’article 99, paragraphe 4: »
  [5] « Lorsque le Bureau de l'IA constate qu'un opérateur relevant du champ d'application de l'article 75, paragraphe 1, ne respecte pas les dispositions pertinentes du présent règlement ou les engagements rendus contraignants au titre de l'article 75 ter, il adopte une décision établissant cette non-conformité. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 1 : Sanctions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [2] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 3 : Sanctions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [3] AI Act — règlement (UE) 2024/1689, article 100 : Amendes administratives imposées aux institutions, organes et organismes de l’Union (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_100
  [4] AI Act — règlement (UE) 2024/1689, article 75 quater, paragraphe 4 : Non-conformité, amendes et astreintes (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_75c
  [5] AI Act — règlement (UE) 2024/1689, article 75 quater, paragraphe 1 : Non-conformité, amendes et astreintes (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_75c

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Ces sanctions doivent être effectives, proportionnées et dissuasives. Lorsqu'ils imposent des sanctions, les États membres tiennent compte des intérêts des PME, y compris les jeunes pousses, et des petites entreprises à moyenne capitalisation, ainsi que de leur viabilité économique. »
- [2] « Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’amendes administratives pouvant aller jusqu’à 35 000 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 7 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu. »
- [3] « Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’une amende administrative pouvant aller jusqu’à 1 500 000 EUR. »
- [3] « La non-conformité du système d’IA avec les exigences ou obligations au titre du présent règlement, autres que celles énoncées à l’article 5, fait l’objet d’une amende administrative pouvant aller jusqu’à 750 000 EUR. »
- [4] « Une décision adoptée en vertu du paragraphe 1 du présent article peut s'accompagner de l'imposition de sanctions conformément à l'article 99, paragraphes 3 à 7, dont les dispositions s'appliquent mutatis mutandis au Bureau de l'IA dans l'exécution de ses tâches de surveillance et de contrôle visées à l’article 75, paragraphe 1. En particulier, fait l'objet d'une amende administrative visée à l’article 99, paragraphe 4: »
- [5] « Lorsque le Bureau de l'IA constate qu'un opérateur relevant du champ d'application de l'article 75, paragraphe 1, ne respecte pas les dispositions pertinentes du présent règlement ou les engagements rendus contraignants au titre de l'article 75 ter, il adopte une décision établissant cette non-conformité. »

RÉPONSE :
Le règlement européen sur l'intelligence artificielle prévoit plusieurs types d'amendes. Pour le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5, les amendes peuvent aller jusqu’à 35 000 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 7 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu [2]. Pour les institutions, organes ou organismes de l’Union, le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’une amende administrative pouvant aller jusqu’à 1 500 000 EUR [3], tandis que la non-conformité du système d’IA avec d'autres exigences du règlement (hors article 5) fait l’objet d’une amende administrative pouvant aller jusqu’à 750 000 EUR [3]. Ces sanctions s’appliquent mutatis mutandis au Bureau de l’IA dans l’exécution de ses tâches de surveillance et de contrôle [4]. Les amendes sont imposées selon des critères précis, notamment la nature, la gravité et la durée de la violation, le degré de responsabilité, la coopération avec le Contrôleur européen de la protection des données, et le budget annuel de l’organisme concerné [3]. Les droits de la défense des parties concernées sont pleinement respectés [3]. Les fonds collectés contribuent au budget général de l’Union [3].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : sanctions financières ; pénalités ; sanctions ; mesures de sanction ; responsabilité civile ; responsabilité pénale

Temps : recherche 30.0 s · génération 43.8 s (2889 tokens lus, 936 écrits, 33.6 tokens/s) · contrôle de pertinence 6.3 s · reformulation 3.2 s

## h03 — Comment déclarer la création d'une association en préfecture ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [3] RGPD — règlement (UE) 2016/679, article 60, paragraphe 7 : Coopération entre l'autorité de contrôle chef de file et les autres autorités de contrôle concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_60
  [4] RGPD — règlement (UE) 2016/679, article 60, paragraphe 1 : Coopération entre l'autorité de contrôle chef de file et les autres autorités de contrôle concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_60
  [5] RGPD — règlement (UE) 2016/679, article 4, définition 2 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun  
RÉPONSE : Les textes trouvés ne traitent pas de la déclaration de création d'une association en préfecture.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : création d'association ; déclaration au registre du commerce et des sociétés ; inscription au registre des associations ; demande de reconnaissance d'activité ; dépôt de la constitution ; procédure administrative

Temps : recherche 21.0 s · génération 15.9 s (2776 tokens lus, 36 écrits, 36.1 tokens/s) · reformulation 3.5 s

## h04 — Quel est le montant du SMIC cette année ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, annexe X, point 7 a : Actes législatifs de l'Union relatifs aux systèmes d'information à grande échelle au sein de l'espace de liberté, de sécurité et de justice
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_X
  [2] AI Act — règlement (UE) 2024/1689, article 112, paragraphe 4 : Évaluation et réexamen
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_112
  [3] AI Act — règlement (UE) 2024/1689, article 112, paragraphe 1 : Évaluation et réexamen
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_112
  [4] AI Act — règlement (UE) 2024/1689, article 1 : Objet
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_1
  [5] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 6 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun  
RÉPONSE : Les textes trouvés ne traitent pas de ce point.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : salaire minimum interprofessionnel ; revenu de référence ; seuil de pauvreté ; niveau de vie ; revenu minimum ; taux de base

Temps : recherche 18.1 s · génération 12.4 s (2384 tokens lus, 26 écrits, 37.6 tokens/s) · reformulation 3.3 s

## h05 — Comment rédiger les statuts d'une association ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 4, définition 7 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [2] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [3] RGPD — règlement (UE) 2016/679, article 40, paragraphe 1 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
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
- [2] « Les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent élaborer des codes de conduite, les modifier ou les proroger, aux fins de préciser les modalités d'application du présent règlement, telles que: a) le traitement loyal et transparent; b) les intérêts légitimes poursuivis par les responsables du traitement dans des contextes spécifiques; c) la collecte des données à caractère personnel; d) la pseudonymisation des données à caractère personnel; e) les informations communiquées au public et aux personnes concernées; f) l'exercice des droits des personnes concernées; g) les informations communiquées aux enfants et la protection dont bénéficient les enfants et la manière d'obtenir le consentement des titulaires de la responsabilité parentale à l'égard de l'enfant; h) les mesures et les procédures visées aux articles 24 et 25 et les mesures visant à assurer la sécurité du traitement visées à l'article 32; i) la notification aux autorités de contrôle des violations de données à caractère personnel et la communication de ces violations aux personnes concernées; j) le transfert de données à caractère personnel vers des pays tiers ou à des organisations internationales; ou k) les procédures extrajudiciaires et autres procédures de règlement des litiges permettant de résoudre les litiges entre les responsables du traitement et les personnes concernées en ce qui concerne le traitement, sans préjudice des droits des personnes concernées au titre des articles 77 et 79. »  
- [3] « Les États membres, les autorités de contrôle, le comité et la Commission encouragent l'élaboration de codes de conduite destinés à contribuer à la bonne application du présent règlement, compte tenu de la spécificité des différents secteurs de traitement et des besoins spécifiques des micro, petites et moyennes entreprises. »  

RÉPONSE :  
Les statuts d'une association doivent inclure des dispositions relatives au traitement des données à caractère personnel, en particulier en ce qui concerne le traitement loyal et transparent, la collecte des données, la pseudonymisation, l'exercice des droits des personnes concernées, les informations communiquées aux enfants, la protection des données et les procédures de règlement des litiges, conformément aux codes de conduite établis par des associations représentant des catégories de responsables du traitement ou de sous-traitants [2]. L'élaboration de tels codes est encouragée par les États membres, les autorités de contrôle, le comité et la Commission, en tenant compte de la spécificité des secteurs de traitement et des besoins des micro, petites et moyennes entreprises [3].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : statuts ; finalité ; objet ; composition ; pouvoir ; fonctionnement

Temps : recherche 27.3 s · génération 32.7 s (2634 tokens lus, 645 écrits, 34.8 tokens/s) · contrôle de pertinence 6.4 s · reformulation 2.8 s
