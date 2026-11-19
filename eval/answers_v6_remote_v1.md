# Réponses du copilote — v6_remote_v1

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 18/11/2026 à 17:11 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen/qwen3.8-27b` via l'API compatible OpenAI https://api.groq.com/openai/v1 (expérience de la séance 7, questions de test seulement ; modèle tel que servi par l'API à la date ci-dessus) — température 0.1, raisonnement : réglage par défaut du modèle, passages calculés pour un contexte de 8192 tokens comme en local, 2000 tokens au plus par réponse (raisonnement compris) ; le juge est le même modèle
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu, reranker `BAAI/bge-reranker-v2-m3` sur CPU (20 candidats reclassés avant la limite par article), reformulation de la question par le modèle avant la recherche (termes juridiques ajoutés, sans conclusion)
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_v1.jsonl` (17 + 3 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q11 | Un client me demande d'effacer toutes ses données : suis-je obligé de le faire ? | 13/13 | non | — | 41 s |
| q12 | Un salarié demande une copie de toutes les données que nous avons sur lui : que dois-je lui donner ? | 5/6 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1]) : ignoré(s).; La réponse met entre « » un texte introuvable dans les extraits vérifiés : « les finalités du traitement ». | 30 s |
| q13 | Un adhérent veut récupérer ses données pour les donner à une autre association : est-ce un droit ? | 4/4 | non | — | 32 s |
| q14 | Puis-je envoyer une lettre d'information par e-mail à mes adhérents, et peuvent-ils refuser ? | 5/5 | non | — | 32 s |
| q15 | Mon prestataire informatique a accès à nos fichiers : faut-il signer un contrat particulier ? | 6/6 | non | — | 39 s |
| q16 | Puis-je stocker les fichiers de mon association chez un hébergeur situé aux États-Unis ? | 6/6 | non | — | 35 s |
| q17 | Quelles sanctions risque une petite entreprise qui ne respecte pas le RGPD ? | 2/5 | non | 3 extrait(s) introuvable(s) mot pour mot dans le passage cité ([2], [4], [4]) : ignoré(s).; La réponse cite [2], [4] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations. | 30 s |
| q18 | Notre association peut-elle collecter des informations sur la santé de ses bénévoles ? | 6/6 | non | La réponse ne reprend que 7 des 9 cas énumérés au passage [1], sans dire qu'elle n'en cite qu'une partie. Vérifiez la liste complète. | 29 s |
| q19 | Qu'est-ce qu'une donnée personnelle ? | 2/2 | non | — | 30 s |
| q20 | À partir de quel âge un enfant peut-il s'inscrire seul à notre service en ligne ? | 3/3 | non | — | 26 s |
| q21 | Comment dois-je protéger les données personnelles que nous conservons ? | 6/6 | non | — | 28 s |
| q22 | Le consentement d'une personne doit-il être donné par écrit ? | 2/2 | non | La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Non, le consentement ne doit pas obligatoirement être donné par écrit. ». Vérifiez ce point. | 25 s |
| q23 | Quelles utilisations de l'intelligence artificielle sont interdites en Europe ? | 6/6 | non | — | 32 s |
| q24 | Ai-je le droit d'utiliser une IA qui analyse les émotions de mes salariés ? | 4/4 | non | — | 34 s |
| q25 | Mon logiciel est-il un « système d'IA » au sens de la loi européenne ? | 1/1 | non | — | 33 s |
| q26 | Dois-je indiquer qu'une image publiée sur notre site a été créée par une IA ? | 4/4 | non | La réponse met entre « » un texte introuvable dans les extraits vérifiés : « indiquez que les contenus ont été générés ou manipulés par une IA ». | 35 s |
| q27 | Quelles amendes prévoit le règlement européen sur l'intelligence artificielle ? | 5/5 | non | — | 33 s |
| h03 | Comment déclarer la création d'une association en préfecture ? | 0/0 | oui | — | 22 s |
| h04 | Quel est le montant du SMIC cette année ? | 0/0 | oui | — | 27 s |
| h05 | Comment rédiger les statuts d'une association ? | 0/0 | oui | — | 29 s |

## q11 — Un client me demande d'effacer toutes ses données : suis-je obligé de le faire ?

Article attendu : RGPD art. 17 — passage [1].

### Réponse du copilote

> Non, vous n'êtes pas obligé d'effacer toutes les données de votre client dans tous les cas, car le droit à l'effacement (RGPD, article 17) ne s'applique que si l'un des motifs spécifiques prévus par la loi est rempli [1]. Vous avez l'obligation d'effacer les données « dans les meilleurs délais » uniquement lorsque, par exemple, « les données à caractère personnel ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées d'une autre manière » [1], ou si « la personne concernée retire le consentement sur lequel est fondé le traitement [...] et il n'existe pas d'autre fondement juridique au traitement » [1]. L'effacement est également requis si « la personne concernée s'oppose au traitement en vertu de l'article 21, paragraphe 1, et il n'existe pas de motif légitime impérieux pour le traitement » [1], si « les données à caractère personnel ont fait l'objet d'un traitement illicite » [1], si « les données à caractère personnel doivent être effacées pour respecter une obligation légale qui est prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis » [1], ou si « les données à caractère personnel ont été collectées dans le cadre de l'offre de services de la société de l'information visée à l'article 8, paragraphe 1 » [1]. En revanche, le droit à l'effacement ne s'applique pas si le traitement est nécessaire « à l'exercice du droit à la liberté d'expression et d'information » [1], « pour respecter une obligation légale qui requiert le traitement prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis, ou pour exécuter une mission d'intérêt public ou relevant de l'exercice de l'autorité publique dont est investi le responsable du traitement » [1], « pour des motifs d'intérêt public dans le domaine de la santé publique, conformément à l'article 9, paragraphe 2, points h) et i), ainsi qu'à l'article 9, paragraphe 3 » [1], « à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, dans la mesure où le droit visé au paragraphe 1 est susceptible de rendre impossible ou de compromettre gravement la réalisation des objectifs dudit traitement » [1], ou « à la constatation, à l'exercice ou à la défense de droits en justice » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit d'obtenir du responsable du traitement l'effacement, dans les meilleurs délais, de données à caractère personnel la concernant et le responsable du traitement a l'obligation d'effacer ces données à caractère personnel dans les meilleurs délais, lorsque l'un des motifs suivants s'applique: »
  [1] « a) les données à caractère personnel ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées d'une autre manière; »
  [1] « b) la personne concernée retire le consentement sur lequel est fondé le traitement, conformément à l'article 6, paragraphe 1, point a), ou à l'article 9, paragraphe 2, point a), et il n'existe pas d'autre fondement juridique au traitement; »
  [1] « c) la personne concernée s'oppose au traitement en vertu de l'article 21, paragraphe 1, et il n'existe pas de motif légitime impérieux pour le traitement, ou la personne concernée s'oppose au traitement en vertu de l'article 21, paragraphe 2; »
  [1] « d) les données à caractère personnel ont fait l'objet d'un traitement illicite; »
  [1] « e) les données à caractère personnel doivent être effacées pour respecter une obligation légale qui est prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis; »
  [1] « f) les données à caractère personnel ont été collectées dans le cadre de l'offre de services de la société de l'information visée à l'article 8, paragraphe 1. »
  [1] « Les paragraphes 1 et 2 ne s'appliquent pas dans la mesure où ce traitement est nécessaire: »
  [1] « a) à l'exercice du droit à la liberté d'expression et d'information; »
  [1] « b) pour respecter une obligation légale qui requiert le traitement prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis, ou pour exécuter une mission d'intérêt public ou relevant de l'exercice de l'autorité publique dont est investi le responsable du traitement; »
  [1] « c) pour des motifs d'intérêt public dans le domaine de la santé publique, conformément à l'article 9, paragraphe 2, points h) et i), ainsi qu'à l'article 9, paragraphe 3; »
  [1] « d) à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, dans la mesure où le droit visé au paragraphe 1 est susceptible de rendre impossible ou de compromettre gravement la réalisation des objectifs dudit traitement; ou »
  [1] « e) à la constatation, à l'exercice ou à la défense de droits en justice. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 17 : Droit à l'effacement («droit à l'oubli») (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_17
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [3] RGPD — règlement (UE) 2016/679, article 19 : Obligation de notification en ce qui concerne la rectification ou l'effacement de données à caractère personnel ou la limitation du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_19
  [4] RGPD — règlement (UE) 2016/679, article 18 : Droit à la limitation du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_18
  [5] RGPD — règlement (UE) 2016/679, article 21 : Droit d'opposition
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_21

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « La personne concernée a le droit d'obtenir du responsable du traitement l'effacement, dans les meilleurs délais, de données à caractère personnel la concernant et le responsable du traitement a l'obligation d'effacer ces données à caractère personnel dans les meilleurs délais, lorsque l'un des motifs suivants s'applique: »
- [1] « a) les données à caractère personnel ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées d'une autre manière; »
- [1] « b) la personne concernée retire le consentement sur lequel est fondé le traitement, conformément à l'article 6, paragraphe 1, point a), ou à l'article 9, paragraphe 2, point a), et il n'existe pas d'autre fondement juridique au traitement; »
- [1] « c) la personne concernée s'oppose au traitement en vertu de l'article 21, paragraphe 1, et il n'existe pas de motif légitime impérieux pour le traitement, ou la personne concernée s'oppose au traitement en vertu de l'article 21, paragraphe 2; »
- [1] « d) les données à caractère personnel ont fait l'objet d'un traitement illicite; »
- [1] « e) les données à caractère personnel doivent être effacées pour respecter une obligation légale qui est prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis; »
- [1] « f) les données à caractère personnel ont été collectées dans le cadre de l'offre de services de la société de l'information visée à l'article 8, paragraphe 1. »
- [1] « Les paragraphes 1 et 2 ne s'appliquent pas dans la mesure où ce traitement est nécessaire: »
- [1] « a) à l'exercice du droit à la liberté d'expression et d'information; »
- [1] « b) pour respecter une obligation légale qui requiert le traitement prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis, ou pour exécuter une mission d'intérêt public ou relevant de l'exercice de l'autorité publique dont est investi le responsable du traitement; »
- [1] « c) pour des motifs d'intérêt public dans le domaine de la santé publique, conformément à l'article 9, paragraphe 2, points h) et i), ainsi qu'à l'article 9, paragraphe 3; »
- [1] « d) à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, dans la mesure où le droit visé au paragraphe 1 est susceptible de rendre impossible ou de compromettre gravement la réalisation des objectifs dudit traitement; ou »
- [1] « e) à la constatation, à l'exercice ou à la défense de droits en justice. »

