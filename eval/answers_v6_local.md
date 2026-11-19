# Réponses du copilote — v6_local

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 18/11/2026 à 15:49 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen3:4b-instruct` via Ollama 0.40.16 — température 0.1, contexte 8192 tokens, couches sur la carte graphique : toutes, 2000 tokens au plus par réponse
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu, reranker `BAAI/bge-reranker-v2-m3` sur CPU (20 candidats reclassés avant la limite par article), reformulation de la question par le modèle avant la recherche (termes juridiques ajoutés, sans conclusion)
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_v0.jsonl` (10), `eval/questions_offtopic_v0.jsonl` (0 + 2 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q01 | Dois-je désigner un DPO ? | 2/3 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([7]) : ignoré(s).; Citation vers un passage inexistant : [7] (seuls les passages [1] à [5] ont été fournis). | 110 s |
| q02 | Dois-je tenir un registre des traitements ? | 2/2 | non | — | 66 s |
| q03 | Combien de temps puis-je garder les données de mes clients ou adhérents ? | 1/2 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1]) : ignoré(s). | 72 s |
| q04 | Que dois-je mettre dans la mention d'information d'un formulaire ? | 25/26 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([4]) : ignoré(s). | 135 s |
| q05 | Une personne demande l'accès à ses données : quel délai pour répondre ? | 1/1 | non | — | 70 s |
| q06 | J'ai eu une fuite de données : que faire, et en combien de temps ? | 7/7 | non | La réponse change le sens d'une condition ou d'une exception (négation ou inversion ajoutée ou retirée, ou règle contraire à celle de l'extrait) : « sauf si la violation n'est pas susceptible d'engendrer un risque pour les droits et ». Vérifiez ce point. | 89 s |
| q07 | Quand faut-il faire une analyse d'impact (AIPD) ? | 5/5 | non | La réponse ne reprend que 5 des 13 cas énumérés au passage [4], sans dire qu'elle n'en cite qu'une partie. Vérifiez la liste complète.; La réponse s'appuie sur le RGPD et l'AI Act sans dire de quel règlement vient chaque obligation : « Une analyse d'impact (AIPD) doit être effectuée avant le traitement, lorsque ce traitement est susceptible d'engendrer … » (et 3 autre(s)). | 97 s |
| q08 | Mon chatbot doit-il dire aux clients qu'il est une IA ? | 2/2 | non | La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui, votre chatbot doit indiquer clairement qu’il s’agit d’un système d’IA, au moment de la première interaction avec … » (et 1 autre(s)). Vérifiez qui est concerné. | 62 s |
| q09 | Puis-je utiliser une IA pour trier des CV ? | 2/2 | non | La réponse cite [2] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.; La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Aucune obligation de détection ou de correction de biais n’est imposée par ce texte . ». Vérifiez ce point. | 78 s |
| q10 | Mes salariés ou bénévoles utilisent une IA générative : ai-je des obligations ? | 4/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 81 s |
| h01 | Quel est le taux de TVA en France ? | 0/0 | oui | — | 38 s |
| h02 | Comment faire une déclaration d'impôts ? | 0/0 | oui | — | 60 s |

## q01 — Dois-je désigner un DPO ?

Article attendu : RGPD art. 37 — passage [1].

### Réponse du copilote

> Oui : vous devez désigner un délégué à la protection des données (DPO) si les conditions suivantes sont remplies : si le traitement est effectué par une autorité publique ou un organisme public (sauf juridictions en exercice de leur fonction juridictionnelle), ou si vos activités de base consistent en des opérations de traitement à grande échelle nécessitant un suivi régulier et systématique des personnes concernées, ou si vous effectuez un traitement à grande échelle de catégories particulières de données (article 9) ou de données relatives à des condamnations pénales ou infractions (article 10) [1]. Dans les cas autres que ceux visés au paragraphe 1, vous pouvez désigner un DPO, ou être tenu de le désigner par le droit de l'Union ou un État membre [1]. Le responsable du traitement ou du sous-traitant publie les coordonnées du DPO et les communique à l'autorité de contrôle [7].

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
  [5] RGPD — règlement (UE) 2016/679, article 35, paragraphe 1 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
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
Oui : vous devez désigner un délégué à la protection des données (DPO) si les conditions suivantes sont remplies : si le traitement est effectué par une autorité publique ou un organisme public (sauf juridictions en exercice de leur fonction juridictionnelle), ou si vos activités de base consistent en des opérations de traitement à grande échelle nécessitant un suivi régulier et systématique des personnes concernées, ou si vous effectuez un traitement à grande échelle de catégories particulières de données (article 9) ou de données relatives à des condamnations pénales ou infractions (article 10) [1]. Dans les cas autres que ceux visés au paragraphe 1, vous pouvez désigner un DPO, ou être tenu de le désigner par le droit de l'Union ou un État membre [1]. Le responsable du traitement ou du sous-traitant publie les coordonnées du DPO et les communique à l'autorité de contrôle [7].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : Responsable de la protection des données ; personne désignée pour la protection des données ; représentant désigné ; responsable de la protection des données personnelles ; personne chargée de la protection des données ; représentant de la protection des données

Temps : recherche 50.2 s · génération 43.9 s (3026 tokens lus, 604 écrits, 34.2 tokens/s) · contrôle de pertinence 5.4 s · reformulation 10.3 s

## q02 — Dois-je tenir un registre des traitements ?

Article attendu : RGPD art. 30 — passage [1].

### Réponse du copilote

> Oui : vous devez tenir un registre des activités de traitement si vous êtes responsable du traitement ou un sous-traitant, conformément à l’article 30 du RGPD [1]. Cependant, cette obligation ne s’applique pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu’elle effectue est susceptible de comporter un risque pour les droits et libertés des personnes concernées, s’il n’est pas occasionnel ou s’il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Chaque responsable du traitement et, le cas échéant, le représentant du responsable du traitement tiennent un registre des activités de traitement effectuées sous leur responsabilité. »
  [1] « Les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 6, paragraphe 4 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
  [3] RGPD — règlement (UE) 2016/679, article 6, paragraphe 1 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
  [4] RGPD — règlement (UE) 2016/679, article 4, définition 7 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [5] RGPD — règlement (UE) 2016/679, article 24 : Responsabilité du responsable du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_24

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Chaque responsable du traitement et, le cas échéant, le représentant du responsable du traitement tiennent un registre des activités de traitement effectuées sous leur responsabilité. »
- [1] « Les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10. »

