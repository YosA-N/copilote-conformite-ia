# Réponses du copilote — heldout_v4_big_qwen27b

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 15/11/2026 à 17:13 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen/qwen3.8-27b` via l'API compatible OpenAI https://api.groq.com/openai/v1 (expérience de la séance 7, questions de test seulement ; modèle tel que servi par l'API à la date ci-dessus) — température 0.1, raisonnement : « none » (reasoning_effort), passages calculés pour un contexte de 8192 tokens comme en local, 2000 tokens au plus par réponse (raisonnement compris) ; le juge est le même modèle
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_v1.jsonl` (17 + 3 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q11 | Un client me demande d'effacer toutes ses données : suis-je obligé de le faire ? | 6/6 | non | — | 5 s |
| q12 | Un salarié demande une copie de toutes les données que nous avons sur lui : que dois-je lui donner ? | 5/6 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([2]) : ignoré(s). | 4 s |
| q13 | Un adhérent veut récupérer ses données pour les donner à une autre association : est-ce un droit ? | 4/4 | non | — | 4 s |
| q14 | Puis-je envoyer une lettre d'information par e-mail à mes adhérents, et peuvent-ils refuser ? | 6/6 | non | — | 4 s |
| q15 | Mon prestataire informatique a accès à nos fichiers : faut-il signer un contrat particulier ? | 6/6 | non | — | 4 s |
| q16 | Puis-je stocker les fichiers de mon association chez un hébergeur situé aux États-Unis ? | 6/6 | non | — | 5 s |
| q17 | Quelles sanctions risque une petite entreprise qui ne respecte pas le RGPD ? | 6/6 | non | — | 4 s |
| q18 | Notre association peut-elle collecter des informations sur la santé de ses bénévoles ? | 4/4 | non | — | 34 s |
| q19 | Qu'est-ce qu'une donnée personnelle ? | 3/3 | non | La réponse s'appuie sur le RGPD et l'AI Act sans dire de quel règlement vient chaque obligation : « Une donnée à caractère personnel est « toute information se rapportant à une personne physique identifiée ou … » (et 1 autre(s)). | 3 s |
| q20 | À partir de quel âge un enfant peut-il s'inscrire seul à notre service en ligne ? | 3/3 | non | — | 3 s |
| q21 | Comment dois-je protéger les données personnelles que nous conservons ? | 6/6 | non | — | 4 s |
| q22 | Le consentement d'une personne doit-il être donné par écrit ? | 3/3 | non | La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Non, le consentement ne doit pas obligatoirement être donné par écrit. ». Vérifiez ce point. | 4 s |
| q23 | Quelles utilisations de l'intelligence artificielle sont interdites en Europe ? | 6/6 | non | — | 6 s |
| q24 | Ai-je le droit d'utiliser une IA qui analyse les émotions de mes salariés ? | 6/6 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 5 s |
| q25 | Mon logiciel est-il un « système d'IA » au sens de la loi européenne ? | 1/1 | non | La réponse met entre « » un texte introuvable dans les extraits vérifiés : « déduire, à partir des entrées qu’il reçoit, la manière de générer des sorties telles que des prédictions, du contenu, … ». | 3 s |
| q26 | Dois-je indiquer qu'une image publiée sur notre site a été créée par une IA ? | 4/4 | non | La réponse met entre « » un texte introuvable dans les extraits vérifiés : « indiquez que les contenus ont été générés ou manipulés par une IA ». | 4 s |
| q27 | Quelles amendes prévoit le règlement européen sur l'intelligence artificielle ? | 9/9 | non | — | 5 s |
| h03 | Comment déclarer la création d'une association en préfecture ? | 0/0 | oui | — | 3 s |
| h04 | Quel est le montant du SMIC cette année ? | 0/0 | oui | — | 3 s |
| h05 | Comment rédiger les statuts d'une association ? | 0/0 | oui | — | 3 s |

## q11 — Un client me demande d'effacer toutes ses données : suis-je obligé de le faire ?

Article attendu : RGPD art. 17 — passage [1].

### Réponse du copilote

> Non, vous n'êtes pas obligé d'effacer toutes les données systématiquement ; l'effacement est obligatoire uniquement si l'un des motifs spécifiques prévus par le RGPD s'applique [1]. Vous devez effacer les données « dans les meilleurs délais » si, par exemple, elles « ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées » [1], ou si le client retire son consentement et qu'« il n'existe pas d'autre fondement juridique au traitement » [1]. L'effacement est également requis si le client s'oppose au traitement et qu'« il n'existe pas de motif légitime impérieux pour le traitement » [1], si les données ont fait l'objet d'un « traitement illicite » [1], ou si elles « doivent être effacées pour respecter une obligation légale » [1]. Si aucun de ces cas ne se présente, les passages fournis ne précisent pas d'autre obligation d'effacement immédiat.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit d'obtenir du responsable du traitement l'effacement, dans les meilleurs délais, de données à caractère personnel la concernant et le responsable du traitement a l'obligation d'effacer ces données à caractère personnel dans les meilleurs délais, lorsque l'un des motifs suivants s'applique: »
  [1] « a) les données à caractère personnel ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées d'une autre manière; »
  [1] « b) la personne concernée retire le consentement sur lequel est fondé le traitement, conformément à l'article 6, paragraphe 1, point a), ou à l'article 9, paragraphe 2, point a), et il n'existe pas d'autre fondement juridique au traitement; »
  [1] « c) la personne concernée s'oppose au traitement en vertu de l'article 21, paragraphe 1, et il n'existe pas de motif légitime impérieux pour le traitement, ou la personne concernée s'oppose au traitement en vertu de l'article 21, paragraphe 2; »
  [1] « d) les données à caractère personnel ont fait l'objet d'un traitement illicite; »
  [1] « e) les données à caractère personnel doivent être effacées pour respecter une obligation légale qui est prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis; »

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
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14

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

RÉPONSE :
Non, vous n'êtes pas obligé d'effacer toutes les données systématiquement ; l'effacement est obligatoire uniquement si l'un des motifs spécifiques prévus par le RGPD s'applique [1]. Vous devez effacer les données « dans les meilleurs délais » si, par exemple, elles « ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées » [1], ou si le client retire son consentement et qu'« il n'existe pas d'autre fondement juridique au traitement » [1]. L'effacement est également requis si le client s'oppose au traitement et qu'« il n'existe pas de motif légitime impérieux pour le traitement » [1], si les données ont fait l'objet d'un « traitement illicite » [1], ou si elles « doivent être effacées pour respecter une obligation légale » [1]. Si aucun de ces cas ne se présente, les passages fournis ne précisent pas d'autre obligation d'effacement immédiat.
```

</details>

Temps : recherche 2.6 s · génération 1.7 s (3231 tokens lus, 560 écrits, 478.8 tokens/s) · contrôle de pertinence 0.4 s · attente des limites de l'API 27 s (non comptée)

## q12 — Un salarié demande une copie de toutes les données que nous avons sur lui : que dois-je lui donner ?

Article attendu : RGPD art. 15 — passage [2].

### Réponse du copilote

> Vous devez fournir au salarié une copie des données à caractère personnel le concernant, ainsi que la confirmation que ces données sont traitées [2]. En plus de la copie, vous devez lui communiquer les informations suivantes : les finalités du traitement [2], les catégories de données concernées [2], les destinataires ou catégories de destinataires auxquels les données ont été ou seront communiquées [2], et, lorsque cela est possible, la durée de conservation envisagée ou les critères utilisés pour la déterminer [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: »
  [2] « b) les catégories de données à caractère personnel concernées; »
  [2] « c) les destinataires ou catégories de destinataires auxquels les données à caractère personnel ont été ou seront communiquées, en particulier les destinataires qui sont établis dans des pays tiers ou les organisations internationales; »
  [2] « d) lorsque cela est possible, la durée de conservation des données à caractère personnel envisagée ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; »
  [2] « Le responsable du traitement fournit une copie des données à caractère personnel faisant l'objet d'un traitement. »

Sources citées :
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [3] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [4] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([2]) : ignoré(s).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [2] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: »
- [2] « a) les finalités du traitement; »
- [2] « b) les catégories de données à caractère personnel concernées; »
- [2] « c) les destinataires ou catégories de destinataires auxquels les données à caractère personnel ont été ou seront communiquées, en particulier les destinataires qui sont établis dans des pays tiers ou les organisations internationales; »
- [2] « d) lorsque cela est possible, la durée de conservation des données à caractère personnel envisagée ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; »
- [2] « Le responsable du traitement fournit une copie des données à caractère personnel faisant l'objet d'un traitement. »

RÉPONSE :
Vous devez fournir au salarié une copie des données à caractère personnel le concernant, ainsi que la confirmation que ces données sont traitées [2]. En plus de la copie, vous devez lui communiquer les informations suivantes : les finalités du traitement [2], les catégories de données concernées [2], les destinataires ou catégories de destinataires auxquels les données ont été ou seront communiquées [2], et, lorsque cela est possible, la durée de conservation envisagée ou les critères utilisés pour la déterminer [2].
```

