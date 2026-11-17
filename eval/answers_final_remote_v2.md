# Réponses du copilote — final_remote_v2

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 17/11/2026 à 23:49 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen/qwen3.8-27b` via l'API compatible OpenAI https://api.groq.com/openai/v1 (expérience de la séance 7, questions de test seulement ; modèle tel que servi par l'API à la date ci-dessus) — température 0.1, raisonnement : réglage par défaut du modèle, passages calculés pour un contexte de 8192 tokens comme en local, 2000 tokens au plus par réponse (raisonnement compris) ; le juge est le même modèle
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_v2.jsonl` (17 + 3 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q28 | Un adhérent nous signale que son adresse et sa date de naissance sont fausses dans notre fichier : devons-nous les corriger, et dans quel délai ? | 4/4 | non | — | 4 s |
| q29 | Une cliente conteste l'exactitude des informations que nous avons sur elle : pouvons-nous continuer à les utiliser pendant que nous vérifions ? | 2/2 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 4 s |
| q30 | Pouvons-nous refuser automatiquement une demande d'inscription à notre service à partir d'un score calculé par un logiciel, sans qu'une personne ne vérifie ? | 3/5 | non | 2 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1], [1]) : ignoré(s).; La réponse met entre « » un texte introuvable dans les extraits vérifiés : « autorisée par le droit de l'Union ou le droit de l'État membre... » (et 2 autre(s)). | 4 s |
| q31 | Nous faisons développer une application mobile pour nos membres : quelles précautions de protection des données devons-nous prévoir dès sa conception ? | 6/6 | non | — | 4 s |
| q32 | Nous organisons un festival avec une autre association et nous gérons ensemble le fichier des participants : qui est responsable de ces données ? | 6/6 | non | — | 5 s |
| q33 | Nous avons acheté un fichier de prospects à une autre entreprise : devons-nous informer ces personnes, et dans quel délai ? | 5/5 | non | — | 4 s |
| q34 | Puis-je installer des caméras dans l'atelier pour surveiller le travail de mes salariés ? | 0/0 | oui | — | 3 s |
| q35 | Notre fédération sportive peut-elle rédiger un guide de bonnes pratiques RGPD que ses clubs pourraient suivre officiellement ? | 3/3 | non | La réponse met entre « » un texte introuvable dans les extraits vérifiés : « rendre un avis et approuve les codes de conduite qui fournissent des garanties suffisantes ». | 4 s |
| q36 | Un ancien bénévole menace de se plaindre de nous auprès de la CNIL : en a-t-il le droit, et quels autres recours a-t-il ? | 4/4 | non | — | 5 s |
| q37 | Si une fuite de données cause un préjudice à un client, peut-il nous demander réparation ? | 0/0 | oui | — | 3 s |
| q38 | Notre club de sport peut-il demander un extrait de casier judiciaire aux bénévoles qui encadrent des enfants ? | 0/0 | oui | — | 3 s |
| q39 | Si nous remplaçons les noms de nos adhérents par des numéros, les données sont-elles encore des données personnelles ? | 2/2 | non | — | 3 s |
| q40 | Nous allons utiliser un logiciel d'IA à haut risque qui attribue les tâches à nos salariés : devons-nous les prévenir avant de l'utiliser ? | 3/3 | non | — | 4 s |
| q41 | Notre organisme de formation peut-il utiliser une IA pour noter les examens de ses stagiaires ? Est-ce encadré ? | 6/6 | non | — | 4 s |
| q42 | Un candidat refusé après l'analyse de sa candidature par un outil d'IA à haut risque nous demande pourquoi : devons-nous lui expliquer ? | 2/2 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 4 s |
| q43 | Le règlement européen sur l'IA prévoit-il des mesures particulières pour les PME ? | 6/6 | non | — | 5 s |
| q44 | À partir de quelle date devrons-nous respecter les obligations sur les systèmes d'IA à haut risque utilisés pour le recrutement ? | 0/0 | oui | — | 3 s |
| h06 | Quelles mentions obligatoires doivent figurer sur une facture ? | 0/0 | oui | — | 3 s |
| h07 | Comment demander une subvention à la mairie pour notre association ? | 0/0 | oui | — | 3 s |
| h08 | Quelles sont les règles pour embaucher un apprenti dans une PME ? | 0/0 | oui | — | 3 s |

## q28 — Un adhérent nous signale que son adresse et sa date de naissance sont fausses dans notre fichier : devons-nous les corriger, et dans quel délai ?

Article attendu : RGPD art. 16 — passage [1].

### Réponse du copilote

> Oui, vous devez corriger l'adresse et la date de naissance de l'adhérent, car il s'agit de données inexactes [1]. En tant que responsable du traitement, vous avez l'obligation de procéder à cette rectification « dans les meilleurs délais » [1]. Si vous avez communiqué ces données à des tiers, vous devez notifier la rectification à chaque destinataire, « à moins qu'une telle communication se révèle impossible ou exige des efforts disproportionnés » [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit d'obtenir du responsable du traitement, dans les meilleurs délais, la rectification des données à caractère personnel la concernant qui sont inexactes. »
  [1] « Compte tenu des finalités du traitement, la personne concernée a le droit d'obtenir que les données à caractère personnel incomplètes soient complétées, y compris en fournissant une déclaration complémentaire. »
  [2] « Le responsable du traitement notifie à chaque destinataire auquel les données à caractère personnel ont été communiquées toute rectification ou tout effacement de données à caractère personnel ou toute limitation du traitement effectué conformément à l'article 16, à l'article 17, paragraphe 1, et à l'article 18, à moins qu'une telle communication se révèle impossible ou exige des efforts disproportionnés. »
  [2] « Le responsable du traitement fournit à la personne concernée des informations sur ces destinataires si celle-ci en fait la demande. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 16 : Droit de rectification (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_16
  [2] RGPD — règlement (UE) 2016/679, article 19 : Obligation de notification en ce qui concerne la rectification ou l'effacement de données à caractère personnel ou la limitation du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_19
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 33 : Notification à l'autorité de contrôle d'une violation de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_33
  [4] RGPD — règlement (UE) 2016/679, article 17 : Droit à l'effacement («droit à l'oubli»)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_17
  [5] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « La personne concernée a le droit d'obtenir du responsable du traitement, dans les meilleurs délais, la rectification des données à caractère personnel la concernant qui sont inexactes. »
- [1] « Compte tenu des finalités du traitement, la personne concernée a le droit d'obtenir que les données à caractère personnel incomplètes soient complétées, y compris en fournissant une déclaration complémentaire. »
- [2] « Le responsable du traitement notifie à chaque destinataire auquel les données à caractère personnel ont été communiquées toute rectification ou tout effacement de données à caractère personnel ou toute limitation du traitement effectué conformément à l'article 16, à l'article 17, paragraphe 1, et à l'article 18, à moins qu'une telle communication se révèle impossible ou exige des efforts disproportionnés. »
- [2] « Le responsable du traitement fournit à la personne concernée des informations sur ces destinataires si celle-ci en fait la demande. »

RÉPONSE :
Oui, vous devez corriger l'adresse et la date de naissance de l'adhérent, car il s'agit de données inexactes [1]. En tant que responsable du traitement, vous avez l'obligation de procéder à cette rectification « dans les meilleurs délais » [1]. Si vous avez communiqué ces données à des tiers, vous devez notifier la rectification à chaque destinataire, « à moins qu'une telle communication se révèle impossible ou exige des efforts disproportionnés » [2].
```

</details>

Temps : recherche 2.6 s · génération 1.2 s (3235 tokens lus, 325 écrits, 510.8 tokens/s) · contrôle de pertinence 0.1 s

## q29 — Une cliente conteste l'exactitude des informations que nous avons sur elle : pouvons-nous continuer à les utiliser pendant que nous vérifions ?

Article attendu : RGPD art. 18 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 12, paragraphe 6 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [3] RGPD — règlement (UE) 2016/679, article 16 : Droit de rectification
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_16
  [4] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [5] RGPD — règlement (UE) 2016/679, article 21 : Droit d'opposition
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_21
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [3] « La personne concernée a le droit d'obtenir du responsable du traitement, dans les meilleurs délais, la rectification des données à caractère personnel la concernant qui sont inexactes. »
- [1] « Sans préjudice de l'article 11, lorsque le responsable du traitement a des doutes raisonnables quant à l'identité de la personne physique présentant la demande visée aux articles 15 à 21, il peut demander que lui soient fournies des informations supplémentaires nécessaires pour confirmer l'identité de la personne concernée. »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question. Ils précisent que la personne concernée a le droit d'obtenir la rectification des données inexactes « dans les meilleurs délais » [3], et que vous pouvez demander des informations supplémentaires pour confirmer son identité si vous avez des doutes raisonnables [1]. Cependant, les extraits fournis ne contiennent pas de règle spécifique indiquant si vous devez suspendre l'utilisation des données pendant la vérification de leur exactitude.
```

</details>

Temps : recherche 2.2 s · génération 0.8 s (2954 tokens lus, 235 écrits, 525.2 tokens/s) · contrôle de pertinence 1.0 s

## q30 — Pouvons-nous refuser automatiquement une demande d'inscription à notre service à partir d'un score calculé par un logiciel, sans qu'une personne ne vérifie ?

Article attendu : RGPD art. 22 — passage [1].

### Réponse du copilote

> Non, vous ne pouvez pas refuser automatiquement une demande d'inscription sans aucune vérification humaine, car la personne concernée a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé produisant des effets juridiques ou l'affectant de manière significative [1]. Cette interdiction ne s'applique pas uniquement si la décision est « nécessaire à la conclusion ou à l'exécution d'un contrat entre la personne concernée et un responsable du traitement », « autorisée par le droit de l'Union ou le droit de l'État membre... » ou « fondée sur le consentement explicite de la personne concernée » [1]. Dans les cas où l'exception du contrat (point a) ou du consentement (point c) s'applique, le responsable du traitement doit « mettre en œuvre des mesures appropriées pour la sauvegarde des droits et libertés et des intérêts légitimes de la personne concernée, au moins du droit de la personne concernée d'obtenir une intervention humaine de la part du responsable du traitement, d'exprimer son point de vue et de contester la décision » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé, y compris le profilage, produisant des effets juridiques la concernant ou l'affectant de manière significative de façon similaire. »
  [1] « Le paragraphe 1 ne s'applique pas lorsque la décision: a) est nécessaire à la conclusion ou à l'exécution d'un contrat entre la personne concernée et un responsable du traitement; »
  [1] « Dans les cas visés au paragraphe 2, points a) et c), le responsable du traitement met en œuvre des mesures appropriées pour la sauvegarde des droits et libertés et des intérêts légitimes de la personne concernée, au moins du droit de la personne concernée d'obtenir une intervention humaine de la part du responsable du traitement, d'exprimer son point de vue et de contester la décision. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 22 : Décision individuelle automatisée, y compris le profilage (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_22
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 60, paragraphe 5 : Essais de systèmes d’IA à haut risque en conditions réelles en dehors des bacs à sable réglementaires de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_60
  [3] AI Act — règlement (UE) 2024/1689, article 60, paragraphe 1 : Essais de systèmes d’IA à haut risque en conditions réelles en dehors des bacs à sable réglementaires de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_60
  [4] AI Act — règlement (UE) 2024/1689, annexe VII, point 4 c (1/2) : Conformité fondée sur une évaluation du système de gestion de la qualité et une évaluation de la documentation technique
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_VII
  [5] AI Act — règlement (UE) 2024/1689, article 75, paragraphe 1 sexies : Surveillance du marché et contrôle des systèmes d'IA et assistance mutuelle
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_75
Attention : 2 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1], [1]) : ignoré(s).
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « autorisée par le droit de l'Union ou le droit de l'État membre... » (et 2 autre(s)).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « La personne concernée a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé, y compris le profilage, produisant des effets juridiques la concernant ou l'affectant de manière significative de façon similaire. »
- [1] « Le paragraphe 1 ne s'applique pas lorsque la décision: a) est nécessaire à la conclusion ou à l'exécution d'un contrat entre la personne concernée et un responsable du traitement; »
- [1] « Le paragraphe 1 ne s'applique pas lorsque la décision: b) est autorisée par le droit de l'Union ou le droit de l'État membre auquel le responsable du traitement est soumis et qui prévoit également des mesures appropriées pour la sauvegarde des droits et libertés et des intérêts légitimes de la personne concernée; ou »
- [1] « Le paragraphe 1 ne s'applique pas lorsque la décision: c) est fondée sur le consentement explicite de la personne concernée. »
- [1] « Dans les cas visés au paragraphe 2, points a) et c), le responsable du traitement met en œuvre des mesures appropriées pour la sauvegarde des droits et libertés et des intérêts légitimes de la personne concernée, au moins du droit de la personne concernée d'obtenir une intervention humaine de la part du responsable du traitement, d'exprimer son point de vue et de contester la décision. »

