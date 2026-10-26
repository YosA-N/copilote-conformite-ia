# Réponses du copilote — v4

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 26/10/2026 à 14:35 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen3:4b-instruct` via Ollama 0.40.11 — température 0.1, contexte 8192 tokens, couches sur la carte graphique : toutes, 2000 tokens au plus par réponse
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_v0.jsonl` (10), `eval/questions_offtopic_v0.jsonl` (0 + 2 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q01 | Dois-je désigner un DPO ? | 2/2 | non | — | 55 s |
| q02 | Dois-je tenir un registre des traitements ? | 2/2 | non | — | 37 s |
| q03 | Combien de temps puis-je garder les données de mes clients ou adhérents ? | 1/1 | non | — | 28 s |
| q04 | Que dois-je mettre dans la mention d'information d'un formulaire ? | 3/4 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1]) : ignoré(s). | 89 s |
| q05 | Une personne demande l'accès à ses données : quel délai pour répondre ? | 2/2 | non | — | 38 s |
| q06 | J'ai eu une fuite de données : que faire, et en combien de temps ? | 3/6 | non | 3 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1], [1], [1]) : ignoré(s). | 52 s |
| q07 | Quand faut-il faire une analyse d'impact (AIPD) ? | 5/5 | non | La réponse s'appuie sur le RGPD et l'AI Act sans dire de quel règlement vient chaque obligation : « Elle doit être effectuée avant le traitement, notamment dans les cas de traitement automatisé fondé sur le profilage ou … » (et 1 autre(s)). | 59 s |
| q08 | Mon chatbot doit-il dire aux clients qu'il est une IA ? | 1/1 | non | La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui: votre chatbot doit indiquer clairement qu’il s’agit d’un système d’IA, sauf si cela ressort clairement du point de … ». Vérifiez qui est concerné. | 40 s |
| q09 | Puis-je utiliser une IA pour trier des CV ? | 2/2 | non | — | 39 s |
| q10 | Mes salariés ou bénévoles utilisent une IA générative : ai-je des obligations ? | 2/3 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([5]) : ignoré(s).; La réponse cite [5] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.; La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Selon l’AI Act, article 50, paragraphes 1 et 2, les déployeurs doivent veiller à ce que les personnes physiques … ». Vérifiez qui est concerné. | 51 s |
| h01 | Quel est le taux de TVA en France ? | 0/0 | oui | — | 14 s |
| h02 | Comment faire une déclaration d'impôts ? | 0/0 | oui | — | 21 s |

## q01 — Dois-je désigner un DPO ?

Article attendu : RGPD art. 37 — passage [1].

### Réponse du copilote

