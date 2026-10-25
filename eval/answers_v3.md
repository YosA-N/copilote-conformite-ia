# Réponses du copilote — v3

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 25/10/2026 à 18:00 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen3:4b-instruct` via Ollama 0.40.11 — température 0.1, contexte 8192 tokens, couches sur la carte graphique : toutes, 1500 tokens au plus par réponse
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_v0.jsonl` (10) et `eval/questions_offtopic_v0.jsonl` (2, hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q01 | Dois-je désigner un DPO ? | 2/3 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([7]) : ignoré(s).; Citation vers un passage inexistant : [7] (seuls les passages [1] à [5] ont été fournis). | 46 s |
| q02 | Dois-je tenir un registre des traitements ? | 2/2 | non | — | 31 s |
| q03 | Combien de temps puis-je garder les données de mes clients ou adhérents ? | 2/2 | non | — | 29 s |
| q04 | Que dois-je mettre dans la mention d'information d'un formulaire ? | 3/4 | non | Réponse coupée : le modèle a atteint la limite de 1500 tokens (LLM_MAX_TOKENS), la fin de la réponse manque. Posez une question plus précise ou augmentez LLM_MAX_TOKENS dans .env.; 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1]) : ignoré(s). | 70 s |
| q05 | Une personne demande l'accès à ses données : quel délai pour répondre ? | 1/1 | non | — | 26 s |
| q06 | J'ai eu une fuite de données : que faire, et en combien de temps ? | 5/5 | non | — | 48 s |
| q07 | Quand faut-il faire une analyse d'impact (AIPD) ? | 3/3 | non | — | 50 s |
| q08 | Mon chatbot doit-il dire aux clients qu'il est une IA ? | 1/1 | non | La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui, votre chatbot doit indiquer clairement qu’il s’agit d’un système d’IA, car il interagit directement avec des … » (et 1 autre(s)). Vérifiez qui est concerné. | 37 s |
| q09 | Puis-je utiliser une IA pour trier des CV ? | 2/2 | non | — | 36 s |
| q10 | Mes salariés ou bénévoles utilisent une IA générative : ai-je des obligations ? | 2/3 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([5]) : ignoré(s).; La réponse cite [5] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.; La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Vous devez informer les personnes physiques concernées qu’elles interagissent avec un système d’IA, sauf si cela … ». Vérifiez qui est concerné. | 46 s |
| h01 | Quel est le taux de TVA en France ? | 0/0 | oui | — | 20 s |
| h02 | Comment faire une déclaration d'impôts ? | 0/0 | oui | — | 21 s |

## q01 — Dois-je désigner un DPO ?

Article attendu : RGPD art. 37 — passage [1].

### Réponse du copilote

> Oui, vous devez désigner un délégué à la protection des données (DPO) si l'un des cas suivants est rempli : le traitement est effectué par une autorité publique ou un organisme public (sauf les juridictions dans leur fonction juridictionnelle), les activités de base consistent en des opérations de traitement à grande échelle nécessitant un suivi régulier et systématique des personnes concernées, ou si le traitement concerne à grande échelle des catégories particulières de données visées à l’article 9 ou des données relatives à des condamnations pénales et infractions (article 10) [1]. Dans les cas autres que ceux visés au paragraphe 1, vous pouvez désigner un DPO, ou être tenu de le désigner selon le droit de l'Union ou d'un État membre [1]. Le DPO doit être désigné sur la base de ses qualités professionnelles, de ses connaissances spécialisées et de sa capacité à accomplir les missions visées à l'article 39, et ses coordonnées doivent être publiées et communiquées à l'autorité de contrôle [1][7].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le responsable du traitement et le sous-traitant désignent en tout état de cause un délégué à la protection des données lorsque: a) le traitement est effectué par une autorité publique ou un organisme public, à l'exception des juridictions agissant dans l'exercice de leur fonction juridictionnelle; b) les activités de base du responsable du traitement ou du sous-traitant consistent en des opérations de traitement qui, du fait de leur nature, de leur portée et/ou de leurs finalités, exigent un suivi régulier et systématique à grande échelle des personnes concernées; ou c) les activités de base du responsable du traitement ou du sous-traitant consistent en un traitement à grande échelle de catégories particulières de données visées à l’article 9 ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l’article 10. »
  [1] « Dans les cas autres que ceux visés au paragraphe 1, le responsable du traitement ou le sous-traitant ou les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent désigner ou, si le droit de l'Union ou le droit d'un État membre l'exige, sont tenus de désigner un délégué à la protection des données. »

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
  [5] RGPD — règlement (UE) 2016/679, article 50 : Coopération internationale dans le domaine de la protection des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_50
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([7]) : ignoré(s).
Attention : Citation vers un passage inexistant : [7] (seuls les passages [1] à [5] ont été fournis).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le responsable du traitement et le sous-traitant désignent en tout état de cause un délégué à la protection des données lorsque: a) le traitement est effectué par une autorité publique ou un organisme public, à l'exception des juridictions agissant dans l'exercice de leur fonction juridictionnelle; b) les activités de base du responsable du traitement ou du sous-traitant consistent en des opérations de traitement qui, du fait de leur nature, de leur portée et/ou de leurs finalités, exigent un suivi régulier et systématique à grande échelle des personnes concernées; ou c) les activités de base du responsable du traitement ou du sous-traitant consistent en un traitement à grande échelle de catégories particulières de données visées à l’article 9 ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l’article 10. »
- [1] « Dans les cas autres que ceux visés au paragraphe 1, le responsable du traitement ou le sous-traitant ou les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent désigner ou, si le droit de l'Union ou le droit d'un État membre l'exige, sont tenus de désigner un délégué à la protection des données. »
- [7] « Le responsable du traitement ou le sous-traitant publient les coordonnées du délégué à la protection des données et les communiquent à l'autorité de contrôle. »

