# Réponses du copilote — exam2_remote_3

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 27/11/2026 à 15:06 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen/qwen3.8-27b` via l'API compatible OpenAI https://api.groq.com/openai/v1 (expérience de la séance 7, questions de test seulement ; modèle tel que servi par l'API à la date ci-dessus) — température 0.1, raisonnement : réglage par défaut du modèle, passages calculés pour un contexte de 8192 tokens comme en local, 2000 tokens au plus par réponse (raisonnement compris) ; le juge est le même modèle
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu, reranker `BAAI/bge-reranker-v2-m3` sur CPU (20 candidats reclassés avant la limite par article), reformulation de la question par le modèle avant la recherche (termes juridiques ajoutés, sans conclusion)
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_exam2.jsonl` (24 + 4 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| e01 | Je veux installer des caméras dans mon magasin et dans la salle de pause. J'en ai le droit ? Qu'est-ce que je dois dire à mes salariés ? | 5/6 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 46 s |
| e02 | Une ancienne cliente me demande d'effacer toutes ses données. On doit garder ses factures pour la comptabilité. Je dois quand même tout supprimer ? | 4/4 | non | La réponse ne reprend que 4 des 6 cas énumérés au passage [2], sans dire qu'elle n'en cite qu'une partie. Vérifiez la liste complète. | 34 s |
| e03 | Combien de temps je peux garder les CV des candidats que je n'ai pas retenus ? | 3/3 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 35 s |
| e04 | Notre association garde la liste des bénévoles (adresses, téléphones) dans un fichier Excel partagé sur Google Drive. C'est un problème ? | 6/6 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 32 s |
| e05 | Sur mon site web, j'utilise seulement Google Analytics. Je suis obligé de mettre un bandeau cookies ? | 0/0 | oui | — | 27 s |
| e06 | La boîte mail de l'accueil a été piratée hier. Qu'est-ce que je dois faire ? Je dois prévenir quelqu'un ? | 6/6 | non | La réponse met entre « » un texte introuvable dans les extraits vérifiés : « communique[r] la violation de données à caractère personnel à la personne concernée dans les meilleurs délais » (et 2 autre(s)).; La réponse ne reprend que 2 des 3 cas énumérés au passage [2], sans dire qu'elle n'en cite qu'une partie. Vérifiez la liste complète. | 35 s |
| e07 | Un prestataire extérieur gère notre paie. Je dois signer un contrat spécial avec lui pour les données ? | 6/6 | non | — | 28 s |
| e08 | Je peux envoyer notre newsletter à mes anciens clients sans leur demander leur accord ? | 6/6 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 33 s |
| e09 | Un salarié me demande une copie de toutes les données que j'ai sur lui, même les mails où on parle de lui. Je dois tout lui donner ? J'ai combien de temps pour répondre ? | 6/6 | non | — | 31 s |
| e10 | Un salarié est parti de l'entreprise. Je peux encore lire sa boîte mail professionnelle ? | 0/0 | oui | — | 27 s |
| e11 | Dans notre organisme de formation, on demande aux stagiaires leur numéro de sécurité sociale et des informations sur leur handicap. On a le droit ? | 5/5 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 33 s |
| e12 | Je peux suivre les véhicules de mes techniciens par GPS ? | 6/6 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 30 s |
| e13 | On veut publier sur Facebook des photos des bénévoles prises pendant notre fête annuelle. Il faut leur accord écrit ? | 4/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 28 s |
| e14 | On a 8 salariés. On doit tenir un registre des traitements et nommer un DPO ? | 3/3 | non | — | 32 s |
| e15 | Notre logiciel de gestion des clients est hébergé aux États-Unis. C'est autorisé ? | 6/6 | non | La réponse ne reprend que 1 des 7 cas énumérés au passage [5], sans dire qu'elle n'en cite qu'une partie. Vérifiez la liste complète. | 30 s |
| e16 | On ne crée pas d'IA, on utilise juste des outils comme ChatGPT. Est-ce que l'AI Act nous concerne quand même ? | 6/6 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 33 s |
| e17 | Je voudrais utiliser un logiciel d'IA qui trie automatiquement les CV. C'est interdit ? Sinon, quelles règles je dois respecter ? | 6/6 | non | La réponse cite [1], [2] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations. | 34 s |
| e18 | On a mis un chatbot sur notre site. On doit dire aux visiteurs qu'ils parlent avec une machine ? | 1/1 | non | La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à moins que cela ne soit déjà évident pour eux [1] ». Vérifiez-la dans les textes.; La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui, vous devez informer les visiteurs qu'ils interagissent avec un système d'IA, à moins que cela ne soit déjà évident … » (et 1 autre(s)). Vérifiez qui est concerné. | 36 s |
| e19 | Notre organisme de formation veut utiliser une IA pour corriger les examens et noter les stagiaires. C'est risqué ? | 6/6 | non | — | 34 s |
| e20 | On m'a dit que je dois former mes salariés à l'IA. C'est vraiment obligatoire ? | 5/5 | non | — | 33 s |
| e21 | On crée nos visuels pour les réseaux sociaux avec une IA. Il faut écrire qu'ils sont générés par IA ? | 4/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 31 s |
| e22 | Un fournisseur nous propose un outil qui analyse les émotions des salariés pendant les visioconférences. On a le droit de l'utiliser ? | 5/5 | non | — | 35 s |
| e23 | Si l'outil d'IA qu'on a acheté se trompe et écarte injustement un candidat, qui est responsable : moi ou le fournisseur ? | 6/6 | non | La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Les passages trouvés ne traitent pas directement de votre question concernant la responsabilité pour un préjudice causé … » (et 1 autre(s)). Vérifiez qui est concerné. | 29 s |
| e24 | À partir de quand les règles de l'AI Act s'appliquent vraiment ? Qu'est-ce qui est déjà en vigueur ? | 6/6 | non | — | 29 s |
| e25 | Mes salariés copient des données clients dans ChatGPT pour aller plus vite. C'est un problème ? Comment je peux encadrer ça ? | 6/6 | non | — | 33 s |
| he01 | Comment je déclare la TVA chaque trimestre ? | 0/0 | oui | — | 28 s |
| he02 | Si un salarié en CDI démissionne, combien de temps dure son préavis ? | 0/0 | oui | — | 30 s |
| he03 | Tu as des idées pour organiser une fête de fin d'année pour les bénévoles avec un petit budget ? | 0/0 | oui | — | 26 s |

## e01 — Je veux installer des caméras dans mon magasin et dans la salle de pause. J'en ai le droit ? Qu'est-ce que je dois dire à mes salariés ?

Article attendu : RGPD art. 6, paragraphe 1 ou RGPD art. 13 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [2] RGPD — règlement (UE) 2016/679, article 35, paragraphe 9 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [3] RGPD — règlement (UE) 2016/679, article 35, paragraphe 1 : Analyse d'impact relative à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_35
  [4] RGPD — règlement (UE) 2016/679, article 12, paragraphe 2 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [5] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

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
- [3] « Lorsqu'un type de traitement, en particulier par le recours à de nouvelles technologies, et compte tenu de la nature, de la portée, du contexte et des finalités du traitement, est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques, le responsable du traitement effectue, avant le traitement, une analyse de l'impact des opérations de traitement envisagées sur la protection des données à caractère personnel. »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question concernant le droit d'installer des caméras ou les interdictions spécifiques liées aux salles de pause. Ils précisent uniquement les obligations d'information et d'analyse d'impact qui s'appliquent si vous traitez des données personnelles.

En tant que responsable du traitement, vous devez fournir aux personnes concernées (vos salariés) des informations sur le traitement de leurs données [1]. Ces informations doivent inclure « les finalités du traitement » [1], « les catégories de données à caractère personnel concernées » [1], « les destinataires ou catégories de destinataires auxquels les données à caractère personnel ont été ou seront communiquées » [1], ainsi que « la durée de conservation des données à caractère personnel envisagée ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée » [1].

De plus, si l'installation de caméras est « susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques », vous devez effectuer « avant le traitement, une analyse de l'impact des opérations de traitement envisagées sur la protection des données à caractère personnel » [3].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : vidéosurveillance ; information des personnes concernées ; registre des traitements ; consultation des représentants du personnel ; finalité du traitement ; durée de conservation

Temps : recherche 44.0 s · génération 1.5 s (2344 tokens lus, 540 écrits, 456.9 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.2 s · attente des limites de l'API 30 s (non comptée)

## e02 — Une ancienne cliente me demande d'effacer toutes ses données. On doit garder ses factures pour la comptabilité. Je dois quand même tout supprimer ?

Article attendu : RGPD art. 17 — passage [2].

### Réponse du copilote

> Non, vous n'êtes pas obligé de supprimer toutes les données si leur conservation est requise par la loi. Le RGPD, article 17, paragraphe 1, impose au responsable du traitement l'obligation d'effacer les données « dans les meilleurs délais » lorsque, par exemple, « les données à caractère personnel ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées d'une autre manière » [2]. Cependant, ce droit à l'effacement ne s'applique pas « dans la mesure où ce traitement est nécessaire » pour « respecter une obligation légale qui requiert le traitement prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis » [2]. Si la conservation de vos factures est une obligation légale de comptabilité, vous pouvez donc conserver ces données spécifiques malgré la demande de l'ancienne cliente [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « La personne concernée a le droit d'obtenir du responsable du traitement l'effacement, dans les meilleurs délais, de données à caractère personnel la concernant et le responsable du traitement a l'obligation d'effacer ces données à caractère personnel dans les meilleurs délais, lorsque l'un des motifs suivants s'applique: »
  [2] « Les paragraphes 1 et 2 ne s'appliquent pas dans la mesure où ce traitement est nécessaire: »
  [2] « b) pour respecter une obligation légale qui requiert le traitement prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis, ou pour exécuter une mission d'intérêt public ou relevant de l'exercice de l'autorité publique dont est investi le responsable du traitement; »
  [2] « a) les données à caractère personnel ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées d'une autre manière; »

Sources citées :
  [2] RGPD — règlement (UE) 2016/679, article 17 : Droit à l'effacement («droit à l'oubli») (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_17
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 18 : Droit à la limitation du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_18
  [3] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [4] RGPD — règlement (UE) 2016/679, article 19 : Obligation de notification en ce qui concerne la rectification ou l'effacement de données à caractère personnel ou la limitation du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_19
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
Attention : La réponse ne reprend que 4 des 6 cas énumérés au passage [2], sans dire qu'elle n'en cite qu'une partie. Vérifiez la liste complète.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [2] « La personne concernée a le droit d'obtenir du responsable du traitement l'effacement, dans les meilleurs délais, de données à caractère personnel la concernant et le responsable du traitement a l'obligation d'effacer ces données à caractère personnel dans les meilleurs délais, lorsque l'un des motifs suivants s'applique: »
- [2] « Les paragraphes 1 et 2 ne s'appliquent pas dans la mesure où ce traitement est nécessaire: »
- [2] « b) pour respecter une obligation légale qui requiert le traitement prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis, ou pour exécuter une mission d'intérêt public ou relevant de l'exercice de l'autorité publique dont est investi le responsable du traitement; »
- [2] « a) les données à caractère personnel ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées d'une autre manière; »

