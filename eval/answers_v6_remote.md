# Réponses du copilote — v6_remote

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 18/11/2026 à 16:56 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen/qwen3.8-27b` via l'API compatible OpenAI https://api.groq.com/openai/v1 (expérience de la séance 7, questions de test seulement ; modèle tel que servi par l'API à la date ci-dessus) — température 0.1, raisonnement : réglage par défaut du modèle, passages calculés pour un contexte de 8192 tokens comme en local, 2000 tokens au plus par réponse (raisonnement compris) ; le juge est le même modèle
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu, reranker `BAAI/bge-reranker-v2-m3` sur CPU (20 candidats reclassés avant la limite par article), reformulation de la question par le modèle avant la recherche (termes juridiques ajoutés, sans conclusion)
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_v0.jsonl` (10), `eval/questions_offtopic_v0.jsonl` (0 + 2 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q01 | Dois-je désigner un DPO ? | 5/5 | non | — | 46 s |
| q02 | Dois-je tenir un registre des traitements ? | 5/6 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1]) : ignoré(s). | 36 s |
| q03 | Combien de temps puis-je garder les données de mes clients ou adhérents ? | 3/3 | non | — | 35 s |
| q04 | Que dois-je mettre dans la mention d'information d'un formulaire ? | 6/6 | non | — | 36 s |
| q05 | Une personne demande l'accès à ses données : quel délai pour répondre ? | 3/3 | non | — | 37 s |
| q06 | J'ai eu une fuite de données : que faire, et en combien de temps ? | 6/6 | non | La réponse met entre « » un texte introuvable dans les extraits vérifiés : « documenter toute violation de données à caractère personnel, en indiquant les faits concernant la violation des données … » (et 1 autre(s)). | 38 s |
| q07 | Quand faut-il faire une analyse d'impact (AIPD) ? | 5/5 | non | — | 24 s |
| q08 | Mon chatbot doit-il dire aux clients qu'il est une IA ? | 2/2 | non | La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui, votre chatbot doit informer les clients qu'ils interagissent avec une IA, car il s'agit d'un système destiné à … » (et 1 autre(s)). Vérifiez qui est concerné. | 29 s |
| q09 | Puis-je utiliser une IA pour trier des CV ? | 5/5 | non | La réponse met entre « » un texte introuvable dans les extraits vérifiés : « toujours considérée comme étant à haut risque ». | 27 s |
| q10 | Mes salariés ou bénévoles utilisent une IA générative : ai-je des obligations ? | 5/5 | non | — | 28 s |
| h01 | Quel est le taux de TVA en France ? | 0/0 | oui | — | 30 s |
| h02 | Comment faire une déclaration d'impôts ? | 0/0 | oui | — | 29 s |

## q01 — Dois-je désigner un DPO ?

Article attendu : RGPD art. 37 — passage [1].

### Réponse du copilote

> Vous devez désigner un délégué à la protection des données (DPO) si vous êtes une autorité publique ou un organisme public, « à l'exception des juridictions agissant dans l'exercice de leur fonction juridictionnelle » [1]. La désignation est également obligatoire si vos activités de base consistent en des opérations de traitement qui « exigent un suivi régulier et systématique à grande échelle des personnes concernées » [1], ou si elles consistent en « un traitement à grande échelle de catégories particulières de données visées à l’article 9 ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l’article 10 » [1]. Dans les autres cas, vous « pouvez désigner » un DPO, ou vous en êtes « tenu » si « le droit de l'Union ou le droit d'un État membre l'exige » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le responsable du traitement et le sous-traitant désignent en tout état de cause un délégué à la protection des données lorsque: »
  [1] « a) le traitement est effectué par une autorité publique ou un organisme public, à l'exception des juridictions agissant dans l'exercice de leur fonction juridictionnelle; »
  [1] « b) les activités de base du responsable du traitement ou du sous-traitant consistent en des opérations de traitement qui, du fait de leur nature, de leur portée et/ou de leurs finalités, exigent un suivi régulier et systématique à grande échelle des personnes concernées; ou »
  [1] « c) les activités de base du responsable du traitement ou du sous-traitant consistent en un traitement à grande échelle de catégories particulières de données visées à l’article 9 ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l’article 10. »
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
  [5] RGPD — règlement (UE) 2016/679, article 35, paragraphe 1 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le responsable du traitement et le sous-traitant désignent en tout état de cause un délégué à la protection des données lorsque: »
- [1] « a) le traitement est effectué par une autorité publique ou un organisme public, à l'exception des juridictions agissant dans l'exercice de leur fonction juridictionnelle; »
- [1] « b) les activités de base du responsable du traitement ou du sous-traitant consistent en des opérations de traitement qui, du fait de leur nature, de leur portée et/ou de leurs finalités, exigent un suivi régulier et systématique à grande échelle des personnes concernées; ou »
- [1] « c) les activités de base du responsable du traitement ou du sous-traitant consistent en un traitement à grande échelle de catégories particulières de données visées à l’article 9 ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l’article 10. »
- [1] « Dans les cas autres que ceux visés au paragraphe 1, le responsable du traitement ou le sous-traitant ou les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent désigner ou, si le droit de l'Union ou le droit d'un État membre l'exige, sont tenus de désigner un délégué à la protection des données. »