RÉPONSE :
Non, vous n'êtes pas obligé d'effacer toutes les données de votre client dans tous les cas, car le droit à l'effacement (RGPD, article 17) ne s'applique que si l'un des motifs spécifiques prévus par la loi est rempli [1]. Vous avez l'obligation d'effacer les données « dans les meilleurs délais » uniquement lorsque, par exemple, « les données à caractère personnel ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées d'une autre manière » [1], ou si « la personne concernée retire le consentement sur lequel est fondé le traitement [...] et il n'existe pas d'autre fondement juridique au traitement » [1]. L'effacement est également requis si « la personne concernée s'oppose au traitement en vertu de l'article 21, paragraphe 1, et il n'existe pas de motif légitime impérieux pour le traitement » [1], si « les données à caractère personnel ont fait l'objet d'un traitement illicite » [1], si « les données à caractère personnel doivent être effacées pour respecter une obligation légale qui est prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis » [1], ou si « les données à caractère personnel ont été collectées dans le cadre de l'offre de services de la société de l'information visée à l'article 8, paragraphe 1 » [1]. En revanche, le droit à l'effacement ne s'applique pas si le traitement est nécessaire « à l'exercice du droit à la liberté d'expression et d'information » [1], « pour respecter une obligation légale qui requiert le traitement prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis, ou pour exécuter une mission d'intérêt public ou relevant de l'exercice de l'autorité publique dont est investi le responsable du traitement » [1], « pour des motifs d'intérêt public dans le domaine de la santé publique, conformément à l'article 9, paragraphe 2, points h) et i), ainsi qu'à l'article 9, paragraphe 3 » [1], « à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, dans la mesure où le droit visé au paragraphe 1 est susceptible de rendre impossible ou de compromettre gravement la réalisation des objectifs dudit traitement » [1], ou « à la constatation, à l'exercice ou à la défense de droits en justice » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit à l'effacement ; droit à l'oubli ; demande d'effacement ; données à caractère personnel

Temps : recherche 36.1 s · génération 4.1 s (3505 tokens lus, 1282 écrits, 450.8 tokens/s) · contrôle de pertinence 0.4 s · reformulation 0.3 s · attente des limites de l'API 32 s (non comptée)

## q12 — Un salarié demande une copie de toutes les données que nous avons sur lui : que dois-je lui donner ?

Article attendu : RGPD art. 15 — passage [1].

### Réponse du copilote

> Vous devez fournir au salarié une copie des données à caractère personnel le concernant, ainsi que la confirmation que ces données sont traitées [1]. En plus de la copie, vous devez lui communiquer les informations suivantes : « les finalités du traitement » [1], « les catégories de données à caractère personnel concernées » [1], « les destinataires ou catégories de destinataires auxquels les données à caractère personnel ont été ou seront communiquées, en particulier les destinataires qui sont établis dans des pays tiers ou les organisations internationales » [1], et « lorsque cela est possible, la durée de conservation des données à caractère personnel envisagée ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: »
  [1] « b) les catégories de données à caractère personnel concernées; »
  [1] « c) les destinataires ou catégories de destinataires auxquels les données à caractère personnel ont été ou seront communiquées, en particulier les destinataires qui sont établis dans des pays tiers ou les organisations internationales; »
  [1] « d) lorsque cela est possible, la durée de conservation des données à caractère personnel envisagée ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; »
  [1] « Le responsable du traitement fournit une copie des données à caractère personnel faisant l'objet d'un traitement. »

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
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1]) : ignoré(s).
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « les finalités du traitement ».

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: »
- [1] « a) les finalités du traitement; »
- [1] « b) les catégories de données à caractère personnel concernées; »
- [1] « c) les destinataires ou catégories de destinataires auxquels les données à caractère personnel ont été ou seront communiquées, en particulier les destinataires qui sont établis dans des pays tiers ou les organisations internationales; »
- [1] « d) lorsque cela est possible, la durée de conservation des données à caractère personnel envisagée ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; »
- [1] « Le responsable du traitement fournit une copie des données à caractère personnel faisant l'objet d'un traitement. »

RÉPONSE :
Vous devez fournir au salarié une copie des données à caractère personnel le concernant, ainsi que la confirmation que ces données sont traitées [1]. En plus de la copie, vous devez lui communiquer les informations suivantes : « les finalités du traitement » [1], « les catégories de données à caractère personnel concernées » [1], « les destinataires ou catégories de destinataires auxquels les données à caractère personnel ont été ou seront communiquées, en particulier les destinataires qui sont établis dans des pays tiers ou les organisations internationales » [1], et « lorsque cela est possible, la durée de conservation des données à caractère personnel envisagée ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit d'accès ; données à caractère personnel ; information relative au traitement ; copie des données

Temps : recherche 27.3 s · génération 1.2 s (3505 tokens lus, 374 écrits, 466.1 tokens/s) · contrôle de pertinence 0.3 s · reformulation 0.9 s · attente des limites de l'API 8 s (non comptée)

## q13 — Un adhérent veut récupérer ses données pour les donner à une autre association : est-ce un droit ?

Article attendu : RGPD art. 20 — passage [1].

### Réponse du copilote

> Oui, c'est un droit, appelé droit à la portabilité des données, prévu par le RGPD, article 20 [1].
> L'adhérent a le droit de transmettre ses données à un autre responsable du traitement, sans que l'association actuelle ne puisse s'y opposer [1].
> Ce droit s'applique si deux conditions sont remplies : le traitement doit être fondé sur le consentement ou sur un contrat, et il doit être effectué à l'aide de procédés automatisés [1].
> Si le traitement de l'association est nécessaire à l'exécution d'une mission d'intérêt public ou relevant de l'exercice de l'autorité publique, ce droit ne s'applique pas [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les personnes concernées ont le droit de recevoir les données à caractère personnel les concernant qu'elles ont fournies à un responsable du traitement, dans un format structuré, couramment utilisé et lisible par machine, et ont le droit de transmettre ces données à un autre responsable du traitement sans que le responsable du traitement auquel les données à caractère personnel ont été communiquées y fasse obstacle, lorsque: »
  [1] « a) le traitement est fondé sur le consentement en application de l'article 6, paragraphe 1, point a), ou de l'article 9, paragraphe 2, point a), ou sur un contrat en application de l'article 6, paragraphe 1, point b); et »
  [1] « b) le traitement est effectué à l'aide de procédés automatisés. »
  [1] « Ce droit ne s'applique pas au traitement nécessaire à l'exécution d'une mission d'intérêt public ou relevant de l'exercice de l'autorité publique dont est investi le responsable du traitement. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 20 : Droit à la portabilité des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_20
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [3] RGPD — règlement (UE) 2016/679, article 80 : Représentation des personnes concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_80
  [4] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les personnes concernées ont le droit de recevoir les données à caractère personnel les concernant qu'elles ont fournies à un responsable du traitement, dans un format structuré, couramment utilisé et lisible par machine, et ont le droit de transmettre ces données à un autre responsable du traitement sans que le responsable du traitement auquel les données à caractère personnel ont été communiquées y fasse obstacle, lorsque: »
- [1] « a) le traitement est fondé sur le consentement en application de l'article 6, paragraphe 1, point a), ou de l'article 9, paragraphe 2, point a), ou sur un contrat en application de l'article 6, paragraphe 1, point b); et »
- [1] « b) le traitement est effectué à l'aide de procédés automatisés. »
- [1] « Ce droit ne s'applique pas au traitement nécessaire à l'exécution d'une mission d'intérêt public ou relevant de l'exercice de l'autorité publique dont est investi le responsable du traitement. »

RÉPONSE :
Oui, c'est un droit, appelé droit à la portabilité des données, prévu par le RGPD, article 20 [1].
L'adhérent a le droit de transmettre ses données à un autre responsable du traitement, sans que l'association actuelle ne puisse s'y opposer [1].
Ce droit s'applique si deux conditions sont remplies : le traitement doit être fondé sur le consentement ou sur un contrat, et il doit être effectué à l'aide de procédés automatisés [1].
Si le traitement de l'association est nécessaire à l'exécution d'une mission d'intérêt public ou relevant de l'exercice de l'autorité publique, ce droit ne s'applique pas [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit à la portabilité des données ; données à caractère personnel ; destinataire ; transfert de données

Temps : recherche 30.0 s · génération 1.7 s (3145 tokens lus, 394 écrits, 405.6 tokens/s) · contrôle de pertinence 0.1 s · reformulation 0.7 s · attente des limites de l'API 6 s (non comptée)

