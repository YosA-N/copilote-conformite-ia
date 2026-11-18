# Réponses du copilote — v6_remote_v2

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 18/11/2026 à 18:05 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen/qwen3.8-27b` via l'API compatible OpenAI https://api.groq.com/openai/v1 (expérience de la séance 7, questions de test seulement ; modèle tel que servi par l'API à la date ci-dessus) — température 0.1, raisonnement : réglage par défaut du modèle, passages calculés pour un contexte de 8192 tokens comme en local, 2000 tokens au plus par réponse (raisonnement compris) ; le juge est le même modèle
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu, reranker `BAAI/bge-reranker-v2-m3` sur CPU (20 candidats reclassés avant la limite par article), reformulation de la question par le modèle avant la recherche (termes juridiques ajoutés, sans conclusion)
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_v2.jsonl` (17 + 3 hors sujet)
- Reprise : 18 réponse(s) conservée(s) d'une série précédente arrêtée en cours de route (par exemple par le quota de l'API), 1 générée(s) à la date ci-dessus

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q28 | Un adhérent nous signale que son adresse et sa date de naissance sont fausses dans notre fichier : devons-nous les corriger, et dans quel délai ? | 4/4 | non | — | 45 s |
| q29 | Une cliente conteste l'exactitude des informations que nous avons sur elle : pouvons-nous continuer à les utiliser pendant que nous vérifions ? | 3/3 | non | La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Non, vous ne pouvez pas continuer à utiliser les données de manière habituelle pendant la vérification, car la cliente … ». Vérifiez ce point. | 28 s |
| q30 | Pouvons-nous refuser automatiquement une demande d'inscription à notre service à partir d'un score calculé par un logiciel, sans qu'une personne ne vérifie ? | 4/4 | non | — | 30 s |
| q31 | Nous faisons développer une application mobile pour nos membres : quelles précautions de protection des données devons-nous prévoir dès sa conception ? | 4/6 | non | 2 extrait(s) introuvable(s) mot pour mot dans le passage cité ([32], [32]) : ignoré(s).; Citation vers un passage inexistant : [32] (seuls les passages [1] à [5] ont été fournis). | 30 s |
| q32 | Nous organisons un festival avec une autre association et nous gérons ensemble le fichier des participants : qui est responsable de ces données ? | 6/6 | non | — | 30 s |
| q33 | Nous avons acheté un fichier de prospects à une autre entreprise : devons-nous informer ces personnes, et dans quel délai ? | 6/6 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 30 s |
| q34 | Puis-je installer des caméras dans l'atelier pour surveiller le travail de mes salariés ? | 4/6 | non | 2 extrait(s) introuvable(s) mot pour mot dans le passage cité ([13], [13]) : ignoré(s).; Citation vers un passage inexistant : [13] (seuls les passages [1] à [5] ont été fournis).; La réponse met entre « » un texte introuvable dans les extraits vérifiés : « finalités du traitement ». | 33 s |
| q35 | Notre fédération sportive peut-elle rédiger un guide de bonnes pratiques RGPD que ses clubs pourraient suivre officiellement ? | 6/6 | non | — | 27 s |
| q36 | Un ancien bénévole menace de se plaindre de nous auprès de la CNIL : en a-t-il le droit, et quels autres recours a-t-il ? | 4/4 | non | — | 27 s |
| q37 | Si une fuite de données cause un préjudice à un client, peut-il nous demander réparation ? | 3/3 | non | — | 29 s |
| q38 | Notre club de sport peut-il demander un extrait de casier judiciaire aux bénévoles qui encadrent des enfants ? | 0/3 | oui | Aucun des 3 extrait(s) recopié(s) par le modèle n'a été retrouvé mot pour mot dans les passages : sa réponse a été remplacée par un refus. | 28 s |
| q39 | Si nous remplaçons les noms de nos adhérents par des numéros, les données sont-elles encore des données personnelles ? | 2/2 | non | — | 30 s |
| q40 | Nous allons utiliser un logiciel d'IA à haut risque qui attribue les tâches à nos salariés : devons-nous les prévenir avant de l'utiliser ? | 3/3 | non | La réponse met entre « » un texte introuvable dans les extraits vérifiés : « destiné à être utilisés pour [...] attribuer des tâches sur la base du comportement individuel, de traits de … ». | 30 s |
| q41 | Notre organisme de formation peut-il utiliser une IA pour noter les examens de ses stagiaires ? Est-ce encadré ? | 6/6 | non | — | 29 s |
| q42 | Un candidat refusé après l'analyse de sa candidature par un outil d'IA à haut risque nous demande pourquoi : devons-nous lui expliquer ? | 3/3 | non | — | 25 s |
| q43 | Le règlement européen sur l'IA prévoit-il des mesures particulières pour les PME ? | 6/6 | non | La réponse met entre « » un texte introuvable dans les extraits vérifiés : « organiser des activités spécifiques de sensibilisation et de formation à l'application du présent règlement, adaptées … » (et 1 autre(s)). | 31 s |
| q44 | À partir de quelle date devrons-nous respecter les obligations sur les systèmes d'IA à haut risque utilisés pour le recrutement ? | 4/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 27 s |
| h06 | Quelles mentions obligatoires doivent figurer sur une facture ? | 0/0 | oui | — | 50 s |
| h07 | Comment demander une subvention à la mairie pour notre association ? | 0/0 | oui | — | 41 s |

## q28 — Un adhérent nous signale que son adresse et sa date de naissance sont fausses dans notre fichier : devons-nous les corriger, et dans quel délai ?

Article attendu : RGPD art. 16 — passage [1].

### Réponse du copilote

