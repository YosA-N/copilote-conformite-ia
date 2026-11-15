# Réponses du copilote — v4_big_gptoss

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 15/11/2026 à 17:17 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `openai/gpt-oss-120b` via l'API compatible OpenAI https://api.groq.com/openai/v1 (expérience de la séance 7, questions de test seulement ; modèle tel que servi par l'API à la date ci-dessus) — température 0.1, raisonnement : « low » (reasoning_effort), passages calculés pour un contexte de 8192 tokens comme en local, 2000 tokens au plus par réponse (raisonnement compris) ; le juge est le même modèle
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_v0.jsonl` (10), `eval/questions_offtopic_v0.jsonl` (0 + 2 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q01 | Dois-je désigner un DPO ? | 2/2 | non | — | 4 s |
| q02 | Dois-je tenir un registre des traitements ? | 2/2 | non | — | 4 s |
| q03 | Combien de temps puis-je garder les données de mes clients ou adhérents ? | 2/2 | non | — | 4 s |
| q04 | Que dois-je mettre dans la mention d'information d'un formulaire ? | 4/6 | non | 2 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1], [1]) : ignoré(s). | 5 s |
| q05 | Une personne demande l'accès à ses données : quel délai pour répondre ? | 1/2 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([4]) : ignoré(s).; La réponse cite [4] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations. | 4 s |
| q06 | J'ai eu une fuite de données : que faire, et en combien de temps ? | 3/3 | non | — | 4 s |
| q07 | Quand faut-il faire une analyse d'impact (AIPD) ? | 2/2 | non | — | 5 s |
| q08 | Mon chatbot doit-il dire aux clients qu'il est une IA ? | 1/1 | non | La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui, votre chatbot doit informer les clients qu’ils interagissent avec un système d’IA, sauf si, compte tenu du … ». Vérifiez qui est concerné. | 4 s |
| q09 | Puis-je utiliser une IA pour trier des CV ? | 3/3 | non | La réponse met entre « » un texte introuvable dans les extraits vérifiés : « destiné à être utilisé pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des … ». | 5 s |
| q10 | Mes salariés ou bénévoles utilisent une IA générative : ai-je des obligations ? | 5/5 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 5 s |
| h01 | Quel est le taux de TVA en France ? | 0/0 | oui | — | 3 s |
| h02 | Comment faire une déclaration d'impôts ? | 0/0 | oui | — | 3 s |

## q01 — Dois-je désigner un DPO ?

Article attendu : RGPD art. 37 — passage [1].

### Réponse du copilote

> Vous devez désigner un DPO (délégué à la protection des données) si votre activité correspond à l’une des situations énumérées au paragraphe 1 de l’article 37 : traitement réalisé par une autorité ou un organisme public, suivi régulier et systématique à grande échelle des personnes concernées, ou traitement à grande échelle de catégories particulières de données sensibles ou de données pénales [1].  
> Dans les autres cas, la désignation n’est pas obligatoire, mais vous pouvez la faire volontairement, ou elle peut être imposée si le droit de l’Union ou le droit national l’exige, comme le précise le deuxième extrait [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le responsable du traitement et le sous-traitant désignent en tout état de cause un délégué à la protection des données lorsque: a) le traitement est effectué par une autorité publique ou un organisme public, à l'exception des juridictions agissant dans l'exercice de leur fonction juridictionnelle; b) les activités de base du responsable du traitement ou du sous-traitant consistent en des opérations de traitement qui, du fait de leur nature, de leur portée et/ou de leurs finalités, exigent un suivi régulier et systématique à grande échelle des personnes concernées; ou c) les activités de base du responsable du traitement ou du sous-traitant consistent en un traitement à grande échelle de catégories particulières de données visées à l’article 9 ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l’article 10. »
  [1] « Dans les cas autres que ceux visés au paragraphe 1, le responsable du traitement ou le sous-traitant ou les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent désigner ou, si le droit de l'Union ou le droit d'un État membre l'exige, sont tenus de désigner un délégué à la protection des données. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 37 : Désignation du délégué à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_37
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 38 : Fonction du délégué à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_38
  [3] RGPD — règlement (UE) 2016/679, article 39 : Missions du délégué à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_39
  [4] RGPD — règlement (UE) 2016/679, article 35, paragraphe 2 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [5] RGPD — règlement (UE) 2016/679, article 35, paragraphe 1 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
**EXTRAITS :**  
- [1] « Le responsable du traitement et le sous-traitant désignent en tout état de cause un délégué à la protection des données lorsque: a) le traitement est effectué par une autorité publique ou un organisme public, à l'exception des juridictions agissant dans l'exercice de leur fonction juridictionnelle; b) les activités de base du responsable du traitement ou du sous-traitant consistent en des opérations de traitement qui, du fait de leur nature, de leur portée et/ou de leurs finalités, exigent un suivi régulier et systématique à grande échelle des personnes concernées; ou c) les activités de base du responsable du traitement ou du sous-traitant consistent en un traitement à grande échelle de catégories particulières de données visées à l’article 9 ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l’article 10. »  
- [1] « Dans les cas autres que ceux visés au paragraphe 1, le responsable du traitement ou le sous-traitant ou les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent désigner ou, si le droit de l'Union ou le droit d'un État membre l'exige, sont tenus de désigner un délégué à la protection des données. »  

**RÉPONSE :**  
Vous devez désigner un DPO (délégué à la protection des données) si votre activité correspond à l’une des situations énumérées au paragraphe 1 de l’article 37 : traitement réalisé par une autorité ou un organisme public, suivi régulier et systématique à grande échelle des personnes concernées, ou traitement à grande échelle de catégories particulières de données sensibles ou de données pénales [1].  
Dans les autres cas, la désignation n’est pas obligatoire, mais vous pouvez la faire volontairement, ou elle peut être imposée si le droit de l’Union ou le droit national l’exige, comme le précise le deuxième extrait [1].
```

