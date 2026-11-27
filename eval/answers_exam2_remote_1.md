# Réponses du copilote — exam2_remote_1

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 24/11/2026 à 16:13 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen/qwen3.8-27b` via l'API compatible OpenAI https://api.groq.com/openai/v1 (expérience de la séance 7, questions de test seulement ; modèle tel que servi par l'API à la date ci-dessus) — température 0.1, raisonnement : réglage par défaut du modèle, passages calculés pour un contexte de 8192 tokens comme en local, 2000 tokens au plus par réponse (raisonnement compris) ; le juge est le même modèle
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu, reranker `BAAI/bge-reranker-v2-m3` sur CPU (20 candidats reclassés avant la limite par article), reformulation de la question par le modèle avant la recherche (termes juridiques ajoutés, sans conclusion)
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_exam2.jsonl` (24 + 4 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| e01 | Je veux installer des caméras dans mon magasin et dans la salle de pause. J'en ai le droit ? Qu'est-ce que je dois dire à mes salariés ? | 5/6 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 61 s |
| e02 | Une ancienne cliente me demande d'effacer toutes ses données. On doit garder ses factures pour la comptabilité. Je dois quand même tout supprimer ? | 5/6 | non | 1 passage(s) retiré(s) faute de place dans le contexte du modèle (LLM_NUM_CTX = 8192).; 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([5]) : ignoré(s).; Citation vers un passage inexistant : [5] (seuls les passages [1] à [4] ont été fournis).; La réponse met entre « » un texte introuvable dans les extraits vérifiés : « pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées ».; La réponse ne reprend que 2 des 6 cas énumérés au passage [1], sans dire qu'elle n'en cite qu'une partie. Vérifiez la liste complète. | 29 s |
| e03 | Combien de temps je peux garder les CV des candidats que je n'ai pas retenus ? | 3/3 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 30 s |
| e04 | Notre association garde la liste des bénévoles (adresses, téléphones) dans un fichier Excel partagé sur Google Drive. C'est un problème ? | 6/6 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 29 s |
| e05 | Sur mon site web, j'utilise seulement Google Analytics. Je suis obligé de mettre un bandeau cookies ? | 0/0 | oui | — | 26 s |
| e06 | La boîte mail de l'accueil a été piratée hier. Qu'est-ce que je dois faire ? Je dois prévenir quelqu'un ? | 6/6 | non | — | 40 s |
| e07 | Un prestataire extérieur gère notre paie. Je dois signer un contrat spécial avec lui pour les données ? | 6/6 | non | — | 31 s |
| e08 | Je peux envoyer notre newsletter à mes anciens clients sans leur demander leur accord ? | 6/6 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 30 s |
| e09 | Un salarié me demande une copie de toutes les données que j'ai sur lui, même les mails où on parle de lui. Je dois tout lui donner ? J'ai combien de temps pour répondre ? | 6/6 | non | — | 29 s |
| e10 | Un salarié est parti de l'entreprise. Je peux encore lire sa boîte mail professionnelle ? | 0/0 | oui | — | 27 s |
| e11 | Dans notre organisme de formation, on demande aux stagiaires leur numéro de sécurité sociale et des informations sur leur handicap. On a le droit ? | 6/6 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 31 s |
| e12 | Je peux suivre les véhicules de mes techniciens par GPS ? | 6/6 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 30 s |
| e13 | On veut publier sur Facebook des photos des bénévoles prises pendant notre fête annuelle. Il faut leur accord écrit ? | 4/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 34 s |
| e14 | On a 8 salariés. On doit tenir un registre des traitements et nommer un DPO ? | 6/6 | non | La réponse met entre « » un texte introuvable dans les extraits vérifiés : « pouvez désigner ou, si le droit de l'Union ou le droit d'un État membre l'exige, sont tenus de désigner un délégué à la … ». | 31 s |
| e15 | Notre logiciel de gestion des clients est hébergé aux États-Unis. C'est autorisé ? | 6/6 | non | — | 29 s |
| e16 | On ne crée pas d'IA, on utilise juste des outils comme ChatGPT. Est-ce que l'AI Act nous concerne quand même ? | 6/6 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 30 s |
| e17 | Je voudrais utiliser un logiciel d'IA qui trie automatiquement les CV. C'est interdit ? Sinon, quelles règles je dois respecter ? | 4/4 | non | La réponse cite [1], [2] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations. | 28 s |
| e18 | On a mis un chatbot sur notre site. On doit dire aux visiteurs qu'ils parlent avec une machine ? | 1/1 | non | La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à moins que cela ne soit déjà évident pour eux [1] ». Vérifiez-la dans les textes.; La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui, vous devez informer les visiteurs qu'ils interagissent avec un système d'IA, à moins que cela ne soit déjà évident … » (et 2 autre(s)). Vérifiez qui est concerné. | 29 s |
| e19 | Notre organisme de formation veut utiliser une IA pour corriger les examens et noter les stagiaires. C'est risqué ? | 5/5 | non | — | 41 s |
| e20 | On m'a dit que je dois former mes salariés à l'IA. C'est vraiment obligatoire ? | 5/5 | non | — | 29 s |
| e21 | On crée nos visuels pour les réseaux sociaux avec une IA. Il faut écrire qu'ils sont générés par IA ? | 4/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 26 s |
| e22 | Un fournisseur nous propose un outil qui analyse les émotions des salariés pendant les visioconférences. On a le droit de l'utiliser ? | 4/4 | non | — | 27 s |
| e23 | Si l'outil d'IA qu'on a acheté se trompe et écarte injustement un candidat, qui est responsable : moi ou le fournisseur ? | 6/6 | non | — | 25 s |
| e24 | À partir de quand les règles de l'AI Act s'appliquent vraiment ? Qu'est-ce qui est déjà en vigueur ? | 6/6 | non | — | 28 s |
| e25 | Mes salariés copient des données clients dans ChatGPT pour aller plus vite. C'est un problème ? Comment je peux encadrer ça ? | 6/6 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 31 s |
| he01 | Comment je déclare la TVA chaque trimestre ? | 0/0 | oui | — | 29 s |
| he02 | Si un salarié en CDI démissionne, combien de temps dure son préavis ? | 0/0 | oui | — | 25 s |
| he03 | Tu as des idées pour organiser une fête de fin d'année pour les bénévoles avec un petit budget ? | 0/0 | oui | — | 24 s |

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
Les passages trouvés ne traitent pas directement de votre question concernant le droit d'installer des caméras ou les conditions spécifiques de leur mise en place. Ils précisent uniquement les obligations d'information et d'analyse d'impact qui s'appliquent si vous traitez des données personnelles.

En tant que responsable du traitement, vous devez fournir aux personnes concernées (vos salariés) des informations sur le traitement de leurs données [1]. Ces informations doivent inclure « les finalités du traitement » [1], « les catégories de données à caractère personnel concernées » [1], « les destinataires ou catégories de destinataires auxquels les données à caractère personnel ont été ou seront communiquées » [1], ainsi que « la durée de conservation des données à caractère personnel envisagée ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée » [1].

De plus, si l'installation de caméras est « susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques », vous devez effectuer « avant le traitement, une analyse de l'impact des opérations de traitement envisagées sur la protection des données à caractère personnel » [3].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : vidéosurveillance ; information des personnes concernées ; registre des traitements ; consultation des représentants du personnel ; finalité du traitement ; durée de conservation

Temps : recherche 58.1 s · génération 1.6 s (2344 tokens lus, 539 écrits, 432.2 tokens/s) · contrôle de pertinence 0.3 s · reformulation 0.8 s

## e02 — Une ancienne cliente me demande d'effacer toutes ses données. On doit garder ses factures pour la comptabilité. Je dois quand même tout supprimer ?

Article attendu : RGPD art. 17 — passage [1].

### Réponse du copilote

> Non, vous n'êtes pas obligé de supprimer toutes les données si leur conservation est requise par une obligation légale, comme la comptabilité. Le droit à l'effacement (RGPD, article 17) s'applique lorsque les données « ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées » [1], mais il ne s'applique pas « dans la mesure où ce traitement est nécessaire » « pour respecter une obligation légale qui requiert le traitement prévue par le droit de l'Union ou par le droit de l'État membre » [1]. Vous devez donc conserver les factures le temps nécessaire pour respecter vos obligations comptables, conformément au principe de limitation de la conservation qui impose de ne conserver les données que « pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées » [5].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « La personne concernée a le droit d'obtenir du responsable du traitement l'effacement, dans les meilleurs délais, de données à caractère personnel la concernant et le responsable du traitement a l'obligation d'effacer ces données à caractère personnel dans les meilleurs délais, lorsque l'un des motifs suivants s'applique: »
  [1] « a) les données à caractère personnel ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées d'une autre manière; »
  [1] « e) les données à caractère personnel doivent être effacées pour respecter une obligation légale qui est prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis; »
  [1] « Les paragraphes 1 et 2 ne s'appliquent pas dans la mesure où ce traitement est nécessaire: »
  [1] « b) pour respecter une obligation légale qui requiert le traitement prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis, ou pour exécuter une mission d'intérêt public ou relevant de l'exercice de l'autorité publique dont est investi le responsable du traitement; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 17 : Droit à l'effacement («droit à l'oubli») (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_17
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [3] RGPD — règlement (UE) 2016/679, article 18 : Droit à la limitation du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_18
  [4] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
Attention : 1 passage(s) retiré(s) faute de place dans le contexte du modèle (LLM_NUM_CTX = 8192).
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([5]) : ignoré(s).
Attention : Citation vers un passage inexistant : [5] (seuls les passages [1] à [4] ont été fournis).
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées ».
Attention : La réponse ne reprend que 2 des 6 cas énumérés au passage [1], sans dire qu'elle n'en cite qu'une partie. Vérifiez la liste complète.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « La personne concernée a le droit d'obtenir du responsable du traitement l'effacement, dans les meilleurs délais, de données à caractère personnel la concernant et le responsable du traitement a l'obligation d'effacer ces données à caractère personnel dans les meilleurs délais, lorsque l'un des motifs suivants s'applique: »
- [1] « a) les données à caractère personnel ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées d'une autre manière; »
- [1] « e) les données à caractère personnel doivent être effacées pour respecter une obligation légale qui est prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis; »
- [1] « Les paragraphes 1 et 2 ne s'appliquent pas dans la mesure où ce traitement est nécessaire: »
- [1] « b) pour respecter une obligation légale qui requiert le traitement prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis, ou pour exécuter une mission d'intérêt public ou relevant de l'exercice de l'autorité publique dont est investi le responsable du traitement; »
- [5] « conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées; »