RÉPONSE :
Vous devez désigner un délégué à la protection des données (DPO) si vous êtes une autorité publique ou un organisme public, « à l'exception des juridictions agissant dans l'exercice de leur fonction juridictionnelle » [1]. La désignation est également obligatoire si vos activités de base consistent en des opérations de traitement qui « exigent un suivi régulier et systématique à grande échelle des personnes concernées » [1], ou si elles consistent en « un traitement à grande échelle de catégories particulières de données visées à l’article 9 ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l’article 10 » [1]. Dans les autres cas, vous « pouvez désigner » un DPO, ou vous en êtes « tenu » si « le droit de l'Union ou le droit d'un État membre l'exige » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : responsable de la protection des données ; traitement à grande échelle ; données sensibles ; activité principale

Temps : recherche 43.5 s · génération 1.4 s (2815 tokens lus, 523 écrits, 469.0 tokens/s) · contrôle de pertinence 0.1 s · reformulation 0.5 s

## q02 — Dois-je tenir un registre des traitements ?

Article attendu : RGPD art. 30 — passage [1].

### Réponse du copilote

> Oui, en tant que responsable du traitement, vous devez tenir un registre des activités de traitement effectuées sous votre responsabilité [1]. Cette obligation ne s'applique pas si votre entreprise ou organisation compte moins de 250 employés, « sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 » [1]. Le registre doit contenir, entre autres, le nom et les coordonnées du responsable du traitement [1], les finalités du traitement [1] et une description des catégories de personnes concernées et des catégories de données à caractère personnel [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Chaque responsable du traitement et, le cas échéant, le représentant du responsable du traitement tiennent un registre des activités de traitement effectuées sous leur responsabilité. »
  [1] « Les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10. »
  [1] « Ce registre comporte toutes les informations suivantes: »
  [1] « a) le nom et les coordonnées du responsable du traitement et, le cas échéant, du responsable conjoint du traitement, du représentant du responsable du traitement et du délégué à la protection des données; »
  [1] « c) une description des catégories de personnes concernées et des catégories de données à caractère personnel; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 49, paragraphe 6 : Dérogations pour des situations particulières
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_49
  [3] RGPD — règlement (UE) 2016/679, article 49, paragraphe 1 : Dérogations pour des situations particulières
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_49
  [4] RGPD — règlement (UE) 2016/679, article 4, définition 2 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [5] RGPD — règlement (UE) 2016/679, article 24 : Responsabilité du responsable du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_24
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1]) : ignoré(s).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Chaque responsable du traitement et, le cas échéant, le représentant du responsable du traitement tiennent un registre des activités de traitement effectuées sous leur responsabilité. »
- [1] « Les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10. »
- [1] « Ce registre comporte toutes les informations suivantes: »
- [1] « a) le nom et les coordonnées du responsable du traitement et, le cas échéant, du responsable conjoint du traitement, du représentant du responsable du traitement et du délégué à la protection des données; »
- [1] « b) les finalités du traitement; »
- [1] « c) une description des catégories de personnes concernées et des catégories de données à caractère personnel; »

RÉPONSE :
Oui, en tant que responsable du traitement, vous devez tenir un registre des activités de traitement effectuées sous votre responsabilité [1]. Cette obligation ne s'applique pas si votre entreprise ou organisation compte moins de 250 employés, « sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 » [1]. Le registre doit contenir, entre autres, le nom et les coordonnées du responsable du traitement [1], les finalités du traitement [1] et une description des catégories de personnes concernées et des catégories de données à caractère personnel [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : registre des activités de traitement

Temps : recherche 34.4 s · génération 1.5 s (3092 tokens lus, 476 écrits, 457.9 tokens/s) · contrôle de pertinence 0.4 s · reformulation 0.2 s

## q03 — Combien de temps puis-je garder les données de mes clients ou adhérents ?

Article attendu : RGPD art. 5 — passage [3].

### Réponse du copilote

> Vous devez conserver les données de vos clients ou adhérents pendant une durée « n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées » [3]. Il est possible de les conserver « pour des durées plus longues » uniquement si elles sont « traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques » et que des « mesures techniques et organisationnelles appropriées » sont mises en œuvre [3]. En tant que responsable du traitement, vous devez informer la personne concernée de « la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée » [4]. Les passages trouvés ne traitent pas de durées précises (en jours, mois ou années) pour chaque type de donnée ; ces règles concrètes peuvent venir d'autres textes, comme le droit national ou les recommandations de la CNIL.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées »
  [3] « les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée »
  [4] « la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée »

Sources citées :
  [3] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
  [4] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 6, paragraphe 3 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
  [2] RGPD — règlement (UE) 2016/679, article 6, paragraphe 1 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
  [5] RGPD — règlement (UE) 2016/679, article 18 : Droit à la limitation du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_18

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [3] « conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées »
- [3] « les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée »
- [4] « la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée »

RÉPONSE :
Vous devez conserver les données de vos clients ou adhérents pendant une durée « n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées » [3]. Il est possible de les conserver « pour des durées plus longues » uniquement si elles sont « traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques » et que des « mesures techniques et organisationnelles appropriées » sont mises en œuvre [3]. En tant que responsable du traitement, vous devez informer la personne concernée de « la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée » [4]. Les passages trouvés ne traitent pas de durées précises (en jours, mois ou années) pour chaque type de donnée ; ces règles concrètes peuvent venir d'autres textes, comme le droit national ou les recommandations de la CNIL.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : durée de conservation ; limitation de la conservation ; finalité du traitement ; durée de vie des données

Temps : recherche 33.1 s · génération 1.3 s (3562 tokens lus, 392 écrits, 507.0 tokens/s) · contrôle de pertinence 0.3 s · reformulation 0.5 s

## q04 — Que dois-je mettre dans la mention d'information d'un formulaire ?

Article attendu : RGPD art. 13 — passage [1].

### Réponse du copilote

> Si vous collectez les données directement auprès de la personne via un formulaire, vous devez inclure dans la mention d'information l'identité et les coordonnées du responsable du traitement et, le cas échéant, du représentant du responsable du traitement [1]. Vous devez également indiquer, le cas échéant, les coordonnées du délégué à la protection des données [1]. Il est obligatoire de préciser les finalités du traitement ainsi que la base juridique du traitement [1]. Si le traitement repose sur l'intérêt légitime (article 6, paragraphe 1, point f), vous devez mentionner les intérêts légitimes poursuivis par le responsable du traitement ou par un tiers [1]. Vous devez aussi lister les destinataires ou les catégories de destinataires des données, s'ils existent [1]. Enfin, le cas échéant, vous devez informer de l'intention d'effectuer un transfert de données vers un pays tiers ou une organisation internationale, ainsi que de l'existence ou de l'absence d'une décision d'adéquation ou de la référence aux garanties appropriées [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « a) l'identité et les coordonnées du responsable du traitement et, le cas échéant, du représentant du responsable du traitement »
  [1] « b) le cas échéant, les coordonnées du délégué à la protection des données; »
  [1] « c) les finalités du traitement auquel sont destinées les données à caractère personnel ainsi que la base juridique du traitement; »
  [1] « d) lorsque le traitement est fondé sur l'article 6, paragraphe 1, point f), les intérêts légitimes poursuivis par le responsable du traitement ou par un tiers; »
  [1] « e) les destinataires ou les catégories de destinataires des données à caractère personnel, s'ils existent; et »
  [1] « f) le cas échéant, le fait que le responsable du traitement a l'intention d'effectuer un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale, et l'existence ou l'absence d'une décision d'adéquation rendue par la Commission ou, dans le cas des transferts visés à l'article 46 ou 47, ou à l'article 49, paragraphe 1, deuxième alinéa, la référence aux garanties appropriées ou adaptées et les moyens d'en obtenir une copie ou l'endroit où elles ont été mises à disposition; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [3] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [4] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [5] RGPD — règlement (UE) 2016/679, article 6, paragraphe 3 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « a) l'identité et les coordonnées du responsable du traitement et, le cas échéant, du représentant du responsable du traitement »
- [1] « b) le cas échéant, les coordonnées du délégué à la protection des données; »
- [1] « c) les finalités du traitement auquel sont destinées les données à caractère personnel ainsi que la base juridique du traitement; »
- [1] « d) lorsque le traitement est fondé sur l'article 6, paragraphe 1, point f), les intérêts légitimes poursuivis par le responsable du traitement ou par un tiers; »
- [1] « e) les destinataires ou les catégories de destinataires des données à caractère personnel, s'ils existent; et »
- [1] « f) le cas échéant, le fait que le responsable du traitement a l'intention d'effectuer un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale, et l'existence ou l'absence d'une décision d'adéquation rendue par la Commission ou, dans le cas des transferts visés à l'article 46 ou 47, ou à l'article 49, paragraphe 1, deuxième alinéa, la référence aux garanties appropriées ou adaptées et les moyens d'en obtenir une copie ou l'endroit où elles ont été mises à disposition; »

