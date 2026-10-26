# Réponses du copilote — heldout_v4

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 26/10/2026 à 13:18 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen3:4b-instruct` via Ollama 0.40.11 — température 0.1, contexte 8192 tokens, couches sur la carte graphique : toutes, 2000 tokens au plus par réponse
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_v1.jsonl` (17 + 3 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q11 | Un client me demande d'effacer toutes ses données : suis-je obligé de le faire ? | 3/8 | non | 5 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1], [1], [1], [1], [1]) : ignoré(s). | 65 s |
| q12 | Un salarié demande une copie de toutes les données que nous avons sur lui : que dois-je lui donner ? | 2/2 | non | — | 48 s |
| q13 | Un adhérent veut récupérer ses données pour les donner à une autre association : est-ce un droit ? | 1/1 | non | — | 36 s |
| q14 | Puis-je envoyer une lettre d'information par e-mail à mes adhérents, et peuvent-ils refuser ? | 4/4 | non | — | 41 s |
| q15 | Mon prestataire informatique a accès à nos fichiers : faut-il signer un contrat particulier ? | 2/2 | non | La réponse met entre « » un texte introuvable dans les extraits vérifiés : « sur instruction documentée du responsable du traitement ». | 39 s |
| q16 | Puis-je stocker les fichiers de mon association chez un hébergeur situé aux États-Unis ? | 5/5 | non | — | 61 s |
| q17 | Quelles sanctions risque une petite entreprise qui ne respecte pas le RGPD ? | 3/4 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([4]) : ignoré(s). | 216 s |
| q18 | Notre association peut-elle collecter des informations sur la santé de ses bénévoles ? | 3/3 | non | La réponse cite [5] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.; La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Aucune obligation de secret professionnel n’est requise pour une association, donc le traitement ne peut être effectué … ». Vérifiez ce point. | 45 s |
| q19 | Qu'est-ce qu'une donnée personnelle ? | 1/1 | non | — | 27 s |
| q20 | À partir de quel âge un enfant peut-il s'inscrire seul à notre service en ligne ? | 1/1 | non | — | 56722 s |
| q21 | Comment dois-je protéger les données personnelles que nous conservons ? | 4/4 | non | — | 61 s |
| q22 | Le consentement d'une personne doit-il être donné par écrit ? | 3/3 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 32 s |
| q23 | Quelles utilisations de l'intelligence artificielle sont interdites en Europe ? | 8/8 | non | La réponse formule une exception qui ne reprend pas les extraits vérifiés : « sauf dans les cas précisément autorisés : la recherche de victimes d’enlèvement, de traite ». Vérifiez-la dans les textes. | 68 s |
| q24 | Ai-je le droit d'utiliser une IA qui analyse les émotions de mes salariés ? | 2/2 | non | — | 51 s |
| q25 | Mon logiciel est-il un « système d'IA » au sens de la loi européenne ? | 1/1 | non | — | 28 s |
| q26 | Dois-je indiquer qu'une image publiée sur notre site a été créée par une IA ? | 1/2 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([2]) : ignoré(s).; La réponse cite [2] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations. | 42 s |
| q27 | Quelles amendes prévoit le règlement européen sur l'intelligence artificielle ? | 4/4 | non | — | 46 s |
| h03 | Comment déclarer la création d'une association en préfecture ? | 0/0 | oui | — | 33 s |
| h04 | Quel est le montant du SMIC cette année ? | 0/0 | oui | — | 23 s |
| h05 | Comment rédiger les statuts d'une association ? | 0/0 | oui | — | 23 s |

## q11 — Un client me demande d'effacer toutes ses données : suis-je obligé de le faire ?

Article attendu : RGPD art. 17 — passage [1].

### Réponse du copilote

> Oui : vous êtes obligé d'effacer les données à caractère personnel du client dans les meilleurs délais, lorsque l'un des motifs suivants s'applique : a) les données ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées d'une autre manière ; b) le client a retiré son consentement et il n'existe pas d'autre fondement juridique au traitement ; c) le client s'oppose au traitement et il n'existe pas de motif légitime impérieux ; d) le traitement a été illicite ; e) l'effacement est requis par une obligation légale de l'Union ou d'un État membre ; f) les données ont été collectées dans le cadre de l'offre de services de la société de l'information. Cependant, cette obligation ne s'applique pas si le traitement est nécessaire à l'exercice du droit à la liberté d'expression et d'information, à respecter une obligation légale, à exécuter une mission d'intérêt public, à des fins archivistiques, de recherche scientifique ou historique ou à des fins statistiques, ou à la constatation, à l'exercice ou à la défense de droits en justice [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit d'obtenir du responsable du traitement l'effacement, dans les meilleurs délais, de données à caractère personnel la concernant et le responsable du traitement a l'obligation d'effacer ces données à caractère personnel dans les meilleurs délais, lorsque l'un des motifs suivants s'applique: … »
  [1] « … lorsque l'un des motifs suivants s'applique: a) les données à caractère personnel ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées d'une autre manière; … »
  [1] « 3. Les paragraphes 1 et 2 ne s'appliquent pas dans la mesure où ce traitement est nécessaire: a) à l'exercice du droit à la liberté d'expression et d'information; b) pour respecter une obligation légale qui requiert le traitement prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis, ou pour exécuter une mission d'intérêt public ou relevant de l'exercice de l'autorité publique dont est investi le responsable du traitement; c) pour des motifs d'intérêt public dans le domaine de la santé publique, conformément à l'article 9, paragraphe 2, points h) et i), ainsi qu'à l'article 9, paragraphe 3; d) à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, dans la mesure où le droit visé au paragraphe 1 est susceptible de rendre impossible ou de compromettre gravement la réalisation des objectifs dudit traitement; ou e) à la constatation, à l'exercice ou à la défense de droits en justice. »

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
Attention : 5 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1], [1], [1], [1], [1]) : ignoré(s).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « La personne concernée a le droit d'obtenir du responsable du traitement l'effacement, dans les meilleurs délais, de données à caractère personnel la concernant et le responsable du traitement a l'obligation d'effacer ces données à caractère personnel dans les meilleurs délais, lorsque l'un des motifs suivants s'applique: … »
- [1] « … lorsque l'un des motifs suivants s'applique: a) les données à caractère personnel ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées d'une autre manière; … »
- [1] « … lorsque l'un des motifs suivants s'applique: b) la personne concernée retire le consentement sur lequel est fondé le traitement, conformément à l'article 6, paragraphe 1, point a), ou à l'article 9, paragraphe 2, point a), et il n'existe pas d'autre fondement juridique au traitement; … »
- [1] « … lorsque l'un des motifs suivants s'applique: c) la personne concernée s'oppose au traitement en vertu de l'article 21, paragraphe 1, et il n'existe pas de motif légitime impérieux pour le traitement, ou la personne concernée s'oppose au traitement en vertu de l'article 21, paragraphe 2; … »
- [1] « … lorsque l'un des motifs suivants s'applique: d) les données à caractère personnel ont fait l'objet d'un traitement illicite; … »
- [1] « … lorsque l'un des motifs suivants s'applique: e) les données à caractère personnel doivent être effacées pour respecter une obligation légale qui est prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis; … »
- [1] « … lorsque l'un des motifs suivants s'applique: f) les données à caractère personnel ont été collectées dans le cadre de l'offre de services de la société de l'information visée à l'article 8, paragraphe 1. »
- [1] « 3. Les paragraphes 1 et 2 ne s'appliquent pas dans la mesure où ce traitement est nécessaire: a) à l'exercice du droit à la liberté d'expression et d'information; b) pour respecter une obligation légale qui requiert le traitement prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis, ou pour exécuter une mission d'intérêt public ou relevant de l'exercice de l'autorité publique dont est investi le responsable du traitement; c) pour des motifs d'intérêt public dans le domaine de la santé publique, conformément à l'article 9, paragraphe 2, points h) et i), ainsi qu'à l'article 9, paragraphe 3; d) à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, dans la mesure où le droit visé au paragraphe 1 est susceptible de rendre impossible ou de compromettre gravement la réalisation des objectifs dudit traitement; ou e) à la constatation, à l'exercice ou à la défense de droits en justice. »

