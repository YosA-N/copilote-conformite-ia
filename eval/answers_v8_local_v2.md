# Réponses du copilote — v8_local_v2

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 27/11/2026 à 19:58 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen3:4b-instruct` via Ollama 0.40.18 — température 0.1, contexte 8192 tokens, couches sur la carte graphique : toutes, 2000 tokens au plus par réponse, dont 800 gardés pour la réponse (recopie des extraits arrêtée après 1200 tokens si la réponse n'a pas commencé)
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_v2.jsonl` (17 + 3 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q28 | Un adhérent nous signale que son adresse et sa date de naissance sont fausses dans notre fichier : devons-nous les corriger, et dans quel délai ? | 1/1 | non | — | 33 s |
| q29 | Une cliente conteste l'exactitude des informations que nous avons sur elle : pouvons-nous continuer à les utiliser pendant que nous vérifions ? | 1/2 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 37 s |
| q30 | Pouvons-nous refuser automatiquement une demande d'inscription à notre service à partir d'un score calculé par un logiciel, sans qu'une personne ne vérifie ? | 4/4 | non | — | 49 s |
| q31 | Nous faisons développer une application mobile pour nos membres : quelles précautions de protection des données devons-nous prévoir dès sa conception ? | 3/3 | non | — | 53 s |
| q32 | Nous organisons un festival avec une autre association et nous gérons ensemble le fichier des participants : qui est responsable de ces données ? | 3/3 | non | — | 35 s |
| q33 | Nous avons acheté un fichier de prospects à une autre entreprise : devons-nous informer ces personnes, et dans quel délai ? | 3/3 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 47 s |
| q34 | Puis-je installer des caméras dans l'atelier pour surveiller le travail de mes salariés ? | 2/2 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 39 s |
| q35 | Notre fédération sportive peut-elle rédiger un guide de bonnes pratiques RGPD que ses clubs pourraient suivre officiellement ? | 3/3 | non | La réponse met entre « » un texte introuvable dans les extraits vérifiés : « association représentant des catégories de responsables du traitement ». | 46 s |
| q36 | Un ancien bénévole menace de se plaindre de nous auprès de la CNIL : en a-t-il le droit, et quels autres recours a-t-il ? | 3/3 | non | — | 41 s |
| q37 | Si une fuite de données cause un préjudice à un client, peut-il nous demander réparation ? | 5/5 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 45 s |
| q38 | Notre club de sport peut-il demander un extrait de casier judiciaire aux bénévoles qui encadrent des enfants ? | 4/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 38 s |
| q39 | Si nous remplaçons les noms de nos adhérents par des numéros, les données sont-elles encore des données personnelles ? | 1/1 | non | — | 28 s |
| q40 | Nous allons utiliser un logiciel d'IA à haut risque qui attribue les tâches à nos salariés : devons-nous les prévenir avant de l'utiliser ? | 1/1 | non | La réponse cite [3] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations. | 27 s |
| q41 | Notre organisme de formation peut-il utiliser une IA pour noter les examens de ses stagiaires ? Est-ce encadré ? | 4/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 46 s |
| q42 | Un candidat refusé après l'analyse de sa candidature par un outil d'IA à haut risque nous demande pourquoi : devons-nous lui expliquer ? | 3/3 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 29 s |
| q43 | Le règlement européen sur l'IA prévoit-il des mesures particulières pour les PME ? | 8/8 | non | — | 64 s |
| q44 | À partir de quelle date devrons-nous respecter les obligations sur les systèmes d'IA à haut risque utilisés pour le recrutement ? | 2/2 | non | — | 33 s |
| h06 | Quelles mentions obligatoires doivent figurer sur une facture ? | 0/0 | oui | — | 15 s |
| h07 | Comment demander une subvention à la mairie pour notre association ? | 0/0 | oui | — | 28 s |
| h08 | Quelles sont les règles pour embaucher un apprenti dans une PME ? | 0/0 | oui | — | 30 s |

## q28 — Un adhérent nous signale que son adresse et sa date de naissance sont fausses dans notre fichier : devons-nous les corriger, et dans quel délai ?

Article attendu : RGPD art. 16 — passage [1].

### Réponse du copilote

> Oui : vous devez corriger les données à caractère personnel fausses, telles que l'adresse et la date de naissance, car elles sont inexactes. Cette rectification doit être effectuée dans les meilleurs délais [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit d'obtenir du responsable du traitement, dans les meilleurs délais, la rectification des données à caractère personnel la concernant qui sont inexactes. Compte tenu des finalités du traitement, la personne concernée a le droit d'obtenir que les données à caractère personnel incomplètes soient complétées, y compris en fournissant une déclaration complémentaire. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 16 : Droit de rectification (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_16
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 19 : Obligation de notification en ce qui concerne la rectification ou l'effacement de données à caractère personnel ou la limitation du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_19
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
- [1] « La personne concernée a le droit d'obtenir du responsable du traitement, dans les meilleurs délais, la rectification des données à caractère personnel la concernant qui sont inexactes. Compte tenu des finalités du traitement, la personne concernée a le droit d'obtenir que les données à caractère personnel incomplètes soient complétées, y compris en fournissant une déclaration complémentaire. »  

RÉPONSE :  
Oui : vous devez corriger les données à caractère personnel fausses, telles que l'adresse et la date de naissance, car elles sont inexactes. Cette rectification doit être effectuée dans les meilleurs délais [1].
```

</details>

Temps : recherche 2.5 s · génération 26.6 s (3523 tokens lus, 161 écrits, 33.7 tokens/s) · contrôle de pertinence 4.4 s

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
- [3] « La personne concernée a le droit d'obtenir du responsable du traitement, dans les meilleurs délais, la rectification des données à caractère personnel la concernant qui sont inexactes. Compte tenu des finalités du traitement, la personne concernée a le droit d'obtenir que les données à caractère personnel incomplètes soient complétées, y compris en fournissant une déclaration complémentaire. »  
- [4] « Lorsque le traitement est fondé sur l'article 6, paragraphe 1, point e) ou f), y compris un profilage fondé sur ces dispositions, la personne concernée a le droit de s'opposer à tout moment, pour des raisons tenant à sa situation particulière, à un traitement des données à caractère personnel la concernant. Le responsable du traitement ne traite plus les données à caractère personnel, à moins qu'il ne démontre qu'il existe des motifs légitimes et impérieux pour le traitement qui prévalent sur les intérêts et les droits et libertés de la personne concernée, ou pour la constatation, l'exercice ou la défense de droits en justice. »  

RÉPONSE :  
Non : si une cliente conteste l'exactitude des informations sur elle, vous devez arrêter le traitement des données à caractère personnel concernant cette personne, sauf si vous démontriez des motifs légitimes et impérieux pour le traitement qui prévalent sur ses droits et libertés, ou pour la constatation, l'exercice ou la défense de droits en justice [4]. Cette obligation s'applique même pendant la vérification, car le droit de rectification implique que les données inexactes doivent être corrigées rapidement [3]. Vous ne pouvez pas continuer à utiliser les données pendant que vous les vérifiez sans justifier un motif légitime et impérieux [4].
```

</details>

Temps : recherche 2.2 s · génération 31.4 s (3213 tokens lus, 427 écrits, 33.9 tokens/s) · contrôle de pertinence 3.5 s

## q30 — Pouvons-nous refuser automatiquement une demande d'inscription à notre service à partir d'un score calculé par un logiciel, sans qu'une personne ne vérifie ?

Article attendu : RGPD art. 22 — passage [1].

### Réponse du copilote

> Non, vous ne pouvez pas refuser automatiquement une demande d'inscription à votre service à partir d'un score calculé par un logiciel sans que la personne concernée ne vérifie, car cela constituerait une décision fondée exclusivement sur un traitement automatisé produisant des effets juridiques significatifs (RGPD, article 22, paragraphe 1) [1]. Ce droit s'applique sauf si la décision est nécessaire à la conclusion ou à l'exécution d'un contrat entre la personne concernée et un responsable du traitement (RGPD, article 22, paragraphe 2, point a) [1]. Dans les autres cas, notamment si le score est utilisé pour une décision ayant des effets juridiques, le responsable du traitement doit mettre en œuvre des mesures appropriées, notamment le droit de la personne concernée d'obtenir une intervention humaine, d'exprimer son point de vue et de contester la décision (RGPD, article 22, paragraphe 3) [1]. Aucune mention dans les extraits ne permet de justifier un refus automatique sans vérification humaine, ni de considérer que le score suffit à remplacer une évaluation humaine.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé, y compris le profilage, produisant des effets juridiques la concernant ou l'affectant de manière significative de façon similaire. »
  [1] « Le paragraphe 1 ne s'applique pas lorsque la décision: a) est nécessaire à la conclusion ou à l'exécution d'un contrat entre la personne concernée et un responsable du traitement; »
  [1] « Dans les cas visés au paragraphe 2, points a) et c), le responsable du traitement met en œuvre des mesures appropriées pour la sauvegarde des droits et libertés et des intérêts légitimes de la personne concernée, au moins du droit de la personne concernée d'obtenir une intervention humaine de la part du responsable du traitement, d'exprimer son point de vue et de contester la décision. »
  [1] « Les décisions visées au paragraphe 2 ne peuvent être fondées sur les catégories particulières de données à caractère personnel visées à l'article 9, paragraphe 1, à moins que l'article 9, paragraphe 2, point a) ou g), ne s'applique et que des mesures appropriées pour la sauvegarde des droits et libertés et des intérêts légitimes de la personne concernée ne soient en place. »

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
  [5] AI Act — règlement (UE) 2024/1689, article 12 : Enregistrement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_12

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « La personne concernée a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé, y compris le profilage, produisant des effets juridiques la concernant ou l'affectant de manière significative de façon similaire. »  
- [1] « Le paragraphe 1 ne s'applique pas lorsque la décision: a) est nécessaire à la conclusion ou à l'exécution d'un contrat entre la personne concernée et un responsable du traitement; »  
- [1] « Dans les cas visés au paragraphe 2, points a) et c), le responsable du traitement met en œuvre des mesures appropriées pour la sauvegarde des droits et libertés et des intérêts légitimes de la personne concernée, au moins du droit de la personne concernée d'obtenir une intervention humaine de la part du responsable du traitement, d'exprimer son point de vue et de contester la décision. »  
- [1] « Les décisions visées au paragraphe 2 ne peuvent être fondées sur les catégories particulières de données à caractère personnel visées à l'article 9, paragraphe 1, à moins que l'article 9, paragraphe 2, point a) ou g), ne s'applique et que des mesures appropriées pour la sauvegarde des droits et libertés et des intérêts légitimes de la personne concernée ne soient en place. »  