RÉPONSE :
Non, vous n'êtes pas obligé de supprimer toutes les données si leur conservation est requise par la loi. Le RGPD, article 17, paragraphe 1, impose au responsable du traitement l'obligation d'effacer les données « dans les meilleurs délais » lorsque, par exemple, « les données à caractère personnel ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées d'une autre manière » [2]. Cependant, ce droit à l'effacement ne s'applique pas « dans la mesure où ce traitement est nécessaire » pour « respecter une obligation légale qui requiert le traitement prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis » [2]. Si la conservation de vos factures est une obligation légale de comptabilité, vous pouvez donc conserver ces données spécifiques malgré la demande de l'ancienne cliente [2].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit à l'effacement ; exception ; conservation des données ; limitation du traitement

Temps : recherche 32.1 s · génération 1.3 s (3475 tokens lus, 424 écrits, 471.9 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.4 s · attente des limites de l'API 4 s (non comptée)

## e03 — Combien de temps je peux garder les CV des candidats que je n'ai pas retenus ?

Article attendu : RGPD art. 5 — passage [1].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
  [2] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [3] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [4] RGPD — règlement (UE) 2016/679, article 9, paragraphe 2, points a) à i) : Traitement portant sur des catégories particulières de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
  [5] RGPD — règlement (UE) 2016/679, article 9, paragraphe 1 : Traitement portant sur des catégories particulières de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées »
- [1] « les données à caractère personnel peuvent être conservées pour des durées plus longues dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, pour autant que soient mises en œuvre les mesures techniques et organisationnelles appropriées requises par le présent règlement afin de garantir les droits et libertés de la personne concernée »
- [2] « la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée »

RÉPONSE :
Vous devez conserver les CV des candidats non retenus pendant une durée « n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées » [1]. Les passages trouvés ne traitent pas directement de votre question en ce qu'ils ne précisent pas de durée concrète (en jours ou en mois) applicable spécifiquement aux CV de recrutement ; cette règle relève du principe général de limitation de la conservation du RGPD [1]. Vous devez informer les candidats de « la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée » [2]. Les règles concrètes (durées précises) peuvent venir d'autres textes, comme le droit national ou les recommandations de la CNIL.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : durée de conservation des données à caractère personnel ; données relatives aux candidats ; registre des traitements ; finalité du traitement

Temps : recherche 31.8 s · génération 1.2 s (3829 tokens lus, 348 écrits, 545.5 tokens/s) · contrôle de pertinence 1.8 s · reformulation 0.3 s

## e04 — Notre association garde la liste des bénévoles (adresses, téléphones) dans un fichier Excel partagé sur Google Drive. C'est un problème ?

Article attendu : RGPD art. 32 ou RGPD art. 28, paragraphe 1 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 24 : Responsabilité du responsable du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_24
  [2] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [3] RGPD — règlement (UE) 2016/679, article 40, paragraphe 1 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [4] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [5] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « le responsable du traitement met en œuvre des mesures techniques et organisationnelles appropriées pour s'assurer et être en mesure de démontrer que le traitement est effectué conformément au présent règlement. »
- [1] « Ces mesures sont réexaminées et actualisées si nécessaire. »
- [5] « Les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10. »
- [4] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: »
- [4] « le droit d'introduire une réclamation auprès d'une autorité de contrôle; »
- [3] « Les États membres, les autorités de contrôle, le comité et la Commission encouragent l'élaboration de codes de conduite destinés à contribuer à la bonne application du présent règlement, compte tenu de la spécificité des différents secteurs de traitement et des besoins spécifiques des micro, petites et moyennes entreprises. »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question concernant la légalité spécifique de l'utilisation de Google Drive ou de fichiers Excel partagés. Cependant, en tant que responsable du traitement, vous « mettez en œuvre des mesures techniques et organisationnelles appropriées pour s'assurer et être en mesure de démontrer que le traitement est effectué conformément au présent règlement » [1]. Ces mesures doivent être « réexaminées et actualisées si nécessaire » [1]. Si votre association compte moins de 250 employés, l'obligation de tenir un registre des activités de traitement ne s'applique pas « sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 » [5]. Les bénévoles ont le droit d'obtenir la confirmation que leurs données sont traitées et d'accéder à ces données [4]. Ils disposent également du « droit d'introduire une réclamation auprès d'une autorité de contrôle » [4]. Les autorités encouragent l'élaboration de codes de conduite qui tiennent compte des « besoins spécifiques des micro, petites et moyennes entreprises » [3].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : traitement de données à caractère personnel ; responsable du traitement ; mesures techniques et organisationnelles appropriées ; sécurité des données ; hébergement de données ; registre des activités de traitement

Temps : recherche 29.6 s · génération 1.8 s (3172 tokens lus, 664 écrits, 456.1 tokens/s) · contrôle de pertinence 0.4 s · reformulation 0.3 s · attente des limites de l'API 34 s (non comptée)

## e05 — Sur mon site web, j'utilise seulement Google Analytics. Je suis obligé de mettre un bandeau cookies ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
  [2] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 11 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [4] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun

RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : consentement de l'internaute ; bandeau d'information ; cookies de mesure d'audience ; finalité de traitement ; données à caractère personnel

Temps : recherche 26.0 s · génération 0.6 s (3416 tokens lus, 25 écrits, 502.8 tokens/s) · reformulation 0.2 s

## e06 — La boîte mail de l'accueil a été piratée hier. Qu'est-ce que je dois faire ? Je dois prévenir quelqu'un ?

Article attendu : RGPD art. 33 ou RGPD art. 34 — passage [1].

### Réponse du copilote

> Oui, vous devez prévenir l'autorité de contrôle compétente et, potentiellement, les personnes concernées, si vous êtes le responsable du traitement [1]. La notification à l'autorité de contrôle doit être faite « dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance », « à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques » [1]. Si le piratage est susceptible d'engendrer un « risque élevé pour les droits et libertés d'une personne physique », vous devez « communique[r] la violation de données à caractère personnel à la personne concernée dans les meilleurs délais » [2]. Cette communication aux personnes n'est « pas nécessaire » si vous avez mis en œuvre des mesures de protection rendant les données « incompréhensibles pour toute personne qui n'est pas autorisée à y avoir accès, telles que le chiffrement », ou si vous avez pris des mesures garantissant que le risque « n'est plus susceptible de se matérialiser » [2]. Enfin, vous devez « documente[r] toute violation de données à caractère personnel, en indiquant les faits concernant la violation des données à caractère personnel, ses effets et les mesures prises pour y remédier » [1]. Si vous êtes un sous-traitant, vous devez « notifie[r] au responsable du traitement toute violation de données à caractère personnel dans les meilleurs délais après en avoir pris connaissance » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. »
  [1] « Le sous-traitant notifie au responsable du traitement toute violation de données à caractère personnel dans les meilleurs délais après en avoir pris connaissance. »
  [1] « Le responsable du traitement documente toute violation de données à caractère personnel, en indiquant les faits concernant la violation des données à caractère personnel, ses effets et les mesures prises pour y remédier. »
  [2] « Lorsqu'une violation de données à caractère personnel est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement communique la violation de données à caractère personnel à la personne concernée dans les meilleurs délais. »
  [2] « La communication à la personne concernée visée au paragraphe 1 n'est pas nécessaire si l'une ou l'autre des conditions suivantes est remplie: a) le responsable du traitement a mis en œuvre les mesures de protection techniques et organisationnelles appropriées et ces mesures ont été appliquées aux données à caractère personnel affectées par ladite violation, en particulier les mesures qui rendent les données à caractère personnel incompréhensibles pour toute personne qui n'est pas autorisée à y avoir accès, telles que le chiffrement; »
  [2] « b) le responsable du traitement a pris des mesures ultérieures qui garantissent que le risque élevé pour les droits et libertés des personnes concernées visé au paragraphe 1 n'est plus susceptible de se matérialiser; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 33 : Notification à l'autorité de contrôle d'une violation de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_33
  [2] RGPD — règlement (UE) 2016/679, article 34 : Communication à la personne concernée d'une violation de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_34
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 77 : Droit d'introduire une réclamation auprès d'une autorité de contrôle
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_77
  [4] RGPD — règlement (UE) 2016/679, article 58, paragraphe 2 : Pouvoirs
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_58
  [5] RGPD — règlement (UE) 2016/679, article 57, paragraphe 1, points u) à v) : Missions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_57
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « communique[r] la violation de données à caractère personnel à la personne concernée dans les meilleurs délais » (et 2 autre(s)).
Attention : La réponse ne reprend que 2 des 3 cas énumérés au passage [2], sans dire qu'elle n'en cite qu'une partie. Vérifiez la liste complète.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. »
- [1] « Le sous-traitant notifie au responsable du traitement toute violation de données à caractère personnel dans les meilleurs délais après en avoir pris connaissance. »
- [1] « Le responsable du traitement documente toute violation de données à caractère personnel, en indiquant les faits concernant la violation des données à caractère personnel, ses effets et les mesures prises pour y remédier. »
- [2] « Lorsqu'une violation de données à caractère personnel est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement communique la violation de données à caractère personnel à la personne concernée dans les meilleurs délais. »
- [2] « La communication à la personne concernée visée au paragraphe 1 n'est pas nécessaire si l'une ou l'autre des conditions suivantes est remplie: a) le responsable du traitement a mis en œuvre les mesures de protection techniques et organisationnelles appropriées et ces mesures ont été appliquées aux données à caractère personnel affectées par ladite violation, en particulier les mesures qui rendent les données à caractère personnel incompréhensibles pour toute personne qui n'est pas autorisée à y avoir accès, telles que le chiffrement; »
- [2] « b) le responsable du traitement a pris des mesures ultérieures qui garantissent que le risque élevé pour les droits et libertés des personnes concernées visé au paragraphe 1 n'est plus susceptible de se matérialiser; »

RÉPONSE :
Oui, vous devez prévenir l'autorité de contrôle compétente et, potentiellement, les personnes concernées, si vous êtes le responsable du traitement [1]. La notification à l'autorité de contrôle doit être faite « dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance », « à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques » [1]. Si le piratage est susceptible d'engendrer un « risque élevé pour les droits et libertés d'une personne physique », vous devez « communique[r] la violation de données à caractère personnel à la personne concernée dans les meilleurs délais » [2]. Cette communication aux personnes n'est « pas nécessaire » si vous avez mis en œuvre des mesures de protection rendant les données « incompréhensibles pour toute personne qui n'est pas autorisée à y avoir accès, telles que le chiffrement », ou si vous avez pris des mesures garantissant que le risque « n'est plus susceptible de se matérialiser » [2]. Enfin, vous devez « documente[r] toute violation de données à caractère personnel, en indiquant les faits concernant la violation des données à caractère personnel, ses effets et les mesures prises pour y remédier » [1]. Si vous êtes un sous-traitant, vous devez « notifie[r] au responsable du traitement toute violation de données à caractère personnel dans les meilleurs délais après en avoir pris connaissance » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : notification de violation de données personnelles ; autorité de contrôle compétente ; personne concernée ; registre des violations de données personnelles ; mesures d'atténuation

Temps : recherche 31.6 s · génération 1.9 s (2881 tokens lus, 727 écrits, 492.1 tokens/s) · contrôle de pertinence 1.0 s · reformulation 0.2 s · attente des limites de l'API 21 s (non comptée)