RÉPONSE :
Oui : vous devez tenir un registre des activités de traitement si vous êtes responsable du traitement ou un sous-traitant, conformément à l’article 30 du RGPD [1]. Cependant, cette obligation ne s’applique pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu’elle effectue est susceptible de comporter un risque pour les droits et libertés des personnes concernées, s’il n’est pas occasionnel ou s’il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : traitements de données ; enregistrement des traitements ; finalité du traitement ; responsable du traitement ; données personnelles

Temps : recherche 28.7 s · génération 30.2 s (3244 tokens lus, 365 écrits, 34.0 tokens/s) · contrôle de pertinence 3.8 s · reformulation 3.2 s

## q03 — Combien de temps puis-je garder les données de mes clients ou adhérents ?

Article attendu : RGPD art. 5 — passage [1].

### Réponse du copilote

> Vous pouvez conserver les données de vos clients ou adhérents pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées [1]. Cela signifie que la durée de conservation doit être proportionnée aux objectifs du traitement (par exemple, un contrat, une relation commerciale, une prestation). Si les données sont conservées pour des fins archivistiques dans l'intérêt public, ou pour des fins de recherche scientifique ou historique ou statistiques, elles peuvent être conservées plus longtemps, à condition que soient mises en œuvre des mesures techniques et organisationnelles appropriées pour garantir les droits et libertés de la personne concernée [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée (limitation de la conservation); »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 6, paragraphe 3 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
  [3] RGPD — règlement (UE) 2016/679, article 6, paragraphe 1 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
  [4] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [5] RGPD — règlement (UE) 2016/679, article 18 : Droit à la limitation du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_18
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1]) : ignoré(s).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée (limitation de la conservation); »
- [1] « les données à caractère personnel doivent être conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées; »

RÉPONSE :
Vous pouvez conserver les données de vos clients ou adhérents pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées [1]. Cela signifie que la durée de conservation doit être proportionnée aux objectifs du traitement (par exemple, un contrat, une relation commerciale, une prestation). Si les données sont conservées pour des fins archivistiques dans l'intérêt public, ou pour des fins de recherche scientifique ou historique ou statistiques, elles peuvent être conservées plus longtemps, à condition que soient mises en œuvre des mesures techniques et organisationnelles appropriées pour garantir les droits et libertés de la personne concernée [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : durée de conservation ; traitement des données ; finalité du traitement ; finalité des données ; période de stockage ; données personnelles

Temps : recherche 29.7 s · génération 35.7 s (3884 tokens lus, 344 écrits, 32.4 tokens/s) · contrôle de pertinence 3.6 s · reformulation 3.1 s

## q04 — Que dois-je mettre dans la mention d'information d'un formulaire ?

Article attendu : RGPD art. 13 — passage [1].

### Réponse du copilote

> Vous devez inclure dans la mention d'information d'un formulaire les finalités du traitement, les catégories de données concernées, les destinataires ou catégories de destinataires, la durée de conservation des données ou les critères utilisés pour déterminer cette durée, les intérêts légitimes poursuivis (si le traitement est fondé sur l'article 6, point f), l'existence du droit de rectification, d'effacement, de limitation du traitement, de s'opposer au traitement ou de porter une réclamation auprès d'une autorité de contrôle, ainsi que l'information sur la source des données (si elles ne sont pas fournies directement par la personne concernée). Si des données sont transférées à un pays tiers ou à une organisation internationale, vous devez indiquer l'existence ou l'absence d'une décision d'adéquation ou des garanties appropriées, et les moyens d'obtenir une copie de ces garanties [1], [2], [3], [4]. Vous devez aussi préciser si l'exigence de fournir les données est réglementaire ou contractuelle, et les conséquences de la non-fourniture [1], [3]. Si une prise de décision automatisée (y compris un profilage) est utilisée, vous devez fournir des informations utiles sur la logique sous-jacente, ainsi que sur l'importance et les conséquences prévues de ce traitement pour la personne concernée [1], [3], [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « les finalités du traitement auquel sont destinées les données à caractère personnel ainsi que la base juridique du traitement; »
  [1] « lorsque le traitement est fondé sur l'article 6, paragraphe 1, point f), les intérêts légitimes poursuivis par le responsable du traitement ou par un tiers; »
  [1] « les destinataires ou les catégories de destinataires des données à caractère personnel, s'ils existent; »
  [1] « le cas échéant, le fait que le responsable du traitement a l'intention d'effectuer un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale, et l'existence ou l'absence d'une décision d'adéquation rendue par la Commission ou, dans le cas des transferts visés à l'article 46 ou 47, ou à l'article 49, paragraphe 1, deuxième alinéa, la référence aux garanties appropriées ou adaptées et les moyens d'en obtenir une copie ou l'endroit où elles ont été mises à disposition; »
  [1] « la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; »
  [1] « l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ou du droit de s'opposer au traitement et du droit à la portabilité des données; »
  [1] « lorsque le traitement est fondé sur l'article 6, paragraphe 1, point a), ou sur l'article 9, paragraphe 2, point a), l'existence du droit de retirer son consentement à tout moment, sans porter atteinte à la licéité du traitement fondé sur le consentement effectué avant le retrait de celui-ci; »
  [1] « le droit d'introduire une réclamation auprès d'une autorité de contrôle; »
  [1] « des informations sur la question de savoir si l'exigence de fourniture de données à caractère personnel a un caractère réglementaire ou contractuel ou si elle conditionne la conclusion d'un contrat et si la personne concernée est tenue de fournir les données à caractère personnel, ainsi que sur les conséquences éventuelles de la non-fourniture de ces données; »
  [1] « l'existence d'une prise de décision automatisée, y compris un profilage, visée à l'article 22, paragraphes 1 et 4, et, au moins en pareils cas, des informations utiles concernant la logique sous-jacente, ainsi que l'importance et les conséquences prévues de ce traitement pour la personne concernée. »
  [2] « les catégories de données à caractère personnel concernées; »
  [2] « le cas échéant, les destinataires ou les catégories de destinataires des données à caractère personnel; »
  [2] « le cas échéant, le fait que le responsable du traitement a l'intention d'effectuer un transfert de données à caractère personnel à un destinataire dans un pays tiers ou une organisation internationale, et l'existence ou l'absence d'une décision d'adéquation rendue par la Commission ou, dans le cas des transferts visés à l'article 46 ou 47, ou à l'article 49, paragraphe 1, deuxième alinéa, la référence aux garanties appropriées ou adaptées et les moyens d'en obtenir une copie ou l'endroit où elles ont été mises à disposition; »
  [3] « lorsque le traitement est fondé sur l'article 6, paragraphe 1, point f), les intérêts légitimes poursuivis par le responsable du traitement ou par un tiers; »
  [3] « l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ainsi que du droit de s'opposer au traitement et du droit à la portabilité des données; »
  [3] « lorsque le traitement est fondé sur l'article 6, paragraphe 1, point a), ou sur l'article 9, paragraphe 2, point a), l'existence du droit de retirer le consentement à tout moment, sans porter atteinte à la licéité du traitement fondé sur le consentement effectué avant le retrait de celui-ci; »
  [3] « le droit d'introduire une réclamation auprès d'une autorité de contrôle; »
  [3] « l'existence d'une prise de décision automatisée, y compris un profilage, visée à l'article 22, paragraphes 1 et 4, et, au moins en pareils cas, des informations utiles concernant la logique sous-jacente, ainsi que l'importance et les conséquences prévues de ce traitement pour la personne concernée. »
  [4] « les catégories de données à caractère personnel concernées; »
  [4] « les destinataires ou catégories de destinataires auxquels les données à caractère personnel ont été ou seront communiquées, en particulier les destinataires qui sont établis dans des pays tiers ou les organisations internationales; »
  [4] « lorsque cela est possible, la durée de conservation des données à caractère personnel envisagée ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; »
  [4] « l'existence du droit de demander au responsable du traitement la rectification ou l'effacement de données à caractère personnel, ou une limitation du traitement des données à caractère personnel relatives à la personne concernée, ou du droit de s'opposer à ce traitement; »
  [4] « le droit d'introduire une réclamation auprès d'une autorité de contrôle; »
  [4] « lorsque les données à caractère personnel ne sont pas collectées auprès de la personne concernée, toute information disponible quant à leur source; »
  [4] « l'existence d'une prise de décision automatisée, y compris un profilage, visée à l'article 22, paragraphes 1 et 4, et, au moins en pareils cas, des informations utiles concernant la logique sous-jacente, ainsi que l'importance et les conséquences prévues de ce traitement pour la personne concernée. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [2] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [3] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [4] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