RÉPONSE :
Oui : vous êtes obligé d'effacer les données à caractère personnel du client dans les meilleurs délais, lorsque l'un des motifs suivants s'applique : a) les données ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées d'une autre manière ; b) le client a retiré son consentement et il n'existe pas d'autre fondement juridique au traitement ; c) le client s'oppose au traitement et il n'existe pas de motif légitime impérieux ; d) le traitement a été illicite ; e) l'effacement est requis par une obligation légale de l'Union ou d'un État membre ; f) les données ont été collectées dans le cadre de l'offre de services de la société de l'information. Cependant, cette obligation ne s'applique pas si le traitement est nécessaire à l'exercice du droit à la liberté d'expression et d'information, à respecter une obligation légale, à exécuter une mission d'intérêt public, à des fins archivistiques, de recherche scientifique ou historique ou à des fins statistiques, ou à la constatation, à l'exercice ou à la défense de droits en justice [1].
```

</details>

Temps : recherche 3.0 s · génération 55.6 s (4103 tokens lus, 1084 écrits, 24.6 tokens/s) · contrôle de pertinence 6.6 s

## q12 — Un salarié demande une copie de toutes les données que nous avons sur lui : que dois-je lui donner ?

Article attendu : RGPD art. 15 — passage [2].

### Réponse du copilote

> Vous devez lui fournir une copie des données à caractère personnel qui vous concernent, conformément à l’article 15, paragraphe 3 du RGPD [2]. Cette copie peut être fournie sous une forme électronique d’usage courant, à moins qu’il ne demande autrement [2]. En outre, vous lui devez fournir les informations suivantes : les finalités du traitement, les catégories de données concernées, les destinataires ou catégories de destinataires, la durée de conservation des données ou les critères utilisés pour déterminer cette durée, l’existence du droit de rectification, d’effacement, de limitation du traitement, de s’opposer au traitement et du droit à la portabilité des données [2], [4]. Vous pouvez exiger des frais raisonnables basés sur les coûts administratifs pour une copie supplémentaire [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « Le responsable du traitement fournit une copie des données à caractère personnel faisant l'objet d'un traitement. Le responsable du traitement peut exiger le paiement de frais raisonnables basés sur les coûts administratifs pour toute copie supplémentaire demandée par la personne concernée. Lorsque la personne concernée présente sa demande par voie électronique, les informations sont fournies sous une forme électronique d'usage courant, à moins que la personne concernée ne demande qu'il en soit autrement. »
  [4] « En plus des informations visées au paragraphe 1, le responsable du traitement fournit à la personne concernée les informations suivantes nécessaires pour garantir un traitement équitable et transparent à l'égard de la personne concernée: … c) l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ainsi que du droit de s'opposer au traitement et du droit à la portabilité des données; … »

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
- [4] « En plus des informations visées au paragraphe 1, le responsable du traitement fournit à la personne concernée les informations suivantes nécessaires pour garantir un traitement équitable et transparent à l'égard de la personne concernée: … c) l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ainsi que du droit de s'opposer au traitement et du droit à la portabilité des données; … »

RÉPONSE :
Vous devez lui fournir une copie des données à caractère personnel qui vous concernent, conformément à l’article 15, paragraphe 3 du RGPD [2]. Cette copie peut être fournie sous une forme électronique d’usage courant, à moins qu’il ne demande autrement [2]. En outre, vous lui devez fournir les informations suivantes : les finalités du traitement, les catégories de données concernées, les destinataires ou catégories de destinataires, la durée de conservation des données ou les critères utilisés pour déterminer cette durée, l’existence du droit de rectification, d’effacement, de limitation du traitement, de s’opposer au traitement et du droit à la portabilité des données [2], [4]. Vous pouvez exiger des frais raisonnables basés sur les coûts administratifs pour une copie supplémentaire [2].
```

</details>

Temps : recherche 2.4 s · génération 40.5 s (4035 tokens lus, 459 écrits, 25.0 tokens/s) · contrôle de pertinence 5.2 s

## q13 — Un adhérent veut récupérer ses données pour les donner à une autre association : est-ce un droit ?

Article attendu : RGPD art. 20 — passage [1].

### Réponse du copilote

> Oui : un adhérent a le droit de récupérer ses données personnelles pour les transmettre à une autre association, dans les conditions prévues par l'article 20 du RGPD, lorsque le traitement est fondé sur le consentement ou un contrat et qu’il est effectué à l’aide de procédés automatisés [1]. Ce droit s’applique sans que le responsable du traitement y fasse obstacle [1].

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
Oui : un adhérent a le droit de récupérer ses données personnelles pour les transmettre à une autre association, dans les conditions prévues par l'article 20 du RGPD, lorsque le traitement est fondé sur le consentement ou un contrat et qu’il est effectué à l’aide de procédés automatisés [1]. Ce droit s’applique sans que le responsable du traitement y fasse obstacle [1].
```

</details>

Temps : recherche 2.5 s · génération 28.6 s (2937 tokens lus, 286 écrits, 26.6 tokens/s) · contrôle de pertinence 4.6 s

## q14 — Puis-je envoyer une lettre d'information par e-mail à mes adhérents, et peuvent-ils refuser ?

Article attendu : RGPD art. 21 ou RGPD art. 6, paragraphe 1 — passage [1].

### Réponse du copilote

> Oui, vous pouvez envoyer une lettre d'information par e-mail à vos adhérents, car cela relève de la prospection, et donc du traitement à des fins de prospection, tel que prévu dans l'article 21, paragraphe 1, du RGPD [1]. Les adhérents ont le droit de s'opposer à tout moment à ce traitement, notamment au profilage lié à cette prospection [1]. Lorsqu’un adhérent s’oppose à ce traitement, les données ne sont plus utilisées à ces fins [1]. Ce droit est explicitement porté à l’attention de la personne concernée au plus tard au moment de la première communication [1]. Les adhérents peuvent donc refuser ce traitement par e-mail, et ce refus entraîne la cessation du traitement à ces fins [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit de s'opposer à tout moment, pour des raisons tenant à sa situation particulière, à un traitement des données à caractère personnel la concernant fondé sur l'article 6, paragraphe 1, point e) ou f), y compris un profilage fondé sur ces dispositions. »
  [1] « Lorsque les données à caractère personnel sont traitées à des fins de prospection, la personne concernée a le droit de s'opposer à tout moment au traitement des données à caractère personnel la concernant à de telles fins de prospection, y compris au profilage dans la mesure où il est lié à une telle prospection. »
  [1] « Lorsque la personne concernée s'oppose au traitement à des fins de prospection, les données à caractère personnel ne sont plus traitées à ces fins. »
  [2] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: … »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 21 : Droit d'opposition (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_21
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 24 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [4] RGPD — règlement (UE) 2016/679, article 80 : Représentation des personnes concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_80
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

RÉPONSE :
Oui, vous pouvez envoyer une lettre d'information par e-mail à vos adhérents, car cela relève de la prospection, et donc du traitement à des fins de prospection, tel que prévu dans l'article 21, paragraphe 1, du RGPD [1]. Les adhérents ont le droit de s'opposer à tout moment à ce traitement, notamment au profilage lié à cette prospection [1]. Lorsqu’un adhérent s’oppose à ce traitement, les données ne sont plus utilisées à ces fins [1]. Ce droit est explicitement porté à l’attention de la personne concernée au plus tard au moment de la première communication [1]. Les adhérents peuvent donc refuser ce traitement par e-mail, et ce refus entraîne la cessation du traitement à ces fins [1].
```