</details>

Temps : recherche 2.2 s · génération 1.2 s (3572 tokens lus, 328 écrits, 512.0 tokens/s) · contrôle de pertinence 0.2 s · attente des limites de l'API 24 s (non comptée)

## q13 — Un adhérent veut récupérer ses données pour les donner à une autre association : est-ce un droit ?

Article attendu : RGPD art. 20 — passage [1].

### Réponse du copilote

> Oui, c'est un droit, appelé droit à la portabilité des données, mais il est soumis à des conditions précises [1]. L'adhérent a le droit de transmettre ses données à un autre responsable du traitement, comme une autre association, sans que votre association puisse y faire obstacle [1]. Cependant, ce droit ne s'applique que si le traitement est fondé sur le consentement ou sur un contrat, et si le traitement est effectué à l'aide de procédés automatisés [1]. Si le traitement relève d'une mission d'intérêt public ou de l'exercice de l'autorité publique, ce droit ne s'applique pas [1].

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
  [3] RGPD — règlement (UE) 2016/679, article 16 : Droit de rectification
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_16
  [4] RGPD — règlement (UE) 2016/679, article 6, paragraphe 4 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
  [5] RGPD — règlement (UE) 2016/679, article 6, paragraphe 1 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6

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
Oui, c'est un droit, appelé droit à la portabilité des données, mais il est soumis à des conditions précises [1]. L'adhérent a le droit de transmettre ses données à un autre responsable du traitement, comme une autre association, sans que votre association puisse y faire obstacle [1]. Cependant, ce droit ne s'applique que si le traitement est fondé sur le consentement ou sur un contrat, et si le traitement est effectué à l'aide de procédés automatisés [1]. Si le traitement relève d'une mission d'intérêt public ou de l'exercice de l'autorité publique, ce droit ne s'applique pas [1].
```

</details>

Temps : recherche 2.2 s · génération 1.3 s (2695 tokens lus, 379 écrits, 471.3 tokens/s) · contrôle de pertinence 0.3 s · attente des limites de l'API 18 s (non comptée)

## q14 — Puis-je envoyer une lettre d'information par e-mail à mes adhérents, et peuvent-ils refuser ?

Article attendu : RGPD art. 21 ou RGPD art. 6, paragraphe 1 — passage [1].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question concernant la légalité de l'envoi d'une lettre d'information par e-mail (qui relève souvent de la directive ePrivacy et du consentement), mais ils précisent les droits d'opposition des adhérents. Si le traitement de leurs données pour l'envoi de cette lettre est fondé sur l'article 6, paragraphe 1, point e) ou f) du RGPD, l'adhérent a le droit de s'opposer « à tout moment, pour des raisons tenant à sa situation particulière » [1]. Dans ce cas, vous ne traitez plus les données « à moins qu'il ne démontre qu'il existe des motifs légitimes et impérieux pour le traitement qui prévalent sur les intérêts et les droits et libertés de la personne concernée, ou pour la constatation, l'exercice ou la défense de droits en justice » [1]. Si l'envoi est considéré comme une prospection, l'adhérent a le droit de s'opposer « à tout moment au traitement des données à caractère personnel la concernant à de telles fins de prospection » [1]. En cas d'opposition à des fins de prospection, « les données à caractère personnel ne sont plus traitées à ces fins » [1]. Vous devez porter ce droit à l'attention de l'adhérent « au plus tard au moment de la première communication avec la personne concernée » et le présenter « clairement et séparément de toute autre information » [1]. L'adhérent peut exercer ce droit « à l'aide de procédés automatisés utilisant des spécifications techniques » [1].

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
- [1] « Le responsable du traitement ne traite plus les données à caractère personnel, à moins qu'il ne démontre qu'il existe des motifs légitimes et impérieux pour le traitement qui prévalent sur les intérêts et les droits et libertés de la personne concernée, ou pour la constatation, l'exercice ou la défense de droits en justice. »
- [1] « Lorsque les données à caractère personnel sont traitées à des fins de prospection, la personne concernée a le droit de s'opposer à tout moment au traitement des données à caractère personnel la concernant à de telles fins de prospection, y compris au profilage dans la mesure où il est lié à une telle prospection. »
- [1] « Lorsque la personne concernée s'oppose au traitement à des fins de prospection, les données à caractère personnel ne sont plus traitées à ces fins. »
- [1] « Au plus tard au moment de la première communication avec la personne concernée, le droit visé aux paragraphes 1 et 2 est explicitement porté à l'attention de la personne concernée et est présenté clairement et séparément de toute autre information. »
- [1] « Dans le cadre de l'utilisation de services de la société de l'information, et nonobstant la directive 2002/58/CE, la personne concernée peut exercer son droit d'opposition à l'aide de procédés automatisés utilisant des spécifications techniques. »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question concernant la légalité de l'envoi d'une lettre d'information par e-mail (qui relève souvent de la directive ePrivacy et du consentement), mais ils précisent les droits d'opposition des adhérents. Si le traitement de leurs données pour l'envoi de cette lettre est fondé sur l'article 6, paragraphe 1, point e) ou f) du RGPD, l'adhérent a le droit de s'opposer « à tout moment, pour des raisons tenant à sa situation particulière » [1]. Dans ce cas, vous ne traitez plus les données « à moins qu'il ne démontre qu'il existe des motifs légitimes et impérieux pour le traitement qui prévalent sur les intérêts et les droits et libertés de la personne concernée, ou pour la constatation, l'exercice ou la défense de droits en justice » [1]. Si l'envoi est considéré comme une prospection, l'adhérent a le droit de s'opposer « à tout moment au traitement des données à caractère personnel la concernant à de telles fins de prospection » [1]. En cas d'opposition à des fins de prospection, « les données à caractère personnel ne sont plus traitées à ces fins » [1]. Vous devez porter ce droit à l'attention de l'adhérent « au plus tard au moment de la première communication avec la personne concernée » et le présenter « clairement et séparément de toute autre information » [1]. L'adhérent peut exercer ce droit « à l'aide de procédés automatisés utilisant des spécifications techniques » [1].
```

</details>

Temps : recherche 2.2 s · génération 2.0 s (2607 tokens lus, 752 écrits, 472.5 tokens/s) · contrôle de pertinence 0.3 s · attente des limites de l'API 51 s (non comptée)

## q15 — Mon prestataire informatique a accès à nos fichiers : faut-il signer un contrat particulier ?

Article attendu : RGPD art. 28, paragraphe 3 — passage [1].

### Réponse du copilote

