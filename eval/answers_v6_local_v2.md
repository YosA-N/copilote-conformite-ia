# Réponses du copilote — v6_local_v2

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 18/11/2026 à 16:39 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen3:4b-instruct` via Ollama 0.40.16 — température 0.1, contexte 8192 tokens, couches sur la carte graphique : toutes, 2000 tokens au plus par réponse
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu, reranker `BAAI/bge-reranker-v2-m3` sur CPU (20 candidats reclassés avant la limite par article), reformulation de la question par le modèle avant la recherche (termes juridiques ajoutés, sans conclusion)
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_v2.jsonl` (17 + 3 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q28 | Un adhérent nous signale que son adresse et sa date de naissance sont fausses dans notre fichier : devons-nous les corriger, et dans quel délai ? | 1/1 | non | — | 76 s |
| q29 | Une cliente conteste l'exactitude des informations que nous avons sur elle : pouvons-nous continuer à les utiliser pendant que nous vérifions ? | 1/1 | non | La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à condition que cette durée soit suffisante pour permettre la vérification [1] » (et 2 autre(s)). Vérifiez-la dans les textes. | 56 s |
| q30 | Pouvons-nous refuser automatiquement une demande d'inscription à notre service à partir d'un score calculé par un logiciel, sans qu'une personne ne vérifie ? | 4/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 68 s |
| q31 | Nous faisons développer une application mobile pour nos membres : quelles précautions de protection des données devons-nous prévoir dès sa conception ? | 4/4 | non | — | 83 s |
| q32 | Nous organisons un festival avec une autre association et nous gérons ensemble le fichier des participants : qui est responsable de ces données ? | 2/2 | non | — | 55 s |
| q33 | Nous avons acheté un fichier de prospects à une autre entreprise : devons-nous informer ces personnes, et dans quel délai ? | 5/5 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 87 s |
| q34 | Puis-je installer des caméras dans l'atelier pour surveiller le travail de mes salariés ? | 3/3 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 89 s |
| q35 | Notre fédération sportive peut-elle rédiger un guide de bonnes pratiques RGPD que ses clubs pourraient suivre officiellement ? | 3/3 | non | — | 79 s |
| q36 | Un ancien bénévole menace de se plaindre de nous auprès de la CNIL : en a-t-il le droit, et quels autres recours a-t-il ? | 4/4 | non | — | 78 s |
| q37 | Si une fuite de données cause un préjudice à un client, peut-il nous demander réparation ? | 2/2 | non | — | 61 s |
| q38 | Notre club de sport peut-il demander un extrait de casier judiciaire aux bénévoles qui encadrent des enfants ? | 4/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 77 s |
| q39 | Si nous remplaçons les noms de nos adhérents par des numéros, les données sont-elles encore des données personnelles ? | 1/1 | non | — | 63 s |
| q40 | Nous allons utiliser un logiciel d'IA à haut risque qui attribue les tâches à nos salariés : devons-nous les prévenir avant de l'utiliser ? | 3/3 | non | — | 73 s |
| q41 | Notre organisme de formation peut-il utiliser une IA pour noter les examens de ses stagiaires ? Est-ce encadré ? | 3/3 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 85 s |
| q42 | Un candidat refusé après l'analyse de sa candidature par un outil d'IA à haut risque nous demande pourquoi : devons-nous lui expliquer ? | 3/3 | non | — | 63 s |
| q43 | Le règlement européen sur l'IA prévoit-il des mesures particulières pour les PME ? | 7/7 | non | — | 88 s |
| q44 | À partir de quelle date devrons-nous respecter les obligations sur les systèmes d'IA à haut risque utilisés pour le recrutement ? | 2/2 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 60 s |
| h06 | Quelles mentions obligatoires doivent figurer sur une facture ? | 0/0 | oui | — | 50 s |
| h07 | Comment demander une subvention à la mairie pour notre association ? | 0/0 | oui | — | 36 s |
| h08 | Quelles sont les règles pour embaucher un apprenti dans une PME ? | 0/0 | oui | — | 54 s |

## q28 — Un adhérent nous signale que son adresse et sa date de naissance sont fausses dans notre fichier : devons-nous les corriger, et dans quel délai ?

Article attendu : RGPD art. 16 — passage [1].

### Réponse du copilote

> Oui : vous devez corriger les données à caractère personnel inexactes, telles que l'adresse et la date de naissance, car elles sont fausses. Cette rectification doit être effectuée dans les meilleurs délais [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit d'obtenir du responsable du traitement, dans les meilleurs délais, la rectification des données à caractère personnel la concernant qui sont inexactes. Compte tenu des finalités du traitement, la personne concernée a le droit d'obtenir que les données à caractère personnel incomplètes soient complétées, y compris en fournissant une déclaration complémentaire. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 16 : Droit de rectification (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_16
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 24 : Responsabilité du responsable du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_24
  [3] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [4] RGPD — règlement (UE) 2016/679, article 34 : Communication à la personne concernée d'une violation de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_34
  [5] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « La personne concernée a le droit d'obtenir du responsable du traitement, dans les meilleurs délais, la rectification des données à caractère personnel la concernant qui sont inexactes. Compte tenu des finalités du traitement, la personne concernée a le droit d'obtenir que les données à caractère personnel incomplètes soient complétées, y compris en fournissant une déclaration complémentaire. »

RÉPONSE :  
Oui : vous devez corriger les données à caractère personnel inexactes, telles que l'adresse et la date de naissance, car elles sont fausses. Cette rectification doit être effectuée dans les meilleurs délais [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données personnelles ; traitement des données ; obligation de correction ; délai de correction ; responsabilité du responsable du traitement ; conformité avec le règlement

Temps : recherche 40.1 s · génération 28.6 s (3713 tokens lus, 160 écrits, 33.1 tokens/s) · contrôle de pertinence 4.0 s · reformulation 3.4 s

## q29 — Une cliente conteste l'exactitude des informations que nous avons sur elle : pouvons-nous continuer à les utiliser pendant que nous vérifions ?

Article attendu : RGPD art. 18 — passage [1].

### Réponse du copilote

> Oui : lorsque la personne concernée conteste l'exactitude des données à caractère personnel, le traitement peut être limité, mais pendant la durée permettant au responsable du traitement de vérifier l'exactitude, les données peuvent être utilisées, à condition que cette durée soit suffisante pour permettre la vérification [1]. Cette période ne permet pas de continuer à les utiliser sans restriction, car le traitement est soumis à une limitation, sauf si une autre finalité légitime ou un motif d'intérêt public justifie une utilisation continue. La durée de cette période est déterminée par le responsable du traitement, à l'exception de la conservation, qui reste autorisée dans les cas précisés à l'article 18, paragraphe 2 [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « l'exactitude des données à caractère personnel est contestée par la personne concernée, pendant une durée permettant au responsable du traitement de vérifier l'exactitude des données à caractère personnel; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 18 : Droit à la limitation du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_18
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [3] RGPD — règlement (UE) 2016/679, article 16 : Droit de rectification
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_16
  [4] RGPD — règlement (UE) 2016/679, article 4, définition 11 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [5] RGPD — règlement (UE) 2016/679, article 21 : Droit d'opposition
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_21
Attention : La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à condition que cette durée soit suffisante pour permettre la vérification [1] » (et 2 autre(s)). Vérifiez-la dans les textes.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « l'exactitude des données à caractère personnel est contestée par la personne concernée, pendant une durée permettant au responsable du traitement de vérifier l'exactitude des données à caractère personnel; »

RÉPONSE :  
Oui : lorsque la personne concernée conteste l'exactitude des données à caractère personnel, le traitement peut être limité, mais pendant la durée permettant au responsable du traitement de vérifier l'exactitude, les données peuvent être utilisées, à condition que cette durée soit suffisante pour permettre la vérification [1]. Cette période ne permet pas de continuer à les utiliser sans restriction, car le traitement est soumis à une limitation, sauf si une autre finalité légitime ou un motif d'intérêt public justifie une utilisation continue. La durée de cette période est déterminée par le responsable du traitement, à l'exception de la conservation, qui reste autorisée dans les cas précisés à l'article 18, paragraphe 2 [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données personnelles ; traitement ; finalité ; vérification ; droit d'accès ; consentement

Temps : recherche 26.1 s · génération 23.9 s (3050 tokens lus, 225 écrits, 34.4 tokens/s) · contrôle de pertinence 3.0 s · reformulation 3.1 s

## q30 — Pouvons-nous refuser automatiquement une demande d'inscription à notre service à partir d'un score calculé par un logiciel, sans qu'une personne ne vérifie ?

Article attendu : RGPD art. 22 — passage [1].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 22 : Décision individuelle automatisée, y compris le profilage
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_22
  [2] RGPD — règlement (UE) 2016/679, article 35, paragraphe 3 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [3] RGPD — règlement (UE) 2016/679, article 35, paragraphe 1 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [4] AI Act — règlement (UE) 2024/1689, article 6, point c : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
  [5] AI Act — règlement (UE) 2024/1689, article 7, paragraphe 2 : Modifications de l’annexe III
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_7
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « La personne concernée a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé, y compris le profilage, produisant des effets juridiques la concernant ou l'affectant de manière significative de façon similaire. »
- [1] « Le paragraphe 1 ne s'applique pas lorsque la décision: a) est nécessaire à la conclusion ou à l'exécution d'un contrat entre la personne concernée et un responsable du traitement; … c) est fondée sur le consentement explicite de la personne concernée. »
- [1] « Dans les cas visés au paragraphe 2, points a) et c), le responsable du traitement met en œuvre des mesures appropriées pour la sauvegarde des droits et libertés et des intérêts légitimes de la personne concernée, au moins du droit de la personne concernée d'obtenir une intervention humaine de la part du responsable du traitement, d'exprimer son point de vue et de contester la décision. »
- [3] « Lorsqu'un type de traitement, en particulier par le recours à de nouvelles technologies, et compte tenu de la nature, de la portée, du contexte et des finalités du traitement, est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, le responsable du traitement effectue, avant le traitement, une analyse de l'impact des opérations de traitement envisagées sur la protection des données à caractère personnel. »