RÉPONSE :  
Non, vous ne pouvez pas refuser automatiquement une demande d'inscription à votre service à partir d'un score calculé par un logiciel sans que la personne concernée ne vérifie, car cela constituerait une décision fondée exclusivement sur un traitement automatisé produisant des effets juridiques significatifs (RGPD, article 22, paragraphe 1) [1]. Ce droit s'applique sauf si la décision est nécessaire à la conclusion ou à l'exécution d'un contrat entre la personne concernée et un responsable du traitement (RGPD, article 22, paragraphe 2, point a) [1]. Dans les autres cas, notamment si le score est utilisé pour une décision ayant des effets juridiques, le responsable du traitement doit mettre en œuvre des mesures appropriées, notamment le droit de la personne concernée d'obtenir une intervention humaine, d'exprimer son point de vue et de contester la décision (RGPD, article 22, paragraphe 3) [1]. Aucune mention dans les extraits ne permet de justifier un refus automatique sans vérification humaine, ni de considérer que le score suffit à remplacer une évaluation humaine.
```

</details>

Temps : recherche 2.2 s · génération 41.9 s (3603 tokens lus, 628 écrits, 32.6 tokens/s) · contrôle de pertinence 4.9 s

## q31 — Nous faisons développer une application mobile pour nos membres : quelles précautions de protection des données devons-nous prévoir dès sa conception ?

Article attendu : RGPD art. 25 — passage [1].

### Réponse du copilote

> Vous devez prévoir, dès la conception de l'application mobile, des mesures techniques et organisationnelles appropriées pour garantir que seules les données à caractère personnel nécessaires à chaque finalité spécifique du traitement sont collectées, traitées, conservées et accessibles [1]. Ces mesures doivent s'appliquer à la quantité, à l'étendue, à la durée de conservation et à l'accessibilité des données [1]. Vous devez également mettre en œuvre des mesures telles que la pseudonymisation et le chiffrement des données à caractère personnel, afin de garantir un niveau de sécurité adapté au risque [3]. Ces mesures doivent inclure des moyens pour assurer la confidentialité, l'intégrité, la disponibilité et la résilience des systèmes et services de traitement [3]. En outre, une procédure régulière de test, d'analyse et d'évaluation de l'efficacité des mesures doit être mise en place [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le responsable du traitement met en œuvre les mesures techniques et organisationnelles appropriées pour garantir que, par défaut, seules les données à caractère personnel qui sont nécessaires au regard de chaque finalité spécifique du traitement sont traitées. Cela s'applique à la quantité de données à caractère personnel collectées, à l'étendue de leur traitement, à leur durée de conservation et à leur accessibilité. En particulier, ces mesures garantissent que, par défaut, les données à caractère personnel ne sont pas rendues accessibles à un nombre indéterminé de personnes physiques sans l'intervention de la personne physique concernée. »
  [1] « Compte tenu de l'état des connaissances, des coûts de mise en œuvre et de la nature, de la portée, du contexte et des finalités du traitement ainsi que des risques, dont le degré de probabilité et de gravité varie, que présente le traitement pour les droits et libertés des personnes physiques, le responsable du traitement met en œuvre, tant au moment de la détermination des moyens du traitement qu'au moment du traitement lui-même, des mesures techniques et organisationnelles appropriées, telles que la pseudonymisation, qui sont destinées à mettre en œuvre les principes relatifs à la protection des données, par exemple la minimisation des données, de façon effective et à assortir le traitement des garanties nécessaires afin de répondre aux exigences du présent règlement et de protéger les droits de la personne concernée. »
  [3] « Compte tenu de l'état des connaissances, des coûts de mise en œuvre et de la nature, de la portée, du contexte et des finalités du traitement ainsi que des risques, dont le degré de probabilité et de gravité varie, pour les droits et libertés des personnes physiques, le responsable du traitement et le sous-traitant mettent en œuvre les mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque, y compris entre autres, selon les besoins: a) la pseudonymisation et le chiffrement des données à caractère personnel; b) des moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement; c) des moyens permettant de rétablir la disponibilité des données à caractère personnel et l'accès à celles-ci dans des délais appropriés en cas d'incident physique ou technique; d) une procédure visant à tester, à analyser et à évaluer régulièrement l'efficacité des mesures techniques et organisationnelles pour assurer la sécurité du traitement. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 25 : Protection des données dès la conception et protection des données par défaut (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_25
  [3] RGPD — règlement (UE) 2016/679, article 32 : Sécurité du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_32
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [4] RGPD — règlement (UE) 2016/679, article 35, paragraphe 1 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [5] RGPD — règlement (UE) 2016/679, article 50 : Coopération internationale dans le domaine de la protection des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_50

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le responsable du traitement met en œuvre les mesures techniques et organisationnelles appropriées pour garantir que, par défaut, seules les données à caractère personnel qui sont nécessaires au regard de chaque finalité spécifique du traitement sont traitées. Cela s'applique à la quantité de données à caractère personnel collectées, à l'étendue de leur traitement, à leur durée de conservation et à leur accessibilité. En particulier, ces mesures garantissent que, par défaut, les données à caractère personnel ne sont pas rendues accessibles à un nombre indéterminé de personnes physiques sans l'intervention de la personne physique concernée. »
- [1] « Compte tenu de l'état des connaissances, des coûts de mise en œuvre et de la nature, de la portée, du contexte et des finalités du traitement ainsi que des risques, dont le degré de probabilité et de gravité varie, que présente le traitement pour les droits et libertés des personnes physiques, le responsable du traitement met en œuvre, tant au moment de la détermination des moyens du traitement qu'au moment du traitement lui-même, des mesures techniques et organisationnelles appropriées, telles que la pseudonymisation, qui sont destinées à mettre en œuvre les principes relatifs à la protection des données, par exemple la minimisation des données, de façon effective et à assortir le traitement des garanties nécessaires afin de répondre aux exigences du présent règlement et de protéger les droits de la personne concernée. »
- [3] « Compte tenu de l'état des connaissances, des coûts de mise en œuvre et de la nature, de la portée, du contexte et des finalités du traitement ainsi que des risques, dont le degré de probabilité et de gravité varie, pour les droits et libertés des personnes physiques, le responsable du traitement et le sous-traitant mettent en œuvre les mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque, y compris entre autres, selon les besoins: a) la pseudonymisation et le chiffrement des données à caractère personnel; b) des moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement; c) des moyens permettant de rétablir la disponibilité des données à caractère personnel et l'accès à celles-ci dans des délais appropriés en cas d'incident physique ou technique; d) une procédure visant à tester, à analyser et à évaluer régulièrement l'efficacité des mesures techniques et organisationnelles pour assurer la sécurité du traitement. »

RÉPONSE :
Vous devez prévoir, dès la conception de l'application mobile, des mesures techniques et organisationnelles appropriées pour garantir que seules les données à caractère personnel nécessaires à chaque finalité spécifique du traitement sont collectées, traitées, conservées et accessibles [1]. Ces mesures doivent s'appliquer à la quantité, à l'étendue, à la durée de conservation et à l'accessibilité des données [1]. Vous devez également mettre en œuvre des mesures telles que la pseudonymisation et le chiffrement des données à caractère personnel, afin de garantir un niveau de sécurité adapté au risque [3]. Ces mesures doivent inclure des moyens pour assurer la confidentialité, l'intégrité, la disponibilité et la résilience des systèmes et services de traitement [3]. En outre, une procédure régulière de test, d'analyse et d'évaluation de l'efficacité des mesures doit être mise en place [3].
```