> Oui, vous devez signer un contrat particulier avec votre prestataire informatique, car il agit en tant que sous-traitant [4]. En tant que responsable du traitement, vous devez vous assurer que ce sous-traitant présente des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées [2]. Le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique qui lie le sous-traitant à l'égard du responsable du traitement et définit l'objet, la durée, la nature et la finalité du traitement, ainsi que le type de données et les catégories de personnes concernées [1]. Ce contrat doit prévoir notamment que le sous-traitant ne traite les données que sur instruction documentée du responsable du traitement, sauf s'il est tenu d'y procéder en vertu du droit de l'Union ou du droit de l'État membre [1]. Il doit également prévoir que le sous-traitant veille à ce que les personnes autorisées à traiter les données s'engagent à respecter la confidentialité [1] et qu'il prend toutes les mesures requises en vertu de l'article 32 [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [4] « «sous-traitant», la personne physique ou morale, l'autorité publique, le service ou un autre organisme qui traite des données à caractère personnel pour le compte du responsable du traitement; »
  [2] « Lorsqu'un traitement doit être effectué pour le compte d'un responsable du traitement, celui-ci fait uniquement appel à des sous-traitants qui présentent des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées de manière à ce que le traitement réponde aux exigences du présent règlement et garantisse la protection des droits de la personne concernée. »
  [1] « Le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre, qui lie le sous-traitant à l'égard du responsable du traitement, définit l'objet et la durée du traitement, la nature et la finalité du traitement, le type de données à caractère personnel et les catégories de personnes concernées, et les obligations et les droits du responsable du traitement. »
  [1] « Ce contrat ou cet autre acte juridique prévoit, notamment, que le sous-traitant: a) ne traite les données à caractère personnel que sur instruction documentée du responsable du traitement, y compris en ce qui concerne les transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale, à moins qu'il ne soit tenu d'y procéder en vertu du droit de l'Union ou du droit de l'État membre auquel le sous-traitant est soumis; dans ce cas, le sous-traitant informe le responsable du traitement de cette obligation juridique avant le traitement, sauf si le droit concerné interdit une telle information pour des motifs importants d'intérêt public; »
  [1] « b) veille à ce que les personnes autorisées à traiter les données à caractère personnel s'engagent à respecter la confidentialité ou soient soumises à une obligation légale appropriée de confidentialité; »
  [1] « c) prend toutes les mesures requises en vertu de l'article 32; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 28, paragraphe 3 : Sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [2] RGPD — règlement (UE) 2016/679, article 28, paragraphe 1 : Sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [4] RGPD — règlement (UE) 2016/679, article 4, définition 8 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 29 : Traitement effectué sous l'autorité du responsable du traitement ou du sous-traitant
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_29
  [5] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [4] « «sous-traitant», la personne physique ou morale, l'autorité publique, le service ou un autre organisme qui traite des données à caractère personnel pour le compte du responsable du traitement; »
- [2] « Lorsqu'un traitement doit être effectué pour le compte d'un responsable du traitement, celui-ci fait uniquement appel à des sous-traitants qui présentent des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées de manière à ce que le traitement réponde aux exigences du présent règlement et garantisse la protection des droits de la personne concernée. »
- [1] « Le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre, qui lie le sous-traitant à l'égard du responsable du traitement, définit l'objet et la durée du traitement, la nature et la finalité du traitement, le type de données à caractère personnel et les catégories de personnes concernées, et les obligations et les droits du responsable du traitement. »
- [1] « Ce contrat ou cet autre acte juridique prévoit, notamment, que le sous-traitant: a) ne traite les données à caractère personnel que sur instruction documentée du responsable du traitement, y compris en ce qui concerne les transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale, à moins qu'il ne soit tenu d'y procéder en vertu du droit de l'Union ou du droit de l'État membre auquel le sous-traitant est soumis; dans ce cas, le sous-traitant informe le responsable du traitement de cette obligation juridique avant le traitement, sauf si le droit concerné interdit une telle information pour des motifs importants d'intérêt public; »
- [1] « b) veille à ce que les personnes autorisées à traiter les données à caractère personnel s'engagent à respecter la confidentialité ou soient soumises à une obligation légale appropriée de confidentialité; »
- [1] « c) prend toutes les mesures requises en vertu de l'article 32; »

RÉPONSE :
Oui, vous devez signer un contrat particulier avec votre prestataire informatique, car il agit en tant que sous-traitant [4]. En tant que responsable du traitement, vous devez vous assurer que ce sous-traitant présente des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées [2]. Le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique qui lie le sous-traitant à l'égard du responsable du traitement et définit l'objet, la durée, la nature et la finalité du traitement, ainsi que le type de données et les catégories de personnes concernées [1]. Ce contrat doit prévoir notamment que le sous-traitant ne traite les données que sur instruction documentée du responsable du traitement, sauf s'il est tenu d'y procéder en vertu du droit de l'Union ou du droit de l'État membre [1]. Il doit également prévoir que le sous-traitant veille à ce que les personnes autorisées à traiter les données s'engagent à respecter la confidentialité [1] et qu'il prend toutes les mesures requises en vertu de l'article 32 [1].
```

</details>

Temps : recherche 2.2 s · génération 1.7 s (2760 tokens lus, 697 écrits, 489.5 tokens/s) · contrôle de pertinence 0.5 s · attente des limites de l'API 37 s (non comptée)

## q16 — Puis-je stocker les fichiers de mon association chez un hébergeur situé aux États-Unis ?

Article attendu : RGPD art. 44 ou RGPD art. 45, paragraphe 1 ou RGPD art. 46 — passage [1].

### Réponse du copilote

> Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, à condition de respecter les règles du RGPD concernant les transferts de données vers un pays tiers [3].
> Le stockage chez un hébergeur américain constitue un transfert de données à caractère personnel vers un pays tiers [3].
> Ce transfert est autorisé si la Commission européenne a constaté que le pays tiers assure un niveau de protection adéquat, auquel cas « Un tel transfert ne nécessite pas d'autorisation spécifique » [1].
> À défaut de cette décision d'adéquation, le responsable du traitement (votre association) ou le sous-traitant (l'hébergeur) « ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives » [2].
> Parmi ces garanties appropriées, qui peuvent être fournies « sans que cela ne nécessite une autorisation particulière d'une autorité de contrôle », figurent notamment « des clauses types de protection des données adoptées par la Commission » [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « Un transfert, vers un pays tiers ou à une organisation internationale, de données à caractère personnel qui font ou sont destinées à faire l'objet d'un traitement après ce transfert ne peut avoir lieu que si, sous réserve des autres dispositions du présent règlement, les conditions définies dans le présent chapitre sont respectées par le responsable du traitement et le sous-traitant, y compris pour les transferts ultérieurs de données à caractère personnel au départ du pays tiers ou de l'organisation internationale vers un autre pays tiers ou à une autre organisation internationale. »
  [1] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. »
  [1] « Un tel transfert ne nécessite pas d'autorisation spécifique. »
  [2] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
  [2] « Les garanties appropriées visées au paragraphe 1 peuvent être fournies, sans que cela ne nécessite une autorisation particulière d'une autorité de contrôle, par: »
  [2] « c) des clauses types de protection des données adoptées par la Commission en conformité avec la procédure d'examen visée à l'article 93, paragraphe 2; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 45, paragraphe 1 : Transferts fondés sur une décision d'adéquation (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
  [2] RGPD — règlement (UE) 2016/679, article 46 : Transferts moyennant des garanties appropriées (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_46
  [3] RGPD — règlement (UE) 2016/679, article 44 : Principe général applicable aux transferts (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_44
Passages consultés mais non cités :
  [4] RGPD — règlement (UE) 2016/679, article 48 : Transferts ou divulgations non autorisés par le droit de l'Union
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_48
  [5] RGPD — règlement (UE) 2016/679, article 45, paragraphe 2 : Transferts fondés sur une décision d'adéquation
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [3] « Un transfert, vers un pays tiers ou à une organisation internationale, de données à caractère personnel qui font ou sont destinées à faire l'objet d'un traitement après ce transfert ne peut avoir lieu que si, sous réserve des autres dispositions du présent règlement, les conditions définies dans le présent chapitre sont respectées par le responsable du traitement et le sous-traitant, y compris pour les transferts ultérieurs de données à caractère personnel au départ du pays tiers ou de l'organisation internationale vers un autre pays tiers ou à une autre organisation internationale. »
- [1] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. »
- [1] « Un tel transfert ne nécessite pas d'autorisation spécifique. »
- [2] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
- [2] « Les garanties appropriées visées au paragraphe 1 peuvent être fournies, sans que cela ne nécessite une autorisation particulière d'une autorité de contrôle, par: »
- [2] « c) des clauses types de protection des données adoptées par la Commission en conformité avec la procédure d'examen visée à l'article 93, paragraphe 2; »

RÉPONSE :
Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, à condition de respecter les règles du RGPD concernant les transferts de données vers un pays tiers [3].
Le stockage chez un hébergeur américain constitue un transfert de données à caractère personnel vers un pays tiers [3].
Ce transfert est autorisé si la Commission européenne a constaté que le pays tiers assure un niveau de protection adéquat, auquel cas « Un tel transfert ne nécessite pas d'autorisation spécifique » [1].
À défaut de cette décision d'adéquation, le responsable du traitement (votre association) ou le sous-traitant (l'hébergeur) « ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives » [2].
Parmi ces garanties appropriées, qui peuvent être fournies « sans que cela ne nécessite une autorisation particulière d'une autorité de contrôle », figurent notamment « des clauses types de protection des données adoptées par la Commission » [2].
```