RÉPONSE :
Non : vous ne pouvez pas refuser automatiquement une demande d'inscription à votre service à partir d'un score calculé par un logiciel sans que la personne vérifie, car la personne concernée a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé, y compris le profilage, produisant des effets juridiques la concernant ou l'affectant de manière significative de façon similaire [1]. Ce droit s'applique lorsque la décision est fondée exclusivement sur un traitement automatisé, sans intervention humaine [1]. À moins que la décision ne soit nécessaire à la conclusion ou à l'exécution d'un contrat entre la personne concernée et un responsable du traitement [1], ou fondée sur le consentement explicite de la personne concernée [1], une telle décision doit être accompagnée de mesures appropriées, notamment du droit d'obtenir une intervention humaine, d'exprimer son point de vue et de contester la décision [1]. Si le traitement est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, une analyse d'impact relative à la protection des données doit être effectuée avant le traitement [3].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : refus automatique ; décision algorithmique ; évaluation automatique ; traitement automatisé ; décision sans intervention humaine ; base de données décisionnelle

Temps : recherche 24.3 s · génération 35.8 s (3039 tokens lus, 630 écrits, 34.0 tokens/s) · contrôle de pertinence 4.9 s · reformulation 3.3 s

## q31 — Nous faisons développer une application mobile pour nos membres : quelles précautions de protection des données devons-nous prévoir dès sa conception ?

Article attendu : RGPD art. 25 — passage [1].

### Réponse du copilote

> Vous devez prévoir des mesures techniques et organisationnelles appropriées dès la conception de l'application mobile, telles que la pseudonymisation et le chiffrement des données à caractère personnel [1], [5]. Ces mesures doivent garantir que, par défaut, seules les données nécessaires à chaque finalité spécifique du traitement sont collectées, traitées, conservées et accessibles [1]. Elles doivent aussi assurer la confidentialité, l'intégrité, la disponibilité et la résilience des systèmes et services de traitement [5]. De plus, une procédure régulière de test, d'analyse et d'évaluation de l'efficacité de ces mesures doit être mise en place [5]. Ces précautions s'appliquent à la quantité, à l'étendue, à la durée de conservation et à l'accessibilité des données [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le responsable du traitement met en œuvre, tant au moment de la détermination des moyens du traitement qu'au moment du traitement lui-même, des mesures techniques et organisationnelles appropriées, telles que la pseudonymisation, qui sont destinées à mettre en œuvre les principes relatifs à la protection des données, par exemple la minimisation des données, de façon effective et à assortir le traitement des garanties nécessaires afin de répondre aux exigences du présent règlement et de protéger les droits de la personne concernée. »
  [1] « Le responsable du traitement met en œuvre les mesures techniques et organisationnelles appropriées pour garantir que, par défaut, seules les données à caractère personnel qui sont nécessaires au regard de chaque finalité spécifique du traitement sont traitées. Cela s'applique à la quantité de données à caractère personnel collectées, à l'étendue de leur traitement, à leur durée de conservation et à leur accessibilité. En particulier, ces mesures garantissent que, par défaut, les données à caractère personnel ne sont pas rendues accessibles à un nombre indéterminé de personnes physiques sans l'intervention de la personne physique concernée. »
  [3] « Les finalités du traitement sont définies dans cette base juridique ou, en ce qui concerne le traitement visé au paragraphe 1, point e), sont nécessaires à l'exécution d'une mission d'intérêt public ou relevant de l'exercice de l'autorité publique dont est investi le responsable du traitement. »
  [5] « Compte tenu de l'état des connaissances, des coûts de mise en œuvre et de la nature, de la portée, du contexte et des finalités du traitement ainsi que des risques, dont le degré de probabilité et de gravité varie, pour les droits et libertés des personnes physiques, le responsable du traitement et le sous-traitant mettent en œuvre les mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque, y compris entre autres, selon les besoins: a) la pseudonymisation et le chiffrement des données à caractère personnel; b) des moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement; c) des moyens permettant de rétablir la disponibilité des données à caractère personnel et l'accès à celles-ci dans des délais appropriés en cas d'incident physique ou technique; d) une procédure visant à tester, à analyser et à évaluer régulièrement l'efficacité des mesures techniques et organisationnelles pour assurer la sécurité du traitement. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 25 : Protection des données dès la conception et protection des données par défaut (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_25
  [3] RGPD — règlement (UE) 2016/679, article 6, paragraphe 3 : Licéité du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
  [5] RGPD — règlement (UE) 2016/679, article 32 : Sécurité du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_32
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 24 : Responsabilité du responsable du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_24
  [4] RGPD — règlement (UE) 2016/679, article 6, paragraphe 1 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le responsable du traitement met en œuvre, tant au moment de la détermination des moyens du traitement qu'au moment du traitement lui-même, des mesures techniques et organisationnelles appropriées, telles que la pseudonymisation, qui sont destinées à mettre en œuvre les principes relatifs à la protection des données, par exemple la minimisation des données, de façon effective et à assortir le traitement des garanties nécessaires afin de répondre aux exigences du présent règlement et de protéger les droits de la personne concernée. »
- [1] « Le responsable du traitement met en œuvre les mesures techniques et organisationnelles appropriées pour garantir que, par défaut, seules les données à caractère personnel qui sont nécessaires au regard de chaque finalité spécifique du traitement sont traitées. Cela s'applique à la quantité de données à caractère personnel collectées, à l'étendue de leur traitement, à leur durée de conservation et à leur accessibilité. En particulier, ces mesures garantissent que, par défaut, les données à caractère personnel ne sont pas rendues accessibles à un nombre indéterminé de personnes physiques sans l'intervention de la personne physique concernée. »
- [3] « Les finalités du traitement sont définies dans cette base juridique ou, en ce qui concerne le traitement visé au paragraphe 1, point e), sont nécessaires à l'exécution d'une mission d'intérêt public ou relevant de l'exercice de l'autorité publique dont est investi le responsable du traitement. »
- [5] « Compte tenu de l'état des connaissances, des coûts de mise en œuvre et de la nature, de la portée, du contexte et des finalités du traitement ainsi que des risques, dont le degré de probabilité et de gravité varie, pour les droits et libertés des personnes physiques, le responsable du traitement et le sous-traitant mettent en œuvre les mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque, y compris entre autres, selon les besoins: a) la pseudonymisation et le chiffrement des données à caractère personnel; b) des moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement; c) des moyens permettant de rétablir la disponibilité des données à caractère personnel et l'accès à celles-ci dans des délais appropriés en cas d'incident physique ou technique; d) une procédure visant à tester, à analyser et à évaluer régulièrement l'efficacité des mesures techniques et organisationnelles pour assurer la sécurité du traitement. »