Passages consultés mais non cités :
  [5] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([4]) : ignoré(s).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « les finalités du traitement auquel sont destinées les données à caractère personnel ainsi que la base juridique du traitement; »
- [1] « lorsque le traitement est fondé sur l'article 6, paragraphe 1, point f), les intérêts légitimes poursuivis par le responsable du traitement ou par un tiers; »
- [1] « les destinataires ou les catégories de destinataires des données à caractère personnel, s'ils existent; »
- [1] « le cas échéant, le fait que le responsable du traitement a l'intention d'effectuer un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale, et l'existence ou l'absence d'une décision d'adéquation rendue par la Commission ou, dans le cas des transferts visés à l'article 46 ou 47, ou à l'article 49, paragraphe 1, deuxième alinéa, la référence aux garanties appropriées ou adaptées et les moyens d'en obtenir une copie ou l'endroit où elles ont été mises à disposition; »
- [1] « la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; »
- [1] « l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ou du droit de s'opposer au traitement et du droit à la portabilité des données; »
- [1] « lorsque le traitement est fondé sur l'article 6, paragraphe 1, point a), ou sur l'article 9, paragraphe 2, point a), l'existence du droit de retirer son consentement à tout moment, sans porter atteinte à la licéité du traitement fondé sur le consentement effectué avant le retrait de celui-ci; »
- [1] « le droit d'introduire une réclamation auprès d'une autorité de contrôle; »
- [1] « des informations sur la question de savoir si l'exigence de fourniture de données à caractère personnel a un caractère réglementaire ou contractuel ou si elle conditionne la conclusion d'un contrat et si la personne concernée est tenue de fournir les données à caractère personnel, ainsi que sur les conséquences éventuelles de la non-fourniture de ces données; »
- [1] « l'existence d'une prise de décision automatisée, y compris un profilage, visée à l'article 22, paragraphes 1 et 4, et, au moins en pareils cas, des informations utiles concernant la logique sous-jacente, ainsi que l'importance et les conséquences prévues de ce traitement pour la personne concernée. »
- [2] « les catégories de données à caractère personnel concernées; »
- [2] « le cas échéant, les destinataires ou les catégories de destinataires des données à caractère personnel; »
- [2] « le cas échéant, le fait que le responsable du traitement a l'intention d'effectuer un transfert de données à caractère personnel à un destinataire dans un pays tiers ou une organisation internationale, et l'existence ou l'absence d'une décision d'adéquation rendue par la Commission ou, dans le cas des transferts visés à l'article 46 ou 47, ou à l'article 49, paragraphe 1, deuxième alinéa, la référence aux garanties appropriées ou adaptées et les moyens d'en obtenir une copie ou l'endroit où elles ont été mises à disposition; »
- [3] « lorsque le traitement est fondé sur l'article 6, paragraphe 1, point f), les intérêts légitimes poursuivis par le responsable du traitement ou par un tiers; »
- [3] « l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ainsi que du droit de s'opposer au traitement et du droit à la portabilité des données; »
- [3] « lorsque le traitement est fondé sur l'article 6, paragraphe 1, point a), ou sur l'article 9, paragraphe 2, point a), l'existence du droit de retirer le consentement à tout moment, sans porter atteinte à la licéité du traitement fondé sur le consentement effectué avant le retrait de celui-ci; »
- [3] « le droit d'introduire une réclamation auprès d'une autorité de contrôle; »
- [3] « l'existence d'une prise de décision automatisée, y compris un profilage, visée à l'article 22, paragraphes 1 et 4, et, au moins en pareils cas, des informations utiles concernant la logique sous-jacente, ainsi que l'importance et les conséquences prévues de ce traitement pour la personne concernée. »
- [4] « les finalités du traitement; »
- [4] « les catégories de données à caractère personnel concernées; »
- [4] « les destinataires ou catégories de destinataires auxquels les données à caractère personnel ont été ou seront communiquées, en particulier les destinataires qui sont établis dans des pays tiers ou les organisations internationales; »
- [4] « lorsque cela est possible, la durée de conservation des données à caractère personnel envisagée ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; »
- [4] « l'existence du droit de demander au responsable du traitement la rectification ou l'effacement de données à caractère personnel, ou une limitation du traitement des données à caractère personnel relatives à la personne concernée, ou du droit de s'opposer à ce traitement; »
- [4] « le droit d'introduire une réclamation auprès d'une autorité de contrôle; »
- [4] « lorsque les données à caractère personnel ne sont pas collectées auprès de la personne concernée, toute information disponible quant à leur source; »
- [4] « l'existence d'une prise de décision automatisée, y compris un profilage, visée à l'article 22, paragraphes 1 et 4, et, au moins en pareils cas, des informations utiles concernant la logique sous-jacente, ainsi que l'importance et les conséquences prévues de ce traitement pour la personne concernée. »

