# Réponses du copilote — v6b_remote_v1

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 19/11/2026 à 13:06 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen/qwen3.8-27b` via l'API compatible OpenAI https://api.groq.com/openai/v1 (expérience de la séance 7, questions de test seulement ; modèle tel que servi par l'API à la date ci-dessus) — température 0.1, raisonnement : réglage par défaut du modèle, passages calculés pour un contexte de 8192 tokens comme en local, 2000 tokens au plus par réponse (raisonnement compris) ; le juge est le même modèle
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu, reranker `BAAI/bge-reranker-v2-m3` sur CPU (20 candidats reclassés avant la limite par article), reformulation de la question par le modèle avant la recherche (termes juridiques ajoutés, sans conclusion)
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_v1.jsonl` (10 + 1 hors sujet)
- Sélection : seules les questions choisies avec --ids ont été posées (les autres ne figurent pas dans ce fichier)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q13 | Un adhérent veut récupérer ses données pour les donner à une autre association : est-ce un droit ? | 4/4 | non | — | 38 s |
| q14 | Puis-je envoyer une lettre d'information par e-mail à mes adhérents, et peuvent-ils refuser ? | 6/6 | non | — | 30 s |
| q15 | Mon prestataire informatique a accès à nos fichiers : faut-il signer un contrat particulier ? | 6/6 | non | — | 31 s |
| q16 | Puis-je stocker les fichiers de mon association chez un hébergeur situé aux États-Unis ? | 6/6 | non | — | 28 s |
| q18 | Notre association peut-elle collecter des informations sur la santé de ses bénévoles ? | 6/6 | non | La réponse ne reprend que 7 des 9 cas énumérés au passage [1], sans dire qu'elle n'en cite qu'une partie. Vérifiez la liste complète. | 31 s |
| q20 | À partir de quel âge un enfant peut-il s'inscrire seul à notre service en ligne ? | 3/3 | non | — | 25 s |
| q22 | Le consentement d'une personne doit-il être donné par écrit ? | 3/3 | non | La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Non, le consentement ne doit pas obligatoirement être donné par écrit pour le traitement des données à caractère … ». Vérifiez ce point.; La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « L'écrit n'est pas la forme unique exigée, mais si le consentement est donné dans le cadre d'une « déclaration écrite … ». Vérifiez ce point.; La réponse met entre « » un texte introuvable dans les extraits vérifiés : « présenté sous une forme qui la distingue clairement de ces autres questions, sous une forme compréhensible et aisément … ».; La réponse s'appuie sur le RGPD et l'AI Act sans dire de quel règlement vient chaque obligation : « Non, le consentement ne doit pas obligatoirement être donné par écrit pour le traitement des données à caractère … » (et 1 autre(s)). | 25 s |
| q23 | Quelles utilisations de l'intelligence artificielle sont interdites en Europe ? | 4/6 | non | 2 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1], [1]) : ignoré(s). | 33 s |
| q24 | Ai-je le droit d'utiliser une IA qui analyse les émotions de mes salariés ? | 3/3 | non | La réponse met entre « » un texte introuvable dans les extraits vérifiés : « informer les personnes physiques qui y sont exposées du fonctionnement du système » (et 1 autre(s)). | 31 s |
| q25 | Mon logiciel est-il un « système d'IA » au sens de la loi européenne ? | 1/1 | non | — | 26 s |
| h05 | Comment rédiger les statuts d'une association ? | 0/0 | oui | — | 31 s |

## q13 — Un adhérent veut récupérer ses données pour les donner à une autre association : est-ce un droit ?

Article attendu : RGPD art. 20 — passage [1].

### Réponse du copilote

> Oui, il s'agit du droit à la portabilité des données prévu par le RGPD, article 20 [1].
> Cependant, ce droit ne s'applique que si deux conditions sont remplies : le traitement doit être fondé sur le consentement ou sur un contrat, et il doit être effectué à l'aide de procédés automatisés [1].
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
Oui, il s'agit du droit à la portabilité des données prévu par le RGPD, article 20 [1].
Cependant, ce droit ne s'applique que si deux conditions sont remplies : le traitement doit être fondé sur le consentement ou sur un contrat, et il doit être effectué à l'aide de procédés automatisés [1].
Si le traitement de l'association est nécessaire à l'exécution d'une mission d'intérêt public ou relevant de l'exercice de l'autorité publique, ce droit ne s'applique pas [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit à la portabilité des données ; données à caractère personnel ; destinataire ; transfert de données