RÉPONSE :
Vous devez prévoir des mesures techniques et organisationnelles appropriées dès la conception de l'application mobile, telles que la pseudonymisation et le chiffrement des données à caractère personnel [1], [5]. Ces mesures doivent garantir que, par défaut, seules les données nécessaires à chaque finalité spécifique du traitement sont collectées, traitées, conservées et accessibles [1]. Elles doivent aussi assurer la confidentialité, l'intégrité, la disponibilité et la résilience des systèmes et services de traitement [5]. De plus, une procédure régulière de test, d'analyse et d'évaluation de l'efficacité de ces mesures doit être mise en place [5]. Ces précautions s'appliquent à la quantité, à l'étendue, à la durée de conservation et à l'accessibilité des données [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : traitement des données personnelles ; finalité du traitement ; conservation des données ; sécurité des données ; transparence ; responsabilité du responsable du traitement

Temps : recherche 27.4 s · génération 44.2 s (3239 tokens lus, 828 écrits, 33.2 tokens/s) · contrôle de pertinence 7.6 s · reformulation 3.3 s

## q32 — Nous organisons un festival avec une autre association et nous gérons ensemble le fichier des participants : qui est responsable de ces données ?

Article attendu : RGPD art. 26 — passage [2].

### Réponse du copilote

> Lorsque deux associations déterminent conjointement les finalités et les moyens du traitement du fichier des participants, elles sont les responsables conjoints du traitement [2]. Chaque association est responsable de son rôle dans le traitement, et les obligations du responsable du traitement s'appliquent à chacune d'elles [1]. Un point de contact peut être désigné dans l'accord entre elles [2]. La personne concernée peut exercer les droits prévus par le règlement à l'égard de chacun des responsables [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « «responsable du traitement», la personne physique ou morale, l'autorité publique, le service ou un autre organisme qui, seul ou conjointement avec d'autres, détermine les finalités et les moyens du traitement; »
  [2] « Lorsque deux responsables du traitement ou plus déterminent conjointement les finalités et les moyens du traitement, ils sont les responsables conjoints du traitement. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 4, définition 7 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [2] RGPD — règlement (UE) 2016/679, article 26 : Responsables conjoints du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_26
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 24 : Responsabilité du responsable du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_24
  [4] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [5] RGPD — règlement (UE) 2016/679, article 40, paragraphe 1 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « «responsable du traitement», la personne physique ou morale, l'autorité publique, le service ou un autre organisme qui, seul ou conjointement avec d'autres, détermine les finalités et les moyens du traitement; »
- [2] « Lorsque deux responsables du traitement ou plus déterminent conjointement les finalités et les moyens du traitement, ils sont les responsables conjoints du traitement. »

RÉPONSE :
Lorsque deux associations déterminent conjointement les finalités et les moyens du traitement du fichier des participants, elles sont les responsables conjoints du traitement [2]. Chaque association est responsable de son rôle dans le traitement, et les obligations du responsable du traitement s'appliquent à chacune d'elles [1]. Un point de contact peut être désigné dans l'accord entre elles [2]. La personne concernée peut exercer les droits prévus par le règlement à l'égard de chacun des responsables [2].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : responsabilité du traitement ; gestion conjointe ; partage de données ; coordination des données ; obligation de transparence ; lien de confiance

Temps : recherche 28.4 s · génération 19.7 s (2551 tokens lus, 228 écrits, 35.6 tokens/s) · contrôle de pertinence 4.0 s · reformulation 3.2 s

## q33 — Nous avons acheté un fichier de prospects à une autre entreprise : devons-nous informer ces personnes, et dans quel délai ?

Article attendu : RGPD art. 14 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 24 : Responsabilité du responsable du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_24
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [3] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [4] RGPD — règlement (UE) 2016/679, article 34 : Communication à la personne concernée d'une violation de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_34
  [5] RGPD — règlement (UE) 2016/679, article 6, paragraphe 4 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Le responsable du traitement met en œuvre des mesures techniques et organisationnelles appropriées pour s'assurer et être en mesure de démontrer que le traitement est effectué conformément au présent règlement. »  
- [2] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. Lorsque la personne concernée présente sa demande sous une forme électronique, les informations sont fournies par voie électronique lorsque cela est possible, à moins que la personne concernée ne demande qu'il en soit autrement. »  
- [3] « Le responsable du traitement prend des mesures appropriées pour fournir toute information visée aux articles 13 et 14 ainsi que pour procéder à toute communication au titre des articles 15 à 22 et de l'article 34 en ce qui concerne le traitement à la personne concernée d'une façon concise, transparente, compréhensible et aisément accessible, en des termes clairs et simples, en particulier pour toute information destinée spécifiquement à un enfant. Les informations sont fournies par écrit ou par d'autres moyens y compris, lorsque c'est approprié, par voie électronique. Lorsque la personne concernée en fait la demande, les informations peuvent être fournies oralement, à condition que l'identité de la personne concernée soit démontrée par d'autres moyens. »  
- [4] « Lorsqu'une violation de données à caractère personnel est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement communique la violation de données à caractère personnel à la personne concernée dans les meilleurs délais. »  
- [5] « Lorsque le traitement à une fin autre que celle pour laquelle les données ont été collectées n'est pas fondé sur le consentement de la personne concernée ou sur le droit de l'Union ou le droit d'un État membre qui constitue une mesure nécessaire et proportionnée dans une société démocratique pour garantir les objectifs visés à l'article 23, paragraphe 1, le responsable du traitement, afin de déterminer si le traitement à une autre fin est compatible avec la finalité pour laquelle les données à caractère personnel ont été initialement collectées, tient compte, entre autres: a) de l'existence éventuelle d'un lien entre les finalités pour lesquelles les données à caractère personnel ont été collectées et les finalités du traitement ultérieur envisagé; b) du contexte dans lequel les données à caractère personnel ont été collectées, en particulier en ce qui concerne la relation entre les personnes concernées et le responsable du traitement; c) de la nature des données à caractère personnel, en particulier si le traitement porte sur des catégories particulières de données à caractère personnel, en vertu de l'article 9, ou si des données à caractère personnel relatives à des condamnations pénales et à des infractions sont traitées, en vertu de l'article 10; d) des conséquences possibles du traitement ultérieur envisagé pour les personnes concernées; e) de l'existence de garanties appropriées, qui peuvent comprendre le chiffrement ou la pseudonymisation. »

RÉPONSE :  
Non, vous n'avez pas de obligation d'informer les personnes concernées lorsque vous achetez un fichier de prospects, car le traitement initial de ces données (la collecte) a été effectué par l'entreprise de départ, et le fait de les acheter ne constitue pas un traitement à une autre fin fondé sur une finalité autre que celle pour laquelle les données ont été collectées. Le RGPD ne prévoit pas une obligation d'information à la personne concernée dans ce cas, sauf si le traitement à une autre fin est fondé sur un consentement ou sur un droit légal, ce qui n'est pas le cas ici. Les passages trouvés ne traitent pas directement de la vente de fichiers de prospects ou de la communication à la personne concernée dans ce contexte. L'obligation d'information à la personne concernée est uniquement déclenchée par une demande formelle (articles 15 à 22) ou par une violation de données (article 34), et ne s'applique pas à la simple acquisition d'un fichier de prospects. Ainsi, aucune obligation d'information n'est engagée dans ce cas, et aucun délai n'est applicable.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données personnelles ; traitement ; consentement ; délai de notification ; finalité du traitement ; responsabilité du responsable du traitement

Temps : recherche 27.0 s · génération 48.8 s (2868 tokens lus, 1105 écrits, 33.8 tokens/s) · contrôle de pertinence 8.4 s · reformulation 3.1 s

## q34 — Puis-je installer des caméras dans l'atelier pour surveiller le travail de mes salariés ?

Article attendu : RGPD art. 88 — passage [2].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [2] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [3] RGPD — règlement (UE) 2016/679, article 2 : Champ d'application matériel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_2
  [4] RGPD — règlement (UE) 2016/679, article 47, paragraphe 2, points a) à k) : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
  [5] RGPD — règlement (UE) 2016/679, article 47, paragraphe 1 : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: … »  
- [2] « Les États membres peuvent prévoir, par la loi ou au moyen de conventions collectives, des règles plus spécifiques pour assurer la protection des droits et libertés en ce qui concerne le traitement des données à caractère personnel des employés dans le cadre des relations de travail, aux fins, notamment, du recrutement, de l'exécution du contrat de travail, y compris le respect des obligations fixées par la loi ou par des conventions collectives, de la gestion, de la planification et de l'organisation du travail, de l'égalité et de la diversité sur le lieu de travail, de la santé et de la sécurité au travail, de la protection des biens appartenant à l'employeur ou au client, aux fins de l'exercice et de la jouissance des droits et des avantages liés à l'emploi, individuellement ou collectivement, ainsi qu'aux fins de la résiliation de la relation de travail. »  
- [4] « Les règles d'entreprise contraignantes visées au paragraphe 1 précisent au moins: … les droits des personnes concernées à l'égard du traitement et les moyens d'exercer ces droits y compris le droit de ne pas faire l'objet de décisions fondées exclusivement sur un traitement automatisé, y compris le profilage, conformément à l'article 22, le droit d'introduire une réclamation auprès de l'autorité de contrôle compétente et devant les juridictions compétentes des États membres conformément à l'article 79 et d'obtenir réparation et, le cas échéant, une indemnisation pour violation des règles d'entreprise contraignantes; »  

