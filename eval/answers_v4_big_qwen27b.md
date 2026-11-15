# Réponses du copilote — v4_big_qwen27b

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 15/11/2026 à 17:02 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen/qwen3.8-27b` via l'API compatible OpenAI https://api.groq.com/openai/v1 (expérience de la séance 7, questions de test seulement ; modèle tel que servi par l'API à la date ci-dessus) — température 0.1, raisonnement : « none » (reasoning_effort), passages calculés pour un contexte de 8192 tokens comme en local, 2000 tokens au plus par réponse (raisonnement compris) ; le juge est le même modèle
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_v0.jsonl` (10), `eval/questions_offtopic_v0.jsonl` (0 + 2 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q01 | Dois-je désigner un DPO ? | 5/5 | non | — | 38 s |
| q02 | Dois-je tenir un registre des traitements ? | 5/6 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1]) : ignoré(s). | 4 s |
| q03 | Combien de temps puis-je garder les données de mes clients ou adhérents ? | 2/2 | non | — | 4 s |
| q04 | Que dois-je mettre dans la mention d'information d'un formulaire ? | 13/13 | non | — | 5 s |
| q05 | Une personne demande l'accès à ses données : quel délai pour répondre ? | 4/4 | non | — | 4 s |
| q06 | J'ai eu une fuite de données : que faire, et en combien de temps ? | 6/6 | non | — | 6 s |
| q07 | Quand faut-il faire une analyse d'impact (AIPD) ? | 6/6 | non | — | 5 s |
| q08 | Mon chatbot doit-il dire aux clients qu'il est une IA ? | 1/1 | non | La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui, votre chatbot doit informer les clients qu'ils interagissent avec une IA, car il s'agit d'un système destiné à … » (et 1 autre(s)). Vérifiez qui est concerné. | 4 s |
| q09 | Puis-je utiliser une IA pour trier des CV ? | 6/6 | non | — | 4 s |
| q10 | Mes salariés ou bénévoles utilisent une IA générative : ai-je des obligations ? | 5/5 | non | — | 5 s |
| h01 | Quel est le taux de TVA en France ? | 0/0 | oui | — | 3 s |
| h02 | Comment faire une déclaration d'impôts ? | 0/0 | oui | — | 3 s |

## q01 — Dois-je désigner un DPO ?

Article attendu : RGPD art. 37 — passage [1].

### Réponse du copilote

> Vous devez désigner un délégué à la protection des données (DPO) si vous êtes une autorité publique ou un organisme public [1]. La désignation est également obligatoire si vos activités de base consistent en un suivi régulier et systématique à grande échelle des personnes concernées [1]. Elle l'est aussi si vos activités de base consistent en un traitement à grande échelle de catégories particulières de données visées à l’article 9 ou de données relatives à des condamnations pénales et à des infractions visées à l’article 10 [1]. Dans les autres cas, vous pouvez désigner un DPO, ou vous y êtes tenu si le droit de l'Union ou le droit d'un État membre l'exige [1].

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
Vous devez désigner un délégué à la protection des données (DPO) si vous êtes une autorité publique ou un organisme public [1]. La désignation est également obligatoire si vos activités de base consistent en un suivi régulier et systématique à grande échelle des personnes concernées [1]. Elle l'est aussi si vos activités de base consistent en un traitement à grande échelle de catégories particulières de données visées à l’article 9 ou de données relatives à des condamnations pénales et à des infractions visées à l’article 10 [1]. Dans les autres cas, vous pouvez désigner un DPO, ou vous y êtes tenu si le droit de l'Union ou le droit d'un État membre l'exige [1].
```

</details>

Temps : recherche 6.7 s · génération 1.4 s (2678 tokens lus, 486 écrits, 468.2 tokens/s) · contrôle de pertinence 30.2 s · attente des limites de l'API 2 s (non comptée)

## q02 — Dois-je tenir un registre des traitements ?

Article attendu : RGPD art. 30 — passage [1].

### Réponse du copilote

> Oui, vous devez tenir un registre des activités de traitement si vous êtes responsable du traitement, sauf si votre organisation compte moins de 250 employés et que le traitement est occasionnel, ne comporte pas de risque pour les droits et libertés des personnes, et ne porte pas sur des données sensibles [1].
> Ce registre doit contenir, entre autres, le nom et les coordonnées du responsable du traitement [1], les finalités du traitement [1] et une description des catégories de personnes concernées et des catégories de données à caractère personnel [1].
> L'obligation de tenir ce registre ne s'applique pas à une entreprise ou à une organisation comptant moins de 250 employés, « sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 » [1].

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
  [2] RGPD — règlement (UE) 2016/679, article 4, définition 2 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [3] RGPD — règlement (UE) 2016/679, article 24 : Responsabilité du responsable du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_24
  [4] RGPD — règlement (UE) 2016/679, article 6, paragraphe 1 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
  [5] RGPD — règlement (UE) 2016/679, article 9, paragraphe 3 : Traitement portant sur des catégories particulières de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
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
Oui, vous devez tenir un registre des activités de traitement si vous êtes responsable du traitement, sauf si votre organisation compte moins de 250 employés et que le traitement est occasionnel, ne comporte pas de risque pour les droits et libertés des personnes, et ne porte pas sur des données sensibles [1].
Ce registre doit contenir, entre autres, le nom et les coordonnées du responsable du traitement [1], les finalités du traitement [1] et une description des catégories de personnes concernées et des catégories de données à caractère personnel [1].
L'obligation de tenir ce registre ne s'applique pas à une entreprise ou à une organisation comptant moins de 250 employés, « sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 » [1].
```