</details>

Temps : recherche 2.5 s · génération 34.2 s (2842 tokens lus, 461 écrits, 26.7 tokens/s) · contrôle de pertinence 4.6 s

## q15 — Mon prestataire informatique a accès à nos fichiers : faut-il signer un contrat particulier ?

Article attendu : RGPD art. 28, paragraphe 3 — passage [1].

### Réponse du copilote

> Oui : il faut signer un contrat particulier, car le traitement par un sous-traitant, y compris celui qui a accès à vos fichiers, est régi par un contrat ou un autre acte juridique qui définit les obligations du sous-traitant [1]. Ce contrat doit notamment préciser que le sous-traitant ne traite les données qu’« sur instruction documentée du responsable du traitement » [1], et que toute personne agissant sous son autorité ne peut pas traiter ces données sans instruction [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre, qui lie le sous-traitant à l'égard du responsable du traitement, définit l'objet et la durée du traitement, la nature et la finalité du traitement, le type de données à caractère personnel et les catégories de personnes concernées, et les obligations et les droits du responsable du traitement. Ce contrat ou cet autre acte juridique prévoit, notamment, que le sous-traitant: … »
  [3] « Le sous-traitant et toute personne agissant sous l'autorité du responsable du traitement ou sous celle du sous-traitant, qui a accès à des données à caractère personnel, ne peut pas traiter ces données, excepté sur instruction du responsable du traitement, à moins d'y être obligé par le droit de l'Union ou le droit d'un État membre. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 28, paragraphe 3 : Sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [3] RGPD — règlement (UE) 2016/679, article 29 : Traitement effectué sous l'autorité du responsable du traitement ou du sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_29
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 28, paragraphe 1 : Sous-traitant
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [4] RGPD — règlement (UE) 2016/679, article 4, définition 8 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [5] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « sur instruction documentée du responsable du traitement ».

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre, qui lie le sous-traitant à l'égard du responsable du traitement, définit l'objet et la durée du traitement, la nature et la finalité du traitement, le type de données à caractère personnel et les catégories de personnes concernées, et les obligations et les droits du responsable du traitement. Ce contrat ou cet autre acte juridique prévoit, notamment, que le sous-traitant: … »
- [3] « Le sous-traitant et toute personne agissant sous l'autorité du responsable du traitement ou sous celle du sous-traitant, qui a accès à des données à caractère personnel, ne peut pas traiter ces données, excepté sur instruction du responsable du traitement, à moins d'y être obligé par le droit de l'Union ou le droit d'un État membre. »

RÉPONSE :
Oui : il faut signer un contrat particulier, car le traitement par un sous-traitant, y compris celui qui a accès à vos fichiers, est régi par un contrat ou un autre acte juridique qui définit les obligations du sous-traitant [1]. Ce contrat doit notamment préciser que le sous-traitant ne traite les données qu’« sur instruction documentée du responsable du traitement » [1], et que toute personne agissant sous son autorité ne peut pas traiter ces données sans instruction [3].
```

</details>

Temps : recherche 2.4 s · génération 31.9 s (3022 tokens lus, 347 écrits, 26.5 tokens/s) · contrôle de pertinence 4.5 s

## q16 — Puis-je stocker les fichiers de mon association chez un hébergeur situé aux États-Unis ?

Article attendu : RGPD art. 44 ou RGPD art. 45, paragraphe 1 ou RGPD art. 46 — passage [1].

### Réponse du copilote

> Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, à condition que les données à caractère personnel soient transférées en vertu d’un mécanisme de garantie approprié, tel que des clauses types de protection des données approuvées par la Commission, ou un mécanisme de certification approuvé, avec engagement contraignant et exécutoire de respecter les droits des personnes concernées [2]. Cela suppose que les droits des personnes concernées soient effectivement opposables et que des voies de recours effectives soient disponibles [2]. Le transfert est autorisé uniquement si les conditions du présent chapitre sont respectées, notamment en ce qui concerne le niveau de protection des données [3]. Le fait que les États-Unis n’aient pas encore été reconnus comme assurant un niveau de protection adéquat par la Commission ne signifie pas que le transfert est interdit, mais il doit être fondé sur des garanties appropriées [1], [2]. Les dispositions du RGPD s'appliquent de manière à ce que le niveau de protection ne soit pas compromis [3]. Les clauses types ou les mécanismes de certification doivent être approuvés conformément aux articles 40 ou 42 du RGPD [2]. Les transferts ne peuvent avoir lieu que si les conditions du chapitre 45 ou 46 sont respectées [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. Un tel transfert ne nécessite pas d'autorisation spécifique. »
  [2] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
  [3] « Un transfert, vers un pays tiers ou à une organisation internationale, de données à caractère personnel qui font ou sont destinées à faire l'objet d'un traitement après ce transfert ne peut avoir lieu que si, sous réserve des autres dispositions du présent règlement, les conditions définies dans le présent chapitre sont respectées par le responsable du traitement et le sous-traitant, y compris pour les transferts ultérieurs de données à caractère personnel au départ du pays tiers ou de l'organisation internationale vers un autre pays tiers ou à une autre organisation internationale. »
  [4] « Toute décision d'une juridiction ou d'une autorité administrative d'un pays tiers exigeant d'un responsable du traitement ou d'un sous-traitant qu'il transfère ou divulgue des données à caractère personnel ne peut être reconnue ou rendue exécutoire de quelque manière que ce soit qu'à la condition qu'elle soit fondée sur un accord international, tel qu'un traité d'entraide judiciaire, en vigueur entre le pays tiers demandeur et l'Union ou un État membre, sans préjudice d'autres motifs de transfert en vertu du présent chapitre. »
  [5] « Lorsqu'elle évalue le caractère adéquat du niveau de protection, la Commission tient compte, en particulier, des éléments suivants: … la mise en œuvre de ladite législation, les règles en matière de protection des données, les règles professionnelles et les mesures de sécurité, y compris les règles relatives au transfert ultérieur de données à caractère personnel vers un autre pays tiers ou à une autre organisation internationale qui sont respectées dans le pays tiers ou par l'organisation internationale en question, la jurisprudence, ainsi que les droits effectifs et opposables dont bénéficient les personnes concernées et les recours administratifs et judiciaires que peuvent effectivement introduire les personnes concernées dont les données à caractère personnel sont transférées; … »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 45, paragraphe 1 : Transferts fondés sur une décision d'adéquation (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
  [2] RGPD — règlement (UE) 2016/679, article 46 : Transferts moyennant des garanties appropriées (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_46
  [3] RGPD — règlement (UE) 2016/679, article 44 : Principe général applicable aux transferts (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_44
  [4] RGPD — règlement (UE) 2016/679, article 48 : Transferts ou divulgations non autorisés par le droit de l'Union (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_48
  [5] RGPD — règlement (UE) 2016/679, article 45, paragraphe 2 : Transferts fondés sur une décision d'adéquation (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. Un tel transfert ne nécessite pas d'autorisation spécifique. »  
- [2] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »  
- [3] « Un transfert, vers un pays tiers ou à une organisation internationale, de données à caractère personnel qui font ou sont destinées à faire l'objet d'un traitement après ce transfert ne peut avoir lieu que si, sous réserve des autres dispositions du présent règlement, les conditions définies dans le présent chapitre sont respectées par le responsable du traitement et le sous-traitant, y compris pour les transferts ultérieurs de données à caractère personnel au départ du pays tiers ou de l'organisation internationale vers un autre pays tiers ou à une autre organisation internationale. »  
- [4] « Toute décision d'une juridiction ou d'une autorité administrative d'un pays tiers exigeant d'un responsable du traitement ou d'un sous-traitant qu'il transfère ou divulgue des données à caractère personnel ne peut être reconnue ou rendue exécutoire de quelque manière que ce soit qu'à la condition qu'elle soit fondée sur un accord international, tel qu'un traité d'entraide judiciaire, en vigueur entre le pays tiers demandeur et l'Union ou un État membre, sans préjudice d'autres motifs de transfert en vertu du présent chapitre. »  
- [5] « Lorsqu'elle évalue le caractère adéquat du niveau de protection, la Commission tient compte, en particulier, des éléments suivants: … la mise en œuvre de ladite législation, les règles en matière de protection des données, les règles professionnelles et les mesures de sécurité, y compris les règles relatives au transfert ultérieur de données à caractère personnel vers un autre pays tiers ou à une autre organisation internationale qui sont respectées dans le pays tiers ou par l'organisation internationale en question, la jurisprudence, ainsi que les droits effectifs et opposables dont bénéficient les personnes concernées et les recours administratifs et judiciaires que peuvent effectivement introduire les personnes concernées dont les données à caractère personnel sont transférées; … »

RÉPONSE :  
Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, à condition que les données à caractère personnel soient transférées en vertu d’un mécanisme de garantie approprié, tel que des clauses types de protection des données approuvées par la Commission, ou un mécanisme de certification approuvé, avec engagement contraignant et exécutoire de respecter les droits des personnes concernées [2]. Cela suppose que les droits des personnes concernées soient effectivement opposables et que des voies de recours effectives soient disponibles [2]. Le transfert est autorisé uniquement si les conditions du présent chapitre sont respectées, notamment en ce qui concerne le niveau de protection des données [3]. Le fait que les États-Unis n’aient pas encore été reconnus comme assurant un niveau de protection adéquat par la Commission ne signifie pas que le transfert est interdit, mais il doit être fondé sur des garanties appropriées [1], [2]. Les dispositions du RGPD s'appliquent de manière à ce que le niveau de protection ne soit pas compromis [3]. Les clauses types ou les mécanismes de certification doivent être approuvés conformément aux articles 40 ou 42 du RGPD [2]. Les transferts ne peuvent avoir lieu que si les conditions du chapitre 45 ou 46 sont respectées [3].
```

</details>

Temps : recherche 2.5 s · génération 54.4 s (2899 tokens lus, 958 écrits, 26.0 tokens/s) · contrôle de pertinence 4.0 s

## q17 — Quelles sanctions risque une petite entreprise qui ne respecte pas le RGPD ?

Article attendu : RGPD art. 83, paragraphe 4 ou RGPD art. 83, paragraphe 5 — passage [1].

### Réponse du copilote

> Une petite entreprise qui ne respecte pas le RGPD peut être sanctionnée par une amende administrative, qui peut s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [1]. Si la violation concerne des dispositions spécifiques comme les principes de base du traitement ou les droits des personnes concernées, l'amende peut atteindre jusqu'à 20 000 000 EUR ou jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [2]. En outre, l'autorité de contrôle peut ordonner une limitation temporaire ou définitive du traitement [4]. Elle peut aussi imposer une amende administrative en application de l'article 83, en fonction des caractéristiques propres à chaque cas [4]. Ces sanctions s'appliquent aux entreprises, y compris les petites entreprises, sans exception [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »
  [2] « Les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »
  [4] « imposer une amende administrative en application de l'article 83, en complément ou à la place des mesures visées au présent paragraphe, en fonction des caractéristiques propres à chaque cas; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 83, paragraphe 4 : Conditions générales pour imposer des amendes administratives (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83
  [2] RGPD — règlement (UE) 2016/679, article 83, paragraphe 5 : Conditions générales pour imposer des amendes administratives (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83
  [4] RGPD — règlement (UE) 2016/679, article 58, paragraphe 2 : Pouvoirs (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_58
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 84 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_84
  [5] RGPD — règlement (UE) 2016/679, article 57, paragraphe 1, points a) à t) : Missions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_57
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([4]) : ignoré(s).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »
- [2] « Les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »
- [4] « ordonner une limitation temporaire ou définitive, y compris une interdiction, du traitement; »
- [4] « imposer une amende administrative en application de l'article 83, en complément ou à la place des mesures visées au présent paragraphe, en fonction des caractéristiques propres à chaque cas; »

RÉPONSE :
Une petite entreprise qui ne respecte pas le RGPD peut être sanctionnée par une amende administrative, qui peut s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [1]. Si la violation concerne des dispositions spécifiques comme les principes de base du traitement ou les droits des personnes concernées, l'amende peut atteindre jusqu'à 20 000 000 EUR ou jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [2]. En outre, l'autorité de contrôle peut ordonner une limitation temporaire ou définitive du traitement [4]. Elle peut aussi imposer une amende administrative en application de l'article 83, en fonction des caractéristiques propres à chaque cas [4]. Ces sanctions s'appliquent aux entreprises, y compris les petites entreprises, sans exception [1].
```

</details>

Temps : recherche 2.4 s · génération 208.6 s (3411 tokens lus, 536 écrits, 26.1 tokens/s) · contrôle de pertinence 5.3 s

## q18 — Notre association peut-elle collecter des informations sur la santé de ses bénévoles ?

Article attendu : RGPD art. 9, paragraphe 1 ou RGPD art. 9, paragraphe 2 — absent des passages donnés au modèle.

### Réponse du copilote

> Oui : notre association peut collecter des informations sur la santé de ses bénévoles, car ces données relèvent de la catégorie des « données concernant la santé » [2]. Toutefois, ce traitement est soumis à des conditions spécifiques : les États membres peuvent imposer des limitations au traitement de ces données [3]. En l'absence de mention d'une obligation de secret professionnel ou de traitement par un professionnel de la santé, le traitement par une association ne peut être justifié que si les finalités sont déterminées, explicites et légitimes, conformément à l'article 5, paragraphe 1, point b) du RGPD [5]. Aucune obligation de secret professionnel n’est requise pour une association, donc le traitement ne peut être effectué que dans des conditions strictes, notamment en lien avec les finalités du traitement et en respectant les principes de transparence, de légitimité et de minimisation des données [5].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les données à caractère personnel visées au paragraphe 1 peuvent faire l'objet d'un traitement aux fins prévues au paragraphe 2, point h), si ces données sont traitées par un professionnel de la santé soumis à une obligation de secret professionnel conformément au droit de l'Union, au droit d'un État membre ou aux règles arrêtées par les organismes nationaux compétents, ou sous sa responsabilité, ou par une autre personne également soumise à une obligation de secret conformément au droit de l'Union ou au droit d'un État membre ou aux règles arrêtées par les organismes nationaux compétents. »
  [2] « «données concernant la santé», les données à caractère personnel relatives à la santé physique ou mentale d'une personne physique, y compris la prestation de services de soins de santé, qui révèlent des informations sur l'état de santé de cette personne; »
  [3] « Les États membres peuvent maintenir ou introduire des conditions supplémentaires, y compris des limitations, en ce qui concerne le traitement des données génétiques, des données biométriques ou des données concernant la santé. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 9, paragraphe 3 : Traitement portant sur des catégories particulières de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
  [2] RGPD — règlement (UE) 2016/679, article 4, définition 15 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [3] RGPD — règlement (UE) 2016/679, article 9, paragraphe 4 : Traitement portant sur des catégories particulières de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
  [5] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
Passages consultés mais non cités :
  [4] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
Attention : La réponse cite [5] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.
Attention : La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Aucune obligation de secret professionnel n’est requise pour une association, donc le traitement ne peut être effectué … ». Vérifiez ce point.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les données à caractère personnel visées au paragraphe 1 peuvent faire l'objet d'un traitement aux fins prévues au paragraphe 2, point h), si ces données sont traitées par un professionnel de la santé soumis à une obligation de secret professionnel conformément au droit de l'Union, au droit d'un État membre ou aux règles arrêtées par les organismes nationaux compétents, ou sous sa responsabilité, ou par une autre personne également soumise à une obligation de secret conformément au droit de l'Union ou au droit d'un État membre ou aux règles arrêtées par les organismes nationaux compétents. »  
- [2] « «données concernant la santé», les données à caractère personnel relatives à la santé physique ou mentale d'une personne physique, y compris la prestation de services de soins de santé, qui révèlent des informations sur l'état de santé de cette personne; »  
- [3] « Les États membres peuvent maintenir ou introduire des conditions supplémentaires, y compris des limitations, en ce qui concerne le traitement des données génétiques, des données biométriques ou des données concernant la santé. »

RÉPONSE :  
Oui : notre association peut collecter des informations sur la santé de ses bénévoles, car ces données relèvent de la catégorie des « données concernant la santé » [2]. Toutefois, ce traitement est soumis à des conditions spécifiques : les États membres peuvent imposer des limitations au traitement de ces données [3]. En l'absence de mention d'une obligation de secret professionnel ou de traitement par un professionnel de la santé, le traitement par une association ne peut être justifié que si les finalités sont déterminées, explicites et légitimes, conformément à l'article 5, paragraphe 1, point b) du RGPD [5]. Aucune obligation de secret professionnel n’est requise pour une association, donc le traitement ne peut être effectué que dans des conditions strictes, notamment en lien avec les finalités du traitement et en respectant les principes de transparence, de légitimité et de minimisation des données [5].
```

</details>

Temps : recherche 2.5 s · génération 36.9 s (2999 tokens lus, 495 écrits, 26.7 tokens/s) · contrôle de pertinence 5.3 s

## q19 — Qu'est-ce qu'une donnée personnelle ?

Article attendu : RGPD art. 4, définition 1 — passage [1].

### Réponse du copilote

> Une donnée personnelle est toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée») ; une personne physique est réputée être identifiable si elle peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « «données à caractère personnel», toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée»); est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 4, définition 1 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
  [3] AI Act — règlement (UE) 2024/1689, article 3, définition 50 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
  [4] RGPD — règlement (UE) 2016/679, article 4, définition 14 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [5] AI Act — règlement (UE) 2024/1689, article 3, définition 34 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « «données à caractère personnel», toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée»); est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale; »