Temps : recherche 35.9 s · génération 1.2 s (3145 tokens lus, 362 écrits, 443.4 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.2 s

## q14 — Puis-je envoyer une lettre d'information par e-mail à mes adhérents, et peuvent-ils refuser ?

Article attendu : RGPD art. 21 ou RGPD art. 6, paragraphe 1 — passage [1].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question concernant la légalité de l'envoi d'une lettre d'information par e-mail, car ils ne mentionnent pas les conditions spécifiques de consentement ou de base légale pour l'envoi de messages commerciaux ou d'information par voie électronique (souvent régies par la directive 2002/58/CE ou le droit national). Cependant, si le traitement de vos données pour cet envoi est fondé sur l'article 6, paragraphe 1, point e) ou f) du RGPD, ou s'il vise des fins de prospection, vos adhérents disposent d'un droit d'opposition [1]. Dans ce cas, ils peuvent s'opposer « à tout moment, pour des raisons tenant à sa situation particulière » [1]. Si l'opposition concerne des fins de prospection, « les données à caractère personnel ne sont plus traitées à ces fins » [1]. Pour les autres cas d'opposition, le responsable du traitement « ne traite plus les données à caractère personnel, à moins qu'il ne démontre qu'il existe des motifs légitimes et impérieux pour le traitement qui prévalent sur les intérêts et les droits et libertés de la personne concernée, ou pour la constatation, l'exercice ou la défense de droits en justice » [1]. Vous devez informer vos adhérents de ce droit « au plus tard au moment de la première communication avec la personne concernée » et le présenter « clairement et séparément de toute autre information » [1]. Ils peuvent exercer ce droit « à l'aide de procédés automatisés utilisant des spécifications techniques » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit de s'opposer à tout moment, pour des raisons tenant à sa situation particulière, à un traitement des données à caractère personnel la concernant fondé sur l'article 6, paragraphe 1, point e) ou f), y compris un profilage fondé sur ces dispositions. »
  [1] « Le responsable du traitement ne traite plus les données à caractère personnel, à moins qu'il ne démontre qu'il existe des motifs légitimes et impérieux pour le traitement qui prévalent sur les intérêts et les droits et libertés de la personne concernée, ou pour la constatation, l'exercice ou la défense de droits en justice. »
  [1] « Lorsque les données à caractère personnel sont traitées à des fins de prospection, la personne concernée a le droit de s'opposer à tout moment au traitement des données à caractère personnel la concernant à de telles fins de prospection, y compris au profilage dans la mesure où il est lié à une telle prospection. »
  [1] « Lorsque la personne concernée s'oppose au traitement à des fins de prospection, les données à caractère personnel ne sont plus traitées à ces fins. »
  [1] « Au plus tard au moment de la première communication avec la personne concernée, le droit visé aux paragraphes 1 et 2 est explicitement porté à l'attention de la personne concernée et est présenté clairement et séparément de toute autre information. »
  [1] « Dans le cadre de l'utilisation de services de la société de l'information, et nonobstant la directive 2002/58/CE, la personne concernée peut exercer son droit d'opposition à l'aide de procédés automatisés utilisant des spécifications techniques. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 21 : Droit d'opposition (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_21
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [3] RGPD — règlement (UE) 2016/679, article 34 : Communication à la personne concernée d'une violation de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_34
  [4] RGPD — règlement (UE) 2016/679, article 18 : Droit à la limitation du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_18
  [5] RGPD — règlement (UE) 2016/679, article 80 : Représentation des personnes concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_80

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « La personne concernée a le droit de s'opposer à tout moment, pour des raisons tenant à sa situation particulière, à un traitement des données à caractère personnel la concernant fondé sur l'article 6, paragraphe 1, point e) ou f), y compris un profilage fondé sur ces dispositions. »
- [1] « Le responsable du traitement ne traite plus les données à caractère personnel, à moins qu'il ne démontre qu'il existe des motifs légitimes et impérieux pour le traitement qui prévalent sur les intérêts et les droits et libertés de la personne concernée, ou pour la constatation, l'exercice ou la défense de droits en justice. »
- [1] « Lorsque les données à caractère personnel sont traitées à des fins de prospection, la personne concernée a le droit de s'opposer à tout moment au traitement des données à caractère personnel la concernant à de telles fins de prospection, y compris au profilage dans la mesure où il est lié à une telle prospection. »
- [1] « Lorsque la personne concernée s'oppose au traitement à des fins de prospection, les données à caractère personnel ne sont plus traitées à ces fins. »
- [1] « Au plus tard au moment de la première communication avec la personne concernée, le droit visé aux paragraphes 1 et 2 est explicitement porté à l'attention de la personne concernée et est présenté clairement et séparément de toute autre information. »
- [1] « Dans le cadre de l'utilisation de services de la société de l'information, et nonobstant la directive 2002/58/CE, la personne concernée peut exercer son droit d'opposition à l'aide de procédés automatisés utilisant des spécifications techniques. »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question concernant la légalité de l'envoi d'une lettre d'information par e-mail, car ils ne mentionnent pas les conditions spécifiques de consentement ou de base légale pour l'envoi de messages commerciaux ou d'information par voie électronique (souvent régies par la directive 2002/58/CE ou le droit national). Cependant, si le traitement de vos données pour cet envoi est fondé sur l'article 6, paragraphe 1, point e) ou f) du RGPD, ou s'il vise des fins de prospection, vos adhérents disposent d'un droit d'opposition [1]. Dans ce cas, ils peuvent s'opposer « à tout moment, pour des raisons tenant à sa situation particulière » [1]. Si l'opposition concerne des fins de prospection, « les données à caractère personnel ne sont plus traitées à ces fins » [1]. Pour les autres cas d'opposition, le responsable du traitement « ne traite plus les données à caractère personnel, à moins qu'il ne démontre qu'il existe des motifs légitimes et impérieux pour le traitement qui prévalent sur les intérêts et les droits et libertés de la personne concernée, ou pour la constatation, l'exercice ou la défense de droits en justice » [1]. Vous devez informer vos adhérents de ce droit « au plus tard au moment de la première communication avec la personne concernée » et le présenter « clairement et séparément de toute autre information » [1]. Ils peuvent exercer ce droit « à l'aide de procédés automatisés utilisant des spécifications techniques » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : consentement ; droit d'opposition ; communication électronique ; traitement de données à caractère personnel