> Oui, vous devez corriger l'adresse et la date de naissance de l'adhérent, car la personne concernée a le droit d'obtenir la rectification des données inexactes « dans les meilleurs délais » [1]. En tant que responsable du traitement, vous devez fournir des informations sur les mesures prises à la suite de cette demande « dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande » [2]. Si la situation le nécessite, ce délai « peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes » [2], mais vous devez alors informer la personne concernée de cette prolongation et des motifs du report « dans un délai d'un mois à compter de la réception de la demande » [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit d'obtenir du responsable du traitement, dans les meilleurs délais, la rectification des données à caractère personnel la concernant qui sont inexactes. »
  [2] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. »
  [2] « Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. »
  [2] « Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 16 : Droit de rectification (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_16
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [4] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [5] RGPD — règlement (UE) 2016/679, article 12, paragraphe 4 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « La personne concernée a le droit d'obtenir du responsable du traitement, dans les meilleurs délais, la rectification des données à caractère personnel la concernant qui sont inexactes. »
- [2] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. »
- [2] « Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. »
- [2] « Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. »

RÉPONSE :
Oui, vous devez corriger l'adresse et la date de naissance de l'adhérent, car la personne concernée a le droit d'obtenir la rectification des données inexactes « dans les meilleurs délais » [1]. En tant que responsable du traitement, vous devez fournir des informations sur les mesures prises à la suite de cette demande « dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande » [2]. Si la situation le nécessite, ce délai « peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes » [2], mais vous devez alors informer la personne concernée de cette prolongation et des motifs du report « dans un délai d'un mois à compter de la réception de la demande » [2].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit à la rectification ; données à caractère personnel ; responsable du traitement ; délai d'un mois

Temps : recherche 42.8 s · génération 1.2 s (2389 tokens lus, 364 écrits, 480.1 tokens/s) · contrôle de pertinence 0.5 s · reformulation 0.6 s

## q29 — Une cliente conteste l'exactitude des informations que nous avons sur elle : pouvons-nous continuer à les utiliser pendant que nous vérifions ?

Article attendu : RGPD art. 18 — passage [1].

### Réponse du copilote

> Non, vous ne pouvez pas continuer à utiliser les données de manière habituelle pendant la vérification, car la cliente a le droit d'obtenir la limitation du traitement lorsque l'exactitude des données est contestée [1]. Dans cette situation, les données ne peuvent, « à l'exception de la conservation, être traitées qu'avec le consentement de la personne concernée, ou pour la constatation, l'exercice ou la défense de droits en justice, ou pour la protection des droits d'une autre personne physique ou morale, ou encore pour des motifs importants d'intérêt public de l'Union ou d'un État membre » [1]. Vous devez également informer la cliente avant de lever cette limitation [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « a) l'exactitude des données à caractère personnel est contestée par la personne concernée, pendant une durée permettant au responsable du traitement de vérifier l'exactitude des données à caractère personnel; »
  [1] « 2. Lorsque le traitement a été limité en vertu du paragraphe 1, ces données à caractère personnel ne peuvent, à l'exception de la conservation, être traitées qu'avec le consentement de la personne concernée, ou pour la constatation, l'exercice ou la défense de droits en justice, ou pour la protection des droits d'une autre personne physique ou morale, ou encore pour des motifs importants d'intérêt public de l'Union ou d'un État membre. »
  [1] « 3. Une personne concernée qui a obtenu la limitation du traitement en vertu du paragraphe 1 est informée par le responsable du traitement avant que la limitation du traitement ne soit levée. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 18 : Droit à la limitation du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_18
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 16 : Droit de rectification
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_16
  [3] RGPD — règlement (UE) 2016/679, article 21 : Droit d'opposition
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_21
  [4] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [5] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
Attention : La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Non, vous ne pouvez pas continuer à utiliser les données de manière habituelle pendant la vérification, car la cliente … ». Vérifiez ce point.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « a) l'exactitude des données à caractère personnel est contestée par la personne concernée, pendant une durée permettant au responsable du traitement de vérifier l'exactitude des données à caractère personnel; »
- [1] « 2. Lorsque le traitement a été limité en vertu du paragraphe 1, ces données à caractère personnel ne peuvent, à l'exception de la conservation, être traitées qu'avec le consentement de la personne concernée, ou pour la constatation, l'exercice ou la défense de droits en justice, ou pour la protection des droits d'une autre personne physique ou morale, ou encore pour des motifs importants d'intérêt public de l'Union ou d'un État membre. »
- [1] « 3. Une personne concernée qui a obtenu la limitation du traitement en vertu du paragraphe 1 est informée par le responsable du traitement avant que la limitation du traitement ne soit levée. »

RÉPONSE :
Non, vous ne pouvez pas continuer à utiliser les données de manière habituelle pendant la vérification, car la cliente a le droit d'obtenir la limitation du traitement lorsque l'exactitude des données est contestée [1]. Dans cette situation, les données ne peuvent, « à l'exception de la conservation, être traitées qu'avec le consentement de la personne concernée, ou pour la constatation, l'exercice ou la défense de droits en justice, ou pour la protection des droits d'une autre personne physique ou morale, ou encore pour des motifs importants d'intérêt public de l'Union ou d'un État membre » [1]. Vous devez également informer la cliente avant de lever cette limitation [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit de rectification ; données inexactes ; traitement des données ; vérification de l'exactitude ; suspension du traitement

Temps : recherche 26.5 s · génération 1.2 s (3224 tokens lus, 361 écrits, 464.8 tokens/s) · contrôle de pertinence 0.3 s · reformulation 0.2 s

## q30 — Pouvons-nous refuser automatiquement une demande d'inscription à notre service à partir d'un score calculé par un logiciel, sans qu'une personne ne vérifie ?

Article attendu : RGPD art. 22 — passage [1].

### Réponse du copilote

> En principe, vous ne pouvez pas refuser automatiquement une demande d'inscription si ce refus produit des effets juridiques ou affecte significativement la personne, car elle a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé [1]. Cependant, cette interdiction ne s'applique pas si la décision est « nécessaire à la conclusion ou à l'exécution d'un contrat entre la personne concernée et un responsable du traitement » [1]. Dans ce cas spécifique, vous devez tout de même mettre en œuvre des mesures appropriées, garantissant au minimum le droit de la personne d'« obtenir une intervention humaine de la part du responsable du traitement, d'exprimer son point de vue et de contester la décision » [1]. Le calcul d'un score pour évaluer des aspects personnels relève de la définition du profilage [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé, y compris le profilage, produisant des effets juridiques la concernant ou l'affectant de manière significative de façon similaire. »
  [1] « Le paragraphe 1 ne s'applique pas lorsque la décision: a) est nécessaire à la conclusion ou à l'exécution d'un contrat entre la personne concernée et un responsable du traitement; »
  [1] « Dans les cas visés au paragraphe 2, points a) et c), le responsable du traitement met en œuvre des mesures appropriées pour la sauvegarde des droits et libertés et des intérêts légitimes de la personne concernée, au moins du droit de la personne concernée d'obtenir une intervention humaine de la part du responsable du traitement, d'exprimer son point de vue et de contester la décision. »
  [2] « «profilage», toute forme de traitement automatisé de données à caractère personnel consistant à utiliser ces données à caractère personnel pour évaluer certains aspects personnels relatifs à une personne physique, notamment pour analyser ou prédire des éléments concernant le rendement au travail, la situation économique, la santé, les préférences personnelles, les intérêts, la fiabilité, le comportement, la localisation ou les déplacements de cette personne physique; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 22 : Décision individuelle automatisée, y compris le profilage (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_22
  [2] RGPD — règlement (UE) 2016/679, article 4, définition 4 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 35, paragraphe 3 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [4] RGPD — règlement (UE) 2016/679, article 35, paragraphe 1 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [5] AI Act — règlement (UE) 2024/1689, article 6, point c : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « La personne concernée a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé, y compris le profilage, produisant des effets juridiques la concernant ou l'affectant de manière significative de façon similaire. »
- [1] « Le paragraphe 1 ne s'applique pas lorsque la décision: a) est nécessaire à la conclusion ou à l'exécution d'un contrat entre la personne concernée et un responsable du traitement; »
- [1] « Dans les cas visés au paragraphe 2, points a) et c), le responsable du traitement met en œuvre des mesures appropriées pour la sauvegarde des droits et libertés et des intérêts légitimes de la personne concernée, au moins du droit de la personne concernée d'obtenir une intervention humaine de la part du responsable du traitement, d'exprimer son point de vue et de contester la décision. »
- [2] « «profilage», toute forme de traitement automatisé de données à caractère personnel consistant à utiliser ces données à caractère personnel pour évaluer certains aspects personnels relatifs à une personne physique, notamment pour analyser ou prédire des éléments concernant le rendement au travail, la situation économique, la santé, les préférences personnelles, les intérêts, la fiabilité, le comportement, la localisation ou les déplacements de cette personne physique; »

RÉPONSE :
En principe, vous ne pouvez pas refuser automatiquement une demande d'inscription si ce refus produit des effets juridiques ou affecte significativement la personne, car elle a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé [1]. Cependant, cette interdiction ne s'applique pas si la décision est « nécessaire à la conclusion ou à l'exécution d'un contrat entre la personne concernée et un responsable du traitement » [1]. Dans ce cas spécifique, vous devez tout de même mettre en œuvre des mesures appropriées, garantissant au minimum le droit de la personne d'« obtenir une intervention humaine de la part du responsable du traitement, d'exprimer son point de vue et de contester la décision » [1]. Le calcul d'un score pour évaluer des aspects personnels relève de la définition du profilage [2].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : décision automatisée ; profilage ; mesures appropriées ; intervention humaine ; droit d'obtenir une intervention humaine ; mesures de sauvegarde

Temps : recherche 26.3 s · génération 2.2 s (2178 tokens lus, 483 écrits, 445.9 tokens/s) · contrôle de pertinence 0.8 s · reformulation 0.2 s · attente des limites de l'API 32 s (non comptée)

## q31 — Nous faisons développer une application mobile pour nos membres : quelles précautions de protection des données devons-nous prévoir dès sa conception ?

Article attendu : RGPD art. 25 — passage [1].

### Réponse du copilote

> En tant que responsable du traitement, vous devez intégrer la protection des données dès la conception de l'application mobile, conformément à l'article 25 du RGPD. Cela implique de mettre en œuvre des mesures techniques et organisationnelles appropriées, telles que la pseudonymisation, pour garantir la minimisation des données et protéger les droits des personnes concernées [1]. Vous devez également vous assurer que, par défaut, seules les données strictement nécessaires à chaque finalité spécifique sont traitées, ce qui concerne la quantité de données collectées, leur durée de conservation et leur accessibilité [1]. En particulier, les données ne doivent pas être accessibles à un nombre indéterminé de personnes sans l'intervention de la personne concernée [1]. Par ailleurs, l'article 32 du RGPD impose au responsable du traitement et au sous-traitant de garantir un niveau de sécurité adapté au risque, notamment par la pseudonymisation et le chiffrement des données, ainsi que par des moyens assurant la confidentialité, l'intégrité, la disponibilité et la résilience des systèmes [32].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « le responsable du traitement met en œuvre, tant au moment de la détermination des moyens du traitement qu'au moment du traitement lui-même, des mesures techniques et organisationnelles appropriées, telles que la pseudonymisation, qui sont destinées à mettre en œuvre les principes relatifs à la protection des données, par exemple la minimisation des données, de façon effective et à assortir le traitement des garanties nécessaires afin de répondre aux exigences du présent règlement et de protéger les droits de la personne concernée. »
  [1] « Le responsable du traitement met en œuvre les mesures techniques et organisationnelles appropriées pour garantir que, par défaut, seules les données à caractère personnel qui sont nécessaires au regard de chaque finalité spécifique du traitement sont traitées. »
  [1] « Cela s'applique à la quantité de données à caractère personnel collectées, à l'étendue de leur traitement, à leur durée de conservation et à leur accessibilité. »
  [1] « En particulier, ces mesures garantissent que, par défaut, les données à caractère personnel ne sont pas rendues accessibles à un nombre indéterminé de personnes physiques sans l'intervention de la personne physique concernée. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 25 : Protection des données dès la conception et protection des données par défaut (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_25
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 45, paragraphe 2 : Transferts fondés sur une décision d'adéquation
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
  [3] RGPD — règlement (UE) 2016/679, article 45, paragraphe 1 : Transferts fondés sur une décision d'adéquation
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
  [4] RGPD — règlement (UE) 2016/679, article 35, paragraphe 7 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [5] RGPD — règlement (UE) 2016/679, article 32 : Sécurité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_32