</details>

Temps : recherche 2.2 s · génération 1.4 s (2642 tokens lus, 523 écrits, 500.3 tokens/s) · contrôle de pertinence 0.3 s

## q03 — Combien de temps puis-je garder les données de mes clients ou adhérents ?

Article attendu : RGPD art. 5 — passage [5].

### Réponse du copilote

> Vous devez conserver les données de vos clients ou adhérents « pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées » [5]. Il est possible de les garder plus longtemps uniquement si elles sont « traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques » et si des « mesures techniques et organisationnelles appropriées » sont mises en œuvre [5]. Les textes fournis ne précisent pas de durée fixe (en jours, mois ou années) ; la règle concrète dépend donc de la finalité spécifique de votre traitement et peut être complétée par d'autres textes ou recommandations.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [5] « conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées »
  [5] « les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée »

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
- [5] « conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées »
- [5] « les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée »

RÉPONSE :
Vous devez conserver les données de vos clients ou adhérents « pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées » [5]. Il est possible de les garder plus longtemps uniquement si elles sont « traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques » et si des « mesures techniques et organisationnelles appropriées » sont mises en œuvre [5]. Les textes fournis ne précisent pas de durée fixe (en jours, mois ou années) ; la règle concrète dépend donc de la finalité spécifique de votre traitement et peut être complétée par d'autres textes ou recommandations.
```

</details>

Temps : recherche 2.2 s · génération 0.9 s (2420 tokens lus, 306 écrits, 498.7 tokens/s) · contrôle de pertinence 0.5 s · attente des limites de l'API 15 s (non comptée)

## q04 — Que dois-je mettre dans la mention d'information d'un formulaire ?

Article attendu : RGPD art. 13 — passage [1].

### Réponse du copilote

> Si vous collectez les données directement auprès de la personne via le formulaire, vous devez inclure dans la mention d'information l'identité et les coordonnées du responsable du traitement [1]. Vous devez également indiquer les finalités du traitement ainsi que la base juridique [1]. Il est nécessaire de préciser les destinataires ou les catégories de destinataires des données, s'ils existent [1]. Vous devez informer sur la durée de conservation des données ou, si ce n'est pas possible, sur les critères utilisés pour la déterminer [1]. La mention doit aussi lister les droits de la personne concernée, notamment le droit d'accès, de rectification, d'effacement, de limitation, d'opposition et de portabilité [1]. Si le traitement est fondé sur le consentement, vous devez informer du droit de le retirer à tout moment [1]. Enfin, vous devez indiquer le droit d'introduire une réclamation auprès d'une autorité de contrôle [1]. Ces informations doivent être fournies de manière concise, transparente, compréhensible et aisément accessible, en des termes clairs et simples [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « a) l'identité et les coordonnées du responsable du traitement et, le cas échéant, du représentant du responsable du traitement »
  [1] « b) le cas échéant, les coordonnées du délégué à la protection des données; »
  [1] « c) les finalités du traitement auquel sont destinées les données à caractère personnel ainsi que la base juridique du traitement; »
  [1] « d) lorsque le traitement est fondé sur l'article 6, paragraphe 1, point f), les intérêts légitimes poursuivis par le responsable du traitement ou par un tiers; »
  [1] « e) les destinataires ou les catégories de destinataires des données à caractère personnel, s'ils existent; et »
  [1] « f) le cas échéant, le fait que le responsable du traitement a l'intention d'effectuer un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale, et l'existence ou l'absence d'une décision d'adéquation rendue par la Commission ou, dans le cas des transferts visés à l'article 46 ou 47, ou à l'article 49, paragraphe 1, deuxième alinéa, la référence aux garanties appropriées ou adaptées et les moyens d'en obtenir une copie ou l'endroit où elles ont été mises à disposition; »
  [1] « a) la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; »
  [1] « b) l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ou du droit de s'opposer au traitement et du droit à la portabilité des données; »
  [1] « c) lorsque le traitement est fondé sur l'article 6, paragraphe 1, point a), ou sur l'article 9, paragraphe 2, point a), l'existence du droit de retirer son consentement à tout moment, sans porter atteinte à la licéité du traitement fondé sur le consentement effectué avant le retrait de celui-ci; »
  [1] « d) le droit d'introduire une réclamation auprès d'une autorité de contrôle; »
  [1] « e) des informations sur la question de savoir si l'exigence de fourniture de données à caractère personnel a un caractère réglementaire ou contractuel ou si elle conditionne la conclusion d'un contrat et si la personne concernée est tenue de fournir les données à caractère personnel, ainsi que sur les conséquences éventuelles de la non-fourniture de ces données; »
  [1] « f) l'existence d'une prise de décision automatisée, y compris un profilage, visée à l'article 22, paragraphes 1 et 4, et, au moins en pareils cas, des informations utiles concernant la logique sous-jacente, ainsi que l'importance et les conséquences prévues de ce traitement pour la personne concernée. »
  [4] « Les informations sont fournies par écrit ou par d'autres moyens y compris, lorsque c'est approprié, par voie électronique. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [4] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [3] RGPD — règlement (UE) 2016/679, article 12, paragraphe 6 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14

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
- [1] « a) la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; »
- [1] « b) l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ou du droit de s'opposer au traitement et du droit à la portabilité des données; »
- [1] « c) lorsque le traitement est fondé sur l'article 6, paragraphe 1, point a), ou sur l'article 9, paragraphe 2, point a), l'existence du droit de retirer son consentement à tout moment, sans porter atteinte à la licéité du traitement fondé sur le consentement effectué avant le retrait de celui-ci; »
- [1] « d) le droit d'introduire une réclamation auprès d'une autorité de contrôle; »
- [1] « e) des informations sur la question de savoir si l'exigence de fourniture de données à caractère personnel a un caractère réglementaire ou contractuel ou si elle conditionne la conclusion d'un contrat et si la personne concernée est tenue de fournir les données à caractère personnel, ainsi que sur les conséquences éventuelles de la non-fourniture de ces données; »
- [1] « f) l'existence d'une prise de décision automatisée, y compris un profilage, visée à l'article 22, paragraphes 1 et 4, et, au moins en pareils cas, des informations utiles concernant la logique sous-jacente, ainsi que l'importance et les conséquences prévues de ce traitement pour la personne concernée. »
- [4] « Les informations sont fournies par écrit ou par d'autres moyens y compris, lorsque c'est approprié, par voie électronique. »

RÉPONSE :
Si vous collectez les données directement auprès de la personne via le formulaire, vous devez inclure dans la mention d'information l'identité et les coordonnées du responsable du traitement [1]. Vous devez également indiquer les finalités du traitement ainsi que la base juridique [1]. Il est nécessaire de préciser les destinataires ou les catégories de destinataires des données, s'ils existent [1]. Vous devez informer sur la durée de conservation des données ou, si ce n'est pas possible, sur les critères utilisés pour la déterminer [1]. La mention doit aussi lister les droits de la personne concernée, notamment le droit d'accès, de rectification, d'effacement, de limitation, d'opposition et de portabilité [1]. Si le traitement est fondé sur le consentement, vous devez informer du droit de le retirer à tout moment [1]. Enfin, vous devez indiquer le droit d'introduire une réclamation auprès d'une autorité de contrôle [1]. Ces informations doivent être fournies de manière concise, transparente, compréhensible et aisément accessible, en des termes clairs et simples [4].
```

