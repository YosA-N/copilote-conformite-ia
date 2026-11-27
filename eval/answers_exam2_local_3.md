# Réponses du copilote — exam2_local_3

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 24/11/2026 à 15:50 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen3:4b-instruct` via Ollama 0.40.18 — température 0.1, contexte 8192 tokens, couches sur la carte graphique : toutes, 2000 tokens au plus par réponse
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_exam2.jsonl` (24 + 4 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| e01 | Je veux installer des caméras dans mon magasin et dans la salle de pause. J'en ai le droit ? Qu'est-ce que je dois dire à mes salariés ? | 4/5 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 63 s |
| e02 | Une ancienne cliente me demande d'effacer toutes ses données. On doit garder ses factures pour la comptabilité. Je dois quand même tout supprimer ? | 5/6 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([5]) : ignoré(s).; La réponse met entre « » un texte introuvable dans les extraits vérifiés : « pertinentes et limitées à ce qui est nécessaire ».; La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à condition qu' elles soient pertinentes et limitées » (et 1 autre(s)). Vérifiez-la dans les textes.; La réponse ne reprend que 5 des 6 cas énumérés au passage [1], sans dire qu'elle n'en cite qu'une partie. Vérifiez la liste complète. | 47 s |
| e03 | Combien de temps je peux garder les CV des candidats que je n'ai pas retenus ? | 0/0 | oui | — | 15 s |
| e04 | Notre association garde la liste des bénévoles (adresses, téléphones) dans un fichier Excel partagé sur Google Drive. C'est un problème ? | 1/2 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 42 s |
| e05 | Sur mon site web, j'utilise seulement Google Analytics. Je suis obligé de mettre un bandeau cookies ? | 5/5 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 46 s |
| e06 | La boîte mail de l'accueil a été piratée hier. Qu'est-ce que je dois faire ? Je dois prévenir quelqu'un ? | 6/6 | non | — | 45 s |
| e07 | Un prestataire extérieur gère notre paie. Je dois signer un contrat spécial avec lui pour les données ? | 3/3 | non | — | 35 s |
| e08 | Je peux envoyer notre newsletter à mes anciens clients sans leur demander leur accord ? | 5/5 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 48 s |
| e09 | Un salarié me demande une copie de toutes les données que j'ai sur lui, même les mails où on parle de lui. Je dois tout lui donner ? J'ai combien de temps pour répondre ? | 4/4 | non | La réponse formule une exception qui ne reprend pas les extraits vérifiés : « sauf si la demande est complexe ou si le nombre de demandes est élevé, ». Vérifiez-la dans les textes. | 45 s |
| e10 | Un salarié est parti de l'entreprise. Je peux encore lire sa boîte mail professionnelle ? | 2/2 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 53 s |
| e11 | Dans notre organisme de formation, on demande aux stagiaires leur numéro de sécurité sociale et des informations sur leur handicap. On a le droit ? | 1/1 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 36 s |
| e12 | Je peux suivre les véhicules de mes techniciens par GPS ? | 0/0 | oui | — | 18 s |
| e13 | On veut publier sur Facebook des photos des bénévoles prises pendant notre fête annuelle. Il faut leur accord écrit ? | 0/0 | oui | — | 25 s |
| e14 | On a 8 salariés. On doit tenir un registre des traitements et nommer un DPO ? | 3/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 56 s |
| e15 | Notre logiciel de gestion des clients est hébergé aux États-Unis. C'est autorisé ? | 5/5 | non | La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à condition que l'un des mécanismes prévus par le RGPD soit respecté ». Vérifiez-la dans les textes. | 51 s |
| e16 | On ne crée pas d'IA, on utilise juste des outils comme ChatGPT. Est-ce que l'AI Act nous concerne quand même ? | 4/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 45 s |
| e17 | Je voudrais utiliser un logiciel d'IA qui trie automatiquement les CV. C'est interdit ? Sinon, quelles règles je dois respecter ? | 2/3 | non | Réponse coupée : le modèle a atteint la limite de 2000 tokens (LLM_MAX_TOKENS), la fin de la réponse manque. Posez une question plus précise ou augmentez LLM_MAX_TOKENS dans .env.; 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1]) : ignoré(s).; La réponse ne cite aucun passage et une phrase ne reprend pas les extraits vérifiés : « Non, l’utilisation d’un logiciel d’IA qui trie automatiquement les CV n’est pas interdite par l’AI Act. ». Vérifiez-la dans les textes. | 83 s |
| e18 | On a mis un chatbot sur notre site. On doit dire aux visiteurs qu'ils parlent avec une machine ? | 4/4 | non | La réponse cite [5] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.; La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Cependant, cette information ne doit pas être cachée ou trompée, sauf si elle ressort clairement du point de vue d’une … ». Vérifiez ce point.; La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui: vous devez indiquer clairement aux visiteurs que vous interagissez avec un système d’IA, car le chatbot est un … » (et 2 autre(s)). Vérifiez qui est concerné. | 39 s |
| e19 | Notre organisme de formation veut utiliser une IA pour corriger les examens et noter les stagiaires. C'est risqué ? | 4/4 | non | La réponse cite [3], [4] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations. | 33 s |
| e20 | On m'a dit que je dois former mes salariés à l'IA. C'est vraiment obligatoire ? | 1/1 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 38 s |
| e21 | On crée nos visuels pour les réseaux sociaux avec une IA. Il faut écrire qu'ils sont générés par IA ? | 1/2 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([3]) : ignoré(s).; La réponse cite [3] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.; La réponse formule une exception qui ne reprend pas les extraits vérifiés : « sauf dans des cas spécifiques comme une utilisation autorisée par la loi pour des ». Vérifiez-la dans les textes. | 39 s |
| e22 | Un fournisseur nous propose un outil qui analyse les émotions des salariés pendant les visioconférences. On a le droit de l'utiliser ? | 3/3 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 38 s |
| e23 | Si l'outil d'IA qu'on a acheté se trompe et écarte injustement un candidat, qui est responsable : moi ou le fournisseur ? | 4/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 46 s |
| e24 | À partir de quand les règles de l'AI Act s'appliquent vraiment ? Qu'est-ce qui est déjà en vigueur ? | 7/7 | non | — | 66 s |
| e25 | Mes salariés copient des données clients dans ChatGPT pour aller plus vite. C'est un problème ? Comment je peux encadrer ça ? | 3/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 58 s |
| he01 | Comment je déclare la TVA chaque trimestre ? | 0/0 | oui | — | 15 s |
| he02 | Si un salarié en CDI démissionne, combien de temps dure son préavis ? | 0/0 | oui | — | 14 s |
| he03 | Tu as des idées pour organiser une fête de fin d'année pour les bénévoles avec un petit budget ? | 0/0 | oui | — | 19 s |

## e01 — Je veux installer des caméras dans mon magasin et dans la salle de pause. J'en ai le droit ? Qu'est-ce que je dois dire à mes salariés ?

Article attendu : RGPD art. 6, paragraphe 1 ou RGPD art. 13 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [2] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 3 : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [3] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points a) à e) : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [4] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 2 : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [5] AI Act — règlement (UE) 2024/1689, article 75 bis, point e : Pouvoirs de surveillance et de contrôle du Bureau de l'IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_75a
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »  
- [2] « Aux fins du paragraphe 1, premier alinéa, point h), et du paragraphe 2, chaque utilisation à des fins répressives d’un système d’identification biométrique à distance en temps réel dans des espaces accessibles au public est subordonnée à une autorisation préalable octroyée par une autorité judiciaire ou une autorité administrative indépendante dont la décision est contraignante de l’État membre dans lequel cette utilisation doit avoir lieu, délivrée sur demande motivée et conformément aux règles détaillées du droit national visées au paragraphe 5. Toutefois, dans une situation d’urgence dûment justifiée, il est possible de commencer à utiliser ce système sans autorisation à condition que cette autorisation soit demandée sans retard injustifié, au plus tard dans les 24 heures. Si cette autorisation est rejetée, il est mis fin à l’utilisation avec effet immédiat, et toutes les données, ainsi que les résultats et sorties de cette utilisation, sont immédiatement mis au rebut et supprimés. »  
- [3] « la mise sur le marché, la mise en service ou l’utilisation de systèmes d’IA pour mener des évaluations des risques des personnes physiques visant à évaluer ou à prédire le risque qu’une personne physique commette une infraction pénale, uniquement sur la base du profilage d’une personne physique ou de l’évaluation de ses traits de personnalité ou caractéristiques; cette interdiction ne s’applique pas aux systèmes d’IA utilisés pour étayer l’évaluation humaine de l’implication d’une personne dans une activité criminelle, qui est déjà fondée sur des faits objectifs et vérifiables, directement liés à une activité criminelle; »  
- [4] « L’utilisation de systèmes d’identification biométriques à distance en temps réel dans des espaces accessibles au public à des fins répressives en vue de la réalisation de l’un des objectifs énumérés au paragraphe 1, premier alinéa, point h), n’est déployée aux fins énoncées audit point, que pour confirmer l’identité de la personne spécifiquement ciblée et tient compte des éléments suivants: a) la nature de la situation donnant lieu à un éventuel recours au système, en particulier la gravité, la probabilité et l’ampleur du préjudice qui serait causé si le système n’était pas utilisé; b) les conséquences de l’utilisation du système sur les droits et libertés de toutes les personnes concernées, notamment la gravité, la probabilité et l’ampleur de ces conséquences. »  
- [5] « Si une inspection sur place des locaux commerciaux, des terrains ou des biens immobiliers nécessite l'autorisation d'une autorité judiciaire conformément au droit national, le Bureau de l'IA demande cette autorisation. Cette autorisation peut également être demandée par le Bureau de l'IA à titre préventif. »

RÉPONSE :  
Non, vous n’avez pas le droit d’installer des caméras dans votre magasin et dans la salle de pause simplement parce que vous le souhaitez. L’installation de systèmes d’identification biométrique à distance en temps réel dans des espaces accessibles au public, comme un magasin ou une salle de pause, est interdite à des fins répressives (c’est-à-dire pour surveiller ou identifier les personnes) sauf si une autorisation préalable est obtenue par une autorité judiciaire ou administrative indépendante dont la décision est contraignante [2]. Cette autorisation doit être demandée sur demande motivée et conformément aux règles du droit national [2].  

En outre, l’utilisation de ces systèmes ne peut être déployée que pour confirmer l’identité d’une personne spécifiquement ciblée, et doit tenir compte de la gravité, de la probabilité et de l’ampleur du préjudice qui serait causé si le système n’était pas utilisé, ainsi que des conséquences sur les droits et libertés des personnes concernées [4].  

Concernant vos salariés, vous devez les informer clairement que des caméras sont installées dans le magasin et la salle de pause, et que ces caméras sont utilisées pour des raisons de sécurité, mais pas pour identifier ou surveiller les personnes individuellement. Si les caméras sont utilisées à des fins répressives (comme identifier une personne), alors une autorisation préalable de l’État membre est nécessaire, et vous devez les informer de cette autorisation [2].  

Cependant, les extraits ne mentionnent pas une obligation de communication spécifique à vos salariés, ni une règle sur l’information préalable à l’installation de caméras non biométriques. Ainsi, bien que les caméras soient autorisées dans certains cas, leur utilisation à des fins de surveillance ou d’identification biométrique est soumise à des conditions strictes, notamment une autorisation préalable [2]. Si vous installez des caméras sans utilisation de biométrie, les obligations de transparence (comme l’information des personnes concernées) s’appliquent selon l’article 50, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée [1].  