</details>

Temps : recherche 2.2 s · génération 43.4 s (3141 tokens lus, 843 écrits, 33.5 tokens/s) · contrôle de pertinence 7.6 s

## q32 — Nous organisons un festival avec une autre association et nous gérons ensemble le fichier des participants : qui est responsable de ces données ?

Article attendu : RGPD art. 26 — passage [1].

### Réponse du copilote

> Lorsque vous et l'autre association déterminez conjointement les finalités et les moyens du traitement du fichier des participants, vous êtes les responsables conjoints du traitement [1]. Chacun de vous est donc responsable du traitement, et vos obligations respectives doivent être définies de manière transparente par un accord entre vous [1]. Ce cadre s'applique à l'ensemble du traitement des données des participants, y compris l'exercice des droits de la personne concernée [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Lorsque deux responsables du traitement ou plus déterminent conjointement les finalités et les moyens du traitement, ils sont les responsables conjoints du traitement. »
  [1] « Les responsables conjoints du traitement définissent de manière transparente leurs obligations respectives aux fins d'assurer le respect des exigences du présent règlement, notamment en ce qui concerne l'exercice des droits de la personne concernée, et leurs obligations respectives quant à la communication des informations visées aux articles 13 et 14, par voie d'accord entre eux, sauf si, et dans la mesure, où leurs obligations respectives sont définies par le droit de l'Union ou par le droit de l'État membre auquel les responsables du traitement sont soumis. »
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
- [2] « «responsable du traitement», la personne physique ou morale, l'autorité publique, le service ou un autre organisme qui, seul ou conjointement avec d'autres, détermine les finalités et les moyens du traitement; »  

RÉPONSE :  
Lorsque vous et l'autre association déterminez conjointement les finalités et les moyens du traitement du fichier des participants, vous êtes les responsables conjoints du traitement [1]. Chacun de vous est donc responsable du traitement, et vos obligations respectives doivent être définies de manière transparente par un accord entre vous [1]. Ce cadre s'applique à l'ensemble du traitement des données des participants, y compris l'exercice des droits de la personne concernée [1].
```

</details>

Temps : recherche 2.2 s · génération 27.5 s (3009 tokens lus, 355 écrits, 34.5 tokens/s) · contrôle de pertinence 4.9 s

## q33 — Nous avons acheté un fichier de prospects à une autre entreprise : devons-nous informer ces personnes, et dans quel délai ?

Article attendu : RGPD art. 14 — passage [2].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [2] RGPD — règlement (UE) 2016/679, article 14, paragraphe 3 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [3] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [4] AI Act — règlement (UE) 2024/1689, article 31, paragraphe 7 : Exigences concernant les organismes notifiés
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_31
  [5] AI Act — règlement (UE) 2024/1689, article 31, paragraphe 1 : Exigences concernant les organismes notifiés
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_31
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. Lorsque la personne concernée présente sa demande sous une forme électronique, les informations sont fournies par voie électronique lorsque cela est possible, à moins que la personne concernée ne demande qu'il en soit autrement. »  
- [2] « Le responsable du traitement fournit les informations visées aux paragraphes 1 et 2: a) dans un délai raisonnable après avoir obtenu les données à caractère personnel, mais ne dépassant pas un mois, eu égard aux circonstances particulières dans lesquelles les données à caractère personnel sont traitées; b) si les données à caractère personnel doivent être utilisées aux fins de la communication avec la personne concernée, au plus tard au moment de la première communication à ladite personne; ou c) s'il est envisagé de communiquer les informations à un autre destinataire, au plus tard lorsque les données à caractère personnel sont communiquées pour la première fois. »  
- [3] « Lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée, le responsable du traitement fournit à celle-ci toutes les informations suivantes: a) l'identité et les coordonnées du responsable du traitement et, le cas échéant, du représentant du responsable du traitement; b) le cas échéant, les coordonnées du délégué à la protection des données; c) les finalités du traitement auquel sont destinées les données à caractère personnel ainsi que la base juridique du traitement; d) les catégories de données à caractère personnel concernées; e) le cas échéant, les destinataires ou les catégories de destinataires des données à caractère personnel; f) le cas échéant, le fait que le responsable du traitement a l'intention d'effectuer un transfert de données à caractère personnel à un destinataire dans un pays tiers ou une organisation internationale, et l'existence ou l'absence d'une décision d'adéquation rendue par la Commission ou, dans le cas des transferts visés à l'article 46 ou 47, ou à l'article 49, paragraphe 1, deuxième alinéa, la référence aux garanties appropriées ou adaptées et les moyens d'en obtenir une copie ou l'endroit où elles ont été mises à disposition; »  

RÉPONSE :  
Oui, vous devez informer les personnes concernées, car les données à caractère personnel ont été collectées auprès d'elles, même si elles ont été achetées à une autre entreprise. Selon le RGPD, article 14, point 2, a), les informations doivent être fournies dans un délai raisonnable, mais ne dépassant pas un mois, en fonction des circonstances particulières du traitement [2]. Si les données sont utilisées pour une communication avec la personne concernée, les informations doivent être fournies au plus tard au moment de la première communication [2]. Si les données ne sont pas collectées directement auprès de la personne concernée, comme dans le cas d’un fichier acheté, le responsable du traitement doit fournir les informations prévues à l’article 14, notamment sur les finalités du traitement, les catégories de données, les destinataires, et les garanties en cas de transfert à un pays tiers [3]. Ces obligations s’appliquent à l’achat d’un fichier de prospects, car les données à caractère personnel sont traitées dans le cadre d’un traitement de données personnelles [3]. Le délai maximal est de un mois à compter de la réception de la demande, sauf si la demande est formulée par une personne concernée [1].
```

</details>

Temps : recherche 2.2 s · génération 37.7 s (2332 tokens lus, 938 écrits, 35.3 tokens/s) · contrôle de pertinence 7.0 s

## q34 — Puis-je installer des caméras dans l'atelier pour surveiller le travail de mes salariés ?

Article attendu : RGPD art. 88 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

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
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [3] « la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA qui créent ou développent des bases de données de reconnaissance faciale par le moissonnage non ciblé d’images faciales provenant de l’internet ou de la vidéosurveillance; »  
- [4] « à pénétrer dans tous les locaux commerciaux, sur tous les terrains ou dans tous les biens immobiliers de l'opérateur concerné situés dans l'Union; »  

RÉPONSE :  
Non, vous ne pouvez pas installer des caméras dans l'atelier pour surveiller le travail de vos salariés, car cela pourrait constituer une utilisation d’un système d’IA qui génère ou manipule des images ou des contenus audio réalistes, notamment s’il s’agit de vidéos ou d’images de salariés, sans leur consentement libre, spécifique, éclairé, univoque et explicite [3]. De plus, l’installation de caméras dans les locaux commerciaux ou les biens immobiliers de l’opérateur est autorisée par le Bureau de l’IA pour des inspections, mais ne peut pas être justifiée comme une mesure de surveillance continue des salariés [4]. Cette pratique relève d’une interdiction prévue dans l’article 5, point b bis), qui vise à empêcher toute production ou manipulation de contenus réalistes représentant des personnes identifiables sans consentement explicite. Aucun passage ne permet de justifier une surveillance continue des salariés par caméra dans un atelier.
```

</details>

Temps : recherche 2.2 s · génération 32.8 s (3463 tokens lus, 365 écrits, 33.4 tokens/s) · contrôle de pertinence 4.3 s

## q35 — Notre fédération sportive peut-elle rédiger un guide de bonnes pratiques RGPD que ses clubs pourraient suivre officiellement ?

Article attendu : RGPD art. 40 — passage [1].

### Réponse du copilote

> Oui : votre fédération sportive peut rédiger un guide de bonnes pratiques RGPD que ses clubs pourraient suivre officiellement, car elle est une « association représentant des catégories de responsables du traitement » [1]. Ce texte autorise les associations à élaborer des codes de conduite, y compris pour préciser les modalités d'application du RGPD [1]. De plus, le texte précise que les autorités de contrôle, y compris les organismes comme votre fédération, encouragent l'élaboration de codes de conduite [3], et que les codes de conduite peuvent être approuvés par une autorité de contrôle [4]. Ainsi, votre fédération peut, en tant qu'association, élaborer un tel guide, qui pourrait être officiellement reconnu ou approuvé selon les procédures prévues [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent élaborer des codes de conduite, les modifier ou les proroger, aux fins de préciser les modalités d'application du présent règlement, telles que: … »
  [3] « Les États membres, les autorités de contrôle, le comité et la Commission encouragent l'élaboration de codes de conduite destinés à contribuer à la bonne application du présent règlement, compte tenu de la spécificité des différents secteurs de traitement et des besoins spécifiques des micro, petites et moyennes entreprises. »
  [4] « … encourage l'élaboration de codes de conduite en application de l'article 40, paragraphe 1, rend un avis et approuve les codes de conduite qui fournissent des garanties suffisantes, en application de l'article 40, paragraphe 5; »

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
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « association représentant des catégories de responsables du traitement ».

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent élaborer des codes de conduite, les modifier ou les proroger, aux fins de préciser les modalités d'application du présent règlement, telles que: … »  
- [3] « Les États membres, les autorités de contrôle, le comité et la Commission encouragent l'élaboration de codes de conduite destinés à contribuer à la bonne application du présent règlement, compte tenu de la spécificité des différents secteurs de traitement et des besoins spécifiques des micro, petites et moyennes entreprises. »  
- [4] « … encourage l'élaboration de codes de conduite en application de l'article 40, paragraphe 1, rend un avis et approuve les codes de conduite qui fournissent des garanties suffisantes, en application de l'article 40, paragraphe 5; »  

RÉPONSE :  
Oui : votre fédération sportive peut rédiger un guide de bonnes pratiques RGPD que ses clubs pourraient suivre officiellement, car elle est une « association représentant des catégories de responsables du traitement » [1]. Ce texte autorise les associations à élaborer des codes de conduite, y compris pour préciser les modalités d'application du RGPD [1]. De plus, le texte précise que les autorités de contrôle, y compris les organismes comme votre fédération, encouragent l'élaboration de codes de conduite [3], et que les codes de conduite peuvent être approuvés par une autorité de contrôle [4]. Ainsi, votre fédération peut, en tant qu'association, élaborer un tel guide, qui pourrait être officiellement reconnu ou approuvé selon les procédures prévues [4].
```

</details>

Temps : recherche 2.2 s · génération 39.8 s (3975 tokens lus, 436 écrits, 32.1 tokens/s) · contrôle de pertinence 4.2 s

## q36 — Un ancien bénévole menace de se plaindre de nous auprès de la CNIL : en a-t-il le droit, et quels autres recours a-t-il ?

Article attendu : RGPD art. 77 — absent des passages donnés au modèle.

### Réponse du copilote

> Oui : un ancien bénévole a le droit de se plaindre de vous auprès de la CNIL, car il est considéré comme une personne concernée et peut exercer ses droits de réclamation en son nom, notamment en vertu de l’article 80 du RGPD [1]. Il peut également faire valoir son droit de se plaindre auprès de l’autorité de contrôle compétente (comme la CNIL) si le traitement de ses données a été violé [1]. En outre, s’il considère que ses droits ont été violés, il peut engager une action juridictionnelle devant les juridictions de l’État membre où vous disposez d’un établissement ou où il a sa résidence habituelle [4]. Ce droit s’applique même si l’ancien bénévole n’est plus actif dans l’organisation, à condition qu’il soit concerné par le traitement de ses données à caractère personnel [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit de mandater un organisme, une organisation ou une association à but non lucratif, qui a été valablement constitué conformément au droit d'un État membre, dont les objectifs statutaires sont d'intérêt public et est actif dans le domaine de la protection des droits et libertés des personnes concernées dans le cadre de la protection des données à caractère personnel les concernant, pour qu'il introduise une réclamation en son nom, exerce en son nom les droits visés aux articles 77, 78 et 79 et exerce en son nom le droit d'obtenir réparation visé à l'article 82 lorsque le droit d'un État membre le prévoit. »
  [1] « Les États membres peuvent prévoir que tout organisme, organisation ou association visé au paragraphe 1 du présent article, indépendamment de tout mandat confié par une personne concernée, a, dans l'État membre en question, le droit d'introduire une réclamation auprès de l'autorité de contrôle qui est compétente en vertu de l'article 77, et d'exercer les droits visés aux articles 78 et 79 s'il considère que les droits d'une personne concernée prévus dans le présent règlement ont été violés du fait du traitement. »
  [4] « Toute action contre un responsable du traitement ou un sous-traitant est intentée devant les juridictions de l'État membre dans lequel le responsable du traitement ou le sous-traitant dispose d'un établissement. Une telle action peut aussi être intentée devant les juridictions de l'État membre dans lequel la personne concernée a sa résidence habituelle, sauf si le responsable du traitement ou le sous-traitant est une autorité publique d'un État membre agissant dans l'exercice de ses prérogatives de puissance publique. »

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
- [1] « Les États membres peuvent prévoir que tout organisme, organisation ou association visé au paragraphe 1 du présent article, indépendamment de tout mandat confié par une personne concernée, a, dans l'État membre en question, le droit d'introduire une réclamation auprès de l'autorité de contrôle qui est compétente en vertu de l'article 77, et d'exercer les droits visés aux articles 78 et 79 s'il considère que les droits d'une personne concernée prévus dans le présent règlement ont été violés du fait du traitement. »  
- [4] « Toute action contre un responsable du traitement ou un sous-traitant est intentée devant les juridictions de l'État membre dans lequel le responsable du traitement ou le sous-traitant dispose d'un établissement. Une telle action peut aussi être intentée devant les juridictions de l'État membre dans lequel la personne concernée a sa résidence habituelle, sauf si le responsable du traitement ou le sous-traitant est une autorité publique d'un État membre agissant dans l'exercice de ses prérogatives de puissance publique. »  

RÉPONSE :  
Oui : un ancien bénévole a le droit de se plaindre de vous auprès de la CNIL, car il est considéré comme une personne concernée et peut exercer ses droits de réclamation en son nom, notamment en vertu de l’article 80 du RGPD [1]. Il peut également faire valoir son droit de se plaindre auprès de l’autorité de contrôle compétente (comme la CNIL) si le traitement de ses données a été violé [1]. En outre, s’il considère que ses droits ont été violés, il peut engager une action juridictionnelle devant les juridictions de l’État membre où vous disposez d’un établissement ou où il a sa résidence habituelle [4]. Ce droit s’applique même si l’ancien bénévole n’est plus actif dans l’organisation, à condition qu’il soit concerné par le traitement de ses données à caractère personnel [1].
```

</details>

Temps : recherche 2.2 s · génération 32.6 s (2606 tokens lus, 664 écrits, 35.0 tokens/s) · contrôle de pertinence 5.9 s

## q37 — Si une fuite de données cause un préjudice à un client, peut-il nous demander réparation ?

Article attendu : RGPD art. 82 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

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
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Lorsqu'une violation de données à caractère personnel est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement communique la violation de données à caractère personnel à la personne concernée dans les meilleurs délais. »  
- [2] « violation de données à caractère personnel», une violation de la sécurité entraînant, de manière accidentelle ou illicite, la destruction, la perte, l'altération, la divulgation non autorisée de données à caractère personnel transmises, conservées ou traitées d'une autre manière, ou l'accès non autorisé à de telles données;  
- [3] « La personne concernée a le droit d'obtenir du responsable du traitement, dans les meilleurs délais, la rectification des données à caractère personnel la concernant qui sont inexactes. »  
- [4] « Lorsqu'il a rendu publiques les données à caractère personnel et qu'il est tenu de les effacer en vertu du paragraphe 1, le responsable du traitement, compte tenu des technologies disponibles et des coûts de mise en œuvre, prend des mesures raisonnables, y compris d'ordre technique, pour informer les responsables du traitement qui traitent ces données à caractère personnel que la personne concernée a demandé l'effacement par ces responsables du traitement de tout lien vers ces données à caractère personnel, ou de toute copie ou reproduction de celles-ci. »  
- [5] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: … »

RÉPONSE :  
Les textes trouvés ne traitent pas directement de la possibilité de réparation pour un préjudice causé par une fuite de données. Ils énoncent des obligations de communication (article 34), de rectification (article 16), d'accès (article 15) et d'effacement (article 17), mais ne mentionnent aucune obligation de réparation ni de responsabilité civile ou pénale en cas de préjudice. Ainsi, la question de la réparation d'un préjudice à un client ne peut être répondue sur la base des extraits fournis.
```

</details>

Temps : recherche 2.2 s · génération 37.4 s (3445 tokens lus, 542 écrits, 33.1 tokens/s) · contrôle de pertinence 5.9 s

## q38 — Notre club de sport peut-il demander un extrait de casier judiciaire aux bénévoles qui encadrent des enfants ?

Article attendu : RGPD art. 10 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

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
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [5] « les mesures et les procédures visées aux articles 24 et 25 et les mesures visant à assurer la sécurité du traitement visées à l'article 32 »  
- [5] « la notification aux autorités de contrôle des violations de données à caractère personnel et la communication de ces violations aux personnes concernées »  
- [5] « le transfert de données à caractère personnel vers des pays tiers ou à des organisations internationales »  
- [5] « les procédures extrajudiciaires et autres procédures de règlement des litiges permettant de résoudre les litiges entre les responsables du traitement et les personnes concernées en ce qui concerne le traitement, sans préjudice des droits des personnes concernées au titre des articles 77 et 79 »  

RÉPONSE :  
Les passages trouvés ne traitent pas directement de la demande d’un extrait de casier judiciaire par un club de sport à des bénévoles encadrant des enfants. Aucun des extraits ne mentionne la collecte, le traitement ou la demande d’un extrait de casier judiciaire, ni la nécessité d’un consentement éclairé ou de conditions spécifiques pour ce type de données. Bien que le RGPD prévoie des règles sur la collecte de données à caractère personnel (article 5, point a), notamment dans le cadre de la transparence, de la sécurité et du consentement, aucun élément ne justifie ou autorise une demande d’extrait de casier judiciaire, qui relève d’un autre cadre juridique (ex. : droit pénal, droit de l’administration publique). Les obligations relatives à la collecte de données personnelles, comme celles concernant les enfants (point g du passage [5]), ne couvrent pas ce type de demande. Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Temps : recherche 2.2 s · génération 30.9 s (3115 tokens lus, 435 écrits, 34.1 tokens/s) · contrôle de pertinence 4.6 s

## q39 — Si nous remplaçons les noms de nos adhérents par des numéros, les données sont-elles encore des données personnelles ?

Article attendu : RGPD art. 4, définition 5 — passage [3].

### Réponse du copilote

> Oui, les données sont encore des données personnelles si elles permettent d'identifier une personne physique, même par un numéro d'identification, car le RGPD, article 4, définit les « données à caractère personnel » comme toute information se rapportant à une personne physique identifiée ou identifiable, notamment par référence à un identifiant, tel qu'un numéro d'identification [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « «données à caractère personnel», toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée»); est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale; »

Sources citées :
  [2] RGPD — règlement (UE) 2016/679, article 4, définition 1 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 96 : Relation avec les accords conclus antérieurement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_96
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 5 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [4] RGPD — règlement (UE) 2016/679, article 87 : Traitement du numéro d'identification national
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_87
  [5] RGPD — règlement (UE) 2016/679, article 47, paragraphe 2, points a) à k) : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [2] « «données à caractère personnel», toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée»); est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale; »