</details>

Temps : recherche 2.2 s · génération 2.0 s (2637 tokens lus, 639 écrits, 464.2 tokens/s) · contrôle de pertinence 0.4 s · attente des limites de l'API 27 s (non comptée)

## q17 — Quelles sanctions risque une petite entreprise qui ne respecte pas le RGPD ?

Article attendu : RGPD art. 83, paragraphe 4 ou RGPD art. 83, paragraphe 5 — passage [1].

### Réponse du copilote

> Une petite entreprise qui ne respecte pas le RGPD risque des amendes administratives dont le montant dépend de la nature de la violation. Pour les violations des obligations incombant au responsable du traitement et au sous-traitant en vertu des articles 8, 11, 25 à 39, 42 et 43, l'amende peut s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [1]. Pour les violations des principes de base d'un traitement, y compris les conditions applicables au consentement en vertu des articles 5, 6, 7 et 9, l'amende peut s'élever jusqu'à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [3]. Cette même catégorie d'amende s'applique également aux violations des droits dont bénéficient les personnes concernées en vertu des articles 12 à 22 [3] et aux violations concernant les transferts de données à caractère personnel à un destinataire situé dans un pays tiers ou à une organisation internationale en vertu des articles 44 à 49 [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »
  [1] « a) les obligations incombant au responsable du traitement et au sous-traitant en vertu des articles 8, 11, 25 à 39, 42 et 43; »
  [3] « Les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »
  [3] « a) les principes de base d'un traitement, y compris les conditions applicables au consentement en vertu des articles 5, 6, 7 et 9; »
  [3] « b) les droits dont bénéficient les personnes concernées en vertu des articles 12 à 22 »
  [3] « c) les transferts de données à caractère personnel à un destinataire situé dans un pays tiers ou à une organisation internationale en vertu des articles 44 à 49; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 83, paragraphe 4 : Conditions générales pour imposer des amendes administratives (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83
  [3] RGPD — règlement (UE) 2016/679, article 83, paragraphe 5 : Conditions générales pour imposer des amendes administratives (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 83, paragraphe 1 : Conditions générales pour imposer des amendes administratives
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83
  [4] RGPD — règlement (UE) 2016/679, article 84 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_84
  [5] RGPD — règlement (UE) 2016/679, article 58, paragraphe 2 : Pouvoirs
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_58

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »
- [1] « a) les obligations incombant au responsable du traitement et au sous-traitant en vertu des articles 8, 11, 25 à 39, 42 et 43; »
- [3] « Les violations des dispositions suivantes font l'objet, conformément au paragraphe 2, d'amendes administratives pouvant s'élever jusqu'à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu: »
- [3] « a) les principes de base d'un traitement, y compris les conditions applicables au consentement en vertu des articles 5, 6, 7 et 9; »
- [3] « b) les droits dont bénéficient les personnes concernées en vertu des articles 12 à 22 »
- [3] « c) les transferts de données à caractère personnel à un destinataire situé dans un pays tiers ou à une organisation internationale en vertu des articles 44 à 49; »

RÉPONSE :
Une petite entreprise qui ne respecte pas le RGPD risque des amendes administratives dont le montant dépend de la nature de la violation. Pour les violations des obligations incombant au responsable du traitement et au sous-traitant en vertu des articles 8, 11, 25 à 39, 42 et 43, l'amende peut s'élever jusqu'à 10 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 2 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [1]. Pour les violations des principes de base d'un traitement, y compris les conditions applicables au consentement en vertu des articles 5, 6, 7 et 9, l'amende peut s'élever jusqu'à 20 000 000 EUR ou, dans le cas d'une entreprise, jusqu'à 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent, le montant le plus élevé étant retenu [3]. Cette même catégorie d'amende s'applique également aux violations des droits dont bénéficient les personnes concernées en vertu des articles 12 à 22 [3] et aux violations concernant les transferts de données à caractère personnel à un destinataire situé dans un pays tiers ou à une organisation internationale en vertu des articles 44 à 49 [3].
```

</details>

Temps : recherche 2.2 s · génération 1.9 s (2272 tokens lus, 650 écrits, 445.2 tokens/s) · contrôle de pertinence 0.4 s · attente des limites de l'API 42 s (non comptée)

## q18 — Notre association peut-elle collecter des informations sur la santé de ses bénévoles ?

Article attendu : RGPD art. 9, paragraphe 1 ou RGPD art. 9, paragraphe 2 — passage [2].

### Réponse du copilote

> En principe, non : le traitement des données concernant la santé est interdit [2]. Ces données sont définies comme celles relatives à la santé physique ou mentale d'une personne physique [3]. Une exception existe si les données sont traitées par un professionnel de la santé soumis à une obligation de secret professionnel, ou par une autre personne également soumise à une obligation de secret [1]. De plus, les États membres peuvent introduire des conditions supplémentaires ou des limitations concernant ce type de données [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « Le traitement des données à caractère personnel qui révèle l'origine raciale ou ethnique, les opinions politiques, les convictions religieuses ou philosophiques ou l'appartenance syndicale, ainsi que le traitement des données génétiques, des données biométriques aux fins d'identifier une personne physique de manière unique, des données concernant la santé ou des données concernant la vie sexuelle ou l'orientation sexuelle d'une personne physique sont interdits. »
  [3] « «données concernant la santé», les données à caractère personnel relatives à la santé physique ou mentale d'une personne physique, y compris la prestation de services de soins de santé, qui révèlent des informations sur l'état de santé de cette personne; »
  [1] « Les données à caractère personnel visées au paragraphe 1 peuvent faire l'objet d'un traitement aux fins prévues au paragraphe 2, point h), si ces données sont traitées par un professionnel de la santé soumis à une obligation de secret professionnel conformément au droit de l'Union, au droit d'un État membre ou aux règles arrêtées par les organismes nationaux compétents, ou sous sa responsabilité, ou par une autre personne également soumise à une obligation de secret conformément au droit de l'Union ou au droit d'un État membre ou aux règles arrêtées par les organismes nationaux compétents. »
  [4] « Les États membres peuvent maintenir ou introduire des conditions supplémentaires, y compris des limitations, en ce qui concerne le traitement des données génétiques, des données biométriques ou des données concernant la santé. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 9, paragraphe 3 : Traitement portant sur des catégories particulières de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
  [2] RGPD — règlement (UE) 2016/679, article 9, paragraphe 1 : Traitement portant sur des catégories particulières de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 15 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [4] RGPD — règlement (UE) 2016/679, article 9, paragraphe 4 : Traitement portant sur des catégories particulières de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
Passages consultés mais non cités :
  [5] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [2] « Le traitement des données à caractère personnel qui révèle l'origine raciale ou ethnique, les opinions politiques, les convictions religieuses ou philosophiques ou l'appartenance syndicale, ainsi que le traitement des données génétiques, des données biométriques aux fins d'identifier une personne physique de manière unique, des données concernant la santé ou des données concernant la vie sexuelle ou l'orientation sexuelle d'une personne physique sont interdits. »
- [3] « «données concernant la santé», les données à caractère personnel relatives à la santé physique ou mentale d'une personne physique, y compris la prestation de services de soins de santé, qui révèlent des informations sur l'état de santé de cette personne; »
- [1] « Les données à caractère personnel visées au paragraphe 1 peuvent faire l'objet d'un traitement aux fins prévues au paragraphe 2, point h), si ces données sont traitées par un professionnel de la santé soumis à une obligation de secret professionnel conformément au droit de l'Union, au droit d'un État membre ou aux règles arrêtées par les organismes nationaux compétents, ou sous sa responsabilité, ou par une autre personne également soumise à une obligation de secret conformément au droit de l'Union ou au droit d'un État membre ou aux règles arrêtées par les organismes nationaux compétents. »
- [4] « Les États membres peuvent maintenir ou introduire des conditions supplémentaires, y compris des limitations, en ce qui concerne le traitement des données génétiques, des données biométriques ou des données concernant la santé. »

RÉPONSE :
En principe, non : le traitement des données concernant la santé est interdit [2]. Ces données sont définies comme celles relatives à la santé physique ou mentale d'une personne physique [3]. Une exception existe si les données sont traitées par un professionnel de la santé soumis à une obligation de secret professionnel, ou par une autre personne également soumise à une obligation de secret [1]. De plus, les États membres peuvent introduire des conditions supplémentaires ou des limitations concernant ce type de données [4].
```