RÉPONSE :
Si vous collectez les données directement auprès de la personne via un formulaire, vous devez inclure dans la mention d'information l'identité et les coordonnées du responsable du traitement et, le cas échéant, du représentant du responsable du traitement [1]. Vous devez également indiquer, le cas échéant, les coordonnées du délégué à la protection des données [1]. Il est obligatoire de préciser les finalités du traitement ainsi que la base juridique du traitement [1]. Si le traitement repose sur l'intérêt légitime (article 6, paragraphe 1, point f), vous devez mentionner les intérêts légitimes poursuivis par le responsable du traitement ou par un tiers [1]. Vous devez aussi lister les destinataires ou les catégories de destinataires des données, s'ils existent [1]. Enfin, le cas échéant, vous devez informer de l'intention d'effectuer un transfert de données vers un pays tiers ou une organisation internationale, ainsi que de l'existence ou de l'absence d'une décision d'adéquation ou de la référence aux garanties appropriées [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : identité du responsable du traitement ; finalités du traitement ; destinataires des données ; durée de conservation des données ; droits de l'intéressé

Temps : recherche 33.3 s · génération 1.7 s (3660 tokens lus, 538 écrits, 480.1 tokens/s) · contrôle de pertinence 0.3 s · reformulation 0.5 s · attente des limites de l'API 2 s (non comptée)

## q05 — Une personne demande l'accès à ses données : quel délai pour répondre ?

Article attendu : RGPD art. 12, paragraphe 3 — passage [1].

### Réponse du copilote

> Le responsable du traitement doit répondre à la demande d'accès aux données dans un délai d'un mois à compter de la réception de la demande [1]. Ce délai peut être prolongé de deux mois si la demande est complexe ou s'il y a un grand nombre de demandes [1]. Dans ce cas, vous devez informer la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. »
  [1] « Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. »
  [1] « Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [3] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [4] RGPD — règlement (UE) 2016/679, article 12, paragraphe 4 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. »
- [1] « Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. »
- [1] « Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. »

RÉPONSE :
Le responsable du traitement doit répondre à la demande d'accès aux données dans un délai d'un mois à compter de la réception de la demande [1]. Ce délai peut être prolongé de deux mois si la demande est complexe ou s'il y a un grand nombre de demandes [1]. Dans ce cas, vous devez informer la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit d'accès ; délai d'un mois ; prolongation de deux mois

Temps : recherche 34.8 s · génération 1.4 s (2706 tokens lus, 247 écrits, 356.6 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.3 s

## q06 — J'ai eu une fuite de données : que faire, et en combien de temps ?

Article attendu : RGPD art. 33 ou RGPD art. 34 — passage [1].

### Réponse du copilote

> En tant que responsable du traitement, vous devez notifier la violation à l'autorité de contrôle compétente « dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance » [1]. Cette obligation ne s'applique pas « à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques » [1]. Si vous ne pouvez pas notifier dans les 72 heures, la notification doit être « accompagnée des motifs du retard » [1].
>
> La notification doit contenir au minimum : « a) décrire la nature de la violation de données à caractère personnel y compris, si possible, les catégories et le nombre approximatif de personnes concernées par la violation et les catégories et le nombre approximatif d'enregistrements de données à caractère personnel concernés » [1] ; « b) communiquer le nom et les coordonnées du délégué à la protection des données ou d'un autre point de contact auprès duquel des informations supplémentaires peuvent être obtenues » [1] ; « c) décrire les conséquences probables de la violation de données à caractère personnel » [1] ; et « d) décrire les mesures prises ou que le responsable du traitement propose de prendre pour remédier à la violation de données à caractère personnel, y compris, le cas échéant, les mesures pour en atténuer les éventuelles conséquences négatives » [1]. Si vous n'avez pas toutes les informations immédiatement, « les informations peuvent être communiquées de manière échelonnée sans autre retard indu » [1].
>
> Vous devez également « documenter toute violation de données à caractère personnel, en indiquant les faits concernant la violation des données à caractère personnel, ses effets et les mesures prises pour y remédier » [1]. Si vous êtes un sous-traitant, vous devez « notifier au responsable du traitement toute violation de données à caractère personnel dans les meilleurs délais après en avoir pris connaissance » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. »
  [1] « Le sous-traitant notifie au responsable du traitement toute violation de données à caractère personnel dans les meilleurs délais après en avoir pris connaissance. »
  [1] « La notification visée au paragraphe 1 doit, à tout le moins: a) décrire la nature de la violation de données à caractère personnel y compris, si possible, les catégories et le nombre approximatif de personnes concernées par la violation et les catégories et le nombre approximatif d'enregistrements de données à caractère personnel concernés; b) communiquer le nom et les coordonnées du délégué à la protection des données ou d'un autre point de contact auprès duquel des informations supplémentaires peuvent être obtenues; c) décrire les conséquences probables de la violation de données à caractère personnel; d) décrire les mesures prises ou que le responsable du traitement propose de prendre pour remédier à la violation de données à caractère personnel, y compris, le cas échéant, les mesures pour en atténuer les éventuelles conséquences négatives. »
  [1] « Si, et dans la mesure où, il n'est pas possible de fournir toutes les informations en même temps, les informations peuvent être communiquées de manière échelonnée sans autre retard indu. »
  [1] « Le responsable du traitement documente toute violation de données à caractère personnel, en indiquant les faits concernant la violation des données à caractère personnel, ses effets et les mesures prises pour y remédier. »
  [1] « Lorsque la notification à l'autorité de contrôle n'a pas lieu dans les 72 heures, elle est accompagnée des motifs du retard. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 33 : Notification à l'autorité de contrôle d'une violation de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_33
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 58, paragraphe 2 : Pouvoirs
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_58
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 22 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [4] RGPD — règlement (UE) 2016/679, article 79 : Droit à un recours juridictionnel effectif contre un responsable du traitement ou un sous-traitant
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_79
  [5] RGPD — règlement (UE) 2016/679, article 58, paragraphe 1 : Pouvoirs
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_58
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « documenter toute violation de données à caractère personnel, en indiquant les faits concernant la violation des données … » (et 1 autre(s)).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. »
- [1] « Le sous-traitant notifie au responsable du traitement toute violation de données à caractère personnel dans les meilleurs délais après en avoir pris connaissance. »
- [1] « La notification visée au paragraphe 1 doit, à tout le moins: a) décrire la nature de la violation de données à caractère personnel y compris, si possible, les catégories et le nombre approximatif de personnes concernées par la violation et les catégories et le nombre approximatif d'enregistrements de données à caractère personnel concernés; b) communiquer le nom et les coordonnées du délégué à la protection des données ou d'un autre point de contact auprès duquel des informations supplémentaires peuvent être obtenues; c) décrire les conséquences probables de la violation de données à caractère personnel; d) décrire les mesures prises ou que le responsable du traitement propose de prendre pour remédier à la violation de données à caractère personnel, y compris, le cas échéant, les mesures pour en atténuer les éventuelles conséquences négatives. »
- [1] « Si, et dans la mesure où, il n'est pas possible de fournir toutes les informations en même temps, les informations peuvent être communiquées de manière échelonnée sans autre retard indu. »
- [1] « Le responsable du traitement documente toute violation de données à caractère personnel, en indiquant les faits concernant la violation des données à caractère personnel, ses effets et les mesures prises pour y remédier. »
- [1] « Lorsque la notification à l'autorité de contrôle n'a pas lieu dans les 72 heures, elle est accompagnée des motifs du retard. »