Temps : recherche 27.4 s · génération 2.1 s (3357 tokens lus, 752 écrits, 472.5 tokens/s) · contrôle de pertinence 0.7 s · reformulation 0.2 s · attente des limites de l'API 26 s (non comptée)

## q15 — Mon prestataire informatique a accès à nos fichiers : faut-il signer un contrat particulier ?

Article attendu : RGPD art. 28, paragraphe 3 — passage [4].

### Réponse du copilote

> Oui, vous devez signer un contrat spécifique avec votre prestataire informatique, car il agit en tant que sous-traitant pour votre compte [3]. Ce contrat, régi par le RGPD (article 28), doit définir l'objet, la durée, la nature et la finalité du traitement, ainsi que le type de données et les catégories de personnes concernées [4]. Il doit également prévoir que le sous-traitant ne traite les données que sur instruction documentée de votre part, veille à la confidentialité du personnel, prend les mesures de sécurité requises et vous permet de réaliser des audits [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « Lorsqu'un traitement doit être effectué pour le compte d'un responsable du traitement, celui-ci fait uniquement appel à des sous-traitants qui présentent des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées de manière à ce que le traitement réponde aux exigences du présent règlement et garantisse la protection des droits de la personne concernée. »
  [4] « Le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre, qui lie le sous-traitant à l'égard du responsable du traitement, définit l'objet et la durée du traitement, la nature et la finalité du traitement, le type de données à caractère personnel et les catégories de personnes concernées, et les obligations et les droits du responsable du traitement. »
  [4] « Ce contrat ou cet autre acte juridique prévoit, notamment, que le sous-traitant: a) ne traite les données à caractère personnel que sur instruction documentée du responsable du traitement, y compris en ce qui concerne les transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale, à moins qu'il ne soit tenu d'y procéder en vertu du droit de l'Union ou du droit de l'État membre auquel le sous-traitant est soumis; dans ce cas, le sous-traitant informe le responsable du traitement de cette obligation juridique avant le traitement, sauf si le droit concerné interdit une telle information pour des motifs importants d'intérêt public; »
  [4] « b) veille à ce que les personnes autorisées à traiter les données à caractère personnel s'engagent à respecter la confidentialité ou soient soumises à une obligation légale appropriée de confidentialité; »
  [4] « c) prend toutes les mesures requises en vertu de l'article 32; »
  [4] « h) met à la disposition du responsable du traitement toutes les informations nécessaires pour démontrer le respect des obligations prévues au présent article et pour permettre la réalisation d'audits, y compris des inspections, par le responsable du traitement ou un autre auditeur qu'il a mandaté, et contribuer à ces audits. »

Sources citées :
  [3] RGPD — règlement (UE) 2016/679, article 28, paragraphe 1 : Sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [4] RGPD — règlement (UE) 2016/679, article 28, paragraphe 3 : Sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30
  [2] RGPD — règlement (UE) 2016/679, article 28, paragraphe 4 : Sous-traitant
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [5] RGPD — règlement (UE) 2016/679, article 29 : Traitement effectué sous l'autorité du responsable du traitement ou du sous-traitant
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_29

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [3] « Lorsqu'un traitement doit être effectué pour le compte d'un responsable du traitement, celui-ci fait uniquement appel à des sous-traitants qui présentent des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées de manière à ce que le traitement réponde aux exigences du présent règlement et garantisse la protection des droits de la personne concernée. »
- [4] « Le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre, qui lie le sous-traitant à l'égard du responsable du traitement, définit l'objet et la durée du traitement, la nature et la finalité du traitement, le type de données à caractère personnel et les catégories de personnes concernées, et les obligations et les droits du responsable du traitement. »
- [4] « Ce contrat ou cet autre acte juridique prévoit, notamment, que le sous-traitant: a) ne traite les données à caractère personnel que sur instruction documentée du responsable du traitement, y compris en ce qui concerne les transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale, à moins qu'il ne soit tenu d'y procéder en vertu du droit de l'Union ou du droit de l'État membre auquel le sous-traitant est soumis; dans ce cas, le sous-traitant informe le responsable du traitement de cette obligation juridique avant le traitement, sauf si le droit concerné interdit une telle information pour des motifs importants d'intérêt public; »
- [4] « b) veille à ce que les personnes autorisées à traiter les données à caractère personnel s'engagent à respecter la confidentialité ou soient soumises à une obligation légale appropriée de confidentialité; »
- [4] « c) prend toutes les mesures requises en vertu de l'article 32; »
- [4] « h) met à la disposition du responsable du traitement toutes les informations nécessaires pour démontrer le respect des obligations prévues au présent article et pour permettre la réalisation d'audits, y compris des inspections, par le responsable du traitement ou un autre auditeur qu'il a mandaté, et contribuer à ces audits. »