</details>

Temps : recherche 2.2 s · génération 31.5 s (2347 tokens lus, 442 écrits, 461.7 tokens/s) · contrôle de pertinence 0.3 s · attente des limites de l'API 31 s (non comptée)

## q19 — Qu'est-ce qu'une donnée personnelle ?

Article attendu : RGPD art. 4, définition 1 — passage [1].

### Réponse du copilote

> Une donnée à caractère personnel est « toute information se rapportant à une personne physique identifiée ou identifiable » [1]. Cette définition s'applique également dans le cadre de l'AI Act, qui renvoie à la définition du RGPD [3]. Une personne est considérée comme identifiable si elle peut être identifiée « directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « «données à caractère personnel», toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée»); »
  [1] « est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale; »
  [3] « «données à caractère personnel», les données à caractère personnel définies à l’article 4, point 1), du règlement (UE) 2016/679; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 4, définition 1 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [3] AI Act — règlement (UE) 2024/1689, article 3, définition 50 : Définitions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
  [4] RGPD — règlement (UE) 2016/679, article 4, définition 14 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [5] AI Act — règlement (UE) 2024/1689, article 3, définition 34 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
Attention : La réponse s'appuie sur le RGPD et l'AI Act sans dire de quel règlement vient chaque obligation : « Une donnée à caractère personnel est « toute information se rapportant à une personne physique identifiée ou … » (et 1 autre(s)).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « «données à caractère personnel», toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée»); »
- [1] « est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale; »
- [3] « «données à caractère personnel», les données à caractère personnel définies à l’article 4, point 1), du règlement (UE) 2016/679; »

RÉPONSE :
Une donnée à caractère personnel est « toute information se rapportant à une personne physique identifiée ou identifiable » [1]. Cette définition s'applique également dans le cadre de l'AI Act, qui renvoie à la définition du RGPD [3]. Une personne est considérée comme identifiable si elle peut être identifiée « directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale » [1].
```

</details>

Temps : recherche 2.2 s · génération 0.9 s (1979 tokens lus, 324 écrits, 488.3 tokens/s) · contrôle de pertinence 0.4 s · attente des limites de l'API 17 s (non comptée)

## q20 — À partir de quel âge un enfant peut-il s'inscrire seul à notre service en ligne ?

Article attendu : RGPD art. 8 — passage [1].

### Réponse du copilote

> En principe, un enfant peut s'inscrire seul à votre service en ligne à partir de 16 ans, car le traitement de ses données est licite « lorsque l'enfant est âgé d'au moins 16 ans » [1].
> Si l'enfant a moins de 16 ans, il ne peut pas s'inscrire seul : le consentement doit être « donné ou autorisé par le titulaire de la responsabilité parentale à l'égard de l'enfant » [1].
> Cependant, l'âge minimal peut être abaissé par la loi de votre pays, mais « pour autant que cet âge inférieur ne soit pas en-dessous de 13 ans » [1].

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
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [3] RGPD — règlement (UE) 2016/679, article 57, paragraphe 1, points a) à t) : Missions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_57
  [4] AI Act — règlement (UE) 2024/1689, article 58, paragraphe 2 : Modalités détaillées pour les bacs à sable réglementaires de l’IA et fonctionnement de ceux-ci
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_58
  [5] AI Act — règlement (UE) 2024/1689, article 58, paragraphe 1 : Modalités détaillées pour les bacs à sable réglementaires de l’IA et fonctionnement de ceux-ci
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_58

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « le traitement des données à caractère personnel relatives à un enfant est licite lorsque l'enfant est âgé d'au moins 16 ans. »
- [1] « Lorsque l'enfant est âgé de moins de 16 ans, ce traitement n'est licite que si, et dans la mesure où, le consentement est donné ou autorisé par le titulaire de la responsabilité parentale à l'égard de l'enfant. »
- [1] « Les États membres peuvent prévoir par la loi un âge inférieur pour ces finalités pour autant que cet âge inférieur ne soit pas en-dessous de 13 ans. »

RÉPONSE :
En principe, un enfant peut s'inscrire seul à votre service en ligne à partir de 16 ans, car le traitement de ses données est licite « lorsque l'enfant est âgé d'au moins 16 ans » [1].
Si l'enfant a moins de 16 ans, il ne peut pas s'inscrire seul : le consentement doit être « donné ou autorisé par le titulaire de la responsabilité parentale à l'égard de l'enfant » [1].
Cependant, l'âge minimal peut être abaissé par la loi de votre pays, mais « pour autant que cet âge inférieur ne soit pas en-dessous de 13 ans » [1].
```

</details>

Temps : recherche 2.1 s · génération 1.1 s (3619 tokens lus, 293 écrits, 478.0 tokens/s) · contrôle de pertinence 0.3 s · attente des limites de l'API 14 s (non comptée)

## q21 — Comment dois-je protéger les données personnelles que nous conservons ?

Article attendu : RGPD art. 32 — passage [1].

### Réponse du copilote