## q14 — Puis-je envoyer une lettre d'information par e-mail à mes adhérents, et peuvent-ils refuser ?

Article attendu : RGPD art. 21 ou RGPD art. 6, paragraphe 1 — passage [1].

### Réponse du copilote

> Oui, vous pouvez envoyer une lettre d'information par e-mail à vos adhérents, mais cela dépend de la base légale que vous utilisez pour ce traitement. Si vous vous appuyez sur le consentement de vos adhérents, ils ont le droit de le retirer à tout moment [3]. Ce retrait doit être aussi simple que la procédure de consentement initial [3]. Si le traitement est fondé sur votre intérêt légitime (par exemple, l'information de vos membres), les adhérents ont le droit de s'opposer à tout moment au traitement de leurs données à des fins de prospection [1]. En cas d'opposition, vous ne devez plus traiter leurs données à ces fins [1]. Dans tous les cas, vous devez porter explicitement à leur attention ce droit d'opposition au plus tard au moment de la première communication, en le présentant clairement et séparément de toute autre information [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit de s'opposer à tout moment au traitement des données à caractère personnel la concernant à de telles fins de prospection, y compris au profilage dans la mesure où il est lié à une telle prospection. »
  [1] « Lorsque la personne concernée s'oppose au traitement à des fins de prospection, les données à caractère personnel ne sont plus traitées à ces fins. »
  [1] « Au plus tard au moment de la première communication avec la personne concernée, le droit visé aux paragraphes 1 et 2 est explicitement porté à l'attention de la personne concernée et est présenté clairement et séparément de toute autre information. »
  [3] « La personne concernée a le droit de retirer son consentement à tout moment. »
  [3] « Il est aussi simple de retirer que de donner son consentement. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 21 : Droit d'opposition (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_21
  [3] RGPD — règlement (UE) 2016/679, article 7 : Conditions applicables au consentement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_7
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [4] RGPD — règlement (UE) 2016/679, article 34 : Communication à la personne concernée d'une violation de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_34
  [5] RGPD — règlement (UE) 2016/679, article 80 : Représentation des personnes concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_80

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « La personne concernée a le droit de s'opposer à tout moment au traitement des données à caractère personnel la concernant à de telles fins de prospection, y compris au profilage dans la mesure où il est lié à une telle prospection. »
- [1] « Lorsque la personne concernée s'oppose au traitement à des fins de prospection, les données à caractère personnel ne sont plus traitées à ces fins. »
- [1] « Au plus tard au moment de la première communication avec la personne concernée, le droit visé aux paragraphes 1 et 2 est explicitement porté à l'attention de la personne concernée et est présenté clairement et séparément de toute autre information. »
- [3] « La personne concernée a le droit de retirer son consentement à tout moment. »
- [3] « Il est aussi simple de retirer que de donner son consentement. »

RÉPONSE :
Oui, vous pouvez envoyer une lettre d'information par e-mail à vos adhérents, mais cela dépend de la base légale que vous utilisez pour ce traitement. Si vous vous appuyez sur le consentement de vos adhérents, ils ont le droit de le retirer à tout moment [3]. Ce retrait doit être aussi simple que la procédure de consentement initial [3]. Si le traitement est fondé sur votre intérêt légitime (par exemple, l'information de vos membres), les adhérents ont le droit de s'opposer à tout moment au traitement de leurs données à des fins de prospection [1]. En cas d'opposition, vous ne devez plus traiter leurs données à ces fins [1]. Dans tous les cas, vous devez porter explicitement à leur attention ce droit d'opposition au plus tard au moment de la première communication, en le présentant clairement et séparément de toute autre information [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : consentement ; droit d'opposition ; traitement de données à caractère personnel ; communication électronique ; droit de retrait

Temps : recherche 30.3 s · génération 1.3 s (3273 tokens lus, 399 écrits, 462.6 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.2 s · attente des limites de l'API 6 s (non comptée)

## q15 — Mon prestataire informatique a accès à nos fichiers : faut-il signer un contrat particulier ?

Article attendu : RGPD art. 28, paragraphe 3 — passage [3].

### Réponse du copilote

> Oui, vous devez signer un contrat spécifique avec votre prestataire informatique, car il agit en tant que sous-traitant pour votre compte [2]. Ce contrat, exigé par le RGPD (article 28), doit définir l'objet, la durée, la nature et la finalité du traitement, ainsi que le type de données et les catégories de personnes concernées [3]. Il doit également prévoir que le sous-traitant ne traite les données que sur instruction documentée de votre part, veille à la confidentialité du personnel, prend les mesures de sécurité requises par l'article 32, et respecte les conditions pour recruter d'autres sous-traitants [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « Lorsqu'un traitement doit être effectué pour le compte d'un responsable du traitement, celui-ci fait uniquement appel à des sous-traitants qui présentent des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées de manière à ce que le traitement réponde aux exigences du présent règlement et garantisse la protection des droits de la personne concernée. »
  [3] « Le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre, qui lie le sous-traitant à l'égard du responsable du traitement, définit l'objet et la durée du traitement, la nature et la finalité du traitement, le type de données à caractère personnel et les catégories de personnes concernées, et les obligations et les droits du responsable du traitement. »
  [3] « Ce contrat ou cet autre acte juridique prévoit, notamment, que le sous-traitant: a) ne traite les données à caractère personnel que sur instruction documentée du responsable du traitement, y compris en ce qui concerne les transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale, à moins qu'il ne soit tenu d'y procéder en vertu du droit de l'Union ou du droit de l'État membre auquel le sous-traitant est soumis; dans ce cas, le sous-traitant informe le responsable du traitement de cette obligation juridique avant le traitement, sauf si le droit concerné interdit une telle information pour des motifs importants d'intérêt public; »
  [3] « b) veille à ce que les personnes autorisées à traiter les données à caractère personnel s'engagent à respecter la confidentialité ou soient soumises à une obligation légale appropriée de confidentialité; »
  [3] « c) prend toutes les mesures requises en vertu de l'article 32; »
  [3] « d) respecte les conditions visées aux paragraphes 2 et 4 pour recruter un autre sous-traitant; »

Sources citées :
  [2] RGPD — règlement (UE) 2016/679, article 28, paragraphe 1 : Sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [3] RGPD — règlement (UE) 2016/679, article 28, paragraphe 3 : Sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 28, paragraphe 4 : Sous-traitant
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [4] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30
  [5] RGPD — règlement (UE) 2016/679, article 27 : Représentants des responsables du traitement ou des sous-traitants qui ne sont pas établis dans l'Union
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_27

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [2] « Lorsqu'un traitement doit être effectué pour le compte d'un responsable du traitement, celui-ci fait uniquement appel à des sous-traitants qui présentent des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées de manière à ce que le traitement réponde aux exigences du présent règlement et garantisse la protection des droits de la personne concernée. »
- [3] « Le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre, qui lie le sous-traitant à l'égard du responsable du traitement, définit l'objet et la durée du traitement, la nature et la finalité du traitement, le type de données à caractère personnel et les catégories de personnes concernées, et les obligations et les droits du responsable du traitement. »
- [3] « Ce contrat ou cet autre acte juridique prévoit, notamment, que le sous-traitant: a) ne traite les données à caractère personnel que sur instruction documentée du responsable du traitement, y compris en ce qui concerne les transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale, à moins qu'il ne soit tenu d'y procéder en vertu du droit de l'Union ou du droit de l'État membre auquel le sous-traitant est soumis; dans ce cas, le sous-traitant informe le responsable du traitement de cette obligation juridique avant le traitement, sauf si le droit concerné interdit une telle information pour des motifs importants d'intérêt public; »
- [3] « b) veille à ce que les personnes autorisées à traiter les données à caractère personnel s'engagent à respecter la confidentialité ou soient soumises à une obligation légale appropriée de confidentialité; »
- [3] « c) prend toutes les mesures requises en vertu de l'article 32; »
- [3] « d) respecte les conditions visées aux paragraphes 2 et 4 pour recruter un autre sous-traitant; »

RÉPONSE :
Oui, vous devez signer un contrat spécifique avec votre prestataire informatique, car il agit en tant que sous-traitant pour votre compte [2]. Ce contrat, exigé par le RGPD (article 28), doit définir l'objet, la durée, la nature et la finalité du traitement, ainsi que le type de données et les catégories de personnes concernées [3]. Il doit également prévoir que le sous-traitant ne traite les données que sur instruction documentée de votre part, veille à la confidentialité du personnel, prend les mesures de sécurité requises par l'article 32, et respecte les conditions pour recruter d'autres sous-traitants [3].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : sous-traitant ; responsable du traitement ; contrat de sous-traitance ; mesures techniques et organisationnelles ; obligations contractuelles ; registre des activités de traitement

Temps : recherche 32.0 s · génération 4.4 s (3347 tokens lus, 583 écrits, 332.4 tokens/s) · contrôle de pertinence 2.8 s · reformulation 0.3 s · attente des limites de l'API 2 s (non comptée)

## q16 — Puis-je stocker les fichiers de mon association chez un hébergeur situé aux États-Unis ?

Article attendu : RGPD art. 44 ou RGPD art. 45, paragraphe 1 ou RGPD art. 46 — passage [1].

### Réponse du copilote

> Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, à condition de respecter les règles relatives aux transferts de données hors de l'Union européenne [5].
> Le stockage chez un hébergeur américain constitue un transfert de données vers un pays tiers, qui ne peut avoir lieu que si les conditions définies dans le chapitre du RGPD sont respectées par le responsable du traitement et le sous-traitant [5].
> Ce transfert est possible si la Commission européenne a constaté par voie de décision que le pays tiers assure un niveau de protection adéquat, auquel cas le transfert ne nécessite pas d'autorisation spécifique [4].
> À défaut de cette décision d'adéquation, le responsable du traitement ou le sous-traitant ne peut transférer les données que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives [1].
> Parmi ces garanties appropriées, figurent notamment les clauses types de protection des données adoptées par la Commission [1].
> Si ni la décision d'adéquation ni les garanties appropriées ne sont présentes, le transfert ne peut avoir lieu qu'à l'une des conditions spécifiques prévues pour des situations particulières, telles que le consentement explicite de la personne concernée ou la nécessité d'exécuter un contrat [2].
> Les passages trouvés ne permettent pas de confirmer si les États-Unis bénéficient actuellement d'une décision d'adéquation, car la liste des pays reconnus est publiée par la Commission européenne et ne figure pas dans les extraits fournis.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [5] « Un transfert, vers un pays tiers ou à une organisation internationale, de données à caractère personnel qui font ou sont destinées à faire l'objet d'un traitement après ce transfert ne peut avoir lieu que si, sous réserve des autres dispositions du présent règlement, les conditions définies dans le présent chapitre sont respectées par le responsable du traitement et le sous-traitant, y compris pour les transferts ultérieurs de données à caractère personnel au départ du pays tiers ou de l'organisation internationale vers un autre pays tiers ou à une autre organisation internationale. »
  [4] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. »
  [4] « Un tel transfert ne nécessite pas d'autorisation spécifique. »
  [1] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
  [1] « Les garanties appropriées visées au paragraphe 1 peuvent être fournies, sans que cela ne nécessite une autorisation particulière d'une autorité de contrôle, par: … c) des clauses types de protection des données adoptées par la Commission en conformité avec la procédure d'examen visée à l'article 93, paragraphe 2; … »
  [2] « En l'absence de décision d'adéquation en vertu de l'article 45, paragraphe 3, ou de garanties appropriées en vertu de l'article 46, y compris des règles d'entreprise contraignantes, un transfert ou un ensemble de transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale ne peut avoir lieu qu'à l'une des conditions suivantes: … »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 46 : Transferts moyennant des garanties appropriées (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_46
  [2] RGPD — règlement (UE) 2016/679, article 49, paragraphe 1 : Dérogations pour des situations particulières (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_49
  [4] RGPD — règlement (UE) 2016/679, article 45, paragraphe 1 : Transferts fondés sur une décision d'adéquation (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
  [5] RGPD — règlement (UE) 2016/679, article 44 : Principe général applicable aux transferts (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_44
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 45, paragraphe 2 : Transferts fondés sur une décision d'adéquation
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
Note : La liste des pays bénéficiant d'une décision d'adéquation n'est pas dans les textes utilisés par le copilote : consultez la page de la Commission européenne sur les décisions d'adéquation (en anglais) : https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [5] « Un transfert, vers un pays tiers ou à une organisation internationale, de données à caractère personnel qui font ou sont destinées à faire l'objet d'un traitement après ce transfert ne peut avoir lieu que si, sous réserve des autres dispositions du présent règlement, les conditions définies dans le présent chapitre sont respectées par le responsable du traitement et le sous-traitant, y compris pour les transferts ultérieurs de données à caractère personnel au départ du pays tiers ou de l'organisation internationale vers un autre pays tiers ou à une autre organisation internationale. »
- [4] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. »
- [4] « Un tel transfert ne nécessite pas d'autorisation spécifique. »
- [1] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
- [1] « Les garanties appropriées visées au paragraphe 1 peuvent être fournies, sans que cela ne nécessite une autorisation particulière d'une autorité de contrôle, par: … c) des clauses types de protection des données adoptées par la Commission en conformité avec la procédure d'examen visée à l'article 93, paragraphe 2; … »
- [2] « En l'absence de décision d'adéquation en vertu de l'article 45, paragraphe 3, ou de garanties appropriées en vertu de l'article 46, y compris des règles d'entreprise contraignantes, un transfert ou un ensemble de transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale ne peut avoir lieu qu'à l'une des conditions suivantes: … »

RÉPONSE :
Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, à condition de respecter les règles relatives aux transferts de données hors de l'Union européenne [5].
Le stockage chez un hébergeur américain constitue un transfert de données vers un pays tiers, qui ne peut avoir lieu que si les conditions définies dans le chapitre du RGPD sont respectées par le responsable du traitement et le sous-traitant [5].
Ce transfert est possible si la Commission européenne a constaté par voie de décision que le pays tiers assure un niveau de protection adéquat, auquel cas le transfert ne nécessite pas d'autorisation spécifique [4].
À défaut de cette décision d'adéquation, le responsable du traitement ou le sous-traitant ne peut transférer les données que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives [1].
Parmi ces garanties appropriées, figurent notamment les clauses types de protection des données adoptées par la Commission [1].
Si ni la décision d'adéquation ni les garanties appropriées ne sont présentes, le transfert ne peut avoir lieu qu'à l'une des conditions spécifiques prévues pour des situations particulières, telles que le consentement explicite de la personne concernée ou la nécessité d'exécuter un contrat [2].
Les passages trouvés ne permettent pas de confirmer si les États-Unis bénéficient actuellement d'une décision d'adéquation, car la liste des pays reconnus est publiée par la Commission européenne et ne figure pas dans les extraits fournis.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : transfert de données vers un pays tiers ; pays tiers ; mesures de sauvegarde ; protection des données à caractère personnel ; hébergeur ; données personnelles

Temps : recherche 30.2 s · génération 2.8 s (3313 tokens lus, 819 écrits, 452.9 tokens/s) · contrôle de pertinence 0.7 s · reformulation 0.8 s · attente des limites de l'API 49 s (non comptée)

## q17 — Quelles sanctions risque une petite entreprise qui ne respecte pas le RGPD ?

Article attendu : RGPD art. 83, paragraphe 4 ou RGPD art. 83, paragraphe 5 — passage [1].

### Réponse du copilote

> Une petite entreprise qui ne respecte pas le RGPD risque des amendes administratives dont le montant dépend de la nature de la violation. Pour certaines violations, comme celles relatives aux principes de base du traitement ou aux droits des personnes concernées, les amendes peuvent s'élever jusqu'à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [1]. Pour d'autres violations, notamment celles liées aux obligations du responsable du traitement et du sous-traitant, les amendes peuvent s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [3]. Ces amendes doivent être effectives, proportionnées et dissuasives [2]. En outre, les États membres déterminent le régime des autres sanctions applicables en cas de violations du présent règlement, en particulier pour les violations qui ne font pas l'objet des amendes administratives prévues à l'article 83 [4]. Ces sanctions sont également effectives, proportionnées et dissuasives [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »
  [3] « Les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 83, paragraphe 5 : Conditions générales pour imposer des amendes administratives (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83
  [2] RGPD — règlement (UE) 2016/679, article 83, paragraphe 1 : Conditions générales pour imposer des amendes administratives (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83
  [3] RGPD — règlement (UE) 2016/679, article 83, paragraphe 4 : Conditions générales pour imposer des amendes administratives (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83
  [4] RGPD — règlement (UE) 2016/679, article 84 : Sanctions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_84
Passages consultés mais non cités :
  [5] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 1 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
Attention : 3 extrait(s) introuvable(s) mot pour mot dans le passage cité ([2], [4], [4]) : ignoré(s).
Attention : La réponse cite [2], [4] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »
- [3] « Les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »
- [2] « Chaque autorite de contrôle veille à ce que les amendes adminstratives imposes en vertu du présent article pour des violations du présent règlement vises au paragraphe 4, 5 et 6 soient, dans chaque cas, effectives, proportionnes et dssuatives. »*
- [4] 「Les États membres déterminent le régime des autres sanctions applicables en cas de violations du présent règlement, en particulier pour les violations qui ne font pas l'objet des amendes administratives prévues à l'article 83, et prennent toutes les mesures nécessaires pour garantir leur mise en œuvre.」
- [4] 「Ces sanctions sont effectives, proportionnées et dissuasives.」

RÉPONSE :
Une petite entreprise qui ne respecte pas le RGPD risque des amendes administratives dont le montant dépend de la nature de la violation. Pour certaines violations, comme celles relatives aux principes de base du traitement ou aux droits des personnes concernées, les amendes peuvent s'élever jusqu'à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [1]. Pour d'autres violations, notamment celles liées aux obligations du responsable du traitement et du sous-traitant, les amendes peuvent s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [3]. Ces amendes doivent être effectives, proportionnées et dissuasives [2]. En outre, les États membres déterminent le régime des autres sanctions applicables en cas de violations du présent règlement, en particulier pour les violations qui ne font pas l'objet des amendes administratives prévues à l'article 83 [4]. Ces sanctions sont également effectives, proportionnées et dissuasives [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : amende administrative ; amende forfaitaire ; amende maximale ; amende proportionnée ; amende effective ; amende dissuasive

Temps : recherche 27.4 s · génération 1.8 s (2135 tokens lus, 607 écrits, 452.1 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.4 s · attente des limites de l'API 12 s (non comptée)

## q18 — Notre association peut-elle collecter des informations sur la santé de ses bénévoles ?

Article attendu : RGPD art. 9, paragraphe 1 ou RGPD art. 9, paragraphe 2 — passage [1].

### Réponse du copilote

> Oui, votre association peut collecter des informations sur la santé de ses bénévoles, mais uniquement si l'une des conditions d'exception prévues par le RGPD est remplie [1].
> La première possibilité est que la personne concernée ait donné son « consentement explicite au traitement de ces données à caractère personnel pour une ou plusieurs finalités spécifiques » [1].
> La deuxième possibilité concerne les associations à but non lucratif : le traitement est autorisé s'il est effectué « dans le cadre de leurs activités légitimes et moyennant les garanties appropriées » et s'il se rapporte « exclusivement aux membres ou aux anciens membres dudit organisme ou aux personnes entretenant avec celui-ci des contacts réguliers en liaison avec ses finalités » [1].
> Dans ce cas, il est impératif que « les données à caractère personnel ne soient pas communiquées en dehors de cet organisme sans le consentement des personnes concernées » [1].
> Une autre exception existe si le traitement est « nécessaire aux fins de la médecine préventive ou de la médecine du travail... sur la base du droit de l'Union, du droit d'un État membre ou en vertu d'un contrat conclu avec un professionnel de la santé » [1].
> En tant que responsable du traitement, vous devez informer les bénévoles des « finalités du traitement... ainsi que la base juridique du traitement » [4].
> Vous devez également leur communiquer « la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée » [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le paragraphe 1 ne s'applique pas si l'une des conditions suivantes est remplie: »
  [1] « a) la personne concernée a donné son consentement explicite au traitement de ces données à caractère personnel pour une ou plusieurs finalités spécifiques, sauf lorsque le droit de l'Union ou le droit de l'État membre prévoit que l'interdiction visée au paragraphe 1 ne peut pas être levée par la personne concernée; »
  [1] « d) le traitement est effectué, dans le cadre de leurs activités légitimes et moyennant les garanties appropriées, par une fondation, une association ou tout autre organisme à but non lucratif et poursuivant une finalité politique, philosophique, religieuse ou syndicale, à condition que ledit traitement se rapporte exclusivement aux membres ou aux anciens membres dudit organisme ou aux personnes entretenant avec celui-ci des contacts réguliers en liaison avec ses finalités et que les données à caractère personnel ne soient pas communiquées en dehors de cet organisme sans le consentement des personnes concernées; »
  [1] « h) le traitement est nécessaire aux fins de la médecine préventive ou de la médecine du travail, de l'appréciation de la capacité de travail du travailleur, de diagnostics médicaux, de la prise en charge sanitaire ou sociale, ou de la gestion des systèmes et des services de soins de santé ou de protection sociale sur la base du droit de l'Union, du droit d'un État membre ou en vertu d'un contrat conclu avec un professionnel de la santé et soumis aux conditions et garanties visées au paragraphe 3; »
  [4] « c) les finalités du traitement auquel sont destinées les données à caractère personnel ainsi que la base juridique du traitement; »
  [4] « a) la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 9, paragraphe 2, points a) à i) : Traitement portant sur des catégories particulières de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
  [4] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [3] RGPD — règlement (UE) 2016/679, article 40, paragraphe 1 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [5] RGPD — règlement (UE) 2016/679, article 6, paragraphe 4 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