RÉPONSE :
Non, vous ne pouvez pas refuser automatiquement une demande d'inscription sans aucune vérification humaine, car la personne concernée a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé produisant des effets juridiques ou l'affectant de manière significative [1]. Cette interdiction ne s'applique pas uniquement si la décision est « nécessaire à la conclusion ou à l'exécution d'un contrat entre la personne concernée et un responsable du traitement », « autorisée par le droit de l'Union ou le droit de l'État membre... » ou « fondée sur le consentement explicite de la personne concernée » [1]. Dans les cas où l'exception du contrat (point a) ou du consentement (point c) s'applique, le responsable du traitement doit « mettre en œuvre des mesures appropriées pour la sauvegarde des droits et libertés et des intérêts légitimes de la personne concernée, au moins du droit de la personne concernée d'obtenir une intervention humaine de la part du responsable du traitement, d'exprimer son point de vue et de contester la décision » [1].
```

</details>

Temps : recherche 2.2 s · génération 1.6 s (3211 tokens lus, 566 écrits, 464.3 tokens/s) · contrôle de pertinence 0.3 s · attente des limites de l'API 20 s (non comptée)

## q31 — Nous faisons développer une application mobile pour nos membres : quelles précautions de protection des données devons-nous prévoir dès sa conception ?

Article attendu : RGPD art. 25 — passage [1].

### Réponse du copilote

> En tant que responsable du traitement, vous devez intégrer la protection des données dès la conception de l'application mobile, conformément au RGPD, article 25 [1]. Cela implique de mettre en œuvre des mesures techniques et organisationnelles appropriées, telles que la pseudonymisation, pour garantir la minimisation des données et protéger les droits des personnes concernées [1]. Vous devez également vous assurer que, par défaut, seules les données nécessaires à chaque finalité spécifique sont traitées, ce qui concerne la quantité de données collectées, leur durée de conservation et leur accessibilité [1]. De plus, les données ne doivent pas être accessibles à un nombre indéterminé de personnes sans l'intervention de la personne concernée [1].
>
> Parallèlement, le RGPD, article 32, impose au responsable du traitement et au sous-traitant de garantir un niveau de sécurité adapté au risque, notamment par la pseudonymisation et le chiffrement des données, ainsi que par des moyens assurant la confidentialité, l'intégrité et la disponibilité des systèmes [3]. Il est également requis de disposer de moyens pour rétablir l'accès aux données en cas d'incident et de tester régulièrement l'efficacité de ces mesures [3].
>
> Enfin, si le développement de cette application, en particulier par le recours à de nouvelles technologies, est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes, vous devez effectuer une analyse d'impact relative à la protection des données avant le traitement, conformément au RGPD, article 35 [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « le responsable du traitement met en œuvre, tant au moment de la détermination des moyens du traitement qu'au moment du traitement lui-même, des mesures techniques et organisationnelles appropriées, telles que la pseudonymisation, qui sont destinées à mettre en œuvre les principes relatifs à la protection des données, par exemple la minimisation des données, de façon effective et à assortir le traitement des garanties nécessaires afin de répondre aux exigences du présent règlement et de protéger les droits de la personne concernée. »
  [1] « Le responsable du traitement met en œuvre les mesures techniques et organisationnelles appropriées pour garantir que, par défaut, seules les données à caractère personnel qui sont nécessaires au regard de chaque finalité spécifique du traitement sont traitées. »
  [1] « Cela s'applique à la quantité de données à caractère personnel collectées, à l'étendue de leur traitement, à leur durée de conservation et à leur accessibilité. »
  [1] « En particulier, ces mesures garantissent que, par défaut, les données à caractère personnel ne sont pas rendues accessibles à un nombre indéterminé de personnes physiques sans l'intervention de la personne physique concernée. »
  [3] « le responsable du traitement et le sous-traitant mettent en œuvre les mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque, y compris entre autres, selon les besoins: a) la pseudonymisation et le chiffrement des données à caractère personnel; b) des moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement; c) des moyens permettant de rétablir la disponibilité des données à caractère personnel et l'accès à celles-ci dans des délais appropriés en cas d'incident physique ou technique; d) une procédure visant à tester, à analyser et à évaluer régulièrement l'efficacité des mesures techniques et organisationnelles pour assurer la sécurité du traitement. »
  [4] « Lorsqu'un type de traitement, en particulier par le recours à de nouvelles technologies, et compte tenu de la nature, de la portée, du contexte et des finalités du traitement, est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, le responsable du traitement effectue, avant le traitement, une analyse de l'impact des opérations de traitement envisagées sur la protection des données à caractère personnel. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 25 : Protection des données dès la conception et protection des données par défaut (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_25
  [3] RGPD — règlement (UE) 2016/679, article 32 : Sécurité du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_32
  [4] RGPD — règlement (UE) 2016/679, article 35, paragraphe 1 : Analyse d'impact relative à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [5] RGPD — règlement (UE) 2016/679, article 50 : Coopération internationale dans le domaine de la protection des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_50

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « le responsable du traitement met en œuvre, tant au moment de la détermination des moyens du traitement qu'au moment du traitement lui-même, des mesures techniques et organisationnelles appropriées, telles que la pseudonymisation, qui sont destinées à mettre en œuvre les principes relatifs à la protection des données, par exemple la minimisation des données, de façon effective et à assortir le traitement des garanties nécessaires afin de répondre aux exigences du présent règlement et de protéger les droits de la personne concernée. »
- [1] « Le responsable du traitement met en œuvre les mesures techniques et organisationnelles appropriées pour garantir que, par défaut, seules les données à caractère personnel qui sont nécessaires au regard de chaque finalité spécifique du traitement sont traitées. »
- [1] « Cela s'applique à la quantité de données à caractère personnel collectées, à l'étendue de leur traitement, à leur durée de conservation et à leur accessibilité. »
- [1] « En particulier, ces mesures garantissent que, par défaut, les données à caractère personnel ne sont pas rendues accessibles à un nombre indéterminé de personnes physiques sans l'intervention de la personne physique concernée. »
- [3] « le responsable du traitement et le sous-traitant mettent en œuvre les mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque, y compris entre autres, selon les besoins: a) la pseudonymisation et le chiffrement des données à caractère personnel; b) des moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement; c) des moyens permettant de rétablir la disponibilité des données à caractère personnel et l'accès à celles-ci dans des délais appropriés en cas d'incident physique ou technique; d) une procédure visant à tester, à analyser et à évaluer régulièrement l'efficacité des mesures techniques et organisationnelles pour assurer la sécurité du traitement. »
- [4] « Lorsqu'un type de traitement, en particulier par le recours à de nouvelles technologies, et compte tenu de la nature, de la portée, du contexte et des finalités du traitement, est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, le responsable du traitement effectue, avant le traitement, une analyse de l'impact des opérations de traitement envisagées sur la protection des données à caractère personnel. »

RÉPONSE :
En tant que responsable du traitement, vous devez intégrer la protection des données dès la conception de l'application mobile, conformément au RGPD, article 25 [1]. Cela implique de mettre en œuvre des mesures techniques et organisationnelles appropriées, telles que la pseudonymisation, pour garantir la minimisation des données et protéger les droits des personnes concernées [1]. Vous devez également vous assurer que, par défaut, seules les données nécessaires à chaque finalité spécifique sont traitées, ce qui concerne la quantité de données collectées, leur durée de conservation et leur accessibilité [1]. De plus, les données ne doivent pas être accessibles à un nombre indéterminé de personnes sans l'intervention de la personne concernée [1].

Parallèlement, le RGPD, article 32, impose au responsable du traitement et au sous-traitant de garantir un niveau de sécurité adapté au risque, notamment par la pseudonymisation et le chiffrement des données, ainsi que par des moyens assurant la confidentialité, l'intégrité et la disponibilité des systèmes [3]. Il est également requis de disposer de moyens pour rétablir l'accès aux données en cas d'incident et de tester régulièrement l'efficacité de ces mesures [3].

Enfin, si le développement de cette application, en particulier par le recours à de nouvelles technologies, est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes, vous devez effectuer une analyse d'impact relative à la protection des données avant le traitement, conformément au RGPD, article 35 [4].
```