RÉPONSE :
Oui, vous devez désigner un délégué à la protection des données (DPO) si l'un des cas suivants est rempli : le traitement est effectué par une autorité publique ou un organisme public (sauf les juridictions dans leur fonction juridictionnelle), les activités de base consistent en des opérations de traitement à grande échelle nécessitant un suivi régulier et systématique des personnes concernées, ou si le traitement concerne à grande échelle des catégories particulières de données visées à l’article 9 ou des données relatives à des condamnations pénales et infractions (article 10) [1]. Dans les cas autres que ceux visés au paragraphe 1, vous pouvez désigner un DPO, ou être tenu de le désigner selon le droit de l'Union ou d'un État membre [1]. Le DPO doit être désigné sur la base de ses qualités professionnelles, de ses connaissances spécialisées et de sa capacité à accomplir les missions visées à l'article 39, et ses coordonnées doivent être publiées et communiquées à l'autorité de contrôle [1][7].
```

</details>

Temps : recherche 8.1 s · génération 38.4 s (2973 tokens lus, 640 écrits, 33.6 tokens/s)

## q02 — Dois-je tenir un registre des traitements ?

Article attendu : RGPD art. 30 — passage [1].

### Réponse du copilote

> Oui : vous devez tenir un registre des activités de traitement si vous êtes responsable du traitement ou un sous-traitant, comme prévus à l'article 30, paragraphe 1 du RGPD [1]. Cependant, cette obligation ne s'applique pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elle effectue est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Chaque responsable du traitement et, le cas échéant, le représentant du responsable du traitement tiennent un registre des activités de traitement effectuées sous leur responsabilité. »
  [1] « Les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10. »

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
- [1] « Chaque responsable du traitement et, le cas échéant, le représentant du responsable du traitement tiennent un registre des activités de traitement effectuées sous leur responsabilité. »
- [1] « Les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10. »

RÉPONSE :
Oui : vous devez tenir un registre des activités de traitement si vous êtes responsable du traitement ou un sous-traitant, comme prévus à l'article 30, paragraphe 1 du RGPD [1]. Cependant, cette obligation ne s'applique pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elle effectue est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 [1].
```

</details>

Temps : recherche 2.1 s · génération 28.4 s (2881 tokens lus, 374 écrits, 34.1 tokens/s)

## q03 — Combien de temps puis-je garder les données de mes clients ou adhérents ?

Article attendu : RGPD art. 5 — passage [4].

### Réponse du copilote

> Vous pouvez garder les données de vos clients ou adhérents pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées [4]. Si les données sont conservées pour des fins archivistiques dans l'intérêt public, ou pour des fins de recherche scientifique ou historique ou statistiques, cela peut être autorisé, à condition que des mesures techniques et organisationnelles appropriées soient mises en œuvre [4]. La durée de conservation doit être précisée, ou, si cela n'est pas possible, des critères doivent être fournis pour déterminer cette durée [5].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [4] « les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée (limitation de la conservation); »
  [5] « a) la durée pendant laquelle les données à caractère personnel seront conservées ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; »

Sources citées :
  [4] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 4, définition 3 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [2] RGPD — règlement (UE) 2016/679, article 18 : Droit à la limitation du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_18
  [3] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [4] « les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée (limitation de la conservation); »
- [5] « a) la durée pendant laquelle les données à caractère personnel seront conservées ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; »

