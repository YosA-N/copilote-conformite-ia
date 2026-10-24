# Réponses du copilote — v1

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 25/10/2026 à 01:37 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen3:4b-instruct` via Ollama 0.40.10 — température 0.1, contexte 8192 tokens, couches sur la carte graphique : toutes, 1500 tokens au plus par réponse
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_v0.jsonl` (10) et `eval/questions_offtopic_v0.jsonl` (2, hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q01 | Dois-je désigner un DPO ? | 1/1 | non | La réponse ne cite aucun passage : vérifiez-la avec les extraits et les sources. | 43 s |
| q02 | Dois-je tenir un registre des traitements ? | 3/3 | non | La réponse ne cite aucun passage : vérifiez-la avec les extraits et les sources. | 30 s |
| q03 | Combien de temps puis-je garder les données de mes clients ou adhérents ? | 1/2 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([4]) : ignoré(s).; La réponse ne cite aucun passage : vérifiez-la avec les extraits et les sources. | 26 s |
| q04 | Que dois-je mettre dans la mention d'information d'un formulaire ? | 1/2 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1]) : ignoré(s).; La réponse cite [1], [4] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations. | 61 s |
| q05 | Une personne demande l'accès à ses données : quel délai pour répondre ? | 1/1 | non | La réponse ne cite aucun passage : vérifiez-la avec les extraits et les sources. | 22 s |
| q06 | J'ai eu une fuite de données : que faire, et en combien de temps ? | 4/4 | non | La réponse ne cite aucun passage : vérifiez-la avec les extraits et les sources. | 36 s |
| q07 | Quand faut-il faire une analyse d'impact (AIPD) ? | 4/4 | non | La réponse ne cite aucun passage : vérifiez-la avec les extraits et les sources. | 30 s |
| q08 | Mon chatbot doit-il dire aux clients qu'il est une IA ? | 1/1 | non | La réponse ne cite aucun passage : vérifiez-la avec les extraits et les sources. | 29 s |
| q09 | Puis-je utiliser une IA pour trier des CV ? | 1/1 | non | La réponse ne cite aucun passage : vérifiez-la avec les extraits et les sources. | 30 s |
| q10 | Mes salariés ou bénévoles utilisent une IA générative : ai-je des obligations ? | 4/4 | non | — | 27 s |
| h01 | Quel est le taux de TVA en France ? | 0/0 | oui | — | 19 s |
| h02 | Comment faire une déclaration d'impôts ? | 0/0 | oui | — | 20 s |

## q01 — Dois-je désigner un DPO ?

Article attendu : RGPD art. 37 — passage [1].

### Réponse du copilote

> Oui, vous devez désigner un délégué à la protection des données (DPO) si vos activités de traitement répondent à l’un des cas suivants : si vous êtes une autorité publique ou un organisme public (sauf juridictions), si vos activités consistent en des opérations de traitement à grande échelle nécessitant un suivi régulier des personnes concernées, ou si vous traitez à grande échelle des catégories particulières de données (comme les données sensibles ou liées à des condamnations). Si aucun de ces cas ne s’applique, vous pouvez choisir de désigner un DPO, mais cela n’est pas obligatoire sauf si le droit de l’Union ou d’un État membre l’exige.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le responsable du traitement et le sous-traitant désignent en tout état de cause un délégué à la protection des données lorsque:   … a) le traitement est effectué par une autorité publique ou un organisme public, à l'exception des juridictions agissant dans l'exercice de leur fonction juridictionnelle; … b) les activités de base du responsable du traitement ou du sous-traitant consistent en des opérations de traitement qui, du fait de leur nature, de leur portée et/ou de leurs finalités, exigent un suivi régulier et systématique à grande échelle des personnes concernées; ou … c) les activités de base du responsable du traitement ou du sous-traitant consistent en un traitement à grande échelle de catégories particulières de données visées à l’article 9 ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l’article 10. … 4. Dans les cas autres que ceux visés au paragraphe 1, le responsable du traitement ou le sous-traitant ou les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent désigner ou, si le droit de l'Union ou le droit d'un État membre l'exige, sont tenus de désigner un délégué à la protection des données. »

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
Attention : La réponse ne cite aucun passage : vérifiez-la avec les extraits et les sources.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
[1] Le responsable du traitement et le sous-traitant désignent en tout état de cause un délégué à la protection des données lorsque:  
a) le traitement est effectué par une autorité publique ou un organisme public, à l'exception des juridictions agissant dans l'exercice de leur fonction juridictionnelle;  
b) les activités de base du responsable du traitement ou du sous-traitant consistent en des opérations de traitement qui, du fait de leur nature, de leur portée et/ou de leurs finalités, exigent un suivi régulier et systématique à grande échelle des personnes concernées; ou  
c) les activités de base du responsable du traitement ou du sous-traitant consistent en un traitement à grande échelle de catégories particulières de données visées à l’article 9 ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l’article 10.  
4. Dans les cas autres que ceux visés au paragraphe 1, le responsable du traitement ou le sous-traitant ou les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent désigner ou, si le droit de l'Union ou le droit d'un État membre l'exige, sont tenus de désigner un délégué à la protection des données.  