</details>

<details><summary>Raisonnement renvoyé par l'API (32 mots, non affiché à l'utilisateur, compté dans les tokens écrits)</summary>

```text
We need extracts that state when designation required. From [1] paragraph 1 lists cases a,b,c. Also 4 mentions can be required. So answer: Yes if any of those conditions apply. Provide extracts.
```

</details>

Temps : recherche 2.5 s · génération 1.5 s (2589 tokens lus, 492 écrits, raisonnement ≈ 32 mots, 481.2 tokens/s) · contrôle de pertinence 0.3 s

## q02 — Dois-je tenir un registre des traitements ?

Article attendu : RGPD art. 30 — passage [1].

### Réponse du copilote

> Oui, en tant que responsable du traitement, vous devez tenir un registre des activités de traitement que vous effectuez [1]. Cette obligation ne s’applique pas si votre organisation compte moins de 250 employés, à moins que le traitement présente un risque pour les droits et libertés des personnes, ne soit pas occasionnel ou porte sur des catégories particulières de données sensibles [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Chaque responsable du traitement … tiennent un registre des activités de traitement effectuées sous leur responsabilité. »
  [1] « Les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données … »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 4, définition 2 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [3] RGPD — règlement (UE) 2016/679, article 24 : Responsabilité du responsable du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_24
  [4] RGPD — règlement (UE) 2016/679, article 6, paragraphe 1 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
  [5] RGPD — règlement (UE) 2016/679, article 9, paragraphe 3 : Traitement portant sur des catégories particulières de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Chaque responsable du traitement … tiennent un registre des activités de traitement effectuées sous leur responsabilité. »
- [1] « Les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données … »  

RÉPONSE :
Oui, en tant que responsable du traitement, vous devez tenir un registre des activités de traitement que vous effectuez [1]. Cette obligation ne s’applique pas si votre organisation compte moins de 250 employés, à moins que le traitement présente un risque pour les droits et libertés des personnes, ne soit pas occasionnel ou porte sur des catégories particulières de données sensibles [1].
```

</details>

<details><summary>Raisonnement renvoyé par l'API (27 mots, non affiché à l'utilisateur, compté dans les tokens écrits)</summary>

```text
We need extracts showing obligation. From [1] article 30 paragraph1 says each responsible must keep a register. Also exception paragraph5. So answer yes unless exception. Provide extracts.
```

</details>

Temps : recherche 2.2 s · génération 0.9 s (2588 tokens lus, 248 écrits, raisonnement ≈ 27 mots, 481.2 tokens/s) · contrôle de pertinence 0.6 s

## q03 — Combien de temps puis-je garder les données de mes clients ou adhérents ?

Article attendu : RGPD art. 5 — passage [5].

### Réponse du copilote

> Vous devez conserver les données de vos clients ou adhérents « pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées » [5]. Elles ne peuvent être conservées plus longtemps que nécessaire, sauf si vous les utilisez « exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques » et que vous appliquez les mesures techniques et organisationnelles appropriées pour garantir les droits des personnes concernées [5].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [5] « les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée (limitation de la conservation) »
  [5] « conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées »

Sources citées :
  [5] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 4, définition 3 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [2] RGPD — règlement (UE) 2016/679, article 18 : Droit à la limitation du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_18
  [3] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [4] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [5] « les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée (limitation de la conservation) »
- [5] « conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées » 

RÉPONSE :
Vous devez conserver les données de vos clients ou adhérents « pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées » [5]. Elles ne peuvent être conservées plus longtemps que nécessaire, sauf si vous les utilisez « exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques » et que vous appliquez les mesures techniques et organisationnelles appropriées pour garantir les droits des personnes concernées [5].
```

</details>

<details><summary>Raisonnement renvoyé par l'API (38 mots, non affiché à l'utilisateur, compté dans les tokens écrits)</summary>