RÉPONSE :  
Non, vous ne pouvez pas installer des caméras dans l'atelier pour surveiller le travail de vos salariés sans respecter des obligations spécifiques de transparence et de protection des données, notamment en ce qui concerne le traitement des données à caractère personnel. Le RGPD (article 22) interdit le traitement automatisé fondé sur un profilage sans consentement explicite ou sans base juridique appropriée, et les caméras peuvent constituer un traitement automatisé visant à surveiller les salariés, ce qui implique un risque de violation des droits fondamentaux. Le traitement de données relatives à l'activité de travail des salariés est soumis à des règles spécifiques (article 88), qui exigent une transparence, une protection de la dignité humaine et des droits fondamentaux, notamment le droit de ne pas faire l'objet de décisions fondées exclusivement sur un traitement automatisé. Ces droits doivent être clairement communiqués aux salariés, et les règles d'entreprise contraignantes (article 47) doivent prévoir les droits des personnes concernées, notamment le droit de s'opposer à ce traitement. Ainsi, l'installation de caméras nécessite une autorisation explicite, une communication claire des finalités du traitement, et une justification juridique solide, en lien avec les droits fondamentaux des salariés. [4]
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : enregistrement vidéo ; surveillance ; données personnelles ; traitement ; données d'identification ; activité professionnelle

Temps : recherche 29.3 s · génération 49.8 s (3876 tokens lus, 770 écrits, 31.8 tokens/s) · contrôle de pertinence 6.4 s · reformulation 3.1 s

## q35 — Notre fédération sportive peut-elle rédiger un guide de bonnes pratiques RGPD que ses clubs pourraient suivre officiellement ?

Article attendu : RGPD art. 40 — passage [4].

### Réponse du copilote

> Oui : notre fédération sportive peut rédiger un guide de bonnes pratiques RGPD que ses clubs pourraient suivre officiellement, car elle est une « association » représentant des catégories de responsables du traitement (article 40, paragraphe 2, [4]), et peut donc élaborer des codes de conduite pour préciser les modalités d'application du RGPD. Ce guide peut inclure des points comme le traitement loyal et transparent, la collecte des données, la pseudonymisation, l'exercice des droits des personnes concernées, ou la notification des violations. Les États membres et les autorités de contrôle encouragent cette démarche, notamment pour les micro, petites et moyennes entreprises, ce qui s'applique à une fédération sportive représentant des clubs [5]. Ce guide peut servir de référence pour les clubs, qui sont des responsables du traitement, en leur fournissant des directives conformes au RGPD [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « responsable du traitement», la personne physique ou morale, l'autorité publique, le service ou un autre organisme qui, seul ou conjointement avec d'autres, détermine les finalités et les moyens du traitement; lorsque les finalités et les moyens de ce traitement sont déterminés par le droit de l'Union ou le droit d'un État membre, le responsable du traitement peut être désigné ou les critères spécifiques applicables à sa désignation peuvent être prévus par le droit de l'Union ou par le droit d'un État membre; »
  [4] « Les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent élaborer des codes de conduite, les modifier ou les proroger, aux fins de préciser les modalités d'application du présent règlement, telles que: a) le traitement loyal et transparent; b) les intérêts légitimes poursuivis par les responsables du traitement dans des contextes spécifiques; c) la collecte des données à caractère personnel; d) la pseudonymisation des données à caractère personnel; e) les informations communiquées au public et aux personnes concernées; f) l'exercice des droits des personnes concernées; g) les informations communiquées aux enfants et la protection dont bénéficient les enfants et la manière d'obtenir le consentement des titulaires de la responsabilité parentale à l'égard de l'enfant; h) les mesures et les procédures visées aux articles 24 et 25 et les mesures visant à assurer la sécurité du traitement visées à l'article 32; i) la notification aux autorités de contrôle des violations de données à caractère personnel et la communication de ces violations aux personnes concernées; j) le transfert de données à caractère personnel vers des pays tiers ou à des organisations internationales; ou k) les procédures extrajudiciaires et autres procédures de règlement des litiges permettant de résoudre les litiges entre les responsables du traitement et les personnes concernées en ce qui concerne le traitement, sans préjudice des droits des personnes concernées au titre des articles 77 et 79. »
  [5] « Les États membres, les autorités de contrôle, le comité et la Commission encouragent l'élaboration de codes de conduite destinés à contribuer à la bonne application du présent règlement, compte tenu de la spécificité des différents secteurs de traitement et des besoins spécifiques des micro, petites et moyennes entreprises. »

Sources citées :
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 7 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [4] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [5] RGPD — règlement (UE) 2016/679, article 40, paragraphe 1 : Codes de conduite (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 24 : Responsabilité du responsable du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_24
  [2] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [3] «responsable du traitement», la personne physique ou morale, l'autorité publique, le service ou un autre organisme qui, seul ou conjointement avec d'autres, détermine les finalités et les moyens du traitement; lorsque les finalités et les moyens de ce traitement sont déterminés par le droit de l'Union ou le droit d'un État membre, le responsable du traitement peut être désigné ou les critères spécifiques applicables à sa désignation peuvent être prévus par le droit de l'Union ou par le droit d'un État membre;  
- [4] «Les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent élaborer des codes de conduite, les modifier ou les proroger, aux fins de préciser les modalités d'application du présent règlement, telles que: a) le traitement loyal et transparent; b) les intérêts légitimes poursuivis par les responsables du traitement dans des contextes spécifiques; c) la collecte des données à caractère personnel; d) la pseudonymisation des données à caractère personnel; e) les informations communiquées au public et aux personnes concernées; f) l'exercice des droits des personnes concernées; g) les informations communiquées aux enfants et la protection dont bénéficient les enfants et la manière d'obtenir le consentement des titulaires de la responsabilité parentale à l'égard de l'enfant; h) les mesures et les procédures visées aux articles 24 et 25 et les mesures visant à assurer la sécurité du traitement visées à l'article 32; i) la notification aux autorités de contrôle des violations de données à caractère personnel et la communication de ces violations aux personnes concernées; j) le transfert de données à caractère personnel vers des pays tiers ou à des organisations internationales; ou k) les procédures extrajudiciaires et autres procédures de règlement des litiges permettant de résoudre les litiges entre les responsables du traitement et les personnes concernées en ce qui concerne le traitement, sans préjudice des droits des personnes concernées au titre des articles 77 et 79.»  
- [5] «Les États membres, les autorités de contrôle, le comité et la Commission encouragent l'élaboration de codes de conduite destinés à contribuer à la bonne application du présent règlement, compte tenu de la spécificité des différents secteurs de traitement et des besoins spécifiques des micro, petites et moyennes entreprises.»

RÉPONSE :  
Oui : notre fédération sportive peut rédiger un guide de bonnes pratiques RGPD que ses clubs pourraient suivre officiellement, car elle est une « association » représentant des catégories de responsables du traitement (article 40, paragraphe 2, [4]), et peut donc élaborer des codes de conduite pour préciser les modalités d'application du RGPD. Ce guide peut inclure des points comme le traitement loyal et transparent, la collecte des données, la pseudonymisation, l'exercice des droits des personnes concernées, ou la notification des violations. Les États membres et les autorités de contrôle encouragent cette démarche, notamment pour les micro, petites et moyennes entreprises, ce qui s'applique à une fédération sportive représentant des clubs [5]. Ce guide peut servir de référence pour les clubs, qui sont des responsables du traitement, en leur fournissant des directives conformes au RGPD [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données personnelles ; traitements de données ; responsabilité du responsable du traitement ; finalité du traitement ; transparence ; consentement explicite

Temps : recherche 28.9 s · génération 39.0 s (2786 tokens lus, 814 écrits, 34.4 tokens/s) · contrôle de pertinence 7.3 s · reformulation 3.4 s

## q36 — Un ancien bénévole menace de se plaindre de nous auprès de la CNIL : en a-t-il le droit, et quels autres recours a-t-il ?

Article attendu : RGPD art. 77 — passage [2].

### Réponse du copilote