## e07 — Un prestataire extérieur gère notre paie. Je dois signer un contrat spécial avec lui pour les données ?

Article attendu : RGPD art. 28, paragraphe 3 — passage [3].

### Réponse du copilote

> Oui, vous devez signer un contrat spécifique avec votre prestataire de paie, car il agit en tant que sous-traitant pour votre compte [2]. Ce contrat, exigé par le RGPD (article 28), doit définir l'objet, la durée, la nature et la finalité du traitement, ainsi que le type de données et les catégories de personnes concernées [3]. Il doit également prévoir que le sous-traitant ne traite les données que sur instruction documentée de votre part, veille à la confidentialité du personnel, prend les mesures de sécurité requises et respecte les conditions pour recruter d'autres sous-traitants [3].

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
Oui, vous devez signer un contrat spécifique avec votre prestataire de paie, car il agit en tant que sous-traitant pour votre compte [2]. Ce contrat, exigé par le RGPD (article 28), doit définir l'objet, la durée, la nature et la finalité du traitement, ainsi que le type de données et les catégories de personnes concernées [3]. Il doit également prévoir que le sous-traitant ne traite les données que sur instruction documentée de votre part, veille à la confidentialité du personnel, prend les mesures de sécurité requises et respecte les conditions pour recruter d'autres sous-traitants [3].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : sous-traitant ; contrat de traitement ; mesures techniques et organisationnelles ; registre des activités de traitement ; responsable de traitement ; données à caractère personnel

Temps : recherche 23.3 s · génération 1.6 s (3351 tokens lus, 577 écrits, 474.8 tokens/s) · contrôle de pertinence 2.7 s · reformulation 0.2 s · attente des limites de l'API 27 s (non comptée)

## e08 — Je peux envoyer notre newsletter à mes anciens clients sans leur demander leur accord ?

Article attendu : RGPD art. 6, paragraphe 1 ou RGPD art. 21 — passage [1].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 21 : Droit d'opposition
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_21
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [3] RGPD — règlement (UE) 2016/679, article 7 : Conditions applicables au consentement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_7
  [4] RGPD — règlement (UE) 2016/679, article 4, définition 11 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [5] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

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
- [3] « Dans les cas où le traitement repose sur le consentement, le responsable du traitement est en mesure de démontrer que la personne concernée a donné son consentement au traitement de données à caractère personnel la concernant. »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question, car ils ne précisent pas si l'envoi d'une newsletter à des anciens clients est interdit ou permis sans consentement préalable, mais ils définissent les droits d'opposition et les conditions du consentement. Si vous basez l'envoi sur le consentement, vous devez être en mesure de démontrer que la personne concernée a donné son consentement [3]. Si vous basez le traitement sur un autre fondement légal (comme l'intérêt légitime, visé par l'article 6, paragraphe 1, point f), la personne concernée a le droit de s'opposer à tout moment [1]. En cas d'opposition, vous ne traitez plus les données, sauf si vous démontrez qu'il existe des « motifs légitimes et impérieux pour le traitement qui prévalent sur les intérêts et les droits et libertés de la personne concernée » [1]. Si l'envoi est considéré comme de la prospection, l'opposition entraîne l'arrêt immédiat du traitement à ces fins [1]. Dans tous les cas, vous devez informer la personne de son droit d'opposition « au plus tard au moment de la première communication » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : consentement ; consentement explicite ; consentement préalable ; droit d'opposition ; traitement de données à caractère personnel

Temps : recherche 27.9 s · génération 1.7 s (3123 tokens lus, 638 écrits, 516.1 tokens/s) · contrôle de pertinence 2.7 s · reformulation 0.8 s · attente des limites de l'API 32 s (non comptée)

## e09 — Un salarié me demande une copie de toutes les données que j'ai sur lui, même les mails où on parle de lui. Je dois tout lui donner ? J'ai combien de temps pour répondre ?

Article attendu : RGPD art. 15 ou RGPD art. 12, paragraphe 3 — passage [1].

### Réponse du copilote

> Oui, vous devez fournir une copie des données à caractère personnel faisant l'objet d'un traitement, ce qui inclut les e-mails où le salarié est mentionné, car il a le droit d'accéder à ces données [1]. Cependant, cette obligation n'est pas absolue : le droit d'obtenir une copie « ne porte pas atteinte aux droits et libertés d'autrui » [1]. Vous avez un délai d'un mois à compter de la réception de la demande pour répondre [2]. Si la demande est complexe ou si vous recevez de nombreuses demandes, vous pouvez prolonger ce délai de deux mois, à condition d'informer la personne concernée de cette prolongation et des motifs du report dans le premier mois [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: »
  [1] « Le responsable du traitement fournit une copie des données à caractère personnel faisant l'objet d'un traitement. »
  [1] « Le droit d'obtenir une copie visé au paragraphe 3 ne porte pas atteinte aux droits et libertés d'autrui. »
  [2] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. »
  [2] « Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. »
  [2] « Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [4] RGPD — règlement (UE) 2016/679, article 12, paragraphe 4 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [5] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: »
- [1] « Le responsable du traitement fournit une copie des données à caractère personnel faisant l'objet d'un traitement. »
- [1] « Le droit d'obtenir une copie visé au paragraphe 3 ne porte pas atteinte aux droits et libertés d'autrui. »
- [2] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. »
- [2] « Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. »
- [2] « Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. »

RÉPONSE :
Oui, vous devez fournir une copie des données à caractère personnel faisant l'objet d'un traitement, ce qui inclut les e-mails où le salarié est mentionné, car il a le droit d'accéder à ces données [1]. Cependant, cette obligation n'est pas absolue : le droit d'obtenir une copie « ne porte pas atteinte aux droits et libertés d'autrui » [1]. Vous avez un délai d'un mois à compter de la réception de la demande pour répondre [2]. Si la demande est complexe ou si vous recevez de nombreuses demandes, vous pouvez prolonger ce délai de deux mois, à condition d'informer la personne concernée de cette prolongation et des motifs du report dans le premier mois [2].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit d'accès ; données à caractère personnel ; délai d'un mois ; demande d'accès ; information du sujet

Temps : recherche 27.1 s · génération 1.8 s (3146 tokens lus, 428 écrits, 517.9 tokens/s) · contrôle de pertinence 1.5 s · reformulation 0.2 s · attente des limites de l'API 3 s (non comptée)

## e10 — Un salarié est parti de l'entreprise. Je peux encore lire sa boîte mail professionnelle ?

Article attendu : RGPD art. 5 ou RGPD art. 6, paragraphe 1 — passage [3].

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [2] RGPD — règlement (UE) 2016/679, article 6, paragraphe 4 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
  [3] RGPD — règlement (UE) 2016/679, article 6, paragraphe 1 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
  [4] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun

RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droits de l'employeur sur les données professionnelles ; confidentialité des communications ; proportionnalité de l'accès ; finalité du traitement ; consentement du salarié ; protection des données à caractère personnel

Temps : recherche 26.1 s · génération 0.4 s (3133 tokens lus, 25 écrits, 486.8 tokens/s) · reformulation 0.2 s · attente des limites de l'API 14 s (non comptée)

## e11 — Dans notre organisme de formation, on demande aux stagiaires leur numéro de sécurité sociale et des informations sur leur handicap. On a le droit ?

Article attendu : RGPD art. 9, paragraphe 1 ou RGPD art. 9, paragraphe 2_a i ou RGPD art. 87 — passage [1].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 9, paragraphe 2, points a) à i) : Traitement portant sur des catégories particulières de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
  [2] RGPD — règlement (UE) 2016/679, article 9, paragraphe 1 : Traitement portant sur des catégories particulières de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
  [3] RGPD — règlement (UE) 2016/679, article 9, paragraphe 3 : Traitement portant sur des catégories particulières de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
  [4] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [5] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [2] « Le traitement des données à caractère personnel qui révèle l'origine raciale ou ethnique, les opinions politiques, les convictions religieuses ou philosophiques ou l'appartenance syndicale, ainsi que le traitement des données génétiques, des données biométriques aux fins d'identifier une personne physique de manière unique, des données concernant la santé ou des données concernant la vie sexuelle ou l'orientation sexuelle d'une personne physique sont interdits. »
- [1] « a) la personne concernée a donné son consentement explicite au traitement de ces données à caractère personnel pour une ou plusieurs finalités spécifiques, sauf lorsque le droit de l'Union ou le droit de l'État membre prévoit que l'interdiction visée au paragraphe 1 ne peut pas être levée par la personne concernée; »
- [1] « b) le traitement est nécessaire aux fins de l'exécution des obligations et de l'exercice des droits propres au responsable du traitement ou à la personne concernée en matière de droit du travail, de la sécurité sociale et de la protection sociale, dans la mesure où ce traitement est autorisé par le droit de l'Union, par le droit d'un État membre ou par une convention collective conclue en vertu du droit d'un État membre qui prévoit des garanties appropriées pour les droits fondamentaux et les intérêts de la personne concernée; »
- [1] « h) le traitement est nécessaire aux fins de la médecine préventive ou de la médecine du travail, de l'appréciation de la capacité de travail du travailleur, de diagnostics médicaux, de la prise en charge sanitaire ou sociale, ou de la gestion des systèmes et des services de soins de santé ou de protection sociale sur la base du droit de l'Union, du droit d'un État membre ou en vertu d'un contrat conclu avec un professionnel de la santé et soumis aux conditions et garanties visées au paragraphe 3; »
- [3] « Les données à caractère personnel visées au paragraphe 1 peuvent faire l'objet d'un traitement aux fins prévues au paragraphe 2, point h), si ces données sont traitées par un professionnel de la santé soumis à une obligation de secret professionnel conformément au droit de l'Union, au droit d'un État membre ou aux règles arrêtées par les organismes nationaux compétents, ou sous sa responsabilité, ou par une autre personne également soumise à une obligation de secret conformément au droit de l'Union ou au droit d'un État membre ou aux règles arrêtées par les organismes nationaux compétents. »

RÉPONSE :
Le traitement des données concernant la santé, comme les informations sur un handicap, est en principe interdit par le RGPD, article 9, paragraphe 1 [2].
Cependant, ce traitement est possible si l'une des conditions d'exception prévues à l'article 9, paragraphe 2 est remplie [1].
Parmi ces conditions, le consentement explicite de la personne concernée pour une finalité spécifique est admis, « sauf lorsque le droit de l'Union ou le droit de l'État membre prévoit que l'interdiction visée au paragraphe 1 ne peut pas être levée par la personne concernée » [1].
Une autre condition possible est que le traitement soit « nécessaire aux fins de l'exécution des obligations et de l'exercice des droits propres au responsable du traitement ou à la personne concernée en matière de droit du travail, de la sécurité sociale et de la protection sociale », à condition que ce traitement soit « autorisé par le droit de l'Union, par le droit d'un État membre ou par une convention collective conclue en vertu du droit d'un État membre qui prévoit des garanties appropriées pour les droits fondamentaux et les intérêts de la personne concernée » [1].
Si le traitement vise la médecine préventive ou la prise en charge sanitaire, il doit être effectué par un professionnel de la santé soumis à une obligation de secret professionnel, ou sous sa responsabilité [3].
Les passages fournis ne précisent pas si la demande d'un numéro de sécurité sociale et d'informations sur le handicap dans le cadre d'un organisme de formation remplit spécifiquement l'une de ces conditions légales ou conventionnelles, il convient donc de vérifier la base légale applicable dans votre contexte national.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données de santé ; données sensibles ; consentement ; minimisation des données ; finalité