```text
We need extracts about retention. From [5] article5 e) gives duration: "conservées ... pendant une durée n'excédant pas celle nécessaire ... ; ... peuvent être conservées pour des durées plus longues ...". Use that. No other. So answer.
```

</details>

Temps : recherche 2.2 s · génération 1.1 s (2370 tokens lus, 329 écrits, raisonnement ≈ 38 mots, 473.4 tokens/s) · contrôle de pertinence 0.6 s · attente des limites de l'API 8 s (non comptée)

## q04 — Que dois-je mettre dans la mention d'information d'un formulaire ?

Article attendu : RGPD art. 13 — passage [1].

### Réponse du copilote

> Dans la mention d’information d’un formulaire, vous devez indiquer, en tant que responsable du traitement, : votre identité et vos coordonnées (ou celles de votre représentant) [1], les coordonnées du délégué à la protection des données le cas échéant [1], les finalités du traitement ainsi que la base juridique qui le fonde [1], les destinataires ou catégories de destinataires des données [1], la durée de conservation prévue ou les critères permettant de la déterminer [1], et les droits dont disposent les personnes concernées (droit d’accès, de rectification, d’effacement, de limitation, d’opposition et de portabilité) [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « … b) le cas échéant, les coordonnées du délégué à la protection des données; »
  [1] « … c) les finalités du traitement auquel sont destinées les données à caractère personnel ainsi que la base juridique du traitement; »
  [1] « … a) la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; »
  [1] « … b) l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ou du droit de s'opposer au traitement et du droit à la portabilité des données; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [3] RGPD — règlement (UE) 2016/679, article 12, paragraphe 6 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [4] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
Attention : 2 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1], [1]) : ignoré(s).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
**EXTRAITS :**  
- [1] « Lorsque des données à caractère personnel relatives à une personne concernée sont collectées auprès de cette personne, le responsable du traitement lui fournit, au moment où les données en question sont obtenues, toutes les informations suivantes : a) l'identité et les coordonnées du responsable du traitement et, le cas échéant, du représentant du responsable du traitement »  
- [1] « … b) le cas échéant, les coordonnées du délégué à la protection des données; »  
- [1] « … c) les finalités du traitement auquel sont destinées les données à caractère personnel ainsi que la base juridique du traitement; »  
- [1] « … d) les destinataires ou les catégories de destinataires des données à caractère personnel, s'ils existent; »  
- [1] « … a) la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; »  
- [1] « … b) l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ou du droit de s'opposer au traitement et du droit à la portabilité des données; »  