RÉPONSE :  
Oui, les données sont encore des données personnelles si elles permettent d'identifier une personne physique, même par un numéro d'identification, car le RGPD, article 4, définit les « données à caractère personnel » comme toute information se rapportant à une personne physique identifiée ou identifiable, notamment par référence à un identifiant, tel qu'un numéro d'identification [2].
```

</details>

Temps : recherche 2.2 s · génération 21.8 s (2803 tokens lus, 230 écrits, 35.1 tokens/s) · contrôle de pertinence 3.7 s

## q40 — Nous allons utiliser un logiciel d'IA à haut risque qui attribue les tâches à nos salariés : devons-nous les prévenir avant de l'utiliser ?

Article attendu : AI Act art. 26 — passage [1].

### Réponse du copilote

> Oui : vous devez prévenir les représentants des travailleurs et les travailleurs concernés avant de mettre en service ou d’utiliser un système d’IA à haut risque sur le lieu de travail [1]. Ce point s’applique à un logiciel d’IA à haut risque attribuant des tâches aux salariés, puisque ce type d’usage relève du domaine de la gestion de la main-d’œuvre visé à l’annexe III, point 4, a) et b) [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Avant de mettre en service ou d’utiliser un système d’IA à haut risque sur le lieu de travail, les déployeurs qui sont des employeurs informent les représentants des travailleurs et les travailleurs concernés qu’ils seront soumis à l’utilisation du système d’IA à haut risque. »

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
Attention : La réponse cite [3] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Avant de mettre en service ou d’utiliser un système d’IA à haut risque sur le lieu de travail, les déployeurs qui sont des employeurs informent les représentants des travailleurs et les travailleurs concernés qu’ils seront soumis à l’utilisation du système d’IA à haut risque. »

RÉPONSE :
Oui : vous devez prévenir les représentants des travailleurs et les travailleurs concernés avant de mettre en service ou d’utiliser un système d’IA à haut risque sur le lieu de travail [1]. Ce point s’applique à un logiciel d’IA à haut risque attribuant des tâches aux salariés, puisque ce type d’usage relève du domaine de la gestion de la main-d’œuvre visé à l’annexe III, point 4, a) et b) [3].
```