RÉPONSE :  
Oui, vous devez désigner un délégué à la protection des données (DPO) si vos activités de traitement répondent à l’un des cas suivants : si vous êtes une autorité publique ou un organisme public (sauf juridictions), si vos activités consistent en des opérations de traitement à grande échelle nécessitant un suivi régulier des personnes concernées, ou si vous traitez à grande échelle des catégories particulières de données (comme les données sensibles ou liées à des condamnations). Si aucun de ces cas ne s’applique, vous pouvez choisir de désigner un DPO, mais cela n’est pas obligatoire sauf si le droit de l’Union ou d’un État membre l’exige.
```

</details>

Temps : recherche 2.4 s · génération 40.8 s (2391 tokens lus, 494 écrits, 36.3 tokens/s)

## q02 — Dois-je tenir un registre des traitements ?

Article attendu : RGPD art. 30 — passage [1].

### Réponse du copilote

> Oui, vous devez tenir un registre des traitements si vous êtes un responsable du traitement, sauf si votre entreprise compte moins de 250 employés et que le traitement est occasionnel, sans risque pour les droits et libertés des personnes concernées. Ce registre doit inclure les finalités, les données concernées, les destinataires et les mesures de sécurité, et doit être sous forme écrite ou électronique.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Chaque responsable du traitement et, le cas échéant, le représentant du responsable du traitement tiennent un registre des activités de traitement effectuées sous leur responsabilité. »
  [1] « Les registres visés aux paragraphes 1 et 2 se présentent sous une forme écrite y compris la forme électronique. »
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
Attention : La réponse ne cite aucun passage : vérifiez-la avec les extraits et les sources.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
[1] Chaque responsable du traitement et, le cas échéant, le représentant du responsable du traitement tiennent un registre des activités de traitement effectuées sous leur responsabilité.  
[1] Les registres visés aux paragraphes 1 et 2 se présentent sous une forme écrite y compris la forme électronique.  
[1] Les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10.

RÉPONSE :  
Oui, vous devez tenir un registre des traitements si vous êtes un responsable du traitement, sauf si votre entreprise compte moins de 250 employés et que le traitement est occasionnel, sans risque pour les droits et libertés des personnes concernées. Ce registre doit inclure les finalités, les données concernées, les destinataires et les mesures de sécurité, et doit être sous forme écrite ou électronique.
```

</details>

Temps : recherche 5.2 s · génération 24.7 s (2299 tokens lus, 320 écrits, 36.6 tokens/s)

## q03 — Combien de temps puis-je garder les données de mes clients ou adhérents ?

Article attendu : RGPD art. 5 — passage [4].

### Réponse du copilote

> Vous pouvez garder les données de vos clients ou adhérents pendant une durée n'excédant pas celle nécessaire aux finalités pour lesquelles elles sont traitées. Si vous les conservez plus longtemps, cela ne peut se faire que pour des fins archivistiques dans l'intérêt public, de recherche scientifique ou historique, ou de statistiques, à condition de mettre en œuvre des mesures techniques et organisationnelles appropriées pour protéger les droits et libertés des personnes concernées.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [4] « les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée (limitation de la conservation); »