Attention : La réponse ne reprend que 7 des 9 cas énumérés au passage [1], sans dire qu'elle n'en cite qu'une partie. Vérifiez la liste complète.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le paragraphe 1 ne s'applique pas si l'une des conditions suivantes est remplie: »
- [1] « a) la personne concernée a donné son consentement explicite au traitement de ces données à caractère personnel pour une ou plusieurs finalités spécifiques, sauf lorsque le droit de l'Union ou le droit de l'État membre prévoit que l'interdiction visée au paragraphe 1 ne peut pas être levée par la personne concernée; »
- [1] « d) le traitement est effectué, dans le cadre de leurs activités légitimes et moyennant les garanties appropriées, par une fondation, une association ou tout autre organisme à but non lucratif et poursuivant une finalité politique, philosophique, religieuse ou syndicale, à condition que ledit traitement se rapporte exclusivement aux membres ou aux anciens membres dudit organisme ou aux personnes entretenant avec celui-ci des contacts réguliers en liaison avec ses finalités et que les données à caractère personnel ne soient pas communiquées en dehors de cet organisme sans le consentement des personnes concernées; »
- [1] « h) le traitement est nécessaire aux fins de la médecine préventive ou de la médecine du travail, de l'appréciation de la capacité de travail du travailleur, de diagnostics médicaux, de la prise en charge sanitaire ou sociale, ou de la gestion des systèmes et des services de soins de santé ou de protection sociale sur la base du droit de l'Union, du droit d'un État membre ou en vertu d'un contrat conclu avec un professionnel de la santé et soumis aux conditions et garanties visées au paragraphe 3; »
- [4] « c) les finalités du traitement auquel sont destinées les données à caractère personnel ainsi que la base juridique du traitement; »
- [4] « a) la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; »

RÉPONSE :
Oui, votre association peut collecter des informations sur la santé de ses bénévoles, mais uniquement si l'une des conditions d'exception prévues par le RGPD est remplie [1].
La première possibilité est que la personne concernée ait donné son « consentement explicite au traitement de ces données à caractère personnel pour une ou plusieurs finalités spécifiques » [1].
La deuxième possibilité concerne les associations à but non lucratif : le traitement est autorisé s'il est effectué « dans le cadre de leurs activités légitimes et moyennant les garanties appropriées » et s'il se rapporte « exclusivement aux membres ou aux anciens membres dudit organisme ou aux personnes entretenant avec celui-ci des contacts réguliers en liaison avec ses finalités » [1].
Dans ce cas, il est impératif que « les données à caractère personnel ne soient pas communiquées en dehors de cet organisme sans le consentement des personnes concernées » [1].
Une autre exception existe si le traitement est « nécessaire aux fins de la médecine préventive ou de la médecine du travail... sur la base du droit de l'Union, du droit d'un État membre ou en vertu d'un contrat conclu avec un professionnel de la santé » [1].
En tant que responsable du traitement, vous devez informer les bénévoles des « finalités du traitement... ainsi que la base juridique du traitement » [4].
Vous devez également leur communiquer « la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée » [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données de santé ; données à caractère personnel ; responsable du traitement ; consentement ; minimisation des données

Temps : recherche 26.0 s · génération 2.0 s (3600 tokens lus, 742 écrits, 491.8 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.4 s · attente des limites de l'API 18 s (non comptée)

## q19 — Qu'est-ce qu'une donnée personnelle ?

Article attendu : RGPD art. 4, définition 1 — passage [1].

### Réponse du copilote

> Une donnée à caractère personnel est définie comme « toute information se rapportant à une personne physique identifiée ou identifiable » [1]. Cette définition inclut les informations permettant d'identifier une personne « directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « «données à caractère personnel», toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée»); »
  [1] « est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale; »

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
- [1] « «données à caractère personnel», toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée»); »
- [1] « est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale; »

RÉPONSE :
Une donnée à caractère personnel est définie comme « toute information se rapportant à une personne physique identifiée ou identifiable » [1]. Cette définition inclut les informations permettant d'identifier une personne « directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : donnée à caractère personnel

Temps : recherche 28.7 s · génération 0.9 s (2891 tokens lus, 252 écrits, 491.1 tokens/s) · contrôle de pertinence 0.4 s · reformulation 0.3 s · attente des limites de l'API 20 s (non comptée)

## q20 — À partir de quel âge un enfant peut-il s'inscrire seul à notre service en ligne ?

Article attendu : RGPD art. 8 — passage [1].

### Réponse du copilote

> En principe, un enfant peut s'inscrire seul à votre service en ligne à partir de 16 ans [1]. En dessous de cet âge, l'inscription n'est licite que si le consentement est donné ou autorisé par le titulaire de la responsabilité parentale [1]. Toutefois, les États membres peuvent prévoir par la loi un âge inférieur pour ces finalités, pour autant que cet âge inférieur ne soit pas en-dessous de 13 ans [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « le traitement des données à caractère personnel relatives à un enfant est licite lorsque l'enfant est âgé d'au moins 16 ans. »
  [1] « Lorsque l'enfant est âgé de moins de 16 ans, ce traitement n'est licite que si, et dans la mesure où, le consentement est donné ou autorisé par le titulaire de la responsabilité parentale à l'égard de l'enfant. »
  [1] « Les États membres peuvent prévoir par la loi un âge inférieur pour ces finalités pour autant que cet âge inférieur ne soit pas en-dessous de 13 ans. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 8 : Conditions applicables au consentement des enfants en ce qui concerne les services de la société de l'information (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_8
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 7 : Conditions applicables au consentement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_7
  [3] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [4] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [5] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « le traitement des données à caractère personnel relatives à un enfant est licite lorsque l'enfant est âgé d'au moins 16 ans. »
- [1] « Lorsque l'enfant est âgé de moins de 16 ans, ce traitement n'est licite que si, et dans la mesure où, le consentement est donné ou autorisé par le titulaire de la responsabilité parentale à l'égard de l'enfant. »
- [1] « Les États membres peuvent prévoir par la loi un âge inférieur pour ces finalités pour autant que cet âge inférieur ne soit pas en-dessous de 13 ans. »

RÉPONSE :
En principe, un enfant peut s'inscrire seul à votre service en ligne à partir de 16 ans [1]. En dessous de cet âge, l'inscription n'est licite que si le consentement est donné ou autorisé par le titulaire de la responsabilité parentale [1]. Toutefois, les États membres peuvent prévoir par la loi un âge inférieur pour ces finalités, pour autant que cet âge inférieur ne soit pas en-dessous de 13 ans [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : consentement parental ; âge de la responsabilité numérique ; consentement de l'enfant ; données à caractère personnel des mineurs

Temps : recherche 24.4 s · génération 0.9 s (3391 tokens lus, 244 écrits, 506.7 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.3 s · attente des limites de l'API 2 s (non comptée)

## q21 — Comment dois-je protéger les données personnelles que nous conservons ?

Article attendu : RGPD art. 32 — passage [1].

### Réponse du copilote

> Pour protéger les données personnelles que vous conservez, vous devez, en tant que responsable du traitement, mettre en œuvre des mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque [1]. Ces mesures incluent, selon les besoins, la pseudonymisation et le chiffrement des données à caractère personnel [1]. Vous devez également disposer de moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement [1]. Il est nécessaire de prévoir des moyens permettant de rétablir la disponibilité des données et l'accès à celles-ci dans des délais appropriés en cas d'incident physique ou technique [1]. Enfin, vous devez instaurer une procédure visant à tester, à analyser et à évaluer régulièrement l'efficacité de ces mesures [1]. Concernant la conservation, les données doivent être conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « le responsable du traitement et le sous-traitant mettent en œuvre les mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque, y compris entre autres, selon les besoins: »
  [1] « a) la pseudonymisation et le chiffrement des données à caractère personnel; »
  [1] « b) des moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement; »
  [1] « c) des moyens permettant de rétablir la disponibilité des données à caractère personnel et l'accès à celles-ci dans des délais appropriés en cas d'incident physique ou technique; »
  [1] « d) une procédure visant à tester, à analyser et à évaluer régulièrement l'efficacité des mesures techniques et organisationnelles pour assurer la sécurité du traitement. »
  [3] « conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 32 : Sécurité du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_32
  [3] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 25 : Protection des données dès la conception et protection des données par défaut
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_25
  [4] RGPD — règlement (UE) 2016/679, article 24 : Responsabilité du responsable du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_24
  [5] RGPD — règlement (UE) 2016/679, article 45, paragraphe 2 : Transferts fondés sur une décision d'adéquation
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « le responsable du traitement et le sous-traitant mettent en œuvre les mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque, y compris entre autres, selon les besoins: »
- [1] « a) la pseudonymisation et le chiffrement des données à caractère personnel; »
- [1] « b) des moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement; »
- [1] « c) des moyens permettant de rétablir la disponibilité des données à caractère personnel et l'accès à celles-ci dans des délais appropriés en cas d'incident physique ou technique; »
- [1] « d) une procédure visant à tester, à analyser et à évaluer régulièrement l'efficacité des mesures techniques et organisationnelles pour assurer la sécurité du traitement. »
- [3] « conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées; »