</details>

Temps : recherche 2.2 s · génération 2.0 s (2823 tokens lus, 848 écrits, 518.7 tokens/s) · contrôle de pertinence 0.2 s · attente des limites de l'API 42 s (non comptée)

## q32 — Nous organisons un festival avec une autre association et nous gérons ensemble le fichier des participants : qui est responsable de ces données ?

Article attendu : RGPD art. 26 — passage [1].

### Réponse du copilote

> Vous et l'autre association êtes les « responsables conjoints du traitement » car vous déterminez conjointement les finalités et les moyens du traitement du fichier des participants [1]. Cette qualification s'applique car le responsable du traitement est défini comme l'organisme qui détermine les finalités et les moyens du traitement, seul ou conjointement avec d'autres [2]. Vous devez définir de manière transparente vos obligations respectives, notamment concernant l'exercice des droits des participants et la communication des informations, par voie d'accord entre vous, « sauf si, et dans la mesure, où leurs obligations respectives sont définies par le droit de l'Union ou par le droit de l'État membre auquel les responsables du traitement sont soumis » [1]. Cet accord doit refléter vos rôles respectifs et vos relations vis-à-vis des personnes concernées, et ses grandes lignes doivent être mises à la disposition de la personne concernée [1]. Enfin, chaque participant peut exercer ses droits à l'égard de et contre chacun des responsables du traitement, indépendamment des termes de votre accord [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Lorsque deux responsables du traitement ou plus déterminent conjointement les finalités et les moyens du traitement, ils sont les responsables conjoints du traitement. »
  [1] « Les responsables conjoints du traitement définissent de manière transparente leurs obligations respectives aux fins d'assurer le respect des exigences du présent règlement, notamment en ce qui concerne l'exercice des droits de la personne concernée, et leurs obligations respectives quant à la communication des informations visées aux articles 13 et 14, par voie d'accord entre eux, sauf si, et dans la mesure, où leurs obligations respectives sont définies par le droit de l'Union ou par le droit de l'État membre auquel les responsables du traitement sont soumis. »
  [1] « L'accord visé au paragraphe 1 reflète dûment les rôles respectifs des responsables conjoints du traitement et leurs relations vis-à-vis des personnes concernées. »
  [1] « Les grandes lignes de l'accord sont mises à la disposition de la personne concernée. »
  [1] « Indépendamment des termes de l'accord visé au paragraphe 1, la personne concernée peut exercer les droits que lui confère le présent règlement à l'égard de et contre chacun des responsables du traitement. »
  [2] « «responsable du traitement», la personne physique ou morale, l'autorité publique, le service ou un autre organisme qui, seul ou conjointement avec d'autres, détermine les finalités et les moyens du traitement; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 26 : Responsables conjoints du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_26
  [2] RGPD — règlement (UE) 2016/679, article 4, définition 7 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30
  [4] RGPD — règlement (UE) 2016/679, article 24 : Responsabilité du responsable du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_24
  [5] RGPD — règlement (UE) 2016/679, article 4, définition 10 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Lorsque deux responsables du traitement ou plus déterminent conjointement les finalités et les moyens du traitement, ils sont les responsables conjoints du traitement. »