Sources citées :
  [4] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 4, définition 3 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [2] RGPD — règlement (UE) 2016/679, article 18 : Droit à la limitation du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_18
  [3] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([4]) : ignoré(s).
Attention : La réponse ne cite aucun passage : vérifiez-la avec les extraits et les sources.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
[4] « les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée (limitation de la conservation); »  
[4] « les données à caractère personnel doivent être conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées; »  

RÉPONSE :  
Vous pouvez garder les données de vos clients ou adhérents pendant une durée n'excédant pas celle nécessaire aux finalités pour lesquelles elles sont traitées. Si vous les conservez plus longtemps, cela ne peut se faire que pour des fins archivistiques dans l'intérêt public, de recherche scientifique ou historique, ou de statistiques, à condition de mettre en œuvre des mesures techniques et organisationnelles appropriées pour protéger les droits et libertés des personnes concernées.
```

</details>

Temps : recherche 2.2 s · génération 24.0 s (2262 tokens lus, 300 écrits, 36.7 tokens/s)

## q04 — Que dois-je mettre dans la mention d'information d'un formulaire ?

Article attendu : RGPD art. 13 — passage [1].

### Réponse du copilote

> Dans la mention d'information d'un formulaire, tu dois inclure :  
> - l'identité et les coordonnées du responsable du traitement (et, le cas échéant, de son représentant) [1] ;  
> - les finalités du traitement et la base juridique du traitement [1] ;  
> - les destinataires ou catégories de destinataires des données [1] ;  
> - la durée de conservation des données ou les critères utilisés pour déterminer cette durée [1, 2] ;  
> - le droit de demander l'accès, la rectification, l'effacement ou une limitation du traitement, le droit de s'opposer au traitement et le droit à la portabilité des données [1, 2] ;  
> - le droit de retirer son consentement à tout moment [1, 2] ;  
> - le droit d'introduire une réclamation auprès d'une autorité de contrôle [1, 2] ;  
> - l'existence d'une prise de décision automatisée (comme un profilage) et des informations sur la logique sous-jacente, ainsi que sur l'importance et les conséquences prévues pour la personne concernée [1, 2] ;  
> - la source des données et si elles sont accessibles au public [2].  
>
> Ces informations doivent être fournies de manière claire, concise, transparente et compréhensible, notamment pour les enfants, et peuvent être données par écrit ou par voie électronique [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « a) la durée pendant laquelle les données à caractère personnel seront conservées ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée;   … b) lorsque le traitement est fondé sur l'article 6, paragraphe 1, point f), les intérêts légitimes poursuivis par le responsable du traitement ou par un tiers; … c) l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ainsi que du droit de s'opposer au traitement et du droit à la portabilité des données; … d) lorsque le traitement est fondé sur l'article 6, paragraphe 1, point a), ou sur l'article 9, paragraphe 2, point a), l'existence du droit de retirer le consentement à tout moment, sans porter atteinte à la licéité du traitement fondé sur le consentement effectué avant le retrait de celui-ci; … e) le droit d'introduire une réclamation auprès d'une autorité de contrôle; … f) la source d'où proviennent les données à caractère personnel et, le cas échéant, une mention indiquant qu'elles sont issues ou non de sources accessibles au public; … g) l'existence d'une prise de décision automatisée, y compris un profilage, visée à l'article 22, paragraphes 1 et 4, et, au moins en pareils cas, des informations utiles concernant la logique sous-jacente, ainsi que l'importance et les conséquences prévues de ce traitement pour la personne concernée. »

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
  [5] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1]) : ignoré(s).
Attention : La réponse cite [1], [4] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
[1] a) l'identité et les coordonnées du responsable du traitement et, le cas échéant, du représentant du responsable du traitement  
b) le cas échéant, les coordonnées du délégué à la protection des données;  
c) les finalités du traitement auquel sont destinées les données à caractère personnel ainsi que la base juridique du traitement;  
d) lorsque le traitement est fondé sur l'article 6, paragraphe 1, point f), les intérêts légitimes poursuivis par le responsable du traitement ou par un tiers;  
e) les destinataires ou les catégories de destinataires des données à caractère personnel, s'ils existent;  
f) le cas échéant, le fait que le responsable du traitement a l'intention d'effectuer un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale, et l'existence ou l'absence d'une décision d'adéquation rendue par la Commission ou, dans le cas des transferts visés à l'article 46 ou 47, ou à l'article 49, paragraphe 1, deuxième alinéa, la référence aux garanties appropriées ou adaptées et les moyens d'en obtenir une copie ou l'endroit où elles ont été mises à disposition;  
2. a) la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée;  
b) l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ou du droit de s'opposer au traitement et du droit à la portabilité des données;  
c) lorsque le traitement est fondé sur l'article 6, paragraphe 1, point a), ou sur l'article 9, paragraphe 2, point a), l'existence du droit de retirer son consentement à tout moment, sans porter atteinte à la licéité du traitement fondé sur le consentement effectué avant le retrait de celui-ci;  
d) le droit d'introduire une réclamation auprès d'une autorité de contrôle;  
e) des informations sur la question de savoir si l'exigence de fourniture de données à caractère personnel a un caractère réglementaire ou contractuel ou si elle conditionne la conclusion d'un contrat et si la personne concernée est tenue de fournir les données à caractère personnel, ainsi que sur les conséquences éventuelles de la non-fourniture de ces données;  
f) l'existence d'une prise de décision automatisée, y compris un profilage, visée à l'article 22, paragraphes 1 et 4, et, au moins en pareils cas, des informations utiles concernant la logique sous-jacente, ainsi que l'importance et les conséquences prévues de ce traitement pour la personne concernée.  

[2] a) la durée pendant laquelle les données à caractère personnel seront conservées ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée;  
b) lorsque le traitement est fondé sur l'article 6, paragraphe 1, point f), les intérêts légitimes poursuivis par le responsable du traitement ou par un tiers;  
c) l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ainsi que du droit de s'opposer au traitement et du droit à la portabilité des données;  
d) lorsque le traitement est fondé sur l'article 6, paragraphe 1, point a), ou sur l'article 9, paragraphe 2, point a), l'existence du droit de retirer le consentement à tout moment, sans porter atteinte à la licéité du traitement fondé sur le consentement effectué avant le retrait de celui-ci;  
e) le droit d'introduire une réclamation auprès d'une autorité de contrôle;  
f) la source d'où proviennent les données à caractère personnel et, le cas échéant, une mention indiquant qu'elles sont issues ou non de sources accessibles au public;  
g) l'existence d'une prise de décision automatisée, y compris un profilage, visée à l'article 22, paragraphes 1 et 4, et, au moins en pareils cas, des informations utiles concernant la logique sous-jacente, ainsi que l'importance et les conséquences prévues de ce traitement pour la personne concernée.

RÉPONSE :  
Dans la mention d'information d'un formulaire, tu dois inclure :  
- l'identité et les coordonnées du responsable du traitement (et, le cas échéant, de son représentant) [1a] ;  
- les finalités du traitement et la base juridique du traitement [1c] ;  
- les destinataires ou catégories de destinataires des données [1e] ;  
- la durée de conservation des données ou les critères utilisés pour déterminer cette durée [1a, 2a] ;  
- le droit de demander l'accès, la rectification, l'effacement ou une limitation du traitement, le droit de s'opposer au traitement et le droit à la portabilité des données [1b, 2c] ;  
- le droit de retirer son consentement à tout moment [1c, 2d] ;  
- le droit d'introduire une réclamation auprès d'une autorité de contrôle [1d, 2e] ;  
- l'existence d'une prise de décision automatisée (comme un profilage) et des informations sur la logique sous-jacente, ainsi que sur l'importance et les conséquences prévues pour la personne concernée [1f, 2g] ;  
- la source des données et si elles sont accessibles au public [2f].  

Ces informations doivent être fournies de manière claire, concise, transparente et compréhensible, notamment pour les enfants, et peuvent être données par écrit ou par voie électronique [4].
```