RÉPONSE :
Pour protéger les données personnelles que vous conservez, vous devez, en tant que responsable du traitement, mettre en œuvre des mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque [1]. Ces mesures incluent, selon les besoins, la pseudonymisation et le chiffrement des données à caractère personnel [1]. Vous devez également disposer de moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement [1]. Il est nécessaire de prévoir des moyens permettant de rétablir la disponibilité des données et l'accès à celles-ci dans des délais appropriés en cas d'incident physique ou technique [1]. Enfin, vous devez instaurer une procédure visant à tester, à analyser et à évaluer régulièrement l'efficacité de ces mesures [1]. Concernant la conservation, les données doivent être conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées [3].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : mesures techniques et organisationnelles appropriées ; sécurité des données à caractère personnel ; protection des données ; confidentialité ; intégrité ; disponibilité

Temps : recherche 26.0 s · génération 1.5 s (3210 tokens lus, 469 écrits, 454.3 tokens/s) · contrôle de pertinence 0.5 s · reformulation 0.3 s

## q22 — Le consentement d'une personne doit-il être donné par écrit ?

Article attendu : RGPD art. 7 — passage [1].

### Réponse du copilote

> Non, le consentement ne doit pas obligatoirement être donné par écrit. Il s'agit d'une « manifestation de volonté, libre, spécifique, éclairée et univoque » acceptée « par une déclaration ou par un acte positif clair » [2]. L'écrit n'est mentionné que comme un cas possible (« Si le consentement... est donné dans le cadre d'une déclaration écrite »), auquel cas il doit être distingué clairement des autres questions [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « «consentement» de la personne concernée, toute manifestation de volonté, libre, spécifique, éclairée et univoque par laquelle la personne concernée accepte, par une déclaration ou par un acte positif clair, que des données à caractère personnel la concernant fassent l'objet d'un traitement; »
  [1] « Si le consentement de la personne concernée est donné dans le cadre d'une déclaration écrite qui concerne également d'autres questions, la demande de consentement est présentée sous une forme qui la distingue clairement de ces autres questions, sous une forme compréhensible et aisément accessible, et formulée en des termes clairs et simples. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 7 : Conditions applicables au consentement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_7
  [2] RGPD — règlement (UE) 2016/679, article 4, définition 11 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [4] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [5] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
Attention : La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Non, le consentement ne doit pas obligatoirement être donné par écrit. ». Vérifiez ce point.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [2] « «consentement» de la personne concernée, toute manifestation de volonté, libre, spécifique, éclairée et univoque par laquelle la personne concernée accepte, par une déclaration ou par un acte positif clair, que des données à caractère personnel la concernant fassent l'objet d'un traitement; »
- [1] « Si le consentement de la personne concernée est donné dans le cadre d'une déclaration écrite qui concerne également d'autres questions, la demande de consentement est présentée sous une forme qui la distingue clairement de ces autres questions, sous une forme compréhensible et aisément accessible, et formulée en des termes clairs et simples. »

RÉPONSE :
Non, le consentement ne doit pas obligatoirement être donné par écrit. Il s'agit d'une « manifestation de volonté, libre, spécifique, éclairée et univoque » acceptée « par une déclaration ou par un acte positif clair » [2]. L'écrit n'est mentionné que comme un cas possible (« Si le consentement... est donné dans le cadre d'une déclaration écrite »), auquel cas il doit être distingué clairement des autres questions [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : consentement explicite ; consentement libre ; consentement spécifique ; consentement informé ; consentement par écrit ; consentement par déclaration

Temps : recherche 22.5 s · génération 1.3 s (2538 tokens lus, 248 écrits, 450.8 tokens/s) · contrôle de pertinence 0.8 s · reformulation 0.2 s · attente des limites de l'API 8 s (non comptée)

## q23 — Quelles utilisations de l'intelligence artificielle sont interdites en Europe ?

Article attendu : AI Act art. 5, paragraphe 1 — passage [1].

### Réponse du copilote

> L’AI Act interdit plusieurs pratiques spécifiques en matière d’intelligence artificielle [1].
> Sont notamment interdits les systèmes utilisant des techniques subliminales ou manipulatrices pour altérer le comportement d’une personne et causer un préjudice important [1].
> L’exploitation de vulnérabilités liées à l’âge, au handicap ou à la situation sociale ou économique est également interdite si elle altère le comportement et cause un préjudice [1].
> La génération ou la manipulation de contenus réalistes représentant des parties intimes ou des activités sexuellement explicites sans consentement explicite est interdite [1].
> L’évaluation ou la classification de personnes par « note sociale » (social scoring) est interdite lorsqu’elle conduit à un traitement préjudiciable ou disproportionné [1].
> L’inférence des émotions sur le lieu de travail et dans les établissements d’enseignement est interdite, « sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité » [2].
> L’identification biométrique à distance en temps réel dans des espaces publics à des fins répressives est interdite, « sauf si et dans la mesure où cette utilisation est strictement nécessaire » pour des objectifs précis comme la recherche de victimes d’enlèvement ou la prévention de menaces terroristes [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « a) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui a recours à des techniques subliminales, au-dessous du seuil de conscience d’une personne, ou à des techniques délibérément manipulatrices ou trompeuses, avec pour objectif ou effet d’altérer substantiellement le comportement d’une personne ou d’un groupe de personnes en portant considérablement atteinte à leur capacité à prendre une décision éclairée, amenant ainsi la personne à prendre une décision qu’elle n’aurait pas prise autrement, d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne, à une autre personne ou à un groupe de personnes; »
  [1] « b) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui exploite les éventuelles vulnérabilités dues à l’âge, au handicap ou à la situation sociale ou économique spécifique d’une personne physique ou d’un groupe de personnes donné avec pour objectif ou effet d’altérer substantiellement le comportement de cette personne ou d’un membre de ce groupe d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne ou à un tiers; »
  [1] « b bis) la mise sur le marché, la mise en service ou l'utilisation d'un système d'IA qui génère ou manipule des images, des vidéos, des contenus audio ou tout autre matériel similaire réalistes représentant les parties intimes d'une personne identifiable, ou une personne identifiable se livrant à des activités sexuellement explicites, sans le consentement libre, spécifique, éclairé, univoque et explicite de cette personne pour cette production ou manipulation; »
  [1] « c) la mise sur le marché, la mise en service ou l’utilisation de systèmes d’IA pour l’évaluation ou la classification de personnes physiques ou de groupes de personnes au cours d’une période donnée en fonction de leur comportement social ou de caractéristiques personnelles ou de personnalité connues, déduites ou prédites, la note sociale conduisant à l’une ou l’autre des situations suivantes, ou aux deux: »
  [2] « f) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement, sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité; »
  [2] « h) l’utilisation de systèmes d’identification biométrique à distance en temps réel dans des espaces accessibles au public à des fins répressives, sauf si et dans la mesure où cette utilisation est strictement nécessaire eu égard à l’un des objectifs suivants: »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points a) à e) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [2] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points f) à h) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, article 1 : Objet
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_1
  [4] AI Act — règlement (UE) 2024/1689, article 6, paragraphe 5 : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
  [5] AI Act — règlement (UE) 2024/1689, article 6, paragraphe 1 : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « a) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui a recours à des techniques subliminales, au-dessous du seuil de conscience d’une personne, ou à des techniques délibérément manipulatrices ou trompeuses, avec pour objectif ou effet d’altérer substantiellement le comportement d’une personne ou d’un groupe de personnes en portant considérablement atteinte à leur capacité à prendre une décision éclairée, amenant ainsi la personne à prendre une décision qu’elle n’aurait pas prise autrement, d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne, à une autre personne ou à un groupe de personnes; »