En résumé : vous pouvez installer des caméras dans votre magasin et la salle de pause, mais seulement si elles ne sont pas utilisées à des fins répressives (comme identifier des personnes) ; dans ce cas, une autorisation préalable de l’État membre est requise [2]. Vous devez informer vos salariés de l’existence des caméras et de leur utilisation, en particulier si elles sont utilisées pour des raisons de sécurité, mais pas pour identifier les personnes individuellement. Si les caméras sont utilisées à des fins de surveillance, vous devez les informer de la nature de l’utilisation, en tenant compte de la transparence exigée par l’article 50 [1].
```

</details>

Temps : recherche 2.5 s · génération 53.2 s (4049 tokens lus, 1528 écrits, 30.7 tokens/s) · contrôle de pertinence 7.2 s

## e02 — Une ancienne cliente me demande d'effacer toutes ses données. On doit garder ses factures pour la comptabilité. Je dois quand même tout supprimer ?

Article attendu : RGPD art. 17 — passage [1].

### Réponse du copilote

> Non, vous n'avez pas obligation d'effacer toutes les données de l'ancienne cliente, car le traitement des factures pour la comptabilité relève d'une finalité légitime et nécessaire, conforme à l'article 5, point c) du RGPD, qui exige que les données soient « pertinentes et limitées à ce qui est nécessaire ». Cela signifie que les données peuvent être conservées si elles sont nécessaires pour des finalités comme la comptabilité, à condition qu'elles soient pertinentes et limitées. L'effacement ne s'applique pas dans la mesure où le traitement est nécessaire à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques, conformément à l'article 89, paragraphe 1, « dans la mesure où le droit visé au paragraphe 1 est susceptible de rendre impossible ou de compromettre gravement la réalisation des objectifs dudit traitement » [1]. Ainsi, les factures peuvent être conservées pour la comptabilité, à moins que cette finalité ne soit incompatible avec les autres finalités initiales, ce qui n'est pas le cas ici. Les données à caractère personnel ne doivent pas être effacées si elles sont nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « les données à caractère personnel ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées d'une autre manière; »
  [1] « les données à caractère personnel ont fait l'objet d'un traitement illicite; »
  [1] « les données à caractère personnel doivent être effacées pour respecter une obligation légale qui est prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis; »
  [1] « les données à caractère personnel ont été collectées dans le cadre de l'offre de services de la société de l'information visée à l'article 8, paragraphe 1. »
  [1] « Les paragraphes 1 et 2 ne s'appliquent pas dans la mesure où ce traitement est nécessaire: … à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, dans la mesure où le droit visé au paragraphe 1 est susceptible de rendre impossible ou de compromettre gravement la réalisation des objectifs dudit traitement; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 17 : Droit à l'effacement («droit à l'oubli») (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_17
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 19 : Obligation de notification en ce qui concerne la rectification ou l'effacement de données à caractère personnel ou la limitation du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_19
  [3] RGPD — règlement (UE) 2016/679, article 12, paragraphe 5 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [4] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [5] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([5]) : ignoré(s).
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « pertinentes et limitées à ce qui est nécessaire ».
Attention : La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à condition qu' elles soient pertinentes et limitées » (et 1 autre(s)). Vérifiez-la dans les textes.
Attention : La réponse ne reprend que 5 des 6 cas énumérés au passage [1], sans dire qu'elle n'en cite qu'une partie. Vérifiez la liste complète.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « les données à caractère personnel ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées d'une autre manière; »  
- [1] « les données à caractère personnel ont fait l'objet d'un traitement illicite; »  
- [1] « les données à caractère personnel doivent être effacées pour respecter une obligation légale qui est prévue par le droit de l'Union ou par le droit de l'État membre auquel le responsable du traitement est soumis; »  
- [1] « les données à caractère personnel ont été collectées dans le cadre de l'offre de services de la société de l'information visée à l'article 8, paragraphe 1. »  
- [1] « Les paragraphes 1 et 2 ne s'appliquent pas dans la mesure où ce traitement est nécessaire: … à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques conformément à l'article 89, paragraphe 1, dans la mesure où le droit visé au paragraphe 1 est susceptible de rendre impossible ou de compromettre gravement la réalisation des objectifs dudit traitement; »  
- [5] « les données à caractère personnel doivent être adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités pour lesquelles elles sont traitées (minimisation des données); »  

RÉPONSE :  
Non, vous n'avez pas obligation d'effacer toutes les données de l'ancienne cliente, car le traitement des factures pour la comptabilité relève d'une finalité légitime et nécessaire, conforme à l'article 5, point c) du RGPD, qui exige que les données soient « pertinentes et limitées à ce qui est nécessaire ». Cela signifie que les données peuvent être conservées si elles sont nécessaires pour des finalités comme la comptabilité, à condition qu'elles soient pertinentes et limitées. L'effacement ne s'applique pas dans la mesure où le traitement est nécessaire à des fins archivistiques dans l'intérêt public, à des fins de recherche scientifique ou historique ou à des fins statistiques, conformément à l'article 89, paragraphe 1, « dans la mesure où le droit visé au paragraphe 1 est susceptible de rendre impossible ou de compromettre gravement la réalisation des objectifs dudit traitement » [1]. Ainsi, les factures peuvent être conservées pour la comptabilité, à moins que cette finalité ne soit incompatible avec les autres finalités initiales, ce qui n'est pas le cas ici. Les données à caractère personnel ne doivent pas être effacées si elles sont nécessaires au regard des finalités pour lesquelles elles ont été collectées ou traitées [1].
```

</details>

Temps : recherche 2.2 s · génération 39.1 s (3302 tokens lus, 640 écrits, 33.1 tokens/s) · contrôle de pertinence 5.4 s

## e03 — Combien de temps je peux garder les CV des candidats que je n'ai pas retenus ?

Article attendu : RGPD art. 5 — absent des passages donnés au modèle.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 36, paragraphe 9 : Modifications apportées aux notifications
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_36
  [2] AI Act — règlement (UE) 2024/1689, article 36, paragraphe 1 : Modifications apportées aux notifications
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_36
  [3] RGPD — règlement (UE) 2016/679, article 43, paragraphe 4 : Organismes de certification
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_43
  [4] RGPD — règlement (UE) 2016/679, article 43, paragraphe 1 : Organismes de certification
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_43
  [5] AI Act — règlement (UE) 2024/1689, article 36, paragraphe 5 : Modifications apportées aux notifications
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_36

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun  
RÉPONSE : Les textes trouvés ne traitent pas de la conservation des dossiers de candidats ou de la durée de conservation des données personnelles dans le cadre de recrutement. La question concernant la durée de conservation des CV des candidats n'est pas abordée dans les passages fournis.
```

</details>

Temps : recherche 2.3 s · génération 12.8 s (2278 tokens lus, 75 écrits, 36.7 tokens/s)

## e04 — Notre association garde la liste des bénévoles (adresses, téléphones) dans un fichier Excel partagé sur Google Drive. C'est un problème ?

Article attendu : RGPD art. 32 ou RGPD art. 28, paragraphe 1 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 91 : Règles existantes des églises et associations religieuses en matière de protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_91
  [2] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [3] RGPD — règlement (UE) 2016/679, article 40, paragraphe 1 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [4] RGPD — règlement (UE) 2016/679, article 75 : Secrétariat
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_75
  [5] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [5] « Chaque responsable du traitement et, le cas échéant, le représentant du responsable du traitement tiennent un registre des activités de traitement effectuées sous leur responsabilité. Ce registre comporte toutes les informations suivantes: … c) les catégories de destinataires auxquels les données à caractère personnel ont été ou seront communiquées, y compris les destinataires dans des pays tiers ou des organisations internationales; … f) dans la mesure du possible, les délais prévus pour l'effacement des différentes catégories de données; … g) dans la mesure du possible, une description générale des mesures de sécurité techniques et organisationnelles visées à l'article 32, paragraphe 1. »  
- [5] « Les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10. »  

RÉPONSE :  
Oui, cela peut constituer un problème, car votre association doit tenir un registre des activités de traitement, notamment les données à caractère personnel des bénévoles (adresses, téléphones), conformément à l’article 30 du RGPD [5]. Ce registre doit être mis à la disposition de l'autorité de contrôle sur demande [5]. Cependant, cette obligation ne s'applique pas à une organisation comptant moins de 250 employés, sauf si le traitement est susceptible de comporter un risque pour les droits et libertés des personnes concernées, s’il n’est pas occasionnel ou s’il porte sur des catégories particulières de données [5]. Puisque la liste des bénévoles est un traitement de données personnelles, il est nécessaire de vérifier si ce traitement relève de ces cas spécifiques. En l’absence de tel risque, le simple fait de garder les données dans un fichier Excel partagé sur Google Drive ne suffit pas à garantir la conformité, car le registre doit être structuré et accessible selon les exigences du RGPD [5].
```

</details>

Temps : recherche 2.2 s · génération 36.3 s (3261 tokens lus, 565 écrits, 33.4 tokens/s) · contrôle de pertinence 3.7 s

## e05 — Sur mon site web, j'utilise seulement Google Analytics. Je suis obligé de mettre un bandeau cookies ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 42 : Certification
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_42
  [2] AI Act — règlement (UE) 2024/1689, article 4 bis : Traitement de catégories particulières de données à caractère personnel à des fins de détection et de correction des biais
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_4a
  [3] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 4 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [4] AI Act — règlement (UE) 2024/1689, annexe X, point 5 b : Actes législatifs de l'Union relatifs aux systèmes d'information à grande échelle au sein de l'espace de liberté, de sécurité et de justice
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_X
  [5] AI Act — règlement (UE) 2024/1689, article 48 : Marquage CE
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_48
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] RGPD — règlement (UE) 2016/679 — Article 42 : Certification  
- [2] AI Act — règlement (UE) 2024/1689 — Article 4 bis : Traitement de catégories particulières de données à caractère personnel à des fins de détection et de correction des biais  
- [3] AI Act — règlement (UE) 2024/1689 — Article 50 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA  
- [4] AI Act — règlement (UE) 2024/1689 — Annexe X : Actes législatifs de l'Union relatifs aux systèmes d'information à grande échelle au sein de l'espace de liberté, de sécurité et de justice  
- [5] AI Act — règlement (UE) 2024/1689 — Article 48 : Marquage CE  

RÉPONSE :  
Les passages trouvés ne traitent pas directement de l'utilisation de Google Analytics sur un site web ni de l'obligation de mettre un bandeau cookies. Aucun des textes ne mentionne explicitement le traitement de données par Google Analytics, ni la nécessité d'un bandeau cookies pour les outils de suivi de trafic. La question de l'obligation d'un bandeau cookies relève du RGPD, notamment de l'article 5-1, sur le traitement des données personnelles, et de l'article 4, sur les consentements, mais ces dispositions ne sont pas reproduites dans les extraits fournis. Par conséquent, les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Temps : recherche 2.2 s · génération 39.5 s (4009 tokens lus, 412 écrits, 31.8 tokens/s) · contrôle de pertinence 4.3 s

## e06 — La boîte mail de l'accueil a été piratée hier. Qu'est-ce que je dois faire ? Je dois prévenir quelqu'un ?

Article attendu : RGPD art. 33 ou RGPD art. 34 — passage [1].

### Réponse du copilote