RÉPONSE :
Vous pouvez garder les données de vos clients ou adhérents pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées [4]. Si les données sont conservées pour des fins archivistiques dans l'intérêt public, ou pour des fins de recherche scientifique ou historique ou statistiques, cela peut être autorisé, à condition que des mesures techniques et organisationnelles appropriées soient mises en œuvre [4]. La durée de conservation doit être précisée, ou, si cela n'est pas possible, des critères doivent être fournis pour déterminer cette durée [5].
```

</details>

Temps : recherche 2.2 s · génération 26.4 s (2844 tokens lus, 318 écrits, 34.3 tokens/s)

## q04 — Que dois-je mettre dans la mention d'information d'un formulaire ?

Article attendu : RGPD art. 13 — passage [1].

### Réponse du copilote

> Vous devez inclure dans la mention d'information d'un formulaire les éléments suivants : l'identité et les coordonnées du responsable du traitement, le cas échéant du représentant ou du délégué à la protection des données ; les finalités du traitement et la base juridique du traitement ; les intérêts légitimes poursuivis (lorsque le traitement est fondé sur

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « En plus des informations visées au paragraphe 1, le responsable du traitement fournit à la personne concernée, au moment où les données à caractère personnel sont obtenues, les informations complémentaires suivantes qui sont nécessaires pour garantir un traitement équitable et transparent: a) la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; b) l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ou du droit de s'opposer au traitement et du droit à la portabilité des données; c) lorsque le traitement est fondé sur l'article 6, paragraphe 1, point a), ou sur l'article 9, paragraphe 2, point a), l'existence du droit de retirer son consentement à tout moment, sans porter atteinte à la licéité du traitement fondé sur le consentement effectué avant le retrait de celui-ci; d) le droit d'introduire une réclamation auprès d'une autorité de contrôle; e) des informations sur la question de savoir si l'exigence de fourniture de données à caractère personnel a un caractère réglementaire ou contractuel ou si elle conditionne la conclusion d'un contrat et si la personne concernée est tenue de fournir les données à caractère personnel, ainsi que sur les conséquences éventuelles de la non-fourniture de ces données; f) l'existence d'une prise de décision automatisée, y compris un profilage, visée à l'article 22, paragraphes 1 et 4, et, au moins en pareils cas, des informations utiles concernant la logique sous-jacente, ainsi que l'importance et les conséquences prévues de ce traitement pour la personne concernée. »
  [2] « En plus des informations visées au paragraphe 1, le responsable du traitement fournit à la personne concernée les informations suivantes nécessaires pour garantir un traitement équitable et transparent à l'égard de la personne concernée: a) la durée pendant laquelle les données à caractère personnel seront conservées ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; b) lorsque le traitement est fondé sur l'article 6, paragraphe 1, point f), les intérêts légitimes poursuivis par le responsable du traitement ou par un tiers; c) l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ainsi que du droit de s'opposer au traitement et du droit à la portabilité des données; d) lorsque le traitement est fondé sur l'article 6, paragraphe 1, point a), ou sur l'article 9, paragraphe 2, point a), l'existence du droit de retirer le consentement à tout moment, sans porter atteinte à la licéité du traitement fondé sur le consentement effectué avant le retrait de celui-ci; e) le droit d'introduire une réclamation auprès d'une autorité de contrôle; f) la source d'où proviennent les données à caractère personnel et, le cas échéant, une mention indiquant qu'elles sont issues ou non de sources accessibles au public; g) l'existence d'une prise de décision automatisée, y compris un profilage, visée à l'article 22, paragraphes 1 et 4, et, au moins en pareils cas, des informations utiles concernant la logique sous-jacente, ainsi que l'importance et les conséquences prévues de ce traitement pour la personne concernée. »
  [4] « Le responsable du traitement prend des mesures appropriées pour fournir toute information visée aux articles 13 et 14 ainsi que pour procéder à toute communication au titre des articles 15 à 22 et de l'article 34 en ce qui concerne le traitement à la personne concernée d'une façon concise, transparente, compréhensible et aisément accessible, en des termes clairs et simples, en particulier pour toute information destinée spécifiquement à un enfant. Les informations sont fournies par écrit ou par d'autres moyens y compris, lorsque c'est approprié, par voie électronique. Lorsque la personne concernée en fait la demande, les informations peuvent être fournies oralement, à condition que l'identité de la personne concernée soit démontrée par d'autres moyens. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [2] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [4] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 12, paragraphe 6 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
Attention : Réponse coupée : le modèle a atteint la limite de 1500 tokens (LLM_MAX_TOKENS), la fin de la réponse manque. Posez une question plus précise ou augmentez LLM_MAX_TOKENS dans .env.
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1]) : ignoré(s).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Lorsque des données à caractère personnel relatives à une personne concernée sont collectées auprès de cette personne, le responsable du traitement lui fournit, au moment où les données en question sont obtenues, toutes les informations suivantes: a) l'identité et les coordonnées du responsable du traitement et, le cas échéant, du représentant du responsable du traitement; b) le cas échéant, les coordonnées du délégué à la protection des données; c) les finalités du traitement auquel sont destinées les données à caractère personnel ainsi que la base juridique du traitement; d) lorsque le traitement est fondé sur l'article 6, paragraphe 1, point f), les intérêts légitimes poursuivis par le responsable du traitement ou par un tiers; e) les destinataires ou les catégories de destinataires des données à caractère personnel, s'ils existent; et f) le cas échéant, le fait que le responsable du traitement a l'intention d'effectuer un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale, et l'existence ou l'absence d'une décision d'adéquation rendue par la Commission ou, dans le cas des transferts visés à l'article 46 ou 47, ou à l'article 49, paragraphe 1, deuxième alinéa, la référence aux garanties appropriées ou adaptées et les moyens d'en obtenir une copie ou l'endroit où elles ont été mises à disposition; »
- [1] « En plus des informations visées au paragraphe 1, le responsable du traitement fournit à la personne concernée, au moment où les données à caractère personnel sont obtenues, les informations complémentaires suivantes qui sont nécessaires pour garantir un traitement équitable et transparent: a) la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; b) l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ou du droit de s'opposer au traitement et du droit à la portabilité des données; c) lorsque le traitement est fondé sur l'article 6, paragraphe 1, point a), ou sur l'article 9, paragraphe 2, point a), l'existence du droit de retirer son consentement à tout moment, sans porter atteinte à la licéité du traitement fondé sur le consentement effectué avant le retrait de celui-ci; d) le droit d'introduire une réclamation auprès d'une autorité de contrôle; e) des informations sur la question de savoir si l'exigence de fourniture de données à caractère personnel a un caractère réglementaire ou contractuel ou si elle conditionne la conclusion d'un contrat et si la personne concernée est tenue de fournir les données à caractère personnel, ainsi que sur les conséquences éventuelles de la non-fourniture de ces données; f) l'existence d'une prise de décision automatisée, y compris un profilage, visée à l'article 22, paragraphes 1 et 4, et, au moins en pareils cas, des informations utiles concernant la logique sous-jacente, ainsi que l'importance et les conséquences prévues de ce traitement pour la personne concernée. »
- [2] « En plus des informations visées au paragraphe 1, le responsable du traitement fournit à la personne concernée les informations suivantes nécessaires pour garantir un traitement équitable et transparent à l'égard de la personne concernée: a) la durée pendant laquelle les données à caractère personnel seront conservées ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; b) lorsque le traitement est fondé sur l'article 6, paragraphe 1, point f), les intérêts légitimes poursuivis par le responsable du traitement ou par un tiers; c) l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ainsi que du droit de s'opposer au traitement et du droit à la portabilité des données; d) lorsque le traitement est fondé sur l'article 6, paragraphe 1, point a), ou sur l'article 9, paragraphe 2, point a), l'existence du droit de retirer le consentement à tout moment, sans porter atteinte à la licéité du traitement fondé sur le consentement effectué avant le retrait de celui-ci; e) le droit d'introduire une réclamation auprès d'une autorité de contrôle; f) la source d'où proviennent les données à caractère personnel et, le cas échéant, une mention indiquant qu'elles sont issues ou non de sources accessibles au public; g) l'existence d'une prise de décision automatisée, y compris un profilage, visée à l'article 22, paragraphes 1 et 4, et, au moins en pareils cas, des informations utiles concernant la logique sous-jacente, ainsi que l'importance et les conséquences prévues de ce traitement pour la personne concernée. »
- [4] « Le responsable du traitement prend des mesures appropriées pour fournir toute information visée aux articles 13 et 14 ainsi que pour procéder à toute communication au titre des articles 15 à 22 et de l'article 34 en ce qui concerne le traitement à la personne concernée d'une façon concise, transparente, compréhensible et aisément accessible, en des termes clairs et simples, en particulier pour toute information destinée spécifiquement à un enfant. Les informations sont fournies par écrit ou par d'autres moyens y compris, lorsque c'est approprié, par voie électronique. Lorsque la personne concernée en fait la demande, les informations peuvent être fournies oralement, à condition que l'identité de la personne concernée soit démontrée par d'autres moyens. »

RÉPONSE :
Vous devez inclure dans la mention d'information d'un formulaire les éléments suivants : l'identité et les coordonnées du responsable du traitement, le cas échéant du représentant ou du délégué à la protection des données ; les finalités du traitement et la base juridique du traitement ; les intérêts légitimes poursuivis (lorsque le traitement est fondé sur
```