Temps : recherche 29.9 s · génération 2.8 s (3175 tokens lus, 900 écrits, 422.8 tokens/s) · contrôle de pertinence 0.1 s · reformulation 0.4 s · attente des limites de l'API 45 s (non comptée)

## e12 — Je peux suivre les véhicules de mes techniciens par GPS ?

Article attendu : RGPD art. 6, paragraphe 1 ou RGPD art. 5 — passage [1].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [3] RGPD — règlement (UE) 2016/679, article 20 : Droit à la portabilité des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_20
  [4] RGPD — règlement (UE) 2016/679, article 7 : Conditions applicables au consentement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_7
  [5] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les données à caractère personnel doivent être: a) traitées de manière licite, loyale et transparente au regard de la personne concernée (licéité, loyauté, transparence); »
- [1] « b) collectées pour des finalités déterminées, explicites et légitimes, et ne pas être traitées ultérieurement d'une manière incompatible avec ces finalités; »
- [1] « c) adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités pour lesquelles elles sont traitées (minimisation des données); »
- [1] « e) conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées; »
- [1] « f) traitées de façon à garantir une sécurité appropriée des données à caractère personnel, y compris la protection contre le traitement non autorisé ou illicite et contre la perte, la destruction ou les dégâts d'origine accidentelle, à l'aide de mesures techniques ou organisationnelles appropriées (intégrité et confidentialité); »
- [1] « 2. Le responsable du traitement est responsable du respect du paragraphe 1 et est en mesure de démontrer que celui-ci est respecté (responsabilité). »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question. Ils ne précisent pas si le suivi GPS des véhicules de techniciens est autorisé ou interdit, mais ils énoncent les principes généraux que vous devez respecter si vous traitez ces données. En tant que responsable du traitement, vous devez traiter les données de manière licite, loyale et transparente [1]. Vous devez les collecter pour des finalités déterminées, explicites et légitimes, et ne pas les traiter ultérieurement d'une manière incompatible avec ces finalités [1]. Les données doivent être adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités pour lesquelles elles sont traitées [1]. Vous devez les conserver pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées [1]. Enfin, vous devez garantir une sécurité appropriée des données à caractère personnel, y compris la protection contre le traitement non autorisé ou illicite [1]. Vous êtes responsable du respect de ces principes et devez être en mesure de le démontrer [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données de localisation ; données à caractère personnel ; consentement ; finalité ; minimisation des données ; droit à l'information

Temps : recherche 28.2 s · génération 1.6 s (3747 tokens lus, 526 écrits, 480.4 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.2 s · attente des limites de l'API 23 s (non comptée)

## e13 — On veut publier sur Facebook des photos des bénévoles prises pendant notre fête annuelle. Il faut leur accord écrit ?

Article attendu : RGPD art. 6, paragraphe 1 ou RGPD art. 7 — passage [1].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 7 : Conditions applicables au consentement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_7
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [3] RGPD — règlement (UE) 2016/679, article 4, définition 11 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [4] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [3] « «consentement» de la personne concernée, toute manifestation de volonté, libre, spécifique, éclairée et univoque par laquelle la personne concernée accepte, par une déclaration ou par un acte positif clair, que des données à caractère personnel la concernant fassent l'objet d'un traitement; »
- [1] « Si le consentement de la personne concernée est donné dans le cadre d'une déclaration écrite qui concerne également d'autres questions, la demande de consentement est présentée sous une forme qui la distingue clairement de ces autres questions, sous une forme compréhensible et aisément accessible, et formulée en des termes clairs et simples. »
- [1] « La personne concernée a le droit de retirer son consentement à tout moment. »
- [1] « Il est aussi simple de retirer que de donner son consentement. »

RÉPONSE :
Non, il ne faut pas obligatoirement un accord écrit, car le consentement peut être donné par « une déclaration ou par un acte positif clair » [3]. Cependant, si vous choisissez de recueillir ce consentement par écrit, la demande doit être « présentée sous une forme qui la distingue clairement de ces autres questions, sous une forme compréhensible et aisément accessible, et formulée en des termes clairs et simples » [1]. Vous devez également informer les bénévoles qu'ils ont « le droit de retirer son consentement à tout moment » et que « il est aussi simple de retirer que de donner son consentement » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : consentement ; données à caractère personnel ; traitement ; responsable du traitement ; droit à l'information

Temps : recherche 26.8 s · génération 1.0 s (2891 tokens lus, 320 écrits, 473.7 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.3 s · attente des limites de l'API 10 s (non comptée)

## e14 — On a 8 salariés. On doit tenir un registre des traitements et nommer un DPO ?

Article attendu : RGPD art. 30 ou RGPD art. 37 — passage [1].

### Réponse du copilote

> Concernant le registre des traitements, vous n'êtes pas obligé de le tenir si vous comptez moins de 250 employés, « sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 » [1].
> Concernant la nomination du DPO, l'obligation de désigner un délégué à la protection des données « en tout état de cause » ne s'applique que si vous êtes une autorité publique, si vos activités de base consistent en un suivi régulier et systématique à grande échelle, ou si elles consistent en un traitement à grande échelle de catégories particulières de données [2]. Dans les autres cas, vous « pouvez désigner » un DPO, ou vous en êtes « tenu » seulement « si le droit de l'Union ou le droit d'un État membre l'exige » [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10. »
  [2] « Le responsable du traitement et le sous-traitant désignent en tout état de cause un délégué à la protection des données lorsque: a) le traitement est effectué par une autorité publique ou un organisme public, à l'exception des juridictions agissant dans l'exercice de leur fonction juridictionnelle; b) les activités de base du responsable du traitement ou du sous-traitant consistent en des opérations de traitement qui, du fait de leur nature, de leur portée et/ou de leurs finalités, exigent un suivi régulier et systématique à grande échelle des personnes concernées; ou c) les activités de base du responsable du traitement ou du sous-traitant consistent en un traitement à grande échelle de catégories particulières de données visées à l’article 9 ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l’article 10. »
  [2] « Dans les cas autres que ceux visés au paragraphe 1, le responsable du traitement ou le sous-traitant ou les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent désigner ou, si le droit de l'Union ou le droit d'un État membre l'exige, sont tenus de désigner un délégué à la protection des données. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30
  [2] RGPD — règlement (UE) 2016/679, article 37 : Désignation du délégué à la protection des données (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_37
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 38 : Fonction du délégué à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_38
  [4] RGPD — règlement (UE) 2016/679, article 39 : Missions du délégué à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_39
  [5] RGPD — règlement (UE) 2016/679, article 24 : Responsabilité du responsable du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_24

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10. »
- [2] « Le responsable du traitement et le sous-traitant désignent en tout état de cause un délégué à la protection des données lorsque: a) le traitement est effectué par une autorité publique ou un organisme public, à l'exception des juridictions agissant dans l'exercice de leur fonction juridictionnelle; b) les activités de base du responsable du traitement ou du sous-traitant consistent en des opérations de traitement qui, du fait de leur nature, de leur portée et/ou de leurs finalités, exigent un suivi régulier et systématique à grande échelle des personnes concernées; ou c) les activités de base du responsable du traitement ou du sous-traitant consistent en un traitement à grande échelle de catégories particulières de données visées à l’article 9 ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l’article 10. »
- [2] « Dans les cas autres que ceux visés au paragraphe 1, le responsable du traitement ou le sous-traitant ou les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent désigner ou, si le droit de l'Union ou le droit d'un État membre l'exige, sont tenus de désigner un délégué à la protection des données. »

RÉPONSE :
Concernant le registre des traitements, vous n'êtes pas obligé de le tenir si vous comptez moins de 250 employés, « sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 » [1].
Concernant la nomination du DPO, l'obligation de désigner un délégué à la protection des données « en tout état de cause » ne s'applique que si vous êtes une autorité publique, si vos activités de base consistent en un suivi régulier et systématique à grande échelle, ou si elles consistent en un traitement à grande échelle de catégories particulières de données [2]. Dans les autres cas, vous « pouvez désigner » un DPO, ou vous en êtes « tenu » seulement « si le droit de l'Union ou le droit d'un État membre l'exige » [2].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : registre des activités de traitement ; responsable de la protection des données

Temps : recherche 29.8 s · génération 1.9 s (3587 tokens lus, 687 écrits, 468.6 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.6 s · attente des limites de l'API 28 s (non comptée)

## e15 — Notre logiciel de gestion des clients est hébergé aux États-Unis. C'est autorisé ?

Article attendu : RGPD art. 44 ou RGPD art. 45, paragraphe 1 ou RGPD art. 46 — passage [1].

### Réponse du copilote

> Oui, l'hébergement de votre logiciel aux États-Unis est autorisé, mais uniquement si vous respectez les conditions légales pour les transferts de données vers un pays tiers [1]. En tant que responsable du traitement, vous ne pouvez transférer des données vers un pays tiers que si vous avez prévu des « garanties appropriées » et que les personnes concernées disposent de « droits opposables et de voies de droit effectives » [1]. Ces garanties peuvent être fournies, par exemple, par des « clauses types de protection des données adoptées par la Commission » ou par une autorité de contrôle approuvée par la Commission [1]. Si aucune de ces garanties n'est en place, le transfert n'est possible que dans des situations particulières, comme si « la personne concernée a donné son consentement explicite au transfert envisagé, après avoir été informée des risques » [5]. Les passages trouvés ne permettent pas de savoir si les États-Unis bénéficient actuellement d'une décision d'adéquation de la Commission européenne ; cette liste est publiée par la Commission européenne.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
  [1] « Les garanties appropriées visées au paragraphe 1 peuvent être fournies, sans que cela ne nécessite une autorisation particulière d'une autorité de contrôle, par: »
  [1] « c) des clauses types de protection des données adoptées par la Commission en conformité avec la procédure d'examen visée à l'article 93, paragraphe 2; »
  [1] « d) des clauses types de protection des données adoptées par une autorité de contrôle et approuvées par la Commission en conformité avec la procédure d'examen visée à l'article 93, paragraphe 2; »
  [5] « En l'absence de décision d'adéquation en vertu de l'article 45, paragraphe 3, ou de garanties appropriées en vertu de l'article 46, y compris des règles d'entreprise contraignantes, un transfert ou un ensemble de transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale ne peut avoir lieu qu'à l'une des conditions suivantes: »
  [5] « a) la personne concernée a donné son consentement explicite au transfert envisagé, après avoir été informée des risques que ce transfert pouvait comporter pour elle en raison de l'absence de décision d'adéquation et de garanties appropriées; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 46 : Transferts moyennant des garanties appropriées (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_46
  [5] RGPD — règlement (UE) 2016/679, article 49, paragraphe 1 : Dérogations pour des situations particulières (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_49
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 45, paragraphe 2 : Transferts fondés sur une décision d'adéquation
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
  [3] RGPD — règlement (UE) 2016/679, article 40, paragraphe 3 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [4] RGPD — règlement (UE) 2016/679, article 40, paragraphe 1 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
Note : La liste des pays bénéficiant d'une décision d'adéquation n'est pas dans les textes utilisés par le copilote : consultez la page de la Commission européenne sur les décisions d'adéquation (en anglais) : https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en
Attention : La réponse ne reprend que 1 des 7 cas énumérés au passage [5], sans dire qu'elle n'en cite qu'une partie. Vérifiez la liste complète.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
- [1] « Les garanties appropriées visées au paragraphe 1 peuvent être fournies, sans que cela ne nécessite une autorisation particulière d'une autorité de contrôle, par: »
- [1] « c) des clauses types de protection des données adoptées par la Commission en conformité avec la procédure d'examen visée à l'article 93, paragraphe 2; »
- [1] « d) des clauses types de protection des données adoptées par une autorité de contrôle et approuvées par la Commission en conformité avec la procédure d'examen visée à l'article 93, paragraphe 2; »
- [5] « En l'absence de décision d'adéquation en vertu de l'article 45, paragraphe 3, ou de garanties appropriées en vertu de l'article 46, y compris des règles d'entreprise contraignantes, un transfert ou un ensemble de transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale ne peut avoir lieu qu'à l'une des conditions suivantes: »
- [5] « a) la personne concernée a donné son consentement explicite au transfert envisagé, après avoir été informée des risques que ce transfert pouvait comporter pour elle en raison de l'absence de décision d'adéquation et de garanties appropriées; »