RÉPONSE :
En tant que responsable du traitement, vous devez notifier la violation à l'autorité de contrôle compétente « dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance » [1]. Cette obligation ne s'applique pas « à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques » [1]. Si vous ne pouvez pas notifier dans les 72 heures, la notification doit être « accompagnée des motifs du retard » [1].

La notification doit contenir au minimum : « a) décrire la nature de la violation de données à caractère personnel y compris, si possible, les catégories et le nombre approximatif de personnes concernées par la violation et les catégories et le nombre approximatif d'enregistrements de données à caractère personnel concernés » [1] ; « b) communiquer le nom et les coordonnées du délégué à la protection des données ou d'un autre point de contact auprès duquel des informations supplémentaires peuvent être obtenues » [1] ; « c) décrire les conséquences probables de la violation de données à caractère personnel » [1] ; et « d) décrire les mesures prises ou que le responsable du traitement propose de prendre pour remédier à la violation de données à caractère personnel, y compris, le cas échéant, les mesures pour en atténuer les éventuelles conséquences négatives » [1]. Si vous n'avez pas toutes les informations immédiatement, « les informations peuvent être communiquées de manière échelonnée sans autre retard indu » [1].

Vous devez également « documenter toute violation de données à caractère personnel, en indiquant les faits concernant la violation des données à caractère personnel, ses effets et les mesures prises pour y remédier » [1]. Si vous êtes un sous-traitant, vous devez « notifier au responsable du traitement toute violation de données à caractère personnel dans les meilleurs délais après en avoir pris connaissance » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : autorité de contrôle ; responsable du traitement ; sous-traitant ; mesures correctives

Temps : recherche 35.4 s · génération 2.1 s (2777 tokens lus, 863 écrits, 531.7 tokens/s) · contrôle de pertinence 0.4 s · reformulation 0.4 s · attente des limites de l'API 22 s (non comptée)

## q07 — Quand faut-il faire une analyse d'impact (AIPD) ?

Article attendu : RGPD art. 35, paragraphe 1 ou RGPD art. 35, paragraphe 3 — passage [1].

### Réponse du copilote