</details>

Temps : recherche 2.2 s · génération 67.7 s (3210 tokens lus, 1500 écrits, 31.8 tokens/s)

## q05 — Une personne demande l'accès à ses données : quel délai pour répondre ?

Article attendu : RGPD art. 12 — passage [1].

### Réponse du copilote

> Le responsable du traitement doit répondre à la demande d'accès des données de la personne concernée dans un délai d'un mois à compter de la réception de la demande [1]. Ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes [1]. Le responsable du traitement doit informer la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [3] RGPD — règlement (UE) 2016/679, article 12, paragraphe 4 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [4] RGPD — règlement (UE) 2016/679, article 14, paragraphe 3 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. »

RÉPONSE :
Le responsable du traitement doit répondre à la demande d'accès des données de la personne concernée dans un délai d'un mois à compter de la réception de la demande [1]. Ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes [1]. Le responsable du traitement doit informer la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande [1].
```

</details>

Temps : recherche 2.2 s · génération 23.4 s (2727 tokens lus, 251 écrits, 34.4 tokens/s)

## q06 — J'ai eu une fuite de données : que faire, et en combien de temps ?

Article attendu : RGPD art. 33 ou RGPD art. 34 — passage [1].

### Réponse du copilote

> Lors d'une fuite de données (c’est-à-dire une violation de données à caractère personnel), le responsable du traitement doit notifier la violation à l'autorité de contrôle compétente dans les meilleurs délais, et, si possible, dans les 72 heures après en avoir pris connaissance, « à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques » [1]. Si la notification n’est pas faite dans les 72 heures, elle doit être accompagnée des motifs du retard [1]. Le sous-traitant doit, dans les meilleurs délais, notifie à son responsable du traitement toute violation de données à caractère personnel [1]. En outre, si la violation est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement doit communiquer la violation à la personne concernée dans les meilleurs délais [2]. Cette communication doit être claire et simple, et inclure les informations et mesures visées à l'article 33, paragraphe 3, points b), c) et d) [2]. La fuite de données est définie comme une violation de la sécurité entraînant la divulgation non autorisée de données à caractère personnel [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. Lorsque la notification à l'autorité de contrôle n'a pas lieu dans les 72 heures, elle est accompagnée des motifs du retard. »
  [1] « Le sous-traitant notifie au responsable du traitement toute violation de données à caractère personnel dans les meilleurs délais après en avoir pris connaissance. »
  [2] « Lorsqu'une violation de données à caractère personnel est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement communique la violation de données à caractère personnel à la personne concernée dans les meilleurs délais. »
  [2] « La communication à la personne concernée visée au paragraphe 1 du présent article décrit, en des termes clairs et simples, la nature de la violation de données à caractère personnel et contient au moins les informations et mesures visées à l'article 33, paragraphe 3, points b), c) et d). »
  [3] « «violation de données à caractère personnel», une violation de la sécurité entraînant, de manière accidentelle ou illicite, la destruction, la perte, l'altération, la divulgation non autorisée de données à caractère personnel transmises, conservées ou traitées d'une autre manière, ou l'accès non autorisé à de telles données; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 33 : Notification à l'autorité de contrôle d'une violation de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_33
  [2] RGPD — règlement (UE) 2016/679, article 34 : Communication à la personne concernée d'une violation de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_34
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 12 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
Passages consultés mais non cités :
  [4] RGPD — règlement (UE) 2016/679, article 17 : Droit à l'effacement («droit à l'oubli»)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_17
  [5] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. Lorsque la notification à l'autorité de contrôle n'a pas lieu dans les 72 heures, elle est accompagnée des motifs du retard. »
- [1] « Le sous-traitant notifie au responsable du traitement toute violation de données à caractère personnel dans les meilleurs délais après en avoir pris connaissance. »
- [2] « Lorsqu'une violation de données à caractère personnel est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement communique la violation de données à caractère personnel à la personne concernée dans les meilleurs délais. »
- [2] « La communication à la personne concernée visée au paragraphe 1 du présent article décrit, en des termes clairs et simples, la nature de la violation de données à caractère personnel et contient au moins les informations et mesures visées à l'article 33, paragraphe 3, points b), c) et d). »
- [3] « «violation de données à caractère personnel», une violation de la sécurité entraînant, de manière accidentelle ou illicite, la destruction, la perte, l'altération, la divulgation non autorisée de données à caractère personnel transmises, conservées ou traitées d'une autre manière, ou l'accès non autorisé à de telles données; »

RÉPONSE :
Lors d'une fuite de données (c’est-à-dire une violation de données à caractère personnel), le responsable du traitement doit notifier la violation à l'autorité de contrôle compétente dans les meilleurs délais, et, si possible, dans les 72 heures après en avoir pris connaissance, « à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques » [1]. Si la notification n’est pas faite dans les 72 heures, elle doit être accompagnée des motifs du retard [1]. Le sous-traitant doit, dans les meilleurs délais, notifie à son responsable du traitement toute violation de données à caractère personnel [1]. En outre, si la violation est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement doit communiquer la violation à la personne concernée dans les meilleurs délais [2]. Cette communication doit être claire et simple, et inclure les informations et mesures visées à l'article 33, paragraphe 3, points b), c) et d) [2]. La fuite de données est définie comme une violation de la sécurité entraînant la divulgation non autorisée de données à caractère personnel [3].
```