- [1] « Les responsables conjoints du traitement définissent de manière transparente leurs obligations respectives aux fins d'assurer le respect des exigences du présent règlement, notamment en ce qui concerne l'exercice des droits de la personne concernée, et leurs obligations respectives quant à la communication des informations visées aux articles 13 et 14, par voie d'accord entre eux, sauf si, et dans la mesure, où leurs obligations respectives sont définies par le droit de l'Union ou par le droit de l'État membre auquel les responsables du traitement sont soumis. »
- [1] « L'accord visé au paragraphe 1 reflète dûment les rôles respectifs des responsables conjoints du traitement et leurs relations vis-à-vis des personnes concernées. »
- [1] « Les grandes lignes de l'accord sont mises à la disposition de la personne concernée. »
- [1] « Indépendamment des termes de l'accord visé au paragraphe 1, la personne concernée peut exercer les droits que lui confère le présent règlement à l'égard de et contre chacun des responsables du traitement. »
- [2] « «responsable du traitement», la personne physique ou morale, l'autorité publique, le service ou un autre organisme qui, seul ou conjointement avec d'autres, détermine les finalités et les moyens du traitement; »

RÉPONSE :
Vous et l'autre association êtes les « responsables conjoints du traitement » car vous déterminez conjointement les finalités et les moyens du traitement du fichier des participants [1]. Cette qualification s'applique car le responsable du traitement est défini comme l'organisme qui détermine les finalités et les moyens du traitement, seul ou conjointement avec d'autres [2]. Vous devez définir de manière transparente vos obligations respectives, notamment concernant l'exercice des droits des participants et la communication des informations, par voie d'accord entre vous, « sauf si, et dans la mesure, où leurs obligations respectives sont définies par le droit de l'Union ou par le droit de l'État membre auquel les responsables du traitement sont soumis » [1]. Cet accord doit refléter vos rôles respectifs et vos relations vis-à-vis des personnes concernées, et ses grandes lignes doivent être mises à la disposition de la personne concernée [1]. Enfin, chaque participant peut exercer ses droits à l'égard de et contre chacun des responsables du traitement, indépendamment des termes de votre accord [1].
```

</details>

Temps : recherche 2.2 s · génération 2.1 s (2738 tokens lus, 571 écrits, 531.3 tokens/s) · contrôle de pertinence 0.6 s · attente des limites de l'API 61 s (non comptée)

## q33 — Nous avons acheté un fichier de prospects à une autre entreprise : devons-nous informer ces personnes, et dans quel délai ?

Article attendu : RGPD art. 14 — passage [2].

### Réponse du copilote

> Oui, vous devez informer ces personnes car leurs données n'ont pas été collectées directement auprès d'eux [3]. En tant que responsable du traitement, vous devez fournir les informations prévues par le RGPD, article 14 [2]. Le délai général est « dans un délai raisonnable après avoir obtenu les données à caractère personnel, mais ne dépassant pas un mois » [2]. Cependant, si vous comptez utiliser ces données pour communiquer avec les prospects, l'information doit être fournie « au plus tard au moment de la première communication à ladite personne » [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « Lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée, le responsable du traitement fournit à celle-ci toutes les informations suivantes: »
  [2] « Le responsable du traitement fournit les informations visées aux paragraphes 1 et 2: »
  [2] « a) dans un délai raisonnable après avoir obtenu les données à caractère personnel, mais ne dépassant pas un mois, eu égard aux circonstances particulières dans lesquelles les données à caractère personnel sont traitées; »
  [2] « b) si les données à caractère personnel doivent être utilisées aux fins de la communication avec la personne concernée, au plus tard au moment de la première communication à ladite personne; ou »
  [2] « c) s'il est envisagé de communiquer les informations à un autre destinataire, au plus tard lorsque les données à caractère personnel sont communiquées pour la première fois. »

Sources citées :
  [2] RGPD — règlement (UE) 2016/679, article 14, paragraphe 3 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [3] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [4] AI Act — règlement (UE) 2024/1689, article 31, paragraphe 7 : Exigences concernant les organismes notifiés
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_31
  [5] AI Act — règlement (UE) 2024/1689, article 31, paragraphe 1 : Exigences concernant les organismes notifiés
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_31

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [3] « Lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée, le responsable du traitement fournit à celle-ci toutes les informations suivantes: »
- [2] « Le responsable du traitement fournit les informations visées aux paragraphes 1 et 2: »
- [2] « a) dans un délai raisonnable après avoir obtenu les données à caractère personnel, mais ne dépassant pas un mois, eu égard aux circonstances particulières dans lesquelles les données à caractère personnel sont traitées; »
- [2] « b) si les données à caractère personnel doivent être utilisées aux fins de la communication avec la personne concernée, au plus tard au moment de la première communication à ladite personne; ou »
- [2] « c) s'il est envisagé de communiquer les informations à un autre destinataire, au plus tard lorsque les données à caractère personnel sont communiquées pour la première fois. »

RÉPONSE :
Oui, vous devez informer ces personnes car leurs données n'ont pas été collectées directement auprès d'eux [3]. En tant que responsable du traitement, vous devez fournir les informations prévues par le RGPD, article 14 [2]. Le délai général est « dans un délai raisonnable après avoir obtenu les données à caractère personnel, mais ne dépassant pas un mois » [2]. Cependant, si vous comptez utiliser ces données pour communiquer avec les prospects, l'information doit être fournie « au plus tard au moment de la première communication à ladite personne » [2].
```

</details>

Temps : recherche 2.2 s · génération 1.0 s (2133 tokens lus, 331 écrits, 522.6 tokens/s) · contrôle de pertinence 0.5 s

## q34 — Puis-je installer des caméras dans l'atelier pour surveiller le travail de mes salariés ?

Article attendu : RGPD art. 88 — absent des passages donnés au modèle.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 75 bis, point e : Pouvoirs de surveillance et de contrôle du Bureau de l'IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_75a
  [2] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1 bis : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [3] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points a) à e) : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [4] AI Act — règlement (UE) 2024/1689, article 75 bis, point a : Pouvoirs de surveillance et de contrôle du Bureau de l'IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_75a
  [5] AI Act — règlement (UE) 2024/1689, article 89 : Mesures de contrôle
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_89

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Temps : recherche 2.2 s · génération 0.5 s (3153 tokens lus, 25 écrits, 456.0 tokens/s) · attente des limites de l'API 14 s (non comptée)

## q35 — Notre fédération sportive peut-elle rédiger un guide de bonnes pratiques RGPD que ses clubs pourraient suivre officiellement ?

Article attendu : RGPD art. 40 — passage [1].

### Réponse du copilote

> Oui, votre fédération sportive peut rédiger un tel guide, car les associations représentant des catégories de responsables du traitement « peuvent élaborer des codes de conduite » pour préciser les modalités d'application du RGPD [1]. Cette initiative est d'ailleurs encouragée par les autorités, notamment compte tenu des besoins spécifiques des micro, petites et moyennes entreprises [3]. Cependant, pour que ce guide soit officiellement reconnu, l'autorité de contrôle doit « rendre un avis et approuve les codes de conduite qui fournissent des garanties suffisantes » [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent élaborer des codes de conduite, les modifier ou les proroger, aux fins de préciser les modalités d'application du présent règlement, telles que: »
  [3] « Les États membres, les autorités de contrôle, le comité et la Commission encouragent l'élaboration de codes de conduite destinés à contribuer à la bonne application du présent règlement, compte tenu de la spécificité des différents secteurs de traitement et des besoins spécifiques des micro, petites et moyennes entreprises. »
  [4] « encourage l'élaboration de codes de conduite en application de l'article 40, paragraphe 1, rend un avis et approuve les codes de conduite qui fournissent des garanties suffisantes, en application de l'article 40, paragraphe 5; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [3] RGPD — règlement (UE) 2016/679, article 40, paragraphe 1 : Codes de conduite (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [4] RGPD — règlement (UE) 2016/679, article 57, paragraphe 1, points a) à t) : Missions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_57
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 70, paragraphe 1, points a) à l) : Missions du comité
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_70
  [5] RGPD — règlement (UE) 2016/679, article 91 : Règles existantes des églises et associations religieuses en matière de protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_91
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « rendre un avis et approuve les codes de conduite qui fournissent des garanties suffisantes ».

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent élaborer des codes de conduite, les modifier ou les proroger, aux fins de préciser les modalités d'application du présent règlement, telles que: »
- [3] « Les États membres, les autorités de contrôle, le comité et la Commission encouragent l'élaboration de codes de conduite destinés à contribuer à la bonne application du présent règlement, compte tenu de la spécificité des différents secteurs de traitement et des besoins spécifiques des micro, petites et moyennes entreprises. »
- [4] « encourage l'élaboration de codes de conduite en application de l'article 40, paragraphe 1, rend un avis et approuve les codes de conduite qui fournissent des garanties suffisantes, en application de l'article 40, paragraphe 5; »