RÉPONSE :
Non, vous n'êtes pas obligé de supprimer toutes les données si leur conservation est requise par une obligation légale, comme la comptabilité. Le droit à l'effacement (RGPD, article 17) s'applique lorsque les données « ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées » [1], mais il ne s'applique pas « dans la mesure où ce traitement est nécessaire » « pour respecter une obligation légale qui requiert le traitement prévue par le droit de l'Union ou par le droit de l'État membre » [1]. Vous devez donc conserver les factures le temps nécessaire pour respecter vos obligations comptables, conformément au principe de limitation de la conservation qui impose de ne conserver les données que « pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées » [5].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit à l'effacement ; obligation de conservation ; données à caractère personnel ; finalité

Temps : recherche 26.0 s · génération 2.0 s (3394 tokens lus, 507 écrits, 368.1 tokens/s) · contrôle de pertinence 0.1 s · reformulation 0.6 s

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
  [3] RGPD — règlement (UE) 2016/679, article 18 : Droit à la limitation du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_18
  [4] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 3 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
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
Vous devez conserver les CV des candidats non retenus pendant une durée « n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées » [1]. Les passages trouvés ne traitent pas directement de votre question en ce qu'ils ne précisent pas de délai concret (en jours ou en mois) applicable spécifiquement aux CV de recrutement, mais ils indiquent que vous devez informer les candidats de « la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée » [2]. Une conservation plus longue est possible uniquement « dans la mesure où elles seront traitées exclusivement à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques » et sous réserve de mesures appropriées [1]. Les règles concrètes de durée peuvent venir d'autres textes, comme le droit national ou les recommandations de la CNIL.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : durée de conservation des données à caractère personnel ; données relatives à des candidats à un emploi ; principe de limitation du stockage

Temps : recherche 28.2 s · génération 1.4 s (3477 tokens lus, 385 écrits, 455.7 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.3 s

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
- [1] « Compte tenu de la nature, de la portée, du contexte et des finalités du traitement ainsi que des risques, dont le degré de probabilité et de gravité varie, pour les droits et libertés des personnes physiques, le responsable du traitement met en œuvre des mesures techniques et organisationnelles appropriées pour s'assurer et être en mesure de démontrer que le traitement est effectué conformément au présent règlement. »
- [5] « Les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10. »
- [5] « Chaque responsable du traitement et, le cas échéant, le représentant du responsable du traitement tiennent un registre des activités de traitement effectuées sous leur responsabilité. »
- [4] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: »
- [4] « Le responsable du traitement fournit une copie des données à caractère personnel faisant l'objet d'un traitement. »
- [1] « Ces mesures sont réexaminées et actualisées si nécessaire. »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question concernant la légalité spécifique de l'utilisation de Google Drive ou de fichiers Excel partagés, mais ils définissent les obligations générales qui s'appliquent à votre association en tant que responsable du traitement. Vous devez mettre en œuvre des « mesures techniques et organisationnelles appropriées » pour protéger les données, compte tenu des risques pour les droits et libertés des personnes [1]. Ces mesures doivent être « réexaminées et actualisées si nécessaire » [1]. Concernant le registre des activités de traitement, l'obligation de le tenir ne s'applique pas à votre association si vous comptez moins de 250 employés, « sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 » [5]. Si ces conditions d'exception ne sont pas remplies, vous n'avez pas l'obligation de tenir ce registre [5]. En revanche, vous devez être en mesure de répondre aux demandes d'accès des personnes concernées, qui ont le droit d'obtenir la confirmation du traitement et une copie de leurs données [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : traitement de données à caractère personnel ; responsable du traitement ; mesures techniques et organisationnelles appropriées ; sécurité des données ; hébergement de données ; registre des activités de traitement

Temps : recherche 25.3 s · génération 3.0 s (3172 tokens lus, 681 écrits, 451.4 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.5 s · attente des limites de l'API 1 s (non comptée)

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

Temps : recherche 24.8 s · génération 0.5 s (3416 tokens lus, 25 écrits, 523.5 tokens/s) · reformulation 0.3 s

## e06 — La boîte mail de l'accueil a été piratée hier. Qu'est-ce que je dois faire ? Je dois prévenir quelqu'un ?

Article attendu : RGPD art. 33 ou RGPD art. 34 — passage [1].

### Réponse du copilote

> Oui, vous devez prévenir l'autorité de contrôle compétente si vous êtes le responsable du traitement, « dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance », sauf si « la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques » [1]. Si vous êtes un sous-traitant, vous devez notifier la violation au responsable du traitement « dans les meilleurs délais après en avoir pris connaissance » [1]. La notification à l'autorité doit décrire la nature de la violation, les catégories de personnes concernées, les conséquences probables et les mesures prises ou proposées pour remédier à la situation [1]. Vous devez également documenter la violation en indiquant les faits, ses effets et les mesures prises [1]. Si la violation est « susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique », vous devez aussi communiquer la violation à la personne concernée « dans les meilleurs délais » [2]. Cette communication doit décrire la nature de la violation en des termes clairs et simples et inclure les informations sur le point de contact, les conséquences probables et les mesures de remédiation [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. »
  [1] « Le sous-traitant notifie au responsable du traitement toute violation de données à caractère personnel dans les meilleurs délais après en avoir pris connaissance. »
  [1] « La notification visée au paragraphe 1 doit, à tout le moins: a) décrire la nature de la violation de données à caractère personnel y compris, si possible, les catégories et le nombre approximatif de personnes concernées par la violation et les catégories et le nombre approximatif d'enregistrements de données à caractère personnel concernés; b) communiquer le nom et les coordonnées du délégué à la protection des données ou d'un autre point de contact auprès duquel des informations supplémentaires peuvent être obtenues; c) décrire les conséquences probables de la violation de données à caractère personnel; d) décrire les mesures prises ou que le responsable du traitement propose de prendre pour remédier à la violation de données à caractère personnel, y compris, le cas échéant, les mesures pour en atténuer les éventuelles conséquences négatives. »
  [1] « Le responsable du traitement documente toute violation de données à caractère personnel, en indiquant les faits concernant la violation des données à caractère personnel, ses effets et les mesures prises pour y remédier. »
  [2] « Lorsqu'une violation de données à caractère personnel est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement communique la violation de données à caractère personnel à la personne concernée dans les meilleurs délais. »
  [2] « La communication à la personne concernée visée au paragraphe 1 du présent article décrit, en des termes clairs et simples, la nature de la violation de données à caractère personnel et contient au moins les informations et mesures visées à l'article 33, paragraphe 3, points b), c) et d). »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 33 : Notification à l'autorité de contrôle d'une violation de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_33
  [2] RGPD — règlement (UE) 2016/679, article 34 : Communication à la personne concernée d'une violation de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_34
Passages consultés mais non cités :
  [3] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [4] RGPD — règlement (UE) 2016/679, article 77 : Droit d'introduire une réclamation auprès d'une autorité de contrôle
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_77
  [5] RGPD — règlement (UE) 2016/679, article 58, paragraphe 2 : Pouvoirs
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_58

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
- [2] « La communication à la personne concernée visée au paragraphe 1 du présent article décrit, en des termes clairs et simples, la nature de la violation de données à caractère personnel et contient au moins les informations et mesures visées à l'article 33, paragraphe 3, points b), c) et d). »

RÉPONSE :
Oui, vous devez prévenir l'autorité de contrôle compétente si vous êtes le responsable du traitement, « dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance », sauf si « la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques » [1]. Si vous êtes un sous-traitant, vous devez notifier la violation au responsable du traitement « dans les meilleurs délais après en avoir pris connaissance » [1]. La notification à l'autorité doit décrire la nature de la violation, les catégories de personnes concernées, les conséquences probables et les mesures prises ou proposées pour remédier à la situation [1]. Vous devez également documenter la violation en indiquant les faits, ses effets et les mesures prises [1]. Si la violation est « susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique », vous devez aussi communiquer la violation à la personne concernée « dans les meilleurs délais » [2]. Cette communication doit décrire la nature de la violation en des termes clairs et simples et inclure les informations sur le point de contact, les conséquences probables et les mesures de remédiation [2].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : notification de violation de données à caractère personnel ; autorité de contrôle ; responsable du traitement ; données à caractère personnel ; violation de la sécurité

Temps : recherche 27.7 s · génération 2.1 s (3328 tokens lus, 758 écrits, 464.3 tokens/s) · contrôle de pertinence 9.5 s · reformulation 0.4 s · attente des limites de l'API 27 s (non comptée)

## e07 — Un prestataire extérieur gère notre paie. Je dois signer un contrat spécial avec lui pour les données ?

Article attendu : RGPD art. 28, paragraphe 3 — passage [3].

### Réponse du copilote