</details>

Temps : recherche 2.2 s · génération 2.3 s (2978 tokens lus, 947 écrits, 471.4 tokens/s) · contrôle de pertinence 0.3 s · attente des limites de l'API 57 s (non comptée)

## q05 — Une personne demande l'accès à ses données : quel délai pour répondre ?

Article attendu : RGPD art. 12, paragraphe 3 — passage [1].

### Réponse du copilote

> Vous devez répondre à la demande d'accès aux données dans un délai d'un mois à compter de la réception de la demande [1]. Ce délai peut être prolongé de deux mois si la demande est complexe ou si vous recevez de nombreuses demandes [1]. Dans ce cas, vous devez informer la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande [1]. Si vous ne donnez pas suite à la demande, vous devez informer la personne concernée des motifs de votre inaction et de ses recours dans un délai d'un mois [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. »
  [1] « Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. »
  [1] « Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. »
  [4] « Si le responsable du traitement ne donne pas suite à la demande formulée par la personne concernée, il informe celle-ci sans tarder et au plus tard dans un délai d'un mois à compter de la réception de la demande des motifs de son inaction et de la possibilité d'introduire une réclamation auprès d'une autorité de contrôle et de former un recours juridictionnel. »

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

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. »
- [1] « Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. »
- [1] « Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. »
- [4] « Si le responsable du traitement ne donne pas suite à la demande formulée par la personne concernée, il informe celle-ci sans tarder et au plus tard dans un délai d'un mois à compter de la réception de la demande des motifs de son inaction et de la possibilité d'introduire une réclamation auprès d'une autorité de contrôle et de former un recours juridictionnel. »