**RÉPONSE :**  
Dans la mention d’information d’un formulaire, vous devez indiquer, en tant que responsable du traitement, : votre identité et vos coordonnées (ou celles de votre représentant) [1], les coordonnées du délégué à la protection des données le cas échéant [1], les finalités du traitement ainsi que la base juridique qui le fonde [1], les destinataires ou catégories de destinataires des données [1], la durée de conservation prévue ou les critères permettant de la déterminer [1], et les droits dont disposent les personnes concernées (droit d’accès, de rectification, d’effacement, de limitation, d’opposition et de portabilité) [1].
```

</details>

<details><summary>Raisonnement renvoyé par l'API (17 mots, non affiché à l'utilisateur, compté dans les tokens écrits)</summary>

```text
We need extract relevant parts about info to provide in form. Use article13 and 14. Provide extracts.
```

</details>

Temps : recherche 2.2 s · génération 1.7 s (2918 tokens lus, 461 écrits, raisonnement ≈ 17 mots, 483.6 tokens/s) · contrôle de pertinence 0.6 s · attente des limites de l'API 23 s (non comptée)

## q05 — Une personne demande l'accès à ses données : quel délai pour répondre ?

Article attendu : RGPD art. 12, paragraphe 3 — passage [1].

### Réponse du copilote

> Le responsable du traitement doit répondre à une demande d’accès dans un délai d’un mois à compter de la réception de la demande [1]. Si la demande est complexe ou très nombreuse, ce délai peut être prolongé de deux mois, mais le responsable doit alors informer la personne concernée de la prolongation et des raisons du report dans un délai d’un mois à compter de la réception de la demande [1]. En cas de non‑réponse, le responsable doit tout de même informer la personne des motifs de son inaction dans le même délai d’un mois [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « le responsable du traitement fournit à la personne concernée des informations … dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [4] RGPD — règlement (UE) 2016/679, article 12, paragraphe 4 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [3] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 3 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([4]) : ignoré(s).
Attention : La réponse cite [4] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « le responsable du traitement fournit à la personne concernée des informations … dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. »
- [4] « il informe celle‑ci … au plus tard dans un délai d'un mois à compter de la réception de la demande des motifs de son inaction … »

RÉPONSE :
Le responsable du traitement doit répondre à une demande d’accès dans un délai d’un mois à compter de la réception de la demande [1]. Si la demande est complexe ou très nombreuse, ce délai peut être prolongé de deux mois, mais le responsable doit alors informer la personne concernée de la prolongation et des raisons du report dans un délai d’un mois à compter de la réception de la demande [1]. En cas de non‑réponse, le responsable doit tout de même informer la personne des motifs de son inaction dans le même délai d’un mois [4].
```

</details>

<details><summary>Raisonnement renvoyé par l'API (45 mots, non affiché à l'utilisateur, compté dans les tokens écrits)</summary>

```text
We need extracts about deadline. From [1] says deadline one month, can extend two months. Also [3] mentions copy provided, but deadline? Not. So use [1]. Also maybe [4] about no response deadline one month. But question about access request deadline. Use [1]. Provide answer.
```

</details>

Temps : recherche 2.2 s · génération 1.3 s (2263 tokens lus, 338 écrits, raisonnement ≈ 45 mots, 478.5 tokens/s) · contrôle de pertinence 0.4 s · attente des limites de l'API 20 s (non comptée)

## q06 — J'ai eu une fuite de données : que faire, et en combien de temps ?

Article attendu : RGPD art. 33 ou RGPD art. 34 — passage [1].

### Réponse du copilote

> Vous devez notifier la violation à l’autorité de contrôle dans les meilleurs délais et, si possible, **au plus tard 72 heures** après en avoir pris connaissance, sauf si la fuite ne risque pas d’affecter les droits et libertés des personnes concernées [1]. Si vous dépassez ce délai de 72 heures, vous devez expliquer les raisons du retard dans la notification [1]. Par ailleurs, vous devez **documenter** la violation en consignant les faits, les effets et les mesures correctives que vous avez prises [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation … dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. »
  [1] « Lorsque la notification à l’autorité de contrôle n’a pas lieu dans les 72 heures, elle est accompagnée des motifs du retard. »
  [1] « Le responsable du traitement documente toute violation de données à caractère personnel, en indiquant les faits concernant la violation des données à caractère personnel, ses effets et les mesures prises pour y remédier. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 33 : Notification à l'autorité de contrôle d'une violation de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_33
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 34 : Communication à la personne concernée d'une violation de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_34
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 12 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [4] RGPD — règlement (UE) 2016/679, article 17 : Droit à l'effacement («droit à l'oubli»)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_17
  [5] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation … dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. »
- [1] « Lorsque la notification à l’autorité de contrôle n’a pas lieu dans les 72 heures, elle est accompagnée des motifs du retard. »
- [1] « Le responsable du traitement documente toute violation de données à caractère personnel, en indiquant les faits concernant la violation des données à caractère personnel, ses effets et les mesures prises pour y remédier. » 