</details>

Temps : recherche 2.2 s · génération 58.9 s (2506 tokens lus, 1413 écrits, 34.4 tokens/s)

## q05 — Une personne demande l'accès à ses données : quel délai pour répondre ?

Article attendu : RGPD art. 12 — passage [1].

### Réponse du copilote

> Le responsable du traitement doit répondre à la demande d'accès dans un délai de un mois à compter de la réception de la demande. Ce délai peut être prolongé de deux mois en cas de complexité ou de nombre important de demandes, et le responsable doit informer la personne concernée de cette prolongation.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. »

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
Attention : La réponse ne cite aucun passage : vérifiez-la avec les extraits et les sources.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
[1] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. »  

RÉPONSE : Le responsable du traitement doit répondre à la demande d'accès dans un délai de un mois à compter de la réception de la demande. Ce délai peut être prolongé de deux mois en cas de complexité ou de nombre important de demandes, et le responsable doit informer la personne concernée de cette prolongation.
```

</details>

Temps : recherche 2.2 s · génération 19.6 s (2145 tokens lus, 179 écrits, 36.8 tokens/s)

## q06 — J'ai eu une fuite de données : que faire, et en combien de temps ?

Article attendu : RGPD art. 33 ou RGPD art. 34 — passage [1].

### Réponse du copilote

> Si vous avez eu une fuite de données, vous devez la signaler à l'autorité de contrôle dans les meilleurs délais, et en tout cas au plus tard 72 heures après avoir pris connaissance de la fuite. Si vous ne pouvez pas communiquer toutes les informations en même temps, vous pouvez les transmettre de manière échelonnée sans retard supplémentaire.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. »
  [1] « Lorsque la notification à l'autorité de contrôle n'a pas lieu dans les 72 heures, elle est accompagnée des motifs du retard. »
  [1] « La notification visée au paragraphe 1 doit, à tout le moins: a) décrire la nature de la violation de données à caractère personnel y compris, si possible, les catégories et le nombre approximatif de personnes concernées par la violation et les catégories et le nombre approximatif d'enregistrements de données à caractère personnel concernés; »
  [1] « Si, et dans la mesure où, il n'est pas possible de fournir toutes les informations en même temps, les informations peuvent être communiquées de manière échelonnée sans autre retard indu. »

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
Attention : La réponse ne cite aucun passage : vérifiez-la avec les extraits et les sources.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. »
- [1] « Lorsque la notification à l'autorité de contrôle n'a pas lieu dans les 72 heures, elle est accompagnée des motifs du retard. »
- [1] « La notification visée au paragraphe 1 doit, à tout le moins: a) décrire la nature de la violation de données à caractère personnel y compris, si possible, les catégories et le nombre approximatif de personnes concernées par la violation et les catégories et le nombre approximatif d'enregistrements de données à caractère personnel concernés; »
- [1] « Si, et dans la mesure où, il n'est pas possible de fournir toutes les informations en même temps, les informations peuvent être communiquées de manière échelonnée sans autre retard indu. »

RÉPONSE :  
Si vous avez eu une fuite de données, vous devez la signaler à l'autorité de contrôle dans les meilleurs délais, et en tout cas au plus tard 72 heures après avoir pris connaissance de la fuite. Si vous ne pouvez pas communiquer toutes les informations en même temps, vous pouvez les transmettre de manière échelonnée sans retard supplémentaire.
```