> Oui, un ancien bénévole a le droit de se plaindre de vous auprès de la CNIL, car il est une personne concernée et a le droit d'introduire une réclamation auprès d'une autorité de contrôle, notamment dans l'État membre où il a sa résidence habituelle, son lieu de travail ou le lieu où la violation aurait été commise [2]. Ce droit s'applique même s'il n'est plus bénévole, tant qu'il est concerné par le traitement de données à caractère personnel [2]. Il peut également exercer le droit d'obtenir réparation du dommage subi, si le traitement a causé un dommage matériel ou moral [4]. En outre, il peut mandater un organisme, organisation ou association à but non lucratif, actif dans le domaine de la protection des droits et libertés des personnes, pour qu'il introduise une réclamation en son nom [1]. Les autres recours incluent le droit d'introduire une réclamation auprès de l'autorité de contrôle compétente [1], et le droit d'obtenir réparation du préjudice subi [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit de mandater un organisme, une organisation ou une association à but non lucratif, qui a été valablement constitué conformément au droit d'un État membre, dont les objectifs statutaires sont d'intérêt public et est actif dans le domaine de la protection des droits et libertés des personnes concernées dans le cadre de la protection des données à caractère personnel les concernant, pour qu'il introduise une réclamation en son nom, exerce en son nom les droits visés aux articles 77, 78 et 79 et exerce en son nom le droit d'obtenir réparation visé à l'article 82 lorsque le droit d'un État membre le prévoit. »
  [1] « Les États membres peuvent prévoir que tout organisme, organisation ou association visé au paragraphe 1 du présent article, indépendamment de tout mandat confié par une personne concernée, a, dans l'État membre en question, le droit d'introduire une réclamation auprès de l'autorité de contrôle qui est compétente en vertu de l'article 77, et d'exercer les droits visés aux articles 78 et 79 s'il considère que les droits d'une personne concernée prévus dans le présent règlement ont été violés du fait du traitement. »
  [2] « Sans préjudice de tout autre recours administratif ou juridictionnel, toute personne concernée a le droit d'introduire une réclamation auprès d'une autorité de contrôle, en particulier dans l'État membre dans lequel se trouve sa résidence habituelle, son lieu de travail ou le lieu où la violation aurait été commise, si elle considère que le traitement de données à caractère personnel la concernant constitue une violation du présent règlement. »
  [4] « Toute personne ayant subi un dommage matériel ou moral du fait d'une violation du présent règlement a le droit d'obtenir du responsable du traitement ou du sous-traitant réparation du préjudice subi. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 80 : Représentation des personnes concernées (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_80
  [2] RGPD — règlement (UE) 2016/679, article 77 : Droit d'introduire une réclamation auprès d'une autorité de contrôle (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_77
  [4] RGPD — règlement (UE) 2016/679, article 82 : Droit à réparation et responsabilité (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_82
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [5] RGPD — règlement (UE) 2016/679, article 21 : Droit d'opposition
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_21

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « La personne concernée a le droit de mandater un organisme, une organisation ou une association à but non lucratif, qui a été valablement constitué conformément au droit d'un État membre, dont les objectifs statutaires sont d'intérêt public et est actif dans le domaine de la protection des droits et libertés des personnes concernées dans le cadre de la protection des données à caractère personnel les concernant, pour qu'il introduise une réclamation en son nom, exerce en son nom les droits visés aux articles 77, 78 et 79 et exerce en son nom le droit d'obtenir réparation visé à l'article 82 lorsque le droit d'un État membre le prévoit. »  
- [1] « Les États membres peuvent prévoir que tout organisme, organisation ou association visé au paragraphe 1 du présent article, indépendamment de tout mandat confié par une personne concernée, a, dans l'État membre en question, le droit d'introduire une réclamation auprès de l'autorité de contrôle qui est compétente en vertu de l'article 77, et d'exercer les droits visés aux articles 78 et 79 s'il considère que les droits d'une personne concernée prévus dans le présent règlement ont été violés du fait du traitement. »  
- [2] « Sans préjudice de tout autre recours administratif ou juridictionnel, toute personne concernée a le droit d'introduire une réclamation auprès d'une autorité de contrôle, en particulier dans l'État membre dans lequel se trouve sa résidence habituelle, son lieu de travail ou le lieu où la violation aurait été commise, si elle considère que le traitement de données à caractère personnel la concernant constitue une violation du présent règlement. »  
- [4] « Toute personne ayant subi un dommage matériel ou moral du fait d'une violation du présent règlement a le droit d'obtenir du responsable du traitement ou du sous-traitant réparation du préjudice subi. »  

RÉPONSE :  
Oui, un ancien bénévole a le droit de se plaindre de vous auprès de la CNIL, car il est une personne concernée et a le droit d'introduire une réclamation auprès d'une autorité de contrôle, notamment dans l'État membre où il a sa résidence habituelle, son lieu de travail ou le lieu où la violation aurait été commise [2]. Ce droit s'applique même s'il n'est plus bénévole, tant qu'il est concerné par le traitement de données à caractère personnel [2]. Il peut également exercer le droit d'obtenir réparation du dommage subi, si le traitement a causé un dommage matériel ou moral [4]. En outre, il peut mandater un organisme, organisation ou association à but non lucratif, actif dans le domaine de la protection des droits et libertés des personnes, pour qu'il introduise une réclamation en son nom [1]. Les autres recours incluent le droit d'introduire une réclamation auprès de l'autorité de contrôle compétente [1], et le droit d'obtenir réparation du préjudice subi [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit de porter plainte ; recours à la CNIL ; action en responsabilité civile ; demande de réparation ; recours judiciaire ; droit de réclamation

Temps : recherche 23.8 s · génération 44.1 s (3454 tokens lus, 738 écrits, 32.8 tokens/s) · contrôle de pertinence 6.7 s · reformulation 3.6 s

## q37 — Si une fuite de données cause un préjudice à un client, peut-il nous demander réparation ?

Article attendu : RGPD art. 82 — passage [3].

### Réponse du copilote

> Oui : si une fuite de données cause un préjudice à un client, ce client a le droit d'obtenir réparation du responsable du traitement ou du sous-traitant [3]. Cette obligation s'applique même lorsque plusieurs responsables participent au traitement, car chacun est tenu responsable du dommage dans sa totalité afin de garantir une réparation effective [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « Toute personne ayant subi un dommage matériel ou moral du fait d'une violation du présent règlement a le droit d'obtenir du responsable du traitement ou du sous-traitant réparation du préjudice subi. »
  [3] « Lorsque plusieurs responsables du traitement ou sous-traitants ou lorsque, à la fois, un responsable du traitement et un sous-traitant participent au même traitement et, lorsque, au titre des paragraphes 2 et 3, ils sont responsables d'un dommage causé par le traitement, chacun des responsables du traitement ou des sous-traitants est tenu responsable du dommage dans sa totalité afin de garantir à la personne concernée une réparation effective. »

Sources citées :
  [3] RGPD — règlement (UE) 2016/679, article 82 : Droit à réparation et responsabilité (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_82
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 34 : Communication à la personne concernée d'une violation de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_34
  [2] RGPD — règlement (UE) 2016/679, article 80 : Représentation des personnes concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_80
  [4] RGPD — règlement (UE) 2016/679, article 4, définition 1 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [5] RGPD — règlement (UE) 2016/679, article 4, définition 12 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [3] « Toute personne ayant subi un dommage matériel ou moral du fait d'une violation du présent règlement a le droit d'obtenir du responsable du traitement ou du sous-traitant réparation du préjudice subi. »
- [3] « Lorsque plusieurs responsables du traitement ou sous-traitants ou lorsque, à la fois, un responsable du traitement et un sous-traitant participent au même traitement et, lorsque, au titre des paragraphes 2 et 3, ils sont responsables d'un dommage causé par le traitement, chacun des responsables du traitement ou des sous-traitants est tenu responsable du dommage dans sa totalité afin de garantir à la personne concernée une réparation effective. »

RÉPONSE :
Oui : si une fuite de données cause un préjudice à un client, ce client a le droit d'obtenir réparation du responsable du traitement ou du sous-traitant [3]. Cette obligation s'applique même lorsque plusieurs responsables participent au traitement, car chacun est tenu responsable du dommage dans sa totalité afin de garantir une réparation effective [3].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données personnelles ; dommages-intérêts ; responsabilité civile ; préjudice ; demande de réparation ; obligation de confidentialité

Temps : recherche 29.3 s · génération 23.8 s (2896 tokens lus, 258 écrits, 34.9 tokens/s) · contrôle de pertinence 4.5 s · reformulation 3.4 s

## q38 — Notre club de sport peut-il demander un extrait de casier judiciaire aux bénévoles qui encadrent des enfants ?

Article attendu : RGPD art. 10 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [2] RGPD — règlement (UE) 2016/679, article 6, paragraphe 1 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
  [3] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
  [4] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [5] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [2] « Le traitement est nécessaire aux fins des intérêts légitimes poursuivis par le responsable du traitement ou par un tiers, à moins que ne prévalent les intérêts ou les libertés et droits fondamentaux de la personne concernée qui exigent une protection des données à caractère personnel, notamment lorsque la personne concernée est un enfant. »  
- [5] « les mesures et les procédures visées aux articles 24 et 25 et les mesures visant à assurer la sécurité du traitement visées à l'article 32; »  
- [1] « les finalités du traitement auquel sont destinées les données à caractère personnel ainsi que la base juridique du traitement; »  
- [4] « la personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: … »  

RÉPONSE :  
Non, le club de sport ne peut pas demander un extrait de casier judiciaire aux bénévoles qui encadrent des enfants, car le traitement de données à caractère personnel, notamment un extrait de casier judiciaire, relève d'une finalité qui, lorsqu'elle concerne un enfant, doit être justifiée par une base juridique appropriée et ne peut être fondée sur des intérêts légitimes sans que ne prévalent les intérêts ou les libertés et droits fondamentaux de l'enfant, notamment la protection de ses données personnelles [2]. Le RGPD impose une exigence de transparence et de légitimité dans le traitement des données, notamment pour les enfants, et ne permet pas de recueillir des données sensibles comme un casier judiciaire sans une base juridique fondée sur un intérêt légitime ou une finalité nécessaire, comme l'exécution d'un contrat ou la sauvegarde d'un intérêt vital [1]. De plus, le traitement de données sensibles, comme celles relatives à un casier judiciaire, est soumis à des règles spécifiques de protection, notamment pour les enfants, et ne peut être justifié sans une base juridique clairement établie [2]. Les bénévoles ne peuvent pas être tenus de fournir ce type de données, car le droit d'accès à ces données est limité par les principes de protection des données des enfants [4]. Les textes ne prévoient pas un traitement d'un casier judiciaire comme finalité licite pour un enfant, ni une base juridique adéquate pour ce traitement [2].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données personnelles ; traitement des données ; finalité du traitement ; consentement explicite ; données sensibles

Temps : recherche 24.9 s · génération 44.8 s (4118 tokens lus, 614 écrits, 31.6 tokens/s) · contrôle de pertinence 4.2 s · reformulation 3.3 s

## q39 — Si nous remplaçons les noms de nos adhérents par des numéros, les données sont-elles encore des données personnelles ?

Article attendu : RGPD art. 4, définition 5 — passage [5].

### Réponse du copilote

> Oui : les données sont encore des données personnelles si elles permettent d'identifier une personne physique, même par un numéro d'identification, car le RGPD considère comme «personne physique identifiable» une personne qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale [1]. La substitution d'un nom par un numéro ne supprime pas la nature personnelle des données, tant que ce numéro peut être lié à une personne physique identifiable.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « «données à caractère personnel», toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée»); est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 4, définition 1 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [3] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [4] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
  [5] RGPD — règlement (UE) 2016/679, article 4, définition 5 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « «données à caractère personnel», toute information se rapportant à une personne physique identifiée ou identifiable (ci-après dénommée «personne concernée»); est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale; »

RÉPONSE :
Oui : les données sont encore des données personnelles si elles permettent d'identifier une personne physique, même par un numéro d'identification, car le RGPD considère comme «personne physique identifiable» une personne qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale [1]. La substitution d'un nom par un numéro ne supprime pas la nature personnelle des données, tant que ce numéro peut être lié à une personne physique identifiable.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données personnelles ; identifiants ; informations personnelles ; données à caractère personnel ; données individuelles

Temps : recherche 22.4 s · génération 33.3 s (3703 tokens lus, 305 écrits, 32.8 tokens/s) · contrôle de pertinence 3.7 s · reformulation 3.1 s

## q40 — Nous allons utiliser un logiciel d'IA à haut risque qui attribue les tâches à nos salariés : devons-nous les prévenir avant de l'utiliser ?

Article attendu : AI Act art. 26 — passage [1].

### Réponse du copilote

> Oui : vous devez prévenir les salariés avant d’utiliser le logiciel d’IA à haut risque, car il est destiné à attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques personnelles, ce qui relève du domaine de l’emploi, de la gestion de la main-d’œuvre et de l’attribution de tâches visé à l’annexe III, point 4, b) [4]. Conformément à l’article 26, paragraphe 11, des déployeurs de systèmes d’IA à haut risque qui prennent des décisions ou facilitent les prises de décision concernant des personnes physiques, il est obligatoire d’informer ces personnes physiques qu’elles sont soumises à l’utilisation du système d’IA à haut risque [5]. Cette obligation s’applique également aux salariés concernés par l’attribution de tâches [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Avant de mettre en service ou d’utiliser un système d’IA à haut risque sur le lieu de travail, les déployeurs qui sont des employeurs informent les représentants des travailleurs et les travailleurs concernés qu’ils seront soumis à l’utilisation du système d’IA à haut risque. »
  [4] « Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des domaines suivants: 4. Emploi, gestion de la main-d'œuvre et accès à l'emploi indépendant: a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; b) systèmes d'IA destinés à être utilisés pour prendre des décisions influant sur les conditions des relations professionnelles, la promotion ou le licenciement dans le cadre de relations professionnelles contractuelles, pour attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques personnelles ou pour suivre et évaluer les performances et le comportement de personnes dans le cadre de telles relations. »
  [5] « Sans préjudice de l’article 50 du présent règlement, les déployeurs de systèmes d’IA à haut risque visés à l’annexe III, qui prennent des décisions ou facilitent les prises de décision concernant des personnes physiques, informent lesdites personnes physiques qu’elles sont soumises à l’utilisation du système d’IA à haut risque. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 7 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
  [4] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [5] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 11 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 1 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
  [3] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Avant de mettre en service ou d’utiliser un système d’IA à haut risque sur le lieu de travail, les déployeurs qui sont des employeurs informent les représentants des travailleurs et les travailleurs concernés qu’ils seront soumis à l’utilisation du système d’IA à haut risque. »
- [4] « Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des domaines suivants: 4. Emploi, gestion de la main-d'œuvre et accès à l'emploi indépendant: a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; b) systèmes d'IA destinés à être utilisés pour prendre des décisions influant sur les conditions des relations professionnelles, la promotion ou le licenciement dans le cadre de relations professionnelles contractuelles, pour attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques personnelles ou pour suivre et évaluer les performances et le comportement de personnes dans le cadre de telles relations. »
- [5] « Sans préjudice de l’article 50 du présent règlement, les déployeurs de systèmes d’IA à haut risque visés à l’annexe III, qui prennent des décisions ou facilitent les prises de décision concernant des personnes physiques, informent lesdites personnes physiques qu’elles sont soumises à l’utilisation du système d’IA à haut risque. »

RÉPONSE :
Oui : vous devez prévenir les salariés avant d’utiliser le logiciel d’IA à haut risque, car il est destiné à attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques personnelles, ce qui relève du domaine de l’emploi, de la gestion de la main-d’œuvre et de l’attribution de tâches visé à l’annexe III, point 4, b) [4]. Conformément à l’article 26, paragraphe 11, des déployeurs de systèmes d’IA à haut risque qui prennent des décisions ou facilitent les prises de décision concernant des personnes physiques, il est obligatoire d’informer ces personnes physiques qu’elles sont soumises à l’utilisation du système d’IA à haut risque [5]. Cette obligation s’applique également aux salariés concernés par l’attribution de tâches [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données d'IA ; traitement automatisé ; décision automatisée ; utilisation d'outils d'IA ; responsabilité des employeurs ; information préalable

Temps : recherche 28.5 s · génération 35.7 s (2939 tokens lus, 641 écrits, 34.3 tokens/s) · contrôle de pertinence 5.5 s · reformulation 3.4 s

## q41 — Notre organisme de formation peut-il utiliser une IA pour noter les examens de ses stagiaires ? Est-ce encadré ?

Article attendu : AI Act annexe III, point 3 — passage [2].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 4 : Maîtrise de l'IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_4
  [2] AI Act — règlement (UE) 2024/1689, annexe III, point 3 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [3] AI Act — règlement (UE) 2024/1689, article 59, paragraphe 1, points a) à i) : Traitement ultérieur de données à caractère personnel en vue du développement de certains systèmes d’IA dans l’intérêt public dans le cadre du bac à sable réglementaire de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_59
  [4] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [5] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [2] « systèmes d'IA destinés à être utilisés pour surveiller et détecter des comportements interdits chez les étudiants lors d'examens dans le contexte d'établissements d'enseignement et de formation ou en leur sein à tous les niveaux; »  
- [5] « Pour les systèmes d’IA à haut risque visés à l’annexe III, point 1 a), les mesures prévues au paragraphe 3 du présent article sont de nature à garantir que, en outre, aucune mesure ou décision n’est prise par le déployeur sur la base de l’identification résultant du système sans vérification et confirmation distinctes de cette identification par au moins deux personnes physiques disposant des compétences, de la formation et de l’autorité nécessaires. »  
- [5] « L’exigence d’une vérification distincte par au moins deux personnes physiques ne s’applique pas aux systèmes d’IA à haut risque utilisés à des fins répressives ou dans les domaines de la migration, des contrôles aux frontières ou de l’asile, lorsque le droit de l’Union ou le droit national considère que l’application de cette exigence est disproportionnée. »

RÉPONSE :  
Oui, l’organisme de formation peut utiliser une IA pour noter les examens de ses stagiaires, car ce type d’utilisation relève du domaine de l’éducation et de la formation professionnelle, comme prévus à l’article 6, paragraphe 2, de l’AI Act (annexe III, point 3a). Cependant, ce système d’IA est considéré comme un système d’IA à haut risque, et donc est encadré par l’AI Act. En particulier, pour les systèmes d’IA à haut risque visés à l’annexe III, point 1 a), il est exigé que toute décision fondée sur l’identification du système soit vérifiée et confirmée par au moins deux personnes physiques disposant des compétences, de la formation et de l’autorité nécessaires. Cette exigence s’applique sauf dans les domaines de la migration, des contrôles aux frontières ou de l’asile, où elle peut être considérée comme disproportionnée par le droit de l’Union ou national. Dans le cas d’un examen de formation, cette exigence s’applique, sauf si le droit national considère que son application est disproportionnée.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données personnelles ; traitements automatisés ; finalité du traitement ; responsabilité du responsable ; transparence du traitement

Temps : recherche 29.3 s · génération 46.6 s (4192 tokens lus, 568 écrits, 31.5 tokens/s) · contrôle de pertinence 5.4 s · reformulation 3.3 s

## q42 — Un candidat refusé après l'analyse de sa candidature par un outil d'IA à haut risque nous demande pourquoi : devons-nous lui expliquer ?

Article attendu : AI Act art. 86 — passage [1].

### Réponse du copilote

> Oui : vous devez lui expliquer, car le candidat est concerné par une décision prise par un déployeur sur la base d’un système d’IA à haut risque visé à l’annexe III, notamment dans le domaine du recrutement ou de la sélection de personnes physiques [1][2]. Ce droit s’applique lorsque la décision a des effets juridiques ou affecte significativement le candidat de façon qu’il considère comme ayant des conséquences négatives sur sa santé, sa sécurité ou ses droits fondamentaux [1]. Cependant, ce droit ne s’applique pas si les exceptions ou restrictions prévues par le droit de l’Union ou le droit national empêchent l’obligation d’explication [1]. Le fait que le système d’IA soit utilisé pour analyser et évaluer les candidatures relève du domaine énuméré à l’annexe III [2], et donc du champ d’application de l’article 86 de l’AI Act [1]. La condition d’application de l’obligation d’explication est remplie lorsque le système d’IA produit des effets juridiques ou affecte significativement le candidat [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Toute personne concernée faisant l’objet d’une décision prise par un déployeur sur la base des sorties d’un système d’IA à haut risque mentionné à l’annexe III, à l’exception des systèmes énumérés au point 2 de ladite annexe, et qui produit des effets juridiques ou affecte significativement cette personne de façon similaire d’une manière qu’elle considère comme ayant des conséquences négatives sur sa santé, sa sécurité ou ses droits fondamentaux a le droit d’obtenir du déployeur des explications claires et pertinentes sur le rôle du système d’IA dans la procédure décisionnelle et sur les principaux éléments de la décision prise. »
  [2] « a) systèmes d’IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »
  [4] « Le premier alinéa s’applique lorsqu’une des conditions suivantes est remplie: »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 86 : Droit à l’explication des décisions individuelles (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_86
  [2] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [4] AI Act — règlement (UE) 2024/1689, article 6, paragraphe 3 : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, annexe III, point 8 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [5] AI Act — règlement (UE) 2024/1689, article 6, paragraphe 1 : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Toute personne concernée faisant l’objet d’une décision prise par un déployeur sur la base des sorties d’un système d’IA à haut risque mentionné à l’annexe III, à l’exception des systèmes énumérés au point 2 de ladite annexe, et qui produit des effets juridiques ou affecte significativement cette personne de façon similaire d’une manière qu’elle considère comme ayant des conséquences négatives sur sa santé, sa sécurité ou ses droits fondamentaux a le droit d’obtenir du déployeur des explications claires et pertinentes sur le rôle du système d’IA dans la procédure décisionnelle et sur les principaux éléments de la décision prise. »
- [2] « a) systèmes d’IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »
- [4] « Le premier alinéa s’applique lorsqu’une des conditions suivantes est remplie: »

RÉPONSE :
Oui : vous devez lui expliquer, car le candidat est concerné par une décision prise par un déployeur sur la base d’un système d’IA à haut risque visé à l’annexe III, notamment dans le domaine du recrutement ou de la sélection de personnes physiques [1][2]. Ce droit s’applique lorsque la décision a des effets juridiques ou affecte significativement le candidat de façon qu’il considère comme ayant des conséquences négatives sur sa santé, sa sécurité ou ses droits fondamentaux [1]. Cependant, ce droit ne s’applique pas si les exceptions ou restrictions prévues par le droit de l’Union ou le droit national empêchent l’obligation d’explication [1]. Le fait que le système d’IA soit utilisé pour analyser et évaluer les candidatures relève du domaine énuméré à l’annexe III [2], et donc du champ d’application de l’article 86 de l’AI Act [1]. La condition d’application de l’obligation d’explication est remplie lorsque le système d’IA produit des effets juridiques ou affecte significativement le candidat [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : justificatif de décision ; données personnelles ; traitement automatisé ; décision algorithmique ; motif d'exclusion ; droit à l'explication

Temps : recherche 26.3 s · génération 29.1 s (2588 tokens lus, 542 écrits, 35.1 tokens/s) · contrôle de pertinence 4.6 s · reformulation 3.3 s

## q43 — Le règlement européen sur l'IA prévoit-il des mesures particulières pour les PME ?

Article attendu : AI Act art. 62 — passage [1].

### Réponse du copilote

> Oui : le règlement européen sur l'IA prévoit des mesures particulières pour les PME. Les États membres accordent aux PME, y compris les jeunes pousses, un accès prioritaire aux bacs à sable réglementaires de l’IA, dans la mesure où elles remplissent les conditions d’éligibilité et les critères de sélection [1]. Ils organisent des activités spécifiques de sensibilisation et de formation adaptées aux besoins des PME [1]. Ils utilisent des canaux privilégiés pour fournir des conseils et répondre à leurs questions [1]. Ils facilitent la participation des PME au processus d’élaboration de la normalisation [1]. Les PME peuvent se conformer de manière simplifiée à certains éléments du système de gestion de la qualité, avec des lignes directrices spécifiques tenant compte de leurs besoins [2]. Les sanctions sont ajustées en tenant compte des intérêts des PME et de leur viabilité économique [3]. La Commission soutient les PME dans l’application de l’obligation de maîtrise de l’IA, en publiant des exemples pratiques sur sa plateforme d’information unique [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les États membres: a) accordent aux PME, y compris les jeunes pousses, qui ont leur siège social ou une succursale dans l’Union, un accès prioritaire aux bacs à sable réglementaires de l’IA, dans la mesure où elles remplissent les conditions d’éligibilité et les critères de sélection; l’accès prioritaire n’empêche pas d’autres PME, y compris les jeunes pousses, autres que celles visées au présent alinéa, d’accéder au bac à sable réglementaire de l’IA, pour autant qu’elles remplissent également les conditions d’éligibilité et les critères de sélection; »
  [1] « b) organisent des activités spécifiques de sensibilisation et de formation à l’application du présent règlement, adaptées aux besoins des PME, y compris les jeunes pousses, les déployeurs et, si nécessaire, les pouvoirs publics locaux; »
  [1] « c) utilisent des canaux privilégiés existants et, s’il y a lieu, en établissent de nouveaux avec les PME, y compris les jeunes pousses, les déployeurs, d’autres innovateurs et, si nécessaire, les pouvoirs publics locaux, afin de fournir des conseils et de répondre aux questions relatives à la mise en œuvre du présent règlement, y compris en ce qui concerne la participation à des bacs à sable réglementaires de l’IA; »
  [1] « d) facilitent la participation des PME et d’autres parties concernées au processus d’élaboration de la normalisation. »
  [2] « Les PME, y compris les jeunes pousses, peuvent se conformer de manière simplifiée à certains éléments du système de gestion de la qualité requis par l'article 17, pour autant qu'elles n'aient pas d'entreprises partenaires ou d'entreprises liées au sens de la recommandation 2003/361/CE. À cette fin, la Commission élabore des lignes directrices sur les éléments du système de gestion de la qualité qui peuvent être respectés de manière simplifiée en tenant compte des besoins des PME, sans affecter le niveau de protection ni la nécessité de se conformer aux exigences relatives aux systèmes d'IA à haut risque. »
  [3] « Lorsqu'ils imposent des sanctions, les États membres tiennent compte des intérêts des PME, y compris les jeunes pousses, et des petites entreprises à moyenne capitalisation, ainsi que de leur viabilité économique. »
  [4] « La Commission et les États membres soutiennent et facilitent les efforts déployés par les fournisseurs et les déployeurs de systèmes d'IA, en particulier les PME, pour s'acquitter de l'obligation qui leur incombe en vertu du paragraphe 1 du présent article. À cette fin, la Commission publie des exemples pratiques sur la manière de respecter cette obligation sur la plateforme d'information unique visée à l’article 62, paragraphe 3, point b). »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 62 : Mesures en faveur des fournisseurs et déployeurs, en particulier les PME, y compris les jeunes pousses (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_62
  [2] AI Act — règlement (UE) 2024/1689, article 63 : Dérogations pour des opérateurs spécifiques (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_63
  [3] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 1 : Sanctions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [4] AI Act — règlement (UE) 2024/1689, article 4 : Maîtrise de l'IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_4
Passages consultés mais non cités :
  [5] AI Act — règlement (UE) 2024/1689, article 70, paragraphe 8 : Désignation des autorités nationales compétentes et des points de contact uniques
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_70

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les États membres: a) accordent aux PME, y compris les jeunes pousses, qui ont leur siège social ou une succursale dans l’Union, un accès prioritaire aux bacs à sable réglementaires de l’IA, dans la mesure où elles remplissent les conditions d’éligibilité et les critères de sélection; l’accès prioritaire n’empêche pas d’autres PME, y compris les jeunes pousses, autres que celles visées au présent alinéa, d’accéder au bac à sable réglementaire de l’IA, pour autant qu’elles remplissent également les conditions d’éligibilité et les critères de sélection; »
- [1] « b) organisent des activités spécifiques de sensibilisation et de formation à l’application du présent règlement, adaptées aux besoins des PME, y compris les jeunes pousses, les déployeurs et, si nécessaire, les pouvoirs publics locaux; »
- [1] « c) utilisent des canaux privilégiés existants et, s’il y a lieu, en établissent de nouveaux avec les PME, y compris les jeunes pousses, les déployeurs, d’autres innovateurs et, si nécessaire, les pouvoirs publics locaux, afin de fournir des conseils et de répondre aux questions relatives à la mise en œuvre du présent règlement, y compris en ce qui concerne la participation à des bacs à sable réglementaires de l’IA; »
- [1] « d) facilitent la participation des PME et d’autres parties concernées au processus d’élaboration de la normalisation. »
- [2] « Les PME, y compris les jeunes pousses, peuvent se conformer de manière simplifiée à certains éléments du système de gestion de la qualité requis par l'article 17, pour autant qu'elles n'aient pas d'entreprises partenaires ou d'entreprises liées au sens de la recommandation 2003/361/CE. À cette fin, la Commission élabore des lignes directrices sur les éléments du système de gestion de la qualité qui peuvent être respectés de manière simplifiée en tenant compte des besoins des PME, sans affecter le niveau de protection ni la nécessité de se conformer aux exigences relatives aux systèmes d'IA à haut risque. »
- [3] « Lorsqu'ils imposent des sanctions, les États membres tiennent compte des intérêts des PME, y compris les jeunes pousses, et des petites entreprises à moyenne capitalisation, ainsi que de leur viabilité économique. »
- [4] « La Commission et les États membres soutiennent et facilitent les efforts déployés par les fournisseurs et les déployeurs de systèmes d'IA, en particulier les PME, pour s'acquitter de l'obligation qui leur incombe en vertu du paragraphe 1 du présent article. À cette fin, la Commission publie des exemples pratiques sur la manière de respecter cette obligation sur la plateforme d'information unique visée à l’article 62, paragraphe 3, point b). »