RÉPONSE :
Vous devez répondre à la demande d'accès aux données dans un délai d'un mois à compter de la réception de la demande [1]. Ce délai peut être prolongé de deux mois si la demande est complexe ou si vous recevez de nombreuses demandes [1]. Dans ce cas, vous devez informer la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande [1]. Si vous ne donnez pas suite à la demande, vous devez informer la personne concernée des motifs de votre inaction et de ses recours dans un délai d'un mois [4].
```

</details>

Temps : recherche 2.2 s · génération 1.1 s (2311 tokens lus, 364 écrits, 478.8 tokens/s) · contrôle de pertinence 0.3 s

## q06 — J'ai eu une fuite de données : que faire, et en combien de temps ?

Article attendu : RGPD art. 33 ou RGPD art. 34 — passage [1].

### Réponse du copilote

> En cas de fuite de données, vous devez d'abord vérifier si l'événement constitue bien une « violation de données à caractère personnel », définie comme une violation de la sécurité entraînant, de manière accidentelle ou illicite, la destruction, la perte, l'altération, la divulgation non autorisée ou l'accès non autorisé à des données [3]. Si vous êtes le responsable du traitement, vous devez notifier cette violation à l'autorité de contrôle compétente « dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance », sauf si « la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques » [1]. Cette notification doit contenir au minimum la nature de la violation, les coordonnées du délégué à la protection des données, les conséquences probables et les mesures prises ou proposées pour remédier à la situation [1]. Vous devez également documenter toute violation, en indiquant les faits, ses effets et les mesures prises, afin de permettre à l'autorité de contrôle de vérifier le respect de l'article [1]. Si la violation est susceptible d'engendrer un « risque élevé pour les droits et libertés d'une personne physique », vous devez communiquer la violation à la personne concernée « dans les meilleurs délais » [2]. Si vous êtes un sous-traitant, votre obligation est de notifier au responsable du traitement toute violation « dans les meilleurs délais après en avoir pris connaissance » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. »
  [1] « Le sous-traitant notifie au responsable du traitement toute violation de données à caractère personnel dans les meilleurs délais après en avoir pris connaissance. »
  [1] « La notification visée au paragraphe 1 doit, à tout le moins: a) décrire la nature de la violation de données à caractère personnel y compris, si possible, les catégories et le nombre approximatif de personnes concernées par la violation et les catégories et le nombre approximatif d'enregistrements de données à caractère personnel concernés; b) communiquer le nom et les coordonnées du délégué à la protection des données ou d'un autre point de contact auprès duquel des informations supplémentaires peuvent être obtenues; c) décrire les conséquences probables de la violation de données à caractère personnel; d) décrire les mesures prises ou que le responsable du traitement propose de prendre pour remédier à la violation de données à caractère personnel, y compris, le cas échéant, les mesures pour en atténuer les éventuelles conséquences négatives. »
  [1] « Le responsable du traitement documente toute violation de données à caractère personnel, en indiquant les faits concernant la violation des données à caractère personnel, ses effets et les mesures prises pour y remédier. »
  [2] « Lorsqu'une violation de données à caractère personnel est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement communique la violation de données à caractère personnel à la personne concernée dans les meilleurs délais. »
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
- [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. »
- [1] « Le sous-traitant notifie au responsable du traitement toute violation de données à caractère personnel dans les meilleurs délais après en avoir pris connaissance. »
- [1] « La notification visée au paragraphe 1 doit, à tout le moins: a) décrire la nature de la violation de données à caractère personnel y compris, si possible, les catégories et le nombre approximatif de personnes concernées par la violation et les catégories et le nombre approximatif d'enregistrements de données à caractère personnel concernés; b) communiquer le nom et les coordonnées du délégué à la protection des données ou d'un autre point de contact auprès duquel des informations supplémentaires peuvent être obtenues; c) décrire les conséquences probables de la violation de données à caractère personnel; d) décrire les mesures prises ou que le responsable du traitement propose de prendre pour remédier à la violation de données à caractère personnel, y compris, le cas échéant, les mesures pour en atténuer les éventuelles conséquences négatives. »
- [1] « Le responsable du traitement documente toute violation de données à caractère personnel, en indiquant les faits concernant la violation des données à caractère personnel, ses effets et les mesures prises pour y remédier. »
- [2] « Lorsqu'une violation de données à caractère personnel est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement communique la violation de données à caractère personnel à la personne concernée dans les meilleurs délais. »
- [3] « «violation de données à caractère personnel», une violation de la sécurité entraînant, de manière accidentelle ou illicite, la destruction, la perte, l'altération, la divulgation non autorisée de données à caractère personnel transmises, conservées ou traitées d'une autre manière, ou l'accès non autorisé à de telles données; »

RÉPONSE :
En cas de fuite de données, vous devez d'abord vérifier si l'événement constitue bien une « violation de données à caractère personnel », définie comme une violation de la sécurité entraînant, de manière accidentelle ou illicite, la destruction, la perte, l'altération, la divulgation non autorisée ou l'accès non autorisé à des données [3]. Si vous êtes le responsable du traitement, vous devez notifier cette violation à l'autorité de contrôle compétente « dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance », sauf si « la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques » [1]. Cette notification doit contenir au minimum la nature de la violation, les coordonnées du délégué à la protection des données, les conséquences probables et les mesures prises ou proposées pour remédier à la situation [1]. Vous devez également documenter toute violation, en indiquant les faits, ses effets et les mesures prises, afin de permettre à l'autorité de contrôle de vérifier le respect de l'article [1]. Si la violation est susceptible d'engendrer un « risque élevé pour les droits et libertés d'une personne physique », vous devez communiquer la violation à la personne concernée « dans les meilleurs délais » [2]. Si vous êtes un sous-traitant, votre obligation est de notifier au responsable du traitement toute violation « dans les meilleurs délais après en avoir pris connaissance » [1].
```