> Vous devez effectuer une analyse d'impact relative à la protection des données (AIPD) avant le traitement lorsqu'un type de traitement, notamment par le recours à de nouvelles technologies, est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques [1]. Cette obligation s'applique spécifiquement dans trois cas principaux : l'évaluation systématique et approfondie d'aspects personnels par traitement automatisé (y compris le profilage) menant à des décisions ayant des effets juridiques ou affectant significativement la personne [2] ; le traitement à grande échelle de catégories particulières de données (comme celles de l'article 9) ou de données relatives à des condamnations pénales [2] ; et la surveillance systématique à grande échelle d'une zone accessible au public [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Lorsqu'un type de traitement, en particulier par le recours à de nouvelles technologies, et compte tenu de la nature, de la portée, du contexte et des finalités du traitement, est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, le responsable du traitement effectue, avant le traitement, une analyse de l'impact des opérations de traitement envisagées sur la protection des données à caractère personnel. »
  [2] « L'analyse d'impact relative à la protection des données visée au paragraphe 1 est, en particulier, requise dans les cas suivants: »
  [2] « a) l'évaluation systématique et approfondie d'aspects personnels concernant des personnes physiques, qui est fondée sur un traitement automatisé, y compris le profilage, et sur la base de laquelle sont prises des décisions produisant des effets juridiques à l'égard d'une personne physique ou l'affectant de manière significative de façon similaire; »
  [2] « b) le traitement à grande échelle de catégories particulières de données visées à l'article 9, paragraphe 1, ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10; ou »
  [2] « c) la surveillance systématique à grande échelle d'une zone accessible au public. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 35, paragraphe 1 : Analyse d'impact relative à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [2] RGPD — règlement (UE) 2016/679, article 35, paragraphe 3 : Analyse d'impact relative à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 34 : Communication à la personne concernée d'une violation de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_34
  [4] AI Act — règlement (UE) 2024/1689, article 4 bis : Traitement de catégories particulières de données à caractère personnel à des fins de détection et de correction des biais
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_4a
  [5] RGPD — règlement (UE) 2016/679, article 9, paragraphe 2, points a) à i) : Traitement portant sur des catégories particulières de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Lorsqu'un type de traitement, en particulier par le recours à de nouvelles technologies, et compte tenu de la nature, de la portée, du contexte et des finalités du traitement, est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, le responsable du traitement effectue, avant le traitement, une analyse de l'impact des opérations de traitement envisagées sur la protection des données à caractère personnel. »
- [2] « L'analyse d'impact relative à la protection des données visée au paragraphe 1 est, en particulier, requise dans les cas suivants: »
- [2] « a) l'évaluation systématique et approfondie d'aspects personnels concernant des personnes physiques, qui est fondée sur un traitement automatisé, y compris le profilage, et sur la base de laquelle sont prises des décisions produisant des effets juridiques à l'égard d'une personne physique ou l'affectant de manière significative de façon similaire; »
- [2] « b) le traitement à grande échelle de catégories particulières de données visées à l'article 9, paragraphe 1, ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10; ou »
- [2] « c) la surveillance systématique à grande échelle d'une zone accessible au public. »

RÉPONSE :
Vous devez effectuer une analyse d'impact relative à la protection des données (AIPD) avant le traitement lorsqu'un type de traitement, notamment par le recours à de nouvelles technologies, est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques [1]. Cette obligation s'applique spécifiquement dans trois cas principaux : l'évaluation systématique et approfondie d'aspects personnels par traitement automatisé (y compris le profilage) menant à des décisions ayant des effets juridiques ou affectant significativement la personne [2] ; le traitement à grande échelle de catégories particulières de données (comme celles de l'article 9) ou de données relatives à des condamnations pénales [2] ; et la surveillance systématique à grande échelle d'une zone accessible au public [2].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : traitement susceptible d'engendrer un risque élevé ; traitement à grande échelle ; traitement de données sensibles ; traitement de données à caractère personnel