RÉPONSE :
Vous devez inclure dans la mention d'information d'un formulaire les finalités du traitement, les catégories de données concernées, les destinataires ou catégories de destinataires, la durée de conservation des données ou les critères utilisés pour déterminer cette durée, les intérêts légitimes poursuivis (si le traitement est fondé sur l'article 6, point f), l'existence du droit de rectification, d'effacement, de limitation du traitement, de s'opposer au traitement ou de porter une réclamation auprès d'une autorité de contrôle, ainsi que l'information sur la source des données (si elles ne sont pas fournies directement par la personne concernée). Si des données sont transférées à un pays tiers ou à une organisation internationale, vous devez indiquer l'existence ou l'absence d'une décision d'adéquation ou des garanties appropriées, et les moyens d'obtenir une copie de ces garanties [1], [2], [3], [4]. Vous devez aussi préciser si l'exigence de fournir les données est réglementaire ou contractuelle, et les conséquences de la non-fourniture [1], [3]. Si une prise de décision automatisée (y compris un profilage) est utilisée, vous devez fournir des informations utiles sur la logique sous-jacente, ainsi que sur l'importance et les conséquences prévues de ce traitement pour la personne concernée [1], [3], [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : informations identifiantes ; données personnelles ; finalité du traitement ; durée de conservation ; responsabilité du traitement

Temps : recherche 28.4 s · génération 90.5 s (4203 tokens lus, 1861 écrits, 30.1 tokens/s) · contrôle de pertinence 12.9 s · reformulation 3.1 s

## q05 — Une personne demande l'accès à ses données : quel délai pour répondre ?

Article attendu : RGPD art. 12, paragraphe 3 — passage [1].

### Réponse du copilote

> Le responsable du traitement doit répondre à la demande d'accès dans un délai de un mois à compter de la réception de la demande [1]. Ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes [1]. Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [3] RGPD — règlement (UE) 2016/679, article 12, paragraphe 4 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [4] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. »

RÉPONSE :
Le responsable du traitement doit répondre à la demande d'accès dans un délai de un mois à compter de la réception de la demande [1]. Ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes [1]. Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : délai de réponse ; demande d'accès ; traitement des données ; obligation de réponse ; délai maximum ; information claire

Temps : recherche 30.5 s · génération 32.5 s (2943 tokens lus, 243 écrits, 34.8 tokens/s) · contrôle de pertinence 4.2 s · reformulation 3.1 s

## q06 — J'ai eu une fuite de données : que faire, et en combien de temps ?

Article attendu : RGPD art. 33 ou RGPD art. 34 — passage [1].

### Réponse du copilote

> Lorsqu'une fuite de données (c’est-à-dire une violation de données à caractère personnel) survient, le responsable du traitement doit en notifier la violation à l'autorité de contrôle compétente dans les meilleurs délais, et, si possible, dans les 72 heures après en avoir pris connaissance [1]. Cette notification est obligatoire, sauf si la violation n'est pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques [1]. Si la notification n’est pas faite dans les 72 heures, elle doit être accompagnée des motifs du retard [1]. En outre, le sous-traitant doit notifié au responsable du traitement toute violation dans les meilleurs délais après en avoir pris connaissance [1]. Si la violation est susceptible d'engendrer un risque élevé pour une personne physique, le responsable du traitement doit communiquer la violation à la personne concernée dans les meilleurs délais [2]. Cette communication doit être claire et simple, et doit inclure les informations et mesures visées à l'article 33, paragraphe 3, points b), c) et d) [2]. La notification à l'autorité de contrôle et la communication à la personne concernée sont des obligations du responsable du traitement, conformément à l'article 33 et à l'article 34 du RGPD [1][2]. La fuite de données est définie comme une violation de la sécurité entraînant la destruction, la perte, l'altération, la divulgation non autorisée ou l'accès non autorisé à des données à caractère personnel [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. Lorsque la notification à l'autorité de contrôle n'a pas lieu dans les 72 heures, elle est accompagnée des motifs du retard. »
  [1] « Le sous-traitant notifie au responsable du traitement toute violation de données à caractère personnel dans les meilleurs délais après en avoir pris connaissance. »
  [1] « La notification visée au paragraphe 1 doit, à tout le moins: a) décrire la nature de la violation de données à caractère personnel y compris, si possible, les catégories et le nombre approximatif de personnes concernées par la violation et les catégories et le nombre approximatif d'enregistrements de données à caractère personnel concernés; b) communiquer le nom et les coordonnées du délégué à la protection des données ou d'un autre point de contact auprès duquel des informations supplémentaires peuvent être obtenues; c) décrire les conséquences probables de la violation de données à caractère personnel; d) décrire les mesures prises ou que le responsable du traitement propose de prendre pour remédier à la violation de données à caractère personnel, y compris, le cas échéant, les mesures pour en atténuer les éventuelles conséquences négatives. »
  [2] « Lorsqu'une violation de données à caractère personnel est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement communique la violation de données à caractère personnel à la personne concernée dans les meilleurs délais. »
  [2] « La communication à la personne concernée visée au paragraphe 1 du présent article décrit, en des termes clairs et simples, la nature de la violation de données à caractère personnel et contient au moins les informations et mesures visées à l'article 33, paragraphe 3, points b), c) et d). »
  [3] « «violation de données à caractère personnel», une violation de la sécurité entraînant, de manière accidentelle ou illicite, la destruction, la perte, l'altération, la divulgation non autorisée de données à caractère personnel transmises, conservées ou traitées d'une autre manière, ou l'accès non autorisé à de telles données; »
  [4] « Le responsable du traitement fournit les informations visées aux paragraphes 1 et 2: a) dans un délai raisonnable après avoir obtenu les données à caractère personnel, mais ne dépassant pas un mois, eu égard aux circonstances particulières dans lesquelles les données à caractère personnel sont traitées; b) si les données à caractère personnel doivent être utilisées aux fins de la communication avec la personne concernée, au plus tard au moment de la première communication à ladite personne; ou c) s'il est envisagé de communiquer les informations à un autre destinataire, au plus tard lorsque les données à caractère personnel sont communiquées pour la première fois. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 33 : Notification à l'autorité de contrôle d'une violation de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_33
  [2] RGPD — règlement (UE) 2016/679, article 34 : Communication à la personne concernée d'une violation de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_34
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 12 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [4] RGPD — règlement (UE) 2016/679, article 14, paragraphe 3 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
Passages consultés mais non cités :
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
Attention : La réponse change le sens d'une condition ou d'une exception (négation ou inversion ajoutée ou retirée, ou règle contraire à celle de l'extrait) : « sauf si la violation n'est pas susceptible d'engendrer un risque pour les droits et ». Vérifiez ce point.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. Lorsque la notification à l'autorité de contrôle n'a pas lieu dans les 72 heures, elle est accompagnée des motifs du retard. »
- [1] « Le sous-traitant notifie au responsable du traitement toute violation de données à caractère personnel dans les meilleurs délais après en avoir pris connaissance. »
- [1] « La notification visée au paragraphe 1 doit, à tout le moins: a) décrire la nature de la violation de données à caractère personnel y compris, si possible, les catégories et le nombre approximatif de personnes concernées par la violation et les catégories et le nombre approximatif d'enregistrements de données à caractère personnel concernés; b) communiquer le nom et les coordonnées du délégué à la protection des données ou d'un autre point de contact auprès duquel des informations supplémentaires peuvent être obtenues; c) décrire les conséquences probables de la violation de données à caractère personnel; d) décrire les mesures prises ou que le responsable du traitement propose de prendre pour remédier à la violation de données à caractère personnel, y compris, le cas échéant, les mesures pour en atténuer les éventuelles conséquences négatives. »
- [2] « Lorsqu'une violation de données à caractère personnel est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement communique la violation de données à caractère personnel à la personne concernée dans les meilleurs délais. »
- [2] « La communication à la personne concernée visée au paragraphe 1 du présent article décrit, en des termes clairs et simples, la nature de la violation de données à caractère personnel et contient au moins les informations et mesures visées à l'article 33, paragraphe 3, points b), c) et d). »
- [3] « «violation de données à caractère personnel», une violation de la sécurité entraînant, de manière accidentelle ou illicite, la destruction, la perte, l'altération, la divulgation non autorisée de données à caractère personnel transmises, conservées ou traitées d'une autre manière, ou l'accès non autorisé à de telles données; »
- [4] « Le responsable du traitement fournit les informations visées aux paragraphes 1 et 2: a) dans un délai raisonnable après avoir obtenu les données à caractère personnel, mais ne dépassant pas un mois, eu égard aux circonstances particulières dans lesquelles les données à caractère personnel sont traitées; b) si les données à caractère personnel doivent être utilisées aux fins de la communication avec la personne concernée, au plus tard au moment de la première communication à ladite personne; ou c) s'il est envisagé de communiquer les informations à un autre destinataire, au plus tard lorsque les données à caractère personnel sont communiquées pour la première fois. »