RÉPONSE :
Vous devez notifier la violation à l’autorité de contrôle dans les meilleurs délais et, si possible, **au plus tard 72 heures** après en avoir pris connaissance, sauf si la fuite ne risque pas d’affecter les droits et libertés des personnes concernées [1]. Si vous dépassez ce délai de 72 heures, vous devez expliquer les raisons du retard dans la notification [1]. Par ailleurs, vous devez **documenter** la violation en consignant les faits, les effets et les mesures correctives que vous avez prises [1].
```

</details>

<details><summary>Raisonnement renvoyé par l'API (15 mots, non affiché à l'utilisateur, compté dans les tokens écrits)</summary>

```text
Need extract about notification timeline 72h. Use [1] point 1. Also maybe documentation. Provide answer.
```

</details>

Temps : recherche 2.2 s · génération 1.5 s (3305 tokens lus, 318 écrits, raisonnement ≈ 15 mots, 472.1 tokens/s) · contrôle de pertinence 0.5 s · attente des limites de l'API 21 s (non comptée)

## q07 — Quand faut-il faire une analyse d'impact (AIPD) ?

Article attendu : RGPD art. 35, paragraphe 1 ou RGPD art. 35, paragraphe 3 — passage [1].

### Réponse du copilote

> Vous devez réaliser une analyse d’impact relative à la protection des données (AIPD) dès que le traitement envisagé, compte tenu de sa nature, portée, contexte et finalités, est susceptible d’engendrer un risque élevé pour les droits et libertés des personnes physiques, et ce **avant** de commencer le traitement [2]. De plus, l’AIPD est obligatoirement requise dans les cas suivants : (a) lorsqu’il s’agit d’une évaluation systématique et approfondie d’aspects personnels fondée sur un traitement automatisé, y compris le profilage, entraînant des décisions ayant des effets juridiques ou des impacts significatifs ; (b) lorsqu’il y a un traitement à grande échelle de catégories particulières de données sensibles ou de données relatives à des condamnations pénales ; ou (c) lorsqu’il s’agit d’une surveillance systématique à grande échelle d’une zone accessible au public [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « Lorsqu'un type de traitement, en particulier par le recours à de nouvelles technologies, et compte tenu de la nature, de la portée, du contexte et des finalités du traitement, est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, le responsable du traitement effectue, avant le traitement, une analyse de l'impact des opérations de traitement envisagées sur la protection des données à caractère personnel. »
  [1] « L'analyse d'impact relative à la protection des données … est, en particulier, requise dans les cas suivants: a) l'évaluation systématique et approfondie d'aspects personnels … fondée sur un traitement automatisé, y compris le profilage, … ; b) le traitement à grande échelle de catégories particulières de données … ; c) la surveillance systématique à grande échelle d'une zone accessible au public. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 35, paragraphe 3 : Analyse d'impact relative à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [2] RGPD — règlement (UE) 2016/679, article 35, paragraphe 1 : Analyse d'impact relative à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 35, paragraphe 11 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [4] AI Act — règlement (UE) 2024/1689, article 27 : Analyse d’impact des systèmes d’IA à haut risque sur les droits fondamentaux
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_27
  [5] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 9 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [2] « Lorsqu'un type de traitement, en particulier par le recours à de nouvelles technologies, et compte tenu de la nature, de la portée, du contexte et des finalités du traitement, est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, le responsable du traitement effectue, avant le traitement, une analyse de l'impact des opérations de traitement envisagées sur la protection des données à caractère personnel. »
- [1] « L'analyse d'impact relative à la protection des données … est, en particulier, requise dans les cas suivants: a) l'évaluation systématique et approfondie d'aspects personnels … fondée sur un traitement automatisé, y compris le profilage, … ; b) le traitement à grande échelle de catégories particulières de données … ; c) la surveillance systématique à grande échelle d'une zone accessible au public. »

RÉPONSE :
Vous devez réaliser une analyse d’impact relative à la protection des données (AIPD) dès que le traitement envisagé, compte tenu de sa nature, portée, contexte et finalités, est susceptible d’engendrer un risque élevé pour les droits et libertés des personnes physiques, et ce **avant** de commencer le traitement [2]. De plus, l’AIPD est obligatoirement requise dans les cas suivants : (a) lorsqu’il s’agit d’une évaluation systématique et approfondie d’aspects personnels fondée sur un traitement automatisé, y compris le profilage, entraînant des décisions ayant des effets juridiques ou des impacts significatifs ; (b) lorsqu’il y a un traitement à grande échelle de catégories particulières de données sensibles ou de données relatives à des condamnations pénales ; ou (c) lorsqu’il s’agit d’une surveillance systématique à grande échelle d’une zone accessible au public [1].
```

</details>