RÉPONSE :
Oui : le règlement européen sur l'IA prévoit des mesures particulières pour les PME. Les États membres accordent aux PME, y compris les jeunes pousses, un accès prioritaire aux bacs à sable réglementaires de l’IA, dans la mesure où elles remplissent les conditions d’éligibilité et les critères de sélection [1]. Ils organisent des activités spécifiques de sensibilisation et de formation adaptées aux besoins des PME [1]. Ils utilisent des canaux privilégiés pour fournir des conseils et répondre à leurs questions [1]. Ils facilitent la participation des PME au processus d’élaboration de la normalisation [1]. Les PME peuvent se conformer de manière simplifiée à certains éléments du système de gestion de la qualité, avec des lignes directrices spécifiques tenant compte de leurs besoins [2]. Les sanctions sont ajustées en tenant compte des intérêts des PME et de leur viabilité économique [3]. La Commission soutient les PME dans l’application de l’obligation de maîtrise de l’IA, en publiant des exemples pratiques sur sa plateforme d’information unique [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : mesures adaptées ; obligations spécifiques ; conditions de mise en œuvre ; exigences simplifiées ; accompagnement ; responsabilités proportionnelles

Temps : recherche 28.5 s · génération 48.1 s (3058 tokens lus, 1025 écrits, 33.4 tokens/s) · contrôle de pertinence 7.7 s · reformulation 3.3 s

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
  [3] AI Act — règlement (UE) 2024/1689, article 6, paragraphe 5 : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
  [4] AI Act — règlement (UE) 2024/1689, article 16 : Obligations incombant aux fournisseurs de systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_16
  [5] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Au plus tard le 2 août 2027, la Commission adopte des actes délégués conformément à l'article 97 afin de compléter le présent règlement afin de préciser les systèmes d'IA à haut risque concernés, les exigences ou obligations qui peuvent être limitées, les conditions dans lesquelles cette limitation s'applique et la portée de la limitation. »