RÉPONSE :
Lorsqu'une fuite de données (c’est-à-dire une violation de données à caractère personnel) survient, le responsable du traitement doit en notifier la violation à l'autorité de contrôle compétente dans les meilleurs délais, et, si possible, dans les 72 heures après en avoir pris connaissance [1]. Cette notification est obligatoire, sauf si la violation n'est pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques [1]. Si la notification n’est pas faite dans les 72 heures, elle doit être accompagnée des motifs du retard [1]. En outre, le sous-traitant doit notifié au responsable du traitement toute violation dans les meilleurs délais après en avoir pris connaissance [1]. Si la violation est susceptible d'engendrer un risque élevé pour une personne physique, le responsable du traitement doit communiquer la violation à la personne concernée dans les meilleurs délais [2]. Cette communication doit être claire et simple, et doit inclure les informations et mesures visées à l'article 33, paragraphe 3, points b), c) et d) [2]. La notification à l'autorité de contrôle et la communication à la personne concernée sont des obligations du responsable du traitement, conformément à l'article 33 et à l'article 34 du RGPD [1][2]. La fuite de données est définie comme une violation de la sécurité entraînant la destruction, la perte, l'altération, la divulgation non autorisée ou l'accès non autorisé à des données à caractère personnel [3].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : fuite de données ; notification ; délai de notification ; responsable de la protection des données ; traitement de données ; données personnelles

Temps : recherche 28.4 s · génération 50.0 s (2944 tokens lus, 1115 écrits, 33.6 tokens/s) · contrôle de pertinence 7.6 s · reformulation 3.1 s

## q07 — Quand faut-il faire une analyse d'impact (AIPD) ?