<details><summary>Raisonnement renvoyé par l'API (46 mots, non affiché à l'utilisateur, compté dans les tokens écrits)</summary>

```text
We need extracts that state when to do AIPD. From RGPD article 35 passages [1] and [2] give conditions. Also AI Act maybe but question about AIPD (analyse d'impact protection des données). Use [2] for risk high before processing, and [1] for specific cases. Provide answer.
```

</details>

Temps : recherche 2.2 s · génération 1.8 s (2461 tokens lus, 474 écrits, raisonnement ≈ 46 mots, 376.2 tokens/s) · contrôle de pertinence 0.5 s · attente des limites de l'API 13 s (non comptée)

## q08 — Mon chatbot doit-il dire aux clients qu'il est une IA ?

Article attendu : AI Act art. 50, paragraphe 1 — passage [1].

### Réponse du copilote

> Oui, votre chatbot doit informer les clients qu’ils interagissent avec un système d’IA, sauf si, compte tenu du contexte et des circonstances, il est évident pour une personne normalement informée et raisonnablement attentive que l’interaction se fait avec une IA [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 2 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [3] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14
  [4] AI Act — règlement (UE) 2024/1689, annexe III, point 5 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [5] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points a) à e) : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
Attention : La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui, votre chatbot doit informer les clients qu’ils interagissent avec un système d’IA, sauf si, compte tenu du … ». Vérifiez qui est concerné.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
**EXTRAITS :**  
- [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »

**RÉPONSE :**  
Oui, votre chatbot doit informer les clients qu’ils interagissent avec un système d’IA, sauf si, compte tenu du contexte et des circonstances, il est évident pour une personne normalement informée et raisonnablement attentive que l’interaction se fait avec une IA [1].
```

</details>

<details><summary>Raisonnement renvoyé par l'API (28 mots, non affiché à l'utilisateur, compté dans les tokens écrits)</summary>

```text
We need extract relevant. From [1] about informing users interacting with IA unless obvious. That's answer. Also maybe [2] not about chatbot. Use [1]. Provide extracts and response.
```

</details>

Temps : recherche 2.2 s · génération 1.5 s (3472 tokens lus, 214 écrits, raisonnement ≈ 28 mots, 482.6 tokens/s) · contrôle de pertinence 0.7 s · attente des limites de l'API 23 s (non comptée)

## q09 — Puis-je utiliser une IA pour trier des CV ?

Article attendu : AI Act annexe III, point 4 ou AI Act art. 26 — passage [3].

### Réponse du copilote

> Oui, vous pouvez utiliser une IA pour trier des CV, mais le système concerné est classé comme IA à haut risque au sens de l'AI Act, car il « destiné à être utilisé pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats » [3].  
>
> En conséquence, vous devez mettre en place des mesures de contrôle proportionnées aux risques et au contexte d’utilisation, soit intégrées par le fournisseur avant la mise sur le marché, soit mises en œuvre par vous, le déployeur [1].  
>
> De plus, vous devez garantir que les personnes chargées du contrôle humain comprennent les capacités et limites du système, peuvent surveiller son fonctionnement, détecter les anomalies, décider de ne pas l’utiliser ou d’en inverser les sorties, et disposer d’un moyen d’interruption sécurisé (bouton d’arrêt) [1].  
>
> Ces obligations s’appliquent à vous, en tant que déployeur du système d’IA à haut risque.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats »
  [1] « Les mesures de contrôle sont proportionnées aux risques, au niveau d’autonomie et au contexte d’utilisation du système d’IA à haut risque, et sont assurées au moyen d’un ou des deux types de mesures suivants: a) des mesures identifiées et, lorsque cela est techniquement possible, intégrées par le fournisseur dans le système d’IA à haut risque avant la mise sur le marché ou la mise en service de ce dernier; b) des mesures identifiées par le fournisseur avant la mise sur le marché ou la mise en service du système d’IA à haut risque et qui se prêtent à une mise en œuvre par le déployeur. »
  [1] « aux fins de la mise en œuvre des dispositions des paragraphes 1, 2 et 3, le système d’IA à haut risque est fourni au déployeur de telle manière que les personnes physiques chargées d’effectuer un contrôle humain, … ont la possibilité: a) de comprendre correctement les capacités et les limites pertinentes du système d’IA à haut risque et d’être en mesure de surveiller correctement son fonctionnement, y compris en vue de détecter et de traiter les anomalies, les dysfonctionnements et les performances inattendues; … d) de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou inverser la sortie du système d’IA à haut risque; … e) d’intervenir dans le fonctionnement du système d’IA à haut risque ou d’interrompre le système au moyen d’un bouton d’arrêt ou d’une procédure similaire permettant au système de s’arrêter de manière sécurisée. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14
  [3] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 4 bis : Traitement de catégories particulières de données à caractère personnel à des fins de détection et de correction des biais
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_4a
  [4] AI Act — règlement (UE) 2024/1689, article 59, paragraphe 1, point j) : Traitement ultérieur de données à caractère personnel en vue du développement de certains systèmes d’IA dans l’intérêt public dans le cadre du bac à sable réglementaire de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_59
  [5] AI Act — règlement (UE) 2024/1689, article 59, paragraphe 3 : Traitement ultérieur de données à caractère personnel en vue du développement de certains systèmes d’IA dans l’intérêt public dans le cadre du bac à sable réglementaire de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_59
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « destiné à être utilisé pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des … ».

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [3] « systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats ».
- [1] « Les mesures de contrôle sont proportionnées aux risques, au niveau d’autonomie et au contexte d’utilisation du système d’IA à haut risque, et sont assurées au moyen d’un ou des deux types de mesures suivants: a) des mesures identifiées et, lorsque cela est techniquement possible, intégrées par le fournisseur dans le système d’IA à haut risque avant la mise sur le marché ou la mise en service de ce dernier; b) des mesures identifiées par le fournisseur avant la mise sur le marché ou la mise en service du système d’IA à haut risque et qui se prêtent à une mise en œuvre par le déployeur. ».
- [1] « aux fins de la mise en œuvre des dispositions des paragraphes 1, 2 et 3, le système d’IA à haut risque est fourni au déployeur de telle manière que les personnes physiques chargées d’effectuer un contrôle humain, … ont la possibilité: a) de comprendre correctement les capacités et les limites pertinentes du système d’IA à haut risque et d’être en mesure de surveiller correctement son fonctionnement, y compris en vue de détecter et de traiter les anomalies, les dysfonctionnements et les performances inattendues; … d) de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou inverser la sortie du système d’IA à haut risque; … e) d’intervenir dans le fonctionnement du système d’IA à haut risque ou d’interrompre le système au moyen d’un bouton d’arrêt ou d’une procédure similaire permettant au système de s’arrêter de manière sécurisée. ».

RÉPONSE :
Oui, vous pouvez utiliser une IA pour trier des CV, mais le système concerné est classé comme IA à haut risque au sens de l'AI Act, car il « destiné à être utilisé pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats » [3].  

En conséquence, vous devez mettre en place des mesures de contrôle proportionnées aux risques et au contexte d’utilisation, soit intégrées par le fournisseur avant la mise sur le marché, soit mises en œuvre par vous, le déployeur [1].  

De plus, vous devez garantir que les personnes chargées du contrôle humain comprennent les capacités et limites du système, peuvent surveiller son fonctionnement, détecter les anomalies, décider de ne pas l’utiliser ou d’en inverser les sorties, et disposer d’un moyen d’interruption sécurisé (bouton d’arrêt) [1].  

Ces obligations s’appliquent à vous, en tant que déployeur du système d’IA à haut risque.
```

</details>

<details><summary>Raisonnement renvoyé par l'API (27 mots, non affiché à l'utilisateur, compté dans les tokens écrits)</summary>