- [1] « b) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui exploite les éventuelles vulnérabilités dues à l’âge, au handicap ou à la situation sociale ou économique spécifique d’une personne physique ou d’un groupe de personnes donné avec pour objectif ou effet d’altérer substantiellement le comportement de cette personne ou d’un membre de ce groupe d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne ou à un tiers; »
- [1] « b bis) la mise sur le marché, la mise en service ou l'utilisation d'un système d'IA qui génère ou manipule des images, des vidéos, des contenus audio ou tout autre matériel similaire réalistes représentant les parties intimes d'une personne identifiable, ou une personne identifiable se livrant à des activités sexuellement explicites, sans le consentement libre, spécifique, éclairé, univoque et explicite de cette personne pour cette production ou manipulation; »
- [1] « c) la mise sur le marché, la mise en service ou l’utilisation de systèmes d’IA pour l’évaluation ou la classification de personnes physiques ou de groupes de personnes au cours d’une période donnée en fonction de leur comportement social ou de caractéristiques personnelles ou de personnalité connues, déduites ou prédites, la note sociale conduisant à l’une ou l’autre des situations suivantes, ou aux deux: »
- [2] « f) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement, sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité; »
- [2] « h) l’utilisation de systèmes d’identification biométrique à distance en temps réel dans des espaces accessibles au public à des fins répressives, sauf si et dans la mesure où cette utilisation est strictement nécessaire eu égard à l’un des objectifs suivants: »

RÉPONSE :
L’AI Act interdit plusieurs pratiques spécifiques en matière d’intelligence artificielle [1].
Sont notamment interdits les systèmes utilisant des techniques subliminales ou manipulatrices pour altérer le comportement d’une personne et causer un préjudice important [1].
L’exploitation de vulnérabilités liées à l’âge, au handicap ou à la situation sociale ou économique est également interdite si elle altère le comportement et cause un préjudice [1].
La génération ou la manipulation de contenus réalistes représentant des parties intimes ou des activités sexuellement explicites sans consentement explicite est interdite [1].
L’évaluation ou la classification de personnes par « note sociale » (social scoring) est interdite lorsqu’elle conduit à un traitement préjudiciable ou disproportionné [1].
L’inférence des émotions sur le lieu de travail et dans les établissements d’enseignement est interdite, « sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité » [2].
L’identification biométrique à distance en temps réel dans des espaces publics à des fins répressives est interdite, « sauf si et dans la mesure où cette utilisation est strictement nécessaire » pour des objectifs précis comme la recherche de victimes d’enlèvement ou la prévention de menaces terroristes [2].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : systèmes de scoring social ; manipulation subliminale ; exploitation de vulnérabilités ; reconnaissance faciale en temps réel dans l'espace public

Temps : recherche 28.6 s · génération 2.8 s (3334 tokens lus, 924 écrits, 453.2 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.4 s · attente des limites de l'API 8 s (non comptée)

## q24 — Ai-je le droit d'utiliser une IA qui analyse les émotions de mes salariés ?

Article attendu : AI Act art. 5, paragraphe 1_f h — passage [2].

### Réponse du copilote

> Non, vous n'avez pas le droit d'utiliser une IA qui analyse les émotions de vos salariés, car l'AI Act interdit « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement » [2]. Cette interdiction comporte une exception « sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité » [2]. Si votre usage ne relève pas de ces raisons médicales ou de sécurité, l'utilisation est interdite. Si, dans un cas hypothétique où l'usage serait autorisé (par exemple pour la sécurité), vous auriez l'obligation d'informer les personnes exposées du fonctionnement du système et de traiter les données conformément au RGPD [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « f) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement, sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité; »
  [1] « c) systèmes d'IA destinés à être utilisés pour la reconnaissance des émotions. »
  [4] « Les déployeurs d’un système de reconnaissance des émotions ou d’un système de catégorisation biométrique informent les personnes physiques qui y sont exposées du fonctionnement du système et traitent les données à caractère personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680, selon le cas. »
  [4] « Cette obligation ne s’applique pas aux systèmes d’IA utilisés pour la catégorisation biométrique et la reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l’Union. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, annexe III, point 1 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [2] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points f) à h) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [4] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 3 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, article 86 : Droit à l’explication des décisions individuelles
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_86
  [5] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [2] « f) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement, sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité; »
- [1] « c) systèmes d'IA destinés à être utilisés pour la reconnaissance des émotions. »
- [4] « Les déployeurs d’un système de reconnaissance des émotions ou d’un système de catégorisation biométrique informent les personnes physiques qui y sont exposées du fonctionnement du système et traitent les données à caractère personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680, selon le cas. »
- [4] « Cette obligation ne s’applique pas aux systèmes d’IA utilisés pour la catégorisation biométrique et la reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l’Union. »

RÉPONSE :
Non, vous n'avez pas le droit d'utiliser une IA qui analyse les émotions de vos salariés, car l'AI Act interdit « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement » [2]. Cette interdiction comporte une exception « sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité » [2]. Si votre usage ne relève pas de ces raisons médicales ou de sécurité, l'utilisation est interdite. Si, dans un cas hypothétique où l'usage serait autorisé (par exemple pour la sécurité), vous auriez l'obligation d'informer les personnes exposées du fonctionnement du système et de traiter les données conformément au RGPD [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données biométriques ; inférence sur l'état émotionnel ; système d'IA à haut risque ; traitement de données à caractère personnel ; consentement ; profilage

Temps : recherche 31.5 s · génération 2.3 s (2707 tokens lus, 503 écrits, 480.9 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.2 s · attente des limites de l'API 39 s (non comptée)

## q25 — Mon logiciel est-il un « système d'IA » au sens de la loi européenne ?

Article attendu : AI Act art. 3, définition 1 — passage [1].

### Réponse du copilote

> Pour déterminer si votre logiciel est un « système d'IA », il doit correspondre à la définition légale qui exige qu'il s'agisse d'un « système automatisé » conçu pour fonctionner à différents niveaux d'autonomie et capable de s'adapter après son déploiement [1]. De plus, le logiciel doit déduire, à partir des entrées reçues, la manière de générer des sorties comme des prédictions, du contenu, des recommandations ou des décisions, et ces sorties doivent pouvoir influencer des environnements physiques ou virtuels [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « 1) «système d’IA», un système automatisé qui est conçu pour fonctionner à différents niveaux d’autonomie et peut faire preuve d’une capacité d’adaptation après son déploiement, et qui, pour des objectifs explicites ou implicites, déduit, à partir des entrées qu’il reçoit, la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels; »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 3, définition 1 : Définitions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, annexe III, point 8 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [3] AI Act — règlement (UE) 2024/1689, article 6, paragraphe 1 : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
  [4] AI Act — règlement (UE) 2024/1689, annexe III, point 1 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [5] AI Act — règlement (UE) 2024/1689, article 6, paragraphe 1 bis : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « 1) «système d’IA», un système automatisé qui est conçu pour fonctionner à différents niveaux d’autonomie et peut faire preuve d’une capacité d’adaptation après son déploiement, et qui, pour des objectifs explicites ou implicites, déduit, à partir des entrées qu’il reçoit, la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels; »