Article attendu : RGPD art. 35, paragraphe 1 ou RGPD art. 35, paragraphe 3 — passage [1].

### Réponse du copilote

> Une analyse d'impact (AIPD) doit être effectuée avant le traitement, lorsque ce traitement est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, notamment en cas de traitement automatisé fondé sur le profilage ou de décisions produisant des effets juridiques [2]. Elle est également requise dans les cas précisés à l'article 35, paragraphe 1, point 3, a), b) ou c) : l'évaluation systématique d'aspects personnels fondée sur un traitement automatisé, le traitement à grande échelle de catégories particulières de données ou de données relatives à des condamnations pénales, ou la surveillance systématique à grande échelle d'une zone accessible au public [1]. Pour les systèmes d’IA à haut risque, une analyse d’impact sur les droits fondamentaux est obligatoire avant leur déploiement, à l’exception des systèmes utilisés dans le domaine visé à l’annexe III, point 2 [3]. Cette obligation s’applique à la première utilisation du système, et peut être basée sur des analyses antérieures ou existantes [3]. Les déployeurs doivent également tenir compte des critères précisés à l’article 7, point 2, lors de l’évaluation du risque de préjudice ou d’incidence négative [4]. Le risque de préjudice ou d’incidence négative doit être équivalent ou supérieur à celui des systèmes d’IA à haut risque déjà visés à l’annexe III pour que l’analyse soit requise [5].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « L'analyse d'impact relative à la protection des données visée au paragraphe 1 est, en particulier, requise dans les cas suivants: a) l'évaluation systématique et approfondie d'aspects personnels concernant des personnes physiques, qui est fondée sur un traitement automatisé, y compris le profilage, et sur la base de laquelle sont prises des décisions produisant des effets juridiques à l'égard d'une personne physique ou l'affectant de manière significative de façon similaire; b) le traitement à grande échelle de catégories particulières de données visées à l'article 9, paragraphe 1, ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10; ou c) la surveillance systématique à grande échelle d'une zone accessible au public. »
  [2] « Lorsqu'un type de traitement, en particulier par le recours à de nouvelles technologies, et compte tenu de la nature, de la portée, du contexte et des finalités du traitement, est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, le responsable du traitement effectue, avant le traitement, une analyse de l'impact des opérations de traitement envisagées sur la protection des données à caractère personnel. Une seule et même analyse peut porter sur un ensemble d'opérations de traitement similaires qui présentent des risques élevés similaires. »
  [3] « Avant le déploiement d’un système d’IA à haut risque visé à l’article 6, paragraphe 2, à l’exception des systèmes d’IA à haut risque destinés à être utilisés dans le domaine visé à l’annexe III, point 2, les déployeurs qui sont des organismes de droit public ou des entités privées fournissant des services publics et les déployeurs de systèmes d’IA à haut risque visés à l’annexe III, points 5), b) et c), effectuent une analyse de l’impact sur les droits fondamentaux que l’utilisation de ce système peut produire. »
  [4] « Lorsqu’elle évalue les conditions visées au paragraphe 1, point b), la Commission tient compte des critères suivants: … »
  [5] « La Commission est habilitée à adopter des actes délégués conformément à l’article 97 pour modifier l’annexe III en y ajoutant des cas d’utilisation de systèmes d’IA à haut risque, ou en les modifiant, lorsque les deux conditions suivantes sont remplies: a) les systèmes d’IA sont destinés à être utilisés dans l’un des domaines énumérés à l’annexe III; b) les systèmes d’IA présentent un risque de préjudice pour la santé et la sécurité, ou un risque d’incidence négative sur les droits fondamentaux, et ce risque est équivalent ou supérieur au risque de préjudice ou d’incidence négative que présentent les systèmes d’IA à haut risque déjà visés à l’annexe III. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 35, paragraphe 3 : Analyse d'impact relative à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [2] RGPD — règlement (UE) 2016/679, article 35, paragraphe 1 : Analyse d'impact relative à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [3] AI Act — règlement (UE) 2024/1689, article 27 : Analyse d’impact des systèmes d’IA à haut risque sur les droits fondamentaux (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_27
  [4] AI Act — règlement (UE) 2024/1689, article 7, paragraphe 2 : Modifications de l’annexe III (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_7
  [5] AI Act — règlement (UE) 2024/1689, article 7, paragraphe 1 : Modifications de l’annexe III (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_7
Attention : La réponse ne reprend que 5 des 13 cas énumérés au passage [4], sans dire qu'elle n'en cite qu'une partie. Vérifiez la liste complète.
Attention : La réponse s'appuie sur le RGPD et l'AI Act sans dire de quel règlement vient chaque obligation : « Une analyse d'impact (AIPD) doit être effectuée avant le traitement, lorsque ce traitement est susceptible d'engendrer … » (et 3 autre(s)).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « L'analyse d'impact relative à la protection des données visée au paragraphe 1 est, en particulier, requise dans les cas suivants: a) l'évaluation systématique et approfondie d'aspects personnels concernant des personnes physiques, qui est fondée sur un traitement automatisé, y compris le profilage, et sur la base de laquelle sont prises des décisions produisant des effets juridiques à l'égard d'une personne physique ou l'affectant de manière significative de façon similaire; b) le traitement à grande échelle de catégories particulières de données visées à l'article 9, paragraphe 1, ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10; ou c) la surveillance systématique à grande échelle d'une zone accessible au public. »
- [2] « Lorsqu'un type de traitement, en particulier par le recours à de nouvelles technologies, et compte tenu de la nature, de la portée, du contexte et des finalités du traitement, est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, le responsable du traitement effectue, avant le traitement, une analyse de l'impact des opérations de traitement envisagées sur la protection des données à caractère personnel. Une seule et même analyse peut porter sur un ensemble d'opérations de traitement similaires qui présentent des risques élevés similaires. »
- [3] « Avant le déploiement d’un système d’IA à haut risque visé à l’article 6, paragraphe 2, à l’exception des systèmes d’IA à haut risque destinés à être utilisés dans le domaine visé à l’annexe III, point 2, les déployeurs qui sont des organismes de droit public ou des entités privées fournissant des services publics et les déployeurs de systèmes d’IA à haut risque visés à l’annexe III, points 5), b) et c), effectuent une analyse de l’impact sur les droits fondamentaux que l’utilisation de ce système peut produire. »
- [4] « Lorsqu’elle évalue les conditions visées au paragraphe 1, point b), la Commission tient compte des critères suivants: … »
- [5] « La Commission est habilitée à adopter des actes délégués conformément à l’article 97 pour modifier l’annexe III en y ajoutant des cas d’utilisation de systèmes d’IA à haut risque, ou en les modifiant, lorsque les deux conditions suivantes sont remplies: a) les systèmes d’IA sont destinés à être utilisés dans l’un des domaines énumérés à l’annexe III; b) les systèmes d’IA présentent un risque de préjudice pour la santé et la sécurité, ou un risque d’incidence négative sur les droits fondamentaux, et ce risque est équivalent ou supérieur au risque de préjudice ou d’incidence négative que présentent les systèmes d’IA à haut risque déjà visés à l’annexe III. »