</details>

Temps : recherche 2.2 s · génération 33.5 s (3073 tokens lus, 367 écrits, 34.2 tokens/s)

## q07 — Quand faut-il faire une analyse d'impact (AIPD) ?

Article attendu : RGPD art. 35 — passage [1].

### Réponse du copilote

> Il faut faire une analyse d'impact (AIPD) quand le traitement est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, notamment dans des cas précis comme l'évaluation systématique d'aspects personnels fondée sur un traitement automatisé, le traitement à grande échelle de données sensibles ou la surveillance systématique à grande échelle d'une zone accessible au public. Cette analyse doit être effectuée avant le traitement, surtout si le traitement implique de nouvelles technologies ou si le risque évolue.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « l'analyse d'impact relative à la protection des données visée au paragraphe 1 est, en particulier, requise dans les cas suivants: a) l'évaluation systématique et approfondie d'aspects personnels concernant des personnes physiques, qui est fondée sur un traitement automatisé, y compris le profilage, et sur la base de laquelle sont prises des décisions produisant des effets juridiques à l'égard d'une personne physique ou l'affectant de manière significative de façon similaire; b) le traitement à grande échelle de catégories particulières de données visées à l'article 9, paragraphe 1, ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10; ou c) la surveillance systématique à grande échelle d'une zone accessible au public. »
  [3] « Lorsqu'un type de traitement, en particulier par le recours à de nouvelles technologies, et compte tenu de la nature, de la portée, du contexte et des finalités du traitement, est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, le responsable du traitement effectue, avant le traitement, une analyse de l'impact des opérations de traitement envisagées sur la protection des données à caractère personnel. »
  [4] « L'analyse contient au moins: a) une description systématique des opérations de traitement envisagées et des finalités du traitement, y compris, le cas échéant, l'intérêt légitime poursuivi par le responsable du traitement; b) une évaluation de la nécessité et de la proportionnalité des opérations de traitement au regard des finalités; c) une évaluation des risques pour les droits et libertés des personnes concernées conformément au paragraphe 1; et d) les mesures envisagées pour faire face aux risques, y compris les garanties, mesures et mécanismes de sécurité visant à assurer la protection des données à caractère personnel et à apporter la preuve du respect du présent règlement, compte tenu des droits et des intérêts légitimes des personnes concernées et des autres personnes affectées. »
  [2] « Si nécessaire, le responsable du traitement procède à un examen afin d'évaluer si le traitement est effectué conformément à l'analyse d'impact relative à la protection des données, au moins quand il se produit une modification du risque présenté par les opérations de traitement. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 35, paragraphe 3 : Analyse d'impact relative à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [2] RGPD — règlement (UE) 2016/679, article 35, paragraphe 11 : Analyse d'impact relative à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [3] RGPD — règlement (UE) 2016/679, article 35, paragraphe 1 : Analyse d'impact relative à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [4] RGPD — règlement (UE) 2016/679, article 35, paragraphe 7 : Analyse d'impact relative à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