RÉPONSE :
Pour déterminer si votre logiciel est un « système d'IA », il doit correspondre à la définition légale qui exige qu'il s'agisse d'un « système automatisé » conçu pour fonctionner à différents niveaux d'autonomie et capable de s'adapter après son déploiement [1]. De plus, le logiciel doit déduire, à partir des entrées reçues, la manière de générer des sorties comme des prédictions, du contenu, des recommandations ou des décisions, et ces sorties doivent pouvoir influencer des environnements physiques ou virtuels [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : système d'IA ; système d'intelligence artificielle ; système autonome ; système d'IA à risque élevé

Temps : recherche 30.9 s · génération 0.8 s (2179 tokens lus, 231 écrits, 517.0 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.8 s · attente des limites de l'API 7 s (non comptée)

## q26 — Dois-je indiquer qu'une image publiée sur notre site a été créée par une IA ?

Article attendu : AI Act art. 50, paragraphe 4 — passage [1].

### Réponse du copilote

> Oui, vous devez indiquer que l'image a été créée par une IA si elle constitue un « hypertrucage », c'est-à-dire une image « présentant une ressemblance avec des personnes, des objets, des lieux, des entités ou événements existants et pouvant être perçu à tort par une personne comme authentiques ou véridiques » [4]. En tant que déployeur du système d'IA, vous « indiquez que les contenus ont été générés ou manipulés par une IA » [1]. Cette obligation ne s'applique pas « lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière » [1]. Si l'image fait partie d’une œuvre « manifestement artistique, créatif, satirique, fictif ou analogue », l'obligation se limite « à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. »
  [1] « Cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. »
  [1] « Lorsque le contenu fait partie d’une œuvre ou d’un programme manifestement artistique, créatif, satirique, fictif ou analogue, les obligations de transparence énoncées au présent paragraphe se limitent à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre. »
  [4] « «hypertrucage», une image ou un contenu audio ou vidéo généré ou manipulé par l’IA, présentant une ressemblance avec des personnes, des objets, des lieux, des entités ou événements existants et pouvant être perçu à tort par une personne comme authentiques ou véridiques; »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 4 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [4] AI Act — règlement (UE) 2024/1689, article 3, définition 60 : Définitions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [3] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 2 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [5] AI Act — règlement (UE) 2024/1689, annexe XII : Informations relatives à la transparence visées à l'article 53, paragraphe 1, point b) – documentation technique pour les fournisseurs de modèles d'IA à usage général aux fournisseurs en aval qui intègrent le modèle dans leur système d'IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_XII
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « indiquez que les contenus ont été générés ou manipulés par une IA ».

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. »
- [1] « Cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. »
- [1] « Lorsque le contenu fait partie d’une œuvre ou d’un programme manifestement artistique, créatif, satirique, fictif ou analogue, les obligations de transparence énoncées au présent paragraphe se limitent à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre. »
- [4] « «hypertrucage», une image ou un contenu audio ou vidéo généré ou manipulé par l’IA, présentant une ressemblance avec des personnes, des objets, des lieux, des entités ou événements existants et pouvant être perçu à tort par une personne comme authentiques ou véridiques; »

RÉPONSE :
Oui, vous devez indiquer que l'image a été créée par une IA si elle constitue un « hypertrucage », c'est-à-dire une image « présentant une ressemblance avec des personnes, des objets, des lieux, des entités ou événements existants et pouvant être perçu à tort par une personne comme authentiques ou véridiques » [4]. En tant que déployeur du système d'IA, vous « indiquez que les contenus ont été générés ou manipulés par une IA » [1]. Cette obligation ne s'applique pas « lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière » [1]. Si l'image fait partie d’une œuvre « manifestement artistique, créatif, satirique, fictif ou analogue », l'obligation se limite « à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : contenu généré par une machine ; transparence ; étiquetage ; obligation d'information ; contenu synthétique ; notification

Temps : recherche 31.9 s · génération 2.1 s (2589 tokens lus, 509 écrits, 472.0 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.6 s · attente des limites de l'API 22 s (non comptée)

## q27 — Quelles amendes prévoit le règlement européen sur l'intelligence artificielle ?

Article attendu : AI Act art. 99, paragraphe 4 ou AI Act art. 99, paragraphe 6 — absent des passages donnés au modèle.

### Réponse du copilote

> Le règlement européen sur l'intelligence artificielle prévoit plusieurs niveaux d'amendes selon l'acteur concerné et la nature de la violation. Pour les opérateurs en général, les États membres déterminent le régime des sanctions, qui peuvent inclure des amendes administratives [1]. En cas de non-respect des pratiques interdites visées à l'article 5, l'amende peut atteindre 35 000 000 EUR ou 7 % du chiffre d'affaires annuel mondial total de l'entreprise, le montant le plus élevé étant retenu [3]. Pour les institutions, organes et organismes de l'Union, le non-respect de ces mêmes interdictions entraîne une amende pouvant aller jusqu'à 1 500 000 EUR [2], tandis que la non-conformité avec d'autres exigences du règlement est sanctionnée par une amende pouvant aller jusqu'à 750 000 EUR [2]. Enfin, pour les fournisseurs de modèles d'IA à usage général, la Commission peut infliger des amendes n'excédant pas 3 % de leur chiffre d'affaires annuel mondial total ou 15 000 000 EUR, le montant le plus élevé étant retenu [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « les États membres déterminent le régime des sanctions et autres mesures d'exécution, qui peuvent également comprendre des amendes administratives, des avertissements et des mesures non monétaires, applicables à toute violation du présent règlement commise par des opérateurs »
  [3] « Le non-respect de l'interdiction des pratiques en matière d'IA visées à l'article 5 fait l'objet d'amendes administratives pouvant aller jusqu'à 35 000 000 EUR ou, si l'auteur de l'infraction est une entreprise, jusqu'à 7 % de son chiffre d'affaires annuel mondial total réalisé au cours de l'exercice précédent, le montant le plus élevé étant retenu. »
  [2] « Le non-respect de l'interdiction des pratiques en matière d'IA visées à l'article 5 fait l'objet d'une amende administrative pouvant aller jusqu'à 1 500 000 EUR. »
  [2] « La non-conformité du système d'IA avec les exigences ou obligations au titre du présent règlement, autres que celles énoncées à l'article 5, fait l'objet d'une amende administrative pouvant aller jusqu'à 750 000 EUR. »
  [4] « La Commission peut infliger aux fournisseurs de modèles d'IA à usage général des amendes n'excédant pas 3 % de leur chiffre d'affaires annuel mondial total réalisé au cours de l'exercice précédent, ou 15 000 000 EUR, le montant le plus élevé étant retenu »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 1 : Sanctions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [2] AI Act — règlement (UE) 2024/1689, article 100 : Amendes administratives imposées aux institutions, organes et organismes de l’Union (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_100
  [3] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 3 : Sanctions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [4] AI Act — règlement (UE) 2024/1689, article 101 : Amendes applicables aux fournisseurs de modèles d’IA à usage général (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_101
Passages consultés mais non cités :
  [5] AI Act — règlement (UE) 2024/1689, article 75 quater, paragraphe 4 : Non-conformité, amendes et astreintes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_75c

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « les États membres déterminent le régime des sanctions et autres mesures d'exécution, qui peuvent également comprendre des amendes administratives, des avertissements et des mesures non monétaires, applicables à toute violation du présent règlement commise par des opérateurs »
- [3] « Le non-respect de l'interdiction des pratiques en matière d'IA visées à l'article 5 fait l'objet d'amendes administratives pouvant aller jusqu'à 35 000 000 EUR ou, si l'auteur de l'infraction est une entreprise, jusqu'à 7 % de son chiffre d'affaires annuel mondial total réalisé au cours de l'exercice précédent, le montant le plus élevé étant retenu. »
- [2] « Le non-respect de l'interdiction des pratiques en matière d'IA visées à l'article 5 fait l'objet d'une amende administrative pouvant aller jusqu'à 1 500 000 EUR. »
- [2] « La non-conformité du système d'IA avec les exigences ou obligations au titre du présent règlement, autres que celles énoncées à l'article 5, fait l'objet d'une amende administrative pouvant aller jusqu'à 750 000 EUR. »
- [4] « La Commission peut infliger aux fournisseurs de modèles d'IA à usage général des amendes n'excédant pas 3 % de leur chiffre d'affaires annuel mondial total réalisé au cours de l'exercice précédent, ou 15 000 000 EUR, le montant le plus élevé étant retenu »

RÉPONSE :
Le règlement européen sur l'intelligence artificielle prévoit plusieurs niveaux d'amendes selon l'acteur concerné et la nature de la violation. Pour les opérateurs en général, les États membres déterminent le régime des sanctions, qui peuvent inclure des amendes administratives [1]. En cas de non-respect des pratiques interdites visées à l'article 5, l'amende peut atteindre 35 000 000 EUR ou 7 % du chiffre d'affaires annuel mondial total de l'entreprise, le montant le plus élevé étant retenu [3]. Pour les institutions, organes et organismes de l'Union, le non-respect de ces mêmes interdictions entraîne une amende pouvant aller jusqu'à 1 500 000 EUR [2], tandis que la non-conformité avec d'autres exigences du règlement est sanctionnée par une amende pouvant aller jusqu'à 750 000 EUR [2]. Enfin, pour les fournisseurs de modèles d'IA à usage général, la Commission peut infliger des amendes n'excédant pas 3 % de leur chiffre d'affaires annuel mondial total ou 15 000 000 EUR, le montant le plus élevé étant retenu [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : sanctions administratives ; amendes administratives ; violations

Temps : recherche 30.2 s · génération 2.6 s (3125 tokens lus, 637 écrits, 318.8 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.2 s · attente des limites de l'API 15 s (non comptée)

## h03 — Comment déclarer la création d'une association en préfecture ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 4, définition 7 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [2] RGPD — règlement (UE) 2016/679, article 60, paragraphe 10 : Coopération entre l'autorité de contrôle chef de file et les autres autorités de contrôle concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_60
  [3] RGPD — règlement (UE) 2016/679, article 60, paragraphe 1 : Coopération entre l'autorité de contrôle chef de file et les autres autorités de contrôle concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_60
  [4] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30
  [5] RGPD — règlement (UE) 2016/679, article 60, paragraphe 9 : Coopération entre l'autorité de contrôle chef de file et les autres autorités de contrôle concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_60

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : déclaration de création ; association ; préfecture ; registre national des associations

Temps : recherche 20.8 s · génération 0.9 s (2574 tokens lus, 25 écrits, 201.9 tokens/s) · reformulation 0.3 s · attente des limites de l'API 14 s (non comptée)

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
  [4] RGPD — règlement (UE) 2016/679, article 83, paragraphe 4 : Conditions générales pour imposer des amendes administratives
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

Temps : recherche 26.2 s · génération 0.6 s (2156 tokens lus, 25 écrits, 449.9 tokens/s) · reformulation 0.6 s

## h05 — Comment rédiger les statuts d'une association ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

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
  [4] RGPD — règlement (UE) 2016/679, article 80 : Représentation des personnes concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_80
  [5] RGPD — règlement (UE) 2016/679, article 4, définition 10 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : personne morale de droit privé ; objet social ; siège social ; assemblée générale ; organe de direction ; organe de contrôle

Temps : recherche 28.0 s · génération 0.6 s (2175 tokens lus, 25 écrits, 162.9 tokens/s) · reformulation 0.5 s