RÉPONSE :
Une donnée personnelle est toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée») ; une personne physique est réputée être identifiable si elle peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale [1].
```

</details>

Temps : recherche 2.2 s · génération 20.6 s (2151 tokens lus, 274 écrits, 28.1 tokens/s) · contrôle de pertinence 3.7 s

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

Temps : recherche 2.4 s · génération 56708.1 s (3976 tokens lus, 218 écrits, 0.0 tokens/s) · contrôle de pertinence 11.9 s

## q21 — Comment dois-je protéger les données personnelles que nous conservons ?

Article attendu : RGPD art. 32 — passage [1].

### Réponse du copilote

> Vous devez protéger les données personnelles que vous conservez en mettant en œuvre des mesures techniques et organisationnelles appropriées, conformément à l’article 32 du RGPD, afin de garantir un niveau de sécurité adapté au risque, notamment par la pseudonymisation et le chiffrement des données, la garantie de la confidentialité, de l’intégrité, de la disponibilité et de la résilience des systèmes, la possibilité de rétablir la disponibilité des données en cas d’incident, ainsi qu’une procédure régulière de test, d’analyse et d’évaluation de ces mesures [1]. Vous devez également assurer que, par défaut, seules les données nécessaires au regard des finalités spécifiques sont traitées, en limitant la quantité, l’étendue, la durée de conservation et l’accessibilité des données [2]. Les données doivent être adéquates, pertinentes et limitées à ce qui est nécessaire, conservées pendant une durée ne dépassant pas celle nécessaire aux finalités, et traitées de façon à garantir une sécurité appropriée, notamment contre le traitement non autorisé, la perte ou la destruction accidentelle [3]. Enfin, le responsable du traitement doit mettre en œuvre des mesures pour s’assurer que le traitement est effectué conformément au RGPD, et réexaminer et actualiser ces mesures si nécessaire [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Compte tenu de l'état des connaissances, des coûts de mise en œuvre et de la nature, de la portée, du contexte et des finalités du traitement ainsi que des risques, dont le degré de probabilité et de gravité varie, pour les droits et libertés des personnes physiques, le responsable du traitement et le sous-traitant mettent en œuvre les mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque, y compris entre autres, selon les besoins: a) la pseudonymisation et le chiffrement des données à caractère personnel; b) des moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement; c) des moyens permettant de rétablir la disponibilité des données à caractère personnel et l'accès à celles-ci dans des délais appropriés en cas d'incident physique ou technique; d) une procédure visant à tester, à analyser et à évaluer régulièrement l'efficacité des mesures techniques et organisationnelles pour assurer la sécurité du traitement. »
  [2] « Le responsable du traitement met en œuvre les mesures techniques et organisationnelles appropriées pour garantir que, par défaut, seules les données à caractère personnel qui sont nécessaires au regard de chaque finalité spécifique du traitement sont traitées. Cela s'applique à la quantité de données à caractère personnel collectées, à l'étendue de leur traitement, à leur durée de conservation et à leur accessibilité. En particulier, ces mesures garantissent que, par défaut, les données à caractère personnel ne sont pas rendues accessibles à un nombre indéterminé de personnes physiques sans l'intervention de la personne physique concernée. »
  [3] « Les données à caractère personnel doivent être: … c) adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités pour lesquelles elles sont traitées (minimisation des données); … e) conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées; … f) traitées de façon à garantir une sécurité appropriée des données à caractère personnel, y compris la protection contre le traitement non autorisé ou illicite et contre la perte, la destruction ou les dégâts d'origine accidentelle, à l'aide de mesures techniques ou organisationnelles appropriées (intégrité et confidentialité); »
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
- [3] « Les données à caractère personnel doivent être: … c) adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités pour lesquelles elles sont traitées (minimisation des données); … e) conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées; … f) traitées de façon à garantir une sécurité appropriée des données à caractère personnel, y compris la protection contre le traitement non autorisé ou illicite et contre la perte, la destruction ou les dégâts d'origine accidentelle, à l'aide de mesures techniques ou organisationnelles appropriées (intégrité et confidentialité); »
- [4] « Compte tenu de la nature, de la portée, du contexte et des finalités du traitement ainsi que des risques, dont le degré de probabilité et de gravité varie, pour les droits et libertés des personnes physiques, le responsable du traitement met en œuvre des mesures techniques et organisationnelles appropriées pour s'assurer et être en mesure de démontrer que le traitement est effectué conformément au présent règlement. Ces mesures sont réexaminées et actualisées si nécessaire. »

RÉPONSE :
Vous devez protéger les données personnelles que vous conservez en mettant en œuvre des mesures techniques et organisationnelles appropriées, conformément à l’article 32 du RGPD, afin de garantir un niveau de sécurité adapté au risque, notamment par la pseudonymisation et le chiffrement des données, la garantie de la confidentialité, de l’intégrité, de la disponibilité et de la résilience des systèmes, la possibilité de rétablir la disponibilité des données en cas d’incident, ainsi qu’une procédure régulière de test, d’analyse et d’évaluation de ces mesures [1]. Vous devez également assurer que, par défaut, seules les données nécessaires au regard des finalités spécifiques sont traitées, en limitant la quantité, l’étendue, la durée de conservation et l’accessibilité des données [2]. Les données doivent être adéquates, pertinentes et limitées à ce qui est nécessaire, conservées pendant une durée ne dépassant pas celle nécessaire aux finalités, et traitées de façon à garantir une sécurité appropriée, notamment contre le traitement non autorisé, la perte ou la destruction accidentelle [3]. Enfin, le responsable du traitement doit mettre en œuvre des mesures pour s’assurer que le traitement est effectué conformément au RGPD, et réexaminer et actualiser ces mesures si nécessaire [4].
```