Passages consultés mais non cités :
  [5] RGPD — règlement (UE) 2016/679, article 35, paragraphe 4 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
Attention : La réponse ne cite aucun passage : vérifiez-la avec les extraits et les sources.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
[1] « l'analyse d'impact relative à la protection des données visée au paragraphe 1 est, en particulier, requise dans les cas suivants: a) l'évaluation systématique et approfondie d'aspects personnels concernant des personnes physiques, qui est fondée sur un traitement automatisé, y compris le profilage, et sur la base de laquelle sont prises des décisions produisant des effets juridiques à l'égard d'une personne physique ou l'affectant de manière significative de façon similaire; b) le traitement à grande échelle de catégories particulières de données visées à l'article 9, paragraphe 1, ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10; ou c) la surveillance systématique à grande échelle d'une zone accessible au public. »  
[3] « Lorsqu'un type de traitement, en particulier par le recours à de nouvelles technologies, et compte tenu de la nature, de la portée, du contexte et des finalités du traitement, est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, le responsable du traitement effectue, avant le traitement, une analyse de l'impact des opérations de traitement envisagées sur la protection des données à caractère personnel. »  
[4] « L'analyse contient au moins: a) une description systématique des opérations de traitement envisagées et des finalités du traitement, y compris, le cas échéant, l'intérêt légitime poursuivi par le responsable du traitement; b) une évaluation de la nécessité et de la proportionnalité des opérations de traitement au regard des finalités; c) une évaluation des risques pour les droits et libertés des personnes concernées conformément au paragraphe 1; et d) les mesures envisagées pour faire face aux risques, y compris les garanties, mesures et mécanismes de sécurité visant à assurer la protection des données à caractère personnel et à apporter la preuve du respect du présent règlement, compte tenu des droits et des intérêts légitimes des personnes concernées et des autres personnes affectées. »  
[2] « Si nécessaire, le responsable du traitement procède à un examen afin d'évaluer si le traitement est effectué conformément à l'analyse d'impact relative à la protection des données, au moins quand il se produit une modification du risque présenté par les opérations de traitement. »