> Oui, vous devez signer un contrat spécifique avec ce prestataire, car il agit en tant que sous-traitant [5]. En tant que responsable du traitement, vous ne pouvez faire appel qu'à des sous-traitants qui présentent des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées [2]. Le traitement par ce sous-traitant doit être régi par un contrat ou un autre acte juridique qui définit l'objet, la durée, la nature et la finalité du traitement, ainsi que le type de données et les catégories de personnes concernées [3]. Ce contrat doit notamment prévoir que le sous-traitant ne traite les données que sur instruction documentée de votre part [3], veille à la confidentialité des personnes autorisées à traiter les données [3], et prend toutes les mesures requises en vertu de l'article 32 [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [5] « «sous-traitant», la personne physique ou morale, l'autorité publique, le service ou un autre organisme qui traite des données à caractère personnel pour le compte du responsable du traitement; »
  [2] « Lorsqu'un traitement doit être effectué pour le compte d'un responsable du traitement, celui-ci fait uniquement appel à des sous-traitants qui présentent des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées de manière à ce que le traitement réponde aux exigences du présent règlement et garantisse la protection des droits de la personne concernée. »
  [3] « Le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre, qui lie le sous-traitant à l'égard du responsable du traitement, définit l'objet et la durée du traitement, la nature et la finalité du traitement, le type de données à caractère personnel et les catégories de personnes concernées, et les obligations et les droits du responsable du traitement. »
  [3] « Ce contrat ou cet autre acte juridique prévoit, notamment, que le sous-traitant: a) ne traite les données à caractère personnel que sur instruction documentée du responsable du traitement, y compris en ce qui concerne les transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale, à moins qu'il ne soit tenu d'y procéder en vertu du droit de l'Union ou du droit de l'État membre auquel le sous-traitant est soumis; dans ce cas, le sous-traitant informe le responsable du traitement de cette obligation juridique avant le traitement, sauf si le droit concerné interdit une telle information pour des motifs importants d'intérêt public; »
  [3] « b) veille à ce que les personnes autorisées à traiter les données à caractère personnel s'engagent à respecter la confidentialité ou soient soumises à une obligation légale appropriée de confidentialité; »
  [3] « c) prend toutes les mesures requises en vertu de l'article 32; »

Sources citées :
  [2] RGPD — règlement (UE) 2016/679, article 28, paragraphe 1 : Sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [3] RGPD — règlement (UE) 2016/679, article 28, paragraphe 3 : Sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [5] RGPD — règlement (UE) 2016/679, article 4, définition 8 : Définitions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 28, paragraphe 4 : Sous-traitant
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [4] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [5] « «sous-traitant», la personne physique ou morale, l'autorité publique, le service ou un autre organisme qui traite des données à caractère personnel pour le compte du responsable du traitement; »
- [2] « Lorsqu'un traitement doit être effectué pour le compte d'un responsable du traitement, celui-ci fait uniquement appel à des sous-traitants qui présentent des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées de manière à ce que le traitement réponde aux exigences du présent règlement et garantisse la protection des droits de la personne concernée. »
- [3] « Le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre, qui lie le sous-traitant à l'égard du responsable du traitement, définit l'objet et la durée du traitement, la nature et la finalité du traitement, le type de données à caractère personnel et les catégories de personnes concernées, et les obligations et les droits du responsable du traitement. »
- [3] « Ce contrat ou cet autre acte juridique prévoit, notamment, que le sous-traitant: a) ne traite les données à caractère personnel que sur instruction documentée du responsable du traitement, y compris en ce qui concerne les transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale, à moins qu'il ne soit tenu d'y procéder en vertu du droit de l'Union ou du droit de l'État membre auquel le sous-traitant est soumis; dans ce cas, le sous-traitant informe le responsable du traitement de cette obligation juridique avant le traitement, sauf si le droit concerné interdit une telle information pour des motifs importants d'intérêt public; »
- [3] « b) veille à ce que les personnes autorisées à traiter les données à caractère personnel s'engagent à respecter la confidentialité ou soient soumises à une obligation légale appropriée de confidentialité; »
- [3] « c) prend toutes les mesures requises en vertu de l'article 32; »

RÉPONSE :
Oui, vous devez signer un contrat spécifique avec ce prestataire, car il agit en tant que sous-traitant [5]. En tant que responsable du traitement, vous ne pouvez faire appel qu'à des sous-traitants qui présentent des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées [2]. Le traitement par ce sous-traitant doit être régi par un contrat ou un autre acte juridique qui définit l'objet, la durée, la nature et la finalité du traitement, ainsi que le type de données et les catégories de personnes concernées [3]. Ce contrat doit notamment prévoir que le sous-traitant ne traite les données que sur instruction documentée de votre part [3], veille à la confidentialité des personnes autorisées à traiter les données [3], et prend toutes les mesures requises en vertu de l'article 32 [3].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : sous-traitant ; contrat de traitement ; mesures techniques et organisationnelles ; registre des activités de traitement ; responsable de la protection des données ; notification de violation de données

Temps : recherche 27.3 s · génération 3.1 s (3008 tokens lus, 639 écrits, 491.3 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.3 s

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
  [2] RGPD — règlement (UE) 2016/679, article 4, définition 11 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [3] RGPD — règlement (UE) 2016/679, article 7 : Conditions applicables au consentement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_7
  [4] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
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
- [2] « «consentement» de la personne concernée, toute manifestation de volonté, libre, spécifique, éclairée et univoque par laquelle la personne concernée accepte, par une déclaration ou par un acte positif clair, que des données à caractère personnel la concernant fassent l'objet d'un traitement; »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question, car ils ne précisent pas si l'envoi d'une newsletter à des anciens clients est interdit ou permis sans consentement préalable, mais ils définissent les droits d'opposition et les conditions d'information. Si vous traitez les données pour de la prospection, la personne concernée a le droit de s'opposer à tout moment [1]. Dans ce cas, « les données à caractère personnel ne sont plus traitées à ces fins » dès lors qu'elle s'oppose [1]. Vous devez informer la personne de ce droit « au plus tard au moment de la première communication avec la personne concernée » et le présenter « clairement et séparément de toute autre information » [1]. Si le traitement repose sur le consentement, celui-ci doit être une « manifestation de volonté, libre, spécifique, éclairée et univoque » [2].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : consentement ; consentement explicite ; consentement préalable ; consentement libre ; consentement spécifique ; consentement informé

Temps : recherche 26.9 s · génération 2.2 s (3045 tokens lus, 589 écrits, 450.1 tokens/s) · contrôle de pertinence 0.3 s · reformulation 0.5 s · attente des limites de l'API 21 s (non comptée)

## e09 — Un salarié me demande une copie de toutes les données que j'ai sur lui, même les mails où on parle de lui. Je dois tout lui donner ? J'ai combien de temps pour répondre ?

Article attendu : RGPD art. 15 ou RGPD art. 12, paragraphe 3 — passage [1].

### Réponse du copilote

> Oui, vous devez fournir une copie des données à caractère personnel faisant l'objet d'un traitement, ce qui inclut les e-mails où le salarié est mentionné, car il a le droit d'obtenir l'accès à ces données [1]. Cependant, cette obligation n'est pas absolue : le droit d'obtenir une copie « ne porte pas atteinte aux droits et libertés d'autrui » [1]. Vous avez un délai d'un mois à compter de la réception de la demande pour répondre [2]. Si la demande est complexe ou si vous recevez de nombreuses demandes, ce délai peut être prolongé de deux mois [2]. Dans ce cas, vous devez informer le salarié de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande [2].

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
  [4] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [5] RGPD — règlement (UE) 2016/679, article 12, paragraphe 4 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12

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
Oui, vous devez fournir une copie des données à caractère personnel faisant l'objet d'un traitement, ce qui inclut les e-mails où le salarié est mentionné, car il a le droit d'obtenir l'accès à ces données [1]. Cependant, cette obligation n'est pas absolue : le droit d'obtenir une copie « ne porte pas atteinte aux droits et libertés d'autrui » [1]. Vous avez un délai d'un mois à compter de la réception de la demande pour répondre [2]. Si la demande est complexe ou si vous recevez de nombreuses demandes, ce délai peut être prolongé de deux mois [2]. Dans ce cas, vous devez informer le salarié de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande [2].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit d'accès ; données à caractère personnel ; délai d'un mois ; demande d'accès ; données personnelles

Temps : recherche 27.3 s · génération 1.6 s (3146 tokens lus, 443 écrits, 410.1 tokens/s) · contrôle de pertinence 0.4 s · reformulation 0.3 s · attente des limites de l'API 18 s (non comptée)

## e10 — Un salarié est parti de l'entreprise. Je peux encore lire sa boîte mail professionnelle ?

Article attendu : RGPD art. 5 ou RGPD art. 6, paragraphe 1 — absent des passages donnés au modèle.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [2] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [3] RGPD — règlement (UE) 2016/679, article 6, paragraphe 4 : Licéité du traitement
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

Reformulation de la question (termes ajoutés avant la recherche) : données à caractère personnel ; finalité de la collecte ; proportionnalité ; sécurité des données ; accès aux données ; consentement

Temps : recherche 26.3 s · génération 0.5 s (3680 tokens lus, 25 écrits, 453.0 tokens/s) · reformulation 0.5 s

## e11 — Dans notre organisme de formation, on demande aux stagiaires leur numéro de sécurité sociale et des informations sur leur handicap. On a le droit ?

Article attendu : RGPD art. 9, paragraphe 1 ou RGPD art. 9, paragraphe 2_a i ou RGPD art. 87 — passage [2].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 32 : Sécurité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_32
  [2] RGPD — règlement (UE) 2016/679, article 9, paragraphe 2, points a) à i) : Traitement portant sur des catégories particulières de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
  [3] RGPD — règlement (UE) 2016/679, article 9, paragraphe 1 : Traitement portant sur des catégories particulières de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
  [4] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [5] RGPD — règlement (UE) 2016/679, article 9, paragraphe 3 : Traitement portant sur des catégories particulières de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [3] « Le traitement des données à caractère personnel qui révèle l'origine raciale ou ethnique, les opinions politiques, les convictions religieuses ou philosophiques ou l'appartenance syndicale, ainsi que le traitement des données génétiques, des données biométriques aux fins d'identifier une personne physique de manière unique, des données concernant la santé ou des données concernant la vie sexuelle ou l'orientation sexuelle d'une personne physique sont interdits. »