```text
Need extracts about using IA for recruitment. Passage [3] lists systems high risk for recruitment. So answer: yes but it's high risk and obligations apply. Use extracts.
```

</details>

Temps : recherche 2.2 s · génération 2.0 s (3161 tokens lus, 673 écrits, raisonnement ≈ 27 mots, 480.9 tokens/s) · contrôle de pertinence 0.4 s · attente des limites de l'API 23 s (non comptée)

## q10 — Mes salariés ou bénévoles utilisent une IA générative : ai-je des obligations ?

Article attendu : AI Act art. 4 — passage [5].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 4 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [3] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 3 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
  [4] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 1 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
  [5] AI Act — règlement (UE) 2024/1689, article 4 : Maîtrise de l'IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_4
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
**EXTRAITS :**  
- [2] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. »  
- [2] « Les déployeurs d’un système d’IA qui génère ou manipule des textes publiés dans le but d’informer le public sur des questions d’intérêt public indiquent que le texte a été généré ou manipulé par une IA. »  
- [2] « Cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. »  
- [2] « …ou lorsque le contenu généré par l’IA a fait l’objet d’un processus d’examen humain ou de contrôle éditorial et lorsqu’une personne physique ou morale assume la responsabilité éditoriale de la publication du contenu. »  
- [4] « Les déployeurs de systèmes d’IA à haut risque prennent des mesures techniques et organisationnelles appropriées afin de garantir qu’ils utilisent ces systèmes conformément aux notices d’utilisation accompagnant les systèmes, conformément aux paragraphes 3 et 6. »  