RÉPONSE :  
Il faut faire une analyse d'impact (AIPD) quand le traitement est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, notamment dans des cas précis comme l'évaluation systématique d'aspects personnels fondée sur un traitement automatisé, le traitement à grande échelle de données sensibles ou la surveillance systématique à grande échelle d'une zone accessible au public. Cette analyse doit être effectuée avant le traitement, surtout si le traitement implique de nouvelles technologies ou si le risque évolue.
```

</details>

Temps : recherche 2.2 s · génération 28.1 s (1365 tokens lus, 731 écrits, 37.9 tokens/s)

## q08 — Mon chatbot doit-il dire aux clients qu'il est une IA ?

Article attendu : AI Act art. 50 — passage [1].

### Réponse du copilote

> Oui, votre chatbot doit dire aux clients qu’il est une IA, sauf si, dans le contexte d’utilisation, une personne physique normalement informée et raisonnablement attentive pourrait considérer que l’interaction avec un système d’IA est clairement prévue ou acceptée. Cela dépend du contexte : par exemple, si le chatbot est utilisé dans un domaine comme la prévention ou la détection d’infractions pénales, ou s’il est mis à disposition du public pour signaler une infraction, l’obligation peut être suspendue. Sinon, la transparence est obligatoire.

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
  [3] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 3 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [4] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14
  [5] AI Act — règlement (UE) 2024/1689, annexe III, point 5 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
Attention : La réponse ne cite aucun passage : vérifiez-la avec les extraits et les sources.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
[1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »

RÉPONSE :  
Oui, votre chatbot doit dire aux clients qu’il est une IA, sauf si, dans le contexte d’utilisation, une personne physique normalement informée et raisonnablement attentive pourrait considérer que l’interaction avec un système d’IA est clairement prévue ou acceptée. Cela dépend du contexte : par exemple, si le chatbot est utilisé dans un domaine comme la prévention ou la détection d’infractions pénales, ou s’il est mis à disposition du public pour signaler une infraction, l’obligation peut être suspendue. Sinon, la transparence est obligatoire.
```

</details>

Temps : recherche 2.2 s · génération 26.7 s (2656 tokens lus, 261 écrits, 35.1 tokens/s)

## q09 — Puis-je utiliser une IA pour trier des CV ?

Article attendu : AI Act annexe III, point 4 ou AI Act art. 26 — passage [3].

### Réponse du copilote

> Oui, vous pouvez utiliser une IA pour trier des CV, car cela relève des systèmes d’IA à haut risque visés dans le domaine de l’emploi, de la gestion de la main-d’œuvre et de l’accès à l’emploi indépendant. Cela signifie que, si vous utilisez une telle IA, vous devez appliquer les exigences spécifiques de contrôle humain et de prévention des biais prévues par l’AI Act.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats »

Sources citées :
  [3] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14
  [2] AI Act — règlement (UE) 2024/1689, article 4 bis : Traitement de catégories particulières de données à caractère personnel à des fins de détection et de correction des biais
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_4a
  [4] AI Act — règlement (UE) 2024/1689, article 59, paragraphe 1, point j) : Traitement ultérieur de données à caractère personnel en vue du développement de certains systèmes d’IA dans l’intérêt public dans le cadre du bac à sable réglementaire de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_59
  [5] AI Act — règlement (UE) 2024/1689, article 59, paragraphe 3 : Traitement ultérieur de données à caractère personnel en vue du développement de certains systèmes d’IA dans l’intérêt public dans le cadre du bac à sable réglementaire de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_59
Attention : La réponse ne cite aucun passage : vérifiez-la avec les extraits et les sources.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
[3] « systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats »  