- [2] « Le paragraphe 1 ne s'applique pas si l'une des conditions suivantes est remplie: »
- [2] « a) la personne concernée a donné son consentement explicite au traitement de ces données à caractère personnel pour une ou plusieurs finalités spécifiques, sauf lorsque le droit de l'Union ou le droit de l'État membre prévoit que l'interdiction visée au paragraphe 1 ne peut pas être levée par la personne concernée; »
- [2] « b) le traitement est nécessaire aux fins de l'exécution des obligations et de l'exercice des droits propres au responsable du traitement ou à la personne concernée en matière de droit du travail, de la sécurité sociale et de la protection sociale, dans la mesure où ce traitement est autorisé par le droit de l'Union, par le droit d'un État membre ou par une convention collective conclue en vertu du droit d'un État membre qui prévoit des garanties appropriées pour les droits fondamentaux et les intérêts de la personne concernée; »
- [2] « h) le traitement est nécessaire aux fins de la médecine préventive ou de la médecine du travail, de l'appréciation de la capacité de travail du travailleur, de diagnostics médicaux, de la prise en charge sanitaire ou sociale, ou de la gestion des systèmes et des services de soins de santé ou de protection sociale sur la base du droit de l'Union, du droit d'un État membre ou en vertu d'un contrat conclu avec un professionnel de la santé et soumis aux conditions et garanties visées au paragraphe 3; »
- [5] « Les données à caractère personnel visées au paragraphe 1 peuvent faire l'objet d'un traitement aux fins prévues au paragraphe 2, point h), si ces données sont traitées par un professionnel de la santé soumis à une obligation de secret professionnel conformément au droit de l'Union, au droit d'un État membre ou aux règles arrêtées par les organismes nationaux compétents, ou sous sa responsabilité, ou par une autre personne également soumise à une obligation de secret conformément au droit de l'Union ou au droit d'un État membre ou aux règles arrêtées par les organismes nationaux compétents. »

RÉPONSE :
Le traitement des données concernant la santé, qui incluent les informations sur le handicap, est en principe interdit par le RGPD, article 9, paragraphe 1 [3]. Cependant, cette interdiction ne s'applique pas si l'une des conditions d'exception prévues à l'article 9, paragraphe 2 est remplie [2]. Parmi ces conditions, le consentement explicite de la personne concernée pour une finalité spécifique est possible, « sauf lorsque le droit de l'Union ou le droit de l'État membre prévoit que l'interdiction visée au paragraphe 1 ne peut pas être levée par la personne concernée » [2]. Une autre exception concerne le traitement nécessaire à l'exécution des obligations en matière de droit du travail, de la sécurité sociale et de la protection sociale, « dans la mesure où ce traitement est autorisé par le droit de l'Union, par le droit d'un État membre ou par une convention collective conclue en vertu du droit d'un État membre qui prévoit des garanties appropriées pour les droits fondamentaux et les intérêts de la personne concernée » [2]. Enfin, le traitement est permis s'il est nécessaire à la prise en charge sanitaire ou sociale, « sur la base du droit de l'Union, du droit d'un État membre ou en vertu d'un contrat conclu avec un professionnel de la santé et soumis aux conditions et garanties visées au paragraphe 3 » [2]. Dans ce dernier cas, les données doivent être traitées par un professionnel de la santé soumis à une obligation de secret professionnel, ou sous sa responsabilité, ou par une autre personne également soumise à une obligation de secret [5]. Les passages trouvés ne traitent pas spécifiquement de la collecte du numéro de sécurité sociale dans le contexte d'un organisme de formation, mais indiquent que les règles concrètes dépendent du droit national ou des conditions légales applicables.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données de santé ; données sensibles ; consentement explicite ; mesures de sécurité ; minimisation des données

Temps : recherche 27.5 s · génération 2.6 s (3305 tokens lus, 961 écrits, 477.7 tokens/s) · contrôle de pertinence 0.9 s · reformulation 0.3 s · attente des limites de l'API 53 s (non comptée)

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
  [2] RGPD — règlement (UE) 2016/679, article 6, paragraphe 4 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
  [3] RGPD — règlement (UE) 2016/679, article 6, paragraphe 1 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
  [4] RGPD — règlement (UE) 2016/679, article 7 : Conditions applicables au consentement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_7
  [5] RGPD — règlement (UE) 2016/679, article 32 : Sécurité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_32
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les données à caractère personnel doivent être: a) traitées de manière licite, loyale et transparente au regard de la personne concernée (licéité, loyauté, transparence); »
- [1] « c) adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités pour lesquelles elles sont traitées (minimisation des données); »
- [3] « Le traitement n'est licite que si, et dans la mesure où, au moins une des conditions suivantes est remplie: a) la personne concernée a consenti au traitement de ses données à caractère personnel pour une ou plusieurs finalités spécifiques; »
- [3] « f) le traitement est nécessaire aux fins des intérêts légitimes poursuivis par le responsable du traitement ou par un tiers, à moins que ne prévalent les intérêts ou les libertés et droits fondamentaux de la personne concernée qui exigent une protection des données à caractère personnel, notamment lorsque la personne concernée est un enfant. »
- [4] « Dans les cas où le traitement repose sur le consentement, le responsable du traitement est en mesure de démontrer que la personne concernée a donné son consentement au traitement de données à caractère personnel la concernant. »
- [4] « La personne concernée a le droit de retirer son consentement à tout moment. »

RÉPONSE :
Oui, vous pouvez suivre les véhicules de vos techniciens par GPS, à condition de respecter les principes du RGPD.
Le traitement doit être « licite, loyale et transparent au regard de la personne concernée » [1].
Vous devez choisir une base légale, par exemple le consentement de la personne concernée [3] ou l'intérêt légitime du responsable du traitement [3].
Si vous choisissez le consentement, vous devez être en mesure de démontrer que la personne l'a donné [4] et elle a le droit de le retirer à tout moment [4].
Les données collectées doivent être « adéquates, pertinentes et limitées à ce qui est nécessaire » [1].
Si vous invoquez l'intérêt légitime, cela ne s'applique que « à moins que ne prévalent les intérêts ou les libertés et droits fondamentaux de la personne concernée » [3].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : traitement de données à caractère personnel ; consentement ; finalité du traitement ; minimisation des données ; données de localisation

Temps : recherche 27.8 s · génération 1.5 s (3123 tokens lus, 490 écrits, 455.8 tokens/s) · contrôle de pertinence 0.6 s · reformulation 0.4 s

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
  [2] RGPD — règlement (UE) 2016/679, article 4, définition 11 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [3] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
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
- [2] « «consentement» de la personne concernée, toute manifestation de volonté, libre, spécifique, éclairée et univoque par laquelle la personne concernée accepte, par une déclaration ou par un acte positif clair, que des données à caractère personnel la concernant fassent l'objet d'un traitement; »
- [1] « Si le consentement de la personne concernée est donné dans le cadre d'une déclaration écrite qui concerne également d'autres questions, la demande de consentement est présentée sous une forme qui la distingue clairement de ces autres questions, sous une forme compréhensible et aisément accessible, et formulée en des termes clairs et simples. »
- [1] « La personne concernée a le droit de retirer son consentement à tout moment. »
- [1] « Il est aussi simple de retirer que de donner son consentement. »

RÉPONSE :
Non, il ne faut pas nécessairement leur accord écrit, car le consentement peut être donné « par une déclaration ou par un acte positif clair » [2]. Cependant, si vous choisissez de recueillir ce consentement par écrit, la demande doit être « présentée sous une forme qui la distingue clairement de ces autres questions, sous une forme compréhensible et aisément accessible, et formulée en des termes clairs et simples » [1]. Vous devez également informer les bénévoles qu'ils ont « le droit de retirer son consentement à tout moment » et que « il est aussi simple de retirer que de donner son consentement » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : consentement ; données à caractère personnel ; traitement ; responsable du traitement

Temps : recherche 25.9 s · génération 3.7 s (2891 tokens lus, 319 écrits, 454.2 tokens/s) · contrôle de pertinence 3.7 s · reformulation 0.3 s · attente des limites de l'API 40 s (non comptée)

## e14 — On a 8 salariés. On doit tenir un registre des traitements et nommer un DPO ?

Article attendu : RGPD art. 30 ou RGPD art. 37 — passage [1].

### Réponse du copilote

> Concernant le registre des traitements, vous n'êtes pas obligé de le tenir si vous comptez moins de 250 employés, « sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 » [1].
> Concernant la désignation d'un DPO, l'obligation de désigner un délégué à la protection des données « en tout état de cause » ne s'applique que si vous êtes une autorité publique, si vos activités de base consistent en un suivi régulier et systématique à grande échelle, ou si elles consistent en un traitement à grande échelle de catégories particulières de données [2].
> Dans les autres cas, vous « pouvez désigner ou, si le droit de l'Union ou le droit d'un État membre l'exige, sont tenus de désigner un délégué à la protection des données » [2]. Les passages trouvés ne précisent pas les conditions spécifiques du droit national qui pourraient imposer cette désignation pour une PME de 8 salariés.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10. »
  [2] « Le responsable du traitement et le sous-traitant désignent en tout état de cause un délégué à la protection des données lorsque: »
  [2] « a) le traitement est effectué par une autorité publique ou un organisme public, à l'exception des juridictions agissant dans l'exercice de leur fonction juridictionnelle; »
  [2] « b) les activités de base du responsable du traitement ou du sous-traitant consistent en des opérations de traitement qui, du fait de leur nature, de leur portée et/ou de leurs finalités, exigent un suivi régulier et systématique à grande échelle des personnes concernées; ou »
  [2] « c) les activités de base du responsable du traitement ou du sous-traitant consistent en un traitement à grande échelle de catégories particulières de données visées à l’article 9 ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l’article 10. »
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
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « pouvez désigner ou, si le droit de l'Union ou le droit d'un État membre l'exige, sont tenus de désigner un délégué à la … ».

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10. »
- [2] « Le responsable du traitement et le sous-traitant désignent en tout état de cause un délégué à la protection des données lorsque: »
- [2] « a) le traitement est effectué par une autorité publique ou un organisme public, à l'exception des juridictions agissant dans l'exercice de leur fonction juridictionnelle; »
- [2] « b) les activités de base du responsable du traitement ou du sous-traitant consistent en des opérations de traitement qui, du fait de leur nature, de leur portée et/ou de leurs finalités, exigent un suivi régulier et systématique à grande échelle des personnes concernées; ou »
- [2] « c) les activités de base du responsable du traitement ou du sous-traitant consistent en un traitement à grande échelle de catégories particulières de données visées à l’article 9 ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l’article 10. »
- [2] « Dans les cas autres que ceux visés au paragraphe 1, le responsable du traitement ou le sous-traitant ou les associations et autres organismes représentant des catégories de responsables du traitement ou de sous-traitants peuvent désigner ou, si le droit de l'Union ou le droit d'un État membre l'exige, sont tenus de désigner un délégué à la protection des données. »