Temps : recherche 22.5 s · génération 1.4 s (3555 tokens lus, 481 écrits, 513.4 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.2 s · attente des limites de l'API 20 s (non comptée)

## q08 — Mon chatbot doit-il dire aux clients qu'il est une IA ?

Article attendu : AI Act art. 50, paragraphe 1 — passage [1].

### Réponse du copilote

> Oui, votre chatbot doit informer les clients qu'ils interagissent avec une IA, car il s'agit d'un système destiné à interagir directement avec des personnes physiques [1]. Cette obligation incombe au fournisseur du système d'IA [1]. L'information doit être fournie de manière claire et reconnaissable au plus tard au moment de la première interaction [2]. Il existe une exception si le fait d'interagir avec une IA « ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »
  [2] « Les informations visées aux paragraphes 1 à 4 sont fournies aux personnes physiques concernées de manière claire et reconnaissable au plus tard au moment de la première interaction ou de la première exposition. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 5 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, annexe III, point 8 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [4] AI Act — règlement (UE) 2024/1689, article 13 : Transparence et fourniture d’informations aux déployeurs
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_13
  [5] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14
Attention : La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui, votre chatbot doit informer les clients qu'ils interagissent avec une IA, car il s'agit d'un système destiné à … » (et 1 autre(s)). Vérifiez qui est concerné.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »
- [2] « Les informations visées aux paragraphes 1 à 4 sont fournies aux personnes physiques concernées de manière claire et reconnaissable au plus tard au moment de la première interaction ou de la première exposition. »

RÉPONSE :
Oui, votre chatbot doit informer les clients qu'ils interagissent avec une IA, car il s'agit d'un système destiné à interagir directement avec des personnes physiques [1]. Cette obligation incombe au fournisseur du système d'IA [1]. L'information doit être fournie de manière claire et reconnaissable au plus tard au moment de la première interaction [2]. Il existe une exception si le fait d'interagir avec une IA « ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : transparence ; obligation d'information ; identification de l'IA ; interaction homme-machine ; notification de l'utilisateur ; divulgation de la nature artificielle

Temps : recherche 27.6 s · génération 1.0 s (3358 tokens lus, 285 écrits, 465.7 tokens/s) · contrôle de pertinence 0.3 s · reformulation 0.2 s

## q09 — Puis-je utiliser une IA pour trier des CV ?

Article attendu : AI Act annexe III, point 4 ou AI Act art. 26 — passage [1].

### Réponse du copilote

> Oui, vous pouvez utiliser une IA pour trier des CV, car ce type de système est explicitement mentionné dans l'AI Act comme étant destiné à « analyser et filtrer les candidatures » [1]. Cependant, ce système est classé comme « à haut risque » [1]. Si l'IA effectue un profilage de personnes physiques, elle est « toujours considérée comme étant à haut risque » [2]. En tant que déployeur, vous devez vous assurer que le système permet « un contrôle effectif par des personnes physiques » [4]. Cela implique que les personnes chargées du contrôle doivent avoir la possibilité « de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou inverser la sortie du système d’IA à haut risque » [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »
  [2] « Nonobstant le premier alinéa, un système d’IA visé à l’annexe III est toujours considéré comme étant à haut risque lorsqu’il effectue un profilage de personnes physiques. »
  [4] « 1. La conception et le développement des systèmes d’IA à haut risque permettent, notamment au moyen d’interfaces homme-machine appropriées, un contrôle effectif par des personnes physiques pendant leur période d’utilisation. »
  [4] « 4. Aux fins de la mise en œuvre des dispositions des paragraphes 1, 2 et 3, le système d’IA à haut risque est fourni au déployeur de telle manière que les personnes physiques chargées d’effectuer un contrôle humain, dans la mesure où cela est approprié et proportionné, ont la possibilité: »
  [4] « d) de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou inverser la sortie du système d’IA à haut risque; »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [2] AI Act — règlement (UE) 2024/1689, article 6, point d : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
  [4] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, annexe III, point 5 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [5] AI Act — règlement (UE) 2024/1689, article 4 bis : Traitement de catégories particulières de données à caractère personnel à des fins de détection et de correction des biais
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_4a
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « toujours considérée comme étant à haut risque ».

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »
- [2] « Nonobstant le premier alinéa, un système d’IA visé à l’annexe III est toujours considéré comme étant à haut risque lorsqu’il effectue un profilage de personnes physiques. »
- [4] « 1. La conception et le développement des systèmes d’IA à haut risque permettent, notamment au moyen d’interfaces homme-machine appropriées, un contrôle effectif par des personnes physiques pendant leur période d’utilisation. »
- [4] « 4. Aux fins de la mise en œuvre des dispositions des paragraphes 1, 2 et 3, le système d’IA à haut risque est fourni au déployeur de telle manière que les personnes physiques chargées d’effectuer un contrôle humain, dans la mesure où cela est approprié et proportionné, ont la possibilité: »
- [4] « d) de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou inverser la sortie du système d’IA à haut risque; »