</details>

Temps : recherche 2.2 s · génération 46.3 s (3655 tokens lus, 690 écrits, 31.9 tokens/s)

## q07 — Quand faut-il faire une analyse d'impact (AIPD) ?

Article attendu : RGPD art. 35 — passage [1].

### Réponse du copilote

> Une analyse d'impact relative à la protection des données (AIPD) est requise dans les cas suivants : l'évaluation systématique et approfondie d'aspects personnels concernant des personnes physiques, fondée sur un traitement automatisé, y compris le profilage, et sur la base de laquelle sont prises des décisions produisant des effets juridiques à l'égard d'une personne physique ou l'affectant de manière significative de façon similaire [1] ; le traitement à grande échelle de catégories particulières de données visées à l'article 9, paragraphe 1, ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 [1] ; ou la surveillance systématique à grande échelle d'une zone accessible au public [1].  
> Avant le déploiement d’un système d’IA à haut risque (sauf dans le domaine visé à l’annexe III, point 2), les déployeurs, qu’ils soient des organismes de droit public ou des entités privées fournissant des services publics, ou les déployeurs de systèmes d’IA à haut risque visés à l’annexe III, points 5), b) et c), doivent effectuer une analyse de l’impact sur les droits fondamentaux [3].  
> Le cas échéant, les déployeurs de systèmes d’IA à haut risque utilisent les informations fournies en application de l’article 13 pour se conformer à leur obligation de procéder à une analyse d’impact relative à la protection des données en vertu de l’article 35 du RGPD [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « L'analyse d'impact relative à la protection des données visée au paragraphe 1 est, en particulier, requise dans les cas suivants: a) l'évaluation systématique et approfondie d'aspects personnels concernant des personnes physiques, qui est fondée sur un traitement automatisé, y compris le profilage, et sur la base de laquelle sont prises des décisions produisant des effets juridiques à l'égard d'une personne physique ou l'affectant de manière significative de façon similaire; b) le traitement à grande échelle de catégories particulières de données visées à l'article 9, paragraphe 1, ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10; ou c) la surveillance systématique à grande échelle d'une zone accessible au public. »
  [3] « Avant le déploiement d’un système d’IA à haut risque visé à l’article 6, paragraphe 2, à l’exception des systèmes d’IA à haut risque destinés à être utilisés dans le domaine visé à l’annexe III, point 2, les déployeurs qui sont des organismes de droit public ou des entités privées fournissant des services publics et les déployeurs de systèmes d’IA à haut risque visés à l’annexe III, points 5), b) et c), effectuent une analyse de l’impact sur les droits fondamentaux que l’utilisation de ce système peut produire. »
  [4] « Le cas échéant, les déployeurs de systèmes d’IA à haut risque utilisent les informations fournies en application de l’article 13 du présent règlement pour se conformer à leur obligation de procéder à une analyse d’impact relative à la protection des données en vertu de l’article 35 du règlement (UE) 2016/679 ou de l’article 27 de la directive (UE) 2016/680. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 35, paragraphe 3 : Analyse d'impact relative à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [3] AI Act — règlement (UE) 2024/1689, article 27 : Analyse d’impact des systèmes d’IA à haut risque sur les droits fondamentaux (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_27
  [4] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 9 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 35, paragraphe 11 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [5] RGPD — règlement (UE) 2016/679, article 83, paragraphe 2 : Conditions générales pour imposer des amendes administratives
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « L'analyse d'impact relative à la protection des données visée au paragraphe 1 est, en particulier, requise dans les cas suivants: a) l'évaluation systématique et approfondie d'aspects personnels concernant des personnes physiques, qui est fondée sur un traitement automatisé, y compris le profilage, et sur la base de laquelle sont prises des décisions produisant des effets juridiques à l'égard d'une personne physique ou l'affectant de manière significative de façon similaire; b) le traitement à grande échelle de catégories particulières de données visées à l'article 9, paragraphe 1, ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10; ou c) la surveillance systématique à grande échelle d'une zone accessible au public. »
- [3] « Avant le déploiement d’un système d’IA à haut risque visé à l’article 6, paragraphe 2, à l’exception des systèmes d’IA à haut risque destinés à être utilisés dans le domaine visé à l’annexe III, point 2, les déployeurs qui sont des organismes de droit public ou des entités privées fournissant des services publics et les déployeurs de systèmes d’IA à haut risque visés à l’annexe III, points 5), b) et c), effectuent une analyse de l’impact sur les droits fondamentaux que l’utilisation de ce système peut produire. »
- [4] « Le cas échéant, les déployeurs de systèmes d’IA à haut risque utilisent les informations fournies en application de l’article 13 du présent règlement pour se conformer à leur obligation de procéder à une analyse d’impact relative à la protection des données en vertu de l’article 35 du règlement (UE) 2016/679 ou de l’article 27 de la directive (UE) 2016/680. »