RÉPONSE :
Concernant le registre des traitements, vous n'êtes pas obligé de le tenir si vous comptez moins de 250 employés, « sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10 » [1].
Concernant la désignation d'un DPO, l'obligation de désigner un délégué à la protection des données « en tout état de cause » ne s'applique que si vous êtes une autorité publique, si vos activités de base consistent en un suivi régulier et systématique à grande échelle, ou si elles consistent en un traitement à grande échelle de catégories particulières de données [2].
Dans les autres cas, vous « pouvez désigner ou, si le droit de l'Union ou le droit d'un État membre l'exige, sont tenus de désigner un délégué à la protection des données » [2]. Les passages trouvés ne précisent pas les conditions spécifiques du droit national qui pourraient imposer cette désignation pour une PME de 8 salariés.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : registre des activités de traitement ; responsable de la protection des données

Temps : recherche 25.9 s · génération 2.2 s (3587 tokens lus, 747 écrits, 453.8 tokens/s) · contrôle de pertinence 1.2 s · reformulation 2.2 s · attente des limites de l'API 28 s (non comptée)

## e15 — Notre logiciel de gestion des clients est hébergé aux États-Unis. C'est autorisé ?

Article attendu : RGPD art. 44 ou RGPD art. 45, paragraphe 1 ou RGPD art. 46 — passage [1].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question, car ils ne précisent pas si les États-Unis font l'objet d'une décision d'adéquation spécifique. Cependant, le RGPD encadre strictement les transferts de données vers des pays tiers comme les États-Unis. Si aucune décision d'adéquation n'existe pour ce pays, vous ne pouvez transférer des données que si vous avez prévu des « garanties appropriées » et que les personnes concernées disposent de « droits opposables et de voies de droit effectives » [1]. Parmi ces garanties, vous pouvez utiliser des « clauses types de protection des données adoptées par la Commission » [1] ou un « code de conduite approuvé conformément à l'article 40, assorti de l'engagement contraignant et exécutoire » [1]. À défaut de ces garanties, un transfert n'est possible que dans des situations particulières, par exemple si « la personne concernée a donné son consentement explicite au transfert envisagé, après avoir été informée des risques » [5]. La liste des pays reconnus par une décision d'adéquation est publiée par la Commission européenne, mais les textes fournis ne permettent pas de confirmer le statut actuel des États-Unis.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
  [1] « Les garanties appropriées visées au paragraphe 1 peuvent être fournies, sans que cela ne nécessite une autorisation particulière d'une autorité de contrôle, par: »
  [1] « c) des clauses types de protection des données adoptées par la Commission en conformité avec la procédure d'examen visée à l'article 93, paragraphe 2; »
  [1] « e) un code de conduite approuvé conformément à l'article 40, assorti de l'engagement contraignant et exécutoire pris par le responsable du traitement ou le sous-traitant dans le pays tiers d'appliquer les garanties appropriées, y compris en ce qui concerne les droits des personnes concernées; ou »
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

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
- [1] « Les garanties appropriées visées au paragraphe 1 peuvent être fournies, sans que cela ne nécessite une autorisation particulière d'une autorité de contrôle, par: »
- [1] « c) des clauses types de protection des données adoptées par la Commission en conformité avec la procédure d'examen visée à l'article 93, paragraphe 2; »
- [1] « e) un code de conduite approuvé conformément à l'article 40, assorti de l'engagement contraignant et exécutoire pris par le responsable du traitement ou le sous-traitant dans le pays tiers d'appliquer les garanties appropriées, y compris en ce qui concerne les droits des personnes concernées; ou »
- [5] « En l'absence de décision d'adéquation en vertu de l'article 45, paragraphe 3, ou de garanties appropriées en vertu de l'article 46, y compris des règles d'entreprise contraignantes, un transfert ou un ensemble de transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale ne peut avoir lieu qu'à l'une des conditions suivantes: »
- [5] « a) la personne concernée a donné son consentement explicite au transfert envisagé, après avoir été informée des risques que ce transfert pouvait comporter pour elle en raison de l'absence de décision d'adéquation et de garanties appropriées; »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question, car ils ne précisent pas si les États-Unis font l'objet d'une décision d'adéquation spécifique. Cependant, le RGPD encadre strictement les transferts de données vers des pays tiers comme les États-Unis. Si aucune décision d'adéquation n'existe pour ce pays, vous ne pouvez transférer des données que si vous avez prévu des « garanties appropriées » et que les personnes concernées disposent de « droits opposables et de voies de droit effectives » [1]. Parmi ces garanties, vous pouvez utiliser des « clauses types de protection des données adoptées par la Commission » [1] ou un « code de conduite approuvé conformément à l'article 40, assorti de l'engagement contraignant et exécutoire » [1]. À défaut de ces garanties, un transfert n'est possible que dans des situations particulières, par exemple si « la personne concernée a donné son consentement explicite au transfert envisagé, après avoir été informée des risques » [5]. La liste des pays reconnus par une décision d'adéquation est publiée par la Commission européenne, mais les textes fournis ne permettent pas de confirmer le statut actuel des États-Unis.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : transfert de données vers un pays tiers ; pays tiers ; mesures de sécurité appropriées ; garanties appropriées ; décision d'adéquation ; sous-traitant

Temps : recherche 25.5 s · génération 2.1 s (3338 tokens lus, 670 écrits, 423.8 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.8 s · attente des limites de l'API 48 s (non comptée)

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
Oui, l'AI Act vous concerne en tant qu'utilisateur (déployeur), même si vous ne créez pas l'IA, car le règlement impose des obligations spécifiques aux déployeurs dans certains cas. Par exemple, si vous utilisez un outil pour générer ou manipuler des images, audios ou vidéos constituant un hypertrucage, vous devez « indiquer que les contenus ont été générés ou manipulés par une IA » [1]. De même, si vous publiez des textes générés par IA « dans le but d’informer le public sur des questions d’intérêt public », vous devez « indiquer que le texte a été généré ou manipulé par une IA » [1]. En revanche, les obligations liées à la conception, au développement et à la marque technique des sorties incombent aux fournisseurs, comme le prévoit l'article 50, paragraphes 1 et 3 [2] [3]. Les passages trouvés ne traitent pas directement de l'obligation d'information des utilisateurs finaux par le fournisseur dans le cadre d'une interaction simple, mais précisent que la transparence est une exigence pour les systèmes d'IA à haut risque afin de permettre aux déployeurs d'interpréter les sorties [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : fournisseur de modèle de fondation ; utilisateur déployant ; modèle de fondation ; système d'IA ; obligation de transparence ; utilisateur

Temps : recherche 27.4 s · génération 1.9 s (3237 tokens lus, 642 écrits, 450.5 tokens/s) · contrôle de pertinence 0.4 s · reformulation 0.5 s · attente des limites de l'API 22 s (non comptée)

## e17 — Je voudrais utiliser un logiciel d'IA qui trie automatiquement les CV. C'est interdit ? Sinon, quelles règles je dois respecter ?

Article attendu : AI Act annexe III, point 4 ou AI Act art. 26 — passage [3].

### Réponse du copilote

> Non, l'utilisation d'un logiciel d'IA pour trier automatiquement les CV n'est pas interdite par l'AI Act, car cette pratique ne figure pas dans la liste des pratiques interdites de l'article 5 [1] [2].
> Cependant, ce type de système est classé comme « à haut risque » car il est destiné à être utilisé pour le recrutement ou la sélection de personnes physiques, notamment pour analyser et filtrer les candidatures [3].
> Ce classement en système à haut risque est systématique si le logiciel effectue un profilage de personnes physiques [4].
> Il existe une exception : le système n'est pas considéré comme à haut risque s'il ne présente pas de risque important de préjudice pour la santé, la sécurité ou les droits fondamentaux des personnes physiques, y compris en n'ayant pas d'incidence significative sur le résultat de la prise de décision [5].
> Les passages fournis ne détaillent pas les obligations spécifiques (comme les évaluations de conformité ou la documentation) que vous devez respecter en tant que déployeur d'un système à haut risque, mais indiquent uniquement les critères de classification.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »
  [4] « Nonobstant le premier alinéa, un système d’IA visé à l’annexe III est toujours considéré comme étant à haut risque lorsqu’il effectue un profilage de personnes physiques. »
  [5] « 3. Par dérogation au paragraphe 2, un système d’IA visé à l’annexe III n’est pas considéré comme étant à haut risque lorsqu’il ne présente pas de risque important de préjudice pour la santé, la sécurité ou les droits fondamentaux des personnes physiques, y compris en n’ayant pas d’incidence significative sur le résultat de la prise de décision. »
  [5] « Le premier alinéa s’applique lorsqu’une des conditions suivantes est remplie: »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points f) à h) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [2] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points a) à e) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [3] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [4] AI Act — règlement (UE) 2024/1689, article 6, point d : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
  [5] AI Act — règlement (UE) 2024/1689, article 6, paragraphe 3 : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