RÉPONSE :
Une analyse d'impact (AIPD) doit être effectuée avant le traitement, lorsque ce traitement est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, notamment en cas de traitement automatisé fondé sur le profilage ou de décisions produisant des effets juridiques [2]. Elle est également requise dans les cas précisés à l'article 35, paragraphe 1, point 3, a), b) ou c) : l'évaluation systématique d'aspects personnels fondée sur un traitement automatisé, le traitement à grande échelle de catégories particulières de données ou de données relatives à des condamnations pénales, ou la surveillance systématique à grande échelle d'une zone accessible au public [1]. Pour les systèmes d’IA à haut risque, une analyse d’impact sur les droits fondamentaux est obligatoire avant leur déploiement, à l’exception des systèmes utilisés dans le domaine visé à l’annexe III, point 2 [3]. Cette obligation s’applique à la première utilisation du système, et peut être basée sur des analyses antérieures ou existantes [3]. Les déployeurs doivent également tenir compte des critères précisés à l’article 7, point 2, lors de l’évaluation du risque de préjudice ou d’incidence négative [4]. Le risque de préjudice ou d’incidence négative doit être équivalent ou supérieur à celui des systèmes d’IA à haut risque déjà visés à l’annexe III pour que l’analyse soit requise [5].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : analyse d'impact sur le traitement des données ; évaluation des risques liés au traitement ; examen de la conformité avec le règlement ; évaluation des effets sur les droits fondamentaux ; vérification des finalités du traitement

Temps : recherche 24.9 s · génération 59.6 s (3688 tokens lus, 1134 écrits, 31.9 tokens/s) · contrôle de pertinence 8.5 s · reformulation 4.0 s

## q08 — Mon chatbot doit-il dire aux clients qu'il est une IA ?

Article attendu : AI Act art. 50, paragraphe 1 — passage [1].

### Réponse du copilote

> Oui, votre chatbot doit indiquer clairement qu’il s’agit d’un système d’IA, au moment de la première interaction avec un client, car il est destiné à interagir directement avec des personnes physiques [1]. Cette information doit être fournie de manière claire et reconnaissable [2]. Cependant, cette obligation ne s’applique pas si l’information qu’il s’agit d’un système d’IA ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation [1].

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
  [3] AI Act — règlement (UE) 2024/1689, article 3, définition 1 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
  [4] AI Act — règlement (UE) 2024/1689, annexe III, point 8 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [5] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points a) à e) : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
Attention : La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui, votre chatbot doit indiquer clairement qu’il s’agit d’un système d’IA, au moment de la première interaction avec … » (et 1 autre(s)). Vérifiez qui est concerné.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »  
- [2] « Les informations visées aux paragraphes 1 à 4 sont fournies aux personnes physiques concernées de manière claire et reconnaissable au plus tard au moment de la première interaction ou de la première exposition. »  

RÉPONSE :  
Oui, votre chatbot doit indiquer clairement qu’il s’agit d’un système d’IA, au moment de la première interaction avec un client, car il est destiné à interagir directement avec des personnes physiques [1]. Cette information doit être fournie de manière claire et reconnaissable [2]. Cependant, cette obligation ne s’applique pas si l’information qu’il s’agit d’un système d’IA ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : information sur l'origine de l'IA ; déclaration explicite de l'automatisation ; nature de l'entité ; capacité de traitement de données ; fonctionnement autonome ; utilisation de modèles d'IA

Temps : recherche 27.1 s · génération 27.1 s (3034 tokens lus, 320 écrits, 34.5 tokens/s) · contrôle de pertinence 4.6 s · reformulation 3.6 s

## q09 — Puis-je utiliser une IA pour trier des CV ?

Article attendu : AI Act annexe III, point 4 ou AI Act art. 26 — passage [1].

### Réponse du copilote

> Oui : vous pouvez utiliser une IA pour trier des CV, car cela relève du domaine du recrutement et de la sélection de personnes physiques, comme prévus à l’article 6, paragraphe 2, de l’AI Act, dans l’annexe III, point a) [1]. Cependant, cette utilisation est interdite si elle exploite des vulnérabilités liées à l’âge, au handicap ou à la situation sociale ou économique d’une personne, avec un effet de manipulation ou de préjudice important [4]. Aucune obligation de détection ou de correction de biais n’est imposée par ce texte [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »
  [4] « la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui exploite les éventuelles vulnérabilités dues à l’âge, au handicap ou à la situation sociale ou économique spécifique d’une personne physique ou d’un groupe de personnes donné avec pour objectif ou effet d’altérer substantiellement le comportement de cette personne ou d’un membre de ce groupe d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne ou à un tiers; »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [2] AI Act — règlement (UE) 2024/1689, article 4 bis : Traitement de catégories particulières de données à caractère personnel à des fins de détection et de correction des biais (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_4a
  [4] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points a) à e) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, annexe III, point 5 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [5] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
Attention : La réponse cite [2] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.
Attention : La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Aucune obligation de détection ou de correction de biais n’est imposée par ce texte . ». Vérifiez ce point.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »
- [4] « la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui exploite les éventuelles vulnérabilités dues à l’âge, au handicap ou à la situation sociale ou économique spécifique d’une personne physique ou d’un groupe de personnes donné avec pour objectif ou effet d’altérer substantiellement le comportement de cette personne ou d’un membre de ce groupe d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne ou à un tiers; »