> Pour protéger les données personnelles que vous conservez, vous devez, en tant que responsable du traitement, mettre en œuvre des mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque [1].
> Ces mesures incluent, selon les besoins :
> a) la pseudonymisation et le chiffrement des données à caractère personnel [1] ;
> b) des moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement [1] ;
> c) des moyens permettant de rétablir la disponibilité des données à caractère personnel et l'accès à celles-ci dans des délais appropriés en cas d'incident physique ou technique [1] ;
> d) une procédure visant à tester, à analyser et à évaluer régulièrement l'efficacité des mesures techniques et organisationnelles pour assurer la sécurité du traitement [1].
> Par ailleurs, vous devez conserver les données sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées [3].

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
  [5] RGPD — règlement (UE) 2016/679, article 98 : Réexamen d'autres actes juridiques de l'Union relatifs à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_98

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
Pour protéger les données personnelles que vous conservez, vous devez, en tant que responsable du traitement, mettre en œuvre des mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque [1].
Ces mesures incluent, selon les besoins :
a) la pseudonymisation et le chiffrement des données à caractère personnel [1] ;
b) des moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement [1] ;
c) des moyens permettant de rétablir la disponibilité des données à caractère personnel et l'accès à celles-ci dans des délais appropriés en cas d'incident physique ou technique [1] ;
d) une procédure visant à tester, à analyser et à évaluer régulièrement l'efficacité des mesures techniques et organisationnelles pour assurer la sécurité du traitement [1].
Par ailleurs, vous devez conserver les données sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées [3].
```

</details>

Temps : recherche 2.2 s · génération 1.4 s (2786 tokens lus, 480 écrits, 493.9 tokens/s) · contrôle de pertinence 0.3 s · attente des limites de l'API 25 s (non comptée)

## q22 — Le consentement d'une personne doit-il être donné par écrit ?

Article attendu : RGPD art. 7 — passage [1].

### Réponse du copilote

> Non, le consentement ne doit pas obligatoirement être donné par écrit. Selon le RGPD, le consentement est défini comme une manifestation de volonté acceptée « par une déclaration ou par un acte positif clair » [3]. L'article 7 du RGPD précise seulement que si le consentement est donné « dans le cadre d'une déclaration écrite qui concerne également d'autres questions », il doit être distingué clairement de ces autres questions [1]. En revanche, pour les essais en conditions réelles visés par l'AI Act, le consentement éclairé « est daté et documenté » [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « «consentement» de la personne concernée, toute manifestation de volonté, libre, spécifique, éclairée et univoque par laquelle la personne concernée accepte, par une déclaration ou par un acte positif clair, que des données à caractère personnel la concernant fassent l'objet d'un traitement; »
  [1] « Si le consentement de la personne concernée est donné dans le cadre d'une déclaration écrite qui concerne également d'autres questions, la demande de consentement est présentée sous une forme qui la distingue clairement de ces autres questions, sous une forme compréhensible et aisément accessible, et formulée en des termes clairs et simples. »
  [2] « Le consentement éclairé est daté et documenté et une copie en est remise aux participants aux essais ou à leur représentant légal. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 7 : Conditions applicables au consentement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_7
  [2] AI Act — règlement (UE) 2024/1689, article 61 : Consentement éclairé à participer aux essais en conditions réelles en dehors des bacs à sable réglementaires de l’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_61
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 11 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
Passages consultés mais non cités :
  [4] AI Act — règlement (UE) 2024/1689, article 3, définition 59 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
  [5] RGPD — règlement (UE) 2016/679, article 8 : Conditions applicables au consentement des enfants en ce qui concerne les services de la société de l'information
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_8
Attention : La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Non, le consentement ne doit pas obligatoirement être donné par écrit. ». Vérifiez ce point.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [3] « «consentement» de la personne concernée, toute manifestation de volonté, libre, spécifique, éclairée et univoque par laquelle la personne concernée accepte, par une déclaration ou par un acte positif clair, que des données à caractère personnel la concernant fassent l'objet d'un traitement; »
- [1] « Si le consentement de la personne concernée est donné dans le cadre d'une déclaration écrite qui concerne également d'autres questions, la demande de consentement est présentée sous une forme qui la distingue clairement de ces autres questions, sous une forme compréhensible et aisément accessible, et formulée en des termes clairs et simples. »
- [2] « Le consentement éclairé est daté et documenté et une copie en est remise aux participants aux essais ou à leur représentant légal. »

RÉPONSE :
Non, le consentement ne doit pas obligatoirement être donné par écrit. Selon le RGPD, le consentement est défini comme une manifestation de volonté acceptée « par une déclaration ou par un acte positif clair » [3]. L'article 7 du RGPD précise seulement que si le consentement est donné « dans le cadre d'une déclaration écrite qui concerne également d'autres questions », il doit être distingué clairement de ces autres questions [1]. En revanche, pour les essais en conditions réelles visés par l'AI Act, le consentement éclairé « est daté et documenté » [2].
```

</details>

Temps : recherche 2.2 s · génération 1.0 s (2194 tokens lus, 308 écrits, 477.1 tokens/s) · contrôle de pertinence 0.3 s · attente des limites de l'API 16 s (non comptée)

## q23 — Quelles utilisations de l'intelligence artificielle sont interdites en Europe ?

Article attendu : AI Act art. 5, paragraphe 1 — passage [1].

### Réponse du copilote

> L’AI Act interdit plusieurs pratiques spécifiques en matière d’intelligence artificielle, énumérées à l’article 5.
> Sont interdits les systèmes qui utilisent des techniques subliminales ou manipulatrices pour altérer le comportement d’une personne et causer un préjudice important [2].
> Il est également interdit d’exploiter les vulnérabilités d’une personne (liées à l’âge, au handicap ou à la situation sociale) pour altérer son comportement et causer un préjudice [2].
> La génération ou la manipulation de contenus réalistes représentant des parties intimes ou des activités sexuellement explicites sans le consentement explicite de la personne est interdite [2].
> L’évaluation ou la classification de personnes (social scoring) est interdite si elle conduit à un traitement préjudiciable ou disproportionné [2].
> L’inférence des émotions d’une personne sur le lieu de travail ou dans les établissements d’enseignement est interdite, « sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité » [1].
> Enfin, la catégorisation biométrique visant à déduire la race, les opinions politiques, l’affiliation syndicale, les convictions religieuses ou l’orientation sexuelle est interdite [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « a) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui a recours à des techniques subliminales, au-dessous du seuil de conscience d’une personne, ou à des techniques délibérément manipulatrices ou trompeuses, avec pour objectif ou effet d’altérer substantiellement le comportement d’une personne ou d’un groupe de personnes en portant considérablement atteinte à leur capacité à prendre une décision éclairée, amenant ainsi la personne à prendre une décision qu’elle n’aurait pas prise autrement, d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne, à une autre personne ou à un groupe de personnes; »
  [2] « b) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui exploite les éventuelles vulnérabilités dues à l’âge, au handicap ou à la situation sociale ou économique spécifique d’une personne physique ou d’un groupe de personnes donné avec pour objectif ou effet d’altérer substantiellement le comportement de cette personne ou d’un membre de ce groupe d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne ou à un tiers; »
  [2] « b bis) la mise sur le marché, la mise en service ou l'utilisation d'un système d'IA qui génère ou manipule des images, des vidéos, des contenus audio ou tout autre matériel similaire réalistes représentant les parties intimes d'une personne identifiable, ou une personne identifiable se livrant à des activités sexuellement explicites, sans le consentement libre, spécifique, éclairé, univoque et explicite de cette personne pour cette production ou manipulation; »
  [2] « c) la mise sur le marché, la mise en service ou l’utilisation de systèmes d’IA pour l’évaluation ou la classification de personnes physiques ou de groupes de personnes au cours d’une période donnée en fonction de leur comportement social ou de caractéristiques personnelles ou de personnalité connues, déduites ou prédites, la note sociale conduisant à l’une ou l’autre des situations suivantes, ou aux deux: »
  [1] « f) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement, sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité; »
  [1] « g) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes de catégorisation biométrique qui catégorisent individuellement les personnes physiques sur la base de leurs données biométriques afin d’arriver à des déductions ou des inférences concernant leur race, leurs opinions politiques, leur affiliation à une organisation syndicale, leurs convictions religieuses ou philosophiques, leur vie sexuelle ou leur orientation sexuelle; »

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

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [2] « a) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui a recours à des techniques subliminales, au-dessous du seuil de conscience d’une personne, ou à des techniques délibérément manipulatrices ou trompeuses, avec pour objectif ou effet d’altérer substantiellement le comportement d’une personne ou d’un groupe de personnes en portant considérablement atteinte à leur capacité à prendre une décision éclairée, amenant ainsi la personne à prendre une décision qu’elle n’aurait pas prise autrement, d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne, à une autre personne ou à un groupe de personnes; »
- [2] « b) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui exploite les éventuelles vulnérabilités dues à l’âge, au handicap ou à la situation sociale ou économique spécifique d’une personne physique ou d’un groupe de personnes donné avec pour objectif ou effet d’altérer substantiellement le comportement de cette personne ou d’un membre de ce groupe d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne ou à un tiers; »
- [2] « b bis) la mise sur le marché, la mise en service ou l'utilisation d'un système d'IA qui génère ou manipule des images, des vidéos, des contenus audio ou tout autre matériel similaire réalistes représentant les parties intimes d'une personne identifiable, ou une personne identifiable se livrant à des activités sexuellement explicites, sans le consentement libre, spécifique, éclairé, univoque et explicite de cette personne pour cette production ou manipulation; »
- [2] « c) la mise sur le marché, la mise en service ou l’utilisation de systèmes d’IA pour l’évaluation ou la classification de personnes physiques ou de groupes de personnes au cours d’une période donnée en fonction de leur comportement social ou de caractéristiques personnelles ou de personnalité connues, déduites ou prédites, la note sociale conduisant à l’une ou l’autre des situations suivantes, ou aux deux: »
- [1] « f) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement, sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité; »
- [1] « g) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes de catégorisation biométrique qui catégorisent individuellement les personnes physiques sur la base de leurs données biométriques afin d’arriver à des déductions ou des inférences concernant leur race, leurs opinions politiques, leur affiliation à une organisation syndicale, leurs convictions religieuses ou philosophiques, leur vie sexuelle ou leur orientation sexuelle; »