Attention : La réponse cite [1], [2] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [3] « a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; »
- [4] « Nonobstant le premier alinéa, un système d’IA visé à l’annexe III est toujours considéré comme étant à haut risque lorsqu’il effectue un profilage de personnes physiques. »
- [5] « 3. Par dérogation au paragraphe 2, un système d’IA visé à l’annexe III n’est pas considéré comme étant à haut risque lorsqu’il ne présente pas de risque important de préjudice pour la santé, la sécurité ou les droits fondamentaux des personnes physiques, y compris en n’ayant pas d’incidence significative sur le résultat de la prise de décision. »
- [5] « Le premier alinéa s’applique lorsqu’une des conditions suivantes est remplie: »

RÉPONSE :
Non, l'utilisation d'un logiciel d'IA pour trier automatiquement les CV n'est pas interdite par l'AI Act, car cette pratique ne figure pas dans la liste des pratiques interdites de l'article 5 [1] [2].
Cependant, ce type de système est classé comme « à haut risque » car il est destiné à être utilisé pour le recrutement ou la sélection de personnes physiques, notamment pour analyser et filtrer les candidatures [3].
Ce classement en système à haut risque est systématique si le logiciel effectue un profilage de personnes physiques [4].
Il existe une exception : le système n'est pas considéré comme à haut risque s'il ne présente pas de risque important de préjudice pour la santé, la sécurité ou les droits fondamentaux des personnes physiques, y compris en n'ayant pas d'incidence significative sur le résultat de la prise de décision [5].
Les passages fournis ne détaillent pas les obligations spécifiques (comme les évaluations de conformité ou la documentation) que vous devez respecter en tant que déployeur d'un système à haut risque, mais indiquent uniquement les critères de classification.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : système d'IA à haut risque ; employeur ; candidat à un emploi ; profilage ; biais algorithmique ; transparence