</details>

Temps : recherche 2.2 s · génération 2.3 s (3390 tokens lus, 824 écrits, 477.1 tokens/s) · contrôle de pertinence 1.5 s · attente des limites de l'API 36 s (non comptée)

## q07 — Quand faut-il faire une analyse d'impact (AIPD) ?

Article attendu : RGPD art. 35, paragraphe 1 ou RGPD art. 35, paragraphe 3 — passage [1].

### Réponse du copilote

> Vous devez effectuer une analyse d'impact relative à la protection des données (AIPD) avant le traitement, lorsque celui-ci est « susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques » [2]. Cette obligation est requise en particulier dans trois cas : « l'évaluation systématique et approfondie d'aspects personnels concernant des personnes physiques, qui est fondée sur un traitement automatisé, y compris le profilage, et sur la base de laquelle sont prises des décisions produisant des effets juridiques à l'égard d'une personne physique ou l'affectant de manière significative de façon similaire » [1] ; « le traitement à grande échelle de catégories particulières de données visées à l'article 9, paragraphe 1, ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 » [1] ; et « la surveillance systématique à grande échelle d'une zone accessible au public » [1]. De plus, vous devez procéder à un examen pour évaluer la conformité de l'AIPD « au moins quand il se produit une modification du risque présenté par les opérations de traitement » [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « Lorsqu'un type de traitement, en particulier par le recours à de nouvelles technologies, et compte tenu de la nature, de la portée, du contexte et des finalités du traitement, est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, le responsable du traitement effectue, avant le traitement, une analyse de l'impact des opérations de traitement envisagées sur la protection des données à caractère personnel. »
  [1] « L'analyse d'impact relative à la protection des données visée au paragraphe 1 est, en particulier, requise dans les cas suivants: »
  [1] « a) l'évaluation systématique et approfondie d'aspects personnels concernant des personnes physiques, qui est fondée sur un traitement automatisé, y compris le profilage, et sur la base de laquelle sont prises des décisions produisant des effets juridiques à l'égard d'une personne physique ou l'affectant de manière significative de façon similaire; »
  [1] « b) le traitement à grande échelle de catégories particulières de données visées à l'article 9, paragraphe 1, ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10; ou »
  [1] « c) la surveillance systématique à grande échelle d'une zone accessible au public. »
  [3] « Si nécessaire, le responsable du traitement procède à un examen afin d'évaluer si le traitement est effectué conformément à l'analyse d'impact relative à la protection des données, au moins quand il se produit une modification du risque présenté par les opérations de traitement. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 35, paragraphe 3 : Analyse d'impact relative à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [2] RGPD — règlement (UE) 2016/679, article 35, paragraphe 1 : Analyse d'impact relative à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [3] RGPD — règlement (UE) 2016/679, article 35, paragraphe 11 : Analyse d'impact relative à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