RÉPONSE :
Oui, vous devez signer un contrat spécifique avec votre prestataire informatique, car il agit en tant que sous-traitant pour votre compte [3]. Ce contrat, régi par le RGPD (article 28), doit définir l'objet, la durée, la nature et la finalité du traitement, ainsi que le type de données et les catégories de personnes concernées [4]. Il doit également prévoir que le sous-traitant ne traite les données que sur instruction documentée de votre part, veille à la confidentialité du personnel, prend les mesures de sécurité requises et vous permet de réaliser des audits [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : traitement de données à caractère personnel ; sous-traitant ; contrat de traitement ; mesures techniques et organisationnelles ; registre des activités de traitement

Temps : recherche 26.7 s · génération 2.6 s (3044 tokens lus, 606 écrits, 384.8 tokens/s) · contrôle de pertinence 0.2 s · reformulation 1.1 s

## q16 — Puis-je stocker les fichiers de mon association chez un hébergeur situé aux États-Unis ?

Article attendu : RGPD art. 44 ou RGPD art. 45, paragraphe 1 ou RGPD art. 46 — passage [1].

### Réponse du copilote

> Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, à condition de respecter les règles de transfert de données hors de l'Union européenne [1]. Si la Commission européenne a constaté par décision que les États-Unis assurent un niveau de protection adéquat, le transfert peut avoir lieu sans autorisation spécifique [5]. En l'absence de cette décision d'adéquation, vous ne pouvez transférer les données que si vous avez prévu des garanties appropriées et que les personnes concernées disposent de droits opposables et de voies de droit effectives [1]. Parmi ces garanties, vous pouvez utiliser des clauses types de protection des données adoptées par la Commission ou par une autorité de contrôle approuvées par la Commission, sans nécessiter d'autorisation particulière [1]. La liste des pays reconnus comme offrant un niveau de protection adéquat est publiée par la Commission européenne.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
  [1] « Les garanties appropriées visées au paragraphe 1 peuvent être fournies, sans que cela ne nécessite une autorisation particulière d'une autorité de contrôle, par: »
  [1] « c) des clauses types de protection des données adoptées par la Commission en conformité avec la procédure d'examen visée à l'article 93, paragraphe 2; »
  [1] « d) des clauses types de protection des données adoptées par une autorité de contrôle et approuvées par la Commission en conformité avec la procédure d'examen visée à l'article 93, paragraphe 2; »
  [5] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. »
  [5] « Un tel transfert ne nécessite pas d'autorisation spécifique. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 46 : Transferts moyennant des garanties appropriées (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_46
  [5] RGPD — règlement (UE) 2016/679, article 45, paragraphe 1 : Transferts fondés sur une décision d'adéquation (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [3] RGPD — règlement (UE) 2016/679, article 45, paragraphe 2 : Transferts fondés sur une décision d'adéquation
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
  [4] RGPD — règlement (UE) 2016/679, article 49, paragraphe 1 : Dérogations pour des situations particulières
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_49
Note : La liste des pays bénéficiant d'une décision d'adéquation n'est pas dans les textes utilisés par le copilote : consultez la page de la Commission européenne sur les décisions d'adéquation (en anglais) : https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
- [1] « Les garanties appropriées visées au paragraphe 1 peuvent être fournies, sans que cela ne nécessite une autorisation particulière d'une autorité de contrôle, par: »
- [1] « c) des clauses types de protection des données adoptées par la Commission en conformité avec la procédure d'examen visée à l'article 93, paragraphe 2; »
- [1] « d) des clauses types de protection des données adoptées par une autorité de contrôle et approuvées par la Commission en conformité avec la procédure d'examen visée à l'article 93, paragraphe 2; »
- [5] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. »
- [5] « Un tel transfert ne nécessite pas d'autorisation spécifique. »

RÉPONSE :
Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, à condition de respecter les règles de transfert de données hors de l'Union européenne [1]. Si la Commission européenne a constaté par décision que les États-Unis assurent un niveau de protection adéquat, le transfert peut avoir lieu sans autorisation spécifique [5]. En l'absence de cette décision d'adéquation, vous ne pouvez transférer les données que si vous avez prévu des garanties appropriées et que les personnes concernées disposent de droits opposables et de voies de droit effectives [1]. Parmi ces garanties, vous pouvez utiliser des clauses types de protection des données adoptées par la Commission ou par une autorité de contrôle approuvées par la Commission, sans nécessiter d'autorisation particulière [1]. La liste des pays reconnus comme offrant un niveau de protection adéquat est publiée par la Commission européenne.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : transfert de données vers un pays tiers ; pays tiers ; mesures de sécurité ; hébergement de données ; données à caractère personnel ; responsable du traitement

Temps : recherche 25.1 s · génération 2.4 s (3694 tokens lus, 522 écrits, 354.4 tokens/s) · contrôle de pertinence 0.6 s · reformulation 0.2 s · attente des limites de l'API 17 s (non comptée)

## q18 — Notre association peut-elle collecter des informations sur la santé de ses bénévoles ?

Article attendu : RGPD art. 9, paragraphe 1 ou RGPD art. 9, paragraphe 2 — passage [1].

### Réponse du copilote