**RÉPONSE :**  
Oui, en tant que responsable d’une organisation, vous avez des obligations en tant que **déployeur** d’un système d’IA générative. Si vos salariés ou bénévoles utilisent une IA qui génère ou manipule des images, des contenus audio/vidéo ou des textes, vous devez **indiquer que ces contenus ont été générés ou manipulés par une IA** [2]. Cette obligation ne s’applique pas uniquement lorsqu’une loi autorise l’usage à des fins de prévention ou de détection d’infractions pénales [2] ou lorsque le contenu a fait l’objet d’un examen humain ou d’un contrôle éditorial avec une responsabilité éditoriale clairement assumée [2].  

Par ailleurs, si le système d’IA que vous utilisez est classé « à haut risque », vous devez également prendre des **mesures techniques et organisationnelles appropriées** pour l’utiliser conformément aux notices d’utilisation fournies par le fournisseur [4].  

En résumé, vous devez informer le public que les contenus produits par l’IA proviennent de celle‑ci, sauf aux exceptions mentionnées, et veiller à appliquer les mesures de conformité propres aux IA à haut risque.
```

</details>

<details><summary>Raisonnement renvoyé par l'API (68 mots, non affiché à l'utilisateur, compté dans les tokens écrits)</summary>

```text
We need extracts about obligations for users (employees). Passages: [1] about suppliers informing users, not relevant. [2] about deployers of IA generating images/texts – obligations to indicate. That applies to deployers, i.e., the organization using IA. So yes obligations. Also [4] about deployers of high-risk IA taking measures. Might be relevant if generative IA is high risk. But question generic. Use extracts [2] and maybe [4]. Provide answer.
```

</details>

Temps : recherche 2.2 s · génération 1.9 s (2144 tokens lus, 640 écrits, raisonnement ≈ 68 mots, 482.1 tokens/s) · contrôle de pertinence 0.5 s · attente des limites de l'API 15 s (non comptée)

## h01 — Quel est le taux de TVA en France ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 83, paragraphe 5 : Conditions générales pour imposer des amendes administratives
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83
  [2] RGPD — règlement (UE) 2016/679, article 83, paragraphe 1 : Conditions générales pour imposer des amendes administratives
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83
  [3] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 5 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [4] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 1 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [5] RGPD — règlement (UE) 2016/679, article 83, paragraphe 4 : Conditions générales pour imposer des amendes administratives
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun  

RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

<details><summary>Raisonnement renvoyé par l'API (11 mots, non affiché à l'utilisateur, compté dans les tokens écrits)</summary>

```text
We have no info about VAT. Must respond with no extracts.
```

</details>

Temps : recherche 2.1 s · génération 0.7 s (1917 tokens lus, 47 écrits, raisonnement ≈ 11 mots, 477.4 tokens/s) · attente des limites de l'API 12 s (non comptée)

## h02 — Comment faire une déclaration d'impôts ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 77 : Droit d'introduire une réclamation auprès d'une autorité de contrôle
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_77
  [2] AI Act — règlement (UE) 2024/1689, article 47 : Déclaration UE de conformité
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_47
  [3] AI Act — règlement (UE) 2024/1689, annexe V : Déclaration UE de conformité
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_V
  [4] RGPD — règlement (UE) 2016/679, article 12, paragraphe 5 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [5] AI Act — règlement (UE) 2024/1689, article 91 : Pouvoir de demander de la documentation et des informations
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_91

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
aucun

RÉPONSE :
Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

<details><summary>Raisonnement renvoyé par l'API (8 mots, non affiché à l'utilisateur, compté dans les tokens écrits)</summary>

```text
We have no relevant passages. So respond accordingly.
```

</details>

Temps : recherche 2.2 s · génération 0.7 s (2617 tokens lus, 45 écrits, raisonnement ≈ 8 mots, 449.6 tokens/s) · attente des limites de l'API 15 s (non comptée)