> Oui : vous devez désigner un délégué à la protection des données (DPO) si l'un des cas suivants est vérifié : le traitement est effectué par une autorité publique ou un organisme public (sauf juridictions en exercice de leur fonction juridictionnelle) [1], ou si vos activités de base consistent en des opérations de traitement à grande échelle nécessitant un suivi régulier et systématique des personnes concernées [1], ou si vous effectuez un traitement à grande échelle de catégories particulières de données (article 9) ou de données relatives à des condamnations pénales ou infractions (article 10) [1]. Si vous effectuez une analyse d'impact relative à la protection des données, vous devez consulter le DPO, ce qui suppose que le DPO a été désigné [4]. Les passages trouvés ne précisent pas les cas où le DPO n'est pas obligatoire, mais indiquent clairement que la désignation est obligatoire dans les cas précisés.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le responsable du traitement et le sous-traitant désignent en tout état de cause un délégué à la protection des données lorsque: a) le traitement est effectué par une autorité publique ou un organisme public, à l'exception des juridictions agissant dans l'exercice de leur fonction juridictionnelle; b) les activités de base du responsable du traitement ou du sous-traitant consistent en des opérations de traitement qui, du fait de leur nature, de leur portée et/ou de leurs finalités, exigent un suivi régulier et systématique à grande échelle des personnes concernées; ou c) les activités de base du responsable du traitement ou du sous-traitant consistent en un traitement à grande échelle de catégories particulières de données visées à l’article 9 ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l’article 10. »
  [4] « Lorsqu'il effectue une analyse d'impact relative à la protection des données, le responsable du traitement demande conseil au délégué à la protection des données, si un tel délégué a été désigné. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 37 : Désignation du délégué à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_37
  [4] RGPD — règlement (UE) 2016/679, article 35, paragraphe 2 : Analyse d'impact relative à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 38 : Fonction du délégué à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_38
  [3] RGPD — règlement (UE) 2016/679, article 39 : Missions du délégué à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_39
  [5] RGPD — règlement (UE) 2016/679, article 35, paragraphe 1 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le responsable du traitement et le sous-traitant désignent en tout état de cause un délégué à la protection des données lorsque: a) le traitement est effectué par une autorité publique ou un organisme public, à l'exception des juridictions agissant dans l'exercice de leur fonction juridictionnelle; b) les activités de base du responsable du traitement ou du sous-traitant consistent en des opérations de traitement qui, du fait de leur nature, de leur portée et/ou de leurs finalités, exigent un suivi régulier et systématique à grande échelle des personnes concernées; ou c) les activités de base du responsable du traitement ou du sous-traitant consistent en un traitement à grande échelle de catégories particulières de données visées à l’article 9 ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l’article 10. »
- [4] « Lorsqu'il effectue une analyse d'impact relative à la protection des données, le responsable du traitement demande conseil au délégué à la protection des données, si un tel délégué a été désigné. »

RÉPONSE :
Oui : vous devez désigner un délégué à la protection des données (DPO) si l'un des cas suivants est vérifié : le traitement est effectué par une autorité publique ou un organisme public (sauf juridictions en exercice de leur fonction juridictionnelle) [1], ou si vos activités de base consistent en des opérations de traitement à grande échelle nécessitant un suivi régulier et systématique des personnes concernées [1], ou si vous effectuez un traitement à grande échelle de catégories particulières de données (article 9) ou de données relatives à des condamnations pénales ou infractions (article 10) [1]. Si vous effectuez une analyse d'impact relative à la protection des données, vous devez consulter le DPO, ce qui suppose que le DPO a été désigné [4]. Les passages trouvés ne précisent pas les cas où le DPO n'est pas obligatoire, mais indiquent clairement que la désignation est obligatoire dans les cas précisés.
```

</details>

Temps : recherche 2.4 s · génération 47.1 s (2880 tokens lus, 521 écrits, 35.6 tokens/s) · contrôle de pertinence 5.3 s

## q02 — Dois-je tenir un registre des traitements ?

Article attendu : RGPD art. 30 — passage [1].

### Réponse du copilote

> Oui : vous devez tenir un registre des activités de traitement si vous êtes responsable du traitement ou un sous-traitant, conformément à l’article 30 du RGPD [1]. Cependant, cette obligation ne s'applique pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elle effectue est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 [1].

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
Oui : vous devez tenir un registre des activités de traitement si vous êtes responsable du traitement ou un sous-traitant, conformément à l’article 30 du RGPD [1]. Cependant, cette obligation ne s'applique pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elle effectue est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 [1].
```

</details>

Temps : recherche 5.0 s · génération 27.7 s (2915 tokens lus, 366 écrits, 35.6 tokens/s) · contrôle de pertinence 3.9 s

## q03 — Combien de temps puis-je garder les données de mes clients ou adhérents ?

Article attendu : RGPD art. 5 — passage [5].

### Réponse du copilote

> Vous pouvez garder les données de vos clients ou adhérents pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées [5]. Si les données sont traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques, elles peuvent être conservées plus longtemps, à condition que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée [5].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [5] « les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée (limitation de la conservation); »

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
- [5] « les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée (limitation de la conservation); »