> Oui : vous devez prévenir l'autorité de contrôle compétente (RGPD, article 33, [1]), car une violation de données à caractère personnel a eu lieu. Cette notification doit être faite dans les meilleurs délais, et si possible, dans les 72 heures après en avoir pris connaissance, à moins que la violation ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques [1]. Si la violation est susceptible d'engendrer un risque élevé, vous devez également communiquer la violation à la personne concernée dans les meilleurs délais [2]. Vous devez également noter que, si les données concernées ont été communiquées à des destinataires, vous devez les informer de toute rectification ou effacement de données [3]. La notification à l'autorité de contrôle est obligatoire, et elle doit inclure les informations prévues à l'article 33, paragraphe 3, points b), c) et d) [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. Lorsque la notification à l'autorité de contrôle n'a pas lieu dans les 72 heures, elle est accompagnée des motifs du retard. »
  [1] « Le sous-traitant notifie au responsable du traitement toute violation de données à caractère personnel dans les meilleurs délais après en avoir pris connaissance. »
  [2] « Lorsqu'une violation de données à caractère personnel est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement communique la violation de données à caractère personnel à la personne concernée dans les meilleurs délais. »
  [2] « La communication à la personne concernée visée au paragraphe 1 du présent article décrit, en des termes clairs et simples, la nature de la violation de données à caractère personnel et contient au moins les informations et mesures visées à l'article 33, paragraphe 3, points b), c) et d). »
  [3] « Le responsable du traitement notifie à chaque destinataire auquel les données à caractère personnel ont été communiquées toute rectification ou tout effacement de données à caractère personnel ou toute limitation du traitement effectué conformément à l'article 16, à l'article 17, paragraphe 1, et à l'article 18, à moins qu'une telle communication se révèle impossible ou exige des efforts disproportionnés. »
  [4] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: … »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 33 : Notification à l'autorité de contrôle d'une violation de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_33
  [2] RGPD — règlement (UE) 2016/679, article 34 : Communication à la personne concernée d'une violation de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_34
  [3] RGPD — règlement (UE) 2016/679, article 19 : Obligation de notification en ce qui concerne la rectification ou l'effacement de données à caractère personnel ou la limitation du traitement (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_19
  [4] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
Passages consultés mais non cités :
  [5] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 4 : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. Lorsque la notification à l'autorité de contrôle n'a pas lieu dans les 72 heures, elle est accompagnée des motifs du retard. »
- [1] « Le sous-traitant notifie au responsable du traitement toute violation de données à caractère personnel dans les meilleurs délais après en avoir pris connaissance. »
- [2] « Lorsqu'une violation de données à caractère personnel est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement communique la violation de données à caractère personnel à la personne concernée dans les meilleurs délais. »
- [2] « La communication à la personne concernée visée au paragraphe 1 du présent article décrit, en des termes clairs et simples, la nature de la violation de données à caractère personnel et contient au moins les informations et mesures visées à l'article 33, paragraphe 3, points b), c) et d). »
- [3] « Le responsable du traitement notifie à chaque destinataire auquel les données à caractère personnel ont été communiquées toute rectification ou tout effacement de données à caractère personnel ou toute limitation du traitement effectué conformément à l'article 16, à l'article 17, paragraphe 1, et à l'article 18, à moins qu'une telle communication se révèle impossible ou exige des efforts disproportionnés. »
- [4] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: … »

RÉPONSE :
Oui : vous devez prévenir l'autorité de contrôle compétente (RGPD, article 33, [1]), car une violation de données à caractère personnel a eu lieu. Cette notification doit être faite dans les meilleurs délais, et si possible, dans les 72 heures après en avoir pris connaissance, à moins que la violation ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques [1]. Si la violation est susceptible d'engendrer un risque élevé, vous devez également communiquer la violation à la personne concernée dans les meilleurs délais [2]. Vous devez également noter que, si les données concernées ont été communiquées à des destinataires, vous devez les informer de toute rectification ou effacement de données [3]. La notification à l'autorité de contrôle est obligatoire, et elle doit inclure les informations prévues à l'article 33, paragraphe 3, points b), c) et d) [2].
```

</details>

Temps : recherche 2.2 s · génération 40.7 s (3231 tokens lus, 711 écrits, 33.2 tokens/s) · contrôle de pertinence 2.5 s

## e07 — Un prestataire extérieur gère notre paie. Je dois signer un contrat spécial avec lui pour les données ?

Article attendu : RGPD art. 28, paragraphe 3 — absent des passages donnés au modèle.

### Réponse du copilote

> Oui : vous devez signer un contrat spécial avec le prestataire extérieur gérant votre paie, car il s'agit d'un sous-traitant qui traite des données à caractère personnel pour votre organisation [4]. Ce contrat doit inclure des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées afin que le traitement réponde aux exigences du RGPD [2]. Si ce prestataire recrute d'autres prestataires (par exemple, pour gérer les calculs ou les déclarations), les mêmes obligations s'appliquent par contrat ou autre acte juridique [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Lorsqu'un sous-traitant recrute un autre sous-traitant pour mener des activités de traitement spécifiques pour le compte du responsable du traitement, les mêmes obligations en matière de protection de données que celles fixées dans le contrat ou un autre acte juridique entre le responsable du traitement et le sous-traitant conformément au paragraphe 3, sont imposées à cet autre sous-traitant par contrat ou au moyen d'un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre, en particulier pour ce qui est de présenter des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées de manière à ce que le traitement réponde aux exigences du présent règlement. »
  [2] « Lorsqu'un traitement doit être effectué pour le compte d'un responsable du traitement, celui-ci fait uniquement appel à des sous-traitants qui présentent des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées de manière à ce que le traitement réponde aux exigences du présent règlement et garantisse la protection des droits de la personne concernée. »
  [4] « «sous-traitant», la personne physique ou morale, l'autorité publique, le service ou un autre organisme qui traite des données à caractère personnel pour le compte du responsable du traitement; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 28, paragraphe 4 : Sous-traitant (version du 2016-05-04)
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
- [1] « Lorsqu'un sous-traitant recrute un autre sous-traitant pour mener des activités de traitement spécifiques pour le compte du responsable du traitement, les mêmes obligations en matière de protection de données que celles fixées dans le contrat ou un autre acte juridique entre le responsable du traitement et le sous-traitant conformément au paragraphe 3, sont imposées à cet autre sous-traitant par contrat ou au moyen d'un autre acte juridique au titre du droit de l'Union ou du droit d'un État membre, en particulier pour ce qui est de présenter des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées de manière à ce que le traitement réponde aux exigences du présent règlement. »  
- [2] « Lorsqu'un traitement doit être effectué pour le compte d'un responsable du traitement, celui-ci fait uniquement appel à des sous-traitants qui présentent des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées de manière à ce que le traitement réponde aux exigences du présent règlement et garantisse la protection des droits de la personne concernée. »  
- [4] « «sous-traitant», la personne physique ou morale, l'autorité publique, le service ou un autre organisme qui traite des données à caractère personnel pour le compte du responsable du traitement; »  

RÉPONSE :  
Oui : vous devez signer un contrat spécial avec le prestataire extérieur gérant votre paie, car il s'agit d'un sous-traitant qui traite des données à caractère personnel pour votre organisation [4]. Ce contrat doit inclure des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées afin que le traitement réponde aux exigences du RGPD [2]. Si ce prestataire recrute d'autres prestataires (par exemple, pour gérer les calculs ou les déclarations), les mêmes obligations s'appliquent par contrat ou autre acte juridique [1].
```

</details>

Temps : recherche 2.2 s · génération 27.9 s (2697 tokens lus, 474 écrits, 34.8 tokens/s) · contrôle de pertinence 4.8 s

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
  [2] RGPD — règlement (UE) 2016/679, article 80 : Représentation des personnes concernées
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_80
  [3] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [4] RGPD — règlement (UE) 2016/679, article 22 : Décision individuelle automatisée, y compris le profilage
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_22
  [5] RGPD — règlement (UE) 2016/679, article 7 : Conditions applicables au consentement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_7
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « La personne concernée a le droit de s'opposer à tout moment, pour des raisons tenant à sa situation particulière, à un traitement des données à caractère personnel la concernant fondé sur l'article 6, paragraphe 1, point e) ou f), y compris un profilage fondé sur ces dispositions. »  
- [1] « Lorsque les données à caractère personnel sont traitées à des fins de prospection, la personne concernée a le droit de s'opposer à tout moment au traitement des données à caractère personnel la concernant à de telles fins de prospection, y compris au profilage dans la mesure où il est lié à une telle prospection. »  
- [1] « Lorsque la personne concernée s'oppose au traitement à des fins de prospection, les données à caractère personnel ne sont plus traitées à ces fins. »  
- [4] « La personne concernée a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé, y compris le profilage, produisant des effets juridiques la concernant ou l'affectant de manière significative de façon similaire. »  
- [5] « Dans les cas où le traitement repose sur le consentement, le responsable du traitement est en mesure de démontrer que la personne concernée a donné son consentement au traitement de données à caractère personnel la concernant. »  

RÉPONSE :  
Non : vous ne pouvez pas envoyer une newsletter à vos anciens clients sans leur demander leur accord, car le traitement des données à caractère personnel à des fins de prospection (comme une newsletter) relève du droit d'opposition de la personne concernée (RGPD, article 21, paragraphe 1 et 2) [1]. Ce droit s'applique même aux anciens clients, car le traitement à des fins de prospection est concerné, y compris le profilage lié à cette prospection [1]. Le fait que les données soient déjà collectées ne justifie pas le traitement sans consentement. Le consentement est une base légale obligatoire pour le traitement de données à caractère personnel (RGPD, article 7, paragraphe 1) [5], et il doit être donné librement, clairement et de manière distincte [5]. Aucun autre fondement juridique (comme le droit d'opposition ou le consentement implicite) ne permet de traiter les données sans accord explicite. Le traitement automatisé, comme le fait d'envoyer une newsletter, peut être considéré comme une décision fondée sur un traitement automatisé, ce qui implique un droit de ne pas être soumis à une telle décision (RGPD, article 22, paragraphe 1) [4].
```

</details>

Temps : recherche 2.2 s · génération 40.8 s (3510 tokens lus, 629 écrits, 32.7 tokens/s) · contrôle de pertinence 4.6 s

## e09 — Un salarié me demande une copie de toutes les données que j'ai sur lui, même les mails où on parle de lui. Je dois tout lui donner ? J'ai combien de temps pour répondre ?

Article attendu : RGPD art. 15 ou RGPD art. 12, paragraphe 3 — passage [1].

### Réponse du copilote

> Non, vous n'avez pas l'obligation de fournir toutes les données, y compris les mails où on parle de vous, car le droit d'accès ne porte pas atteinte aux droits et libertés d'autrui [4], et les données doivent être fournies de manière appropriée, sans dépasser les données personnelles strictement liées au traitement [3]. Vous devez fournir une copie des données à caractère personnel faisant l'objet d'un traitement, mais pas nécessairement toutes les communications, notamment si elles ne sont pas directement liées au traitement [3]. Vous devez répondre dans un délai d'un mois à compter de la réception de la demande [1], sauf si la demande est complexe ou si le nombre de demandes est élevé, auquel cas le délai peut être prolongé de deux mois [1]. Ce délai peut être prolongé, mais vous devez informer la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande [1]. Lorsque la demande est faite par voie électronique, les informations sont fournies par voie électronique, à moins que la personne concernée ne demande qu'il en soit autrement [1] et [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. Lorsque la personne concernée présente sa demande sous une forme électronique, les informations sont fournies par voie électronique lorsque cela est possible, à moins que la personne concernée ne demande qu'il en soit autrement. »
  [3] « Le responsable du traitement fournit une copie des données à caractère personnel faisant l'objet d'un traitement. Le responsable du traitement peut exiger le paiement de frais raisonnables basés sur les coûts administratifs pour toute copie supplémentaire demandée par la personne concernée. Lorsque la personne concernée présente sa demande par voie électronique, les informations sont fournies sous une forme électronique d'usage courant, à moins que la personne concernée ne demande qu'il en soit autrement. »
  [4] « a) dans un délai raisonnable après avoir obtenu les données à caractère personnel, mais ne dépassant pas un mois, eu égard aux circonstances particulières dans lesquelles les données à caractère personnel sont traitées; »
  [5] « le cas échéant, le fait que le responsable du traitement a l'intention d'effectuer un transfert de données à caractère personnel à un destinataire dans un pays tiers ou une organisation internationale, et l'existence ou l'absence d'une décision d'adéquation rendue par la Commission ou, dans le cas des transferts visés à l'article 46 ou 47, ou à l'article 49, paragraphe 1, deuxième alinéa, la référence aux garanties appropriées ou adaptées et les moyens d'en obtenir une copie ou l'endroit où elles ont été mises à disposition; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 12, paragraphe 3 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [3] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [4] RGPD — règlement (UE) 2016/679, article 14, paragraphe 3 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 1 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
Attention : La réponse formule une exception qui ne reprend pas les extraits vérifiés : « sauf si la demande est complexe ou si le nombre de demandes est élevé, ». Vérifiez-la dans les textes.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. Lorsque la personne concernée présente sa demande sous une forme électronique, les informations sont fournies par voie électronique lorsque cela est possible, à moins que la personne concernée ne demande qu'il en soit autrement. »  
- [3] « Le responsable du traitement fournit une copie des données à caractère personnel faisant l'objet d'un traitement. Le responsable du traitement peut exiger le paiement de frais raisonnables basés sur les coûts administratifs pour toute copie supplémentaire demandée par la personne concernée. Lorsque la personne concernée présente sa demande par voie électronique, les informations sont fournies sous une forme électronique d'usage courant, à moins que la personne concernée ne demande qu'il en soit autrement. »  
- [4] « a) dans un délai raisonnable après avoir obtenu les données à caractère personnel, mais ne dépassant pas un mois, eu égard aux circonstances particulières dans lesquelles les données à caractère personnel sont traitées; »  
- [5] « le cas échéant, le fait que le responsable du traitement a l'intention d'effectuer un transfert de données à caractère personnel à un destinataire dans un pays tiers ou une organisation internationale, et l'existence ou l'absence d'une décision d'adéquation rendue par la Commission ou, dans le cas des transferts visés à l'article 46 ou 47, ou à l'article 49, paragraphe 1, deuxième alinéa, la référence aux garanties appropriées ou adaptées et les moyens d'en obtenir une copie ou l'endroit où elles ont été mises à disposition; »

RÉPONSE :  
Non, vous n'avez pas l'obligation de fournir toutes les données, y compris les mails où on parle de vous, car le droit d'accès ne porte pas atteinte aux droits et libertés d'autrui [4], et les données doivent être fournies de manière appropriée, sans dépasser les données personnelles strictement liées au traitement [3]. Vous devez fournir une copie des données à caractère personnel faisant l'objet d'un traitement, mais pas nécessairement toutes les communications, notamment si elles ne sont pas directement liées au traitement [3]. Vous devez répondre dans un délai d'un mois à compter de la réception de la demande [1], sauf si la demande est complexe ou si le nombre de demandes est élevé, auquel cas le délai peut être prolongé de deux mois [1]. Ce délai peut être prolongé, mais vous devez informer la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande [1]. Lorsque la demande est faite par voie électronique, les informations sont fournies par voie électronique, à moins que la personne concernée ne demande qu'il en soit autrement [1] et [3].
```

</details>

Temps : recherche 2.2 s · génération 39.7 s (2902 tokens lus, 800 écrits, 33.9 tokens/s) · contrôle de pertinence 3.5 s

## e10 — Un salarié est parti de l'entreprise. Je peux encore lire sa boîte mail professionnelle ?

Article attendu : RGPD art. 5 ou RGPD art. 6, paragraphe 1 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [2] RGPD — règlement (UE) 2016/679, article 47, paragraphe 2, points a) à k) : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
  [3] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [4] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30
  [5] RGPD — règlement (UE) 2016/679, article 20 : Droit à la portabilité des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_20
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [3] « le droit d'obtenir une copie visé au paragraphe 3 ne porte pas atteinte aux droits et libertés d'autrui. »  
- [4] « les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10. »  