RÉPONSE :
Oui, votre fédération sportive peut rédiger un tel guide, car les associations représentant des catégories de responsables du traitement « peuvent élaborer des codes de conduite » pour préciser les modalités d'application du RGPD [1]. Cette initiative est d'ailleurs encouragée par les autorités, notamment compte tenu des besoins spécifiques des micro, petites et moyennes entreprises [3]. Cependant, pour que ce guide soit officiellement reconnu, l'autorité de contrôle doit « rendre un avis et approuve les codes de conduite qui fournissent des garanties suffisantes » [4].
```

</details>

Temps : recherche 2.2 s · génération 1.3 s (3548 tokens lus, 316 écrits, 477.1 tokens/s) · contrôle de pertinence 0.2 s · attente des limites de l'API 16 s (non comptée)

## q36 — Un ancien bénévole menace de se plaindre de nous auprès de la CNIL : en a-t-il le droit, et quels autres recours a-t-il ?

Article attendu : RGPD art. 77 — absent des passages donnés au modèle.

### Réponse du copilote

> Oui, l'ancien bénévole a le droit de se plaindre auprès de la CNIL, car chaque personne concernée a le droit d'introduire une réclamation auprès d'une autorité de contrôle [4]. Il peut également exercer un recours juridictionnel effectif s'il considère que ses droits ont été violés par le traitement de ses données [4]. Ce recours peut être intenté devant les juridictions de l'État membre où vous disposez d'un établissement, ou devant celles de l'État membre où il a sa résidence habituelle, « sauf si le responsable du traitement ou le sous-traitant est une autorité publique d'un État membre agissant dans l'exercice de ses prérogatives de puissance publique » [4]. Enfin, il a le droit de mandater un organisme, une organisation ou une association à but non lucratif pour qu'ils introduisent la réclamation et exercent les droits en son nom [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit de mandater un organisme, une organisation ou une association à but non lucratif, qui a été valablement constitué conformément au droit d'un État membre, dont les objectifs statutaires sont d'intérêt public et est actif dans le domaine de la protection des droits et libertés des personnes concernées dans le cadre de la protection des données à caractère personnel les concernant, pour qu'il introduise une réclamation en son nom, exerce en son nom les droits visés aux articles 77, 78 et 79 et exerce en son nom le droit d'obtenir réparation visé à l'article 82 lorsque le droit d'un État membre le prévoit. »
  [4] « Sans préjudice de tout recours administratif ou extrajudiciaire qui lui est ouvert, y compris le droit d'introduire une réclamation auprès d'une autorité de contrôle au titre de l'article 77, chaque personne concernée a droit à un recours juridictionnel effectif si elle considère que les droits que lui confère le présent règlement ont été violés du fait d'un traitement de ses données à caractère personnel effectué en violation du présent règlement. »
  [4] « Toute action contre un responsable du traitement ou un sous-traitant est intentée devant les juridictions de l'État membre dans lequel le responsable du traitement ou le sous-traitant dispose d'un établissement. »
  [4] « Une telle action peut aussi être intentée devant les juridictions de l'État membre dans lequel la personne concernée a sa résidence habituelle, sauf si le responsable du traitement ou le sous-traitant est une autorité publique d'un État membre agissant dans l'exercice de ses prérogatives de puissance publique. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 80 : Représentation des personnes concernées (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_80
  [4] RGPD — règlement (UE) 2016/679, article 79 : Droit à un recours juridictionnel effectif contre un responsable du traitement ou un sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_79
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 36, paragraphe 4 : Modifications apportées aux notifications
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_36
  [3] AI Act — règlement (UE) 2024/1689, article 36, paragraphe 1 : Modifications apportées aux notifications
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_36
  [5] AI Act — règlement (UE) 2024/1689, article 37 : Contestation de la compétence des organismes notifiés
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_37

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « La personne concernée a le droit de mandater un organisme, une organisation ou une association à but non lucratif, qui a été valablement constitué conformément au droit d'un État membre, dont les objectifs statutaires sont d'intérêt public et est actif dans le domaine de la protection des droits et libertés des personnes concernées dans le cadre de la protection des données à caractère personnel les concernant, pour qu'il introduise une réclamation en son nom, exerce en son nom les droits visés aux articles 77, 78 et 79 et exerce en son nom le droit d'obtenir réparation visé à l'article 82 lorsque le droit d'un État membre le prévoit. »
- [4] « Sans préjudice de tout recours administratif ou extrajudiciaire qui lui est ouvert, y compris le droit d'introduire une réclamation auprès d'une autorité de contrôle au titre de l'article 77, chaque personne concernée a droit à un recours juridictionnel effectif si elle considère que les droits que lui confère le présent règlement ont été violés du fait d'un traitement de ses données à caractère personnel effectué en violation du présent règlement. »
- [4] « Toute action contre un responsable du traitement ou un sous-traitant est intentée devant les juridictions de l'État membre dans lequel le responsable du traitement ou le sous-traitant dispose d'un établissement. »
- [4] « Une telle action peut aussi être intentée devant les juridictions de l'État membre dans lequel la personne concernée a sa résidence habituelle, sauf si le responsable du traitement ou le sous-traitant est une autorité publique d'un État membre agissant dans l'exercice de ses prérogatives de puissance publique. »

RÉPONSE :
Oui, l'ancien bénévole a le droit de se plaindre auprès de la CNIL, car chaque personne concernée a le droit d'introduire une réclamation auprès d'une autorité de contrôle [4]. Il peut également exercer un recours juridictionnel effectif s'il considère que ses droits ont été violés par le traitement de ses données [4]. Ce recours peut être intenté devant les juridictions de l'État membre où vous disposez d'un établissement, ou devant celles de l'État membre où il a sa résidence habituelle, « sauf si le responsable du traitement ou le sous-traitant est une autorité publique d'un État membre agissant dans l'exercice de ses prérogatives de puissance publique » [4]. Enfin, il a le droit de mandater un organisme, une organisation ou une association à but non lucratif pour qu'ils introduisent la réclamation et exercent les droits en son nom [1].
```

</details>

Temps : recherche 2.2 s · génération 2.2 s (2373 tokens lus, 585 écrits, 666.0 tokens/s) · contrôle de pertinence 0.1 s · attente des limites de l'API 14 s (non comptée)

## q37 — Si une fuite de données cause un préjudice à un client, peut-il nous demander réparation ?

Article attendu : RGPD art. 82 — absent des passages donnés au modèle.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 34 : Communication à la personne concernée d'une violation de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_34
  [2] RGPD — règlement (UE) 2016/679, article 4, définition 12 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [3] RGPD — règlement (UE) 2016/679, article 16 : Droit de rectification
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_16
  [4] RGPD — règlement (UE) 2016/679, article 17 : Droit à l'effacement («droit à l'oubli»)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_17
  [5] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun

RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Temps : recherche 2.2 s · génération 1.1 s (3158 tokens lus, 25 écrits, 198.7 tokens/s) · attente des limites de l'API 16 s (non comptée)

## q38 — Notre club de sport peut-il demander un extrait de casier judiciaire aux bénévoles qui encadrent des enfants ?

Article attendu : RGPD art. 10 — absent des passages donnés au modèle.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 60, paragraphe 5 : Essais de systèmes d’IA à haut risque en conditions réelles en dehors des bacs à sable réglementaires de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_60
  [2] AI Act — règlement (UE) 2024/1689, article 60, paragraphe 1 : Essais de systèmes d’IA à haut risque en conditions réelles en dehors des bacs à sable réglementaires de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_60
  [3] AI Act — règlement (UE) 2024/1689, article 61 : Consentement éclairé à participer aux essais en conditions réelles en dehors des bacs à sable réglementaires de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_61
  [4] AI Act — règlement (UE) 2024/1689, article 75 bis, point e : Pouvoirs de surveillance et de contrôle du Bureau de l'IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_75a
  [5] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun

RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Temps : recherche 2.2 s · génération 0.7 s (2799 tokens lus, 25 écrits, 177.3 tokens/s) · attente des limites de l'API 21 s (non comptée)

## q39 — Si nous remplaçons les noms de nos adhérents par des numéros, les données sont-elles encore des données personnelles ?

Article attendu : RGPD art. 4, définition 5 — passage [3].

### Réponse du copilote

> Oui, les données restent des données à caractère personnel car une personne physique est réputée identifiable si elle peut l'être « directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification » [2]. Le remplacement des noms par des numéros constitue une pseudonymisation, qui est définie comme un traitement permettant que les données « ne puissent plus être attribuées à une personne concernée précise sans avoir recours à des informations supplémentaires » [3]. Pour que ces données ne soient plus considérées comme personnelles, il faudrait que les informations supplémentaires (la clé de correspondance entre le numéro et la personne) soient « conservées séparément et soumises à des mesures techniques et organisationnelles afin de garantir que les données à caractère personnel ne sont pas attribuées à une personne physique identifiée ou identifiable » [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale; »
  [3] « le traitement de données à caractère personnel de telle façon que celles-ci ne puissent plus être attribuées à une personne concernée précise sans avoir recours à des informations supplémentaires, pour autant que ces informations supplémentaires soient conservées séparément et soumises à des mesures techniques et organisationnelles afin de garantir que les données à caractère personnel ne sont pas attribuées à une personne physique identifiée ou identifiable; »

Sources citées :
  [2] RGPD — règlement (UE) 2016/679, article 4, définition 1 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 5 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 96 : Relation avec les accords conclus antérieurement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_96
  [4] RGPD — règlement (UE) 2016/679, article 87 : Traitement du numéro d'identification national
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_87
  [5] RGPD — règlement (UE) 2016/679, article 47, paragraphe 2, points a) à k) : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [2] « est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale; »
- [3] « le traitement de données à caractère personnel de telle façon que celles-ci ne puissent plus être attribuées à une personne concernée précise sans avoir recours à des informations supplémentaires, pour autant que ces informations supplémentaires soient conservées séparément et soumises à des mesures techniques et organisationnelles afin de garantir que les données à caractère personnel ne sont pas attribuées à une personne physique identifiée ou identifiable; »

RÉPONSE :
Oui, les données restent des données à caractère personnel car une personne physique est réputée identifiable si elle peut l'être « directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification » [2]. Le remplacement des noms par des numéros constitue une pseudonymisation, qui est définie comme un traitement permettant que les données « ne puissent plus être attribuées à une personne concernée précise sans avoir recours à des informations supplémentaires » [3]. Pour que ces données ne soient plus considérées comme personnelles, il faudrait que les informations supplémentaires (la clé de correspondance entre le numéro et la personne) soient « conservées séparément et soumises à des mesures techniques et organisationnelles afin de garantir que les données à caractère personnel ne sont pas attribuées à une personne physique identifiée ou identifiable » [3].
```

</details>

Temps : recherche 2.2 s · génération 1.1 s (2550 tokens lus, 364 écrits, 521.2 tokens/s) · contrôle de pertinence 0.1 s · attente des limites de l'API 31 s (non comptée)

## q40 — Nous allons utiliser un logiciel d'IA à haut risque qui attribue les tâches à nos salariés : devons-nous les prévenir avant de l'utiliser ?

Article attendu : AI Act art. 26 — passage [1].

### Réponse du copilote

> Oui, vous devez prévenir vos salariés avant d'utiliser ce logiciel. L'attribution de tâches aux salariés relève des systèmes d'IA à haut risque visés par l'AI Act, « pour attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques personnelles » [3]. En tant qu'employeur et déployeur, vous avez l'obligation d'informer « les représentants des travailleurs et les travailleurs concernés qu’ils seront soumis à l’utilisation du système d’IA à haut risque » avant de le mettre en service [1]. Cette information doit être fournie « conformément aux règles et procédures prévues par le droit de l’Union et le droit national et aux pratiques en matière d’information des travailleurs et de leurs représentants » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « b) systèmes d'IA destinés à être utilisés pour prendre des décisions influant sur les conditions des relations professionnelles, la promotion ou le licenciement dans le cadre de relations professionnelles contractuelles, pour attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques personnelles ou pour suivre et évaluer les performances et le comportement de personnes dans le cadre de telles relations. »
  [1] « Avant de mettre en service ou d’utiliser un système d’IA à haut risque sur le lieu de travail, les déployeurs qui sont des employeurs informent les représentants des travailleurs et les travailleurs concernés qu’ils seront soumis à l’utilisation du système d’IA à haut risque. »
  [1] « Ces informations sont fournies, le cas échéant, conformément aux règles et procédures prévues par le droit de l’Union et le droit national et aux pratiques en matière d’information des travailleurs et de leurs représentants. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 7 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
  [3] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 1 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
  [4] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14
  [5] AI Act — règlement (UE) 2024/1689, article 9, point c : Système de gestion des risques
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_9

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [3] « b) systèmes d'IA destinés à être utilisés pour prendre des décisions influant sur les conditions des relations professionnelles, la promotion ou le licenciement dans le cadre de relations professionnelles contractuelles, pour attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques personnelles ou pour suivre et évaluer les performances et le comportement de personnes dans le cadre de telles relations. »
- [1] « Avant de mettre en service ou d’utiliser un système d’IA à haut risque sur le lieu de travail, les déployeurs qui sont des employeurs informent les représentants des travailleurs et les travailleurs concernés qu’ils seront soumis à l’utilisation du système d’IA à haut risque. »
- [1] « Ces informations sont fournies, le cas échéant, conformément aux règles et procédures prévues par le droit de l’Union et le droit national et aux pratiques en matière d’information des travailleurs et de leurs représentants. »

RÉPONSE :
Oui, vous devez prévenir vos salariés avant d'utiliser ce logiciel. L'attribution de tâches aux salariés relève des systèmes d'IA à haut risque visés par l'AI Act, « pour attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques personnelles » [3]. En tant qu'employeur et déployeur, vous avez l'obligation d'informer « les représentants des travailleurs et les travailleurs concernés qu’ils seront soumis à l’utilisation du système d’IA à haut risque » avant de le mettre en service [1]. Cette information doit être fournie « conformément aux règles et procédures prévues par le droit de l’Union et le droit national et aux pratiques en matière d’information des travailleurs et de leurs représentants » [1].
```

</details>

Temps : recherche 2.2 s · génération 1.2 s (2601 tokens lus, 382 écrits, 485.9 tokens/s) · contrôle de pertinence 0.3 s · attente des limites de l'API 22 s (non comptée)

## q41 — Notre organisme de formation peut-il utiliser une IA pour noter les examens de ses stagiaires ? Est-ce encadré ?

Article attendu : AI Act annexe III, point 3 — passage [1].

### Réponse du copilote