</details>

Temps : recherche 8.2 s · génération 49.1 s (3096 tokens lus, 1033 écrits, 34.7 tokens/s) · contrôle de pertinence 3.4 s

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
- [1] « Si le consentement de la personne concernée est donné dans le cadre d'une déclaration écrite qui concerne également d'autres questions, la demande de consentement est présentée sous une forme qui la distingue clairement de ces autres questions… »
- [2] « Le consentement éclairé est daté et documenté et une copie en est remise aux participants aux essais ou à leur représentant légal. »
- [4] « «consentement éclairé», l’expression libre, spécifique, univoque et volontaire, par un participant, de sa volonté de participer à un essai en conditions réelles particulier, après avoir été informé de tous les éléments de l’essai qui lui permettent de prendre sa décision concernant sa participation ; »

RÉPONSE :
Non, le consentement n’est pas obligatoirement donné par écrit, car le RGPD (article 4, point 11) définit le consentement comme « toute manifestation de volonté, libre, spécifique, éclairée et univoque par laquelle la personne concernée accepte, par une déclaration ou par un acte positif clair, que des données à caractère personnel la concernant fassent l'objet d'un traitement ». Cela inclut des formes orales ou autres actes positifs clairs, sauf dans les cas précisés. Cependant, dans les essais en conditions réelles prévus par l’AI Act (article 61, point 1), le consentement éclairé doit être « daté et documenté » [2], et une copie est remise aux participants [2]. Ainsi, pour les essais en conditions réelles, le consentement doit être documenté, ce qui implique une forme écrite, mais ce n’est pas une obligation générale pour tous les cas de traitement. Les passages ne précisent pas une obligation universelle de consentement écrit, mais seulement des conditions spécifiques dans certains contextes [1], [2], [4].
```

</details>

Temps : recherche 2.2 s · génération 25.6 s (2432 tokens lus, 448 écrits, 36.7 tokens/s) · contrôle de pertinence 4.2 s

## q23 — Quelles utilisations de l'intelligence artificielle sont interdites en Europe ?

Article attendu : AI Act art. 5, paragraphe 1 — passage [1].

### Réponse du copilote

> Les utilisations de l’intelligence artificielle sont interdites en Europe lorsque :  
> - on infère les émotions d’une personne physique sur le lieu de travail ou dans les établissements d’enseignement, sauf pour des raisons médicales ou de sécurité [1] ;  
> - on catégorise individuellement une personne sur la base de ses données biométriques pour déduire sa race, ses opinions politiques, son affiliation syndicale, ses convictions religieuses ou philosophiques, sa vie sexuelle ou son orientation sexuelle, sauf dans le domaine répressif [1] ;  
> - on utilise des systèmes d’identification biométrique à distance en temps réel dans des espaces accessibles au public à des fins répressives, sauf dans les cas précisément autorisés : la recherche de victimes d’enlèvement, de traite ou d’exploitation sexuelle, la prévention d’une menace imminente pour la vie ou la sécurité, ou la localisation d’une personne soupçonnée d’infraction pénale pour une enquête ou une sanction [1] ;  
> - on utilise des techniques subliminales ou manipulatrices visant à altérer le comportement d’une personne ou d’un groupe, causant un préjudice important [2] ;  
> - on exploite les vulnérabilités liées à l’âge, au handicap ou à la situation sociale ou économique pour altérer le comportement d’une personne ou d’un groupe, causant un préjudice important [2] ;  
> - on génère ou manipule des images, vidéos ou contenus audio réalistes représentant les parties intimes d’une personne identifiable ou une personne se livrant à des activités sexuellement explicites, sans son consentement libre, spécifique, éclairé, univoque et explicite [2] ;  
> - on évalue ou classe des personnes ou groupes sur la base de leur comportement social ou de leurs caractéristiques personnelles, conduisant à un traitement préjudiciable ou défavorable, notamment dans un contexte dissocié de celui de collecte des données ou lorsqu’il est injustifié ou disproportionné [2] ;  
> - on crée ou développe des bases de données de reconnaissance faciale par le moissonnage non ciblé d’images faciales sur internet ou en vidéosurveillance [2].

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
- [2] « la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui génère ou manipule des images, des vidéos, des contenus audio ou tout autre matériel similaire réalistes représentant les parties intimes d'une personne identifiable, ou une personne identifiable se livrant à des activités sexuellement explicites, sans le consentement libre, spécifique, éclairé, univoque et explicite de cette personne pour cette production ou manipulation; »
- [2] « la mise sur le marché, la mise en service ou l’utilisation de systèmes d’IA pour l’évaluation ou la classification de personnes physiques ou de groupes de personnes au cours d’une période donnée en fonction de leur comportement social ou de caractéristiques personnelles ou de personnalité connues, déduites ou prédites, la note sociale conduisant à l’une ou l’autre des situations suivantes, ou aux deux: i) le traitement préjudiciable ou défavorable de certaines personnes physiques ou de groupes de personnes dans des contextes sociaux dissociés du contexte dans lequel les données ont été générées ou collectées à l’origine; ii) le traitement préjudiciable ou défavorable de certaines personnes ou de groupes de personnes, qui est injustifié ou disproportionné par rapport à leur comportement social ou à la gravité de celui-ci; »
- [2] « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA qui créent ou développent des bases de données de reconnaissance faciale par le moissonnage non ciblé d’images faciales provenant de l’internet ou de la vidéosurveillance; »

RÉPONSE :
Les utilisations de l’intelligence artificielle sont interdites en Europe lorsque :  
- on infère les émotions d’une personne physique sur le lieu de travail ou dans les établissements d’enseignement, sauf pour des raisons médicales ou de sécurité [1] ;  
- on catégorise individuellement une personne sur la base de ses données biométriques pour déduire sa race, ses opinions politiques, son affiliation syndicale, ses convictions religieuses ou philosophiques, sa vie sexuelle ou son orientation sexuelle, sauf dans le domaine répressif [1] ;  
- on utilise des systèmes d’identification biométrique à distance en temps réel dans des espaces accessibles au public à des fins répressives, sauf dans les cas précisément autorisés : la recherche de victimes d’enlèvement, de traite ou d’exploitation sexuelle, la prévention d’une menace imminente pour la vie ou la sécurité, ou la localisation d’une personne soupçonnée d’infraction pénale pour une enquête ou une sanction [1] ;  
- on utilise des techniques subliminales ou manipulatrices visant à altérer le comportement d’une personne ou d’un groupe, causant un préjudice important [2] ;  
- on exploite les vulnérabilités liées à l’âge, au handicap ou à la situation sociale ou économique pour altérer le comportement d’une personne ou d’un groupe, causant un préjudice important [2] ;  
- on génère ou manipule des images, vidéos ou contenus audio réalistes représentant les parties intimes d’une personne identifiable ou une personne se livrant à des activités sexuellement explicites, sans son consentement libre, spécifique, éclairé, univoque et explicite [2] ;  
- on évalue ou classe des personnes ou groupes sur la base de leur comportement social ou de leurs caractéristiques personnelles, conduisant à un traitement préjudiciable ou défavorable, notamment dans un contexte dissocié de celui de collecte des données ou lorsqu’il est injustifié ou disproportionné [2] ;  
- on crée ou développe des bases de données de reconnaissance faciale par le moissonnage non ciblé d’images faciales sur internet ou en vidéosurveillance [2].
```