RÉPONSE :
Oui, l'hébergement de votre logiciel aux États-Unis est autorisé, mais uniquement si vous respectez les conditions légales pour les transferts de données vers un pays tiers [1]. En tant que responsable du traitement, vous ne pouvez transférer des données vers un pays tiers que si vous avez prévu des « garanties appropriées » et que les personnes concernées disposent de « droits opposables et de voies de droit effectives » [1]. Ces garanties peuvent être fournies, par exemple, par des « clauses types de protection des données adoptées par la Commission » ou par une autorité de contrôle approuvée par la Commission [1]. Si aucune de ces garanties n'est en place, le transfert n'est possible que dans des situations particulières, comme si « la personne concernée a donné son consentement explicite au transfert envisagé, après avoir été informée des risques » [5]. Les passages trouvés ne permettent pas de savoir si les États-Unis bénéficient actuellement d'une décision d'adéquation de la Commission européenne ; cette liste est publiée par la Commission européenne.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : transfert de données vers un pays tiers ; pays tiers ; mesures de sécurité appropriées ; garanties appropriées ; décision d'adéquation ; sous-traitant

Temps : recherche 27.8 s · génération 1.6 s (3338 tokens lus, 609 écrits, 505.8 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.3 s · attente des limites de l'API 26 s (non comptée)

## e16 — On ne crée pas d'IA, on utilise juste des outils comme ChatGPT. Est-ce que l'AI Act nous concerne quand même ?

Article attendu : AI Act art. 3, définition 4 ou AI Act art. 2, paragraphe 1 ou AI Act art. 4 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 4 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [3] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 2 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [4] AI Act — règlement (UE) 2024/1689, article 13 : Transparence et fourniture d’informations aux déployeurs
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_13
  [5] AI Act — règlement (UE) 2024/1689, article 75, paragraphe 1 : Surveillance du marché et contrôle des systèmes d'IA et assistance mutuelle
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_75
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. »
- [1] « Les déployeurs d’un système d’IA qui génère ou manipule des textes publiés dans le but d’informer le public sur des questions d’intérêt public indiquent que le texte a été généré ou manipulé par une IA. »
- [2] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »
- [3] « Les fournisseurs de systèmes d’IA, y compris de systèmes d’IA à usage général, qui génèrent des contenus de synthèse de type audio, image, vidéo ou texte, veillent à ce que les sorties des systèmes d’IA soient marquées dans un format lisible par machine et identifiables comme ayant été générées ou manipulées par une IA. »
- [4] « La conception et le développement des systèmes d’IA à haut risque sont tels que le fonctionnement de ces systèmes est suffisamment transparent pour permettre aux déployeurs d’interpréter les sorties d’un système et de les utiliser de manière appropriée. »
- [5] « La compétence exclusive visée au premier alinéa s’applique aux fournisseurs de ces systèmes. »

RÉPONSE :
Oui, l'AI Act vous concerne en tant qu'utilisateur (ou « déployeur »), mais vos obligations sont différentes de celles du créateur de l'outil (le « fournisseur »).
Si vous utilisez un outil comme ChatGPT pour générer des images, de l'audio, de la vidéo ou du texte, vous devez indiquer que ces contenus ont été générés ou manipulés par une IA, notamment s'il s'agit d'un « hypertrucage » ou de textes publiés pour informer le public sur des questions d'intérêt public [1].
En revanche, les obligations techniques de conception, comme la garantie que les utilisateurs savent qu'ils interagissent avec une IA ou la mise en place de marquages lisibles par machine, incombent aux fournisseurs des systèmes d'IA, y compris ceux à usage général [2] [3].
Les passages trouvés ne traitent pas directement de la question de savoir si l'utilisation simple d'un outil sans génération de contenu spécifique (par exemple, pour de la simple conversation privée) déclenche des obligations de transparence pour le déployeur, mais ils précisent que la compétence de surveillance s'applique aux fournisseurs [5].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : fournisseur de modèle de fondation ; utilisateur déployant ; modèle de fondation ; système d'IA ; obligation de transparence ; utilisateur

Temps : recherche 31.0 s · génération 1.7 s (3237 tokens lus, 628 écrits, 480.6 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.3 s · attente des limites de l'API 14 s (non comptée)

## e17 — Je voudrais utiliser un logiciel d'IA qui trie automatiquement les CV. C'est interdit ? Sinon, quelles règles je dois respecter ?

Article attendu : AI Act annexe III, point 4 ou AI Act art. 26 — passage [3].

### Réponse du copilote

> Non, l'utilisation d'un logiciel d'IA pour trier automatiquement les CV n'est pas interdite par l'AI Act, car cette pratique ne figure pas dans la liste des pratiques interdites de l'article 5 [1] [2]. En revanche, ce type de système est classé comme un système d'IA à haut risque, car il est destiné à être utilisé pour le recrutement ou la sélection de personnes physiques, notamment pour analyser et filtrer les candidatures [3]. Si le système effectue un profilage de personnes physiques, il est toujours considéré comme étant à haut risque [4]. En tant que déployeur, vous devez vous assurer que le système permet un contrôle effectif par des personnes physiques pendant sa période d'utilisation [5]. Le système doit être conçu pour que les personnes chargées du contrôle humain puissent comprendre les capacités et les limites du système, surveiller son fonctionnement et détecter les anomalies [5]. De plus, ces personnes doivent avoir la possibilité de décider, dans une situation particulière, de ne pas utiliser le système ou d'ignorer, remplacer ou inverser la sortie du système [5].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »
  [4] « Nonobstant le premier alinéa, un système d’IA visé à l’annexe III est toujours considéré comme étant à haut risque lorsqu’il effectue un profilage de personnes physiques. »
  [5] « 1. La conception et le développement des systèmes d’IA à haut risque permettent, notamment au moyen d’interfaces homme-machine appropriées, un contrôle effectif par des personnes physiques pendant leur période d’utilisation. »
  [5] « 4. Aux fins de la mise en œuvre des dispositions des paragraphes 1, 2 et 3, le système d’IA à haut risque est fourni au déployeur de telle manière que les personnes physiques chargées d’effectuer un contrôle humain, dans la mesure où cela est approprié et proportionné, ont la possibilité: »
  [5] « a) de comprendre correctement les capacités et les limites pertinentes du système d’IA à haut risque et d’être en mesure de surveiller correctement son fonctionnement, y compris en vue de détecter et de traiter les anomalies, les dysfonctionnements et les performances inattendues; »
  [5] « d) de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou inverser la sortie du système d’IA à haut risque; »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points f) à h) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [2] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points a) à e) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [3] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [4] AI Act — règlement (UE) 2024/1689, article 6, point d : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
  [5] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14
Attention : La réponse cite [1], [2] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [3] « a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »
- [4] « Nonobstant le premier alinéa, un système d’IA visé à l’annexe III est toujours considéré comme étant à haut risque lorsqu’il effectue un profilage de personnes physiques. »
- [5] « 1. La conception et le développement des systèmes d’IA à haut risque permettent, notamment au moyen d’interfaces homme-machine appropriées, un contrôle effectif par des personnes physiques pendant leur période d’utilisation. »
- [5] « 4. Aux fins de la mise en œuvre des dispositions des paragraphes 1, 2 et 3, le système d’IA à haut risque est fourni au déployeur de telle manière que les personnes physiques chargées d’effectuer un contrôle humain, dans la mesure où cela est approprié et proportionné, ont la possibilité: »
- [5] « a) de comprendre correctement les capacités et les limites pertinentes du système d’IA à haut risque et d’être en mesure de surveiller correctement son fonctionnement, y compris en vue de détecter et de traiter les anomalies, les dysfonctionnements et les performances inattendues; »
- [5] « d) de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou inverser la sortie du système d’IA à haut risque; »

RÉPONSE :
Non, l'utilisation d'un logiciel d'IA pour trier automatiquement les CV n'est pas interdite par l'AI Act, car cette pratique ne figure pas dans la liste des pratiques interdites de l'article 5 [1] [2]. En revanche, ce type de système est classé comme un système d'IA à haut risque, car il est destiné à être utilisé pour le recrutement ou la sélection de personnes physiques, notamment pour analyser et filtrer les candidatures [3]. Si le système effectue un profilage de personnes physiques, il est toujours considéré comme étant à haut risque [4]. En tant que déployeur, vous devez vous assurer que le système permet un contrôle effectif par des personnes physiques pendant sa période d'utilisation [5]. Le système doit être conçu pour que les personnes chargées du contrôle humain puissent comprendre les capacités et les limites du système, surveiller son fonctionnement et détecter les anomalies [5]. De plus, ces personnes doivent avoir la possibilité de décider, dans une situation particulière, de ne pas utiliser le système ou d'ignorer, remplacer ou inverser la sortie du système [5].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : système d'IA à haut risque ; employeur ; candidat à un emploi ; évaluation des risques ; registre des systèmes d'IA ; transparence

Temps : recherche 32.0 s · génération 1.6 s (3784 tokens lus, 590 écrits, 483.5 tokens/s) · contrôle de pertinence 0.1 s · reformulation 0.2 s · attente des limites de l'API 38 s (non comptée)

## e18 — On a mis un chatbot sur notre site. On doit dire aux visiteurs qu'ils parlent avec une machine ?

Article attendu : AI Act art. 50, paragraphe 1 — passage [1].

### Réponse du copilote

> Oui, vous devez informer les visiteurs qu'ils interagissent avec un système d'IA, à moins que cela ne soit déjà évident pour eux [1]. Cette obligation de transparence vise les fournisseurs de systèmes d'IA destinés à interagir directement avec des personnes physiques [1]. L'exception s'applique uniquement « si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 3 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [3] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14
  [4] AI Act — règlement (UE) 2024/1689, article 13 : Transparence et fourniture d’informations aux déployeurs
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_13
  [5] AI Act — règlement (UE) 2024/1689, annexe III, point 8 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
Attention : La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à moins que cela ne soit déjà évident pour eux [1] ». Vérifiez-la dans les textes.
Attention : La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui, vous devez informer les visiteurs qu'ils interagissent avec un système d'IA, à moins que cela ne soit déjà évident … » (et 1 autre(s)). Vérifiez qui est concerné.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »

RÉPONSE :
Oui, vous devez informer les visiteurs qu'ils interagissent avec un système d'IA, à moins que cela ne soit déjà évident pour eux [1]. Cette obligation de transparence vise les fournisseurs de systèmes d'IA destinés à interagir directement avec des personnes physiques [1]. L'exception s'applique uniquement « si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : obligation d'information ; interaction homme-machine ; transparence ; notification de l'interaction avec un système d'IA

Temps : recherche 34.1 s · génération 0.9 s (3486 tokens lus, 212 écrits, 480.1 tokens/s) · contrôle de pertinence 0.7 s · reformulation 0.4 s

## e19 — Notre organisme de formation veut utiliser une IA pour corriger les examens et noter les stagiaires. C'est risqué ?

Article attendu : AI Act annexe III, point 3 — passage [1].

### Réponse du copilote

> Oui, l'utilisation d'une IA pour corriger les examens et noter les stagiaires est considérée comme un système d'IA à haut risque, car elle entre dans la catégorie des systèmes destinés à « évaluer les acquis d'apprentissage » dans le domaine de l'éducation et de la formation professionnelle [1]. Cette classification signifie que le système doit permettre un « contrôle effectif par des personnes physiques » pendant toute sa période d'utilisation [4]. L'objectif de ce contrôle humain est de « prévenir ou à réduire au minimum les risques pour la santé, la sécurité ou les droits fondamentaux » qui pourraient apparaître lors de l'utilisation du système [4]. En tant que déployeur, vous devez également recevoir des informations requises et, éventuellement, une formation du fournisseur, afin que les risques liés à l'utilisation soient éliminés ou réduits en tenant compte de vos connaissances et du contexte d'utilisation [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « b) systèmes d'IA destinés à être utilisés pour évaluer les acquis d'apprentissage, y compris lorsque ceux-ci sont utilisés pour orienter le processus d'apprentissage de personnes physiques dans les établissements d'enseignement et de formation professionnelle, à tous les niveaux; »
  [1] « Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des domaines suivants: »
  [4] « 1. La conception et le développement des systèmes d’IA à haut risque permettent, notamment au moyen d’interfaces homme-machine appropriées, un contrôle effectif par des personnes physiques pendant leur période d’utilisation. »
  [4] « 2. Le contrôle humain vise à prévenir ou à réduire au minimum les risques pour la santé, la sécurité ou les droits fondamentaux qui peuvent apparaître lorsqu’un système d’IA à haut risque est utilisé conformément à sa destination ou dans des conditions de mauvaise utilisation raisonnablement prévisible, en particulier lorsque de tels risques persistent malgré l’application d’autres exigences énoncées dans la présente section. »
  [3] « c) fournir aux déployeurs les informations requises conformément à l’article 13 et, éventuellement, une formation. »
  [3] « En vue de l’élimination ou de la réduction des risques liés à l’utilisation du système d’IA à haut risque, il est dûment tenu compte des connaissances techniques, de l’expérience, de l’éducation et de la formation pouvant être attendues du déployeur, ainsi que du contexte prévisible dans lequel le système est destiné à être utilisé. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, annexe III, point 3 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [3] AI Act — règlement (UE) 2024/1689, article 9, point c : Système de gestion des risques (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_9
  [4] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, annexe III, point 7 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [5] AI Act — règlement (UE) 2024/1689, article 12 : Enregistrement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_12

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « b) systèmes d'IA destinés à être utilisés pour évaluer les acquis d'apprentissage, y compris lorsque ceux-ci sont utilisés pour orienter le processus d'apprentissage de personnes physiques dans les établissements d'enseignement et de formation professionnelle, à tous les niveaux; »
- [1] « Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des domaines suivants: »
- [4] « 1. La conception et le développement des systèmes d’IA à haut risque permettent, notamment au moyen d’interfaces homme-machine appropriées, un contrôle effectif par des personnes physiques pendant leur période d’utilisation. »
- [4] « 2. Le contrôle humain vise à prévenir ou à réduire au minimum les risques pour la santé, la sécurité ou les droits fondamentaux qui peuvent apparaître lorsqu’un système d’IA à haut risque est utilisé conformément à sa destination ou dans des conditions de mauvaise utilisation raisonnablement prévisible, en particulier lorsque de tels risques persistent malgré l’application d’autres exigences énoncées dans la présente section. »
- [3] « c) fournir aux déployeurs les informations requises conformément à l’article 13 et, éventuellement, une formation. »
- [3] « En vue de l’élimination ou de la réduction des risques liés à l’utilisation du système d’IA à haut risque, il est dûment tenu compte des connaissances techniques, de l’expérience, de l’éducation et de la formation pouvant être attendues du déployeur, ainsi que du contexte prévisible dans lequel le système est destiné à être utilisé. »

RÉPONSE :
Oui, l'utilisation d'une IA pour corriger les examens et noter les stagiaires est considérée comme un système d'IA à haut risque, car elle entre dans la catégorie des systèmes destinés à « évaluer les acquis d'apprentissage » dans le domaine de l'éducation et de la formation professionnelle [1]. Cette classification signifie que le système doit permettre un « contrôle effectif par des personnes physiques » pendant toute sa période d'utilisation [4]. L'objectif de ce contrôle humain est de « prévenir ou à réduire au minimum les risques pour la santé, la sécurité ou les droits fondamentaux » qui pourraient apparaître lors de l'utilisation du système [4]. En tant que déployeur, vous devez également recevoir des informations requises et, éventuellement, une formation du fournisseur, afin que les risques liés à l'utilisation soient éliminés ou réduits en tenant compte de vos connaissances et du contexte d'utilisation [3].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : système d'IA à haut risque ; évaluation des risques ; transparence ; responsabilité ; protection des données à caractère personnel ; biais

Temps : recherche 30.9 s · génération 2.0 s (3231 tokens lus, 570 écrits, 358.2 tokens/s) · contrôle de pertinence 0.6 s · reformulation 0.2 s · attente des limites de l'API 18 s (non comptée)

## e20 — On m'a dit que je dois former mes salariés à l'IA. C'est vraiment obligatoire ?

Article attendu : AI Act art. 4 — passage [1].

### Réponse du copilote

> Oui, si vous êtes un déployeur de systèmes d'IA, vous avez l'obligation de prendre des mesures pour favoriser le développement de la « maîtrise de l'IA » par votre personnel [1]. Cette « maîtrise de l'IA » est définie comme l'ensemble des compétences, connaissances et compréhension permettant de déployer les systèmes en toute connaissance de cause et de prendre conscience des risques [4]. Cependant, cette obligation ne vous contraint pas à garantir un niveau spécifique de maîtrise de l'IA par un individu [1]. Si vous utilisez des systèmes d'IA à haut risque sur le lieu de travail, vous devez également informer les travailleurs concernés de l'utilisation de ces systèmes [2]. De plus, pour ces systèmes à haut risque, vous devez confier le contrôle humain à des personnes qui disposent des compétences, de la formation et de l'autorité nécessaires [5].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les fournisseurs et les déployeurs de systèmes d'IA prennent des mesures pour favoriser le développement de la maîtrise de l'IA par leur personnel et les autres personnes s'occupant du fonctionnement et de l'utilisation des systèmes d'IA pour leur compte, en prenant en considération leurs connaissances techniques, leur expérience, leur éducation et leur formation, ainsi que le contexte dans lequel les systèmes d'IA sont destinés à être utilisés, et en tenant compte des personnes ou des groupes de personnes à l'égard desquels les systèmes d'IA sont destinés à être utilisés. »
  [1] « Cette obligation ne contraint pas les fournisseurs ou les déployeurs à garantir un niveau spécifique de maîtrise de l'IA par un individu. »
  [4] « «maîtrise de l’IA», les compétences, les connaissances et la compréhension qui permettent aux fournisseurs, aux déployeurs et aux personnes concernées, compte tenu de leurs droits et obligations respectifs dans le contexte du présent règlement, de procéder à un déploiement des systèmes d'IA en toute connaissance de cause, ainsi que de prendre conscience des possibilités et des risques que comporte l'IA, ainsi que des préjudices potentiels qu’elle peut causer; »
  [2] « Avant de mettre en service ou d’utiliser un système d’IA à haut risque sur le lieu de travail, les déployeurs qui sont des employeurs informent les représentants des travailleurs et les travailleurs concernés qu’ils seront soumis à l’utilisation du système d’IA à haut risque. »
  [5] « Les déployeurs confient le contrôle humain à des personnes physiques qui disposent des compétences, de la formation et de l’autorité nécessaires ainsi que du soutien nécessaire. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 4 : Maîtrise de l'IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_4
  [2] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 7 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
  [4] AI Act — règlement (UE) 2024/1689, article 3, définition 56 : Définitions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
  [5] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 2 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 1 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les fournisseurs et les déployeurs de systèmes d'IA prennent des mesures pour favoriser le développement de la maîtrise de l'IA par leur personnel et les autres personnes s'occupant du fonctionnement et de l'utilisation des systèmes d'IA pour leur compte, en prenant en considération leurs connaissances techniques, leur expérience, leur éducation et leur formation, ainsi que le contexte dans lequel les systèmes d'IA sont destinés à être utilisés, et en tenant compte des personnes ou des groupes de personnes à l'égard desquels les systèmes d'IA sont destinés à être utilisés. »
- [1] « Cette obligation ne contraint pas les fournisseurs ou les déployeurs à garantir un niveau spécifique de maîtrise de l'IA par un individu. »
- [4] « «maîtrise de l’IA», les compétences, les connaissances et la compréhension qui permettent aux fournisseurs, aux déployeurs et aux personnes concernées, compte tenu de leurs droits et obligations respectifs dans le contexte du présent règlement, de procéder à un déploiement des systèmes d'IA en toute connaissance de cause, ainsi que de prendre conscience des possibilités et des risques que comporte l'IA, ainsi que des préjudices potentiels qu’elle peut causer; »
- [2] « Avant de mettre en service ou d’utiliser un système d’IA à haut risque sur le lieu de travail, les déployeurs qui sont des employeurs informent les représentants des travailleurs et les travailleurs concernés qu’ils seront soumis à l’utilisation du système d’IA à haut risque. »
- [5] « Les déployeurs confient le contrôle humain à des personnes physiques qui disposent des compétences, de la formation et de l’autorité nécessaires ainsi que du soutien nécessaire. »

RÉPONSE :
Oui, si vous êtes un déployeur de systèmes d'IA, vous avez l'obligation de prendre des mesures pour favoriser le développement de la « maîtrise de l'IA » par votre personnel [1]. Cette « maîtrise de l'IA » est définie comme l'ensemble des compétences, connaissances et compréhension permettant de déployer les systèmes en toute connaissance de cause et de prendre conscience des risques [4]. Cependant, cette obligation ne vous contraint pas à garantir un niveau spécifique de maîtrise de l'IA par un individu [1]. Si vous utilisez des systèmes d'IA à haut risque sur le lieu de travail, vous devez également informer les travailleurs concernés de l'utilisation de ces systèmes [2]. De plus, pour ces systèmes à haut risque, vous devez confier le contrôle humain à des personnes qui disposent des compétences, de la formation et de l'autorité nécessaires [5].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : formation du personnel ; compétences en matière d'IA ; sensibilisation ; formation des opérateurs