> Oui, votre association peut collecter des informations sur la santé de ses bénévoles, mais uniquement si l'une des conditions d'exception prévues par le RGPD est remplie [1].
> La première possibilité est d'obtenir le « consentement explicite » des bénévoles pour une finalité spécifique, « sauf lorsque le droit de l'Union ou le droit de l'État membre prévoit que l'interdiction visée au paragraphe 1 ne peut pas être levée par la personne concernée » [1].
> Une autre possibilité concerne les associations à but non lucratif : le traitement est autorisé « à condition que ledit traitement se rapporte exclusivement aux membres ou aux anciens membres dudit organisme ou aux personnes entretenant avec celui-ci des contacts réguliers en liaison avec ses finalités et que les données à caractère personnel ne soient pas communiquées en dehors de cet organisme sans le consentement des personnes concernées » [1].
> Il est également possible que le traitement soit « nécessaire aux fins de la médecine préventive ou de la médecine du travail... sur la base du droit de l'Union, du droit d'un État membre ou en vertu d'un contrat conclu avec un professionnel de la santé » [1].
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
La première possibilité est d'obtenir le « consentement explicite » des bénévoles pour une finalité spécifique, « sauf lorsque le droit de l'Union ou le droit de l'État membre prévoit que l'interdiction visée au paragraphe 1 ne peut pas être levée par la personne concernée » [1].
Une autre possibilité concerne les associations à but non lucratif : le traitement est autorisé « à condition que ledit traitement se rapporte exclusivement aux membres ou aux anciens membres dudit organisme ou aux personnes entretenant avec celui-ci des contacts réguliers en liaison avec ses finalités et que les données à caractère personnel ne soient pas communiquées en dehors de cet organisme sans le consentement des personnes concernées » [1].
Il est également possible que le traitement soit « nécessaire aux fins de la médecine préventive ou de la médecine du travail... sur la base du droit de l'Union, du droit d'un État membre ou en vertu d'un contrat conclu avec un professionnel de la santé » [1].
En tant que responsable du traitement, vous devez informer les bénévoles des « finalités du traitement... ainsi que la base juridique du traitement » [4].
Vous devez également leur communiquer « la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée » [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données de santé ; données à caractère personnel ; responsable du traitement ; consentement ; minimisation des données

Temps : recherche 27.7 s · génération 2.6 s (3600 tokens lus, 741 écrits, 464.3 tokens/s) · contrôle de pertinence 0.3 s · reformulation 0.5 s

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
  [3] RGPD — règlement (UE) 2016/679, article 57, paragraphe 1, points a) à t) : Missions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_57
  [4] RGPD — règlement (UE) 2016/679, article 4, définition 11 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [5] RGPD — règlement (UE) 2016/679, article 22 : Décision individuelle automatisée, y compris le profilage
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_22

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

Reformulation de la question (termes ajoutés avant la recherche) : consentement parental ; âge de la responsabilité numérique ; consentement de l'enfant ; consentement explicite ; consentement libre