</details>

Temps : recherche 2.2 s · génération 21.6 s (2902 tokens lus, 198 écrits, 35.1 tokens/s) · contrôle de pertinence 3.2 s

## q41 — Notre organisme de formation peut-il utiliser une IA pour noter les examens de ses stagiaires ? Est-ce encadré ?

Article attendu : AI Act annexe III, point 3 — passage [1].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, annexe III, point 3 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [2] AI Act — règlement (UE) 2024/1689, article 12 : Enregistrement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_12
  [3] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [4] AI Act — règlement (UE) 2024/1689, annexe XIV : Liste des codes, des catégories et des types correspondants de systèmes d'IA aux fins de la procédure de notification visée à l'article 30, précisant le champ d'application de la désignation en tant qu'organismes notifiés
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_XIV
  [5] AI Act — règlement (UE) 2024/1689, article 4 : Maîtrise de l'IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_4
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « systèmes d'IA destinés à être utilisés pour surveiller et détecter des comportements interdits chez les étudiants lors d'examens dans le contexte d'établissements d'enseignement et de formation ou en leur sein à tous les niveaux; »
- [2] « Pour les systèmes d'IA à haut risque visés à l'annexe III, point 1 a), les fonctionnalités de journalisation fournissent, au minimum: … »
- [4] « a) Systèmes d'IA relevant de l'annexe I … »
- [4] « b) Systèmes d'IA relevant de l'annexe III, point 1 … »