- [5] « Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des domaines suivants: 4. Emploi, gestion de la main-d'œuvre et accès à l'emploi indépendant: a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »

RÉPONSE :
Les obligations sur les systèmes d'IA à haut risque utilisés pour le recrutement s'appliquent à partir de la date de l'adoption des actes délégués par la Commission, prévus au plus tard le 2 août 2027 [1]. Ces obligations s'appliquent aux systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats [5].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : systèmes d'IA à haut risque ; recrutement ; obligation de transparence ; évaluation des risques ; mise en œuvre ; mise en conformité

Temps : recherche 25.3 s · génération 26.2 s (2844 tokens lus, 373 écrits, 34.7 tokens/s) · contrôle de pertinence 4.9 s · reformulation 3.5 s

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
  [2] RGPD — règlement (UE) 2016/679, article 47, paragraphe 2, points a) à k) : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
  [3] RGPD — règlement (UE) 2016/679, article 47, paragraphe 1 : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
  [4] AI Act — règlement (UE) 2024/1689, annexe V : Déclaration UE de conformité
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_V
  [5] RGPD — règlement (UE) 2016/679, article 12, paragraphe 7 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun  
RÉPONSE : Les textes trouvés ne traitent pas de ce point.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : numéro de facture ; date de émission ; nom et adresse du vendeur ; nom et adresse du client ; montant total ; mention de la taxe applicable