RÉPONSE :
Oui, vous pouvez utiliser une IA pour trier des CV, car ce type de système est explicitement mentionné dans l'AI Act comme étant destiné à « analyser et filtrer les candidatures » [1]. Cependant, ce système est classé comme « à haut risque » [1]. Si l'IA effectue un profilage de personnes physiques, elle est « toujours considérée comme étant à haut risque » [2]. En tant que déployeur, vous devez vous assurer que le système permet « un contrôle effectif par des personnes physiques » [4]. Cela implique que les personnes chargées du contrôle doivent avoir la possibilité « de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou inverser la sortie du système d’IA à haut risque » [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : système d'IA à haut risque ; profilage ; décision automatisée ; données à caractère personnel ; biais algorithmique ; transparence

Temps : recherche 25.1 s · génération 1.7 s (3452 tokens lus, 468 écrits, 466.2 tokens/s) · contrôle de pertinence 0.4 s · reformulation 0.3 s

## q10 — Mes salariés ou bénévoles utilisent une IA générative : ai-je des obligations ?

Article attendu : AI Act art. 4 — passage [1].

### Réponse du copilote

> Oui, vous avez des obligations en tant que déployeur de systèmes d'IA. Vous devez prendre des mesures pour favoriser le développement de la maîtrise de l'IA par votre personnel ou vos bénévoles qui utilisent ces systèmes, en tenant compte de leurs connaissances et du contexte d'utilisation [1]. Cette obligation ne vous contraint pas à garantir un niveau spécifique de maîtrise de l'IA par un individu [1]. Si vos salariés ou bénévoles génèrent ou manipulent des images, des contenus audio ou vidéo constituant un hypertrucage, vous devez indiquer que ces contenus ont été générés ou manipulés par une IA [2]. De même, s'ils génèrent ou manipulent des textes publiés dans le but d'informer le public sur des questions d'intérêt public, vous devez indiquer que le texte a été généré ou manipulé par une IA [2]. Enfin, si le système d'IA utilisé sur le lieu de travail est classé comme à haut risque, vous devez informer les représentants des travailleurs et les travailleurs concernés avant de le mettre en service ou de l'utiliser [5].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les fournisseurs et les déployeurs de systèmes d'IA prennent des mesures pour favoriser le développement de la maîtrise de l'IA par leur personnel et les autres personnes s'occupant du fonctionnement et de l'utilisation des systèmes d'IA pour leur compte, en prenant en considération leurs connaissances techniques, leur expérience, leur éducation et leur formation, ainsi que le contexte dans lequel les systèmes d'IA sont destinés à être utilisés, et en tenant compte des personnes ou des groupes de personnes à l'égard desquels les systèmes d'IA sont destinés à être utilisés. »
  [1] « Cette obligation ne contraint pas les fournisseurs ou les déployeurs à garantir un niveau spécifique de maîtrise de l'IA par un individu. »
  [2] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. »
  [2] « Les déployeurs d’un système d’IA qui génère ou manipule des textes publiés dans le but d’informer le public sur des questions d’intérêt public indiquent que le texte a été généré ou manipulé par une IA. »
  [5] « Avant de mettre en service ou d’utiliser un système d’IA à haut risque sur le lieu de travail, les déployeurs qui sont des employeurs informent les représentants des travailleurs et les travailleurs concernés qu’ils seront soumis à l’utilisation du système d’IA à haut risque. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 4 : Maîtrise de l'IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_4
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 4 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [5] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 7 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [4] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 2 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les fournisseurs et les déployeurs de systèmes d'IA prennent des mesures pour favoriser le développement de la maîtrise de l'IA par leur personnel et les autres personnes s'occupant du fonctionnement et de l'utilisation des systèmes d'IA pour leur compte, en prenant en considération leurs connaissances techniques, leur expérience, leur éducation et leur formation, ainsi que le contexte dans lequel les systèmes d'IA sont destinés à être utilisés, et en tenant compte des personnes ou des groupes de personnes à l'égard desquels les systèmes d'IA sont destinés à être utilisés. »
- [1] « Cette obligation ne contraint pas les fournisseurs ou les déployeurs à garantir un niveau spécifique de maîtrise de l'IA par un individu. »
- [2] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. »
- [2] « Les déployeurs d’un système d’IA qui génère ou manipule des textes publiés dans le but d’informer le public sur des questions d’intérêt public indiquent que le texte a été généré ou manipulé par une IA. »
- [5] « Avant de mettre en service ou d’utiliser un système d’IA à haut risque sur le lieu de travail, les déployeurs qui sont des employeurs informent les représentants des travailleurs et les travailleurs concernés qu’ils seront soumis à l’utilisation du système d’IA à haut risque. »

RÉPONSE :
Oui, vous avez des obligations en tant que déployeur de systèmes d'IA. Vous devez prendre des mesures pour favoriser le développement de la maîtrise de l'IA par votre personnel ou vos bénévoles qui utilisent ces systèmes, en tenant compte de leurs connaissances et du contexte d'utilisation [1]. Cette obligation ne vous contraint pas à garantir un niveau spécifique de maîtrise de l'IA par un individu [1]. Si vos salariés ou bénévoles génèrent ou manipulent des images, des contenus audio ou vidéo constituant un hypertrucage, vous devez indiquer que ces contenus ont été générés ou manipulés par une IA [2]. De même, s'ils génèrent ou manipulent des textes publiés dans le but d'informer le public sur des questions d'intérêt public, vous devez indiquer que le texte a été généré ou manipulé par une IA [2]. Enfin, si le système d'IA utilisé sur le lieu de travail est classé comme à haut risque, vous devez informer les représentants des travailleurs et les travailleurs concernés avant de le mettre en service ou de l'utiliser [5].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : responsable du traitement ; obligations du responsable du traitement ; transparence ; information des personnes concernées ; évaluation d'impact ; registre des activités de traitement

Temps : recherche 24.9 s · génération 2.1 s (2535 tokens lus, 577 écrits, 402.4 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.3 s

## h01 — Quel est le taux de TVA en France ?

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
  [4] RGPD — règlement (UE) 2016/679, article 83, paragraphe 6 : Conditions générales pour imposer des amendes administratives
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83
  [5] RGPD — règlement (UE) 2016/679, article 83, paragraphe 1 : Conditions générales pour imposer des amendes administratives
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Temps : recherche 29.0 s · génération 0.4 s (2081 tokens lus, 25 écrits, 449.4 tokens/s) · reformulation 0.6 s

## h02 — Comment faire une déclaration d'impôts ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, annexe V : Déclaration UE de conformité
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_V
  [2] RGPD — règlement (UE) 2016/679, article 57, paragraphe 2 : Missions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_57
  [3] RGPD — règlement (UE) 2016/679, article 57, paragraphe 1, points a) à t) : Missions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_57
  [4] RGPD — règlement (UE) 2016/679, article 47, paragraphe 2, points a) à k) : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
  [5] RGPD — règlement (UE) 2016/679, article 47, paragraphe 1 : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Temps : recherche 27.7 s · génération 0.6 s (3596 tokens lus, 25 écrits, 456.9 tokens/s) · reformulation 0.5 s · attente des limites de l'API 1 s (non comptée)