Temps : recherche 30.9 s · génération 1.9 s (1979 tokens lus, 568 écrits, 383.4 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.5 s · attente des limites de l'API 15 s (non comptée)

## e21 — On crée nos visuels pour les réseaux sociaux avec une IA. Il faut écrire qu'ils sont générés par IA ?

Article attendu : AI Act art. 50, paragraphe 4 — passage [1].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 4 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [3] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 2 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [4] AI Act — règlement (UE) 2024/1689, article 3, définition 60 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
  [5] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points a) à e) : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

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
Oui, vous devez indiquer que vos visuels sont générés par une IA, mais cette obligation ne s'applique que si ces visuels constituent un « hypertrucage » [1]. Un hypertrucage est défini comme une image générée ou manipulée par l'IA qui présente une ressemblance avec des éléments existants et peut être perçue à tort comme authentique [4]. Si vos visuels font partie d'une œuvre manifestement artistique, créative, satirique, fictive ou analogue, l'obligation se limite à la « divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre » [1]. Cette obligation ne s'applique pas « lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : contenus générés artificiellement ; obligation de transparence ; étiquetage des contenus synthétiques ; information des personnes

Temps : recherche 28.9 s · génération 1.4 s (3025 tokens lus, 483 écrits, 546.3 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.2 s · attente des limites de l'API 26 s (non comptée)

## e22 — Un fournisseur nous propose un outil qui analyse les émotions des salariés pendant les visioconférences. On a le droit de l'utiliser ?

Article attendu : AI Act art. 5, paragraphe 1_f h — passage [3].

### Réponse du copilote

> Non, vous n'avez pas le droit d'utiliser cet outil pour analyser les émotions de vos salariés, car l'AI Act interdit « l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail » [3]. Cette interdiction comporte une exception « sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité » [3]. Si votre outil ne répond pas à ces conditions strictes, son utilisation est prohibée. Par ailleurs, les systèmes de reconnaissance des émotions sont classés comme des systèmes d'IA à haut risque [4], ce qui implique des obligations de transparence pour les déployeurs, notamment l'information des personnes exposées et le traitement des données conformément au RGPD [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « f) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement, sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité; »
  [1] « Les déployeurs d’un système de reconnaissance des émotions ou d’un système de catégorisation biométrique informent les personnes physiques qui y sont exposées du fonctionnement du système et traitent les données à caractère personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680, selon le cas. »
  [1] « Cette obligation ne s’applique pas aux systèmes d’IA utilisés pour la catégorisation biométrique et la reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l’Union. »
  [4] « c) systèmes d’IA destinés à être utilisés pour la reconnaissance des émotions. »
  [5] « 39) «système de reconnaissance des émotions», un système d’IA permettant la reconnaissance ou la déduction des émotions ou des intentions de personnes physiques sur la base de leurs données biométriques; »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 3 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [3] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points f) à h) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [4] AI Act — règlement (UE) 2024/1689, annexe III, point 1 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [5] AI Act — règlement (UE) 2024/1689, article 3, définition 39 : Définitions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [3] « f) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail et dans les établissements d’enseignement, sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité; »
- [1] « Les déployeurs d’un système de reconnaissance des émotions ou d’un système de catégorisation biométrique informent les personnes physiques qui y sont exposées du fonctionnement du système et traitent les données à caractère personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680, selon le cas. »
- [1] « Cette obligation ne s’applique pas aux systèmes d’IA utilisés pour la catégorisation biométrique et la reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l’Union. »
- [4] « c) systèmes d’IA destinés à être utilisés pour la reconnaissance des émotions. »
- [5] « 39) «système de reconnaissance des émotions», un système d’IA permettant la reconnaissance ou la déduction des émotions ou des intentions de personnes physiques sur la base de leurs données biométriques; »

RÉPONSE :
Non, vous n'avez pas le droit d'utiliser cet outil pour analyser les émotions de vos salariés, car l'AI Act interdit « l’utilisation de systèmes d’IA pour inférer les émotions d’une personne physique sur le lieu de travail » [3]. Cette interdiction comporte une exception « sauf lorsque l’utilisation du système d’IA est destinée à être mise en place ou mise sur le marché pour des raisons médicales ou de sécurité » [3]. Si votre outil ne répond pas à ces conditions strictes, son utilisation est prohibée. Par ailleurs, les systèmes de reconnaissance des émotions sont classés comme des systèmes d'IA à haut risque [4], ce qui implique des obligations de transparence pour les déployeurs, notamment l'information des personnes exposées et le traitement des données conformément au RGPD [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : analyse des émotions ; biométrie ; données biométriques ; système de catégorisation biométrique ; consentement ; finalité

Temps : recherche 31.4 s · génération 2.8 s (2524 tokens lus, 536 écrits, 476.0 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.2 s · attente des limites de l'API 15 s (non comptée)

## e23 — Si l'outil d'IA qu'on a acheté se trompe et écarte injustement un candidat, qui est responsable : moi ou le fournisseur ?

Article attendu : RGPD art. 82 ou AI Act art. 26 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question concernant la responsabilité pour un préjudice causé lors de l'utilisation normale d'un outil d'IA acheté, mais seulement pour les « essais en conditions réelles » [1].
> Selon l'AI Act, le « fournisseur » est défini comme l'organisme qui développe le système et le met sur le marché sous son propre nom [3].
> Vous n'êtes considéré comme un fournisseur, et donc soumis aux obligations spécifiques du fournisseur, que si vous commercialisez l'outil sous votre propre nom, si vous apportez une modification substantielle, ou si vous modifiez sa destination pour en faire un système à haut risque [5].
> Si vous êtes simplement un utilisateur (déployeur) qui achète l'outil sans le modifier ni le revendre sous votre marque, les extraits fournis ne précisent pas qui est responsable du préjudice causé par une erreur de l'outil dans ce contexte, car l'article 60, paragraphe 9, limite explicitement la responsabilité mentionnée aux « essais en conditions réelles » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le fournisseur ou le fournisseur potentiel sont responsables, en vertu du droit de l’Union et du droit national applicable en matière de responsabilité, de tout préjudice causé durant les essais en conditions réelles. »
  [3] « «fournisseur», une personne physique ou morale, une autorité publique, une agence ou tout autre organisme qui développe ou fait développer un système d’IA ou un modèle d’IA à usage général et le met sur le marché ou met le système d’IA en service sous son propre nom ou sa propre marque, à titre onéreux ou gratuit; »
  [5] « Tout distributeur, importateur, déployeur ou autre tiers est considéré comme un fournisseur d’un système d’IA à haut risque aux fins du présent règlement et est soumis aux obligations incombant au fournisseur au titre de l’article 16 dans toutes les circonstances suivantes: »
  [5] « a) il commercialise sous son propre nom ou sa propre marque un système d’IA à haut risque déjà mis sur le marché ou mis en service, sans préjudice des dispositions contractuelles prévoyant une autre répartition des obligations; »
  [5] « b) il apporte une modification substantielle à un système d’IA à haut risque qui a déjà été mis sur le marché ou a déjà été mis en service de telle manière qu’il reste un système d’IA à haut risque en application de l’article 6; »
  [5] « c) il modifie la destination d’un système d’IA, y compris un système d’IA à usage général, qui n’a pas été classé à haut risque et a déjà été mis sur le marché ou mis en service de telle manière que le système d’IA concerné devient un système d’IA à haut risque conformément l’article 6. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 60, paragraphe 9 : Essais de systèmes d’IA à haut risque en conditions réelles en dehors des bacs à sable réglementaires de l’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_60
  [3] AI Act — règlement (UE) 2024/1689, article 3, définition 3 : Définitions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
  [5] AI Act — règlement (UE) 2024/1689, article 25, paragraphe 1 : Responsabilités tout au long de la chaîne de valeur de l’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_25
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 60, paragraphe 1 : Essais de systèmes d’IA à haut risque en conditions réelles en dehors des bacs à sable réglementaires de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_60
  [4] AI Act — règlement (UE) 2024/1689, article 25, paragraphe 4 : Responsabilités tout au long de la chaîne de valeur de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_25
Attention : La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Les passages trouvés ne traitent pas directement de votre question concernant la responsabilité pour un préjudice causé … » (et 1 autre(s)). Vérifiez qui est concerné.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le fournisseur ou le fournisseur potentiel sont responsables, en vertu du droit de l’Union et du droit national applicable en matière de responsabilité, de tout préjudice causé durant les essais en conditions réelles. »
- [3] « «fournisseur», une personne physique ou morale, une autorité publique, une agence ou tout autre organisme qui développe ou fait développer un système d’IA ou un modèle d’IA à usage général et le met sur le marché ou met le système d’IA en service sous son propre nom ou sa propre marque, à titre onéreux ou gratuit; »
- [5] « Tout distributeur, importateur, déployeur ou autre tiers est considéré comme un fournisseur d’un système d’IA à haut risque aux fins du présent règlement et est soumis aux obligations incombant au fournisseur au titre de l’article 16 dans toutes les circonstances suivantes: »
- [5] « a) il commercialise sous son propre nom ou sa propre marque un système d’IA à haut risque déjà mis sur le marché ou mis en service, sans préjudice des dispositions contractuelles prévoyant une autre répartition des obligations; »
- [5] « b) il apporte une modification substantielle à un système d’IA à haut risque qui a déjà été mis sur le marché ou a déjà été mis en service de telle manière qu’il reste un système d’IA à haut risque en application de l’article 6; »
- [5] « c) il modifie la destination d’un système d’IA, y compris un système d’IA à usage général, qui n’a pas été classé à haut risque et a déjà été mis sur le marché ou mis en service de telle manière que le système d’IA concerné devient un système d’IA à haut risque conformément l’article 6. »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question concernant la responsabilité pour un préjudice causé lors de l'utilisation normale d'un outil d'IA acheté, mais seulement pour les « essais en conditions réelles » [1].
Selon l'AI Act, le « fournisseur » est défini comme l'organisme qui développe le système et le met sur le marché sous son propre nom [3].
Vous n'êtes considéré comme un fournisseur, et donc soumis aux obligations spécifiques du fournisseur, que si vous commercialisez l'outil sous votre propre nom, si vous apportez une modification substantielle, ou si vous modifiez sa destination pour en faire un système à haut risque [5].
Si vous êtes simplement un utilisateur (déployeur) qui achète l'outil sans le modifier ni le revendre sous votre marque, les extraits fournis ne précisent pas qui est responsable du préjudice causé par une erreur de l'outil dans ce contexte, car l'article 60, paragraphe 9, limite explicitement la responsabilité mentionnée aux « essais en conditions réelles » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : fournisseur du modèle de fond ; fournisseur du système d'IA ; responsable de l'IA ; utilisateur professionnel ; opérateur