> Oui, votre organisme de formation peut utiliser une IA pour noter les examens, mais cette utilisation est encadrée car elle relève des systèmes d'IA à haut risque [1]. En effet, les systèmes d'IA destinés à évaluer les acquis d'apprentissage dans les établissements d'enseignement et de formation professionnelle sont explicitement listés comme haut risque [1]. Par conséquent, ce système doit permettre techniquement l'enregistrement automatique des événements (journaux) tout au long de sa durée de vie [2]. Ces fonctionnalités de journalisation doivent garantir un degré de traçabilité adapté à la destination du système [2]. De plus, l'évaluation de la conformité de ce type de système peut nécessiter l'intervention d'organismes d'évaluation de la conformité désignés [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « b) systèmes d'IA destinés à être utilisés pour évaluer les acquis d'apprentissage, y compris lorsque ceux-ci sont utilisés pour orienter le processus d'apprentissage de personnes physiques dans les établissements d'enseignement et de formation professionnelle, à tous les niveaux; »
  [1] « Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des domaines suivants: »
  [2] « 1. Les systèmes d’IA à haut risque permettent, techniquement, l’enregistrement automatique des événements (journaux) tout au long de la durée de vie du système. »
  [2] « 2. Afin de garantir un degré de traçabilité du fonctionnement d’un système d’IA qui soit adapté à la destination du système, les fonctionnalités de journalisation permettent l’enregistrement des événements pertinents pour: »
  [4] « L'évaluation de la conformité des systèmes d'IA à haut risque en vertu du présent règlement peut nécessiter l'intervention d'organismes d'évaluation de la conformité. »
  [4] « Seuls les organismes d'évaluation de la conformité qui ont été désignés conformément au présent règlement peuvent effectuer des évaluations de la conformité et uniquement pour les activités liées aux types de systèmes d'IA concernés. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, annexe III, point 3 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [2] AI Act — règlement (UE) 2024/1689, article 12 : Enregistrement (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_12
  [4] AI Act — règlement (UE) 2024/1689, annexe XIV : Liste des codes, des catégories et des types correspondants de systèmes d'IA aux fins de la procédure de notification visée à l'article 30, précisant le champ d'application de la désignation en tant qu'organismes notifiés (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_XIV
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [5] AI Act — règlement (UE) 2024/1689, article 4 : Maîtrise de l'IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_4

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « b) systèmes d'IA destinés à être utilisés pour évaluer les acquis d'apprentissage, y compris lorsque ceux-ci sont utilisés pour orienter le processus d'apprentissage de personnes physiques dans les établissements d'enseignement et de formation professionnelle, à tous les niveaux; »
- [1] « Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des domaines suivants: »
- [2] « 1. Les systèmes d’IA à haut risque permettent, techniquement, l’enregistrement automatique des événements (journaux) tout au long de la durée de vie du système. »
- [2] « 2. Afin de garantir un degré de traçabilité du fonctionnement d’un système d’IA qui soit adapté à la destination du système, les fonctionnalités de journalisation permettent l’enregistrement des événements pertinents pour: »
- [4] « L'évaluation de la conformité des systèmes d'IA à haut risque en vertu du présent règlement peut nécessiter l'intervention d'organismes d'évaluation de la conformité. »
- [4] « Seuls les organismes d'évaluation de la conformité qui ont été désignés conformément au présent règlement peuvent effectuer des évaluations de la conformité et uniquement pour les activités liées aux types de systèmes d'IA concernés. »

RÉPONSE :
Oui, votre organisme de formation peut utiliser une IA pour noter les examens, mais cette utilisation est encadrée car elle relève des systèmes d'IA à haut risque [1]. En effet, les systèmes d'IA destinés à évaluer les acquis d'apprentissage dans les établissements d'enseignement et de formation professionnelle sont explicitement listés comme haut risque [1]. Par conséquent, ce système doit permettre techniquement l'enregistrement automatique des événements (journaux) tout au long de sa durée de vie [2]. Ces fonctionnalités de journalisation doivent garantir un degré de traçabilité adapté à la destination du système [2]. De plus, l'évaluation de la conformité de ce type de système peut nécessiter l'intervention d'organismes d'évaluation de la conformité désignés [4].
```

</details>

Temps : recherche 2.2 s · génération 1.4 s (3474 tokens lus, 481 écrits, 519.7 tokens/s) · contrôle de pertinence 0.2 s · attente des limites de l'API 18 s (non comptée)

## q42 — Un candidat refusé après l'analyse de sa candidature par un outil d'IA à haut risque nous demande pourquoi : devons-nous lui expliquer ?

Article attendu : AI Act art. 86 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [2] AI Act — règlement (UE) 2024/1689, annexe III, point 3 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [3] AI Act — règlement (UE) 2024/1689, article 43, paragraphe 4 : Évaluation de la conformité
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_43
  [4] AI Act — règlement (UE) 2024/1689, article 43, paragraphe 1 : Évaluation de la conformité
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_43
  [5] AI Act — règlement (UE) 2024/1689, article 9, point c : Système de gestion des risques
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_9
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »
- [5] « c) fournir aux déployeurs les informations requises conformément à l’article 13 et, éventuellement, une formation. »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question. Ils indiquent que les systèmes d'IA utilisés pour analyser et filtrer les candidatures sont classés comme à haut risque [1]. Ils précisent également que le fournisseur doit fournir aux déployeurs les informations requises conformément à l’article 13 [5]. Cependant, les extraits fournis ne contiennent pas le texte de l'article 13 ni de disposition spécifique imposant l'obligation d'expliquer la décision de refus au candidat final.
```

</details>

Temps : recherche 2.2 s · génération 0.9 s (2313 tokens lus, 211 écrits, 459.1 tokens/s) · contrôle de pertinence 0.6 s · attente des limites de l'API 19 s (non comptée)

## q43 — Le règlement européen sur l'IA prévoit-il des mesures particulières pour les PME ?

Article attendu : AI Act art. 62 — passage [1].

### Réponse du copilote

> Oui, le règlement européen sur l'IA (AI Act) prévoit plusieurs mesures particulières pour les PME et les jeunes pousses. Les États membres doivent « accordent aux PME, y compris les jeunes pousses, qui ont leur siège social ou une succursale dans l’Union, un accès prioritaire aux bacs à sable réglementaires de l’IA, dans la mesure où elles remplissent les conditions d’éligibilité et les critères de sélection » [1]. Ils doivent également « organisent des activités spécifiques de sensibilisation et de formation à l’application du présent règlement, adaptées aux besoins des PME, y compris les jeunes pousses, les déployeurs et, si nécessaire, les pouvoirs publics locaux » [1]. De plus, les États membres « utilisent des canaux privilégiés existants et, s’il y a lieu, en établissent de nouveaux avec les PME, y compris les jeunes pousses, les déployeurs, d’autres innovateurs et, si nécessaire, les pouvoirs publics locaux, afin de fournir des conseils et de répondre aux questions relatives à la mise en œuvre du présent règlement, y compris en ce qui concerne la participation à des bacs à sable réglementaires de l’IA » [1]. Ils doivent aussi « facilitent la participation des PME et d’autres parties concernées au processus d’élaboration de la normalisation » [1]. Concernant les coûts, « Les intérêts et les besoins spécifiques des PME fournisseuses, y compris les jeunes pousses, sont pris en considération lors de la fixation des frais liés à l’évaluation de la conformité visée à l’article 43, ces frais étant réduits proportionnellement à leur taille, à la taille de leur marché et à d’autres indicateurs pertinents » [1]. Enfin, en matière de conformité, « Les PME, y compris les jeunes pousses, peuvent se conformer de manière simplifiée à certains éléments du système de gestion de la qualité requis par l'article 17, pour autant qu'elles n'aient pas d'entreprises partenaires ou d'entreprises liées au sens de la recommandation 2003/361/CE » [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les États membres: a) accordent aux PME, y compris les jeunes pousses, qui ont leur siège social ou une succursale dans l’Union, un accès prioritaire aux bacs à sable réglementaires de l’IA, dans la mesure où elles remplissent les conditions d’éligibilité et les critères de sélection; »
  [1] « b) organisent des activités spécifiques de sensibilisation et de formation à l’application du présent règlement, adaptées aux besoins des PME, y compris les jeunes pousses, les déployeurs et, si nécessaire, les pouvoirs publics locaux; »
  [1] « c) utilisent des canaux privilégiés existants et, s’il y a lieu, en établissent de nouveaux avec les PME, y compris les jeunes pousses, les déployeurs, d’autres innovateurs et, si nécessaire, les pouvoirs publics locaux, afin de fournir des conseils et de répondre aux questions relatives à la mise en œuvre du présent règlement, y compris en ce qui concerne la participation à des bacs à sable réglementaires de l’IA; »
  [1] « d) facilitent la participation des PME et d’autres parties concernées au processus d’élaboration de la normalisation. »
  [1] « Les intérêts et les besoins spécifiques des PME fournisseuses, y compris les jeunes pousses, sont pris en considération lors de la fixation des frais liés à l’évaluation de la conformité visée à l’article 43, ces frais étant réduits proportionnellement à leur taille, à la taille de leur marché et à d’autres indicateurs pertinents. »
  [2] « Les PME, y compris les jeunes pousses, peuvent se conformer de manière simplifiée à certains éléments du système de gestion de la qualité requis par l'article 17, pour autant qu'elles n'aient pas d'entreprises partenaires ou d'entreprises liées au sens de la recommandation 2003/361/CE. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 62 : Mesures en faveur des fournisseurs et déployeurs, en particulier les PME, y compris les jeunes pousses (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_62
  [2] AI Act — règlement (UE) 2024/1689, article 63 : Dérogations pour des opérateurs spécifiques (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_63
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, article 70, paragraphe 8 : Désignation des autorités nationales compétentes et des points de contact uniques
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_70
  [4] AI Act — règlement (UE) 2024/1689, article 70, paragraphe 1 : Désignation des autorités nationales compétentes et des points de contact uniques
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_70
  [5] AI Act — règlement (UE) 2024/1689, article 58, paragraphe 2 : Modalités détaillées pour les bacs à sable réglementaires de l’IA et fonctionnement de ceux-ci
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_58

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les États membres: a) accordent aux PME, y compris les jeunes pousses, qui ont leur siège social ou une succursale dans l’Union, un accès prioritaire aux bacs à sable réglementaires de l’IA, dans la mesure où elles remplissent les conditions d’éligibilité et les critères de sélection; »
- [1] « b) organisent des activités spécifiques de sensibilisation et de formation à l’application du présent règlement, adaptées aux besoins des PME, y compris les jeunes pousses, les déployeurs et, si nécessaire, les pouvoirs publics locaux; »
- [1] « c) utilisent des canaux privilégiés existants et, s’il y a lieu, en établissent de nouveaux avec les PME, y compris les jeunes pousses, les déployeurs, d’autres innovateurs et, si nécessaire, les pouvoirs publics locaux, afin de fournir des conseils et de répondre aux questions relatives à la mise en œuvre du présent règlement, y compris en ce qui concerne la participation à des bacs à sable réglementaires de l’IA; »
- [1] « d) facilitent la participation des PME et d’autres parties concernées au processus d’élaboration de la normalisation. »
- [1] « Les intérêts et les besoins spécifiques des PME fournisseuses, y compris les jeunes pousses, sont pris en considération lors de la fixation des frais liés à l’évaluation de la conformité visée à l’article 43, ces frais étant réduits proportionnellement à leur taille, à la taille de leur marché et à d’autres indicateurs pertinents. »
- [2] « Les PME, y compris les jeunes pousses, peuvent se conformer de manière simplifiée à certains éléments du système de gestion de la qualité requis par l'article 17, pour autant qu'elles n'aient pas d'entreprises partenaires ou d'entreprises liées au sens de la recommandation 2003/361/CE. »