RÉPONSE :  
Oui, vous pouvez encore lire la boîte mail professionnelle d’un salarié parti de l’entreprise, car le droit d’accès aux données à caractère personnel (article 15, RGPD) permet à la personne concernée d’obtenir une copie des données traitées, et ce droit ne porte pas atteinte aux droits et libertés d’autrui [3]. Cependant, la conservation des données, y compris les emails, doit respecter les règles de durée de conservation et les obligations de sécurité, notamment dans le cadre d’un traitement lié à la relation de travail [1]. Si le traitement de données (comme la gestion des emails) est lié à des finalités professionnelles ou à la gestion du personnel, il peut être soumis à des règles d’entreprise contraignantes (article 47, RGPD), qui exigent une transparence sur les finalités, les destinataires et les durées de conservation [2]. En l’absence de règles spécifiques prévues par la loi ou les conventions collectives, les données peuvent être conservées tant qu’elles ne sont pas supprimées, sauf si le traitement n’est pas susceptible de comporter un risque pour les droits et libertés des personnes concernées [4].
```

</details>

Temps : recherche 2.2 s · génération 46.7 s (4486 tokens lus, 468 écrits, 30.8 tokens/s) · contrôle de pertinence 3.8 s

## e11 — Dans notre organisme de formation, on demande aux stagiaires leur numéro de sécurité sociale et des informations sur leur handicap. On a le droit ?

Article attendu : RGPD art. 9, paragraphe 1 ou RGPD art. 9, paragraphe 2_a i ou RGPD art. 87 — passage [3].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 20 : Droit à la portabilité des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_20
  [2] RGPD — règlement (UE) 2016/679, article 9, paragraphe 3 : Traitement portant sur des catégories particulières de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
  [3] RGPD — règlement (UE) 2016/679, article 9, paragraphe 1 : Traitement portant sur des catégories particulières de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
  [4] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [5] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [3] « Le traitement des données à caractère personnel qui révèle l'origine raciale ou ethnique, les opinions politiques, les convictions religieuses ou philosophiques ou l'appartenance syndicale, ainsi que le traitement des données génétiques, des données biométriques aux fins d'identifier une personne physique de manière unique, des données concernant la santé ou des données concernant la vie sexuelle ou l'orientation sexuelle d'une personne physique sont interdits. »  

RÉPONSE :  
Oui, vous avez le droit de demander aux stagiaires leur numéro de sécurité sociale et des informations sur leur handicap, car ces données ne relèvent pas des catégories interdites au regard de l’article 9, point 1 du RGPD [3]. Cependant, le traitement de données concernant la santé (comme les informations sur le handicap) est interdit par l’article 9, point 1, du RGPD [3]. Ainsi, le traitement de ces données est interdit sauf si des conditions spécifiques sont remplies, comme le traitement par un professionnel de la santé soumis à une obligation de secret professionnel [2]. Dans le cas d’un organisme de formation, ces conditions ne sont pas énoncées dans les extraits, donc le traitement de données sur le handicap est interdit [3]. Le numéro de sécurité sociale, bien qu’il ne soit pas explicitement mentionné dans les catégories interdites, peut être considéré comme une donnée personnelle, mais son traitement n’est pas interdit par l’article 9, point 1, car il ne relève pas des catégories spécifiques mentionnées. Cependant, le traitement de données sur le handicap est interdit [3]. Donc, dans votre organisme de formation, vous n'avez pas le droit de demander des informations sur le handicap, car cela relève d’un traitement interdit par l’article 9, point 1 du RGPD [3].
```

</details>

Temps : recherche 2.2 s · génération 30.0 s (3010 tokens lus, 440 écrits, 34.1 tokens/s) · contrôle de pertinence 3.4 s

## e12 — Je peux suivre les véhicules de mes techniciens par GPS ?

Article attendu : RGPD art. 6, paragraphe 1 ou RGPD art. 5 — absent des passages donnés au modèle.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 41 : Suivi des codes de conduite approuvés
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_41
  [2] RGPD — règlement (UE) 2016/679, article 28, paragraphe 5 : Sous-traitant
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [3] RGPD — règlement (UE) 2016/679, article 28, paragraphe 1 : Sous-traitant
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [4] RGPD — règlement (UE) 2016/679, article 40, paragraphe 3 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [5] RGPD — règlement (UE) 2016/679, article 40, paragraphe 1 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
aucun

RÉPONSE :  
Les textes trouvés ne traitent pas de la surveillance des véhicules de techniciens par GPS. La question porte sur une pratique de suivi de véhicules, qui n'est pas abordée dans les passages fournis, qui se limitent à la mise en œuvre de codes de conduite, aux sous-traitants et aux garanties de protection des données. Aucun passage ne mentionne la surveillance par GPS ni la collecte de données relatives à la localisation des véhicules.
```

</details>

Temps : recherche 2.1 s · génération 16.2 s (2548 tokens lus, 120 écrits, 35.8 tokens/s)

## e13 — On veut publier sur Facebook des photos des bénévoles prises pendant notre fête annuelle. Il faut leur accord écrit ?

Article attendu : RGPD art. 6, paragraphe 1 ou RGPD art. 7 — absent des passages donnés au modèle.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 31, paragraphe 7 : Exigences concernant les organismes notifiés
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_31
  [2] AI Act — règlement (UE) 2024/1689, article 31, paragraphe 1 : Exigences concernant les organismes notifiés
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_31
  [3] AI Act — règlement (UE) 2024/1689, article 31, paragraphe 11 : Exigences concernant les organismes notifiés
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_31
  [4] AI Act — règlement (UE) 2024/1689, article 45 : Obligations d’information des organismes notifiés
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_45
  [5] AI Act — règlement (UE) 2024/1689, article 53 : Obligations incombant aux fournisseurs de modèles d’IA à usage général
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_53

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
aucun

RÉPONSE :  
Les textes trouvés ne traitent pas de la publication sur Facebook de photos de bénévoles prises lors d'une fête annuelle. Aucun passage ne aborde la question de l'obtention d'un accord écrit pour la diffusion de photos de personnes dans un contexte de fête annuelle, ni la réglementation sur le traitement de données personnelles dans ce cadre. La réponse à cette question ne peut donc être tirée des extraits fournis.
```

</details>

Temps : recherche 2.2 s · génération 22.8 s (3269 tokens lus, 113 écrits, 34.4 tokens/s)

## e14 — On a 8 salariés. On doit tenir un registre des traitements et nommer un DPO ?

Article attendu : RGPD art. 30 ou RGPD art. 37 — passage [1].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 30 : Registre des activités de traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_30
  [2] RGPD — règlement (UE) 2016/679, article 37 : Désignation du délégué à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_37
  [3] RGPD — règlement (UE) 2016/679, article 38 : Fonction du délégué à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_38
  [4] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [5] RGPD — règlement (UE) 2016/679, article 39 : Missions du délégué à la protection des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_39
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les obligations visées aux paragraphes 1 et 2 ne s'appliquent pas à une entreprise ou à une organisation comptant moins de 250 employés, sauf si le traitement qu'elles effectuent est susceptible de comporter un risque pour les droits et des libertés des personnes concernées, s'il n'est pas occasionnel ou s'il porte notamment sur les catégories particulières de données visées à l'article 9, paragraphe 1, ou sur des données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l'article 10. »  
- [1] « Chaque responsable du traitement et, le cas échéant, le représentant du responsable du traitement tiennent un registre des activités de traitement effectuées sous leur responsabilité. »  
- [2] « Le responsable du traitement et le sous-traitant désignent en tout état de cause un délégué à la protection des données lorsque: a) le traitement est effectué par une autorité publique ou un organisme public, à l'exception des juridictions agissant dans l'exercice de leur fonction juridictionnelle; b) les activités de base du responsable du traitement ou du sous-traitant consistent en des opérations de traitement qui, du fait de leur nature, de leur portée et/ou de leurs finalités, exigent un suivi régulier et systématique à grande échelle des personnes concernées; ou c) les activités de base du responsable du traitement ou du sous-traitant consistent en un traitement à grande échelle de catégories particulières de données visées à l’article 9 ou de données à caractère personnel relatives à des condamnations pénales et à des infractions visées à l’article 10. »  
- [7] « Le délégué à la protection des données est désigné sur la base de ses qualités professionnelles et, en particulier, de ses connaissances spécialisées du droit et des pratiques en matière de protection des données, et de sa capacité à accomplir les missions visées à l'article 39. »  