RÉPONSE :
Oui, votre organisme de formation peut utiliser une IA pour noter les examens de ses stagiaires, car cela relève du domaine de l'éducation et de la formation professionnelle, visé à l’article 6, paragraphe 2, de l’AI Act, dans l’annexe III, point 3a) [1]. Cependant, cette utilisation est encadrée : les systèmes d’IA destinés à noter les examens ou à évaluer les acquis d’apprentissage sont considérés comme des systèmes d’IA à haut risque [1]. Pour ces systèmes, des obligations spécifiques s’appliquent, notamment l’enregistrement automatique des événements (journalisation) pour garantir une traçabilité adaptée à la destination du système [2]. Ces systèmes doivent être notifiés conformément à l’article 30 du règlement (UE) 2024/1689, en particulier dans le cadre des codes AIB 0201 à AIB 0203, correspondant aux systèmes d’IA relevant de l’annexe III, point 1 [4]. Ainsi, l’utilisation d’une IA pour noter les examens est encadrée par l’AI Act, notamment par l’obligation de notification et de traçabilité.
```

</details>

Temps : recherche 2.2 s · génération 39.7 s (3857 tokens lus, 477 écrits, 32.3 tokens/s) · contrôle de pertinence 3.7 s

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
- [1] « systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »
- [5] « fournir aux déployeurs les informations requises conformément à l’article 13 et, éventuellement, une formation. »
- [5] « En vue de l’élimination ou de la réduction des risques liés à l’utilisation du système d’IA à haut risque, il est dûment tenu compte des connaissances techniques, de l’expérience, de l’éducation et de la formation pouvant être attendues du déployeur, ainsi que du contexte prévisible dans lequel le système est destiné à être utilisé. »

RÉPONSE :
Oui : vous devez lui expliquer pourquoi, car un système d'IA à haut risque destiné à analyser et filtrer les candidatures (article 6, paragraphe 2, point 4a) est visé par l'AI Act, et que le déployeur est tenu de fournir aux utilisateurs les informations requises conformément à l’article 13, y compris une formation, afin de permettre une compréhension des décisions prises (AI Act, article 9, point c). Cette obligation s’inscrit dans le cadre de la réduction des risques liés à l’utilisation du système, en tenant compte des connaissances techniques et de la formation du déployeur [5].
```