RÉPONSE :
Une analyse d'impact relative à la protection des données (AIPD) est requise dans les cas suivants : l'évaluation systématique et approfondie d'aspects personnels concernant des personnes physiques, fondée sur un traitement automatisé, y compris le profilage, et sur la base de laquelle sont prises des décisions produisant des effets juridiques à l'égard d'une personne physique ou l'affectant de manière significative de façon similaire [1] ; le traitement à grande échelle de catégories particulières de données visées à l'article 9, paragraphe 1, ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 [1] ; ou la surveillance systématique à grande échelle d'une zone accessible au public [1].  
Avant le déploiement d’un système d’IA à haut risque (sauf dans le domaine visé à l’annexe III, point 2), les déployeurs, qu’ils soient des organismes de droit public ou des entités privées fournissant des services publics, ou les déployeurs de systèmes d’IA à haut risque visés à l’annexe III, points 5), b) et c), doivent effectuer une analyse de l’impact sur les droits fondamentaux [3].  
Le cas échéant, les déployeurs de systèmes d’IA à haut risque utilisent les informations fournies en application de l’article 13 pour se conformer à leur obligation de procéder à une analyse d’impact relative à la protection des données en vertu de l’article 35 du RGPD [4].
```

</details>

Temps : recherche 2.2 s · génération 48.1 s (3204 tokens lus, 895 écrits, 32.5 tokens/s)

## q08 — Mon chatbot doit-il dire aux clients qu'il est une IA ?

Article attendu : AI Act art. 50 — passage [1].

### Réponse du copilote

> Oui, votre chatbot doit indiquer clairement qu’il s’agit d’un système d’IA, car il interagit directement avec des personnes physiques [1]. Cette obligation s’applique sauf si l’information que le système est une IA ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation [1].

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
Attention : La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui, votre chatbot doit indiquer clairement qu’il s’agit d’un système d’IA, car il interagit directement avec des … » (et 1 autre(s)). Vérifiez qui est concerné.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »  

RÉPONSE :  
Oui, votre chatbot doit indiquer clairement qu’il s’agit d’un système d’IA, car il interagit directement avec des personnes physiques [1]. Cette obligation s’applique sauf si l’information que le système est une IA ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation [1].
```