RÉPONSE :  
Oui : vous devez tenir un registre des activités de traitement (RGPD, article 30, paragraphe 1), car le nombre d’employés (8) est inférieur à 250, mais les obligations du registre s’appliquent sauf si le traitement ne comporte pas de risque pour les droits et libertés des personnes concernées, s’il est occasionnel ou s’il ne porte pas sur des catégories particulières de données (RGPD, article 30, paragraphe 5). Concernant le délégué à la protection des données (DPO), il n’est pas obligatoire pour une entreprise de 8 salariés, sauf si les activités de traitement consistent en des opérations à grande échelle ou si elles portent sur des catégories particulières de données (RGPD, article 37, alinéa 1, b) ou c)). Aucune indication ne précise que le traitement de 8 salariés relève de ces cas. Donc, le DPO n’est pas obligatoire dans ce cas, sauf si les finalités ou la nature du traitement répondent aux conditions prévues à l’article 37.
```

</details>

Temps : recherche 2.2 s · génération 51.1 s (4044 tokens lus, 758 écrits, 31.5 tokens/s) · contrôle de pertinence 2.4 s

## e15 — Notre logiciel de gestion des clients est hébergé aux États-Unis. C'est autorisé ?

Article attendu : RGPD art. 44 ou RGPD art. 45, paragraphe 1 ou RGPD art. 46 — passage [1].

### Réponse du copilote

> Oui, le transfert de données à caractère personnel vers les États-Unis est autorisé, à condition que l'un des mécanismes prévus par le RGPD soit respecté. Si les États-Unis n'ont pas été reconnus comme assurant un niveau de protection adéquat par une décision de la Commission européenne (article 45), alors le transfert doit être fondé sur des garanties appropriées (article 46), par exemple des clauses types de protection des données approuvées par la Commission, ou des règles d'entreprise contraignantes, ou un mécanisme de certification approuvé. Si aucune de ces conditions n'est remplie, le transfert peut être autorisé uniquement dans des cas particuliers précis, tels que le consentement explicite, la nécessité contractuelle, l'intérêt public, ou la défense de droits en justice (article 49). Le responsable du traitement doit informer l'autorité de contrôle du transfert et la personne concernée, notamment sur les intérêts légitimes impérieux qu'il poursuit [5]. Le transfert ne peut pas être répétitif ni toucher un nombre excessif de personnes, et doit être justifié par une évaluation des circonstances [5]. Les conditions du transfert doivent être respectées, notamment pour les transferts ultérieurs vers d'autres pays [3].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. Un tel transfert ne nécessite pas d'autorisation spécifique. »
  [2] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
  [3] « Un transfert, vers un pays tiers ou à une organisation internationale, de données à caractère personnel qui font ou sont destinées à faire l'objet d'un traitement après ce transfert ne peut avoir lieu que si, sous réserve des autres dispositions du présent règlement, les conditions définies dans le présent chapitre sont respectées par le responsable du traitement et le sous-traitant, y compris pour les transferts ultérieurs de données à caractère personnel au départ du pays tiers ou de l'organisation internationale vers un autre pays tiers ou à une autre organisation internationale. »
  [4] « Toute décision d'une juridiction ou d'une autorité administrative d'un pays tiers exigeant d'un responsable du traitement ou d'un sous-traitant qu'il transfère ou divulgue des données à caractère personnel ne peut être reconnue ou rendue exécutoire de quelque manière que ce soit qu'à la condition qu'elle soit fondée sur un accord international, tel qu'un traité d'entraide judiciaire, en vigueur entre le pays tiers demandeur et l'Union ou un État membre, sans préjudice d'autres motifs de transfert en vertu du présent chapitre. »
  [5] « En l'absence de décision d'adéquation en vertu de l'article 45, paragraphe 3, ou de garanties appropriées en vertu de l'article 46, y compris des règles d'entreprise contraignantes, un transfert ou un ensemble de transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale ne peut avoir lieu qu'à l'une des conditions suivantes: … »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 45, paragraphe 1 : Transferts fondés sur une décision d'adéquation (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
  [2] RGPD — règlement (UE) 2016/679, article 46 : Transferts moyennant des garanties appropriées (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_46
  [3] RGPD — règlement (UE) 2016/679, article 44 : Principe général applicable aux transferts (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_44
  [4] RGPD — règlement (UE) 2016/679, article 48 : Transferts ou divulgations non autorisés par le droit de l'Union (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_48
  [5] RGPD — règlement (UE) 2016/679, article 49, paragraphe 1 : Dérogations pour des situations particulières (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_49
Note : La liste des pays bénéficiant d'une décision d'adéquation n'est pas dans les textes utilisés par le copilote : consultez la page de la Commission européenne sur les décisions d'adéquation (en anglais) : https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en
Attention : La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à condition que l'un des mécanismes prévus par le RGPD soit respecté ». Vérifiez-la dans les textes.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. Un tel transfert ne nécessite pas d'autorisation spécifique. »  
- [2] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »  
- [3] « Un transfert, vers un pays tiers ou à une organisation internationale, de données à caractère personnel qui font ou sont destinées à faire l'objet d'un traitement après ce transfert ne peut avoir lieu que si, sous réserve des autres dispositions du présent règlement, les conditions définies dans le présent chapitre sont respectées par le responsable du traitement et le sous-traitant, y compris pour les transferts ultérieurs de données à caractère personnel au départ du pays tiers ou de l'organisation internationale vers un autre pays tiers ou à une autre organisation internationale. »  
- [4] « Toute décision d'une juridiction ou d'une autorité administrative d'un pays tiers exigeant d'un responsable du traitement ou d'un sous-traitant qu'il transfère ou divulgue des données à caractère personnel ne peut être reconnue ou rendue exécutoire de quelque manière que ce soit qu'à la condition qu'elle soit fondée sur un accord international, tel qu'un traité d'entraide judiciaire, en vigueur entre le pays tiers demandeur et l'Union ou un État membre, sans préjudice d'autres motifs de transfert en vertu du présent chapitre. »  
- [5] « En l'absence de décision d'adéquation en vertu de l'article 45, paragraphe 3, ou de garanties appropriées en vertu de l'article 46, y compris des règles d'entreprise contraignantes, un transfert ou un ensemble de transferts de données à caractère personnel vers un pays tiers ou à une organisation internationale ne peut avoir lieu qu'à l'une des conditions suivantes: … »  

RÉPONSE :  
Oui, le transfert de données à caractère personnel vers les États-Unis est autorisé, à condition que l'un des mécanismes prévus par le RGPD soit respecté. Si les États-Unis n'ont pas été reconnus comme assurant un niveau de protection adéquat par une décision de la Commission européenne (article 45), alors le transfert doit être fondé sur des garanties appropriées (article 46), par exemple des clauses types de protection des données approuvées par la Commission, ou des règles d'entreprise contraignantes, ou un mécanisme de certification approuvé. Si aucune de ces conditions n'est remplie, le transfert peut être autorisé uniquement dans des cas particuliers précis, tels que le consentement explicite, la nécessité contractuelle, l'intérêt public, ou la défense de droits en justice (article 49). Le responsable du traitement doit informer l'autorité de contrôle du transfert et la personne concernée, notamment sur les intérêts légitimes impérieux qu'il poursuit [5]. Le transfert ne peut pas être répétitif ni toucher un nombre excessif de personnes, et doit être justifié par une évaluation des circonstances [5]. Les conditions du transfert doivent être respectées, notamment pour les transferts ultérieurs vers d'autres pays [3].
```

</details>

Temps : recherche 2.2 s · génération 46.8 s (3349 tokens lus, 877 écrits, 32.8 tokens/s) · contrôle de pertinence 2.4 s

## e16 — On ne crée pas d'IA, on utilise juste des outils comme ChatGPT. Est-ce que l'AI Act nous concerne quand même ?

Article attendu : AI Act art. 3, définition 4 ou AI Act art. 2, paragraphe 1 ou AI Act art. 4 — passage [2].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 2, paragraphe 6 : Champ d’application
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_2
  [2] AI Act — règlement (UE) 2024/1689, article 2, paragraphe 1 : Champ d’application
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_2
  [3] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points a) à e) : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [4] AI Act — règlement (UE) 2024/1689, article 2, paragraphe 3 : Champ d’application
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_2
  [5] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1 bis : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Le présent règlement ne s’applique pas aux systèmes d’IA ou aux modèles d’IA spécifiquement développés et mis en service uniquement à des fins de recherche et développement scientifiques, ni à leurs sorties. »  
- [2] « Le présent règlement s’applique: a) aux fournisseurs établis ou situés dans l’Union ou dans un pays tiers qui mettent sur le marché ou mettent en service des systèmes d’IA ou qui mettent sur le marché des modèles d’IA à usage général dans l’Union; … g) aux personnes concernées qui sont situées dans l’Union. »  
- [4] « Le présent règlement ne s’applique pas aux systèmes d’IA si et dans la mesure où ils sont mis sur le marché, mis en service ou utilisés avec ou sans modifications exclusivement à des fins militaires, de défense ou de sécurité nationale, quel que soit le type d’entité exerçant ces activités. »  
- [5] « Aux fins du paragraphe 1, premier alinéa, points b bis) et b ter): … n'est interdite que lorsque: i) cette production ou manipulation constitue la destination du système d’IA; ou ii) la conception, l'entraînement, l'architecture, les capacités ou les fonctionnalités destinées aux utilisateurs du système font de cette production ou manipulation un résultat raisonnablement prévisible et reproductible, sans nécessiter de modification technique importante, et le système ne dispose pas de mesures de sécurité techniques raisonnables et adéquates et d'autres garanties pour empêcher de manière fiable cette production ou manipulation, compte tenu d'une mauvaise utilisation raisonnablement prévisible, ni pour corriger une mauvaise utilisation observée ou signalée; »  