Temps : recherche 24.1 s · génération 0.9 s (3184 tokens lus, 244 écrits, 462.5 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.3 s · attente des limites de l'API 26 s (non comptée)

## q22 — Le consentement d'une personne doit-il être donné par écrit ?

Article attendu : RGPD art. 7 — passage [1].

### Réponse du copilote

> Non, le consentement ne doit pas obligatoirement être donné par écrit pour le traitement des données à caractère personnel : il peut résulter d'une « déclaration ou par un acte positif clair » [2]. L'écrit n'est pas la forme unique exigée, mais si le consentement est donné dans le cadre d'une « déclaration écrite qui concerne également d'autres questions », il doit être « présenté sous une forme qui la distingue clairement de ces autres questions, sous une forme compréhensible et aisément accessible, et formulée en des termes clairs et simples » [1]. En revanche, pour les essais en conditions réelles relevant de l'AI Act, le consentement éclairé doit être « daté et documenté » [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « «consentement» de la personne concernée, toute manifestation de volonté, libre, spécifique, éclairée et univoque par laquelle la personne concernée accepte, par une déclaration ou par un acte positif clair, que des données à caractère personnel la concernant fassent l'objet d'un traitement; »
  [1] « Si le consentement de la personne concernée est donné dans le cadre d'une déclaration écrite qui concerne également d'autres questions, la demande de consentement est présentée sous une forme qui la distingue clairement de ces autres questions, sous une forme compréhensible et aisément accessible, et formulée en des termes clairs et simples. »
  [4] « Le consentement éclairé est daté et documenté et une copie en est remise aux participants aux essais ou à leur représentant légal. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 7 : Conditions applicables au consentement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_7
  [2] RGPD — règlement (UE) 2016/679, article 4, définition 11 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [4] AI Act — règlement (UE) 2024/1689, article 61 : Consentement éclairé à participer aux essais en conditions réelles en dehors des bacs à sable réglementaires de l’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_61
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, article 3, définition 59 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
  [5] RGPD — règlement (UE) 2016/679, article 22 : Décision individuelle automatisée, y compris le profilage
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_22
Attention : La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Non, le consentement ne doit pas obligatoirement être donné par écrit pour le traitement des données à caractère … ». Vérifiez ce point.
Attention : La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « L'écrit n'est pas la forme unique exigée, mais si le consentement est donné dans le cadre d'une « déclaration écrite … ». Vérifiez ce point.
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « présenté sous une forme qui la distingue clairement de ces autres questions, sous une forme compréhensible et aisément … ».
Attention : La réponse s'appuie sur le RGPD et l'AI Act sans dire de quel règlement vient chaque obligation : « Non, le consentement ne doit pas obligatoirement être donné par écrit pour le traitement des données à caractère … » (et 1 autre(s)).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [2] « «consentement» de la personne concernée, toute manifestation de volonté, libre, spécifique, éclairée et univoque par laquelle la personne concernée accepte, par une déclaration ou par un acte positif clair, que des données à caractère personnel la concernant fassent l'objet d'un traitement; »
- [1] « Si le consentement de la personne concernée est donné dans le cadre d'une déclaration écrite qui concerne également d'autres questions, la demande de consentement est présentée sous une forme qui la distingue clairement de ces autres questions, sous une forme compréhensible et aisément accessible, et formulée en des termes clairs et simples. »
- [4] « Le consentement éclairé est daté et documenté et une copie en est remise aux participants aux essais ou à leur représentant légal. »

RÉPONSE :
Non, le consentement ne doit pas obligatoirement être donné par écrit pour le traitement des données à caractère personnel : il peut résulter d'une « déclaration ou par un acte positif clair » [2]. L'écrit n'est pas la forme unique exigée, mais si le consentement est donné dans le cadre d'une « déclaration écrite qui concerne également d'autres questions », il doit être « présenté sous une forme qui la distingue clairement de ces autres questions, sous une forme compréhensible et aisément accessible, et formulée en des termes clairs et simples » [1]. En revanche, pour les essais en conditions réelles relevant de l'AI Act, le consentement éclairé doit être « daté et documenté » [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : consentement explicite ; consentement libre ; consentement spécifique ; consentement informé ; consentement par écrit

Temps : recherche 23.2 s · génération 1.0 s (2425 tokens lus, 337 écrits, 503.5 tokens/s) · contrôle de pertinence 0.1 s · reformulation 0.4 s

## q23 — Quelles utilisations de l'intelligence artificielle sont interdites en Europe ?

Article attendu : AI Act art. 5, paragraphe 1 — passage [1].

### Réponse du copilote

> L’AI Act interdit plusieurs pratiques spécifiques en matière d’intelligence artificielle, notamment l’utilisation de techniques subliminales ou manipulatrices visant à altérer le comportement d’une personne et à lui causer un préjudice important [1]. Il est également interdit d’exploiter les vulnérabilités liées à l’âge, au handicap ou à la situation sociale ou économique d’une personne pour altérer son comportement et lui causer un préjudice [1]. La génération ou la manipulation de contenus réalistes représentant des parties intimes ou des activités sexuellement explicites sans le consentement libre, spécifique, éclairé, univoque et explicite de la personne concernée est aussi interdite [1]. De même, la production de matériel relevant de la directive 2011/93/UE est prohibée, « sauf lorsqu'une défense «sans droit» s'applique en vertu du droit national » [1]. L’évaluation ou la classification de personnes par « note sociale » entraînant un traitement préjudiciable, défavorable, injustifié ou disproportionné est interdite [1]. Enfin, la prédiction du risque de commission d’une infraction pénale basée uniquement sur le profilage ou les traits de personnalité est interdite, « cette interdiction ne s’applique pas aux systèmes d’IA utilisés pour étayer l’évaluation humaine de l’implication d’une personne dans une activité criminelle, qui est déjà fondée sur des faits objectifs et vérifiables, directement liés à une activité criminelle » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « a) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui a recours à des techniques subliminales, au-dessous du seuil de conscience d’une personne, ou à des techniques délibérément manipulatrices ou trompeuses, avec pour objectif ou effet d’altérer substantiellement le comportement d’une personne ou d’un groupe de personnes en portant considérablement atteinte à leur capacité à prendre une décision éclairée, amenant ainsi la personne à prendre une décision qu’elle n’aurait pas prise autrement, d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne, à une autre personne ou à un groupe de personnes; »
  [1] « b) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui exploite les éventuelles vulnérabilités dues à l’âge, au handicap ou à la situation sociale ou économique spécifique d’une personne physique ou d’un groupe de personnes donné avec pour objectif ou effet d’altérer substantiellement le comportement de cette personne ou d’un membre de ce groupe d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne ou à un tiers; »
  [1] « b ter) la mise sur le marché, la mise en service ou l'utilisation d'un système d'IA qui génère ou manipule tout matériel ou spectacle au sens de l'article 2, points c) et e), de la directive 2011/93/UE, sauf lorsqu'une défense «sans droit» s'applique en vertu du droit national; »
  [1] « d) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation d’un système d’IA pour mener des évaluations des risques des personnes physiques visant à évaluer ou à prédire le risque qu’une personne physique commette une infraction pénale, uniquement sur la base du profilage d’une personne physique ou de l’évaluation de ses traits de personnalité ou caractéristiques; cette interdiction ne s’applique pas aux systèmes d’IA utilisés pour étayer l’évaluation humaine de l’implication d’une personne dans une activité criminelle, qui est déjà fondée sur des faits objectifs et vérifiables, directement liés à une activité criminelle; »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points a) à e) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points f) à h) : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [3] AI Act — règlement (UE) 2024/1689, article 1 : Objet
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_1
  [4] AI Act — règlement (UE) 2024/1689, article 6, paragraphe 5 : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
  [5] AI Act — règlement (UE) 2024/1689, article 6, paragraphe 1 : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