RÉPONSE :
L’AI Act interdit plusieurs pratiques spécifiques en matière d’intelligence artificielle, énumérées à l’article 5.
Sont interdits les systèmes qui utilisent des techniques subliminales ou manipulatrices pour altérer le comportement d’une personne et causer un préjudice important [2].
Il est également interdit d’exploiter les vulnérabilités d’une personne (liées à l’âge, au handicap ou à la situation sociale) pour altérer son comportement et causer un préjudice [2].
La génération ou la manipulation de contenus réalistes représentant des parties intimes ou des activités sexuellement explicites sans le consentement explicite de la personne est interdite [2].
L’évaluation ou la classification de personnes (social scoring) est interdite si elle conduit à un traitement préjudiciable ou disproportionné [2].
L’inférence des émotions d’une personne sur le lieu de travail ou dans les établissements d’enseignement est interdite, « sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité » [1].
Enfin, la catégorisation biométrique visant à déduire la race, les opinions politiques, l’affiliation syndicale, les convictions religieuses ou l’orientation sexuelle est interdite [1].
```

</details>

Temps : recherche 2.2 s · génération 2.4 s (3494 tokens lus, 959 écrits, 472.5 tokens/s) · contrôle de pertinence 1.1 s · attente des limites de l'API 53 s (non comptée)

## q24 — Ai-je le droit d'utiliser une IA qui analyse les émotions de mes salariés ?

Article attendu : AI Act art. 5, paragraphe 1_f h — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 3 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [2] AI Act — règlement (UE) 2024/1689, article 3, définition 39 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
  [3] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [4] AI Act — règlement (UE) 2024/1689, article 86 : Droit à l’explication des décisions individuelles
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_86
  [5] AI Act — règlement (UE) 2024/1689, annexe III, point 5 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les déployeurs d’un système de reconnaissance des émotions ou d’un système de catégorisation biométrique informent les personnes physiques qui y sont exposées du fonctionnement du système et traitent les données à caractère personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680, selon le cas. »
- [1] « Cette obligation ne s’applique pas aux systèmes d’IA utilisés pour la catégorisation biométrique et la reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l’Union. »
- [2] « «système de reconnaissance des émotions», un système d’IA permettant la reconnaissance ou la déduction des émotions ou des intentions de personnes physiques sur la base de leurs données biométriques; »
- [3] « a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »
- [3] « b) systèmes d'IA destinés à être utilisés pour prendre des décisions influant sur les conditions des relations professionnelles, la promotion ou le licenciement dans le cadre de relations professionnelles contractuelles, pour attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques personnelles ou pour suivre et évaluer les performances et le comportement de personnes dans le cadre de telles relations. »
- [4] « Toute personne concernée faisant l’objet d’une décision prise par un déployeur sur la base des sorties d’un système d’IA à haut risque mentionné à l’annexe III, à l’exception des systèmes énumérés au point 2 de ladite annexe, et qui produit des effets juridiques ou affecte significativement cette personne de façon similaire d’une manière qu’elle considère comme ayant des conséquences négatives sur sa santé, sa sécurité ou ses droits fondamentaux a le droit d’obtenir du déployeur des explications claires et pertinentes sur le rôle du système d’IA dans la procédure décisionnelle et sur les principaux éléments de la décision prise. »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question, car ils ne précisent pas si l'utilisation d'une IA d'analyse des émotions est interdite ou autorisée dans le contexte spécifique de la gestion des salariés, mais ils définissent les obligations applicables si vous déployez un tel système.
Un système qui déduit les émotions à partir de données biométriques est défini comme un « système de reconnaissance des émotions » [2].
En tant que déployeur, vous devez informer les personnes exposées du fonctionnement du système et traiter les données conformément au RGPD [1].
Cette obligation d'information ne s'applique pas « aux systèmes d’IA utilisés pour la catégorisation biométrique et la reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l’Union » [1].
Si votre système est utilisé pour le recrutement, la sélection, ou pour prendre des décisions influant sur les conditions de travail, la promotion, le licenciement, ou pour suivre et évaluer les performances et le comportement, il est classé comme un système d'IA à haut risque [3].
Dans ce cas, les salariés concernés ont le droit d'obtenir des explications claires et pertinentes sur le rôle du système dans la décision qui les concerne [4].
```

</details>

Temps : recherche 2.2 s · génération 2.2 s (2199 tokens lus, 844 écrits, 464.8 tokens/s) · contrôle de pertinence 0.4 s · attente des limites de l'API 27 s (non comptée)

## q25 — Mon logiciel est-il un « système d'IA » au sens de la loi européenne ?

Article attendu : AI Act art. 3, définition 1 — passage [2].

### Réponse du copilote

> Pour déterminer si votre logiciel est un « système d'IA », il doit correspondre à la définition suivante : il s'agit d'un « système automatisé qui est conçu pour fonctionner à différents niveaux d’autonomie et peut faire preuve d’une capacité d’adaptation après son déploiement » [2]. De plus, ce système doit « déduire, à partir des entrées qu’il reçoit, la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels » [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « 1) «système d’IA», un système automatisé qui est conçu pour fonctionner à différents niveaux d’autonomie et peut faire preuve d’une capacité d’adaptation après son déploiement, et qui, pour des objectifs explicites ou implicites, déduit, à partir des entrées qu’il reçoit, la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels; »

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
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « déduire, à partir des entrées qu’il reçoit, la manière de générer des sorties telles que des prédictions, du contenu, … ».

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [2] « 1) «système d’IA», un système automatisé qui est conçu pour fonctionner à différents niveaux d’autonomie et peut faire preuve d’une capacité d’adaptation après son déploiement, et qui, pour des objectifs explicites ou implicites, déduit, à partir des entrées qu’il reçoit, la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels; »

RÉPONSE :
Pour déterminer si votre logiciel est un « système d'IA », il doit correspondre à la définition suivante : il s'agit d'un « système automatisé qui est conçu pour fonctionner à différents niveaux d’autonomie et peut faire preuve d’une capacité d’adaptation après son déploiement » [2]. De plus, ce système doit « déduire, à partir des entrées qu’il reçoit, la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels » [2].
```

</details>

Temps : recherche 2.1 s · génération 0.9 s (2209 tokens lus, 235 écrits, 511.8 tokens/s) · contrôle de pertinence 0.3 s · attente des limites de l'API 31 s (non comptée)

## q26 — Dois-je indiquer qu'une image publiée sur notre site a été créée par une IA ?

Article attendu : AI Act art. 50, paragraphe 4 — passage [1].

### Réponse du copilote

> Oui, vous devez indiquer que l'image a été créée par une IA si elle constitue un « hypertrucage », c'est-à-dire une image « présentant une ressemblance avec des personnes, des objets, des lieux, des entités ou événements existants et pouvant être perçu à tort par une personne comme authentiques ou véridiques » [4]. En tant que déployeur, vous « indiquez que les contenus ont été générés ou manipulés par une IA » [1]. Cette obligation ne s'applique pas « lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière » [1]. Si l'image fait partie d’une œuvre « manifestement artistique, créatif, satirique, fictif ou analogue », l'obligation se limite « à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre » [1].

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
  [5] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1 ter : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
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
Oui, vous devez indiquer que l'image a été créée par une IA si elle constitue un « hypertrucage », c'est-à-dire une image « présentant une ressemblance avec des personnes, des objets, des lieux, des entités ou événements existants et pouvant être perçu à tort par une personne comme authentiques ou véridiques » [4]. En tant que déployeur, vous « indiquez que les contenus ont été générés ou manipulés par une IA » [1]. Cette obligation ne s'applique pas « lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière » [1]. Si l'image fait partie d’une œuvre « manifestement artistique, créatif, satirique, fictif ou analogue », l'obligation se limite « à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre » [1].
```

</details>