Temps : recherche 25.7 s · génération 1.5 s (3120 tokens lus, 467 écrits, 465.1 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.3 s · attente des limites de l'API 37 s (non comptée)

## e18 — On a mis un chatbot sur notre site. On doit dire aux visiteurs qu'ils parlent avec une machine ?

Article attendu : AI Act art. 50, paragraphe 1 — passage [1].

### Réponse du copilote

> Oui, vous devez informer les visiteurs qu'ils interagissent avec un système d'IA, à moins que cela ne soit déjà évident pour eux [1]. Cette obligation de transparence s'applique aux systèmes conçus pour interagir directement avec des personnes physiques, comme un chatbot sur un site web [1]. L'exception s'applique uniquement « si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation » [1].

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
Attention : La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui, vous devez informer les visiteurs qu'ils interagissent avec un système d'IA, à moins que cela ne soit déjà évident … » (et 2 autre(s)). Vérifiez qui est concerné.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »

RÉPONSE :
Oui, vous devez informer les visiteurs qu'ils interagissent avec un système d'IA, à moins que cela ne soit déjà évident pour eux [1]. Cette obligation de transparence s'applique aux systèmes conçus pour interagir directement avec des personnes physiques, comme un chatbot sur un site web [1]. L'exception s'applique uniquement « si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : obligation d'information ; interaction homme-machine ; transparence ; notification de l'interaction avec un système d'IA

Temps : recherche 26.4 s · génération 1.4 s (3486 tokens lus, 218 écrits, 454.1 tokens/s) · contrôle de pertinence 0.8 s · reformulation 0.2 s

## e19 — Notre organisme de formation veut utiliser une IA pour corriger les examens et noter les stagiaires. C'est risqué ?

Article attendu : AI Act annexe III, point 3 — passage [1].

### Réponse du copilote

> Oui, l'utilisation d'une IA pour corriger les examens et noter les stagiaires est considérée comme un système d'IA à haut risque, car elle correspond à la catégorie des systèmes « destinés à être utilisés pour évaluer les acquis d'apprentissage » dans le domaine de l'éducation et de la formation professionnelle [1]. Cette classification signifie que le système est soumis à des exigences strictes de l'AI Act, notamment l'obligation de permettre un « contrôle effectif par des personnes physiques » pendant son utilisation [5]. De plus, le système doit techniquement permettre « l’enregistrement automatique des événements (journaux) » pour assurer la traçabilité [4]. Enfin, lors de la mise en œuvre, il doit être tenu compte des compétences du déployeur et du contexte d'utilisation pour réduire les risques liés à l'usage du système [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « b) systèmes d'IA destinés à être utilisés pour évaluer les acquis d'apprentissage, y compris lorsque ceux-ci sont utilisés pour orienter le processus d'apprentissage de personnes physiques dans les établissements d'enseignement et de formation professionnelle, à tous les niveaux; »
  [1] « Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des domaines suivants: »
  [3] « En vue de l’élimination ou de la réduction des risques liés à l’utilisation du système d’IA à haut risque, il est dûment tenu compte des connaissances techniques, de l’expérience, de l’éducation et de la formation pouvant être attendues du déployeur, ainsi que du contexte prévisible dans lequel le système est destiné à être utilisé. »
  [4] « 1. Les systèmes d’IA à haut risque permettent, techniquement, l’enregistrement automatique des événements (journaux) tout au long de la durée de vie du système. »
  [5] « 1. La conception et le développement des systèmes d’IA à haut risque permettent, notamment au moyen d’interfaces homme-machine appropriées, un contrôle effectif par des personnes physiques pendant leur période d’utilisation. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, annexe III, point 3 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [3] AI Act — règlement (UE) 2024/1689, article 9, point c : Système de gestion des risques (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_9
  [4] AI Act — règlement (UE) 2024/1689, article 12 : Enregistrement (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_12
  [5] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, annexe III, point 7 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « b) systèmes d'IA destinés à être utilisés pour évaluer les acquis d'apprentissage, y compris lorsque ceux-ci sont utilisés pour orienter le processus d'apprentissage de personnes physiques dans les établissements d'enseignement et de formation professionnelle, à tous les niveaux; »
- [1] « Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des domaines suivants: »
- [3] « En vue de l’élimination ou de la réduction des risques liés à l’utilisation du système d’IA à haut risque, il est dûment tenu compte des connaissances techniques, de l’expérience, de l’éducation et de la formation pouvant être attendues du déployeur, ainsi que du contexte prévisible dans lequel le système est destiné à être utilisé. »
- [4] « 1. Les systèmes d’IA à haut risque permettent, techniquement, l’enregistrement automatique des événements (journaux) tout au long de la durée de vie du système. »
- [5] « 1. La conception et le développement des systèmes d’IA à haut risque permettent, notamment au moyen d’interfaces homme-machine appropriées, un contrôle effectif par des personnes physiques pendant leur période d’utilisation. »

RÉPONSE :
Oui, l'utilisation d'une IA pour corriger les examens et noter les stagiaires est considérée comme un système d'IA à haut risque, car elle correspond à la catégorie des systèmes « destinés à être utilisés pour évaluer les acquis d'apprentissage » dans le domaine de l'éducation et de la formation professionnelle [1]. Cette classification signifie que le système est soumis à des exigences strictes de l'AI Act, notamment l'obligation de permettre un « contrôle effectif par des personnes physiques » pendant son utilisation [5]. De plus, le système doit techniquement permettre « l’enregistrement automatique des événements (journaux) » pour assurer la traçabilité [4]. Enfin, lors de la mise en œuvre, il doit être tenu compte des compétences du déployeur et du contexte d'utilisation pour réduire les risques liés à l'usage du système [3].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : système d'IA à haut risque ; évaluation des risques ; transparence ; responsabilité ; biais algorithmique ; protection des données personnelles

Temps : recherche 26.6 s · génération 3.6 s (3231 tokens lus, 482 écrits, 428.3 tokens/s) · contrôle de pertinence 1.2 s · reformulation 9.8 s · attente des limites de l'API 9 s (non comptée)

## e20 — On m'a dit que je dois former mes salariés à l'IA. C'est vraiment obligatoire ?

Article attendu : AI Act art. 4 — passage [1].

### Réponse du copilote

> Oui, si vous êtes un déployeur de systèmes d'IA, vous avez l'obligation de prendre des mesures pour favoriser le développement de la maîtrise de l'IA par votre personnel [1]. Cette obligation vise à ce que vos salariés disposent des compétences, des connaissances et de la compréhension nécessaires pour utiliser les systèmes d'IA en toute connaissance de cause et être conscients des risques [4]. Cependant, cette obligation ne vous contraint pas à garantir un niveau spécifique de maîtrise de l'IA par un individu [1]. Si vous utilisez des systèmes d'IA à haut risque sur le lieu de travail, vous devez également informer les travailleurs concernés de l'utilisation de ces systèmes [2] et vous assurer que les personnes chargées du contrôle humain disposent des compétences et de la formation nécessaires [5].

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
Oui, si vous êtes un déployeur de systèmes d'IA, vous avez l'obligation de prendre des mesures pour favoriser le développement de la maîtrise de l'IA par votre personnel [1]. Cette obligation vise à ce que vos salariés disposent des compétences, des connaissances et de la compréhension nécessaires pour utiliser les systèmes d'IA en toute connaissance de cause et être conscients des risques [4]. Cependant, cette obligation ne vous contraint pas à garantir un niveau spécifique de maîtrise de l'IA par un individu [1]. Si vous utilisez des systèmes d'IA à haut risque sur le lieu de travail, vous devez également informer les travailleurs concernés de l'utilisation de ces systèmes [2] et vous assurer que les personnes chargées du contrôle humain disposent des compétences et de la formation nécessaires [5].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : formation du personnel ; compétences en matière d'IA ; sensibilisation ; formation des utilisateurs

Temps : recherche 26.6 s · génération 1.5 s (1979 tokens lus, 549 écrits, 481.0 tokens/s) · contrôle de pertinence 0.3 s · reformulation 0.5 s · attente des limites de l'API 43 s (non comptée)

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
  [5] AI Act — règlement (UE) 2024/1689, annexe XII : Informations relatives à la transparence visées à l'article 53, paragraphe 1, point b) – documentation technique pour les fournisseurs de modèles d'IA à usage général aux fournisseurs en aval qui intègrent le modèle dans leur système d'IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_XII
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
Oui, vous devez indiquer que vos visuels sont générés par une IA, mais cette obligation ne s'applique que si ces visuels constituent un « hypertrucage » [1]. Un hypertrucage est défini comme une image générée ou manipulée par l'IA qui présente une ressemblance avec des personnes, des objets, des lieux, des entités ou événements existants et qui peut être perçue à tort comme authentique ou véridique [4]. Si vos visuels ne remplissent pas cette définition (par exemple s'ils sont purement abstraits ou ne ressemblent pas à des éléments existants), l'obligation spécifique de transparence pour les hypertrucages ne s'applique pas. Si le contenu fait partie d’une œuvre manifestement artistique, créative, satirique, fictive ou analogue, l'obligation se limite à la divulgation de l'existence de ces contenus d'une manière appropriée qui n'entrave pas l'affichage ou la jouissance de l'œuvre [1]. Cette obligation ne s'applique pas lorsque l'utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d'enquêtes ou de poursuites en la matière [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : contenus générés par l'intelligence artificielle ; obligation de transparence ; étiquetage des contenus synthétiques ; notification des personnes concernées

Temps : recherche 24.5 s · génération 1.5 s (2594 tokens lus, 540 écrits, 465.6 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.3 s · attente des limites de l'API 16 s (non comptée)

## e22 — Un fournisseur nous propose un outil qui analyse les émotions des salariés pendant les visioconférences. On a le droit de l'utiliser ?

Article attendu : AI Act art. 5, paragraphe 1_f h — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.
> L'outil proposé est un système d'IA destiné à la reconnaissance des émotions, ce qui le classe parmi les systèmes d'IA à haut risque visés par l'AI Act [2].
> En tant que déployeur, vous devez informer les salariés exposés au système de son fonctionnement et traiter leurs données personnelles conformément au RGPD (règlement (UE) 2016/679) [1].
> L'exception à cette obligation d'information ne s'applique que si la loi autorise l'utilisation du système à des fins de prévention ou de détection des infractions pénales ou d'enquêtes, sous réserve de garanties appropriées [1].
> Le fournisseur doit avoir documenté son évaluation si il considère que le système n'est pas à haut risque, avant sa mise sur le marché [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [2] « c) systèmes d'IA destinés à être utilisés pour la reconnaissance des émotions. »
  [1] « Les déployeurs d’un système de reconnaissance des émotions ou d’un système de catégorisation biométrique informent les personnes physiques qui y sont exposées du fonctionnement du système et traitent les données à caractère personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680, selon le cas. »
  [1] « Cette obligation ne s’applique pas aux systèmes d’IA utilisés pour la catégorisation biométrique et la reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l’Union. »
  [4] « Un fournisseur qui considère qu’un système d’IA visé à l’annexe III n’est pas à haut risque documente son évaluation avant que ce système ne soit mis sur le marché ou mis en service. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 3 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [2] AI Act — règlement (UE) 2024/1689, annexe III, point 1 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [4] AI Act — règlement (UE) 2024/1689, article 6, paragraphe 4 : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [5] AI Act — règlement (UE) 2024/1689, article 6, paragraphe 1 : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [2] « c) systèmes d'IA destinés à être utilisés pour la reconnaissance des émotions. »
- [1] « Les déployeurs d’un système de reconnaissance des émotions ou d’un système de catégorisation biométrique informent les personnes physiques qui y sont exposées du fonctionnement du système et traitent les données à caractère personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680, selon le cas. »
- [1] « Cette obligation ne s’applique pas aux systèmes d’IA utilisés pour la catégorisation biométrique et la reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l’Union. »
- [4] « Un fournisseur qui considère qu’un système d’IA visé à l’annexe III n’est pas à haut risque documente son évaluation avant que ce système ne soit mis sur le marché ou mis en service. »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question.
L'outil proposé est un système d'IA destiné à la reconnaissance des émotions, ce qui le classe parmi les systèmes d'IA à haut risque visés par l'AI Act [2].
En tant que déployeur, vous devez informer les salariés exposés au système de son fonctionnement et traiter leurs données personnelles conformément au RGPD (règlement (UE) 2016/679) [1].
L'exception à cette obligation d'information ne s'applique que si la loi autorise l'utilisation du système à des fins de prévention ou de détection des infractions pénales ou d'enquêtes, sous réserve de garanties appropriées [1].
Le fournisseur doit avoir documenté son évaluation si il considère que le système n'est pas à haut risque, avant sa mise sur le marché [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : analyse des émotions ; système d'IA à haut risque ; consentement explicite ; protection des données à caractère personnel ; surveillance des travailleurs ; transparence

Temps : recherche 24.1 s · génération 2.5 s (2239 tokens lus, 465 écrits, 218.1 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.3 s · attente des limites de l'API 10 s (non comptée)

## e23 — Si l'outil d'IA qu'on a acheté se trompe et écarte injustement un candidat, qui est responsable : moi ou le fournisseur ?

Article attendu : RGPD art. 82 ou AI Act art. 26 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question concernant la responsabilité en cas d'erreur lors de l'utilisation normale d'un outil d'IA acheté, mais ils précisent les cas où la responsabilité peut changer de mains. En principe, le « fournisseur » est défini comme celui qui développe ou fait développer le système et le met sur le marché sous son nom [5]. Si vous avez simplement acheté l'outil sans le modifier ni le revendre sous votre marque, vous restez le déployeur et non le fournisseur, donc les extraits ne vous attribuent pas la responsabilité de l'erreur de l'outil. Cependant, vous seriez considéré comme un fournisseur, et donc soumis aux obligations du fournisseur, si vous commercialisez le système sous votre propre nom ou marque [2], si vous apportez une modification substantielle au système [2], ou si vous modifiez sa destination pour qu'il devienne un système à haut risque [2]. De plus, si l'erreur survient durant des « essais en conditions réelles », le fournisseur ou le fournisseur potentiel est responsable du préjudice causé [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « Le fournisseur ou le fournisseur potentiel sont responsables, en vertu du droit de l’Union et du droit national applicable en matière de responsabilité, de tout préjudice causé durant les essais en conditions réelles. »
  [2] « Tout distributeur, importateur, déployeur ou autre tiers est considéré comme un fournisseur d’un système d’IA à haut risque aux fins du présent règlement et est soumis aux obligations incombant au fournisseur au titre de l’article 16 dans toutes les circonstances suivantes: »
  [2] « a) il commercialise sous son propre nom ou sa propre marque un système d’IA à haut risque déjà mis sur le marché ou mis en service, sans préjudice des dispositions contractuelles prévoyant une autre répartition des obligations; »
  [2] « b) il apporte une modification substantielle à un système d’IA à haut risque qui a déjà été mis sur le marché ou a déjà été mis en service de telle manière qu’il reste un système d’IA à haut risque en application de l’article 6; »
  [2] « c) il modifie la destination d’un système d’IA, y compris un système d’IA à usage général, qui n’a pas été classé à haut risque et a déjà été mis sur le marché ou mis en service de telle manière que le système d’IA concerné devient un système d’IA à haut risque conformément l’article 6. »
  [5] « «fournisseur», une personne physique ou morale, une autorité publique, une agence ou tout autre organisme qui développe ou fait développer un système d’IA ou un modèle d’IA à usage général et le met sur le marché ou met le système d’IA en service sous son propre nom ou sa propre marque, à titre onéreux ou gratuit; »

Sources citées :
  [2] AI Act — règlement (UE) 2024/1689, article 25, paragraphe 1 : Responsabilités tout au long de la chaîne de valeur de l’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_25
  [3] AI Act — règlement (UE) 2024/1689, article 60, paragraphe 9 : Essais de systèmes d’IA à haut risque en conditions réelles en dehors des bacs à sable réglementaires de l’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_60
  [5] AI Act — règlement (UE) 2024/1689, article 3, définition 3 : Définitions (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 25, paragraphe 4 : Responsabilités tout au long de la chaîne de valeur de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_25
  [4] AI Act — règlement (UE) 2024/1689, article 60, paragraphe 1 : Essais de systèmes d’IA à haut risque en conditions réelles en dehors des bacs à sable réglementaires de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_60

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [3] « Le fournisseur ou le fournisseur potentiel sont responsables, en vertu du droit de l’Union et du droit national applicable en matière de responsabilité, de tout préjudice causé durant les essais en conditions réelles. »
- [2] « Tout distributeur, importateur, déployeur ou autre tiers est considéré comme un fournisseur d’un système d’IA à haut risque aux fins du présent règlement et est soumis aux obligations incombant au fournisseur au titre de l’article 16 dans toutes les circonstances suivantes: »
- [2] « a) il commercialise sous son propre nom ou sa propre marque un système d’IA à haut risque déjà mis sur le marché ou mis en service, sans préjudice des dispositions contractuelles prévoyant une autre répartition des obligations; »
- [2] « b) il apporte une modification substantielle à un système d’IA à haut risque qui a déjà été mis sur le marché ou a déjà été mis en service de telle manière qu’il reste un système d’IA à haut risque en application de l’article 6; »
- [2] « c) il modifie la destination d’un système d’IA, y compris un système d’IA à usage général, qui n’a pas été classé à haut risque et a déjà été mis sur le marché ou mis en service de telle manière que le système d’IA concerné devient un système d’IA à haut risque conformément l’article 6. »
- [5] « «fournisseur», une personne physique ou morale, une autorité publique, une agence ou tout autre organisme qui développe ou fait développer un système d’IA ou un modèle d’IA à usage général et le met sur le marché ou met le système d’IA en service sous son propre nom ou sa propre marque, à titre onéreux ou gratuit; »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question concernant la responsabilité en cas d'erreur lors de l'utilisation normale d'un outil d'IA acheté, mais ils précisent les cas où la responsabilité peut changer de mains. En principe, le « fournisseur » est défini comme celui qui développe ou fait développer le système et le met sur le marché sous son nom [5]. Si vous avez simplement acheté l'outil sans le modifier ni le revendre sous votre marque, vous restez le déployeur et non le fournisseur, donc les extraits ne vous attribuent pas la responsabilité de l'erreur de l'outil. Cependant, vous seriez considéré comme un fournisseur, et donc soumis aux obligations du fournisseur, si vous commercialisez le système sous votre propre nom ou marque [2], si vous apportez une modification substantielle au système [2], ou si vous modifiez sa destination pour qu'il devienne un système à haut risque [2]. De plus, si l'erreur survient durant des « essais en conditions réelles », le fournisseur ou le fournisseur potentiel est responsable du préjudice causé [3].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : fournisseur du système d'IA ; utilisateur du système d'IA ; responsabilité du fournisseur ; responsabilité de l'utilisateur ; système d'IA à haut risque ; biais