Attention : 2 extrait(s) introuvable(s) mot pour mot dans le passage cité ([32], [32]) : ignoré(s).
Attention : Citation vers un passage inexistant : [32] (seuls les passages [1] à [5] ont été fournis).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « le responsable du traitement met en œuvre, tant au moment de la détermination des moyens du traitement qu'au moment du traitement lui-même, des mesures techniques et organisationnelles appropriées, telles que la pseudonymisation, qui sont destinées à mettre en œuvre les principes relatifs à la protection des données, par exemple la minimisation des données, de façon effective et à assortir le traitement des garanties nécessaires afin de répondre aux exigences du présent règlement et de protéger les droits de la personne concernée. »
- [1] « Le responsable du traitement met en œuvre les mesures techniques et organisationnelles appropriées pour garantir que, par défaut, seules les données à caractère personnel qui sont nécessaires au regard de chaque finalité spécifique du traitement sont traitées. »
- [1] « Cela s'applique à la quantité de données à caractère personnel collectées, à l'étendue de leur traitement, à leur durée de conservation et à leur accessibilité. »
- [1] « En particulier, ces mesures garantissent que, par défaut, les données à caractère personnel ne sont pas rendues accessibles à un nombre indéterminé de personnes physiques sans l'intervention de la personne physique concernée. »
- [32] « le responsable du traitement et le sous-traitant mettent en œuvre les mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque, y compris entre autres, selon les besoins: a) la pseudonymisation et le chiffrement des données à caractère personnel; »
- [32] « b) des moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement; »

RÉPONSE :
En tant que responsable du traitement, vous devez intégrer la protection des données dès la conception de l'application mobile, conformément à l'article 25 du RGPD. Cela implique de mettre en œuvre des mesures techniques et organisationnelles appropriées, telles que la pseudonymisation, pour garantir la minimisation des données et protéger les droits des personnes concernées [1]. Vous devez également vous assurer que, par défaut, seules les données strictement nécessaires à chaque finalité spécifique sont traitées, ce qui concerne la quantité de données collectées, leur durée de conservation et leur accessibilité [1]. En particulier, les données ne doivent pas être accessibles à un nombre indéterminé de personnes sans l'intervention de la personne concernée [1]. Par ailleurs, l'article 32 du RGPD impose au responsable du traitement et au sous-traitant de garantir un niveau de sécurité adapté au risque, notamment par la pseudonymisation et le chiffrement des données, ainsi que par des moyens assurant la confidentialité, l'intégrité, la disponibilité et la résilience des systèmes [32].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : protection des données dès la conception ; protection des données par défaut ; minimisation des données ; limitation de la finalité ; sécurité des données ; registre des activités de traitement

Temps : recherche 27.5 s · génération 1.6 s (2791 tokens lus, 593 écrits, 453.6 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.4 s · attente des limites de l'API 2 s (non comptée)

## q32 — Nous organisons un festival avec une autre association et nous gérons ensemble le fichier des participants : qui est responsable de ces données ?

Article attendu : RGPD art. 26 — passage [1].

### Réponse du copilote

> Vous et l'autre association êtes les « responsables conjoints du traitement » car vous déterminez conjointement les finalités et les moyens du traitement [1]. Cette qualification s'applique car le responsable du traitement est celui qui, « seul ou conjointement avec d'autres, détermine les finalités et les moyens du traitement » [2]. Vous devez définir de manière transparente vos obligations respectives, notamment pour l'exercice des droits des participants et la communication des informations, par voie d'accord entre vous, « sauf si, et dans la mesure, où leurs obligations respectives sont définies par le droit de l'Union ou par le droit de l'État membre auquel les responsables du traitement sont soumis » [1]. Cet accord doit refléter vos rôles respectifs et ses grandes lignes doivent être mises à la disposition des personnes concernées [1]. Enfin, chaque participant peut exercer ses droits à l'égard de et contre chacun des responsables du traitement, indépendamment des termes de votre accord [1].

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
  [5] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40

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
Vous et l'autre association êtes les « responsables conjoints du traitement » car vous déterminez conjointement les finalités et les moyens du traitement [1]. Cette qualification s'applique car le responsable du traitement est celui qui, « seul ou conjointement avec d'autres, détermine les finalités et les moyens du traitement » [2]. Vous devez définir de manière transparente vos obligations respectives, notamment pour l'exercice des droits des participants et la communication des informations, par voie d'accord entre vous, « sauf si, et dans la mesure, où leurs obligations respectives sont définies par le droit de l'Union ou par le droit de l'État membre auquel les responsables du traitement sont soumis » [1]. Cet accord doit refléter vos rôles respectifs et ses grandes lignes doivent être mises à la disposition des personnes concernées [1]. Enfin, chaque participant peut exercer ses droits à l'égard de et contre chacun des responsables du traitement, indépendamment des termes de votre accord [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : responsable du traitement ; co-responsable du traitement ; traitement conjoint

Temps : recherche 27.1 s · génération 1.9 s (2980 tokens lus, 552 écrits, 468.6 tokens/s) · contrôle de pertinence 0.7 s · reformulation 0.2 s · attente des limites de l'API 48 s (non comptée)

## q33 — Nous avons acheté un fichier de prospects à une autre entreprise : devons-nous informer ces personnes, et dans quel délai ?

Article attendu : RGPD art. 14 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 28, paragraphe 3 : Sous-traitant
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [3] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30
  [4] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [5] RGPD — règlement (UE) 2016/679, article 90 : Obligations de secret
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_90
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [4] « Lorsque des données à caractère personnel relatives à une personne concernée sont collectées auprès de cette personne, le responsable du traitement lui fournit, au moment où les données en question sont obtenues, toutes les informations suivantes: »
- [4] « les finalités du traitement auquel sont destinées les données à caractère personnel ainsi que la base juridique du traitement; »
- [4] « les destinataires ou les catégories de destinataires des données à caractère personnel, s'ils existent; et »
- [4] « la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; »
- [4] « l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ou du droit de s'opposer au traitement et du droit à la portabilité des données; »
- [4] « le droit d'introduire une réclamation auprès d'une autorité de contrôle; »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question.
Le texte fourni précise uniquement les informations à fournir « lorsque des données à caractère personnel relatives à une personne concernée sont collectées auprès de cette personne » [4].
Il ne contient aucune disposition spécifique concernant l'achat d'un fichier de prospects ou la collecte de données auprès d'un tiers.
Par conséquent, les extraits ne permettent pas de déterminer si vous devez informer ces personnes ni quel délai s'applique dans ce cas précis.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données à caractère personnel ; responsable du traitement ; sous-traitant ; information des personnes concernées ; registre des traitements

Temps : recherche 27.1 s · génération 1.4 s (3927 tokens lus, 348 écrits, 452.1 tokens/s) · contrôle de pertinence 1.1 s · reformulation 0.4 s

## q34 — Puis-je installer des caméras dans l'atelier pour surveiller le travail de mes salariés ?

Article attendu : RGPD art. 88 — passage [1].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question, car ils ne mentionnent pas explicitement l'installation de caméras, mais ils posent les principes généraux applicables au traitement des données des salariés. En tant qu'employeur, vous êtes le responsable du traitement et devez respecter les règles spécifiques prévues par les États membres pour le traitement des données des employés dans le cadre des relations de travail [1]. Ces règles nationales doivent inclure des mesures pour protéger la dignité humaine et accorder une « attention particulière à la transparence du traitement » ainsi qu'aux « systèmes de contrôle sur le lieu de travail » [1]. Vous devez traiter les données de manière « licite, loyale et transparente » et les limiter à ce qui est « nécessaire au regard des finalités » [4]. De plus, vous devez informer les salariés de l'identité du responsable du traitement et des « finalités du traitement » ainsi que de la base juridique [13].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les États membres peuvent prévoir, par la loi ou au moyen de conventions collectives, des règles plus spécifiques pour assurer la protection des droits et libertés en ce qui concerne le traitement des données à caractère personnel des employés dans le cadre des relations de travail, aux fins, notamment, du recrutement, de l'exécution du contrat de travail, y compris le respect des obligations fixées par la loi ou par des conventions collectives, de la gestion, de la planification et de l'organisation du travail, de l'égalité et de la diversité sur le lieu de travail, de la santé et de la sécurité au travail, de la protection des biens appartenant à l'employeur ou au client, aux fins de l'exercice et de la jouissance des droits et des avantages liés à l'emploi, individuellement ou collectivement, ainsi qu'aux fins de la résiliation de la relation de travail. »
  [1] « Ces règles comprennent des mesures appropriées et spécifiques pour protéger la dignité humaine, les intérêts légitimes et les droits fondamentaux des personnes concernées, en accordant une attention particulière à la transparence du traitement, au transfert de données à caractère personnel au sein d'un groupe d'entreprises, ou d'un groupe d'entreprises engagées dans une activité économique conjointe et aux systèmes de contrôle sur le lieu de travail. »
  [4] « Les données à caractère personnel doivent être: a) traitées de manière licite, loyale et transparente au regard de la personne concernée (licéité, loyauté, transparence); »
  [4] « c) adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités pour lesquelles elles sont traitées (minimisation des données); »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [4] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 1 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [5] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