RÉPONSE :
Vous pouvez garder les données de vos clients ou adhérents pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées [5]. Si les données sont traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques, elles peuvent être conservées plus longtemps, à condition que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée [5].
```

</details>

Temps : recherche 2.2 s · génération 22.2 s (2627 tokens lus, 270 écrits, 36.3 tokens/s) · contrôle de pertinence 3.5 s

## q04 — Que dois-je mettre dans la mention d'information d'un formulaire ?

Article attendu : RGPD art. 13 — passage [1].

### Réponse du copilote

> Vous devez inclure dans la mention d'information d'un formulaire les éléments suivants : l'identité et les coordonnées du responsable du traitement, le cas échéant du représentant ou du délégué à la protection des données ; les finalités du traitement et la base juridique du traitement ; les intérêts légitimes poursuivis (lorsque le traitement est fondé sur l'article 6, paragraphe 1, point f) ) ; les destinataires ou catégories de destinataires des données ; le cas échéant, le fait d'effectuer un transfert vers un pays tiers ou une organisation internationale et les garanties ou la décision d'adéquation concernant ce transfert ; la durée de conservation des données ou les critères utilisés pour déterminer cette durée ; l'existence du droit de demander l'accès, la rectification, l'effacement, une limitation du traitement, de s'opposer au traitement ou de porter une réclamation ; le droit de retirer son consentement à tout moment (lorsque le traitement est fondé sur l'article 6, paragraphe 1, point a) ou sur l'article 9, paragraphe 2, point a) ) ; le droit d'introduire une réclamation auprès d'une autorité de contrôle ; des informations sur le caractère réglementaire ou contractuel de l'exigence de données et les conséquences de la non-fourniture ; l'existence d'une prise de décision automatisée (profilage) avec, au moins dans ce cas, des informations sur la logique sous-jacente et l'importance et les conséquences prévues pour la personne concernée ; la source des données, le cas échéant, si elles sont accessibles au public ; et la manière dont les informations sont fournies (par écrit ou électronique, de façon concise, transparente, compréhensible, accessible, en termes clairs et simples, notamment pour les enfants) [1], [2], [4].

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
Vous devez inclure dans la mention d'information d'un formulaire les éléments suivants : l'identité et les coordonnées du responsable du traitement, le cas échéant du représentant ou du délégué à la protection des données ; les finalités du traitement et la base juridique du traitement ; les intérêts légitimes poursuivis (lorsque le traitement est fondé sur l'article 6, paragraphe 1, point f) ) ; les destinataires ou catégories de destinataires des données ; le cas échéant, le fait d'effectuer un transfert vers un pays tiers ou une organisation internationale et les garanties ou la décision d'adéquation concernant ce transfert ; la durée de conservation des données ou les critères utilisés pour déterminer cette durée ; l'existence du droit de demander l'accès, la rectification, l'effacement, une limitation du traitement, de s'opposer au traitement ou de porter une réclamation ; le droit de retirer son consentement à tout moment (lorsque le traitement est fondé sur l'article 6, paragraphe 1, point a) ou sur l'article 9, paragraphe 2, point a) ) ; le droit d'introduire une réclamation auprès d'une autorité de contrôle ; des informations sur le caractère réglementaire ou contractuel de l'exigence de données et les conséquences de la non-fourniture ; l'existence d'une prise de décision automatisée (profilage) avec, au moins dans ce cas, des informations sur la logique sous-jacente et l'importance et les conséquences prévues pour la personne concernée ; la source des données, le cas échéant, si elles sont accessibles au public ; et la manière dont les informations sont fournies (par écrit ou électronique, de façon concise, transparente, compréhensible, accessible, en termes clairs et simples, notamment pour les enfants) [1], [2], [4].
```

</details>

Temps : recherche 2.2 s · génération 77.2 s (3244 tokens lus, 1858 écrits, 32.7 tokens/s) · contrôle de pertinence 9.9 s

## q05 — Une personne demande l'accès à ses données : quel délai pour répondre ?

Article attendu : RGPD art. 12, paragraphe 3 — passage [1].