Passages consultés mais non cités :
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
- [1] « L'analyse d'impact relative à la protection des données visée au paragraphe 1 est, en particulier, requise dans les cas suivants: »
- [1] « a) l'évaluation systématique et approfondie d'aspects personnels concernant des personnes physiques, qui est fondée sur un traitement automatisé, y compris le profilage, et sur la base de laquelle sont prises des décisions produisant des effets juridiques à l'égard d'une personne physique ou l'affectant de manière significative de façon similaire; »
- [1] « b) le traitement à grande échelle de catégories particulières de données visées à l'article 9, paragraphe 1, ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10; ou »
- [1] « c) la surveillance systématique à grande échelle d'une zone accessible au public. »
- [3] « Si nécessaire, le responsable du traitement procède à un examen afin d'évaluer si le traitement est effectué conformément à l'analyse d'impact relative à la protection des données, au moins quand il se produit une modification du risque présenté par les opérations de traitement. »

RÉPONSE :
Vous devez effectuer une analyse d'impact relative à la protection des données (AIPD) avant le traitement, lorsque celui-ci est « susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques » [2]. Cette obligation est requise en particulier dans trois cas : « l'évaluation systématique et approfondie d'aspects personnels concernant des personnes physiques, qui est fondée sur un traitement automatisé, y compris le profilage, et sur la base de laquelle sont prises des décisions produisant des effets juridiques à l'égard d'une personne physique ou l'affectant de manière significative de façon similaire » [1] ; « le traitement à grande échelle de catégories particulières de données visées à l'article 9, paragraphe 1, ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 » [1] ; et « la surveillance systématique à grande échelle d'une zone accessible au public » [1]. De plus, vous devez procéder à un examen pour évaluer la conformité de l'AIPD « au moins quand il se produit une modification du risque présenté par les opérations de traitement » [3].
```

</details>

Temps : recherche 2.2 s · génération 2.8 s (2530 tokens lus, 624 écrits, 347.8 tokens/s) · contrôle de pertinence 0.4 s · attente des limites de l'API 59 s (non comptée)

## q08 — Mon chatbot doit-il dire aux clients qu'il est une IA ?

Article attendu : AI Act art. 50, paragraphe 1 — passage [1].

### Réponse du copilote

> Oui, votre chatbot doit informer les clients qu'ils interagissent avec une IA, car il s'agit d'un système destiné à interagir directement avec des personnes physiques [1]. Cette obligation de transparence est toutefois soumise à une exception : elle ne s'applique pas « sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation » [1].

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
Attention : La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui, votre chatbot doit informer les clients qu'ils interagissent avec une IA, car il s'agit d'un système destiné à … » (et 1 autre(s)). Vérifiez qui est concerné.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »

RÉPONSE :
Oui, votre chatbot doit informer les clients qu'ils interagissent avec une IA, car il s'agit d'un système destiné à interagir directement avec des personnes physiques [1]. Cette obligation de transparence est toutefois soumise à une exception : elle ne s'applique pas « sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation » [1].
```

</details>

Temps : recherche 2.2 s · génération 1.1 s (3565 tokens lus, 204 écrits, 451.3 tokens/s) · contrôle de pertinence 0.3 s