Attention : 2 extrait(s) introuvable(s) mot pour mot dans le passage cité ([13], [13]) : ignoré(s).
Attention : Citation vers un passage inexistant : [13] (seuls les passages [1] à [5] ont été fournis).
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « finalités du traitement ».

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les États membres peuvent prévoir, par la loi ou au moyen de conventions collectives, des règles plus spécifiques pour assurer la protection des droits et libertés en ce qui concerne le traitement des données à caractère personnel des employés dans le cadre des relations de travail, aux fins, notamment, du recrutement, de l'exécution du contrat de travail, y compris le respect des obligations fixées par la loi ou par des conventions collectives, de la gestion, de la planification et de l'organisation du travail, de l'égalité et de la diversité sur le lieu de travail, de la santé et de la sécurité au travail, de la protection des biens appartenant à l'employeur ou au client, aux fins de l'exercice et de la jouissance des droits et des avantages liés à l'emploi, individuellement ou collectivement, ainsi qu'aux fins de la résiliation de la relation de travail. »
- [1] « Ces règles comprennent des mesures appropriées et spécifiques pour protéger la dignité humaine, les intérêts légitimes et les droits fondamentaux des personnes concernées, en accordant une attention particulière à la transparence du traitement, au transfert de données à caractère personnel au sein d'un groupe d'entreprises, ou d'un groupe d'entreprises engagées dans une activité économique conjointe et aux systèmes de contrôle sur le lieu de travail. »
- [4] « Les données à caractère personnel doivent être: a) traitées de manière licite, loyale et transparente au regard de la personne concernée (licéité, loyauté, transparence); »
- [4] « c) adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités pour lesquelles elles sont traitées (minimisation des données); »
- [13] « Lorsque des données à caractère personnel relatives à une personne concernée sont collectées auprès de cette personne, le responsable du traitement lui fournit, au moment où les données en question sont obtenues, toutes les informations suivantes: a) l'identité et les coordonnées du responsable du traitement et, le cas échéant, du représentant du responsable du traitement »
- [13] « c) les finalités du traitement auquel sont destinées les données à caractère personnel ainsi que la base juridique du traitement; »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question, car ils ne mentionnent pas explicitement l'installation de caméras, mais ils posent les principes généraux applicables au traitement des données des salariés. En tant qu'employeur, vous êtes le responsable du traitement et devez respecter les règles spécifiques prévues par les États membres pour le traitement des données des employés dans le cadre des relations de travail [1]. Ces règles nationales doivent inclure des mesures pour protéger la dignité humaine et accorder une « attention particulière à la transparence du traitement » ainsi qu'aux « systèmes de contrôle sur le lieu de travail » [1]. Vous devez traiter les données de manière « licite, loyale et transparente » et les limiter à ce qui est « nécessaire au regard des finalités » [4]. De plus, vous devez informer les salariés de l'identité du responsable du traitement et des « finalités du traitement » ainsi que de la base juridique [13].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : traitement de données à caractère personnel ; vidéosurveillance ; données relatives à la localisation ; consentement ; droits des personnes concernées

Temps : recherche 29.5 s · génération 2.0 s (3624 tokens lus, 693 écrits, 451.8 tokens/s) · contrôle de pertinence 0.9 s · reformulation 0.8 s · attente des limites de l'API 32 s (non comptée)

## q35 — Notre fédération sportive peut-elle rédiger un guide de bonnes pratiques RGPD que ses clubs pourraient suivre officiellement ?

Article attendu : RGPD art. 40 — passage [2].

### Réponse du copilote

> Oui, votre fédération sportive peut rédiger un tel guide, car les associations représentant des catégories de responsables du traitement « peuvent élaborer des codes de conduite » pour préciser les modalités d'application du RGPD [2]. Ce document doit viser à préciser des aspects spécifiques tels que « le traitement loyal et transparent » [2], « les intérêts légitimes poursuivis par les responsables du traitement dans des contextes spécifiques » [2], « la collecte des données à caractère personnel » [2], « la pseudonymisation des données à caractère personnel » [2] ou « les informations communiquées au public et aux personnes concernées » [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « Les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent élaborer des codes de conduite, les modifier ou les proroger, aux fins de préciser les modalités d'application du présent règlement, telles que: »
  [2] « a) le traitement loyal et transparent; »
  [2] « b) les intérêts légitimes poursuivis par les responsables du traitement dans des contextes spécifiques; »
  [2] « c) la collecte des données à caractère personnel; »
  [2] « d) la pseudonymisation des données à caractère personnel; »
  [2] « e) les informations communiquées au public et aux personnes concernées; »

Sources citées :
  [2] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
  [3] RGPD — règlement (UE) 2016/679, article 70, paragraphe 1, points a) à l) : Missions du comité
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_70
  [4] RGPD — règlement (UE) 2016/679, article 1 : Objet et objectifs
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_1
  [5] RGPD — règlement (UE) 2016/679, article 45, paragraphe 2 : Transferts fondés sur une décision d'adéquation
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [2] « Les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent élaborer des codes de conduite, les modifier ou les proroger, aux fins de préciser les modalités d'application du présent règlement, telles que: »
- [2] « a) le traitement loyal et transparent; »
- [2] « b) les intérêts légitimes poursuivis par les responsables du traitement dans des contextes spécifiques; »
- [2] « c) la collecte des données à caractère personnel; »
- [2] « d) la pseudonymisation des données à caractère personnel; »
- [2] « e) les informations communiquées au public et aux personnes concernées; »

RÉPONSE :
Oui, votre fédération sportive peut rédiger un tel guide, car les associations représentant des catégories de responsables du traitement « peuvent élaborer des codes de conduite » pour préciser les modalités d'application du RGPD [2]. Ce document doit viser à préciser des aspects spécifiques tels que « le traitement loyal et transparent » [2], « les intérêts légitimes poursuivis par les responsables du traitement dans des contextes spécifiques » [2], « la collecte des données à caractère personnel » [2], « la pseudonymisation des données à caractère personnel » [2] ou « les informations communiquées au public et aux personnes concernées » [2].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : document d'orientation ; recommandations ; bonnes pratiques ; mesures techniques et organisationnelles ; conformité au droit de l'Union ; traitement de données à caractère personnel

Temps : recherche 25.8 s · génération 1.1 s (3448 tokens lus, 298 écrits, 433.9 tokens/s) · contrôle de pertinence 0.3 s · reformulation 0.2 s · attente des limites de l'API 9 s (non comptée)

## q36 — Un ancien bénévole menace de se plaindre de nous auprès de la CNIL : en a-t-il le droit, et quels autres recours a-t-il ?

Article attendu : RGPD art. 77 — passage [1].

### Réponse du copilote