### Réponse du copilote

> Le responsable du traitement doit répondre à la demande d'accès de la personne concernée dans un délai d'un mois à compter de la réception de la demande [1]. Ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes [1]. Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande [1]. Lorsque la demande est formulée par voie électronique, les informations sont fournies sous une forme électronique d'usage courant, à moins que la personne concernée ne demande qu'il en soit autrement [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. »
  [3] « Lorsque la personne concernée présente sa demande par voie électronique, les informations sont fournies sous une forme électronique d'usage courant, à moins que la personne concernée ne demande qu'il en soit autrement. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [3] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [4] RGPD — règlement (UE) 2016/679, article 12, paragraphe 4 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 3 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. »
- [3] « Lorsque la personne concernée présente sa demande par voie électronique, les informations sont fournies sous une forme électronique d'usage courant, à moins que la personne concernée ne demande qu'il en soit autrement. »

RÉPONSE :
Le responsable du traitement doit répondre à la demande d'accès de la personne concernée dans un délai d'un mois à compter de la réception de la demande [1]. Ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes [1]. Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande [1]. Lorsque la demande est formulée par voie électronique, les informations sont fournies sous une forme électronique d'usage courant, à moins que la personne concernée ne demande qu'il en soit autrement [3].
```

</details>

Temps : recherche 2.2 s · génération 31.4 s (2510 tokens lus, 355 écrits, 36.1 tokens/s) · contrôle de pertinence 4.6 s

## q06 — J'ai eu une fuite de données : que faire, et en combien de temps ?

Article attendu : RGPD art. 33 ou RGPD art. 34 — passage [1].

### Réponse du copilote

> Lors d'une fuite de données, le responsable du traitement doit notifier la violation à l'autorité de contrôle compétente dans les meilleurs délais, et, si possible, dans les 72 heures après en avoir pris connaissance, à moins que la violation ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques [1]. Cette notification doit inclure la nature de la violation, les catégories et le nombre approximatif de personnes concernées, le nom et les coordonnées du délégué à la protection des données ou d'un autre point de contact, les conséquences probables de la violation, et les mesures prises ou proposées pour y remédier [1]. Si la violation est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement doit également communiquer la violation à la personne concernée dans les meilleurs délais [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. Lorsque la notification à l'autorité de contrôle n'a pas lieu dans les 72 heures, elle est accompagnée des motifs du retard. »
  [1] « La notification visée au paragraphe 1 doit, à tout le moins: a) décrire la nature de la violation de données à caractère personnel y compris, si possible, les catégories et le nombre approximatif de personnes concernées par la violation et les catégories et le nombre approximatif d'enregistrements de données à caractère personnel concernés; »
  [2] « Lorsqu'une violation de données à caractère personnel est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement communique la violation de données à caractère personnel à la personne concernée dans les meilleurs délais. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 33 : Notification à l'autorité de contrôle d'une violation de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_33
  [2] RGPD — règlement (UE) 2016/679, article 34 : Communication à la personne concernée d'une violation de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_34
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 12 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [4] RGPD — règlement (UE) 2016/679, article 17 : Droit à l'effacement («droit à l'oubli»)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_17
  [5] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
Attention : 3 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1], [1], [1]) : ignoré(s).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. Lorsque la notification à l'autorité de contrôle n'a pas lieu dans les 72 heures, elle est accompagnée des motifs du retard. »
- [1] « La notification visée au paragraphe 1 doit, à tout le moins: a) décrire la nature de la violation de données à caractère personnel y compris, si possible, les catégories et le nombre approximatif de personnes concernées par la violation et les catégories et le nombre approximatif d'enregistrements de données à caractère personnel concernés; »
- [1] « La notification visée au paragraphe 1 doit, à tout le moins: b) communiquer le nom et les coordonnées du délégué à la protection des données ou d'un autre point de contact auprès duquel des informations supplémentaires peuvent être obtenues; »
- [1] « La notification visée au paragraphe 1 doit, à tout le moins: c) décrire les conséquences probables de la violation de données à caractère personnel; »
- [1] « La notification visée au paragraphe 1 doit, à tout le moins: d) décrire les mesures prises ou que le responsable du traitement propose de prendre pour remédier à la violation de données à caractère personnel, y compris, le cas échéant, les mesures pour en atténuer les éventuelles conséquences négatives. »
- [2] « Lorsqu'une violation de données à caractère personnel est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement communique la violation de données à caractère personnel à la personne concernée dans les meilleurs délais. »

RÉPONSE :
Lors d'une fuite de données, le responsable du traitement doit notifier la violation à l'autorité de contrôle compétente dans les meilleurs délais, et, si possible, dans les 72 heures après en avoir pris connaissance, à moins que la violation ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques [1]. Cette notification doit inclure la nature de la violation, les catégories et le nombre approximatif de personnes concernées, le nom et les coordonnées du délégué à la protection des données ou d'un autre point de contact, les conséquences probables de la violation, et les mesures prises ou proposées pour y remédier [1]. Si la violation est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement doit également communiquer la violation à la personne concernée dans les meilleurs délais [2].
```

</details>

Temps : recherche 2.2 s · génération 45.6 s (3689 tokens lus, 690 écrits, 33.0 tokens/s) · contrôle de pertinence 4.7 s

## q07 — Quand faut-il faire une analyse d'impact (AIPD) ?

Article attendu : RGPD art. 35, paragraphe 1 ou RGPD art. 35, paragraphe 3 — passage [1].

### Réponse du copilote

> Une analyse d'impact relative à la protection des données (AIPD) est requise dans les cas précisés à l'article 35, paragraphe 1, du RGPD : lorsqu’un traitement, notamment automatisé, est susceptible d’engendrer un risque élevé pour les droits et libertés des personnes physiques, comme dans les cas de traitement à grande échelle de données particulières ou de surveillance systématique à grande échelle [1]. Elle doit être effectuée avant le traitement, notamment dans les cas de traitement automatisé fondé sur le profilage ou de décisions produisant des effets juridiques [1]. Elle est également obligatoire avant le déploiement d’un système d’IA à haut risque, sauf dans les domaines spécifiques de l’annexe III, point 2 [4]. Cette obligation s’applique à la première utilisation du système d’IA à haut risque, et peut être renouvelée si les conditions ou les éléments de l’analyse changent [4]. En outre, les déployeurs peuvent s’appuyer sur des analyses d’impact existantes ou sur des analyses d’impact relative à la protection des données préalables [4]. L’analyse d’impact relative à la protection des données peut être utilisée comme base pour une analyse d’impact sur les droits fondamentaux, notamment dans les cas de systèmes d’IA à haut risque [5].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « L'analyse d'impact relative à la protection des données visée au paragraphe 1 est, en particulier, requise dans les cas suivants: a) l'évaluation systématique et approfondie d'aspects personnels concernant des personnes physiques, qui est fondée sur un traitement automatisé, y compris le profilage, et sur la base de laquelle sont prises des décisions produisant des effets juridiques à l'égard d'une personne physique ou l'affectant de manière significative de façon similaire; b) le traitement à grande échelle de catégories particulières de données visées à l'article 9, paragraphe 1, ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10; ou c) la surveillance systématique à grande échelle d'une zone accessible au public. »
  [2] « Lorsqu'un type de traitement, en particulier par le recours à de nouvelles technologies, et compte tenu de la nature, de la portée, du contexte et des finalités du traitement, est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, le responsable du traitement effectue, avant le traitement, une analyse de l'impact des opérations de traitement envisagées sur la protection des données à caractère personnel. Une seule et même analyse peut porter sur un ensemble d'opérations de traitement similaires qui présentent des risques élevés similaires. »
  [4] « Avant le déploiement d’un système d’IA à haut risque visé à l’article 6, paragraphe 2, à l’exception des systèmes d’IA à haut risque destinés à être utilisés dans le domaine visé à l’annexe III, point 2, les déployeurs qui sont des organismes de droit public ou des entités privées fournissant des services publics et les déployeurs de systèmes d’IA à haut risque visés à l’annexe III, points 5), b) et c), effectuent une analyse de l’impact sur les droits fondamentaux que l’utilisation de ce système peut produire. »
  [4] « L’obligation établie au paragraphe 1 s’applique à la première utilisation du système d’IA à haut risque. Le déployeur peut, dans des cas similaires, s’appuyer sur des analyses d’impact sur les droits fondamentaux effectuées précédemment ou sur des analyses d’impact existantes réalisées par le fournisseur. Si, au cours de l’utilisation du système d’IA à haut risque, le déployeur estime qu’un des éléments énumérés au paragraphe 1 a changé ou n’est plus à jour, il prend les mesures nécessaires pour mettre à jour les informations. »
  [5] « Le cas échéant, les déployeurs de systèmes d’IA à haut risque utilisent les informations fournies en application de l’article 13 du présent règlement pour se conformer à leur obligation de procéder à une analyse d’impact relative à la protection des données en vertu de l’article 35 du règlement (UE) 2016/679 ou de l’article 27 de la directive (UE) 2016/680. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 35, paragraphe 3 : Analyse d'impact relative à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [2] RGPD — règlement (UE) 2016/679, article 35, paragraphe 1 : Analyse d'impact relative à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [4] AI Act — règlement (UE) 2024/1689, article 27 : Analyse d’impact des systèmes d’IA à haut risque sur les droits fondamentaux (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_27
  [5] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 9 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 35, paragraphe 11 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
Attention : La réponse s'appuie sur le RGPD et l'AI Act sans dire de quel règlement vient chaque obligation : « Elle doit être effectuée avant le traitement, notamment dans les cas de traitement automatisé fondé sur le profilage ou … » (et 1 autre(s)).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « L'analyse d'impact relative à la protection des données visée au paragraphe 1 est, en particulier, requise dans les cas suivants: a) l'évaluation systématique et approfondie d'aspects personnels concernant des personnes physiques, qui est fondée sur un traitement automatisé, y compris le profilage, et sur la base de laquelle sont prises des décisions produisant des effets juridiques à l'égard d'une personne physique ou l'affectant de manière significative de façon similaire; b) le traitement à grande échelle de catégories particulières de données visées à l'article 9, paragraphe 1, ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10; ou c) la surveillance systématique à grande échelle d'une zone accessible au public. »
- [2] « Lorsqu'un type de traitement, en particulier par le recours à de nouvelles technologies, et compte tenu de la nature, de la portée, du contexte et des finalités du traitement, est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, le responsable du traitement effectue, avant le traitement, une analyse de l'impact des opérations de traitement envisagées sur la protection des données à caractère personnel. Une seule et même analyse peut porter sur un ensemble d'opérations de traitement similaires qui présentent des risques élevés similaires. »
- [4] « Avant le déploiement d’un système d’IA à haut risque visé à l’article 6, paragraphe 2, à l’exception des systèmes d’IA à haut risque destinés à être utilisés dans le domaine visé à l’annexe III, point 2, les déployeurs qui sont des organismes de droit public ou des entités privées fournissant des services publics et les déployeurs de systèmes d’IA à haut risque visés à l’annexe III, points 5), b) et c), effectuent une analyse de l’impact sur les droits fondamentaux que l’utilisation de ce système peut produire. »
- [4] « L’obligation établie au paragraphe 1 s’applique à la première utilisation du système d’IA à haut risque. Le déployeur peut, dans des cas similaires, s’appuyer sur des analyses d’impact sur les droits fondamentaux effectuées précédemment ou sur des analyses d’impact existantes réalisées par le fournisseur. Si, au cours de l’utilisation du système d’IA à haut risque, le déployeur estime qu’un des éléments énumérés au paragraphe 1 a changé ou n’est plus à jour, il prend les mesures nécessaires pour mettre à jour les informations. »
- [5] « Le cas échéant, les déployeurs de systèmes d’IA à haut risque utilisent les informations fournies en application de l’article 13 du présent règlement pour se conformer à leur obligation de procéder à une analyse d’impact relative à la protection des données en vertu de l’article 35 du règlement (UE) 2016/679 ou de l’article 27 de la directive (UE) 2016/680. »