## q09 — Puis-je utiliser une IA pour trier des CV ?

Article attendu : AI Act annexe III, point 4 ou AI Act art. 26 — passage [3].

### Réponse du copilote

> Oui, vous pouvez utiliser une IA pour trier des CV, car les systèmes destinés à « analyser et filtrer les candidatures » sont explicitement listés comme des systèmes d'IA à haut risque [3]. En tant que déployeur, vous devez vous assurer que le système permet « un contrôle effectif par des personnes physiques pendant leur période d’utilisation » [1]. Les mesures de contrôle doivent être « proportionnées aux risques, au niveau d’autonomie et au contexte d’utilisation » et peuvent être intégrées par le fournisseur ou mises en œuvre par vous [1]. Vous devez notamment avoir la possibilité « de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou inverser la sortie du système d’IA à haut risque » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »
  [1] « La conception et le développement des systèmes d’IA à haut risque permettent, notamment au moyen d’interfaces homme-machine appropriées, un contrôle effectif par des personnes physiques pendant leur période d’utilisation. »
  [1] « Les mesures de contrôle sont proportionnées aux risques, au niveau d’autonomie et au contexte d’utilisation du système d’IA à haut risque, et sont assurées au moyen d’un ou des deux types de mesures suivants: »
  [1] « a) des mesures identifiées et, lorsque cela est techniquement possible, intégrées par le fournisseur dans le système d’IA à haut risque avant la mise sur le marché ou la mise en service de ce dernier; »
  [1] « b) des mesures identifiées par le fournisseur avant la mise sur le marché ou la mise en service du système d’IA à haut risque et qui se prêtent à une mise en œuvre par le déployeur. »
  [1] « d) de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou inverser la sortie du système d’IA à haut risque; »

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
- [1] « La conception et le développement des systèmes d’IA à haut risque permettent, notamment au moyen d’interfaces homme-machine appropriées, un contrôle effectif par des personnes physiques pendant leur période d’utilisation. »
- [1] « Les mesures de contrôle sont proportionnées aux risques, au niveau d’autonomie et au contexte d’utilisation du système d’IA à haut risque, et sont assurées au moyen d’un ou des deux types de mesures suivants: »
- [1] « a) des mesures identifiées et, lorsque cela est techniquement possible, intégrées par le fournisseur dans le système d’IA à haut risque avant la mise sur le marché ou la mise en service de ce dernier; »
- [1] « b) des mesures identifiées par le fournisseur avant la mise sur le marché ou la mise en service du système d’IA à haut risque et qui se prêtent à une mise en œuvre par le déployeur. »
- [1] « d) de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou inverser la sortie du système d’IA à haut risque; »