Attention : 2 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1], [1]) : ignoré(s).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « a) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui a recours à des techniques subliminales, au-dessous du seuil de conscience d’une personne, ou à des techniques délibérément manipulatrices ou trompeuses, avec pour objectif ou effet d’altérer substantiellement le comportement d’une personne ou d’un groupe de personnes en portant considérablement atteinte à leur capacité à prendre une décision éclairée, amenant ainsi la personne à prendre une décision qu’elle n’aurait pas prise autrement, d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne, à une autre personne ou à un groupe de personnes; »
- [1] « b) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui exploite les éventuelles vulnérabilités dues à l’âge, au handicap ou à la situation sociale ou économique spécifique d’une personne physique ou d’un groupe de personnes donné avec pour objectif ou effet d’altérer substantiellement le comportement de cette personne ou d’un membre de ce groupe d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne ou à un tiers; »
- [1] « b bis) la prise sur le marché, la prise en service ou l'utilisation d'un système d'IA qui génère ou manipule des images, des vidéos, des contenus audio ou tout autre matériel similaire réalistes représentant les parties intimes d'une personne identifiable, ou une personne identifiable se livrant à des activités sexuellement explicites, sans le consentement libre, spécifique, éclairé, univoque et explicite de cette personne pour cette production ou manipulation; »
- [1] « b ter) la mise sur le marché, la mise en service ou l'utilisation d'un système d'IA qui génère ou manipule tout matériel ou spectacle au sens de l'article 2, points c) et e), de la directive 2011/93/UE, sauf lorsqu'une défense «sans droit» s'applique en vertu du droit national; »
- [1] « c) la prise sur le marché, la prise en service ou l’utilisation de systèmes d’IA pour l’évaluation ou la classification de personnes physiques ou de groupes de personnes au cours d’une période donnée en fonction de leur comportement social ou de leurs traits de personnalité ou de caractéristiques connues, déduites ou prédites, la note sociale conduisant à l’une ou l’une des situations suivantes, ou aux deux: i) le traitement préjudiciable ou défavorable de certaines personnes physiques ou de groupes de personnes dans des contextes sociaux dissociés du contexte dans lequel les données ont été générées ou collectées à l’origine; ii) le traitement préjudiciable ou défavorable de certaines personnes ou de groupes de personnes, qui est injustifié ou disproportionné par rapport à leur comportement social ou à la gravité de celui-ci; »
- [1] « d) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation d’un système d’IA pour mener des évaluations des risques des personnes physiques visant à évaluer ou à prédire le risque qu’une personne physique commette une infraction pénale, uniquement sur la base du profilage d’une personne physique ou de l’évaluation de ses traits de personnalité ou caractéristiques; cette interdiction ne s’applique pas aux systèmes d’IA utilisés pour étayer l’évaluation humaine de l’implication d’une personne dans une activité criminelle, qui est déjà fondée sur des faits objectifs et vérifiables, directement liés à une activité criminelle; »

RÉPONSE :
L’AI Act interdit plusieurs pratiques spécifiques en matière d’intelligence artificielle, notamment l’utilisation de techniques subliminales ou manipulatrices visant à altérer le comportement d’une personne et à lui causer un préjudice important [1]. Il est également interdit d’exploiter les vulnérabilités liées à l’âge, au handicap ou à la situation sociale ou économique d’une personne pour altérer son comportement et lui causer un préjudice [1]. La génération ou la manipulation de contenus réalistes représentant des parties intimes ou des activités sexuellement explicites sans le consentement libre, spécifique, éclairé, univoque et explicite de la personne concernée est aussi interdite [1]. De même, la production de matériel relevant de la directive 2011/93/UE est prohibée, « sauf lorsqu'une défense «sans droit» s'applique en vertu du droit national » [1]. L’évaluation ou la classification de personnes par « note sociale » entraînant un traitement préjudiciable, défavorable, injustifié ou disproportionné est interdite [1]. Enfin, la prédiction du risque de commission d’une infraction pénale basée uniquement sur le profilage ou les traits de personnalité est interdite, « cette interdiction ne s’applique pas aux systèmes d’IA utilisés pour étayer l’évaluation humaine de l’implication d’une personne dans une activité criminelle, qui est déjà fondée sur des faits objectifs et vérifiables, directement liés à une activité criminelle » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : systèmes de scoring social ; manipulation subliminale ; exploitation de vulnérabilités ; reconnaissance faciale en temps réel