RÉPONSE :
Une analyse d'impact relative à la protection des données (AIPD) est requise dans les cas précisés à l'article 35, paragraphe 1, du RGPD : lorsqu’un traitement, notamment automatisé, est susceptible d’engendrer un risque élevé pour les droits et libertés des personnes physiques, comme dans les cas de traitement à grande échelle de données particulières ou de surveillance systématique à grande échelle [1]. Elle doit être effectuée avant le traitement, notamment dans les cas de traitement automatisé fondé sur le profilage ou de décisions produisant des effets juridiques [1]. Elle est également obligatoire avant le déploiement d’un système d’IA à haut risque, sauf dans les domaines spécifiques de l’annexe III, point 2 [4]. Cette obligation s’applique à la première utilisation du système d’IA à haut risque, et peut être renouvelée si les conditions ou les éléments de l’analyse changent [4]. En outre, les déployeurs peuvent s’appuyer sur des analyses d’impact existantes ou sur des analyses d’impact relative à la protection des données préalables [4]. L’analyse d’impact relative à la protection des données peut être utilisée comme base pour une analyse d’impact sur les droits fondamentaux, notamment dans les cas de systèmes d’IA à haut risque [5].
```

</details>

Temps : recherche 2.2 s · génération 49.0 s (2809 tokens lus, 1117 écrits, 34.3 tokens/s) · contrôle de pertinence 7.8 s

## q08 — Mon chatbot doit-il dire aux clients qu'il est une IA ?

Article attendu : AI Act art. 50, paragraphe 1 — passage [1].

### Réponse du copilote

> Oui : votre chatbot doit indiquer clairement qu’il s’agit d’un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation [1].

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
Attention : La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui: votre chatbot doit indiquer clairement qu’il s’agit d’un système d’IA, sauf si cela ressort clairement du point de … ». Vérifiez qui est concerné.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »

RÉPONSE :  
Oui : votre chatbot doit indiquer clairement qu’il s’agit d’un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation [1].
```