RÉPONSE :  
Oui, l’AI Act peut vous concerner même si vous ne créez pas d’IA, car vous êtes « personne concernée » située dans l’Union [2]. En effet, l’AI Act s’applique aux personnes concernées qui sont situées dans l’Union [2], ce qui inclut les utilisateurs d’outils d’IA comme ChatGPT. Cependant, il ne s’applique pas aux systèmes d’IA utilisés exclusivement à des fins militaires, de défense ou de sécurité nationale [4], ni aux systèmes spécifiquement développés pour la recherche scientifique [1]. Si votre utilisation de l’outil ne vise pas ces cas, et que vous ne produisez pas de contenus réalistes représentant des parties intimes ou des activités sexuelles sans consentement [3], alors l’AI Act vous concerne en tant que personne concernée, sans que vous ayez besoin de développer ou de mettre en service un système d’IA. Les pratiques interdites (comme la manipulation ou l’exploitation de vulnérabilités) ne s’appliquent pas à l’usage d’outils d’IA comme ChatGPT, à condition que ce ne soit pas utilisé pour générer ou manipuler des contenus illégaux ou préjudiciables [3], [5].
```

</details>

Temps : recherche 2.2 s · génération 40.7 s (3201 tokens lus, 729 écrits, 33.3 tokens/s) · contrôle de pertinence 2.4 s

## e17 — Je voudrais utiliser un logiciel d'IA qui trie automatiquement les CV. C'est interdit ? Sinon, quelles règles je dois respecter ?

Article attendu : AI Act annexe III, point 4 ou AI Act art. 26 — passage [3].

### Réponse du copilote

> Non, l’utilisation d’un logiciel d’IA qui trie automatiquement les CV n’est pas interdite par l’AI Act. Cependant, ce type de système relève des systèmes d’IA à haut risque au sens de l’article 6, paragraphe 2, car il est destiné à être

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des domaines suivants: 4. Emploi, gestion de la main-d'œuvre et accès à l'emploi indépendant: a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; b) systèmes d'IA destinés à être utilisés pour prendre des décisions influant sur les conditions des relations professionnelles, la promotion ou le licenciement dans le cadre de relations professionnelles contractuelles, pour attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques personnelles ou pour suivre et évaluer les performances et le comportement de personnes dans le cadre de telles relations. »
  [4] « 1. La conception et le développement des systèmes d’IA à haut risque permettent, notamment au moyen d’interfaces homme-machine appropriées, un contrôle effectif par des personnes physiques pendant leur période d’utilisation. 2. Le contrôle humain vise à prévenir ou à réduire au minimum les risques pour la santé, la sécurité ou les droits fondamentaux qui peuvent apparaître lorsqu’un système d’IA à haut risque est utilisé conformément à sa destination ou dans des conditions de mauvaise utilisation raisonnablement prévisible, en particulier lorsque de tels risques persistent malgré l’application d’autres exigences énoncées dans la présente section. 3. Les mesures de contrôle sont proportionnées aux risques, au niveau d’autonomie et au contexte d’utilisation du système d’IA à haut risque, et sont assurées au moyen d’un ou des deux types de mesures suivants: a) des mesures identifiées et, lorsque cela est techniquement possible, intégrées par le fournisseur dans le système d’IA à haut risque avant la mise sur le marché ou la mise en service de ce dernier; b) des mesures identifiées par le fournisseur avant la mise sur le marché ou la mise en service du système d’IA à haut risque et qui se prêtent à une mise en œuvre par le déployeur. 4. Aux fins de la mise en œuvre des dispositions des paragraphes 1, 2 et 3, le système d’IA à haut risque est fourni au déployeur de telle manière que les personnes physiques chargées d’effectuer un contrôle humain, dans la mesure où cela est approprié et proportionné, ont la possibilité: a) de comprendre correctement les capacités et les limites pertinentes du système d’IA à haut risque et d’être en mesure de surveiller correctement son fonctionnement, y compris en vue de détecter et de traiter les anomalies, les dysfonctionnements et les performances inattendues; b) d’avoir conscience d’une éventuelle tendance à se fier automatiquement ou excessivement aux sorties produites par un système d’IA à haut risque (biais d’automatisation), en particulier pour les systèmes d’IA à haut risque utilisés pour fournir des informations ou des recommandations concernant les décisions à prendre par des personnes physiques; c) d’interpréter correctement les sorties du système d’IA à haut risque, compte tenu par exemple des outils et méthodes d’interprétation disponibles; d) de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou inverser la sortie du système d’IA à haut risque; e) d’intervenir dans le fonctionnement du système d’IA à haut risque ou d’interrompre le système au moyen d’un bouton d’arrêt ou d’une procédure similaire permettant au système de s’arrêter de manière sécurisée. 5. Pour les systèmes d’IA à haut risque visés à l’annexe III, point 1 a), les mesures prévues au paragraphe 3 du présent article sont de nature à garantir que, en outre, aucune mesure ou décision n’est prise par le déployeur sur la base de l’identification résultant du système sans vérification et confirmation distinctes de cette identification par au moins deux personnes physiques disposant des compétences, de la formation et de l’autorité nécessaires. L’exigence d’une vérification distincte par au moins deux personnes physiques ne s’applique pas aux systèmes d’IA à haut risque utilisés à des fins répressives ou dans les domaines de la migration, des contrôles aux frontières ou de l’asile, lorsque le droit de l’Union ou le droit national considère que l’application de cette exigence est disproportionnée. »

Sources citées :
  [3] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [4] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points a) à e) : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [2] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points f) à h) : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [5] AI Act — règlement (UE) 2024/1689, article 59, paragraphe 3 : Traitement ultérieur de données à caractère personnel en vue du développement de certains systèmes d’IA dans l’intérêt public dans le cadre du bac à sable réglementaire de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_59
Attention : Réponse coupée : le modèle a atteint la limite de 2000 tokens (LLM_MAX_TOKENS), la fin de la réponse manque. Posez une question plus précise ou augmentez LLM_MAX_TOKENS dans .env.
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1]) : ignoré(s).
Attention : La réponse ne cite aucun passage et une phrase ne reprend pas les extraits vérifiés : « Non, l’utilisation d’un logiciel d’IA qui trie automatiquement les CV n’est pas interdite par l’AI Act. ». Vérifiez-la dans les textes.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les pratiques en matière d’IA suivantes sont interdites: a) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui a recours à des techniques subliminales…; b) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui exploite les éventuelles vulnérabilités dues à l’âge, au handicap ou à la situation sociale ou économique spécifique d’une personne physique ou d’un groupe de personnes donné avec pour objectif ou effet d’altérer substantiellement le comportement de cette personne ou d’un membre de ce groupe d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne ou à un tiers; b bis) la mise sur le marché, la mise en service ou l'utilisation d'un système d'IA qui génère ou manipule des images, des vidéos, des contenus audio ou tout autre matériel similaire réalistes représentant les parties intimes d'une personne identifiable, ou une personne identifiable se livrant à des activités sexuellement explicites, sans le consentement libre, spécifique, éclairé, univoque et explicite de cette personne pour cette production ou manipulation; b ter) la mise sur le marché, la mise en service ou l'utilisation d'un système d'IA qui génère ou manipule tout matériel ou spectacle au sens de l'article 2, points c) et e), de la directive 2011/93/UE, sauf lorsqu'une défense «sans droit» s'applique en vertu du droit national; c) la mise sur le marché, la mise en service ou l’utilisation de systèmes d’IA pour l’évaluation ou la classification de personnes physiques ou de groupes de personnes au cours d’une période donnée en fonction de leur comportement social ou de caractéristiques personnelles ou de personnalité connues, déduites ou prédites, la note sociale conduisant à l’une ou l’autre des situations suivantes, ou aux deux: i) le traitement préjudiciable ou défavorable de certaines personnes physiques ou de groupes de personnes dans des contextes sociaux dissociés du contexte dans lequel les données ont été générées ou collectées à l’origine; ii) le traitement préjudiciable ou défavorable de certaines personnes ou de groupes de personnes, qui est injustifié ou disproportionné par rapport à leur comportement social ou à la gravité de celui-ci; d) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour mener des évaluations des risques des personnes physiques visant à évaluer ou à prédire le risque qu’une personne physique commette une infraction pénale, uniquement sur la base du profilage d’une personne physique ou de l’évaluation de ses traits de personnalité ou caractéristiques; cette interdiction ne s’applique pas aux systèmes d’IA utilisés pour étayer l’évaluation humaine de l’implication d’une personne dans une activité criminelle, qui est déjà fondée sur des faits objectifs et vérifiables, directement liés à une activité criminelle; e) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA qui créent ou développent des bases de données de reconnaissance faciale par le moissonnage non ciblé d’images faciales provenant de l’internet ou de la vidéosurveillance; »  
- [3] « Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des domaines suivants: 4. Emploi, gestion de la main-d'œuvre et accès à l'emploi indépendant: a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; b) systèmes d'IA destinés à être utilisés pour prendre des décisions influant sur les conditions des relations professionnelles, la promotion ou le licenciement dans le cadre de relations professionnelles contractuelles, pour attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques personnelles ou pour suivre et évaluer les performances et le comportement de personnes dans le cadre de telles relations. »  
- [4] « 1. La conception et le développement des systèmes d’IA à haut risque permettent, notamment au moyen d’interfaces homme-machine appropriées, un contrôle effectif par des personnes physiques pendant leur période d’utilisation. 2. Le contrôle humain vise à prévenir ou à réduire au minimum les risques pour la santé, la sécurité ou les droits fondamentaux qui peuvent apparaître lorsqu’un système d’IA à haut risque est utilisé conformément à sa destination ou dans des conditions de mauvaise utilisation raisonnablement prévisible, en particulier lorsque de tels risques persistent malgré l’application d’autres exigences énoncées dans la présente section. 3. Les mesures de contrôle sont proportionnées aux risques, au niveau d’autonomie et au contexte d’utilisation du système d’IA à haut risque, et sont assurées au moyen d’un ou des deux types de mesures suivants: a) des mesures identifiées et, lorsque cela est techniquement possible, intégrées par le fournisseur dans le système d’IA à haut risque avant la mise sur le marché ou la mise en service de ce dernier; b) des mesures identifiées par le fournisseur avant la mise sur le marché ou la mise en service du système d’IA à haut risque et qui se prêtent à une mise en œuvre par le déployeur. 4. Aux fins de la mise en œuvre des dispositions des paragraphes 1, 2 et 3, le système d’IA à haut risque est fourni au déployeur de telle manière que les personnes physiques chargées d’effectuer un contrôle humain, dans la mesure où cela est approprié et proportionné, ont la possibilité: a) de comprendre correctement les capacités et les limites pertinentes du système d’IA à haut risque et d’être en mesure de surveiller correctement son fonctionnement, y compris en vue de détecter et de traiter les anomalies, les dysfonctionnements et les performances inattendues; b) d’avoir conscience d’une éventuelle tendance à se fier automatiquement ou excessivement aux sorties produites par un système d’IA à haut risque (biais d’automatisation), en particulier pour les systèmes d’IA à haut risque utilisés pour fournir des informations ou des recommandations concernant les décisions à prendre par des personnes physiques; c) d’interpréter correctement les sorties du système d’IA à haut risque, compte tenu par exemple des outils et méthodes d’interprétation disponibles; d) de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou inverser la sortie du système d’IA à haut risque; e) d’intervenir dans le fonctionnement du système d’IA à haut risque ou d’interrompre le système au moyen d’un bouton d’arrêt ou d’une procédure similaire permettant au système de s’arrêter de manière sécurisée. 5. Pour les systèmes d’IA à haut risque visés à l’annexe III, point 1 a), les mesures prévues au paragraphe 3 du présent article sont de nature à garantir que, en outre, aucune mesure ou décision n’est prise par le déployeur sur la base de l’identification résultant du système sans vérification et confirmation distinctes de cette identification par au moins deux personnes physiques disposant des compétences, de la formation et de l’autorité nécessaires. L’exigence d’une vérification distincte par au moins deux personnes physiques ne s’applique pas aux systèmes d’IA à haut risque utilisés à des fins répressives ou dans les domaines de la migration, des contrôles aux frontières ou de l’asile, lorsque le droit de l’Union ou le droit national considère que l’application de cette exigence est disproportionnée. »

RÉPONSE :  
Non, l’utilisation d’un logiciel d’IA qui trie automatiquement les CV n’est pas interdite par l’AI Act. Cependant, ce type de système relève des systèmes d’IA à haut risque au sens de l’article 6, paragraphe 2, car il est destiné à être
```

</details>

Temps : recherche 2.2 s · génération 70.1 s (4252 tokens lus, 2000 écrits, 29.7 tokens/s) · contrôle de pertinence 10.7 s

## e18 — On a mis un chatbot sur notre site. On doit dire aux visiteurs qu'ils parlent avec une machine ?

Article attendu : AI Act art. 50, paragraphe 1 — passage [1].

### Réponse du copilote

> Oui : vous devez indiquer clairement aux visiteurs que vous interagissez avec un système d’IA, car le chatbot est un système d’IA destiné à interagir directement avec des personnes physiques [1]. Cette obligation s’applique même si le chatbot ne génère pas d’images ou de vidéos, car il interagit directement avec les utilisateurs [1]. Cependant, cette information ne doit pas être cachée ou trompée, sauf si elle ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation [1]. Si le chatbot est utilisé pour informer le public sur des questions d’intérêt public, vous devez aussi indiquer que le texte a été généré par une IA [2]. Les passages ne mentionnent pas de cas d’exception pour les chatbots non destinés à influencer des décisions humaines ou à remplacer des évaluations humaines, donc l’obligation de transparence s’applique dans ce cas [5].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »
  [2] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. »
  [2] « Les déployeurs d’un système d’IA qui génère ou manipule des textes publiés dans le but d’informer le public sur des questions d’intérêt public indiquent que le texte a été généré ou manipulé par une IA. »
  [3] « Le contrôle humain vise à prévenir ou à réduire au minimum les risques pour la santé, la sécurité ou les droits fondamentaux qui peuvent apparaître lorsqu’un système d’IA à haut risque est utilisé conformément à sa destination ou dans des conditions de mauvaise utilisation raisonnablement prévisible… »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 4 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [3] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14
  [5] AI Act — règlement (UE) 2024/1689, article 6, point c : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
Passages consultés mais non cités :
  [4] AI Act — règlement (UE) 2024/1689, article 21 : Coopération avec les autorités compétentes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_21
Attention : La réponse cite [5] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.
Attention : La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Cependant, cette information ne doit pas être cachée ou trompée, sauf si elle ressort clairement du point de vue d’une … ». Vérifiez ce point.
Attention : La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui: vous devez indiquer clairement aux visiteurs que vous interagissez avec un système d’IA, car le chatbot est un … » (et 2 autre(s)). Vérifiez qui est concerné.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »  
- [2] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. »  
- [2] « Les déployeurs d’un système d’IA qui génère ou manipule des textes publiés dans le but d’informer le public sur des questions d’intérêt public indiquent que le texte a été généré ou manipulé par une IA. »  
- [3] « Le contrôle humain vise à prévenir ou à réduire au minimum les risques pour la santé, la sécurité ou les droits fondamentaux qui peuvent apparaître lorsqu’un système d’IA à haut risque est utilisé conformément à sa destination ou dans des conditions de mauvaise utilisation raisonnablement prévisible… »  