RÉPONSE :
Oui, le règlement européen sur l'IA (AI Act) prévoit plusieurs mesures particulières pour les PME et les jeunes pousses. Les États membres doivent « accordent aux PME, y compris les jeunes pousses, qui ont leur siège social ou une succursale dans l’Union, un accès prioritaire aux bacs à sable réglementaires de l’IA, dans la mesure où elles remplissent les conditions d’éligibilité et les critères de sélection » [1]. Ils doivent également « organisent des activités spécifiques de sensibilisation et de formation à l’application du présent règlement, adaptées aux besoins des PME, y compris les jeunes pousses, les déployeurs et, si nécessaire, les pouvoirs publics locaux » [1]. De plus, les États membres « utilisent des canaux privilégiés existants et, s’il y a lieu, en établissent de nouveaux avec les PME, y compris les jeunes pousses, les déployeurs, d’autres innovateurs et, si nécessaire, les pouvoirs publics locaux, afin de fournir des conseils et de répondre aux questions relatives à la mise en œuvre du présent règlement, y compris en ce qui concerne la participation à des bacs à sable réglementaires de l’IA » [1]. Ils doivent aussi « facilitent la participation des PME et d’autres parties concernées au processus d’élaboration de la normalisation » [1]. Concernant les coûts, « Les intérêts et les besoins spécifiques des PME fournisseuses, y compris les jeunes pousses, sont pris en considération lors de la fixation des frais liés à l’évaluation de la conformité visée à l’article 43, ces frais étant réduits proportionnellement à leur taille, à la taille de leur marché et à d’autres indicateurs pertinents » [1]. Enfin, en matière de conformité, « Les PME, y compris les jeunes pousses, peuvent se conformer de manière simplifiée à certains éléments du système de gestion de la qualité requis par l'article 17, pour autant qu'elles n'aient pas d'entreprises partenaires ou d'entreprises liées au sens de la recommandation 2003/361/CE » [2].
```

</details>

Temps : recherche 2.2 s · génération 2.2 s (3193 tokens lus, 883 écrits, 511.4 tokens/s) · contrôle de pertinence 0.2 s · attente des limites de l'API 68 s (non comptée)

## q44 — À partir de quelle date devrons-nous respecter les obligations sur les systèmes d'IA à haut risque utilisés pour le recrutement ?

Article attendu : AI Act art. 113 — absent des passages donnés au modèle.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [2] AI Act — règlement (UE) 2024/1689, article 2, paragraphe 13 : Champ d’application
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_2
  [3] AI Act — règlement (UE) 2024/1689, article 2, paragraphe 1 : Champ d’application
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_2
  [4] AI Act — règlement (UE) 2024/1689, article 8 : Respect des exigences
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_8
  [5] AI Act — règlement (UE) 2024/1689, article 42 : Présomption de conformité avec certaines exigences
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_42

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun

RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Temps : recherche 2.2 s · génération 0.5 s (2578 tokens lus, 25 écrits, 458.5 tokens/s)

## h06 — Quelles mentions obligatoires doivent figurer sur une facture ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 12, paragraphe 5 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [3] AI Act — règlement (UE) 2024/1689, annexe VII, point 3 a : Conformité fondée sur une évaluation du système de gestion de la qualité et une évaluation de la documentation technique
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_VII
  [4] AI Act — règlement (UE) 2024/1689, annexe V : Déclaration UE de conformité
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_V
  [5] RGPD — règlement (UE) 2016/679, article 57, paragraphe 4 : Missions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_57

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Temps : recherche 2.2 s · génération 0.5 s (2182 tokens lus, 25 écrits, 453.3 tokens/s)

## h07 — Comment demander une subvention à la mairie pour notre association ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 61 : Assistance mutuelle
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_61
  [2] RGPD — règlement (UE) 2016/679, article 80 : Représentation des personnes concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_80
  [3] RGPD — règlement (UE) 2016/679, article 57, paragraphe 1, points a) à t) : Missions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_57
  [4] RGPD — règlement (UE) 2016/679, article 60, paragraphe 9 : Coopération entre l'autorité de contrôle chef de file et les autres autorités de contrôle concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_60
  [5] RGPD — règlement (UE) 2016/679, article 60, paragraphe 1 : Coopération entre l'autorité de contrôle chef de file et les autres autorités de contrôle concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_60

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Temps : recherche 2.2 s · génération 0.8 s (3498 tokens lus, 25 écrits, 200.2 tokens/s) · attente des limites de l'API 21 s (non comptée)

## h08 — Quelles sont les règles pour embaucher un apprenti dans une PME ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 63 : Dérogations pour des opérateurs spécifiques
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_63
  [2] AI Act — règlement (UE) 2024/1689, article 62 : Mesures en faveur des fournisseurs et déployeurs, en particulier les PME, y compris les jeunes pousses
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_62
  [3] AI Act — règlement (UE) 2024/1689, article 17, paragraphe 2 : Système de gestion de la qualité
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_17
  [4] AI Act — règlement (UE) 2024/1689, article 17, paragraphe 1 : Système de gestion de la qualité
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_17
  [5] AI Act — règlement (UE) 2024/1689, article 58, paragraphe 2 : Modalités détaillées pour les bacs à sable réglementaires de l’IA et fonctionnement de ceux-ci
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_58

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Temps : recherche 2.1 s · génération 0.5 s (3583 tokens lus, 25 écrits, 522.5 tokens/s) · attente des limites de l'API 28 s (non comptée)