</details>

Temps : recherche 2.2 s · génération 33.6 s (3971 tokens lus, 196 écrits, 33.0 tokens/s) · contrôle de pertinence 4.1 s

## q09 — Puis-je utiliser une IA pour trier des CV ?

Article attendu : AI Act annexe III, point 4 ou AI Act art. 26 — passage [3].

### Réponse du copilote

> Oui, vous pouvez utiliser une IA pour trier des CV, car ce type d’action relève des systèmes d’IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, notamment pour analyser et filtrer les candidatures [3]. Cependant, si ce système est classé comme un système d’IA à haut risque (comme défini dans l’annexe III), il doit être soumis à un contrôle humain pour prévenir ou réduire les risques pour la santé, la sécurité ou les droits fondamentaux [1].

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
Oui, vous pouvez utiliser une IA pour trier des CV, car ce type d’action relève des systèmes d’IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, notamment pour analyser et filtrer les candidatures [3]. Cependant, si ce système est classé comme un système d’IA à haut risque (comme défini dans l’annexe III), il doit être soumis à un contrôle humain pour prévenir ou réduire les risques pour la santé, la sécurité ou les droits fondamentaux [1].
```

</details>

Temps : recherche 2.2 s · génération 33.4 s (3645 tokens lus, 304 écrits, 33.5 tokens/s) · contrôle de pertinence 3.6 s

## q10 — Mes salariés ou bénévoles utilisent une IA générative : ai-je des obligations ?

Article attendu : AI Act art. 4 — passage [5].

### Réponse du copilote

> Oui : vous avez des obligations en tant que déployeur de systèmes d’IA, car vos salariés ou bénévoles utilisent une IA générative. Selon l’AI Act, article 50, paragraphes 1 et 2, les déployeurs doivent veiller à ce que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation [1]. De plus, si les contenus générés par l’IA sont publiés dans le but d’informer le public sur des questions d’intérêt public, vous devez indiquer que le texte a été généré ou manipulé par une IA [2]. Enfin, vous devez prendre des mesures pour favoriser la maîtrise de l’IA par vos salariés ou bénévoles, en tenant compte de leurs connaissances, de leur formation et du contexte d’utilisation [5]. Cette obligation ne vous oblige pas à garantir un niveau spécifique de maîtrise de l’IA par un individu [5].

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
Attention : La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Selon l’AI Act, article 50, paragraphes 1 et 2, les déployeurs doivent veiller à ce que les personnes physiques … ». Vérifiez qui est concerné.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. Cette obligation ne s’applique pas aux systèmes d’IA dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers, sauf si ces systèmes sont mis à la disposition du public pour permettre le signalement d’une infraction pénale. »
- [2] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. Cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. Lorsque le contenu fait partie d’une œuvre ou d’un programme manifestement artistique, créatif, satirique, fictif ou analogue, les obligations de transparence énoncées au présent paragraphe se limitent à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre. Les déployeurs d’un système d’IA qui génère ou manipule des textes publiés dans le but d’informer le public sur des questions d’intérêt public indiquent que le texte a été généré ou manipulé par une IA. Cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière, ou lorsque le contenu généré par l’IA a fait l’objet d’un processus d’examen humain ou de contrôle éditorial et lorsqu’une personne physique ou morale assume la responsabilité éditoriale de la publication du contenu. »
- [5] « Les fournisseurs et les déployeurs de systèmes d'IA prennent des mesures pour favoriser le développement de la maîtrise de l'IA par leur personnel et les autres personnes s'occupant du fonctionnement et de l'utilisation des systèmes d'IA pour leur compte, en prenant en considération leurs connaissances techniques, leur expérience, leur éducation et leur formation, ainsi que le contexte dans which les systèmes d'IA sont destinés à être utilisés, et en tenant compte des personnes ou des groupes de personnes à l'égard desquels les systèmes d'IA sont destinés à être utilisés. Cette obligation ne contraint pas les fournisseurs ou les déployeurs à garantir un niveau spécifique de maîtrise de l'IA par un individu. »

RÉPONSE :
Oui : vous avez des obligations en tant que déployeur de systèmes d’IA, car vos salariés ou bénévoles utilisent une IA générative. Selon l’AI Act, article 50, paragraphes 1 et 2, les déployeurs doivent veiller à ce que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation [1]. De plus, si les contenus générés par l’IA sont publiés dans le but d’informer le public sur des questions d’intérêt public, vous devez indiquer que le texte a été généré ou manipulé par une IA [2]. Enfin, vous devez prendre des mesures pour favoriser la maîtrise de l’IA par vos salariés ou bénévoles, en tenant compte de leurs connaissances, de leur formation et du contexte d’utilisation [5]. Cette obligation ne vous oblige pas à garantir un niveau spécifique de maîtrise de l’IA par un individu [5].
```

</details>

Temps : recherche 2.2 s · génération 42.1 s (2422 tokens lus, 1027 écrits, 35.5 tokens/s) · contrôle de pertinence 6.4 s

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
RÉPONSE : Les textes trouvés ne traitent pas de ce point.
```

</details>

Temps : recherche 2.1 s · génération 11.8 s (2167 tokens lus, 26 écrits, 38.9 tokens/s)

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
RÉPONSE : Les textes trouvés ne traitent pas de la déclaration d'impôts.
```

</details>

Temps : recherche 2.1 s · génération 18.9 s (3004 tokens lus, 32 écrits, 36.7 tokens/s)