</details>

Temps : recherche 2.9 s · génération 61.8 s (3836 tokens lus, 1736 écrits, 31.8 tokens/s) · contrôle de pertinence 3.4 s

## q24 — Ai-je le droit d'utiliser une IA qui analyse les émotions de mes salariés ?

Article attendu : AI Act art. 5, paragraphe 1_f h — passage [2].

### Réponse du copilote

> Non, vous n’avez pas le droit d’utiliser une IA qui analyse les émotions de vos salariés sur le lieu de travail, sauf si l’utilisation est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité [2]. Cette utilisation est interdite à moins que des raisons médicales ou de sécurité ne soient justifiées. En outre, même si l’analyse est autorisée, les déployeurs doivent informer les personnes exposées du fonctionnement du système et traiter les données conformément aux règles du RGPD, mais cette obligation ne s’applique pas aux cas où l’usage est autorisé pour des fins de prévention ou de détection d’infractions pénales [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement, sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité; »
  [3] « Les déployeurs d’un système de reconnaissance des émotions ou d’un système de catégorisation biométrique informent les personnes physiques qui y sont exposées du fonctionnement du système et traitent les données à caractère personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680, selon le cas. Cette obligation ne s’applique pas aux systèmes d’IA utilisés pour la catégorisation biométrique et la reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l’Union. »

Sources citées :
  [2] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points f) à h) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [3] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 3 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points a) à e) : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [4] AI Act — règlement (UE) 2024/1689, annexe III, point 6 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [5] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [2] « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement, sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité; »