Temps : recherche 2.2 s · génération 1.3 s (2114 tokens lus, 504 écrits, 512.0 tokens/s) · contrôle de pertinence 0.3 s · attente des limites de l'API 27 s (non comptée)

## q27 — Quelles amendes prévoit le règlement européen sur l'intelligence artificielle ?

Article attendu : AI Act art. 99, paragraphe 4 ou AI Act art. 99, paragraphe 6 — absent des passages donnés au modèle.

### Réponse du copilote

> Le règlement européen sur l'intelligence artificielle prévoit plusieurs niveaux d'amendes selon le type d'infraction et l'acteur concerné. Pour les institutions, organes et organismes de l'Union, le non-respect de l'interdiction des pratiques visées à l'article 5 est sanctionné par une amende pouvant aller jusqu'à 1 500 000 EUR [1]. Pour ces mêmes acteurs, la non-conformité avec d'autres exigences du règlement entraîne une amende pouvant aller jusqu'à 750 000 EUR [1]. Pour les opérateurs relevant de la compétence des États membres, le non-respect de l'interdiction des pratiques visées à l'article 5 peut entraîner des amendes allant jusqu'à 35 000 000 EUR ou, pour une entreprise, jusqu'à 7 % de son chiffre d'affaires annuel mondial total, le montant le plus élevé étant retenu [2]. La fourniture d'informations inexactes, incomplètes ou trompeuses aux autorités compétentes est sanctionnée par une amende pouvant aller jusqu'à 7 500 000 EUR ou, pour une entreprise, jusqu'à 1 % de son chiffre d'affaires annuel mondial total, le montant le plus élevé étant retenu [4]. Enfin, la Commission peut infliger aux fournisseurs de modèles d'IA à usage général des amendes n'excédant pas 3 % de leur chiffre d'affaires annuel mondial total ou 15 000 000 EUR, le montant le plus élevé étant retenu, en cas d'enfreinte des dispositions du règlement, de non-réponse aux demandes d'information, de non-conformité aux mesures demandées ou de refus d'accès au modèle pour évaluation [5].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’une amende administrative pouvant aller jusqu’à 1 500 000 EUR. »
  [1] « La non-conformité du système d’IA avec les exigences ou obligations au titre du présent règlement, autres que celles énoncées à l’article 5, fait l’objet d’une amende administrative pouvant aller jusqu’à 750 000 EUR. »
  [2] « Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’amendes administratives pouvant aller jusqu’à 35 000 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 7 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu. »
  [4] « La fourniture d’informations inexactes, incomplètes ou trompeuses aux organismes notifiés ou aux autorités nationales compétentes en réponse à une demande fait l’objet d’une amende administrative pouvant aller jusqu’à 7 500 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 1 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu. »
  [5] « La Commission peut infliger aux fournisseurs de modèles d’IA à usage général des amendes n’excédant pas 3 % de leur chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, ou 15 000 000 EUR, le montant le plus élevé étant retenu, lorsque la Commission constate que le fournisseur, de manière délibérée ou par négligence: »
  [5] « a) a enfreint les dispositions pertinentes du présent règlement; »
  [5] « b) n’a pas donné suite à une demande de document ou d’informations au titre de l’article 91, ou a fourni des informations inexactes, incomplètes ou trompeuses; »
  [5] « c) ne s’est pas conformé à une mesure demandée au titre de l’article 93; »
  [5] « d) n’a pas donné à la Commission accès au modèle d’IA à usage général ou au modèle d’IA à usage général présentant un risque systémique en vue de procéder à une évaluation conformément à l’article 92. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 100 : Amendes administratives imposées aux institutions, organes et organismes de l’Union (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_100
  [2] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 3 : Sanctions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [4] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 5 : Sanctions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [5] AI Act — règlement (UE) 2024/1689, article 101 : Amendes applicables aux fournisseurs de modèles d’IA à usage général (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_101
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 1 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’une amende administrative pouvant aller jusqu’à 1 500 000 EUR. »
- [1] « La non-conformité du système d’IA avec les exigences ou obligations au titre du présent règlement, autres que celles énoncées à l’article 5, fait l’objet d’une amende administrative pouvant aller jusqu’à 750 000 EUR. »
- [2] « Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’amendes administratives pouvant aller jusqu’à 35 000 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 7 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu. »
- [4] « La fourniture d’informations inexactes, incomplètes ou trompeuses aux organismes notifiés ou aux autorités nationales compétentes en réponse à une demande fait l’objet d’une amende administrative pouvant aller jusqu’à 7 500 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 1 % de son chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu. »
- [5] « La Commission peut infliger aux fournisseurs de modèles d’IA à usage général des amendes n’excédant pas 3 % de leur chiffre d’affaires annuel mondial total réalisé au cours de l’exercice précédent, ou 15 000 000 EUR, le montant le plus élevé étant retenu, lorsque la Commission constate que le fournisseur, de manière délibérée ou par négligence: »
- [5] « a) a enfreint les dispositions pertinentes du présent règlement; »
- [5] « b) n’a pas donné suite à une demande de document ou d’informations au titre de l’article 91, ou a fourni des informations inexactes, incomplètes ou trompeuses; »
- [5] « c) ne s’est pas conformé à une mesure demandée au titre de l’article 93; »
- [5] « d) n’a pas donné à la Commission accès au modèle d’IA à usage général ou au modèle d’IA à usage général présentant un risque systémique en vue de procéder à une évaluation conformément à l’article 92. »

RÉPONSE :
Le règlement européen sur l'intelligence artificielle prévoit plusieurs niveaux d'amendes selon le type d'infraction et l'acteur concerné. Pour les institutions, organes et organismes de l'Union, le non-respect de l'interdiction des pratiques visées à l'article 5 est sanctionné par une amende pouvant aller jusqu'à 1 500 000 EUR [1]. Pour ces mêmes acteurs, la non-conformité avec d'autres exigences du règlement entraîne une amende pouvant aller jusqu'à 750 000 EUR [1]. Pour les opérateurs relevant de la compétence des États membres, le non-respect de l'interdiction des pratiques visées à l'article 5 peut entraîner des amendes allant jusqu'à 35 000 000 EUR ou, pour une entreprise, jusqu'à 7 % de son chiffre d'affaires annuel mondial total, le montant le plus élevé étant retenu [2]. La fourniture d'informations inexactes, incomplètes ou trompeuses aux autorités compétentes est sanctionnée par une amende pouvant aller jusqu'à 7 500 000 EUR ou, pour une entreprise, jusqu'à 1 % de son chiffre d'affaires annuel mondial total, le montant le plus élevé étant retenu [4]. Enfin, la Commission peut infliger aux fournisseurs de modèles d'IA à usage général des amendes n'excédant pas 3 % de leur chiffre d'affaires annuel mondial total ou 15 000 000 EUR, le montant le plus élevé étant retenu, en cas d'enfreinte des dispositions du règlement, de non-réponse aux demandes d'information, de non-conformité aux mesures demandées ou de refus d'accès au modèle pour évaluation [5].
```

</details>

Temps : recherche 2.1 s · génération 2.5 s (2967 tokens lus, 984 écrits, 476.0 tokens/s) · contrôle de pertinence 0.5 s · attente des limites de l'API 56 s (non comptée)

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
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Temps : recherche 2.2 s · génération 0.5 s (3538 tokens lus, 25 écrits, 521.6 tokens/s)

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
  [4] AI Act — règlement (UE) 2024/1689, article 101 : Amendes applicables aux fournisseurs de modèles d’IA à usage général
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_101
  [5] AI Act — règlement (UE) 2024/1689, article 62 : Mesures en faveur des fournisseurs et déployeurs, en particulier les PME, y compris les jeunes pousses
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_62

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Temps : recherche 2.1 s · génération 0.7 s (2875 tokens lus, 25 écrits, 449.2 tokens/s)

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
  [2] RGPD — règlement (UE) 2016/679, article 40, paragraphe 1 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 7 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [4] RGPD — règlement (UE) 2016/679, article 26 : Responsables conjoints du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_26
  [5] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Temps : recherche 2.2 s · génération 0.8 s (2687 tokens lus, 25 écrits, 231.1 tokens/s) · attente des limites de l'API 17 s (non comptée)