RÉPONSE :  
Oui : vous devez indiquer clairement aux visiteurs que vous interagissez avec un système d’IA, car le chatbot est un système d’IA destiné à interagir directement avec des personnes physiques [1]. Cette obligation s’applique même si le chatbot ne génère pas d’images ou de vidéos, car il interagit directement avec les utilisateurs [1]. Cependant, cette information ne doit pas être cachée ou trompée, sauf si elle ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation [1]. Si le chatbot est utilisé pour informer le public sur des questions d’intérêt public, vous devez aussi indiquer que le texte a été généré par une IA [2]. Les passages ne mentionnent pas de cas d’exception pour les chatbots non destinés à influencer des décisions humaines ou à remplacer des évaluations humaines, donc l’obligation de transparence s’applique dans ce cas [5].
```

</details>

Temps : recherche 2.2 s · génération 34.5 s (3243 tokens lus, 571 écrits, 33.3 tokens/s) · contrôle de pertinence 2.5 s

## e19 — Notre organisme de formation veut utiliser une IA pour corriger les examens et noter les stagiaires. C'est risqué ?

Article attendu : AI Act annexe III, point 3 — passage [1].

### Réponse du copilote

> Oui, l'utilisation d'une IA pour corriger les examens et noter les stagiaires est considérée comme un système d'IA à haut risque, car elle relève des cas d'utilisation visés à l'annexe III du règlement (UE) 2024/1689, notamment l'évaluation des acquis d'apprentissage (article 6, paragraphe 2, point b) et l'évaluation du niveau d'enseignement approprié (point c) [1]. Ce type d'utilisation est inclus dans les systèmes d'IA à haut risque, même s'il ne s'agit pas directement d'un profilage [5]. Un système d'IA à haut risque est donc soumis à des essais pour déterminer les mesures de gestion des risques les plus appropriées [3], et un système de gestion des risques doit être établi, mis en œuvre, documenté et tenu à jour [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « systèmes d'IA destinés à être utilisés pour surveiller et détecter des comportements interdits chez les étudiants lors d'examens dans le contexte d'établissements d'enseignement et de formation ou en leur sein à tous les niveaux; »
  [1] « systèmes d'IA destinés à être utilisés pour évaluer les acquis d'apprentissage, y compris lorsque ceux-ci sont utilisés pour orienter le processus d'apprentissage de personnes physiques dans les établissements d'enseignement et de formation professionnelle, à tous les niveaux; »
  [1] « systèmes d'IA destinés à être utilisés pour évaluer le niveau d'enseignement approprié qu'une personne recevra ou sera en mesure d'atteindre, dans le contexte ou au sein d'établissements d'enseignement et de formation professionnelle à tous les niveaux; »
  [5] « le système d’IA est destiné à exécuter une tâche préparatoire en vue d’une évaluation pertinente aux fins des cas d’utilisation visés à l’annexe III. Nonobstant le premier alinéa, un système d’IA visé à l’annexe III est toujours considéré comme étant à haut risque lorsqu’il effectue un profilage de personnes physiques. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, annexe III, point 3 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [3] AI Act — règlement (UE) 2024/1689, article 9, paragraphe 6 : Système de gestion des risques (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_9
  [4] AI Act — règlement (UE) 2024/1689, article 9, paragraphe 1 : Système de gestion des risques (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_9
  [5] AI Act — règlement (UE) 2024/1689, article 6, point d : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
Attention : La réponse cite [3], [4] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « systèmes d'IA destinés à être utilisés pour surveiller et détecter des comportements interdits chez les étudiants lors d'examens dans le contexte d'établissements d'enseignement et de formation ou en leur sein à tous les niveaux; »
- [1] « systèmes d'IA destinés à être utilisés pour évaluer les acquis d'apprentissage, y compris lorsque ceux-ci sont utilisés pour orienter le processus d'apprentissage de personnes physiques dans les établissements d'enseignement et de formation professionnelle, à tous les niveaux; »
- [1] « systèmes d'IA destinés à être utilisés pour évaluer le niveau d'enseignement approprié qu'une personne recevra ou sera en mesure d'atteindre, dans le contexte ou au sein d'établissements d'enseignement et de formation professionnelle à tous les niveaux; »
- [5] « le système d’IA est destiné à exécuter une tâche préparatoire en vue d’une évaluation pertinente aux fins des cas d’utilisation visés à l’annexe III. Nonobstant le premier alinéa, un système d’IA visé à l’annexe III est toujours considéré comme étant à haut risque lorsqu’il effectue un profilage de personnes physiques. »

RÉPONSE :
Oui, l'utilisation d'une IA pour corriger les examens et noter les stagiaires est considérée comme un système d'IA à haut risque, car elle relève des cas d'utilisation visés à l'annexe III du règlement (UE) 2024/1689, notamment l'évaluation des acquis d'apprentissage (article 6, paragraphe 2, point b) et l'évaluation du niveau d'enseignement approprié (point c) [1]. Ce type d'utilisation est inclus dans les systèmes d'IA à haut risque, même s'il ne s'agit pas directement d'un profilage [5]. Un système d'IA à haut risque est donc soumis à des essais pour déterminer les mesures de gestion des risques les plus appropriées [3], et un système de gestion des risques doit être établi, mis en œuvre, documenté et tenu à jour [4].
```

</details>

Temps : recherche 2.3 s · génération 25.7 s (2246 tokens lus, 544 écrits, 35.8 tokens/s) · contrôle de pertinence 4.8 s

## e20 — On m'a dit que je dois former mes salariés à l'IA. C'est vraiment obligatoire ?

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
  [2] AI Act — règlement (UE) 2024/1689, annexe III, point 3 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [3] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [4] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [5] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les fournisseurs et les déployeurs de systèmes d'IA prennent des mesures pour favoriser le développement de la maîtrise de l'IA par leur personnel et les autres personnes s'occupant du fonctionnement et de l'utilisation des systèmes d'IA pour leur compte, en prenant en considération leurs connaissances techniques, leur expérience, leur éducation et leur formation, ainsi que le contexte dans lequel les systèmes d'IA sont destinés à être utilisés, et en tenant compte des personnes ou des groupes de personnes à l'égard desquels les systèmes d'IA sont destinés à être utilisés. Cette obligation ne contraint pas les fournisseurs ou les déployeurs à garantir un niveau spécifique de maîtrise de l'IA par un individu. »

RÉPONSE :  
Oui : il est obligatoire de prendre des mesures pour favoriser le développement de la maîtrise de l'IA par le personnel et les autres personnes s'occupant du fonctionnement et de l'utilisation des systèmes d'IA, conformément à l'article 4, paragraphe 1, de l'AI Act [1]. Cette obligation vise à assurer que les personnes concernées disposent des connaissances techniques, de l'expérience, de l'éducation et de la formation appropriées, en fonction du contexte d'utilisation et des groupes concernés. Cependant, cette obligation ne contraint pas les fournisseurs ou les déployeurs à garantir un niveau spécifique de maîtrise de l'IA par un individu [1].
```

</details>

Temps : recherche 2.3 s · génération 32.2 s (3481 tokens lus, 361 écrits, 33.1 tokens/s) · contrôle de pertinence 4.0 s

## e21 — On crée nos visuels pour les réseaux sociaux avec une IA. Il faut écrire qu'ils sont générés par IA ?

Article attendu : AI Act art. 50, paragraphe 4 — passage [1].

### Réponse du copilote

> Oui : il faut écrire qu’ils sont générés par une IA, car les visuels générés par une IA constituent un hypertrucage, et les déployeurs doivent indiquer que les contenus ont été générés ou manipulés par une IA [1]. Cette obligation s’applique aux visuels utilisés sur les réseaux sociaux, sauf dans des cas spécifiques comme une utilisation autorisée par la loi pour des fins de prévention ou de détection des infractions pénales, ou lorsque le contenu fait partie d’un programme manifestement artistique, créatif, satirique, fictif ou analogue [1]. Cependant, cette obligation ne s’applique pas si le système d’IA ne modifie pas de manière substantielle les données d’entrée ou sert uniquement à une fonction d’assistance pour la mise en forme standard [3]. Pour les visuels destinés aux réseaux sociaux, sauf cas particuliers, la transparence est obligatoire.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. Cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. Lorsque le contenu fait partie d’une œuvre ou d’un programme manifestement artistique, créatif, satirique, fictif ou analogue, les obligations de transparence énoncées au présent paragraphe se limitent à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 4 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [3] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 2 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [4] AI Act — règlement (UE) 2024/1689, article 19 : Journaux générés automatiquement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_19
  [5] AI Act — règlement (UE) 2024/1689, article 3, définition 60 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([3]) : ignoré(s).
Attention : La réponse cite [3] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.
Attention : La réponse formule une exception qui ne reprend pas les extraits vérifiés : « sauf dans des cas spécifiques comme une utilisation autorisée par la loi pour des ». Vérifiez-la dans les textes.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. Cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. Lorsque le contenu fait partie d’une œuvre ou d’un programme manifestement artistique, créatif, satirique, fictif ou analogue, les obligations de transparence énoncées au présent paragraphe se limitent à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre. »
- [3] « Les fournisseurs de systèmes d’IA, y compris de systèmes d’IA à usage général, qui génèrent des contenus de synthèse de type audio, image, vidéo ou texte, veillent à ce que les sorties des systèmes d’IA soient marquées dans un format lisible par machine et identifiables comme ayant été générées ou manipulées par une IA. Cette obligation ne s’applique pas dans la mesure où les systèmes d’IA remplissent une fonction d’assistance pour la mise en forme standard ou ne modifient pas de manière substantielle les données d’entrée fournies par le déployeur ou leur sémantique, ou lorsque leur utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. »

RÉPONSE :
Oui : il faut écrire qu’ils sont générés par une IA, car les visuels générés par une IA constituent un hypertrucage, et les déployeurs doivent indiquer que les contenus ont été générés ou manipulés par une IA [1]. Cette obligation s’applique aux visuels utilisés sur les réseaux sociaux, sauf dans des cas spécifiques comme une utilisation autorisée par la loi pour des fins de prévention ou de détection des infractions pénales, ou lorsque le contenu fait partie d’un programme manifestement artistique, créatif, satirique, fictif ou analogue [1]. Cependant, cette obligation ne s’applique pas si le système d’IA ne modifie pas de manière substantielle les données d’entrée ou sert uniquement à une fonction d’assistance pour la mise en forme standard [3]. Pour les visuels destinés aux réseaux sociaux, sauf cas particuliers, la transparence est obligatoire.
```

</details>

Temps : recherche 2.2 s · génération 32.3 s (2673 tokens lus, 627 écrits, 34.7 tokens/s) · contrôle de pertinence 4.1 s

## e22 — Un fournisseur nous propose un outil qui analyse les émotions des salariés pendant les visioconférences. On a le droit de l'utiliser ?

Article attendu : AI Act art. 5, paragraphe 1_f h — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 3, définition 39 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_3
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 3 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [3] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [4] AI Act — règlement (UE) 2024/1689, article 6, paragraphe 4 : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
  [5] AI Act — règlement (UE) 2024/1689, article 6, paragraphe 1 : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « «système de reconnaissance des émotions», un système d’IA permettant la reconnaissance ou la déduction des émotions ou des intentions de personnes physiques sur la base de leurs données biométriques»  
- [2] «Les déployeurs d’un système de reconnaissance des émotions ou d’un système de catégorisation biométrique informent les personnes physiques qui y sont exposées du fonctionnement du système et traitent les données à caractère personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680, selon le cas. Cette obligation ne s’applique pas aux systèmes d’IA utilisés pour la catégorisation biométrique et la reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l’Union.»  
- [3] «Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. Cette obligation ne s’applique pas aux systèmes d’IA dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers, sauf si ces systèmes sont mis à la disposition du public pour permettre le signalement d’une infraction pénale.»

RÉPONSE :  
Oui, vous avez le droit d’utiliser cet outil, car il s’agit d’un système de reconnaissance des émotions, comme défini dans l’article 3, [1], et son utilisation dans un contexte professionnel (analyse des émotions des salariés pendant des visioconférences) ne relève pas de l’utilisation à des fins de prévention ou de détection d’infractions pénales, ni d’enquêtes en la matière, comme précisé dans [2] et [3]. Cependant, le déployeur doit informer les personnes physiques exposées du fonctionnement du système [2], et les fournisseurs doivent s’assurer que les utilisateurs sont clairement informés qu’ils interagissent avec un système d’IA [3], sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation.
```

</details>

Temps : recherche 2.2 s · génération 30.0 s (2272 tokens lus, 694 écrits, 35.6 tokens/s) · contrôle de pertinence 5.4 s

## e23 — Si l'outil d'IA qu'on a acheté se trompe et écarte injustement un candidat, qui est responsable : moi ou le fournisseur ?

Article attendu : RGPD art. 82 ou AI Act art. 26 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 25, paragraphe 2 : Responsabilités tout au long de la chaîne de valeur de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_25
  [2] AI Act — règlement (UE) 2024/1689, article 25, paragraphe 1 : Responsabilités tout au long de la chaîne de valeur de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_25
  [3] AI Act — règlement (UE) 2024/1689, article 25, paragraphe 4 : Responsabilités tout au long de la chaîne de valeur de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_25
  [4] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [5] AI Act — règlement (UE) 2024/1689, article 60, paragraphe 9 : Essais de systèmes d’IA à haut risque en conditions réelles en dehors des bacs à sable réglementaires de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_60
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [2] « Tout distributeur, importateur, déployeur ou autre tiers est considéré comme un fournisseur d’un système d’IA à haut risque aux fins du présent règlement et est soumis aux obligations incombant au fournisseur au titre de l’article 16 dans toutes les circonstances suivantes: a) il commercialise sous son propre nom ou sa propre marque un système d’IA à haut risque déjà mis sur le marché ou mis en service, sans préjudice des dispositions contractuelles prévoyant une autre répartition des obligations; b) il apporte une modification substantielle à un système d’IA à haut risque qui a déjà été mis sur le marché ou a déjà été mis en service de telle manière qu’il reste un système d’IA à haut risque en application de l’article 6; c) il modifie la destination d’un système d’IA, y compris un système d’IA à usage général, qui n’a pas été classé à haut risque et a déjà été mis sur le marché ou mis en service de telle manière que le système d’IA concerné devient un système d’IA à haut risque conformément l’article 6. »  
- [3] « Le fournisseur d'un système d'IA à haut risque et le tiers qui fournit un système d'IA, un modèle d'IA, des outils, services, composants ou processus qui sont utilisés ou intégrés dans un système d'IA à haut risque précisent, par accord écrit, les informations, les capacités, l'accès technique et toute autre assistance nécessaires, sur la base de l'état de la technique généralement reconnu, pour permettre au fournisseur du système d'IA à haut risque de se conformer pleinement aux obligations prévues dans le présent règlement. »  
- [4] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »  
- [1] « Ce fournisseur initial coopère étroitement avec les nouveaux fournisseurs, met à disposition les informations nécessaires et fournit l'accès technique et toute autre assistance raisonnablement attendus nécessaire au respect des obligations énoncées dans le présent règlement, en particulier en ce qui concerne le respect de l'évaluation de la conformité des systèmes d’IA à haut risque. »  

RÉPONSE :  
Si l'outil d'IA que vous avez acheté se trompe et écarte injustement un candidat, le fournisseur est responsable, car il est soumis aux obligations de conformité prévues dans l’AI Act, notamment en ce qui concerne la conception et le fonctionnement des systèmes d’IA destinés à interagir avec des personnes physiques [4]. Ce responsable est également tenu de fournir les informations, les capacités et l’accès technique nécessaires pour permettre la conformité aux obligations du règlement [3]. Tout distributeur, déployeur ou autre tiers qui commercialise ou utilise un système d’IA à haut risque est considéré comme un fournisseur et est donc soumis aux mêmes obligations [2]. Cela signifie que le fournisseur, ou le tiers impliqué dans la chaîne de valeur, est responsable des erreurs ou des comportements inappropriés du système, notamment lorsqu’ils affectent des décisions importantes comme l’admissibilité d’un candidat. Les obligations de transparence et de conformité s’appliquent à l’ensemble de la chaîne de valeur, mais la responsabilité principale incombe au fournisseur initial ou au tiers qui a mis en œuvre le système [1].
```