Temps : recherche 27.0 s · génération 1.6 s (2298 tokens lus, 636 écrits, 515.3 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.2 s · attente des limites de l'API 28 s (non comptée)

## e24 — À partir de quand les règles de l'AI Act s'appliquent vraiment ? Qu'est-ce qui est déjà en vigueur ?

Article attendu : AI Act art. 113 — passage [1].

### Réponse du copilote

> L'AI Act est applicable dans son ensemble à partir du 2 août 2026 [1]. Cependant, certaines parties sont déjà en vigueur ou le seront avant cette date : les chapitres I et II s'appliquent à partir du 2 février 2025, « à l'exception de l'article 5, paragraphe 1, premier alinéa, points b bis) et b ter), et de l'article 5, paragraphes 1 bis et 1 ter, qui s'appliquent à partir du 2 décembre 2026 » [1]. De plus, le chapitre III (section 4), le chapitre V, le chapitre VII, le chapitre XII et l’article 78 s'appliquent à partir du 2 août 2025, « à l'exception de l’article 101 » [1]. Les règles relatives aux systèmes d'IA à haut risque (chapitre III, sections 1, 2 et 3) s'appliquent à des dates ultérieures : « du 2 décembre 2027 en ce qui concerne les systèmes d'IA classés comme étant à haut risque en vertu de l'article 6, paragraphe 2, et de l'annexe III » et « du 2 août 2028 en ce qui concerne les systèmes d'IA classés à haut risque en vertu de l'article 6, paragraphe 1, et de l'annexe I » [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Il est applicable à partir du 2 août 2026. »
  [1] « a) les chapitres I et II s'appliquent à partir du 2 février 2025, à l'exception de l'article 5, paragraphe 1, premier alinéa, points b bis) et b ter), et de l'article 5, paragraphes 1 bis et 1 ter, qui s'appliquent à partir du 2 décembre 2026; »
  [1] « b) le chapitre III, section 4, le chapitre V, le chapitre VII, le chapitre XII et l’article 78 s’appliquent à partir du 2 août 2025, à l’exception de l’article 101; »
  [1] « c) le chapitre III, sections 1, 2 et 3, à l'exception de l'article 6, paragraphe 5, s'applique à partir: »
  [1] « i) du 2 décembre 2027 en ce qui concerne les systèmes d'IA classés comme étant à haut risque en vertu de l'article 6, paragraphe 2, et de l'annexe III; et »
  [1] « ii) du 2 août 2028 en ce qui concerne les systèmes d'IA classés à haut risque en vertu de l'article 6, paragraphe 1, et de l'annexe I; »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 113 : Entrée en vigueur et application (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_113
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 2, paragraphe 13 : Champ d’application
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_2
  [3] AI Act — règlement (UE) 2024/1689, article 111 : Systèmes d’IA déjà mis sur le marché ou mis en service et modèles d’IA à usage général déjà mis sur le marché
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_111
  [4] AI Act — règlement (UE) 2024/1689, article 2, paragraphe 1 : Champ d’application
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_2
  [5] AI Act — règlement (UE) 2024/1689, article 57, paragraphe 1 : Bacs à sable réglementaires de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_57

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Il est applicable à partir du 2 août 2026. »
- [1] « a) les chapitres I et II s'appliquent à partir du 2 février 2025, à l'exception de l'article 5, paragraphe 1, premier alinéa, points b bis) et b ter), et de l'article 5, paragraphes 1 bis et 1 ter, qui s'appliquent à partir du 2 décembre 2026; »
- [1] « b) le chapitre III, section 4, le chapitre V, le chapitre VII, le chapitre XII et l’article 78 s’appliquent à partir du 2 août 2025, à l’exception de l’article 101; »
- [1] « c) le chapitre III, sections 1, 2 et 3, à l'exception de l'article 6, paragraphe 5, s'applique à partir: »
- [1] « i) du 2 décembre 2027 en ce qui concerne les systèmes d'IA classés comme étant à haut risque en vertu de l'article 6, paragraphe 2, et de l'annexe III; et »
- [1] « ii) du 2 août 2028 en ce qui concerne les systèmes d'IA classés à haut risque en vertu de l'article 6, paragraphe 1, et de l'annexe I; »

RÉPONSE :
L'AI Act est applicable dans son ensemble à partir du 2 août 2026 [1]. Cependant, certaines parties sont déjà en vigueur ou le seront avant cette date : les chapitres I et II s'appliquent à partir du 2 février 2025, « à l'exception de l'article 5, paragraphe 1, premier alinéa, points b bis) et b ter), et de l'article 5, paragraphes 1 bis et 1 ter, qui s'appliquent à partir du 2 décembre 2026 » [1]. De plus, le chapitre III (section 4), le chapitre V, le chapitre VII, le chapitre XII et l’article 78 s'appliquent à partir du 2 août 2025, « à l'exception de l’article 101 » [1]. Les règles relatives aux systèmes d'IA à haut risque (chapitre III, sections 1, 2 et 3) s'appliquent à des dates ultérieures : « du 2 décembre 2027 en ce qui concerne les systèmes d'IA classés comme étant à haut risque en vertu de l'article 6, paragraphe 2, et de l'annexe III » et « du 2 août 2028 en ce qui concerne les systèmes d'IA classés à haut risque en vertu de l'article 6, paragraphe 1, et de l'annexe I » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : date d'entrée en vigueur ; date d'application ; dispositions transitoires ; obligations applicables

Temps : recherche 26.8 s · génération 1.8 s (2830 tokens lus, 673 écrits, 468.5 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.2 s · attente des limites de l'API 30 s (non comptée)

## e25 — Mes salariés copient des données clients dans ChatGPT pour aller plus vite. C'est un problème ? Comment je peux encadrer ça ?

Article attendu : RGPD art. 32 ou RGPD art. 29 — passage [1].

### Réponse du copilote

> Oui, c'est un problème car vous devez garantir un niveau de sécurité adapté au risque pour les données que vous traitez [1]. Vos salariés, qui agissent sous votre autorité, ne doivent traiter les données à caractère personnel qu'« excepté sur instruction du responsable du traitement » [1]. Si vous utilisez ChatGPT, le fournisseur de l'outil agit comme sous-traitant et son traitement doit être régi par un contrat qui le lie à votre égard [4]. Ce contrat doit prévoir que le sous-traitant « ne traite les données à caractère personnel que sur instruction documentée du responsable du traitement » et qu'il « prend toutes les mesures requises en vertu de l'article 32 » [4]. Pour encadrer cela, vous devez mettre en œuvre des mesures techniques et organisationnelles appropriées, notamment des moyens garantissant la confidentialité des systèmes [1], et vous assurer que le traitement par le sous-traitant respecte ces exigences via un contrat conforme [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « le responsable du traitement et le sous-traitant mettent en œuvre les mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque »
  [1] « des moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement »
  [1] « Le responsable du traitement et le sous-traitant prennent des mesures afin de garantir que toute personne physique agissant sous l'autorité du responsable du traitement ou sous celle du sous-traitant, qui a accès à des données à caractère personnel, ne les traite pas, excepté sur instruction du responsable du traitement, à moins d'y être obligée par le droit de l'Union ou le droit d'un État membre. »
  [4] « Le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre, qui lie le sous-traitant à l'égard du responsable du traitement »
  [4] « ne traite les données à caractère personnel que sur instruction documentée du responsable du traitement, y compris en ce qui concerne les transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale »
  [4] « prend toutes les mesures requises en vertu de l'article 32 »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 32 : Sécurité du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_32
  [4] RGPD — règlement (UE) 2016/679, article 28, paragraphe 3 : Sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [3] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [5] RGPD — règlement (UE) 2016/679, article 28, paragraphe 1 : Sous-traitant
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « le responsable du traitement et le sous-traitant mettent en œuvre les mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque »
- [1] « des moyens permettant de garantir la confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes et des services de traitement »
- [1] « Le responsable du traitement et le sous-traitant prennent des mesures afin de garantir que toute personne physique agissant sous l'autorité du responsable du traitement ou sous celle du sous-traitant, qui a accès à des données à caractère personnel, ne les traite pas, excepté sur instruction du responsable du traitement, à moins d'y être obligée par le droit de l'Union ou le droit d'un État membre. »
- [4] « Le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre, qui lie le sous-traitant à l'égard du responsable du traitement »
- [4] « ne traite les données à caractère personnel que sur instruction documentée du responsable du traitement, y compris en ce qui concerne les transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale »
- [4] « prend toutes les mesures requises en vertu de l'article 32 »

RÉPONSE :
Oui, c'est un problème car vous devez garantir un niveau de sécurité adapté au risque pour les données que vous traitez [1]. Vos salariés, qui agissent sous votre autorité, ne doivent traiter les données à caractère personnel qu'« excepté sur instruction du responsable du traitement » [1]. Si vous utilisez ChatGPT, le fournisseur de l'outil agit comme sous-traitant et son traitement doit être régi par un contrat qui le lie à votre égard [4]. Ce contrat doit prévoir que le sous-traitant « ne traite les données à caractère personnel que sur instruction documentée du responsable du traitement » et qu'il « prend toutes les mesures requises en vertu de l'article 32 » [4]. Pour encadrer cela, vous devez mettre en œuvre des mesures techniques et organisationnelles appropriées, notamment des moyens garantissant la confidentialité des systèmes [1], et vous assurer que le traitement par le sous-traitant respecte ces exigences via un contrat conforme [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : traitement de données à caractère personnel ; responsable du traitement ; sous-traitant ; mesures techniques et organisationnelles appropriées ; transfert de données hors de l'Union européenne ; consentement de la personne concernée

Temps : recherche 29.0 s · génération 1.5 s (3359 tokens lus, 507 écrits, 459.6 tokens/s) · contrôle de pertinence 0.1 s · reformulation 1.9 s · attente des limites de l'API 14 s (non comptée)

## he01 — Comment je déclare la TVA chaque trimestre ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 97 : Rapports de la Commission
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_97
  [2] RGPD — règlement (UE) 2016/679, article 27 : Représentants des responsables du traitement ou des sous-traitants qui ne sont pas établis dans l'Union
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_27
  [3] RGPD — règlement (UE) 2016/679, article 83, paragraphe 5 : Conditions générales pour imposer des amendes administratives
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83
  [4] RGPD — règlement (UE) 2016/679, article 83, paragraphe 1 : Conditions générales pour imposer des amendes administratives
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_83
  [5] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : déclaration de TVA ; période d'imposition ; assujetti ; base d'imposition ; taux de TVA

Temps : recherche 27.2 s · génération 0.4 s (2544 tokens lus, 25 écrits, 195.5 tokens/s) · reformulation 0.4 s · attente des limites de l'API 6 s (non comptée)

## he02 — Si un salarié en CDI démissionne, combien de temps dure son préavis ?

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
  [3] RGPD — règlement (UE) 2016/679, article 12, paragraphe 4 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [4] RGPD — règlement (UE) 2016/679, article 66 : Procédure d'urgence
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_66
  [5] RGPD — règlement (UE) 2016/679, article 64, paragraphe 7 : Avis du comité
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_64

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : préavis de démission ; contrat à durée indéterminée ; période de préavis

Temps : recherche 29.3 s · génération 0.4 s (2247 tokens lus, 25 écrits, 448.6 tokens/s) · reformulation 0.3 s

## he03 — Tu as des idées pour organiser une fête de fin d'année pour les bénévoles avec un petit budget ?

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
  [3] RGPD — règlement (UE) 2016/679, article 66 : Procédure d'urgence
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_66
  [4] RGPD — règlement (UE) 2016/679, article 57, paragraphe 3 : Missions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_57
  [5] RGPD — règlement (UE) 2016/679, article 57, paragraphe 1, points a) à t) : Missions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_57

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Temps : recherche 25.8 s · génération 0.4 s (3019 tokens lus, 25 écrits, 452.2 tokens/s) · reformulation 0.2 s