RÉPONSE :
Oui : vous pouvez utiliser une IA pour trier des CV, car cela relève du domaine du recrutement et de la sélection de personnes physiques, comme prévus à l’article 6, paragraphe 2, de l’AI Act, dans l’annexe III, point a) [1]. Cependant, cette utilisation est interdite si elle exploite des vulnérabilités liées à l’âge, au handicap ou à la situation sociale ou économique d’une personne, avec un effet de manipulation ou de préjudice important [4]. Aucune obligation de détection ou de correction de biais n’est imposée par ce texte [2].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données personnelles ; traitement automatisé ; finalité du traitement ; données sensibles ; consentement explicite ; finalité déterminée

Temps : recherche 29.6 s · génération 41.1 s (4345 tokens lus, 344 écrits, 31.5 tokens/s) · contrôle de pertinence 3.9 s · reformulation 3.1 s

## q10 — Mes salariés ou bénévoles utilisent une IA générative : ai-je des obligations ?

Article attendu : AI Act art. 4 — passage [1].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 4 : Maîtrise de l'IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_4
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 4 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [3] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 7 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
  [4] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 1 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
  [5] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 3 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les fournisseurs et les déployeurs de systèmes d'IA prennent des mesures pour favoriser le développement de la maîtrise de l'IA par leur personnel et les autres personnes s'occupant du fonctionnement et de l'utilisation des systèmes d'IA pour leur compte, en prenant en considération leurs connaissances techniques, leur expérience, leur éducation et leur formation, ainsi que le contexte dans lequel les systèmes d'IA sont destinés à être utilisés, et en tenant compte des personnes ou des groupes de personnes à l'égard desquels les systèmes d'IA sont destinés à être utilisés. Cette obligation ne contraint pas les fournisseurs ou les déployeurs à garantir un niveau spécifique de maîtrise de l'IA par un individu. »  
- [2] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. Cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. Lorsque le contenu fait partie d’une œuvre ou d’un programme manifestement artistique, créatif, satirique, fictif ou analogue, les obligations de transparence énoncées au présent paragraphe se limitent à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre. Les déployeurs d’un système d’IA qui génère ou manipule des textes publiés dans le but d’informer le public sur des questions d’intérêt public indiquent que le texte a été généré ou manipulé par une IA. Cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière, ou lorsque le contenu généré par l’IA a fait l’objet d’un processus d’examen humain ou de contrôle éditorial et lorsqu’une personne physique ou morale assume la responsabilité éditoriale de la publication du contenu. »  
- [3] « Avant de mettre en service ou d’utiliser un système d’IA à haut risque sur le lieu de travail, les déployeurs qui sont des employeurs informent les représentants des travailleurs et les travailleurs concernés qu’ils seront soumis à l’utilisation du système d’IA à haut risque. Ces informations sont fournies, le cas échéant, conformément aux règles et procédures prévues par le droit de l’Union et le droit national et aux pratiques en matière d’information des travailleurs et de leurs représentants. »  
- [4] « Les déployeurs de systèmes d’IA à haut risque prennent des mesures techniques et organisationnelles appropriées afin de garantir qu’ils utilisent ces systèmes conformément aux notices d’utilisation accompagnant les systèmes, conformément aux paragraphes 3 et 6. »  

RÉPONSE :  
Oui : si vous êtes un déployeur de systèmes d’IA génératifs utilisés par vos salariés ou bénévoles, vous avez des obligations en vertu de l’AI Act. Vous devez prendre des mesures pour favoriser la maîtrise de l’IA par vos salariés ou bénévoles, en tenant compte de leurs connaissances, expérience, formation et du contexte d’utilisation [1]. Si les contenus générés par l’IA sont des images, contenus audio ou vidéo constituant un hypertrucage, vous devez indiquer clairement que ces contenus ont été générés ou manipulés par une IA [2]. Si les contenus sont destinés à informer le public sur des questions d’intérêt public, vous devez aussi indiquer que le texte a été généré ou manipulé par une IA [2]. Si le système d’IA que vous utilisez est classé à haut risque, vous devez informer les travailleurs ou bénévoles concernés qu’ils seront soumis à son utilisation [3]. Vous devez également mettre en œuvre des mesures techniques et organisationnelles appropriées pour garantir une utilisation conforme aux notices d’utilisation [4]. Ces obligations s’appliquent à tous les cas d’utilisation, sauf dans les cas où l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière [2].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données personnelles ; traitements de données ; finalité du traitement ; responsabilité du responsable ; données sensibles

Temps : recherche 26.9 s · génération 43.7 s (2484 tokens lus, 1076 écrits, 34.8 tokens/s) · contrôle de pertinence 7.5 s · reformulation 3.1 s

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
RÉPONSE : Les textes trouvés ne traitent pas de la TVA en France.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : taux de TVA ; imposition des produits et services ; valeur ajoutée ; taxe ; contribution ; prélèvement

Temps : recherche 22.9 s · génération 11.6 s (2269 tokens lus, 29 écrits, 38.4 tokens/s) · reformulation 3.1 s

## h02 — Comment faire une déclaration d'impôts ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 57, paragraphe 2 : Missions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_57
  [2] RGPD — règlement (UE) 2016/679, article 57, paragraphe 1, points a) à t) : Missions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_57
  [3] RGPD — règlement (UE) 2016/679, article 47, paragraphe 2, points a) à k) : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
  [4] RGPD — règlement (UE) 2016/679, article 47, paragraphe 1 : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
  [5] AI Act — règlement (UE) 2024/1689, annexe V : Déclaration UE de conformité
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_V

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun  
RÉPONSE : Les textes trouvés ne traitent pas de la déclaration d'impôts.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : déclaration fiscale ; formulaire ; obligation ; retour ; paiement ; dossier

Temps : recherche 29.6 s · génération 27.6 s (3971 tokens lus, 32 écrits, 33.7 tokens/s) · reformulation 2.8 s