RÉPONSE :  
Oui, vous pouvez utiliser une IA pour trier des CV, car cela relève des systèmes d’IA à haut risque visés dans le domaine de l’emploi, de la gestion de la main-d’œuvre et de l’accès à l’emploi indépendant. Cela signifie que, si vous utilisez une telle IA, vous devez appliquer les exigences spécifiques de contrôle humain et de prévention des biais prévues par l’AI Act.
```

</details>

Temps : recherche 2.2 s · génération 27.6 s (3029 tokens lus, 180 écrits, 34.6 tokens/s)

## q10 — Mes salariés ou bénévoles utilisent une IA générative : ai-je des obligations ?

Article attendu : AI Act art. 4 — absent des passages donnés au modèle.

### Réponse du copilote

> Oui, vous avez des obligations si l’IA générative est utilisée par vos salariés ou bénévoles, notamment pour informer le public ou produire des contenus visuels ou audiovisuels. [2] Cela s’applique si les contenus sont publiés ou partagés, car vous êtes le déployeur du système d’IA. Si les contenus sont destinés à l’information publique, vous devez indiquer clairement que l’IA a généré ou manipulé le contenu. [2] De même, si des images ou vidéos sont créées avec hypertrucage, vous devez le déclarer. [2] Cependant, ces obligations ne s’appliquent pas si l’usage est autorisé par la loi pour des fins de prévention ou de détection de délits, ou si le contenu fait partie d’un œuvre artistique ou fictive. [2] Mais, comme vous n’êtes pas un fournisseur de système d’IA, vous n’êtes pas tenu de garantir la transparence dans tous les cas, sauf si les contenus sont publiés ou utilisés pour informer le public. [2] Aucune obligation n’est énoncée pour l’usage privé ou interne par des salariés ou bénévoles, sauf si des contenus sont publiés. [4] Les obligations de contrôle humain ou de mesures techniques ne s’appliquent pas ici, car il s’agit d’un usage interne.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »
  [2] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. »
  [2] « Les déployeurs d’un système d’IA qui génère ou manipule des textes publiés dans le but d’informer le public sur des questions d’intérêt public indiquent que le texte a été généré ou manipulé par une IA. »
  [4] « Les déployeurs de systèmes d’IA à haut risque prennent des mesures techniques et organisationnelles appropriées afin de garantir qu’ils utilisent ces systèmes conformément aux notices d’utilisation accompagnant les systèmes, conformément aux paragraphes 3 et 6. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 4 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [4] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 1 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 3 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
  [5] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 2 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
[1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »  
[2] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. »  
[2] « Les déployeurs d’un système d’IA qui génère ou manipule des textes publiés dans le but d’informer le public sur des questions d’intérêt public indiquent que le texte a été généré ou manipulé par une IA. »  
[4] « Les déployeurs de systèmes d’IA à haut risque prennent des mesures techniques et organisationnelles appropriées afin de garantir qu’ils utilisent ces systèmes conformément aux notices d’utilisation accompagnant les systèmes, conformément aux paragraphes 3 et 6. »

RÉPONSE :  
Oui, vous avez des obligations si l’IA générative est utilisée par vos salariés ou bénévoles, notamment pour informer le public ou produire des contenus visuels ou audiovisuels. [2] Cela s’applique si les contenus sont publiés ou partagés, car vous êtes le déployeur du système d’IA. Si les contenus sont destinés à l’information publique, vous devez indiquer clairement que l’IA a généré ou manipulé le contenu. [2] De même, si des images ou vidéos sont créées avec hypertrucage, vous devez le déclarer. [2] Cependant, ces obligations ne s’appliquent pas si l’usage est autorisé par la loi pour des fins de prévention ou de détection de délits, ou si le contenu fait partie d’un œuvre artistique ou fictive. [2] Mais, comme vous n’êtes pas un fournisseur de système d’IA, vous n’êtes pas tenu de garantir la transparence dans tous les cas, sauf si les contenus sont publiés ou utilisés pour informer le public. [2] Aucune obligation n’est énoncée pour l’usage privé ou interne par des salariés ou bénévoles, sauf si des contenus sont publiés. [4] Les obligations de contrôle humain ou de mesures techniques ne s’appliquent pas ici, car il s’agit d’un usage interne.
```

</details>

Temps : recherche 2.3 s · génération 24.8 s (1486 tokens lus, 639 écrits, 37.9 tokens/s)

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

Temps : recherche 2.1 s · génération 16.8 s (2279 tokens lus, 29 écrits, 37.9 tokens/s)

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

Temps : recherche 2.1 s · génération 17.6 s (2388 tokens lus, 29 écrits, 37.7 tokens/s)