Temps : recherche 29.3 s · génération 2.9 s (3334 tokens lus, 1127 écrits, 458.0 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.2 s · attente des limites de l'API 40 s (non comptée)

## q24 — Ai-je le droit d'utiliser une IA qui analyse les émotions de mes salariés ?

Article attendu : AI Act art. 5, paragraphe 1_f h — passage [3].

### Réponse du copilote

> Non, vous n'avez pas le droit d'utiliser une IA qui analyse les émotions de vos salariés, car l'AI Act interdit « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement » [3]. Cette interdiction comporte une exception : elle ne s'applique pas « sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité » [3]. Si vous utilisez un tel système dans un cadre autorisé (par exemple pour la sécurité), vous devez en tant que déployeur « informer les personnes physiques qui y sont exposées du fonctionnement du système » et « traiter les données à caractère personnel conformément au règlement (UE) 2016/679 » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « f) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement, sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité; »
  [1] « Les déployeurs d’un système de reconnaissance des émotions ou d’un système de catégorisation biométrique informent les personnes physiques qui y sont exposées du fonctionnement du système et traitent les données à caractère personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680, selon le cas. »
  [1] « Cette obligation ne s’applique pas aux systèmes d’IA utilisés pour la catégorisation biométrique et la reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l’Union. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 3 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [3] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points f) à h) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [4] AI Act — règlement (UE) 2024/1689, article 3, définition 39 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
  [5] AI Act — règlement (UE) 2024/1689, article 86 : Droit à l’explication des décisions individuelles
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_86
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « informer les personnes physiques qui y sont exposées du fonctionnement du système » (et 1 autre(s)).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [3] « f) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement, sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité; »
- [1] « Les déployeurs d’un système de reconnaissance des émotions ou d’un système de catégorisation biométrique informent les personnes physiques qui y sont exposées du fonctionnement du système et traitent les données à caractère personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680, selon le cas. »
- [1] « Cette obligation ne s’applique pas aux systèmes d’IA utilisés pour la catégorisation biométrique et la reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l’Union. »

RÉPONSE :
Non, vous n'avez pas le droit d'utiliser une IA qui analyse les émotions de vos salariés, car l'AI Act interdit « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement » [3]. Cette interdiction comporte une exception : elle ne s'applique pas « sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité » [3]. Si vous utilisez un tel système dans un cadre autorisé (par exemple pour la sécurité), vous devez en tant que déployeur « informer les personnes physiques qui y sont exposées du fonctionnement du système » et « traiter les données à caractère personnel conformément au règlement (UE) 2016/679 » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : analyse des émotions ; données biométriques ; traitement de données à caractère personnel ; consentement ; finalité du traitement ; profilage

Temps : recherche 28.8 s · génération 1.7 s (2539 tokens lus, 482 écrits, 458.5 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.2 s · attente des limites de l'API 23 s (non comptée)

## q25 — Mon logiciel est-il un « système d'IA » au sens de la loi européenne ?

Article attendu : AI Act art. 3, définition 1 — passage [1].

### Réponse du copilote

> Pour déterminer si votre logiciel est un « système d'IA », il doit correspondre à la définition légale qui exige qu'il s'agisse d'un « système automatisé » conçu pour fonctionner à différents niveaux d'autonomie et capable de s'adapter après son déploiement [1]. De plus, le logiciel doit déduire, à partir des entrées reçues, la manière de générer des sorties (prédictions, contenu, recommandations ou décisions) susceptibles d'influencer des environnements physiques ou virtuels [1]. Si votre logiciel ne remplit pas ces critères techniques et fonctionnels précis, il ne relève pas de cette définition spécifique [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « 1) «système d’IA», un système automatisé qui est conçu pour fonctionner à différents niveaux d’autonomie et peut faire preuve d’une capacité d’adaptation après son déploiement, et qui, pour des objectifs explicites ou implicites, déduit, à partir des entrées qu’il reçoit, la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels; »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 3, définition 1 : Définitions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 3, définition 66 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
  [3] AI Act — règlement (UE) 2024/1689, annexe III, point 8 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [4] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 2 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [5] AI Act — règlement (UE) 2024/1689, article 6, paragraphe 1 bis : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « 1) «système d’IA», un système automatisé qui est conçu pour fonctionner à différents niveaux d’autonomie et peut faire preuve d’une capacité d’adaptation après son déploiement, et qui, pour des objectifs explicites ou implicites, déduit, à partir des entrées qu’il reçoit, la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels; »

RÉPONSE :
Pour déterminer si votre logiciel est un « système d'IA », il doit correspondre à la définition légale qui exige qu'il s'agisse d'un « système automatisé » conçu pour fonctionner à différents niveaux d'autonomie et capable de s'adapter après son déploiement [1]. De plus, le logiciel doit déduire, à partir des entrées reçues, la manière de générer des sorties (prédictions, contenu, recommandations ou décisions) susceptibles d'influencer des environnements physiques ou virtuels [1]. Si votre logiciel ne remplit pas ces critères techniques et fonctionnels précis, il ne relève pas de cette définition spécifique [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : système d'IA ; système d'intelligence artificielle ; composant d'IA ; modèle d'IA

Temps : recherche 24.3 s · génération 0.9 s (2085 tokens lus, 253 écrits, 453.8 tokens/s) · contrôle de pertinence 0.3 s · reformulation 0.2 s

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
  [4] RGPD — règlement (UE) 2016/679, article 4, définition 17 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [5] RGPD — règlement (UE) 2016/679, article 80 : Représentation des personnes concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_80

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun

RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : personne morale de droit privé ; objet social ; siège social ; organes de direction ; membres fondateurs ; dissolution

Temps : recherche 30.4 s · génération 0.4 s (2163 tokens lus, 25 écrits, 277.6 tokens/s) · reformulation 0.3 s