> Oui, votre ancien bénévole a le droit de se plaindre auprès de la CNIL, car « toute personne concernée a le droit d'introduire une réclamation auprès d'une autorité de contrôle » si elle estime que le traitement de ses données viole le règlement [1]. Il peut également choisir de mandater une association à but non lucratif active dans la protection des données pour qu'elle introduise la réclamation en son nom [2]. En plus de la réclamation administrative, il dispose du droit à un « recours juridictionnel effectif » s'il considère que ses droits ont été violés par le traitement de ses données [4]. Il peut aussi saisir la justice si l'autorité de contrôle ne traite pas sa réclamation ou ne l'informe pas de son issue « dans un délai de trois mois » [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « toute personne concernée a le droit d'introduire une réclamation auprès d'une autorité de contrôle, en particulier dans l'État membre dans lequel se trouve sa résidence habituelle, son lieu de travail ou le lieu où la violation aurait été commise, si elle considère que le traitement de données à caractère personnel la concernant constitue une violation du présent règlement. »
  [2] « La personne concernée a le droit de mandater un organisme, une organisation ou une association à but non lucratif, qui a été valablement constitué conformément au droit d'un État membre, dont les objectifs statutaires sont d'intérêt public et est actif dans le domaine de la protection des droits et libertés des personnes concernées dans le cadre de la protection des données à caractère personnel les concernant, pour qu'il introduise une réclamation en son nom, exerce en son nom les droits visés aux articles 77, 78 et 79 et exerce en son nom le droit d'obtenir réparation visé à l'article 82 lorsque le droit d'un État membre le prévoit. »
  [3] « toute personne concernée a le droit de former un recours juridictionnel effectif lorsque l'autorité de contrôle qui est compétente en vertu des articles 55 et 56 ne traite pas une réclamation ou n'informe pas la personne concernée, dans un délai de trois mois, de l'état d'avancement ou de l'issue de la réclamation qu'elle a introduite au titre de l'article 77. »
  [4] « chaque personne concernée a droit à un recours juridictionnel effectif si elle considère que les droits que lui confère le présent règlement ont été violés du fait d'un traitement de ses données à caractère personnel effectué en violation du présent règlement. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 77 : Droit d'introduire une réclamation auprès d'une autorité de contrôle (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_77
  [2] RGPD — règlement (UE) 2016/679, article 80 : Représentation des personnes concernées (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_80
  [3] RGPD — règlement (UE) 2016/679, article 78 : Droit à un recours juridictionnel effectif contre une autorité de contrôle (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_78
  [4] RGPD — règlement (UE) 2016/679, article 79 : Droit à un recours juridictionnel effectif contre un responsable du traitement ou un sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_79
Passages consultés mais non cités :
  [5] RGPD — règlement (UE) 2016/679, article 58, paragraphe 4 : Pouvoirs
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_58

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « toute personne concernée a le droit d'introduire une réclamation auprès d'une autorité de contrôle, en particulier dans l'État membre dans lequel se trouve sa résidence habituelle, son lieu de travail ou le lieu où la violation aurait été commise, si elle considère que le traitement de données à caractère personnel la concernant constitue une violation du présent règlement. »
- [2] « La personne concernée a le droit de mandater un organisme, une organisation ou une association à but non lucratif, qui a été valablement constitué conformément au droit d'un État membre, dont les objectifs statutaires sont d'intérêt public et est actif dans le domaine de la protection des droits et libertés des personnes concernées dans le cadre de la protection des données à caractère personnel les concernant, pour qu'il introduise une réclamation en son nom, exerce en son nom les droits visés aux articles 77, 78 et 79 et exerce en son nom le droit d'obtenir réparation visé à l'article 82 lorsque le droit d'un État membre le prévoit. »
- [3] « toute personne concernée a le droit de former un recours juridictionnel effectif lorsque l'autorité de contrôle qui est compétente en vertu des articles 55 et 56 ne traite pas une réclamation ou n'informe pas la personne concernée, dans un délai de trois mois, de l'état d'avancement ou de l'issue de la réclamation qu'elle a introduite au titre de l'article 77. »
- [4] « chaque personne concernée a droit à un recours juridictionnel effectif si elle considère que les droits que lui confère le présent règlement ont été violés du fait d'un traitement de ses données à caractère personnel effectué en violation du présent règlement. »

RÉPONSE :
Oui, votre ancien bénévole a le droit de se plaindre auprès de la CNIL, car « toute personne concernée a le droit d'introduire une réclamation auprès d'une autorité de contrôle » si elle estime que le traitement de ses données viole le règlement [1]. Il peut également choisir de mandater une association à but non lucratif active dans la protection des données pour qu'elle introduise la réclamation en son nom [2]. En plus de la réclamation administrative, il dispose du droit à un « recours juridictionnel effectif » s'il considère que ses droits ont été violés par le traitement de ses données [4]. Il peut aussi saisir la justice si l'autorité de contrôle ne traite pas sa réclamation ou ne l'informe pas de son issue « dans un délai de trois mois » [3].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit d'introduction d'une réclamation ; autorité de contrôle ; droit de recours juridictionnel ; juridiction compétente ; droit d'obtenir réparation ; préjudice

Temps : recherche 24.2 s · génération 1.8 s (2344 tokens lus, 574 écrits, 449.2 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.3 s · attente des limites de l'API 25 s (non comptée)

## q37 — Si une fuite de données cause un préjudice à un client, peut-il nous demander réparation ?

Article attendu : RGPD art. 82 — passage [1].

### Réponse du copilote

> Oui, si la fuite de données constitue une violation du RGPD et cause un dommage, le client peut demander réparation [1]. Une fuite de données est définie comme une « violation de la sécurité entraînant, de manière accidentelle ou illicite, la destruction, la perte, l'altération, la divulgation non autorisée de données à caractère personnel... ou l'accès non autorisé à de telles données » [3]. Le responsable du traitement est responsable du dommage causé par le traitement qui constitue une violation du règlement [1]. Toutefois, vous pouvez être exonéré de responsabilité si vous prouvez que « le fait qui a provoqué le dommage ne lui est nullement imputable » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Toute personne ayant subi un dommage matériel ou moral du fait d'une violation du présent règlement a le droit d'obtenir du responsable du traitement ou du sous-traitant réparation du préjudice subi. »
  [3] « «violation de données à caractère personnel», une violation de la sécurité entraînant, de manière accidentelle ou illicite, la destruction, la perte, l'altération, la divulgation non autorisée de données à caractère personnel transmises, conservées ou traitées d'une autre manière, ou l'accès non autorisé à de telles données; »
  [1] « Un responsable du traitement ou un sous-traitant est exonéré de responsabilité, au titre du paragraphe 2, s'il prouve que le fait qui a provoqué le dommage ne lui est nullement imputable. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 82 : Droit à réparation et responsabilité (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_82
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 12 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 34 : Communication à la personne concernée d'une violation de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_34
  [4] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [5] RGPD — règlement (UE) 2016/679, article 4, définition 1 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Toute personne ayant subi un dommage matériel ou moral du fait d'une violation du présent règlement a le droit d'obtenir du responsable du traitement ou du sous-traitant réparation du préjudice subi. »
- [3] « «violation de données à caractère personnel», une violation de la sécurité entraînant, de manière accidentelle ou illicite, la destruction, la perte, l'altération, la divulgation non autorisée de données à caractère personnel transmises, conservées ou traitées d'une autre manière, ou l'accès non autorisé à de telles données; »
- [1] « Un responsable du traitement ou un sous-traitant est exonéré de responsabilité, au titre du paragraphe 2, s'il prouve que le fait qui a provoqué le dommage ne lui est nullement imputable. »

RÉPONSE :
Oui, si la fuite de données constitue une violation du RGPD et cause un dommage, le client peut demander réparation [1]. Une fuite de données est définie comme une « violation de la sécurité entraînant, de manière accidentelle ou illicite, la destruction, la perte, l'altération, la divulgation non autorisée de données à caractère personnel... ou l'accès non autorisé à de telles données » [3]. Le responsable du traitement est responsable du dommage causé par le traitement qui constitue une violation du règlement [1]. Toutefois, vous pouvez être exonéré de responsabilité si vous prouvez que « le fait qui a provoqué le dommage ne lui est nullement imputable » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit à réparation ; préjudice ; responsabilité ; données à caractère personnel ; violation de la sécurité ; indemnisation

Temps : recherche 27.3 s · génération 1.5 s (2893 tokens lus, 338 écrits, 347.7 tokens/s) · contrôle de pertinence 0.1 s · reformulation 0.4 s · attente des limites de l'API 11 s (non comptée)

## q38 — Notre club de sport peut-il demander un extrait de casier judiciaire aux bénévoles qui encadrent des enfants ?

Article attendu : RGPD art. 10 — passage [1].

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 10 : Traitement des données à caractère personnel relatives aux condamnations pénales et aux infractions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_10
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [3] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [4] RGPD — règlement (UE) 2016/679, article 4, définition 11 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [5] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
Attention : Aucun des 3 extrait(s) recopié(s) par le modèle n'a été retrouvé mot pour mot dans les passages : sa réponse a été remplacée par un refus.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAISTS :
- [1] 「 Le traitement des données à caractère personnel relatives aux condamnations pénales et aux infractions … ne peut être effectué que sous le contrôle de l’autoriture publique, … »
- [1] 「 … ou si le traitement est autorisé par le droit de l’Union ou par le droit d’un État membre qui prévoit des garanties appropriées pour les droits et libertés des personnes concernées. »
- [1] 「 Tout registre complet des condamnations pénales ne peut être tenu que sous le contrôle de l’autorité publique. »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question.
Le RGPD, article 10, indique que le traitement des données relatives aux condamnations pénales « ne peut être effectué que sous le contrôle de l’autorité publique » [1].
Il est toutefois possible de traiter ces données « si le traitement est autorisé par le droit de l’Union ou par le droit d’un État membre qui prévoit des garanties appropriées pour les droits et libertés des personnes concernées » [1].
Les textes fournis ne précisent pas si le droit national français autorise spécifiquement un club de sport à demander un extrait de casier judiciaire à ses bénévoles, ni quelles sont les « garanties appropriées » requises dans ce contexte précis [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données relatives à des condamnations pénales ; données à caractère personnel ; responsable du traitement ; consentement ; protection des données

Temps : recherche 26.0 s · génération 1.6 s (3204 tokens lus, 289 écrits, 484.0 tokens/s) · reformulation 0.3 s

## q39 — Si nous remplaçons les noms de nos adhérents par des numéros, les données sont-elles encore des données personnelles ?

Article attendu : RGPD art. 4, définition 5 — passage [2].

### Réponse du copilote

> Oui, les données restent des données à caractère personnel, car une personne est réputée identifiable si elle peut l'être « directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification » [1]. Le remplacement des noms par des numéros constitue une pseudonymisation, qui est définie comme un traitement permettant que les données « ne puissent plus être attribuées à une personne concernée précise sans avoir recours à des informations supplémentaires » [2]. Pour que cette pseudonymisation soit effective, il faut que ces informations supplémentaires « soient conservées séparément et soumises à des mesures techniques et organisationnelles afin de garantir que les données à caractère personnel ne sont pas attribuées à une personne physique identifiée ou identifiable » [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale; »
  [2] « le traitement de données à caractère personnel de telle façon que celles-ci ne puissent plus être attribuées à une personne concernée précise sans avoir recours à des informations supplémentaires, pour autant que ces informations supplémentaires soient conservées séparément et soumises à des mesures techniques et organisationnelles afin de garantir que les données à caractère personnel ne sont pas attribuées à une personne physique identifiée ou identifiable; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 4, définition 1 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [2] RGPD — règlement (UE) 2016/679, article 4, définition 5 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 25 : Protection des données dès la conception et protection des données par défaut
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_25
  [4] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [5] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale; »
- [2] « le traitement de données à caractère personnel de telle façon que celles-ci ne puissent plus être attribuées à une personne concernée précise sans avoir recours à des informations supplémentaires, pour autant que ces informations supplémentaires soient conservées séparément et soumises à des mesures techniques et organisationnelles afin de garantir que les données à caractère personnel ne sont pas attribuées à une personne physique identifiée ou identifiable; »

RÉPONSE :
Oui, les données restent des données à caractère personnel, car une personne est réputée identifiable si elle peut l'être « directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification » [1]. Le remplacement des noms par des numéros constitue une pseudonymisation, qui est définie comme un traitement permettant que les données « ne puissent plus être attribuées à une personne concernée précise sans avoir recours à des informations supplémentaires » [2]. Pour que cette pseudonymisation soit effective, il faut que ces informations supplémentaires « soient conservées séparément et soumises à des mesures techniques et organisationnelles afin de garantir que les données à caractère personnel ne sont pas attribuées à une personne physique identifiée ou identifiable » [2].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données pseudonymisées ; pseudonymisation ; données à caractère personnel ; réidentification ; clé de chiffrement

Temps : recherche 28.1 s · génération 1.1 s (3248 tokens lus, 348 écrits, 480.7 tokens/s) · contrôle de pertinence 0.6 s · reformulation 0.5 s · attente des limites de l'API 8 s (non comptée)

## q40 — Nous allons utiliser un logiciel d'IA à haut risque qui attribue les tâches à nos salariés : devons-nous les prévenir avant de l'utiliser ?

Article attendu : AI Act art. 26 — passage [1].

### Réponse du copilote

> Oui, vous devez prévenir vos salariés avant d'utiliser ce logiciel. Votre logiciel, qui attribue des tâches aux salariés, est qualifié de système d'IA à haut risque car il est « destiné à être utilisés pour [...] attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques personnelles » [5]. En tant qu'employeur et déployeur, vous avez l'obligation d'informer « les représentants des travailleurs et les travailleurs concernés qu’ils seront soumis à l’utilisation du système d’IA à haut risque » avant de le mettre en service [1]. Cette information doit être fournie « conformément aux règles et procédures prévues par le droit de l’Union et le droit national et aux pratiques en matière d’information des travailleurs et de leurs représentants » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [5] « b) systèmes d'IA destinés à être utilisés pour prendre des décisions influant sur les conditions des relations professionnelles, la promotion ou le licenciement dans le cadre de relations professionnelles contractuelles, pour attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques personnelles ou pour suivre et évaluer les performances et le comportement de personnes dans le cadre de telles relations. »
  [1] « Avant de mettre en service ou d’utiliser un système d’IA à haut risque sur le lieu de travail, les déployeurs qui sont des employeurs informent les représentants des travailleurs et les travailleurs concernés qu’ils seront soumis à l’utilisation du système d’IA à haut risque. »
  [1] « Ces informations sont fournies, le cas échéant, conformément aux règles et procédures prévues par le droit de l’Union et le droit national et aux pratiques en matière d’information des travailleurs et de leurs représentants. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 7 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
  [5] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 1 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
  [3] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14
  [4] AI Act — règlement (UE) 2024/1689, article 13 : Transparence et fourniture d’informations aux déployeurs
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_13
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « destiné à être utilisés pour [...] attribuer des tâches sur la base du comportement individuel, de traits de … ».

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [5] « b) systèmes d'IA destinés à être utilisés pour prendre des décisions influant sur les conditions des relations professionnelles, la promotion ou le licenciement dans le cadre de relations professionnelles contractuelles, pour attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques personnelles ou pour suivre et évaluer les performances et le comportement de personnes dans le cadre de telles relations. »
- [1] « Avant de mettre en service ou d’utiliser un système d’IA à haut risque sur le lieu de travail, les déployeurs qui sont des employeurs informent les représentants des travailleurs et les travailleurs concernés qu’ils seront soumis à l’utilisation du système d’IA à haut risque. »
- [1] « Ces informations sont fournies, le cas échéant, conformément aux règles et procédures prévues par le droit de l’Union et le droit national et aux pratiques en matière d’information des travailleurs et de leurs représentants. »

RÉPONSE :
Oui, vous devez prévenir vos salariés avant d'utiliser ce logiciel. Votre logiciel, qui attribue des tâches aux salariés, est qualifié de système d'IA à haut risque car il est « destiné à être utilisés pour [...] attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques personnelles » [5]. En tant qu'employeur et déployeur, vous avez l'obligation d'informer « les représentants des travailleurs et les travailleurs concernés qu’ils seront soumis à l’utilisation du système d’IA à haut risque » avant de le mettre en service [1]. Cette information doit être fournie « conformément aux règles et procédures prévues par le droit de l’Union et le droit national et aux pratiques en matière d’information des travailleurs et de leurs représentants » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : système d'IA à haut risque ; information des personnes concernées ; transparence ; notification ; employeur ; travailleurs

Temps : recherche 27.6 s · génération 1.2 s (3265 tokens lus, 387 écrits, 475.5 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.7 s · attente des limites de l'API 12 s (non comptée)

## q41 — Notre organisme de formation peut-il utiliser une IA pour noter les examens de ses stagiaires ? Est-ce encadré ?

Article attendu : AI Act annexe III, point 3 — passage [1].

### Réponse du copilote

> Oui, votre organisme de formation peut utiliser une IA pour noter les examens, mais cette utilisation est strictement encadrée car elle relève des systèmes d'IA à haut risque [1]. En effet, les systèmes destinés à évaluer les acquis d'apprentissage dans les établissements de formation sont explicitement listés comme haut risque dans l'Annexe III de l'AI Act [1].
>
> En tant que déployeur, vous devez vous assurer que le système permet un « contrôle effectif par des personnes physiques » [2]. Cela implique que les personnes chargées du contrôle doivent avoir la possibilité de « décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou inverser la sortie du système d’IA à haut risque » [2]. De plus, le système doit techniquement permettre « l’enregistrement automatique des événements (journaux) » pour assurer la traçabilité [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « b) systèmes d'IA destinés à être utilisés pour évaluer les acquis d'apprentissage, y compris lorsque ceux-ci sont utilisés pour orienter le processus d'apprentissage de personnes physiques dans les établissements d'enseignement et de formation professionnelle, à tous les niveaux; »
  [1] « Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des domaines suivants: »
  [2] « 1. La conception et le développement des systèmes d’IA à haut risque permettent, notamment au moyen d’interfaces homme-machine appropriées, un contrôle effectif par des personnes physiques pendant leur période d’utilisation. »
  [2] « 4. Aux fins de la mise en œuvre des dispositions des paragraphes 1, 2 et 3, le système d’IA à haut risque est fourni au déployeur de telle manière que les personnes physiques chargées d’effectuer un contrôle humain, dans la mesure où cela est approprié et proportionné, ont la possibilité: »
  [2] « d) de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou inverser la sortie du système d’IA à haut risque; »
  [4] « 1. Les systèmes d’IA à haut risque permettent, techniquement, l’enregistrement automatique des événements (journaux) tout au long de la durée de vie du système. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, annexe III, point 3 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [2] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14
  [4] AI Act — règlement (UE) 2024/1689, article 12 : Enregistrement (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_12
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, annexe III, point 7 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [5] AI Act — règlement (UE) 2024/1689, article 6, point d : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « b) systèmes d'IA destinés à être utilisés pour évaluer les acquis d'apprentissage, y compris lorsque ceux-ci sont utilisés pour orienter le processus d'apprentissage de personnes physiques dans les établissements d'enseignement et de formation professionnelle, à tous les niveaux; »
- [1] « Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des domaines suivants: »
- [2] « 1. La conception et le développement des systèmes d’IA à haut risque permettent, notamment au moyen d’interfaces homme-machine appropriées, un contrôle effectif par des personnes physiques pendant leur période d’utilisation. »
- [2] « 4. Aux fins de la mise en œuvre des dispositions des paragraphes 1, 2 et 3, le système d’IA à haut risque est fourni au déployeur de telle manière que les personnes physiques chargées d’effectuer un contrôle humain, dans la mesure où cela est approprié et proportionné, ont la possibilité: »
- [2] « d) de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou inverser la sortie du système d’IA à haut risque; »
- [4] « 1. Les systèmes d’IA à haut risque permettent, techniquement, l’enregistrement automatique des événements (journaux) tout au long de la durée de vie du système. »

RÉPONSE :
Oui, votre organisme de formation peut utiliser une IA pour noter les examens, mais cette utilisation est strictement encadrée car elle relève des systèmes d'IA à haut risque [1]. En effet, les systèmes destinés à évaluer les acquis d'apprentissage dans les établissements de formation sont explicitement listés comme haut risque dans l'Annexe III de l'AI Act [1].

En tant que déployeur, vous devez vous assurer que le système permet un « contrôle effectif par des personnes physiques » [2]. Cela implique que les personnes chargées du contrôle doivent avoir la possibilité de « décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou inverser la sortie du système d’IA à haut risque » [2]. De plus, le système doit techniquement permettre « l’enregistrement automatique des événements (journaux) » pour assurer la traçabilité [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : système d'IA à haut risque ; évaluation à distance ; données à caractère personnel ; profilage ; transparence ; supervision humaine

Temps : recherche 27.1 s · génération 1.5 s (3221 tokens lus, 544 écrits, 478.0 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.2 s · attente des limites de l'API 23 s (non comptée)

## q42 — Un candidat refusé après l'analyse de sa candidature par un outil d'IA à haut risque nous demande pourquoi : devons-nous lui expliquer ?

Article attendu : AI Act art. 86 — passage [1].

### Réponse du copilote

> Oui, vous devez lui fournir des explications si vous êtes le déployeur du système d'IA.
> L'analyse de candidatures par un système d'IA entre dans la catégorie des systèmes à haut risque destinés au recrutement ou à la sélection de personnes physiques [2].
> En tant que personne concernée par une décision qui affecte significativement ses droits fondamentaux, le candidat a le droit d'obtenir du déployeur des explications claires et pertinentes sur le rôle du système d'IA dans la procédure décisionnelle et sur les principaux éléments de la décision prise [1].
> Cette obligation s'applique sauf si des exceptions ou des restrictions découlent du droit de l'Union ou du droit national dans le respect du droit de l'Union [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Toute personne concernée faisant l’objet d’une décision prise par un déployeur sur la base des sorties d’un système d’IA à haut risque mentionné à l’annexe III, à l’exception des systèmes énumérés au point 2 de ladite annexe, et qui produit des effets juridiques ou affecte significativement cette personne de façon similaire d’une manière qu’elle considère comme ayant des conséquences négatives sur sa santé, sa sécurité ou ses droits fondamentaux a le droit d’obtenir du déployeur des explications claires et pertinentes sur le rôle du système d’IA dans la procédure décisionnelle et sur les principaux éléments de la décision prise. »
  [2] « systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »
  [1] « Le paragraphe 1 ne s’applique pas à l’utilisation de systèmes d’IA pour lesquels des exceptions ou des restrictions à l’obligation prévue audit paragraphe découlent du droit de l’Union ou du droit national dans le respect du droit de l’Union. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 86 : Droit à l’explication des décisions individuelles (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_86
  [2] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, annexe III, point 8 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [4] AI Act — règlement (UE) 2024/1689, article 6, point d : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
  [5] AI Act — règlement (UE) 2024/1689, article 9, point c : Système de gestion des risques
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_9

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Toute personne concernée faisant l’objet d’une décision prise par un déployeur sur la base des sorties d’un système d’IA à haut risque mentionné à l’annexe III, à l’exception des systèmes énumérés au point 2 de ladite annexe, et qui produit des effets juridiques ou affecte significativement cette personne de façon similaire d’une manière qu’elle considère comme ayant des conséquences négatives sur sa santé, sa sécurité ou ses droits fondamentaux a le droit d’obtenir du déployeur des explications claires et pertinentes sur le rôle du système d’IA dans la procédure décisionnelle et sur les principaux éléments de la décision prise. »
- [2] « systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »
- [1] « Le paragraphe 1 ne s’applique pas à l’utilisation de systèmes d’IA pour lesquels des exceptions ou des restrictions à l’obligation prévue audit paragraphe découlent du droit de l’Union ou du droit national dans le respect du droit de l’Union. »

RÉPONSE :
Oui, vous devez lui fournir des explications si vous êtes le déployeur du système d'IA.
L'analyse de candidatures par un système d'IA entre dans la catégorie des systèmes à haut risque destinés au recrutement ou à la sélection de personnes physiques [2].
En tant que personne concernée par une décision qui affecte significativement ses droits fondamentaux, le candidat a le droit d'obtenir du déployeur des explications claires et pertinentes sur le rôle du système d'IA dans la procédure décisionnelle et sur les principaux éléments de la décision prise [1].
Cette obligation s'applique sauf si des exceptions ou des restrictions découlent du droit de l'Union ou du droit national dans le respect du droit de l'Union [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit à une explication ; décision automatisée ; profilage ; données à caractère personnel ; système d'intelligence artificielle à haut risque ; transparence

Temps : recherche 23.1 s · génération 1.4 s (2212 tokens lus, 435 écrits, 519.6 tokens/s) · contrôle de pertinence 0.3 s · reformulation 0.3 s

## q43 — Le règlement européen sur l'IA prévoit-il des mesures particulières pour les PME ?

Article attendu : AI Act art. 62 — passage [1].

### Réponse du copilote

> Oui, le règlement européen sur l'IA (AI Act) prévoit plusieurs mesures particulières pour les PME et les jeunes pousses. Les États membres doivent leur accorder « un accès prioritaire aux bacs à sable réglementaires de l’IA, dans la mesure où elles remplissent les conditions d’éligibilité et les critères de sélection » [1]. Ils doivent également « organiser des activités spécifiques de sensibilisation et de formation à l'application du présent règlement, adaptées aux besoins des PME, y compris les jeunes pousses, les déployeurs et, si nécessaire, les pouvoirs publics locaux » [1]. De plus, les États membres « utilisent des canaux privilégiés existants et, s’il y a lieu, en établissent de nouveaux avec les PME, y compris les jeunes pousses, les déployeurs, d’autres innovateurs et, si nécessaire, les pouvoirs publics locaux, afin de fournir des conseils et de répondre aux questions relatives à la mise en œuvre du présent règlement, y compris en ce qui concerne la participation à des bacs à sable réglementaires de l’IA » [1]. Ils doivent aussi « faciliter la participation des PME et d’autres parties concernées au processus d’élaboration de la normalisation » [1]. Concernant les coûts, « les intérêts et les besoins spécifiques des PME fournisseuses, y compris les jeunes pousses, sont pris en considération lors de la fixation des frais liés à l’évaluation de la conformité visée à l’article 43, ces frais étant réduits proportionnellement à leur taille, à la taille de leur marché et à d’autres indicateurs pertinents » [1]. Enfin, en matière de gestion de la qualité, « les PME, y compris les jeunes pousses, peuvent se conformer de manière simplifiée à certains éléments du système de gestion de la qualité requis par l'article 17, pour autant qu'elles n'aient pas d'entreprises partenaires ou d'entreprises liées au sens de la recommandation 2003/361/CE » [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les États membres: a) accordent aux PME, y compris les jeunes pousses, qui ont leur siège social ou une succursale dans l’Union, un accès prioritaire aux bacs à sable réglementaires de l’IA, dans la mesure où elles remplissent les conditions d’éligibilité et les critères de sélection; »
  [1] « b) organisent des activités spécifiques de sensibilisation et de formation à l'application du présent règlement, adaptées aux besoins des PME, y compris les jeunes pousses, les déployeurs et, si nécessaire, les pouvoirs publics locaux; »
  [1] « c) utilisent des canaux privilégiés existants et, s’il y a lieu, en établissent de nouveaux avec les PME, y compris les jeunes pousses, les déployeurs, d’autres innovateurs et, si nécessaire, les pouvoirs publics locaux, afin de fournir des conseils et de répondre aux questions relatives à la mise en œuvre du présent règlement, y compris en ce qui concerne la participation à des bacs à sable réglementaires de l’IA; »
  [1] « d) facilitent la participation des PME et d’autres parties concernées au processus d’élaboration de la normalisation. »
  [1] « Les intérêts et les besoins spécifiques des PME fournisseuses, y compris les jeunes pousses, sont pris en considération lors de la fixation des frais liés à l’évaluation de la conformité visée à l’article 43, ces frais étant réduits proportionnellement à leur taille, à la taille de leur marché et à d’autres indicateurs pertinents. »
  [4] « Les PME, y compris les jeunes pousses, peuvent se conformer de manière simplifiée à certains éléments du système de gestion de la qualité requis par l'article 17, pour autant qu'elles n'aient pas d'entreprises partenaires ou d'entreprises liées au sens de la recommandation 2003/361/CE. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 62 : Mesures en faveur des fournisseurs et déployeurs, en particulier les PME, y compris les jeunes pousses (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_62
  [4] AI Act — règlement (UE) 2024/1689, article 63 : Dérogations pour des opérateurs spécifiques (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_63
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 1 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [3] AI Act — règlement (UE) 2024/1689, article 4 : Maîtrise de l'IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_4
  [5] AI Act — règlement (UE) 2024/1689, article 70, paragraphe 8 : Désignation des autorités nationales compétentes et des points de contact uniques
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_70
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « organiser des activités spécifiques de sensibilisation et de formation à l'application du présent règlement, adaptées … » (et 1 autre(s)).

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les États membres: a) accordent aux PME, y compris les jeunes pousses, qui ont leur siège social ou une succursale dans l’Union, un accès prioritaire aux bacs à sable réglementaires de l’IA, dans la mesure où elles remplissent les conditions d’éligibilité et les critères de sélection; »
- [1] « b) organisent des activités spécifiques de sensibilisation et de formation à l'application du présent règlement, adaptées aux besoins des PME, y compris les jeunes pousses, les déployeurs et, si nécessaire, les pouvoirs publics locaux; »
- [1] « c) utilisent des canaux privilégiés existants et, s’il y a lieu, en établissent de nouveaux avec les PME, y compris les jeunes pousses, les déployeurs, d’autres innovateurs et, si nécessaire, les pouvoirs publics locaux, afin de fournir des conseils et de répondre aux questions relatives à la mise en œuvre du présent règlement, y compris en ce qui concerne la participation à des bacs à sable réglementaires de l’IA; »
- [1] « d) facilitent la participation des PME et d’autres parties concernées au processus d’élaboration de la normalisation. »
- [1] « Les intérêts et les besoins spécifiques des PME fournisseuses, y compris les jeunes pousses, sont pris en considération lors de la fixation des frais liés à l’évaluation de la conformité visée à l’article 43, ces frais étant réduits proportionnellement à leur taille, à la taille de leur marché et à d’autres indicateurs pertinents. »
- [4] « Les PME, y compris les jeunes pousses, peuvent se conformer de manière simplifiée à certains éléments du système de gestion de la qualité requis par l'article 17, pour autant qu'elles n'aient pas d'entreprises partenaires ou d'entreprises liées au sens de la recommandation 2003/361/CE. »