</details>

Temps : recherche 2.2 s · génération 34.7 s (3937 tokens lus, 226 écrits, 32.0 tokens/s)

## q09 — Puis-je utiliser une IA pour trier des CV ?

Article attendu : AI Act annexe III, point 4 ou AI Act art. 26 — passage [3].

### Réponse du copilote

> Oui, vous pouvez utiliser une IA pour trier des CV, car cela relève des systèmes d’IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, notamment pour analyser et filtrer les candidatures [3]. Cependant, si ce système est classé comme un système d’IA à haut risque, il doit être soumis à un contrôle humain pour prévenir ou réduire les risques pour les droits fondamentaux, notamment en ce qui concerne la santé, la sécurité ou les droits fondamentaux des candidats [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »
  [1] « Le contrôle humain vise à prévenir ou à réduire au minimum les risques pour la santé, la sécurité ou les droits fondamentaux qui peuvent apparaître lorsqu’un système d’IA à haut risque est utilisé conformément à sa destination ou dans des conditions de mauvaise utilisation raisonnablement prévisible, en particulier lorsque de tels risques persistent malgré l’application d’autres exigences énoncées dans la présente section. »

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

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [3] « systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »  
- [1] « Le contrôle humain vise à prévenir ou à réduire au minimum les risques pour la santé, la sécurité ou les droits fondamentaux qui peuvent apparaître lorsqu’un système d’IA à haut risque est utilisé conformément à sa destination ou dans des conditions de mauvaise utilisation raisonnablement prévisible, en particulier lorsque de tels risques persistent malgré l’application d’autres exigences énoncées dans la présente section. »  

RÉPONSE :  
Oui, vous pouvez utiliser une IA pour trier des CV, car cela relève des systèmes d’IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, notamment pour analyser et filtrer les candidatures [3]. Cependant, si ce système est classé comme un système d’IA à haut risque, il doit être soumis à un contrôle humain pour prévenir ou réduire les risques pour les droits fondamentaux, notamment en ce qui concerne la santé, la sécurité ou les droits fondamentaux des candidats [1].
```

</details>

Temps : recherche 2.2 s · génération 33.9 s (3611 tokens lus, 308 écrits, 32.5 tokens/s)

## q10 — Mes salariés ou bénévoles utilisent une IA générative : ai-je des obligations ?

Article attendu : AI Act art. 4 — passage [5].

### Réponse du copilote

> Oui : si vos salariés ou bénévoles utilisent une IA générative, vous, comme déployeur du système, avez des obligations de transparence et de maîtrise de l’IA. Vous devez informer les personnes physiques concernées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation [1]. Si les contenus générés par l’IA sont des images, audio ou vidéo constituant un hypertrucage, vous devez indiquer que les contenus ont été générés ou manipulés par une IA [2]. Si les contenus sont destinés à informer le public sur des questions d’intérêt public, vous devez aussi indiquer que le texte a été généré ou manipulé par une IA [2]. En outre, vous devez prendre des mesures pour favoriser la maîtrise de l’IA par vos salariés ou bénévoles, en tenant compte de leurs connaissances, expérience, formation et du contexte d’utilisation [5]. Cette obligation ne vous oblige pas à garantir un niveau spécifique de maîtrise de l’IA par un individu [5].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. Cette obligation ne s’applique pas aux systèmes d’IA dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers, sauf si ces systèmes sont mis à la disposition du public pour permettre le signalement d’une infraction pénale. »
  [2] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. Cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. Lorsque le contenu fait partie d’une œuvre ou d’un programme manifestement artistique, créatif, satirique, fictif ou analogue, les obligations de transparence énoncées au présent paragraphe se limitent à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre. Les déployeurs d’un système d’IA qui génère ou manipule des textes publiés dans le but d’informer le public sur des questions d’intérêt public indiquent que le texte a été généré ou manipulé par une IA. Cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière, ou lorsque le contenu généré par l’IA a fait l’objet d’un processus d’examen humain ou de contrôle éditorial et lorsqu’une personne physique ou morale assume la responsabilité éditoriale de la publication du contenu. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 4 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [5] AI Act — règlement (UE) 2024/1689, article 4 : Maîtrise de l'IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_4
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 3 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
  [4] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 1 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([5]) : ignoré(s).
Attention : La réponse cite [5] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.
Attention : La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Vous devez informer les personnes physiques concernées qu’elles interagissent avec un système d’IA, sauf si cela … ». Vérifiez qui est concerné.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. Cette obligation ne s’applique pas aux systèmes d’IA dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers, sauf si ces systèmes sont mis à la disposition du public pour permettre le signalement d’une infraction pénale. »  
- [2] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. Cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. Lorsque le contenu fait partie d’une œuvre ou d’un programme manifestement artistique, créatif, satirique, fictif ou analogue, les obligations de transparence énoncées au présent paragraphe se limitent à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre. Les déployeurs d’un système d’IA qui génère ou manipule des textes publiés dans le but d’informer le public sur des questions d’intérêt public indiquent que le texte a été généré ou manipulé par une IA. Cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière, ou lorsque le contenu généré par l’IA a fait l’objet d’un processus d’examen humain ou de contrôle éditorial et lorsqu’une personne physique ou morale assume la responsabilité éditoriale de la publication du contenu. »  
- [5] « Les fournisseurs et les déployeurs de systèmes d'IA prennent des mesures pour favoriser le développement de la maîtrise de l'IA par leur personnel et les autres personnes s'occupant du fonctionnement et de l'utilisation des systèmes d'IA pour leur compte, en prenant en considération leurs connaissances techniques, leur expérience, leur éducation et leur formation, ainsi que le contexte dans which les systèmes d'IA sont destinés à être utilisés, et en tenant compte des personnes ou des groupes de personnes à l'égard desquels les systèmes d'IA sont destinés à être utilisés. Cette obligation ne contraint pas les fournisseurs ou les déployeurs à garantir un niveau spécifique de maîtrise de l'IA par un individu. »  

RÉPONSE :  
Oui : si vos salariés ou bénévoles utilisent une IA générative, vous, comme déployeur du système, avez des obligations de transparence et de maîtrise de l’IA. Vous devez informer les personnes physiques concernées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation [1]. Si les contenus générés par l’IA sont des images, audio ou vidéo constituant un hypertrucage, vous devez indiquer que les contenus ont été générés ou manipulés par une IA [2]. Si les contenus sont destinés à informer le public sur des questions d’intérêt public, vous devez aussi indiquer que le texte a été généré ou manipulé par une IA [2]. En outre, vous devez prendre des mesures pour favoriser la maîtrise de l’IA par vos salariés ou bénévoles, en tenant compte de leurs connaissances, expérience, formation et du contexte d’utilisation [5]. Cette obligation ne vous oblige pas à garantir un niveau spécifique de maîtrise de l’IA par un individu [5].
```

</details>

Temps : recherche 2.2 s · génération 43.4 s (2388 tokens lus, 1047 écrits, 34.2 tokens/s)

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
  [2] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 5 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [3] RGPD — règlement (UE) 2016/679, article 83, paragraphe 4 : Conditions générales pour imposer des amendes administratives
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83
  [4] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 4 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [5] AI Act — règlement (UE) 2024/1689, article 101 : Amendes applicables aux fournisseurs de modèles d’IA à usage général
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_101

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun  
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Temps : recherche 2.1 s · génération 18.2 s (2861 tokens lus, 29 écrits, 35.4 tokens/s)

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
EXTRAITS : aucun  
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Temps : recherche 2.1 s · génération 19.1 s (2970 tokens lus, 29 écrits, 35.7 tokens/s)