Temps : recherche 22.4 s · génération 2.2 s (2298 tokens lus, 635 écrits, 518.3 tokens/s) · contrôle de pertinence 0.3 s · reformulation 0.3 s · attente des limites de l'API 32 s (non comptée)

## e24 — À partir de quand les règles de l'AI Act s'appliquent vraiment ? Qu'est-ce qui est déjà en vigueur ?

Article attendu : AI Act art. 113 — passage [1].

### Réponse du copilote

> L'AI Act est applicable dans son ensemble à partir du 2 août 2026 [1]. Cependant, certaines parties du règlement sont déjà en vigueur ou le seront avant cette date : les chapitres I et II s'appliquent à partir du 2 février 2025, « à l'exception de l'article 5, paragraphe 1, premier alinéa, points b bis) et b ter), et de l'article 5, paragraphes 1 bis et 1 ter, qui s'appliquent à partir du 2 décembre 2026 » [1]. Par ailleurs, le chapitre III, section 4, le chapitre V, le chapitre VII, le chapitre XII et l’article 78 s’appliquent à partir du 2 août 2025, « à l’exception de l’article 101 » [1]. Enfin, les règles relatives aux systèmes d'IA à haut risque (chapitre III, sections 1, 2 et 3) s'appliquent à partir du 2 décembre 2027 pour ceux classés en vertu de l'article 6, paragraphe 2, et de l'annexe III, et à partir du 2 août 2028 pour ceux classés en vertu de l'article 6, paragraphe 1, et de l'annexe I [1].

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
  [2] AI Act — règlement (UE) 2024/1689, article 1 : Objet
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_1
  [3] AI Act — règlement (UE) 2024/1689, article 111 : Systèmes d’IA déjà mis sur le marché ou mis en service et modèles d’IA à usage général déjà mis sur le marché
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_111
  [4] AI Act — règlement (UE) 2024/1689, article 2, paragraphe 13 : Champ d’application
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_2
  [5] AI Act — règlement (UE) 2024/1689, article 2, paragraphe 1 : Champ d’application
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_2

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
L'AI Act est applicable dans son ensemble à partir du 2 août 2026 [1]. Cependant, certaines parties du règlement sont déjà en vigueur ou le seront avant cette date : les chapitres I et II s'appliquent à partir du 2 février 2025, « à l'exception de l'article 5, paragraphe 1, premier alinéa, points b bis) et b ter), et de l'article 5, paragraphes 1 bis et 1 ter, qui s'appliquent à partir du 2 décembre 2026 » [1]. Par ailleurs, le chapitre III, section 4, le chapitre V, le chapitre VII, le chapitre XII et l’article 78 s’appliquent à partir du 2 août 2025, « à l’exception de l’article 101 » [1]. Enfin, les règles relatives aux systèmes d'IA à haut risque (chapitre III, sections 1, 2 et 3) s'appliquent à partir du 2 décembre 2027 pour ceux classés en vertu de l'article 6, paragraphe 2, et de l'annexe III, et à partir du 2 août 2028 pour ceux classés en vertu de l'article 6, paragraphe 1, et de l'annexe I [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : date d'entrée en vigueur ; date d'application ; obligations applicables ; dispositions en vigueur

Temps : recherche 25.6 s · génération 2.0 s (2991 tokens lus, 650 écrits, 449.5 tokens/s) · contrôle de pertinence 0.5 s · reformulation 0.3 s · attente des limites de l'API 22 s (non comptée)

## e25 — Mes salariés copient des données clients dans ChatGPT pour aller plus vite. C'est un problème ? Comment je peux encadrer ça ?

Article attendu : RGPD art. 32 ou RGPD art. 29 — passage [1].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 32 : Sécurité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_32
  [2] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [3] RGPD — règlement (UE) 2016/679, article 28, paragraphe 3 : Sous-traitant
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [4] RGPD — règlement (UE) 2016/679, article 28, paragraphe 1 : Sous-traitant
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [5] RGPD — règlement (UE) 2016/679, article 34 : Communication à la personne concernée d'une violation de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_34
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [4] « Lorsqu'un traitement doit être effectué pour le compte d'un responsable du traitement, celui-ci fait uniquement appel à des sous-traitants qui présentent des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées de manière à ce que le traitement réponde aux exigences du présent règlement et garantisse la protection des droits de la personne concernée. »
- [3] « Le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre, qui lie le sous-traitant à l'égard du responsable du traitement, définit l'objet et la durée du traitement, la nature et la finalité du traitement, le type de données à caractère personnel et les catégories de personnes concernées, et les obligations et les droits du responsable du traitement. »
- [3] « a) ne traite les données à caractère personnel que sur instruction documentée du responsable du traitement, y compris en ce qui concerne les transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale, à moins qu'il ne soit tenu d'y procéder en vertu du droit de l'Union ou du droit de l'État membre auquel le sous-traitant est soumis; dans ce cas, le sous-traitant informe le responsable du traitement de cette obligation juridique avant le traitement, sauf si le droit concerné interdit une telle information pour des motifs importants d'intérêt public; »
- [1] « le responsable du traitement et le sous-traitant mettent en œuvre les mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque, y compris entre autres, selon les besoins: a) la pseudonymisation et le chiffrement des données à caractère personnel; »
- [1] « Le responsable du traitement et le sous-traitant prennent des mesures afin de garantir que toute personne physique agissant sous l'autorité du responsable du traitement ou sous celle du sous-traitant, qui a accès à des données à caractère personnel, ne les traite pas, excepté sur instruction du responsable du traitement, à moins d'y être obligée par le droit de l'Union ou le droit d'un État membre. »
- [2] « Les États membres peuvent prévoir, par la loi ou au moyen de conventions collectives, des règles plus spécifiques pour assurer la protection des droits et libertés en ce qui concerne le traitement des données à caractère personnel des employés dans le cadre des relations de travail, aux fins, notamment, du recrutement, de l'exécution du contrat de travail, y compris le respect des obligations fixées par la loi ou par des conventions collectives, de la gestion, de la planification et de l'organisation du travail, de l'égalité et de la diversité sur le lieu de travail, de la santé et de la sécurité au travail, de la protection des biens appartenant à l'employeur ou au client, aux fins de l'exercice et de la jouissance des droits et des avantages liés à l'emploi, individuellement ou collectivement, ainsi qu'aux fins de la résiliation de la relation de travail. »

RÉPONSE :
Oui, c'est un problème si vous n'avez pas mis en place les garanties requises par le RGPD, car l'utilisation d'un outil externe comme ChatGPT implique un traitement de données par un tiers [4]. En tant que responsable du traitement, vous devez vous assurer que ce tiers présente des « garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées » [4]. Pour encadrer cette pratique, vous devez conclure un contrat ou un autre acte juridique avec le fournisseur de l'outil, qui définit notamment « l'objet et la durée du traitement, la nature et la finalité du traitement, le type de données à caractère personnel et les catégories de personnes concernées » [3]. Ce contrat doit prévoir que le sous-traitant « ne traite les données à caractère personnel que sur instruction documentée du responsable du traitement » [3]. De plus, vous et le sous-traitant devez mettre en œuvre des mesures de sécurité adaptées au risque, telles que « la pseudonymisation et le chiffrement des données à caractère personnel » [1]. Enfin, vous devez prendre des mesures pour garantir que vos salariés, qui agissent sous votre autorité, ne traitent les données « excepté sur instruction du responsable du traitement » [1]. Les passages trouvés ne traitent pas directement des règles spécifiques applicables aux outils d'intelligence artificielle (AI Act) ni des délais précis de notification en cas de violation, mais ils imposent le cadre contractuel et sécuritaire général du RGPD.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : traitement de données à caractère personnel ; responsable du traitement ; sous-traitant ; mesures techniques et organisationnelles appropriées ; sécurité des données ; transfert de données hors de l'Union européenne

Temps : recherche 27.4 s · génération 2.5 s (3264 tokens lus, 986 écrits, 477.3 tokens/s) · contrôle de pertinence 0.6 s · reformulation 0.3 s · attente des limites de l'API 60 s (non comptée)

## he01 — Comment je déclare la TVA chaque trimestre ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, annexe V : Déclaration UE de conformité
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_V
  [2] RGPD — règlement (UE) 2016/679, article 97 : Rapports de la Commission
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_97
  [3] RGPD — règlement (UE) 2016/679, article 27 : Représentants des responsables du traitement ou des sous-traitants qui ne sont pas établis dans l'Union
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_27
  [4] RGPD — règlement (UE) 2016/679, article 83, paragraphe 5 : Conditions générales pour imposer des amendes administratives
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

Reformulation de la question (termes ajoutés avant la recherche) : déclaration de TVA ; période d'imposition ; assujetti ; base d'imposition ; taux de TVA

Temps : recherche 27.5 s · génération 0.7 s (2728 tokens lus, 25 écrits, 450.2 tokens/s) · reformulation 0.5 s

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

Reformulation de la question (termes ajoutés avant la recherche) : préavis de démission ; contrat de travail à durée indéterminée ; salarié ; employeur

Temps : recherche 23.7 s · génération 0.7 s (2247 tokens lus, 25 écrits, 471.8 tokens/s) · reformulation 0.3 s

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

Temps : recherche 23.4 s · génération 0.6 s (3019 tokens lus, 25 écrits, 496.0 tokens/s) · reformulation 0.2 s