RÉPONSE :
Oui, le règlement européen sur l'IA (AI Act) prévoit plusieurs mesures particulières pour les PME et les jeunes pousses. Les États membres doivent leur accorder « un accès prioritaire aux bacs à sable réglementaires de l’IA, dans la mesure où elles remplissent les conditions d’éligibilité et les critères de sélection » [1]. Ils doivent également « organiser des activités spécifiques de sensibilisation et de formation à l'application du présent règlement, adaptées aux besoins des PME, y compris les jeunes pousses, les déployeurs et, si nécessaire, les pouvoirs publics locaux » [1]. De plus, les États membres « utilisent des canaux privilégiés existants et, s’il y a lieu, en établissent de nouveaux avec les PME, y compris les jeunes pousses, les déployeurs, d’autres innovateurs et, si nécessaire, les pouvoirs publics locaux, afin de fournir des conseils et de répondre aux questions relatives à la mise en œuvre du présent règlement, y compris en ce qui concerne la participation à des bacs à sable réglementaires de l’IA » [1]. Ils doivent aussi « faciliter la participation des PME et d’autres parties concernées au processus d’élaboration de la normalisation » [1]. Concernant les coûts, « les intérêts et les besoins spécifiques des PME fournisseuses, y compris les jeunes pousses, sont pris en considération lors de la fixation des frais liés à l’évaluation de la conformité visée à l’article 43, ces frais étant réduits proportionnellement à leur taille, à la taille de leur marché et à d’autres indicateurs pertinents » [1]. Enfin, en matière de gestion de la qualité, « les PME, y compris les jeunes pousses, peuvent se conformer de manière simplifiée à certains éléments du système de gestion de la qualité requis par l'article 17, pour autant qu'elles n'aient pas d'entreprises partenaires ou d'entreprises liées au sens de la recommandation 2003/361/CE » [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : petites et moyennes entreprises ; micro-entreprises ; mesures d'accompagnement ; soutien à l'innovation ; allègements réglementaires ; obligations proportionnées