</details>

Temps : recherche 2.2 s · génération 23.2 s (2579 tokens lus, 363 écrits, 35.5 tokens/s) · contrôle de pertinence 4.0 s

## q43 — Le règlement européen sur l'IA prévoit-il des mesures particulières pour les PME ?

Article attendu : AI Act art. 62 — passage [1].

### Réponse du copilote

> Oui : le règlement européen sur l’IA prévoit des mesures particulières pour les PME, y compris les jeunes pousses. Les États membres leur accordent un accès prioritaire aux bacs à sable réglementaires de l’IA, dans la mesure où elles remplissent les conditions d’éligibilité et les critères de sélection [1]. Ils organisent des activités spécifiques de sensibilisation et de formation adaptées à leurs besoins [1]. Ils utilisent des canaux privilégiés pour fournir des conseils et répondre à leurs questions [1]. Les autorités nationales compétentes peuvent également fournir des orientations et des conseils, en particulier aux PME [3]. Les PME peuvent se conformer de manière simplifiée à certains éléments du système de gestion de la qualité [2]. L’accès aux bacs à sable réglementaires est gratuit pour les PME [5]. Les procédures administratives sont simples, claires et rationalisées pour faciliter leur participation [5]. Ces mesures visent à répondre aux spécificités des PME, notamment leurs capacités juridiques et administratives limitées [5].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les États membres: a) accordent aux PME, y compris les jeunes pousses, qui ont leur siège social ou une succursale dans l’Union, un accès prioritaire aux bacs à sable réglementaires de l’IA, dans la mesure où elles remplissent les conditions d’éligibilité et les critères de sélection; »
  [1] « b) organisent des activités spécifiques de sensibilisation et de formation à l’application du présent règlement, adaptées aux besoins des PME, y compris les jeunes pousses, les déployeurs et, si nécessaire, les pouvoirs publics locaux; »
  [1] « c) utilisent des canaux privilégiés existants et, s’il y a lieu, en établissent de nouveaux avec les PME, y compris les jeunes pousses, les déployeurs, d’autres innovateurs et, si nécessaire, les pouvoirs publics locaux, afin de fournir des conseils et de répondre aux questions relatives à la mise en œuvre du présent règlement, y compris en ce qui concerne la participation à des bacs à sable réglementaires de l’IA; »
  [1] « d) facilitent la participation des PME et d’autres parties concernées au processus d’élaboration de la normalisation. »
  [2] « Les PME, y compris les jeunes pousses, peuvent se conformer de manière simplifiée à certains éléments du système de gestion de la qualité requis par l'article 17, pour autant qu'elles n'aient pas d'entreprises partenaires ou d'entreprises liées au sens de la recommandation 2003/361/CE. »
  [3] « Les autorités nationales compétentes peuvent fournir des orientations et des conseils sur la mise en œuvre du présent règlement, en particulier aux PME, y compris les jeunes pousses, et aux petites entreprises à moyenne capitalisation, en tenant compte des orientations et conseils du Comité IA et de la Commission, selon le cas. »
  [5] « l’accès aux bacs à sable réglementaires de l’IA est gratuit pour les PME, y compris les jeunes pousses, sans préjudice des coûts exceptionnels que les autorités nationales compétentes peuvent recouvrer de manière équitable et proportionnée; »
  [5] « les procédures, processus et exigences administratives applicables en matière de demande, de sélection, de participation et de sortie dans le cadre du bac à sable réglementaires de l’IA sont simples, facilement compréhensibles et clairement communiqués afin de faciliter la participation des PME, y compris des jeunes pousses, disposant de capacités juridiques et administratives limitées, et sont rationalisés dans toute l’Union, afin d’éviter la fragmentation et de permettre que la participation à un bac à sable réglementaire de l’IA mis en place par un État membre ou par le Contrôleur européen de la protection des données soit mutuellement et uniformément reconnue et produise les mêmes effets juridiques dans l’ensemble de l’Union; »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 62 : Mesures en faveur des fournisseurs et déployeurs, en particulier les PME, y compris les jeunes pousses (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_62
  [2] AI Act — règlement (UE) 2024/1689, article 63 : Dérogations pour des opérateurs spécifiques (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_63
  [3] AI Act — règlement (UE) 2024/1689, article 70, paragraphe 8 : Désignation des autorités nationales compétentes et des points de contact uniques (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_70
  [5] AI Act — règlement (UE) 2024/1689, article 58, paragraphe 2 : Modalités détaillées pour les bacs à sable réglementaires de l’IA et fonctionnement de ceux-ci (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_58
Passages consultés mais non cités :
  [4] AI Act — règlement (UE) 2024/1689, article 70, paragraphe 1 : Désignation des autorités nationales compétentes et des points de contact uniques
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_70

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les États membres: a) accordent aux PME, y compris les jeunes pousses, qui ont leur siège social ou une succursale dans l’Union, un accès prioritaire aux bacs à sable réglementaires de l’IA, dans la mesure où elles remplissent les conditions d’éligibilité et les critères de sélection; »
- [1] « b) organisent des activités spécifiques de sensibilisation et de formation à l’application du présent règlement, adaptées aux besoins des PME, y compris les jeunes pousses, les déployeurs et, si nécessaire, les pouvoirs publics locaux; »
- [1] « c) utilisent des canaux privilégiés existants et, s’il y a lieu, en établissent de nouveaux avec les PME, y compris les jeunes pousses, les déployeurs, d’autres innovateurs et, si nécessaire, les pouvoirs publics locaux, afin de fournir des conseils et de répondre aux questions relatives à la mise en œuvre du présent règlement, y compris en ce qui concerne la participation à des bacs à sable réglementaires de l’IA; »
- [1] « d) facilitent la participation des PME et d’autres parties concernées au processus d’élaboration de la normalisation. »
- [2] « Les PME, y compris les jeunes pousses, peuvent se conformer de manière simplifiée à certains éléments du système de gestion de la qualité requis par l'article 17, pour autant qu'elles n'aient pas d'entreprises partenaires ou d'entreprises liées au sens de la recommandation 2003/361/CE. »
- [3] « Les autorités nationales compétentes peuvent fournir des orientations et des conseils sur la mise en œuvre du présent règlement, en particulier aux PME, y compris les jeunes pousses, et aux petites entreprises à moyenne capitalisation, en tenant compte des orientations et conseils du Comité IA et de la Commission, selon le cas. »
- [5] « l’accès aux bacs à sable réglementaires de l’IA est gratuit pour les PME, y compris les jeunes pousses, sans préjudice des coûts exceptionnels que les autorités nationales compétentes peuvent recouvrer de manière équitable et proportionnée; »
- [5] « les procédures, processus et exigences administratives applicables en matière de demande, de sélection, de participation et de sortie dans le cadre du bac à sable réglementaires de l’IA sont simples, facilement compréhensibles et clairement communiqués afin de faciliter la participation des PME, y compris des jeunes pousses, disposant de capacités juridiques et administratives limitées, et sont rationalisés dans toute l’Union, afin d’éviter la fragmentation et de permettre que la participation à un bac à sable réglementaire de l’IA mis en place par un État membre ou par le Contrôleur européen de la protection des données soit mutuellement et uniformément reconnue et produise les mêmes effets juridiques dans l’ensemble de l’Union; »