RÉPONSE :
Oui, vous pouvez utiliser une IA pour trier des CV, car les systèmes destinés à « analyser et filtrer les candidatures » sont explicitement listés comme des systèmes d'IA à haut risque [3]. En tant que déployeur, vous devez vous assurer que le système permet « un contrôle effectif par des personnes physiques pendant leur période d’utilisation » [1]. Les mesures de contrôle doivent être « proportionnées aux risques, au niveau d’autonomie et au contexte d’utilisation » et peuvent être intégrées par le fournisseur ou mises en œuvre par vous [1]. Vous devez notamment avoir la possibilité « de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou inverser la sortie du système d’IA à haut risque » [1].
```

</details>

Temps : recherche 2.2 s · génération 1.7 s (3255 tokens lus, 492 écrits, 460.2 tokens/s) · contrôle de pertinence 0.3 s · attente des limites de l'API 34 s (non comptée)

## q10 — Mes salariés ou bénévoles utilisent une IA générative : ai-je des obligations ?

Article attendu : AI Act art. 4 — passage [5].

### Réponse du copilote

> Oui, en tant que déployeur de systèmes d'IA, vous avez des obligations spécifiques selon l'usage fait par vos salariés ou bénévoles.
> Vous devez prendre des mesures pour favoriser le développement de la maîtrise de l'IA par votre personnel et les autres personnes utilisant les systèmes pour votre compte, en tenant compte de leurs compétences et du contexte d'utilisation [5].
> Si vos équipes génèrent ou manipulent des images, audio ou vidéo constituant un hypertrucage, vous devez indiquer que ces contenus ont été générés ou manipulés par une IA [2].
> De même, si elles génèrent ou manipulent des textes publiés pour informer le public sur des questions d'intérêt public, vous devez indiquer que le texte a été généré ou manipulé par une IA [2].
> Si vous utilisez des systèmes d'IA à haut risque, vous devez prendre des mesures techniques et organisationnelles appropriées pour garantir que ces systèmes sont utilisés conformément aux notices d'utilisation [4].
> Notez que l'obligation d'informer les personnes qu'elles interagissent avec une IA incombe aux fournisseurs, sauf si cela est évident pour une personne normalement informée [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »
  [2] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. »
  [2] « Les déployeurs d’un système d’IA qui génère ou manipule des textes publiés dans le but d’informer le public sur des questions d’intérêt public indiquent que le texte a été généré ou manipulé par une IA. »
  [4] « Les déployeurs de systèmes d’IA à haut risque prennent des mesures techniques et organisationnelles appropriées afin de garantir qu’ils utilisent ces systèmes conformément aux notices d’utilisation accompagnant les systèmes, conformément aux paragraphes 3 et 6. »
  [5] « Les fournisseurs et les déployeurs de systèmes d'IA prennent des mesures pour favoriser le développement de la maîtrise de l'IA par leur personnel et les autres personnes s'occupant du fonctionnement et de l'utilisation des systèmes d'IA pour leur compte, en prenant en considération leurs connaissances techniques, leur expérience, leur éducation et leur formation, ainsi que le contexte dans lequel les systèmes d'IA sont destinés à être utilisés, et en tenant compte des personnes ou des groupes de personnes à l'égard desquels les systèmes d'IA sont destinés à être utilisés. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 4 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [4] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 1 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
  [5] AI Act — règlement (UE) 2024/1689, article 4 : Maîtrise de l'IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_4
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 3 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »
- [2] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. »
- [2] « Les déployeurs d’un système d’IA qui génère ou manipule des textes publiés dans le but d’informer le public sur des questions d’intérêt public indiquent que le texte a été généré ou manipulé par une IA. »
- [4] « Les déployeurs de systèmes d’IA à haut risque prennent des mesures techniques et organisationnelles appropriées afin de garantir qu’ils utilisent ces systèmes conformément aux notices d’utilisation accompagnant les systèmes, conformément aux paragraphes 3 et 6. »
- [5] « Les fournisseurs et les déployeurs de systèmes d'IA prennent des mesures pour favoriser le développement de la maîtrise de l'IA par leur personnel et les autres personnes s'occupant du fonctionnement et de l'utilisation des systèmes d'IA pour leur compte, en prenant en considération leurs connaissances techniques, leur expérience, leur éducation et leur formation, ainsi que le contexte dans lequel les systèmes d'IA sont destinés à être utilisés, et en tenant compte des personnes ou des groupes de personnes à l'égard desquels les systèmes d'IA sont destinés à être utilisés. »

RÉPONSE :
Oui, en tant que déployeur de systèmes d'IA, vous avez des obligations spécifiques selon l'usage fait par vos salariés ou bénévoles.
Vous devez prendre des mesures pour favoriser le développement de la maîtrise de l'IA par votre personnel et les autres personnes utilisant les systèmes pour votre compte, en tenant compte de leurs compétences et du contexte d'utilisation [5].
Si vos équipes génèrent ou manipulent des images, audio ou vidéo constituant un hypertrucage, vous devez indiquer que ces contenus ont été générés ou manipulés par une IA [2].
De même, si elles génèrent ou manipulent des textes publiés pour informer le public sur des questions d'intérêt public, vous devez indiquer que le texte a été généré ou manipulé par une IA [2].
Si vous utilisez des systèmes d'IA à haut risque, vous devez prendre des mesures techniques et organisationnelles appropriées pour garantir que ces systèmes sont utilisés conformément aux notices d'utilisation [4].
Notez que l'obligation d'informer les personnes qu'elles interagissent avec une IA incombe aux fournisseurs, sauf si cela est évident pour une personne normalement informée [1].
```

</details>

Temps : recherche 2.3 s · génération 2.0 s (2176 tokens lus, 649 écrits, 462.2 tokens/s) · contrôle de pertinence 0.5 s · attente des limites de l'API 35 s (non comptée)

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

Temps : recherche 2.1 s · génération 0.4 s (1975 tokens lus, 25 écrits, 452.1 tokens/s)

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

Temps : recherche 2.2 s · génération 0.3 s (2696 tokens lus, 25 écrits, 524.2 tokens/s)