Temps : recherche 27.9 s · génération 2.3 s (2699 tokens lus, 860 écrits, 476.6 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.3 s · attente des limites de l'API 33 s (non comptée)

## q44 — À partir de quelle date devrons-nous respecter les obligations sur les systèmes d'IA à haut risque utilisés pour le recrutement ?

Article attendu : AI Act art. 113 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 2, paragraphe 13 : Champ d’application
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_2
  [2] AI Act — règlement (UE) 2024/1689, article 2, paragraphe 1 : Champ d’application
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_2
  [3] AI Act — règlement (UE) 2024/1689, article 16 : Obligations incombant aux fournisseurs de systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_16
  [4] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [5] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 11 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Au plus tard le 2 août 2027, la Commission adopte des actes délégués conformément à l'article 97 afin de compléter le présent règlement afin de préciser les systèmes d'IA à haut risque concernés, les exigences ou obligations qui peuvent être limitées, les conditions dans lesquelles cette limitation s'applique et la portée de la limitation. »
- [4] « Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des domaines suivants: »
- [4] « 4. Emploi, gestion de la main-d'œuvre et accès à l'emploi indépendant: »
- [4] « a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question. Ils identifient les systèmes d'IA utilisés pour le recrutement comme des systèmes d'IA à haut risque [4], mais ne précisent pas la date d'entrée en vigueur des obligations associées. Le seul délai mentionné concerne l'adoption d'actes délégués par la Commission « au plus tard le 2 août 2027 » pour préciser certaines limitations [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : systèmes d'IA à haut risque ; recrutement ; obligations ; conformité

Temps : recherche 24.5 s · génération 2.4 s (2610 tokens lus, 317 écrits, 510.3 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.3 s · attente des limites de l'API 239 s (non comptée)

## h06 — Quelles mentions obligatoires doivent figurer sur une facture ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, annexe VII, point 3 a : Conformité fondée sur une évaluation du système de gestion de la qualité et une évaluation de la documentation technique
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_VII
  [2] AI Act — règlement (UE) 2024/1689, annexe VII, point 4 a : Conformité fondée sur une évaluation du système de gestion de la qualité et une évaluation de la documentation technique
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_VII
  [3] AI Act — règlement (UE) 2024/1689, annexe V : Déclaration UE de conformité
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_V
  [4] AI Act — règlement (UE) 2024/1689, annexe IV, point 6 : Documentation technique visée à l'article 11, paragraphe 1
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_IV
  [5] RGPD — règlement (UE) 2016/679, article 4, définition 1 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : facture ; numéro de facture ; date de la facture ; identité du fournisseur ; identité du client ; description des biens ou des services

Temps : recherche 48.3 s · génération 0.8 s (2067 tokens lus, 25 écrits, 453.7 tokens/s) · reformulation 0.9 s

## h07 — Comment demander une subvention à la mairie pour notre association ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 7 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [4] RGPD — règlement (UE) 2016/679, article 12, paragraphe 5 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [5] RGPD — règlement (UE) 2016/679, article 49, paragraphe 4 : Dérogations pour des situations particulières
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_49

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : subvention publique ; association d'intérêt général ; demande de subvention ; convention de subvention ; contrôle de l'emploi des fonds ; transparence financière

Temps : recherche 38.8 s · génération 0.6 s (2021 tokens lus, 25 écrits, 453.7 tokens/s) · reformulation 1.5 s