</details>

Temps : recherche 2.2 s · génération 39.3 s (2561 tokens lus, 901 écrits, 34.6 tokens/s) · contrôle de pertinence 4.9 s

## e24 — À partir de quand les règles de l'AI Act s'appliquent vraiment ? Qu'est-ce qui est déjà en vigueur ?

Article attendu : AI Act art. 113 — passage [1].

### Réponse du copilote

> Les règles de l'AI Act s'appliquent vraiment à partir du 2 août 2026 [1]. Cependant, certaines parties du règlement sont déjà en vigueur : le chapitre I et II s'appliquent à partir du 2 février 2025 [1], le chapitre III, section 4, le chapitre V, le chapitre VII, le chapitre XII et l’article 78 s’appliquent à partir du 2 août 2025 [1], et les articles 102 à 110 s'appliquent à partir du 27 juillet 2026 [1]. Ainsi, plusieurs dispositions sont déjà en vigueur avant le 2 août 2026, notamment à partir du 2 août 2025 pour certains chapitres.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Il est applicable à partir du 2 août 2026. »
  [1] « les chapitres I et II s'appliquent à partir du 2 février 2025, à l'exception de l'article 5, paragraphe 1, premier alinéa, points b bis) et b ter), et de l'article 5, paragraphes 1 bis et 1 ter, qui s'appliquent à partir du 2 décembre 2026; »
  [1] « le chapitre III, section 4, le chapitre V, le chapitre VII, le chapitre XII et l’article 78 s’appliquent à partir du 2 août 2025, à l’exception de l’article 101; »
  [1] « les articles 102 à 110 sont applicables à partir du 27 juillet 2026. »
  [2] « les systèmes d’IA qui sont des composants des systèmes d’information à grande échelle établis par les actes juridiques énumérés à l’annexe X et mis sur le marché ou mis en service avant le 2 août 2027 sont mis en conformité avec le présent règlement au plus tard le 31 décembre 2030. »
  [3] « Lorsque, dans les trois mois suivant la réception de la notification visée au paragraphe 5, aucune objection n’a été émise par une autorité de surveillance du marché d’un État membre ou par la Commission à l’encontre d’une mesure provisoire prise par une autorité de surveillance du marché d’un autre État membre, cette mesure est réputée justifiée. »
  [4] « On entend par systèmes d’IA présentant un risque, un «produit présentant un risque» au sens de l’article 3, point 19), du règlement (UE) 2019/1020, dans la mesure où ils présentent des risques pour la santé ou la sécurité, ou pour les droits fondamentaux, des personnes. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 113 : Entrée en vigueur et application (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_113
  [2] AI Act — règlement (UE) 2024/1689, article 111 : Systèmes d’IA déjà mis sur le marché ou mis en service et modèles d’IA à usage général déjà mis sur le marché (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_111
  [3] AI Act — règlement (UE) 2024/1689, article 79, paragraphe 8 : Procédure applicable au niveau national aux systèmes d’IA présentant un risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_79
  [4] AI Act — règlement (UE) 2024/1689, article 79, paragraphe 1 : Procédure applicable au niveau national aux systèmes d’IA présentant un risque (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_79
Passages consultés mais non cités :
  [5] AI Act — règlement (UE) 2024/1689, article 108 : Modifications du règlement (UE) 2018/1139
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_108

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Il est applicable à partir du 2 août 2026. »
- [1] « les chapitres I et II s'appliquent à partir du 2 février 2025, à l'exception de l'article 5, paragraphe 1, premier alinéa, points b bis) et b ter), et de l'article 5, paragraphes 1 bis et 1 ter, qui s'appliquent à partir du 2 décembre 2026; »
- [1] « le chapitre III, section 4, le chapitre V, le chapitre VII, le chapitre XII et l’article 78 s’appliquent à partir du 2 août 2025, à l’exception de l’article 101; »
- [1] « les articles 102 à 110 sont applicables à partir du 27 juillet 2026. »
- [2] « les systèmes d’IA qui sont des composants des systèmes d’information à grande échelle établis par les actes juridiques énumérés à l’annexe X et mis sur le marché ou mis en service avant le 2 août 2027 sont mis en conformité avec le présent règlement au plus tard le 31 décembre 2030. »
- [3] « Lorsque, dans les trois mois suivant la réception de la notification visée au paragraphe 5, aucune objection n’a été émise par une autorité de surveillance du marché d’un État membre ou par la Commission à l’encontre d’une mesure provisoire prise par une autorité de surveillance du marché d’un autre État membre, cette mesure est réputée justifiée. »
- [4] « On entend par systèmes d’IA présentant un risque, un «produit présentant un risque» au sens de l’article 3, point 19), du règlement (UE) 2019/1020, dans la mesure où ils présentent des risques pour la santé ou la sécurité, ou pour les droits fondamentaux, des personnes. »

RÉPONSE :
Les règles de l'AI Act s'appliquent vraiment à partir du 2 août 2026 [1]. Cependant, certaines parties du règlement sont déjà en vigueur : le chapitre I et II s'appliquent à partir du 2 février 2025 [1], le chapitre III, section 4, le chapitre V, le chapitre VII, le chapitre XII et l’article 78 s’appliquent à partir du 2 août 2025 [1], et les articles 102 à 110 s'appliquent à partir du 27 juillet 2026 [1]. Ainsi, plusieurs dispositions sont déjà en vigueur avant le 2 août 2026, notamment à partir du 2 août 2025 pour certains chapitres.
```

</details>

Temps : recherche 2.2 s · génération 43.2 s (3498 tokens lus, 702 écrits, 32.5 tokens/s) · contrôle de pertinence 21.0 s

## e25 — Mes salariés copient des données clients dans ChatGPT pour aller plus vite. C'est un problème ? Comment je peux encadrer ça ?

Article attendu : RGPD art. 32 ou RGPD art. 29 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 47, paragraphe 2, points a) à k) : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
  [2] RGPD — règlement (UE) 2016/679, article 47, paragraphe 1 : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
  [3] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [4] RGPD — règlement (UE) 2016/679, article 33 : Notification à l'autorité de contrôle d'une violation de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_33
  [5] RGPD — règlement (UE) 2016/679, article 34 : Communication à la personne concernée d'une violation de données à caractère personnel
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_34
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les règles d'entreprise contraignantes visées au paragraphe 1 précisent au moins: … la nature juridiquement contraignante, tant interne qu'externe; … les droits des personnes concernées à l'égard du traitement et les moyens d'exercer ces droits y compris le droit de ne pas faire l'objet de décisions fondées exclusivement sur un traitement automatisé, y compris le profilage, conformément à l'article 22, … »  
- [3] « Ces règles comprennent des mesures appropriées et spécifiques pour protéger la dignité humaine, les intérêts légitimes et les droits fondamentaux des personnes concernées, en accordant une attention particulière à la transparence du traitement, au transfert de données à caractère personnel au sein d'un groupe d'entreprises, ou d'un groupe d'entreprises engagées dans une activité économique conjointe et aux systèmes de contrôle sur le lieu de travail. »  
- [4] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. »  
- [5] « Lorsqu'une violation de données à caractère personnel est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement communique la violation de données à caractère personnel à la personne concernée dans les meilleurs délais. »  

RÉPONSE :  
Oui, cela peut être un problème car le copiage de données clients par des salariés dans un outil comme ChatGPT constitue un traitement automatisé de données à caractère personnel, notamment si ces données sont sensibles (ex. : informations personnelles, données commerciales). Cela peut violer le droit de ne pas faire l'objet de décisions fondées exclusivement sur un traitement automatisé, conformément à l'article 22 du RGPD [1]. De plus, le transfert de données à caractère personnel au sein d’un groupe d’entreprises, ou dans un outil externe, doit être encadré par des règles d’entreprise contraignantes qui précisent la nature juridiquement contraignante des règles, les droits des personnes concernées et les mesures de contrôle sur le lieu de travail [1][3]. Vous devez donc mettre en place des règles d’entreprise contraignantes qui interdisent ou réglementent l’utilisation de telles données dans des outils externes, notamment en précisant les finalités autorisées, les catégories de données concernées et les procédures de contrôle [1]. Si les salariés copient des données clients sans autorisation, cela constitue une violation de données à caractère personnel susceptible d’engendrer un risque élevé pour les droits et libertés des personnes concernées [5], ce qui oblige le responsable du traitement à notifier la violation à l’autorité de contrôle compétente dans les 72 heures [4] et à communiquer la violation à la personne concernée [5]. Pour encadrer cela, il faut donc établir des politiques claires, obligatoires, sur l’utilisation des données clients, et les mettre en œuvre dans le cadre d’un système de contrôle sur le lieu de travail [3].
```

</details>

Temps : recherche 2.2 s · génération 50.0 s (3862 tokens lus, 796 écrits, 31.7 tokens/s) · contrôle de pertinence 5.4 s

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
  [2] RGPD — règlement (UE) 2016/679, article 12, paragraphe 5 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [3] RGPD — règlement (UE) 2016/679, article 12, paragraphe 1 : Transparence des informations et des communications et modalités de l'exercice des droits de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_12
  [4] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 11 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [5] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 1 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun  
RÉPONSE : Les textes trouvés ne traitent pas de la déclaration de la TVA.
```

</details>

Temps : recherche 2.1 s · génération 12.7 s (2414 tokens lus, 31 écrits, 37.3 tokens/s)

## he02 — Si un salarié en CDI démissionne, combien de temps dure son préavis ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 75 quater, paragraphe 8 : Non-conformité, amendes et astreintes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_75c
  [2] AI Act — règlement (UE) 2024/1689, article 75 quater, paragraphe 1 : Non-conformité, amendes et astreintes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_75c
  [3] AI Act — règlement (UE) 2024/1689, article 36, paragraphe 9 : Modifications apportées aux notifications
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_36
  [4] AI Act — règlement (UE) 2024/1689, article 36, paragraphe 1 : Modifications apportées aux notifications
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_36
  [5] AI Act — règlement (UE) 2024/1689, article 36, paragraphe 3 : Modifications apportées aux notifications
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_36

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun  
RÉPONSE : Les textes trouvés ne traitent pas de ce point.
```

</details>

Temps : recherche 2.2 s · génération 12.1 s (2370 tokens lus, 26 écrits, 37.7 tokens/s)

## he03 — Tu as des idées pour organiser une fête de fin d'année pour les bénévoles avec un petit budget ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 40, paragraphe 5 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [2] RGPD — règlement (UE) 2016/679, article 57, paragraphe 4 : Missions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_57
  [3] RGPD — règlement (UE) 2016/679, article 57, paragraphe 1, points a) à t) : Missions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_57
  [4] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 5 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99
  [5] AI Act — règlement (UE) 2024/1689, article 99, paragraphe 1 : Sanctions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_99

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun  
RÉPONSE : Les textes trouvés ne traitent pas de votre question.
```

</details>

Temps : recherche 2.2 s · génération 17.3 s (2966 tokens lus, 26 écrits, 36.4 tokens/s)