RÉPONSE :
Oui : le règlement européen sur l’IA prévoit des mesures particulières pour les PME, y compris les jeunes pousses. Les États membres leur accordent un accès prioritaire aux bacs à sable réglementaires de l’IA, dans la mesure où elles remplissent les conditions d’éligibilité et les critères de sélection [1]. Ils organisent des activités spécifiques de sensibilisation et de formation adaptées à leurs besoins [1]. Ils utilisent des canaux privilégiés pour fournir des conseils et répondre à leurs questions [1]. Les autorités nationales compétentes peuvent également fournir des orientations et des conseils, en particulier aux PME [3]. Les PME peuvent se conformer de manière simplifiée à certains éléments du système de gestion de la qualité [2]. L’accès aux bacs à sable réglementaires est gratuit pour les PME [5]. Les procédures administratives sont simples, claires et rationalisées pour faciliter leur participation [5]. Ces mesures visent à répondre aux spécificités des PME, notamment leurs capacités juridiques et administratives limitées [5].
```

</details>

Temps : recherche 2.2 s · génération 54.4 s (3631 tokens lus, 1009 écrits, 32.1 tokens/s) · contrôle de pertinence 7.7 s

## q44 — À partir de quelle date devrons-nous respecter les obligations sur les systèmes d'IA à haut risque utilisés pour le recrutement ?

Article attendu : AI Act art. 113 — absent des passages donnés au modèle.

### Réponse du copilote

> Les obligations sur les systèmes d'IA à haut risque utilisés pour le recrutement s'appliquent à partir de la date de l'entrée en vigueur du règlement (UE) 2024/1689, qui n'est pas précisée dans les extraits. Cependant, la Commission adopte des actes délégués au plus tard le 2 août 2027 pour préciser les systèmes d'IA à haut risque concernés, les exigences ou obligations qui peuvent être limitées, les conditions dans lesquelles cette limitation s'applique et la portée de la limitation [2]. Ainsi, les obligations devront être respectées à partir de cette date de précision, c’est-à-dire au plus tard le 2 août 2027 [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »
  [2] « Au plus tard le 2 août 2027, la Commission adopte des actes délégués conformément à l'article 97 afin de compléter le présent règlement afin de préciser les systèmes d'IA à haut risque concernés, les exigences ou obligations qui peuvent être limitées, les conditions dans lesquelles cette limitation s'applique et la portée de la limitation. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [2] AI Act — règlement (UE) 2024/1689, article 2, paragraphe 13 : Champ d’application (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_2
Passages consultés mais non cités :
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
EXTRAITS :
- [1] « systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »
- [2] « Au plus tard le 2 août 2027, la Commission adopte des actes délégués conformément à l'article 97 afin de compléter le présent règlement afin de préciser les systèmes d'IA à haut risque concernés, les exigences ou obligations qui peuvent être limitées, les conditions dans lesquelles cette limitation s'applique et la portée de la limitation. »

RÉPONSE :
Les obligations sur les systèmes d'IA à haut risque utilisés pour le recrutement s'appliquent à partir de la date de l'entrée en vigueur du règlement (UE) 2024/1689, qui n'est pas précisée dans les extraits. Cependant, la Commission adopte des actes délégués au plus tard le 2 août 2027 pour préciser les systèmes d'IA à haut risque concernés, les exigences ou obligations qui peuvent être limitées, les conditions dans lesquelles cette limitation s'applique et la portée de la limitation [2]. Ainsi, les obligations devront être respectées à partir de cette date de précision, c’est-à-dire au plus tard le 2 août 2027 [2].
```

</details>

Temps : recherche 2.2 s · génération 26.4 s (2888 tokens lus, 352 écrits, 34.7 tokens/s) · contrôle de pertinence 4.6 s

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
EXTRAITS :  
aucun

RÉPONSE :  
Les textes trouvés ne traitent pas de ce point.
```

</details>

Temps : recherche 2.1 s · génération 12.5 s (2382 tokens lus, 29 écrits, 37.7 tokens/s)

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
RÉPONSE : Les textes trouvés ne traitent pas de votre question.
```

</details>

Temps : recherche 2.1 s · génération 25.8 s (3879 tokens lus, 26 écrits, 34.0 tokens/s)

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
RÉPONSE : Les textes trouvés ne traitent pas de ce point.
```

</details>

Temps : recherche 2.1 s · génération 28.0 s (4065 tokens lus, 26 écrits, 34.0 tokens/s)