- [3] « Les déployeurs d’un système de reconnaissance des émotions ou d’un système de catégorisation biométrique informent les personnes physiques qui y sont exposées du fonctionnement du système et traitent les données à caractère personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680, selon le cas. Cette obligation ne s’applique pas aux systèmes d’IA utilisés pour la catégorisation biométrique et la reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l’Union. »

RÉPONSE :
Non, vous n’avez pas le droit d’utiliser une IA qui analyse les émotions de vos salariés sur le lieu de travail, sauf si l’utilisation est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité [2]. Cette utilisation est interdite à moins que des raisons médicales ou de sécurité ne soient justifiées. En outre, même si l’analyse est autorisée, les déployeurs doivent informer les personnes exposées du fonctionnement du système et traiter les données conformément aux règles du RGPD, mais cette obligation ne s’applique pas aux cas où l’usage est autorisé pour des fins de prévention ou de détection d’infractions pénales [3].
```

</details>

Temps : recherche 2.2 s · génération 43.4 s (3832 tokens lus, 473 écrits, 33.1 tokens/s) · contrôle de pertinence 5.1 s

## q25 — Mon logiciel est-il un « système d'IA » au sens de la loi européenne ?

Article attendu : AI Act art. 3, définition 1 — passage [2].

### Réponse du copilote

> Oui : votre logiciel est un « système d'IA » au sens de la loi européenne [2], s’il est conçu pour fonctionner à différents niveaux d’autonomie, peut s’adapter après son déploiement, et déduit à partir des entrées qu’il reçoit la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels.

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
Oui : votre logiciel est un « système d'IA » au sens de la loi européenne [2], s’il est conçu pour fonctionner à différents niveaux d’autonomie, peut s’adapter après son déploiement, et déduit à partir des entrées qu’il reçoit la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels.
```

</details>

Temps : recherche 2.2 s · génération 22.4 s (2449 tokens lus, 230 écrits, 36.6 tokens/s) · contrôle de pertinence 3.7 s

## q26 — Dois-je indiquer qu'une image publiée sur notre site a été créée par une IA ?

Article attendu : AI Act art. 50, paragraphe 4 — passage [1].

### Réponse du copilote