Temps : recherche 27.5 s · génération 19.2 s (3100 tokens lus, 26 écrits, 35.8 tokens/s) · reformulation 3.3 s

## h07 — Comment demander une subvention à la mairie pour notre association ?

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
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [3] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [4] RGPD — règlement (UE) 2016/679, article 12, paragraphe 5 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [5] RGPD — règlement (UE) 2016/679, article 60, paragraphe 8 : Coopération entre l'autorité de contrôle chef de file et les autres autorités de contrôle concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_60

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun  
RÉPONSE : Les textes trouvés ne traitent pas de votre question.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : demande de subvention ; projet de financement ; justificatif de besoin ; dossier de candidature ; programme de soutien ; objectif de l'association

Temps : recherche 21.0 s · génération 11.5 s (2232 tokens lus, 26 écrits, 38.5 tokens/s) · reformulation 3.4 s

## h08 — Quelles sont les règles pour embaucher un apprenti dans une PME ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [2] RGPD — règlement (UE) 2016/679, article 4, définition 7 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [3] RGPD — règlement (UE) 2016/679, article 24 : Responsabilité du responsable du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_24
  [4] RGPD — règlement (UE) 2016/679, article 47, paragraphe 2, points a) à k) : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
  [5] RGPD — règlement (UE) 2016/679, article 47, paragraphe 1 : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
aucun

RÉPONSE :  
Les textes trouvés ne traitent pas directement de la question de l'embauche d'un apprenti dans une PME. Bien que le RGPD aborde la protection des données des employés dans le cadre des relations de travail (article 88), il ne précise pas les règles spécifiques applicables à l'embauche d'un apprenti. Aucun passage ne mentionne les conditions d'embauche d'un apprenti, ni les obligations spécifiques pour une PME dans ce contexte.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données biométriques ; contrat de travail ; formation professionnelle ; âge minimum ; conditions d'emploi ; droit du travail

Temps : recherche 27.6 s · génération 23.6 s (3275 tokens lus, 130 écrits, 34.3 tokens/s) · reformulation 3.1 s