> Oui : vous devez indiquer qu’une image publiée sur votre site a été créée par une IA, sauf si l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière [1], ou si l’image fait partie d’une œuvre manifestement artistique, créative, satirique, fictif ou analogue, dans ce cas la transparence se limite à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre [1]. De plus, cette obligation ne s’applique pas si le système d’IA ne modifie pas de manière substantielle les données d’entrée fournies par vous ou leur sémantique, ou si son utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière [2].

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
Oui : vous devez indiquer qu’une image publiée sur votre site a été créée par une IA, sauf si l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière [1], ou si l’image fait partie d’une œuvre manifestement artistique, créative, satirique, fictif ou analogue, dans ce cas la transparence se limite à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre [1]. De plus, cette obligation ne s’applique pas si le système d’IA ne modifie pas de manière substantielle les données d’entrée fournies par vous ou leur sémantique, ou si son utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière [2].
```

</details>

Temps : recherche 2.2 s · génération 35.6 s (2704 tokens lus, 642 écrits, 35.5 tokens/s) · contrôle de pertinence 4.4 s

## q27 — Quelles amendes prévoit le règlement européen sur l'intelligence artificielle ?

Article attendu : AI Act art. 99, paragraphe 4 ou AI Act art. 99, paragraphe 6 — absent des passages donnés au modèle.

### Réponse du copilote

> Le règlement européen sur l’intelligence artificielle (AI Act) prévoit plusieurs types d’amendes. Pour le non-respect des interdictions de pratiques en matière d’IA (article 5), les amendes peuvent aller jusqu’à 35 000 000 EUR ou, pour une entreprise, jusqu’à 7 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu [2]. En cas de fourniture d’informations inexactes, incomplètes ou trompeuses aux organismes notifiés ou aux autorités nationales, l’amende peut aller jusqu’à 7 500 000 EUR ou, pour une entreprise, jusqu’à 1 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu [3]. Pour les fournisseurs de modèles d’IA à usage général, les amendes ne dépassent pas 3 % de leur chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, ou 15 000 000 EUR, le montant le plus élevé étant retenu [4]. En outre, pour les institutions, organes ou organismes de l’Union, le non-respect de l’interdiction des pratiques en matière d’IA peut entraîner une amende allant jusqu’à 1 500 000 EUR, tandis que la non-conformité avec d’autres exigences du règlement peut entraîner une amende allant jusqu’à 750 000 EUR [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le Contrôleur européen de la protection des données peut imposer des amendes administratives aux institutions, organes et organismes de l’Union relevant du champ d’application du présent règlement. … le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’une amende administrative pouvant aller jusqu’à 1 500 000 EUR. … La non-conformité du système d’IA avec les exigences ou obligations au titre du présent règlement, autres que celles énoncées à l’article 5, fait l’objet d’une amende administrative pouvant aller jusqu’à 750 000 EUR. »
  [2] « Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’amendes administratives pouvant aller jusqu’à 35 000 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 7 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu. »
  [3] « La fourniture d’informations inexactes, incomplètes ou trompeuses aux organismes notifiés ou aux autorités nationales compétentes en réponse à une demande fait l’objet d’une amende administrative pouvant aller jusqu’à 7 500 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 1 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu. »
  [4] « La Commission peut infliger aux fournisseurs de modèles d’IA à usage général des amendes n’excédant pas 3 % de leur chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, ou 15 000 000 EUR, le montant le plus élevé étant retenu, lorsque la Commission constate que le fournisseur, de manière délibérée ou par négligence: a) a enfreint les dispositions pertinentes du présent règlement; b) n’a pas donné suite à une demande de document ou d’informations au titre de l’article 91, ou a fourni des informations inexactes, incomplètes ou trompeuses; c) ne s’est pas conformé à une mesure demandée au titre de l’article 93; d) n’a pas donné à la Commission accès au modèle d’IA à usage général ou au modèle d’IA à usage général présentant un risque systémique en vue de procéder à une évaluation conformément à l’article 92. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 100 : Amendes administratives imposées aux institutions, organes et organismes de l’Union (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_100
  [2] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 3 : Sanctions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [3] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 5 : Sanctions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [4] AI Act — règlement (UE) 2024/1689, article 101 : Amendes applicables aux fournisseurs de modèles d’IA à usage général (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_101
Passages consultés mais non cités :
  [5] RGPD — règlement (UE) 2016/679, article 83, paragraphe 5 : Conditions générales pour imposer des amendes administratives
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le Contrôleur européen de la protection des données peut imposer des amendes administratives aux institutions, organes et organismes de l’Union relevant du champ d’application du présent règlement. … le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’une amende administrative pouvant aller jusqu’à 1 500 000 EUR. … La non-conformité du système d’IA avec les exigences ou obligations au titre du présent règlement, autres que celles énoncées à l’article 5, fait l’objet d’une amende administrative pouvant aller jusqu’à 750 000 EUR. »
- [2] « Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’amendes administratives pouvant aller jusqu’à 35 000 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 7 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu. »
- [3] « La fourniture d’informations inexactes, incomplètes ou trompeuses aux organismes notifiés ou aux autorités nationales compétentes en réponse à une demande fait l’objet d’une amende administrative pouvant aller jusqu’à 7 500 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 1 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu. »
- [4] « La Commission peut infliger aux fournisseurs de modèles d’IA à usage général des amendes n’excédant pas 3 % de leur chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, ou 15 000 000 EUR, le montant le plus élevé étant retenu, lorsque la Commission constate que le fournisseur, de manière délibérée ou par négligence: a) a enfreint les dispositions pertinentes du présent règlement; b) n’a pas donné suite à une demande de document ou d’informations au titre de l’article 91, ou a fourni des informations inexactes, incomplètes ou trompeuses; c) ne s’est pas conformé à une mesure demandée au titre de l’article 93; d) n’a pas donné à la Commission accès au modèle d’IA à usage général ou au modèle d’IA à usage général présentant un risque systémique en vue de procéder à une évaluation conformément à l’article 92. »

RÉPONSE :
Le règlement européen sur l’intelligence artificielle (AI Act) prévoit plusieurs types d’amendes. Pour le non-respect des interdictions de pratiques en matière d’IA (article 5), les amendes peuvent aller jusqu’à 35 000 000 EUR ou, pour une entreprise, jusqu’à 7 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu [2]. En cas de fourniture d’informations inexactes, incomplètes ou trompeuses aux organismes notifiés ou aux autorités nationales, l’amende peut aller jusqu’à 7 500 000 EUR ou, pour une entreprise, jusqu’à 1 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu [3]. Pour les fournisseurs de modèles d’IA à usage général, les amendes ne dépassent pas 3 % de leur chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, ou 15 000 000 EUR, le montant le plus élevé étant retenu [4]. En outre, pour les institutions, organes ou organismes de l’Union, le non-respect de l’interdiction des pratiques en matière d’IA peut entraîner une amende allant jusqu’à 1 500 000 EUR, tandis que la non-conformité avec d’autres exigences du règlement peut entraîner une amende allant jusqu’à 750 000 EUR [1].
```

</details>

Temps : recherche 2.1 s · génération 38.5 s (3392 tokens lus, 1045 écrits, 33.1 tokens/s) · contrôle de pertinence 5.1 s

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
RÉPONSE : Les textes trouvés ne traitent pas de la création d'une association en préfecture. Ils concernent uniquement des obligations relatives à l'évaluation de la conformité des organismes, aux autorités notifiantes et aux procédures de notification dans le cadre de la législation sur les systèmes d'IA (AI Act) et du RGPD, et ne portent pas sur la création d'associations ou les démarches administratives en préfecture.
```

</details>

Temps : recherche 2.2 s · génération 31.0 s (3970 tokens lus, 113 écrits, 33.1 tokens/s)

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
RÉPONSE : Les textes trouvés ne traitent pas de ce point.
```

</details>

Temps : recherche 2.8 s · génération 20.4 s (3097 tokens lus, 26 écrits, 36.5 tokens/s)

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
  [2] RGPD — règlement (UE) 2016/679, article 4, définition 7 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [3] RGPD — règlement (UE) 2016/679, article 26 : Responsables conjoints du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_26
  [4] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30
  [5] RGPD — règlement (UE) 2016/679, article 6, paragraphe 2 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
aucun

RÉPONSE :  
Les textes trouvés ne traitent pas de la rédaction des statuts d'une association. Ils énoncent des obligations relatives aux codes de conduite, aux responsables du traitement, aux registres des activités de traitement, aux transferts de données ou à l'exercice des droits des personnes concernées, mais ne prévoient aucune règle sur la rédaction des statuts.
```

</details>

Temps : recherche 2.2 s · génération 21.0 s (3004 tokens lus, 99 écrits, 35.7 tokens/s)
