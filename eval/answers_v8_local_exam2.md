# Réponses du copilote — v8_local_exam2

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 27/11/2026 à 20:25 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen3:4b-instruct` via Ollama 0.40.18 — température 0.1, contexte 8192 tokens, couches sur la carte graphique : toutes, 2000 tokens au plus par réponse, dont 800 gardés pour la réponse (recopie des extraits arrêtée après 1200 tokens si la réponse n'a pas commencé)
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_exam2.jsonl` (24 + 4 hors sujet)

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| e01 | Je veux installer des caméras dans mon magasin et dans la salle de pause. J'en ai le droit ? Qu'est-ce que je dois dire à mes salariés ? | 4/5 | abstention | Extraits trop longs : le code a arrêté leur recopie après 1200 tokens pour garder au moins 800 tokens à la réponse (dernier extrait raccourci ou retiré ; le passage complet est dans les sources).; Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 107 s |
| e02 | Une ancienne cliente me demande d'effacer toutes ses données. On doit garder ses factures pour la comptabilité. Je dois quand même tout supprimer ? | 5/6 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([5]) : ignoré(s).; La réponse met entre « » un texte introuvable dans les extraits vérifiés : « pertinentes et limitées à ce qui est nécessaire ».; La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à condition que ce traitement soit dans l'intérêt public ou conforme à une obligation légale » (et 1 autre(s)). Vérifiez-la dans les textes.; La réponse ne reprend que 4 des 6 cas énumérés au passage [1], sans dire qu'elle n'en cite qu'une partie. Vérifiez la liste complète. | 47 s |
| e03 | Combien de temps je peux garder les CV des candidats que je n'ai pas retenus ? | 0/0 | oui | — | 15 s |
| e04 | Notre association garde la liste des bénévoles (adresses, téléphones) dans un fichier Excel partagé sur Google Drive. C'est un problème ? | 1/2 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 43 s |
| e05 | Sur mon site web, j'utilise seulement Google Analytics. Je suis obligé de mettre un bandeau cookies ? | 5/5 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 50 s |
| e06 | La boîte mail de l'accueil a été piratée hier. Qu'est-ce que je dois faire ? Je dois prévenir quelqu'un ? | 7/7 | non | — | 52 s |
| e07 | Un prestataire extérieur gère notre paie. Je dois signer un contrat spécial avec lui pour les données ? | 3/3 | non | — | 37 s |
| e08 | Je peux envoyer notre newsletter à mes anciens clients sans leur demander leur accord ? | 5/5 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 49 s |
| e09 | Un salarié me demande une copie de toutes les données que j'ai sur lui, même les mails où on parle de lui. Je dois tout lui donner ? J'ai combien de temps pour répondre ? | 4/4 | non | La réponse formule une exception qui ne reprend pas les extraits vérifiés : « sauf si la demande est complexe ou si le nombre de demandes est élevé, ». Vérifiez-la dans les textes. | 43 s |
| e10 | Un salarié est parti de l'entreprise. Je peux encore lire sa boîte mail professionnelle ? | 3/3 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 64 s |
| e11 | Dans notre organisme de formation, on demande aux stagiaires leur numéro de sécurité sociale et des informations sur leur handicap. On a le droit ? | 1/1 | non | La réponse cite [2], [4] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.; La réponse formule une exception qui ne reprend pas les extraits vérifiés : « sauf si une exception s’applique, comme le traitement par un professionnel de la santé » (et 2 autre(s)). Vérifiez-la dans les textes. | 38 s |
| e12 | Je peux suivre les véhicules de mes techniciens par GPS ? | 0/0 | oui | — | 18 s |
| e13 | On veut publier sur Facebook des photos des bénévoles prises pendant notre fête annuelle. Il faut leur accord écrit ? | 3/3 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 33 s |
| e14 | On a 8 salariés. On doit tenir un registre des traitements et nommer un DPO ? | 3/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 62 s |
| e15 | Notre logiciel de gestion des clients est hébergé aux États-Unis. C'est autorisé ? | 5/5 | non | La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à condition que l'un des mécanismes prévus par le RGPD soit respecté ». Vérifiez-la dans les textes. | 60 s |
| e16 | On ne crée pas d'IA, on utilise juste des outils comme ChatGPT. Est-ce que l'AI Act nous concerne quand même ? | 4/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 51 s |
| e17 | Je voudrais utiliser un logiciel d'IA qui trie automatiquement les CV. C'est interdit ? Sinon, quelles règles je dois respecter ? | 2/3 | non | Extraits trop longs : le code a arrêté leur recopie après 1200 tokens pour garder au moins 800 tokens à la réponse (dernier extrait raccourci ou retiré ; le passage complet est dans les sources).; 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1]) : ignoré(s).; La réponse cite [1] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.; La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Non, l’utilisation d’un logiciel d’IA qui trie automatiquement les CV n’est pas interdite par l’AI Act, à condition … ». Vérifiez ce point. | 106 s |
| e18 | On a mis un chatbot sur notre site. On doit dire aux visiteurs qu'ils parlent avec une machine ? | 3/3 | non | La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui: vous devez indiquer aux visiteurs qu’ils parlent avec un système d’IA, car votre chatbot est un système d’IA … » (et 1 autre(s)). Vérifiez qui est concerné. | 45 s |
| e19 | Notre organisme de formation veut utiliser une IA pour corriger les examens et noter les stagiaires. C'est risqué ? | 4/4 | non | La réponse cite [3], [4] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations. | 36 s |
| e20 | On m'a dit que je dois former mes salariés à l'IA. C'est vraiment obligatoire ? | 1/1 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 38 s |
| e21 | On crée nos visuels pour les réseaux sociaux avec une IA. Il faut écrire qu'ils sont générés par IA ? | 1/2 | non | 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([3]) : ignoré(s).; La réponse cite [3] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations. | 40 s |
| e22 | Un fournisseur nous propose un outil qui analyse les émotions des salariés pendant les visioconférences. On a le droit de l'utiliser ? | 2/2 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 30 s |
| e23 | Si l'outil d'IA qu'on a acheté se trompe et écarte injustement un candidat, qui est responsable : moi ou le fournisseur ? | 4/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 48 s |
| e24 | À partir de quand les règles de l'AI Act s'appliquent vraiment ? Qu'est-ce qui est déjà en vigueur ? | 4/4 | non | — | 40 s |
| e25 | Mes salariés copient des données clients dans ChatGPT pour aller plus vite. C'est un problème ? Comment je peux encadrer ça ? | 3/4 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 60 s |
| he01 | Comment je déclare la TVA chaque trimestre ? | 0/0 | oui | — | 16 s |
| he02 | Si un salarié en CDI démissionne, combien de temps dure son préavis ? | 0/0 | oui | — | 14 s |
| he03 | Tu as des idées pour organiser une fête de fin d'année pour les bénévoles avec un petit budget ? | 0/0 | oui | — | 20 s |

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
Attention : Extraits trop longs : le code a arrêté leur recopie après 1200 tokens pour garder au moins 800 tokens à la réponse (dernier extrait raccourci ou retiré ; le passage complet est dans les sources).
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. Cette obligation ne s’applique pas aux systèmes d’IA dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers, sauf si ces systèmes sont mis à la disposition du public pour permettre le signalement d’une infraction pénale. »  
- [2] « Aux fins du paragraphe 1, premier alinéa, point h), et du paragraphe 2, chaque utilisation à des fins répressives d’un système d’identification biométrique à distance en temps réel dans des espaces accessibles au public est subordonnée à une autorisation préalable octroyée par une autorité judiciaire ou une autorité administrative indépendante dont la décision est contraignante de l’État membre dans lequel cette utilisation doit avoir lieu, délivrée sur demande motivée et conformément aux règles détaillées du droit national visées au paragraphe 5. Toutefois, dans une situation d’urgence dûment justifiée, il est possible de commencer à utiliser ce système sans autorisation à condition que cette autorisation soit demandée sans retard injustifié, au plus tard dans les 24 heures. Si cette autorisation est rejetée, il est mis fin à l’utilisation avec effet immédiat, et toutes les données, ainsi que les résultats et sorties de cette utilisation, sont immédiatement mis au rebut et supprimés. »  
- [3] « la mise sur le marché, la mise en service ou l’utilisation de systèmes d’IA pour mener des évaluations des risques des personnes physiques visant à évaluer ou à prédire le risque qu’une personne physique commette une infraction pénale, uniquement sur la base du profilage d’une personne physique ou de l’évaluation de ses traits de personnalité ou caractéristiques; cette interdiction ne s’applique pas aux systèmes d’IA utilisés pour étayer l’évaluation humaine de l’implication d’une personne dans une activité criminelle, qui est déjà fondée sur des faits objectifs et vérifiables, directement liés à une activité criminelle; »  
- [4] « L’utilisation de systèmes d’identification biométriques à distance en temps réel dans des espaces accessibles au public à des fins répressives en vue de la réalisation de l’un des objectifs énumérés au paragraphe 1, premier alinéa, point h), n’est déployée aux fins énoncées audit point, que pour confirmer l’identité de la personne spécifiquement ciblée et tient compte des éléments suivants: a) la nature de la situation donnant lieu à un éventuel recours au système, en particulier la gravité, la probabilité et l’ampleur du préjudice qui serait causé si le système n’était pas utilisé; b) les conséquences de l’utilisation du système sur les droits et libertés de toutes les personnes concernées, notamment la gravité, la probabilité et l’ampleur de ces conséquences. En outre, l’utilisation de systèmes d’identification biométriques à distance en temps réel dans des espaces accessibles au public à des fins répressives en vue de la réalisation de l’un des objectifs énumérés au paragraphe 1, premier alinéa, point h), du présent article respecte les garanties et conditions nécessaires et proportionnées en ce qui concerne cette utilisation, conformément au droit national qui l’autorise, notamment eu égard aux limitations temporelles, géographiques et relatives aux personnes. L’utilisation du système d’identification biométrique à distance en temps réel dans des espaces accessibles au public n’est autorisée que si l’autorité répressive a réalisé une analyse d’impact sur les droits fondamentaux conformément à l’article 27 et a enregistré le système dans la base de données de l’UE prévue par l’article 49. Toutefois, dans des cas d’urgence dûment justifiés, il est possible de commencer à utiliser ces systèmes sans enregistrement dans la base de données de l’UE, à condition que cet enregistrement soit effectué sans retard injustifié. »  
- [5] « Si une inspection sur place des locaux commerciaux, des terrains ou des biens immobiliers nécessite l'autorisation d'une autorité judiciaire conformément au droit national, le Bureau de l'IA demande cette autorisation. Cette autorisation peut également être demandée par le Bureau de l'IA à titre préventif. … »

RÉPONSE :
Non, vous n’avez pas le droit d’installer des caméras dans votre magasin ou dans la salle de pause simplement parce que vous le souhaitez. L’installation de caméras à des fins de surveillance, notamment dans des espaces accessibles au public comme un magasin ou une salle de pause, peut être considérée comme une utilisation à des fins répressives d’un système d’identification biométrique à distance en temps réel, notamment si les caméras sont utilisées pour identifier des personnes ou pour enregistrer leurs comportements. Selon l’article 5, point h), de l’AI Act, cette utilisation est subordonnée à une autorisation préalable d’une autorité judiciaire ou administrative indépendante, dont la décision est contraignante, délivrée sur demande motivée et conformément aux règles du droit national. Cette autorisation ne peut être délivrée que si l’usage est nécessaire, proportionné, limité au strict nécessaire en termes de temps et de portée géographique, et si une analyse d’impact sur les droits fondamentaux a été réalisée. Vous devez donc informer vos salariés que l’installation de caméras est autorisée uniquement après une autorisation officielle, et que cette autorisation est conditionnée à une évaluation des risques sur les droits fondamentaux. Vous devez également leur préciser que les données recueillies seront utilisées uniquement pour des fins de sécurité, et que toute utilisation à des fins répressives ou de profilage de personnes est interdite, sauf dans des cas spécifiques fondés sur des faits objectifs vérifiables. En l’absence d’une autorisation officielle, l’installation de caméras est interdite. [2] [4] [3]
```

</details>

Temps : recherche 2.5 s · génération 94.3 s (5254 tokens lus, 1599 écrits, 30.7 tokens/s) · contrôle de pertinence 10.2 s

## e02 — Une ancienne cliente me demande d'effacer toutes ses données. On doit garder ses factures pour la comptabilité. Je dois quand même tout supprimer ?

Article attendu : RGPD art. 17 — passage [1].

### Réponse du copilote

> Non, vous n'êtes pas obligé d'effacer toutes les données de l'ancienne cliente, car le traitement des factures pour la comptabilité relève d'une finalité légitime et nécessaire, conforme à l'article 5, point c) du RGPD, qui exige que les données soient « pertinentes et limitées à ce qui est nécessaire ». Cela signifie que les données peuvent être conservées dans la mesure où elles sont nécessaires au traitement archivistique, notamment pour la comptabilité, à condition que ce traitement soit dans l'intérêt public ou conforme à une obligation légale (RGPD, article 5, point e). Cependant, l'effacement ne s'applique pas dans la mesure où le traitement est nécessaire à des fins archivistiques, à des fins de recherche scientifique ou historique ou à des fins statistiques, conformément à l'article 89, paragraphe 1, « dans la mesure où le droit visé au paragraphe 1 est susceptible de rendre impossible ou de compromettre gravement la réalisation des objectifs dudit traitement » [1]. Ainsi, les factures peuvent être conservées, à condition que le traitement soit justifié par une finalité légitime et nécessaire, comme la comptabilité. Les données personnelles ne doivent pas être effacées si elles sont nécessaires à un traitement légal ou à des fins archivistiques dans l'intérêt public [1].

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
Attention : La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à condition que ce traitement soit dans l'intérêt public ou conforme à une obligation légale » (et 1 autre(s)). Vérifiez-la dans les textes.
Attention : La réponse ne reprend que 4 des 6 cas énumérés au passage [1], sans dire qu'elle n'en cite qu'une partie. Vérifiez la liste complète.

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
Non, vous n'êtes pas obligé d'effacer toutes les données de l'ancienne cliente, car le traitement des factures pour la comptabilité relève d'une finalité légitime et nécessaire, conforme à l'article 5, point c) du RGPD, qui exige que les données soient « pertinentes et limitées à ce qui est nécessaire ». Cela signifie que les données peuvent être conservées dans la mesure où elles sont nécessaires au traitement archivistique, notamment pour la comptabilité, à condition que ce traitement soit dans l'intérêt public ou conforme à une obligation légale (RGPD, article 5, point e). Cependant, l'effacement ne s'applique pas dans la mesure où le traitement est nécessaire à des fins archivistiques, à des fins de recherche scientifique ou historique ou à des fins statistiques, conformément à l'article 89, paragraphe 1, « dans la mesure où le droit visé au paragraphe 1 est susceptible de rendre impossible ou de compromettre gravement la réalisation des objectifs dudit traitement » [1]. Ainsi, les factures peuvent être conservées, à condition que le traitement soit justifié par une finalité légitime et nécessaire, comme la comptabilité. Les données personnelles ne doivent pas être effacées si elles sont nécessaires à un traitement légal ou à des fins archivistiques dans l'intérêt public [1].
```

</details>

Temps : recherche 2.3 s · génération 39.7 s (3302 tokens lus, 655 écrits, 33.2 tokens/s) · contrôle de pertinence 5.4 s

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

Temps : recherche 2.3 s · génération 13.2 s (2278 tokens lus, 75 écrits, 36.8 tokens/s)

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
Oui, cela peut constituer un problème, car votre association doit tenir un registre des activités de traitement, notamment les données à caractère personnel comme les adresses et téléphones des bénévoles (RGPD, article 30). Ce registre doit être mis à la disposition de l'autorité de contrôle sur demande (RGPD, article 30, paragraphe 4). Toutefois, si votre association compte moins de 250 employés et que le traitement des données des bénévoles est occasionnel et ne concerne pas des catégories particulières de données (comme celles visées à l'article 9 ou des données relatives à des condamnations pénales), alors les obligations s'appliquent seulement si le traitement comporte un risque pour les droits et libertés des personnes concernées (RGPD, article 30, paragraphe 5). Ainsi, le fait de garder les données dans un fichier Excel partagé sur Google Drive ne constitue pas automatiquement un problème, à condition que le traitement soit occasionnel et ne porte pas sur des données sensibles. Si le traitement est répété ou s’il concerne des données sensibles, une obligation de registre s’applique.
```

</details>

Temps : recherche 2.2 s · génération 36.9 s (3261 tokens lus, 589 écrits, 33.5 tokens/s) · contrôle de pertinence 3.7 s

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
Non, vous n'êtes pas obligé de mettre un bandeau cookies sur votre site web pour utiliser Google Analytics, car ce service ne relève pas d'une obligation de mise en place de bandeau spécifique selon les textes fournis. Les passages ci-dessus ne mentionnent aucune obligation de bandeau cookies, ni de transparence spécifique pour les outils de suivi comme Google Analytics. Le RGPD (article 42) parle de certification, de labels et de garanties appropriées dans le cadre des transferts de données, mais ne prévoit pas une obligation de bandeau pour les outils de suivi. L'AI Act ne traite pas de la gestion des cookies ni de la transparence en matière de traçabilité des utilisateurs sur les sites web. Aucun des textes ne prévoit une obligation de bandeau cookies pour les outils de statistiques comme Google Analytics. Les obligations de transparence (article 50) ou de certification (article 42) s'appliquent à des cas spécifiques de traitement de données, comme les catégories particulières ou les contenus générés par l'IA, mais ne couvrent pas le cas d'un simple outil de suivi de trafic. Les règles sur les cookies sont donc absentes des passages fournis.
```

</details>

Temps : recherche 2.2 s · génération 43.6 s (4009 tokens lus, 536 écrits, 31.8 tokens/s) · contrôle de pertinence 4.6 s

## e06 — La boîte mail de l'accueil a été piratée hier. Qu'est-ce que je dois faire ? Je dois prévenir quelqu'un ?

Article attendu : RGPD art. 33 ou RGPD art. 34 — passage [1].

### Réponse du copilote

> Oui, vous devez prévenir l'autorité de contrôle compétente, car une violation de données à caractère personnel a eu lieu (la boîte mail a été piratée). Selon l'article 33, [1], vous devez notifiez la violation à l'autorité de contrôle dans les meilleurs délais, et si possible, dans les 72 heures après en avoir pris connaissance, « à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques ». Si la violation est susceptible d'engendrer un risque élevé, vous devez également communiquer à la personne concernée, selon l'article 34, [2]. Vous devez également notifiez à chaque destinataire des données concernées, selon l'article 19, [3]. La notification à l'autorité de contrôle doit inclure les informations prévues à l'article 33, paragraphe 3, points b), c) et d), et, si possible, être faite de manière échelonnée sans autre retard indu, [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. »
  [1] « Lorsque la notification à l'autorité de contrôle n'a pas lieu dans les 72 heures, elle est accompagnée des motifs du retard. »
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
- [1] « En cas de violation de données à caractère personnel, le responsable du traitement en notifie la violation en question à l'autorité de contrôle compétente conformément à l'article 55, dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques. »
- [1] « Lorsque la notification à l'autorité de contrôle n'a pas lieu dans les 72 heures, elle est accompagnée des motifs du retard. »
- [1] « Le sous-traitant notifie au responsable du traitement toute violation de données à caractère personnel dans les meilleurs délais après en avoir pris connaissance. »
- [2] « Lorsqu'une violation de données à caractère personnel est susceptible d'engendrer un risque élevé pour les droits et libertés d'une personne physique, le responsable du traitement communique la violation de données à caractère personnel à la personne concernée dans les meilleurs délais. »
- [2] « La communication à la personne concernée visée au paragraphe 1 du présent article décrit, en des termes clairs et simples, la nature de la violation de données à caractère personnel et contient au moins les informations et mesures visées à l'article 33, paragraphe 3, points b), c) et d). »
- [3] « Le responsable du traitement notifie à chaque destinataire auquel les données à caractère personnel ont été communiquées toute rectification ou tout effacement de données à caractère personnel ou toute limitation du traitement effectué conformément à l'article 16, à l'article 17, paragraphe 1, et à l'article 18, à moins qu'une telle communication se révèle impossible ou exige des efforts disproportionnés. »
- [4] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: … »

RÉPONSE :
Oui, vous devez prévenir l'autorité de contrôle compétente, car une violation de données à caractère personnel a eu lieu (la boîte mail a été piratée). Selon l'article 33, [1], vous devez notifiez la violation à l'autorité de contrôle dans les meilleurs délais, et si possible, dans les 72 heures après en avoir pris connaissance, « à moins que la violation en question ne soit pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques ». Si la violation est susceptible d'engendrer un risque élevé, vous devez également communiquer à la personne concernée, selon l'article 34, [2]. Vous devez également notifiez à chaque destinataire des données concernées, selon l'article 19, [3]. La notification à l'autorité de contrôle doit inclure les informations prévues à l'article 33, paragraphe 3, points b), c) et d), et, si possible, être faite de manière échelonnée sans autre retard indu, [1].
```

</details>

Temps : recherche 3.4 s · génération 42.0 s (3231 tokens lus, 739 écrits, 33.3 tokens/s) · contrôle de pertinence 6.4 s

## e07 — Un prestataire extérieur gère notre paie. Je dois signer un contrat spécial avec lui pour les données ?

Article attendu : RGPD art. 28, paragraphe 3 — absent des passages donnés au modèle.

### Réponse du copilote

> Oui : vous devez signer un contrat spécial avec le prestataire extérieur gérant votre paie, car il s'agit d'un sous-traitant qui traite des données à caractère personnel pour votre organisation [4]. Ce contrat doit inclure des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées afin que le traitement réponde aux exigences du RGPD [2]. Si ce prestataire recrute d'autres prestataires (par exemple, pour gérer les calculs ou les déclarations), les mêmes obligations s'appliquent à ces autres sous-traitants par contrat ou autre acte juridique [1].

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
Oui : vous devez signer un contrat spécial avec le prestataire extérieur gérant votre paie, car il s'agit d'un sous-traitant qui traite des données à caractère personnel pour votre organisation [4]. Ce contrat doit inclure des garanties suffisantes quant à la mise en œuvre de mesures techniques et organisationnelles appropriées afin que le traitement réponde aux exigences du RGPD [2]. Si ce prestataire recrute d'autres prestataires (par exemple, pour gérer les calculs ou les déclarations), les mêmes obligations s'appliquent à ces autres sous-traitants par contrat ou autre acte juridique [1].
```

</details>

Temps : recherche 2.5 s · génération 28.8 s (2697 tokens lus, 481 écrits, 34.9 tokens/s) · contrôle de pertinence 5.7 s

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
Non : vous ne pouvez pas envoyer une newsletter à vos anciens clients sans leur demander leur accord, car le traitement des données à caractère personnel à des fins de prospection (comme une newsletter) relève du droit d'opposition de la personne concernée (RGPD, article 21, paragraphe 1 et 2) et est considéré comme un traitement à des fins de prospection. Cela implique que la personne concernée a le droit de s'opposer à ce traitement à tout moment, y compris au profilage lié à cette prospection (RGPD, article 21, paragraphe 2). De plus, le traitement automatisé (comme l'envoi d'une newsletter) peut être considéré comme une décision fondée sur un traitement automatisé, ce qui donne droit à la personne concernée de ne pas être soumise à une telle décision (RGPD, article 22, paragraphe 1). En l'absence de consentement explicite, le traitement ne peut pas être effectué, car le consentement est une base légale obligatoire (RGPD, article 7, paragraphe 3). Ainsi, le retrait du consentement ne compromet pas la licéité des traitements antérieurs, mais cela ne signifie pas que le traitement peut être effectué sans consentement (RGPD, article 7, paragraphe 3). L'absence de consentement implique donc une violation du RGPD. [1]
```

</details>

Temps : recherche 2.2 s · génération 41.9 s (3510 tokens lus, 663 écrits, 32.7 tokens/s) · contrôle de pertinence 4.9 s

## e09 — Un salarié me demande une copie de toutes les données que j'ai sur lui, même les mails où on parle de lui. Je dois tout lui donner ? J'ai combien de temps pour répondre ?

Article attendu : RGPD art. 15 ou RGPD art. 12, paragraphe 3 — passage [1].

### Réponse du copilote

> Non, vous n'avez pas l'obligation de fournir toutes les données, y compris les mails où on parle de vous, car le droit d'accès ne porte pas atteinte aux droits et libertés d'autrui [4], et les données doivent être fournies de manière appropriée, sans dépasser les données personnelles strictement liées au traitement [3]. Vous devez fournir une copie des données à caractère personnel faisant l'objet d'un traitement, mais pas nécessairement toutes les communications, notamment si elles ne sont pas directement liées à un traitement de données personnelles [3]. Vous devez répondre dans un délai d'un mois à compter de la réception de la demande [1], sauf si la demande est complexe ou si le nombre de demandes est élevé, auquel cas le délai peut être prolongé de deux mois [1]. Ce délai peut être prolongé, mais vous devez informer la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le responsable du traitement fournit à la personne concernée des informations sur les mesures prises à la suite d'une demande formulée en application des articles 15 à 22, dans les meilleurs délais et en tout état de cause dans un délai d'un mois à compter de la réception de la demande. Au besoin, ce délai peut être prolongé de deux mois, compte tenu de la complexité et du nombre de demandes. Le responsable du traitement informe la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande. Lorsque la personne concernée présente sa demande sous une forme électronique, les informations sont fournies par voie électronique lorsque cela est possible, à moins que la personne concernée ne demande qu'il en soit autrement. »
  [3] « Le responsable du traitement fournit une copie des données à caractère personnel faisant l'objet d'un traitement. Le responsable du traitement peut exiger le paiement de frais raisonnables basés sur les coûts administratifs pour toute copie supplémentaire demandée par la personne concernée. Lorsque la personne concernée présente sa demande par voie électronique, les informations sont fournies sous une forme électronique d'usage courant, à moins que la personne concernée ne demande qu'il en soit autrement. »
  [4] « a) dans un délai raisonnable après avoir obtenu les données à caractère personnel, mais ne dépassant pas un mois, eu égard aux circonstances particulières dans lesquelles les données à caractère personnel sont traitées; »
  [5] « le cas échéant, les destinataires ou les catégories de destinataires des données à caractère personnel; »

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
- [5] « le cas échéant, les destinataires ou les catégories de destinataires des données à caractère personnel; »  

RÉPONSE :  
Non, vous n'avez pas l'obligation de fournir toutes les données, y compris les mails où on parle de vous, car le droit d'accès ne porte pas atteinte aux droits et libertés d'autrui [4], et les données doivent être fournies de manière appropriée, sans dépasser les données personnelles strictement liées au traitement [3]. Vous devez fournir une copie des données à caractère personnel faisant l'objet d'un traitement, mais pas nécessairement toutes les communications, notamment si elles ne sont pas directement liées à un traitement de données personnelles [3]. Vous devez répondre dans un délai d'un mois à compter de la réception de la demande [1], sauf si la demande est complexe ou si le nombre de demandes est élevé, auquel cas le délai peut être prolongé de deux mois [1]. Ce délai peut être prolongé, mais vous devez informer la personne concernée de cette prolongation et des motifs du report dans un délai d'un mois à compter de la réception de la demande [1].
```

</details>

Temps : recherche 2.3 s · génération 35.2 s (2902 tokens lus, 637 écrits, 34.3 tokens/s) · contrôle de pertinence 5.5 s

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
- [1] « Les États membres peuvent prévoir, par la loi ou au moyen de conventions collectives, des règles plus spécifiques pour assurer la protection des droits et libertés en ce qui concerne le traitement des données à caractère personnel des employés dans le cadre des relations de travail… »  
- [3] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: … c) les destinataires ou catégories de destinataires auxquels les données à caractère personnel ont été ou seront communiquées, en particulier les destinataires qui sont établis dans des pays tiers ou les organisations internationales; … d) lorsque cela est possible, la durée de conservation des données à caractère personnel envisagée ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; … »  
- [4] « Chaque responsable du traitement et, le cas échéant, le représentant du responsable du traitement tiennent un registre des activités de traitement effectuées sous leur responsabilité. Ce registre comporte toutes les informations suivantes: … d) les catégories de destinataires auxquels les données à caractère personnel ont été ou seront communiquées, y compris les destinataires dans des pays tiers ou des organisations internationales; … f) dans la mesure du possible, les délais prévus pour l'effacement des différentes catégories de données; … »  

RÉPONSE :  
Oui, vous pouvez encore lire la boîte mail professionnelle d’un salarié parti, à condition que le traitement des données à caractère personnel (comme les e-mails) soit encore considéré comme en cours de traitement, et que les données soient conservées dans le cadre des finalités prévues par l’entreprise, notamment pour la gestion du travail ou la planification. Le RGPD, article 15, permet à la personne concernée d’obtenir l’accès aux données à caractère personnel, y compris les e-mails, tant qu’elles sont traitées. Cependant, le registre des activités de traitement (article 4), point d), précise que les destinataires et les catégories de données sont documentées, et que les délais prévus pour l’effacement des données sont indiqués. Si ces délais ne sont pas encore atteints, les données peuvent être conservées. Le traitement peut être justifié par des finalités liées à l’exécution du contrat de travail ou à la gestion du travail, même après la fin de la relation de travail. L’effacement des données est prévu dans la mesure du possible (article 4, point f), mais ne s’applique pas automatiquement à la fin de la relation de travail, sauf si les données ne sont pas nécessaires à l’exécution d’une mission d’intérêt public ou à l’exercice d’une autorité publique (article 20, point 3). Ainsi, la conservation de la boîte mail professionnelle dépend de la finalité du traitement, de la durée de conservation prévue et de la nécessité de conserver les données pour des raisons professionnelles ou légales.
```

</details>

Temps : recherche 2.2 s · génération 55.9 s (4486 tokens lus, 734 écrits, 30.7 tokens/s) · contrôle de pertinence 5.9 s

## e11 — Dans notre organisme de formation, on demande aux stagiaires leur numéro de sécurité sociale et des informations sur leur handicap. On a le droit ?

Article attendu : RGPD art. 9, paragraphe 1 ou RGPD art. 9, paragraphe 2_a i ou RGPD art. 87 — passage [3].

### Réponse du copilote

> Oui, vous avez le droit de demander aux stagiaires leur numéro de sécurité sociale et des informations sur leur handicap, car ces données ne relèvent pas des catégories interdites au regard de l’article 9, point 1 du RGPD [3]. Cependant, le traitement de données concernant la santé (comme les informations sur le handicap) est interdit par l’article 9, point 1, du RGPD [3]. Ainsi, le traitement de ces données est interdit, sauf si une exception s’applique, comme le traitement par un professionnel de la santé soumis à une obligation de secret professionnel [2]. Dans le cadre d’un organisme de formation, si ces données sont utilisées pour des fins d’accompagnement ou de gestion de la diversité, elles doivent être traitées uniquement dans des conditions strictes, notamment en lien avec des finalités de santé ou de protection, et sous réserve de l’existence d’une obligation de secret professionnel ou d’un cadre légal spécifique [4]. Les données sur le handicap relèvent de la catégorie « données concernant la santé » [3], donc leur traitement est interdit sauf dans des cas précis autorisés par la loi ou par des règles nationales spécifiques. Les passages trouvés ne permettent pas de dire si une exception s’applique ici, car aucune mention n’est faite de l’usage d’un professionnel de santé ou d’un cadre de traitement autorisé dans un contexte de formation.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « Le traitement des données à caractère personnel qui révèle l'origine raciale ou ethnique, les opinions politiques, les convictions religieuses ou philosophiques ou l'appartenance syndicale, ainsi que le traitement des données génétiques, des données biométriques aux fins d'identifier une personne physique de manière unique, des données concernant la santé ou des données concernant la vie sexuelle ou l'orientation sexuelle d'une personne physique sont interdits. »

Sources citées :
  [2] RGPD — règlement (UE) 2016/679, article 9, paragraphe 3 : Traitement portant sur des catégories particulières de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
  [3] RGPD — règlement (UE) 2016/679, article 9, paragraphe 1 : Traitement portant sur des catégories particulières de données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_9
  [4] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
Passages consultés mais non cités :
  [1] RGPD — règlement (UE) 2016/679, article 20 : Droit à la portabilité des données
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_20
  [5] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
Attention : La réponse cite [2], [4] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.
Attention : La réponse formule une exception qui ne reprend pas les extraits vérifiés : « sauf si une exception s’applique, comme le traitement par un professionnel de la santé » (et 2 autre(s)). Vérifiez-la dans les textes.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [3] « Le traitement des données à caractère personnel qui révèle l'origine raciale ou ethnique, les opinions politiques, les convictions religieuses ou philosophiques ou l'appartenance syndicale, ainsi que le traitement des données génétiques, des données biométriques aux fins d'identifier une personne physique de manière unique, des données concernant la santé ou des données concernant la vie sexuelle ou l'orientation sexuelle d'une personne physique sont interdits. »  

RÉPONSE :  
Oui, vous avez le droit de demander aux stagiaires leur numéro de sécurité sociale et des informations sur leur handicap, car ces données ne relèvent pas des catégories interdites au regard de l’article 9, point 1 du RGPD [3]. Cependant, le traitement de données concernant la santé (comme les informations sur le handicap) est interdit par l’article 9, point 1, du RGPD [3]. Ainsi, le traitement de ces données est interdit, sauf si une exception s’applique, comme le traitement par un professionnel de la santé soumis à une obligation de secret professionnel [2]. Dans le cadre d’un organisme de formation, si ces données sont utilisées pour des fins d’accompagnement ou de gestion de la diversité, elles doivent être traitées uniquement dans des conditions strictes, notamment en lien avec des finalités de santé ou de protection, et sous réserve de l’existence d’une obligation de secret professionnel ou d’un cadre légal spécifique [4]. Les données sur le handicap relèvent de la catégorie « données concernant la santé » [3], donc leur traitement est interdit sauf dans des cas précis autorisés par la loi ou par des règles nationales spécifiques. Les passages trouvés ne permettent pas de dire si une exception s’applique ici, car aucune mention n’est faite de l’usage d’un professionnel de santé ou d’un cadre de traitement autorisé dans un contexte de formation.
```

</details>

Temps : recherche 2.4 s · génération 30.8 s (3010 tokens lus, 445 écrits, 34.2 tokens/s) · contrôle de pertinence 4.3 s

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
Les textes trouvés ne traitent pas de la surveillance des véhicules de techniciens par GPS. La question porte sur une pratique de suivi de véhicules, qui n'est pas abordée dans les passages fournis, qui se limitent à la mise en œuvre de codes de conduite, aux sous-traitants et aux garanties de protection des données, sans mentionner la surveillance par GPS ni les conditions de traitement de données relatives aux véhicules.
```

</details>

Temps : recherche 2.3 s · génération 16.0 s (2548 tokens lus, 113 écrits, 35.9 tokens/s)

## e13 — On veut publier sur Facebook des photos des bénévoles prises pendant notre fête annuelle. Il faut leur accord écrit ?

Article attendu : RGPD art. 6, paragraphe 1 ou RGPD art. 7 — absent des passages donnés au modèle.

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Passages consultés mais non cités :
  [1] AI Act — règlement (UE) 2024/1689, article 31, paragraphe 7 : Exigences concernant les organismes notifiés
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_31
  [2] AI Act — règlement (UE) 2024/1689, article 31, paragraphe 1 : Exigences concernant les organismes notifiés
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_31
  [3] AI Act — règlement (UE) 2024/1689, article 61 : Consentement éclairé à participer aux essais en conditions réelles en dehors des bacs à sable réglementaires de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_61
  [4] AI Act — règlement (UE) 2024/1689, article 31, paragraphe 11 : Exigences concernant les organismes notifiés
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_31
  [5] AI Act — règlement (UE) 2024/1689, article 45 : Obligations d’information des organismes notifiés
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_45
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Le personnel des organismes notifiés est lié par le secret professionnel pour toutes les informations dont il a connaissance dans l’exercice de ses fonctions au titre du présent règlement, sauf à l’égard des autorités notifiantes de l’État membre où il exerce ses activités. »  
- [3] « Le consentement éclairé est daté et documenté et une copie en est remise aux participants aux essais ou à leur représentant légal. »  
- [5] « Chaque organisme notifié porte à la connaissance des autres organismes notifiés: … les certificats d’évaluation UE de la documentation technique ou les documents complémentaires y afférents qu’il a refusés, retirés, suspendus ou soumis à d’autres restrictions et, sur demande, les certificats et/ou documents complémentaires y afférents qu’il a délivrés. »  

RÉPONSE :  
Non, il n’y a pas d’obligation d’obtention d’un consentement écrit pour publier des photos de bénévoles prises pendant une fête annuelle, car les passages ci-dessus concernent des contextes spécifiques (évaluation de la conformité des systèmes d’IA, organismes notifiés, secrets professionnels, essais en conditions réelles), et ne s’appliquent pas à la publication de photos de bénévoles dans un cadre social ou associatif. Les exigences de consentement éclairé (article 61, point 1) s’appliquent uniquement aux essais en conditions réelles, pas à des activités de communication ou de diffusion de photos. Les textes trouvés ne traitent pas directement de la publication de photos de bénévoles dans un cadre associatif.
```

</details>

Temps : recherche 2.2 s · génération 25.2 s (2626 tokens lus, 404 écrits, 35.2 tokens/s) · contrôle de pertinence 5.6 s

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
Oui : vous devez tenir un registre des activités de traitement (RGPD, article 30, paragraphe 1), car le nombre d’employés (8) est inférieur à 250, mais les obligations s’appliquent sauf si le traitement ne comporte pas de risque pour les droits et libertés des personnes concernées, s’il est occasionnel ou s’il ne porte pas sur des catégories particulières de données (RGPD, article 30, paragraphe 5). Concernant le délégué à la protection des données (DPO), il n’est pas obligatoire pour une entreprise de 8 salariés, sauf si les activités de traitement consistent en un traitement à grande échelle de catégories particulières de données (article 37, point c) ou si elles exigent un suivi régulier et systématique à grande échelle des personnes concernées (article 37, point b). Comme le nombre d’employés est faible (8), et que le traitement n’est pas décrit comme à grande échelle, le DPO n’est pas obligatoire dans ce cas. Les passages trouvés ne permettent pas de conclure qu’un DPO est nécessaire pour un groupe de 8 salariés, sauf dans des cas précis précisés dans l'article 37.
```

</details>

Temps : recherche 2.5 s · génération 52.5 s (4044 tokens lus, 791 écrits, 31.4 tokens/s) · contrôle de pertinence 6.7 s

## e15 — Notre logiciel de gestion des clients est hébergé aux États-Unis. C'est autorisé ?

Article attendu : RGPD art. 44 ou RGPD art. 45, paragraphe 1 ou RGPD art. 46 — passage [1].

### Réponse du copilote

> Oui, le transfert de données à caractère personnel vers les États-Unis est autorisé, à condition que l'un des mécanismes prévus par le RGPD soit respecté. Si les États-Unis n'ont pas été reconnus comme assurant un niveau de protection adéquat par une décision de la Commission européenne (article 45), alors le transfert doit être fondé sur des garanties appropriées (article 46), par exemple des clauses types de protection des données approuvées par la Commission, ou des règles d'entreprise contraignantes, ou un mécanisme de certification approuvé. Si aucune de ces conditions n'est remplie, le transfert peut être autorisé uniquement dans des cas particuliers prévus à l'article 49, comme le consentement explicite, la nécessité contractuelle, ou la sauvegarde des intérêts vitaux. Le responsable du traitement doit informer l'autorité de contrôle du transfert et la personne concernée, notamment sur les intérêts légitimes impérieux qu'il poursuit [5]. Le transfert ne peut pas être répétitif ni toucher un grand nombre de personnes, et doit être justifié par une évaluation des circonstances [5]. Les conditions du transfert doivent être respectées, notamment pour les transferts ultérieurs vers d'autres pays [3].

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
Oui, le transfert de données à caractère personnel vers les États-Unis est autorisé, à condition que l'un des mécanismes prévus par le RGPD soit respecté. Si les États-Unis n'ont pas été reconnus comme assurant un niveau de protection adéquat par une décision de la Commission européenne (article 45), alors le transfert doit être fondé sur des garanties appropriées (article 46), par exemple des clauses types de protection des données approuvées par la Commission, ou des règles d'entreprise contraignantes, ou un mécanisme de certification approuvé. Si aucune de ces conditions n'est remplie, le transfert peut être autorisé uniquement dans des cas particuliers prévus à l'article 49, comme le consentement explicite, la nécessité contractuelle, ou la sauvegarde des intérêts vitaux. Le responsable du traitement doit informer l'autorité de contrôle du transfert et la personne concernée, notamment sur les intérêts légitimes impérieux qu'il poursuit [5]. Le transfert ne peut pas être répétitif ni toucher un grand nombre de personnes, et doit être justifié par une évaluation des circonstances [5]. Les conditions du transfert doivent être respectées, notamment pour les transferts ultérieurs vers d'autres pays [3].
```

</details>

Temps : recherche 3.0 s · génération 48.0 s (3349 tokens lus, 876 écrits, 32.8 tokens/s) · contrôle de pertinence 8.7 s

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
Oui, l’AI Act peut vous concerne même si vous ne créez pas d’IA, car il s’applique aux utilisateurs de systèmes d’IA, notamment lorsqu’ils sont situés dans l’Union (article 2, point g) du règlement). Cela inclut l’utilisation d’outils comme ChatGPT, tant que ces outils sont mis en service ou utilisés dans l’Union. Toutefois, l’AI Act ne s’applique pas aux systèmes d’IA utilisés exclusivement à des fins militaires, de défense ou de sécurité nationale (article 4), ni aux systèmes spécifiquement développés pour la recherche scientifique (article 1). Si votre utilisation ne vise pas ces cas, et que vous n’êtes pas un fournisseur ou déployeur, l’obligation directe n’est pas exercée, mais vous êtes toujours concerné comme « personne concernée » située dans l’Union [2]. L’interdiction de certaines pratiques (comme la manipulation de contenus ou la reconnaissance faciale) s’applique aussi à l’utilisation d’outils d’IA, à condition que le système ne soit pas conçu pour produire ou manipuler des contenus sexuels ou réalistes sans consentement [5].
```

</details>

Temps : recherche 3.2 s · génération 41.3 s (3201 tokens lus, 718 écrits, 33.2 tokens/s) · contrôle de pertinence 6.7 s

## e17 — Je voudrais utiliser un logiciel d'IA qui trie automatiquement les CV. C'est interdit ? Sinon, quelles règles je dois respecter ?

Article attendu : AI Act annexe III, point 4 ou AI Act art. 26 — passage [3].

### Réponse du copilote

> Non, l’utilisation d’un logiciel d’IA qui trie automatiquement les CV n’est pas interdite par l’AI Act, à condition qu’il ne soit pas utilisé pour évaluer les candidats sur la base de traits de personnalité, de comportement ou de caractéristiques personnelles déduites ou prédites, ce qui serait interdit selon l’article 5, point c) [1]. Ce type de système relève des systèmes d’IA à haut risque au sens de l’article 6, paragraphe 2, point 4, a) [3], car il est destiné à être utilisé dans le cadre du recrutement ou de la sélection de personnes physiques. Pour cela, vous devez respecter les règles de contrôle humain prévues à l’article 14, notamment en assurant que les personnes chargées de superviser le système peuvent comprendre ses capacités et ses limites, détecter les anomalies, interpréter ses sorties, décider de ne pas utiliser le système ou d’interrompre son fonctionnement, et que les décisions ne soient pas prises sans vérification distincte par au moins deux personnes disposant des compétences et de l’autorité nécessaires [4]. Ces obligations s’appliquent particulièrement aux systèmes d’IA à haut risque, comme le recrutement, et doivent être mises en œuvre pour prévenir les risques pour les droits fondamentaux ou la sécurité [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des domaines suivants: 4. Emploi, gestion de la main-d'œuvre et accès à l'emploi indépendant: a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; b) systèmes d'IA destinés à être utilisés pour prendre des décisions influant sur les conditions des relations professionnelles, la promotion ou le licenciement dans le cadre de relations professionnelles contractuelles, pour attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques personnelles ou pour suivre et évaluer les performances et le comportement de personnes dans le cadre de telles relations. »
  [4] « 1. La conception et le développement des systèmes d’IA à haut risque permettent, notamment au moyen d’interfaces homme-machine appropriées, un contrôle effectif par des personnes physiques pendant leur période d’utilisation. 2. Le contrôle humain vise à prévenir ou à réduire au minimum les risques pour la santé, la sécurité ou les droits fondamentaux qui peuvent apparaître lorsqu’un système d’IA à haut risque est utilisé conformément à sa destination ou dans des conditions de mauvaise utilisation raisonnablement prévisible, en particulier lorsque de tels risques persistent malgré l’application d’autres exigences énoncées dans la présente section. … »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points a) à e) : Pratiques interdites en matière d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [3] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2 (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [4] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 5, paragraphe 1, points f) à h) : Pratiques interdites en matière d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_5
  [5] AI Act — règlement (UE) 2024/1689, article 59, paragraphe 3 : Traitement ultérieur de données à caractère personnel en vue du développement de certains systèmes d’IA dans l’intérêt public dans le cadre du bac à sable réglementaire de l’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_59
Attention : Extraits trop longs : le code a arrêté leur recopie après 1200 tokens pour garder au moins 800 tokens à la réponse (dernier extrait raccourci ou retiré ; le passage complet est dans les sources).
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1]) : ignoré(s).
Attention : La réponse cite [1] sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.
Attention : La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « Non, l’utilisation d’un logiciel d’IA qui trie automatiquement les CV n’est pas interdite par l’AI Act, à condition … ». Vérifiez ce point.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « les pratiques en matière d’IA suivantes sont interdites: a) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui a recours à des techniques subliminales…; b) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui exploite les éventuelles vulnérabilités dues à l’âge, au handicap ou à la situation sociale ou économique spécifique d’une personne physique ou d’un groupe de personnes donné avec pour objectif ou effet d’altérer substantiellement le comportement de cette personne ou d’un membre de ce groupe d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne ou à un tiers; b bis) la mise sur le marché, la mise en service ou l'utilisation d'un système d'IA qui génère ou manipule des images, des vidéos, des contenus audio ou tout autre matériel similaire réalistes représentant les parties intimes d'une personne identifiable, ou une personne identifiable se livrant à des activités sexuellement explicites, sans le consentement libre, spécifique, éclairé, univoque et explicite de cette personne pour cette production ou manipulation; b ter) la mise sur le marché, la mise en service ou l'utilisation d'un système d'IA qui génère ou manipule tout matériel ou spectacle au sens de l'article 2, points c) et e), de la directive 2011/93/UE, sauf lorsqu'une défense «sans droit» s'applique en vertu du droit national; c) la mise sur le marché, la mise en service ou l’utilisation de systèmes d’IA pour l’évaluation ou la classification de personnes physiques ou de groupes de personnes au cours d’une période donnée en fonction de leur comportement social ou de caractéristiques personnelles ou de personnalité connues, déduites ou prédites, la note sociale conduisant à l’une ou l’autre des situations suivantes, ou aux deux: i) le traitement préjudiciable ou défavorable de certaines personnes physiques ou de groupes de personnes dans des contextes sociaux dissociés du contexte dans lequel les données ont été générées ou collectées à l’origine; ii) le traitement préjudiciable ou défavorable de certaines personnes ou de groupes de personnes, qui est injustifié ou disproportionné par rapport à leur comportement social ou à la gravité de celui-ci; d) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA pour mener des évaluations des risques des personnes physiques visant à évaluer ou à prédire le risque qu’une personne physique commette une infraction pénale, uniquement sur la base du profilage d’une personne physique ou de l’évaluation de ses traits de personnalité ou caractéristiques; cette interdiction ne s’applique pas aux systèmes d’IA utilisés pour étayer l’évaluation humaine de l’implication d’une personne dans une activité criminelle, qui est déjà fondée sur des faits objectifs et vérifiables, directement liés à une activité criminelle; e) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes d’IA qui créent ou développent des bases de données de reconnaissance faciale par le moissonnage non ciblé d’images faciales provenant de l’internet ou de la vidéosurveillance; »  
- [3] « Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des domaines suivants: 4. Emploi, gestion de la main-d'œuvre et accès à l'emploi indépendant: a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats; b) systèmes d'IA destinés à être utilisés pour prendre des décisions influant sur les conditions des relations professionnelles, la promotion ou le licenciement dans le cadre de relations professionnelles contractuelles, pour attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques personnelles ou pour suivre et évaluer les performances et le comportement de personnes dans le cadre de telles relations. »  
- [4] « 1. La conception et le développement des systèmes d’IA à haut risque permettent, notamment au moyen d’interfaces homme-machine appropriées, un contrôle effectif par des personnes physiques pendant leur période d’utilisation. 2. Le contrôle humain vise à prévenir ou à réduire au minimum les risques pour la santé, la sécurité ou les droits fondamentaux qui peuvent apparaître lorsqu’un système d’IA à haut risque est utilisé conformément à sa destination ou dans des conditions de mauvaise utilisation raisonnablement prévisible, en particulier lorsque de tels risques persistent malgré l’application d’autres exigences énoncées dans la présente section. … »

RÉPONSE :
Non, l’utilisation d’un logiciel d’IA qui trie automatiquement les CV n’est pas interdite par l’AI Act, à condition qu’il ne soit pas utilisé pour évaluer les candidats sur la base de traits de personnalité, de comportement ou de caractéristiques personnelles déduites ou prédites, ce qui serait interdit selon l’article 5, point c) [1]. Ce type de système relève des systèmes d’IA à haut risque au sens de l’article 6, paragraphe 2, point 4, a) [3], car il est destiné à être utilisé dans le cadre du recrutement ou de la sélection de personnes physiques. Pour cela, vous devez respecter les règles de contrôle humain prévues à l’article 14, notamment en assurant que les personnes chargées de superviser le système peuvent comprendre ses capacités et ses limites, détecter les anomalies, interpréter ses sorties, décider de ne pas utiliser le système ou d’interrompre son fonctionnement, et que les décisions ne soient pas prises sans vérification distincte par au moins deux personnes disposant des compétences et de l’autorité nécessaires [4]. Ces obligations s’appliquent particulièrement aux systèmes d’IA à haut risque, comme le recrutement, et doivent être mises en œuvre pour prévenir les risques pour les droits fondamentaux ou la sécurité [4].
```

</details>

Temps : recherche 3.0 s · génération 95.9 s (5445 tokens lus, 1529 écrits, 30.2 tokens/s) · contrôle de pertinence 7.3 s

## e18 — On a mis un chatbot sur notre site. On doit dire aux visiteurs qu'ils parlent avec une machine ?

Article attendu : AI Act art. 50, paragraphe 1 — passage [1].

### Réponse du copilote

> Oui : vous devez indiquer aux visiteurs qu’ils parlent avec un système d’IA, car votre chatbot est un système d’IA destiné à interagir directement avec des personnes physiques [1]. Cette obligation s’applique, sauf si l’information est clairement visible pour une personne physique normalement informée et raisonnablement attentive, compte tenu des circonstances et du contexte d’utilisation [1]. Si le chatbot ne génère pas d’images, d’audio ou de vidéos, ni de contenus fictifs ou artistiques, l’obligation de transparence s’applique à l’interaction textuelle [2]. Si le chatbot est utilisé pour informer le public sur des questions d’intérêt public, il doit aussi indiquer que le texte a été généré par une IA [2].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »
  [2] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. »
  [2] « Les déployeurs d’un système d’IA qui génère ou manipule des textes publiés dans le but d’informer le public sur des questions d’intérêt public indiquent que le texte a été généré ou manipulé par une IA. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 1 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
  [2] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 4 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50
Passages consultés mais non cités :
  [3] AI Act — règlement (UE) 2024/1689, article 14 : Contrôle humain
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_14
  [4] AI Act — règlement (UE) 2024/1689, article 21 : Coopération avec les autorités compétentes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_21
  [5] AI Act — règlement (UE) 2024/1689, article 6, point c : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
Attention : La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : « Oui: vous devez indiquer aux visiteurs qu’ils parlent avec un système d’IA, car votre chatbot est un système d’IA … » (et 1 autre(s)). Vérifiez qui est concerné.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :  
- [1] « Les fournisseurs veillent à ce que les systèmes d’IA destinés à interagir directement avec des personnes physiques soient conçus et développés de manière que les personnes physiques concernées soient informées qu’elles interagissent avec un système d’IA, sauf si cela ressort clairement du point de vue d’une personne physique normalement informée et raisonnablement attentive et avisée, compte tenu des circonstances et du contexte d’utilisation. »  
- [2] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. »  
- [2] « Les déployeurs d’un système d’IA qui génère ou manipule des textes publiés dans le but d’informer le public sur des questions d’intérêt public indiquent que le texte a été généré ou manipulé par une IA. »  

RÉPONSE :  
Oui : vous devez indiquer aux visiteurs qu’ils parlent avec un système d’IA, car votre chatbot est un système d’IA destiné à interagir directement avec des personnes physiques [1]. Cette obligation s’applique, sauf si l’information est clairement visible pour une personne physique normalement informée et raisonnablement attentive, compte tenu des circonstances et du contexte d’utilisation [1]. Si le chatbot ne génère pas d’images, d’audio ou de vidéos, ni de contenus fictifs ou artistiques, l’obligation de transparence s’applique à l’interaction textuelle [2]. Si le chatbot est utilisé pour informer le public sur des questions d’intérêt public, il doit aussi indiquer que le texte a été généré par une IA [2].
```

</details>

Temps : recherche 7.5 s · génération 33.2 s (3243 tokens lus, 433 écrits, 33.6 tokens/s) · contrôle de pertinence 4.8 s

## e19 — Notre organisme de formation veut utiliser une IA pour corriger les examens et noter les stagiaires. C'est risqué ?

Article attendu : AI Act annexe III, point 3 — passage [1].

### Réponse du copilote

> Oui, l'utilisation d'une IA pour corriger les examens et noter les stagiaires est considérée comme un système d'IA à haut risque, car elle relève des cas d'utilisation visés à l'annexe III du règlement (UE) 2024/1689, notamment dans le domaine de l'éducation et de la formation professionnelle (point b) et c) de l'article 6, paragraphe 2 [1]. Cette utilisation est également incluse dans les cas d'évaluation des acquis d'apprentissage, qui sont explicitement prévus comme des systèmes à haut risque [1]. En outre, le fait que le système d'IA soit destiné à évaluer les performances des stagiaires, notamment dans le cadre d'un examen, constitue une tâche préparatoire à une évaluation pertinente, ce qui active la classification à haut risque selon l’article 6, paragraphe 2, point d) [5]. Ce système est donc soumis à des essais pour déterminer les mesures de gestion des risques les plus appropriées [3], et un système de gestion des risques doit être établi, mis en œuvre, documenté et tenu à jour [4].

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
Oui, l'utilisation d'une IA pour corriger les examens et noter les stagiaires est considérée comme un système d'IA à haut risque, car elle relève des cas d'utilisation visés à l'annexe III du règlement (UE) 2024/1689, notamment dans le domaine de l'éducation et de la formation professionnelle (point b) et c) de l'article 6, paragraphe 2 [1]. Cette utilisation est également incluse dans les cas d'évaluation des acquis d'apprentissage, qui sont explicitement prévus comme des systèmes à haut risque [1]. En outre, le fait que le système d'IA soit destiné à évaluer les performances des stagiaires, notamment dans le cadre d'un examen, constitue une tâche préparatoire à une évaluation pertinente, ce qui active la classification à haut risque selon l’article 6, paragraphe 2, point d) [5]. Ce système est donc soumis à des essais pour déterminer les mesures de gestion des risques les plus appropriées [3], et un système de gestion des risques doit être établi, mis en œuvre, documenté et tenu à jour [4].
```

</details>

Temps : recherche 2.6 s · génération 28.2 s (2246 tokens lus, 612 écrits, 35.9 tokens/s) · contrôle de pertinence 4.8 s

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
Oui : il est obligatoire de prendre des mesures pour favoriser le développement de la maîtrise de l'IA par le personnel et les autres personnes s'occupant du fonctionnement et de l'utilisation des systèmes d'IA, conformément à l'AI Act, article 4, paragraphe 1 [1]. Cette obligation vise à assurer que les salariés acquièrent les connaissances techniques, l'expérience, l'éducation et la formation nécessaires, en tenant compte du contexte d'utilisation et des personnes concernées. Cependant, cette obligation ne contraint pas les fournisseurs ou les déployeurs à garantir un niveau spécifique de maîtrise de l'IA par un individu [1].
```

</details>

Temps : recherche 2.3 s · génération 32.0 s (3481 tokens lus, 354 écrits, 33.3 tokens/s) · contrôle de pertinence 3.9 s

## e21 — On crée nos visuels pour les réseaux sociaux avec une IA. Il faut écrire qu'ils sont générés par IA ?

Article attendu : AI Act art. 50, paragraphe 4 — passage [1].

### Réponse du copilote

> Oui : il faut écrire que les visuels générés par une IA sont générés ou manipulés par une IA, conformément à l’obligation de transparence prévue pour les contenus de synthèse de type image (RGPD, article 50, paragraphe 4), sauf si le contenu fait partie d’une œuvre manifestement artistique, créative, satirique, fictif ou analogue, dans ce cas la transparence se limite à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre [1]. Cette obligation s’applique également aux visuels générés par des systèmes d’IA à usage général, qui doivent être marqués de manière identifiable comme ayant été générés par une IA [3]. Cependant, cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière, ni lorsque le contenu est utilisé dans une fonction d’assistance pour la mise en forme standard ou ne modifie pas de manière substantielle les données d’entrée [3].

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

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. Cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. Lorsque le contenu fait partie d’une œuvre ou d’un programme manifestement artistique, créatif, satirique, fictif ou analogue, les obligations de transparence énoncées au présent paragraphe se limitent à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre. »
- [3] « Les fournisseurs de systèmes d’IA, y compris de systèmes d’IA à usage général, qui génèrent des contenus de synthèse de type audio, image, vidéo ou texte, veillent à ce que les sorties des systèmes d’IA soient marquées dans un format lisible par machine et identifiables comme ayant été générées ou manipulées par une IA. Cette obligation ne s’applique pas dans la mesure où les systèmes d’IA remplissent une fonction d’assistance pour la mise en forme standard ou ne modifient pas de manière substantielle les données d’entrée fournies par le déployeur ou leur sémantique, ou lorsque leur utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière. »

RÉPONSE :
Oui : il faut écrire que les visuels générés par une IA sont générés ou manipulés par une IA, conformément à l’obligation de transparence prévue pour les contenus de synthèse de type image (RGPD, article 50, paragraphe 4), sauf si le contenu fait partie d’une œuvre manifestement artistique, créative, satirique, fictif ou analogue, dans ce cas la transparence se limite à la divulgation de l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de l’œuvre [1]. Cette obligation s’applique également aux visuels générés par des systèmes d’IA à usage général, qui doivent être marqués de manière identifiable comme ayant été générés par une IA [3]. Cependant, cette obligation ne s’applique pas lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la matière, ni lorsque le contenu est utilisé dans une fonction d’assistance pour la mise en forme standard ou ne modifie pas de manière substantielle les données d’entrée [3].
```

</details>

Temps : recherche 2.2 s · génération 34.0 s (2673 tokens lus, 690 écrits, 34.8 tokens/s) · contrôle de pertinence 4.1 s

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

RÉPONSE :
Oui : l’outil analysant les émotions des salariés pendant les visioconférences relève du concept de «système de reconnaissance des émotions» [1]. Cependant, cette utilisation ne relève pas de la prévention ou de la détection d’infractions pénales, donc l’exception prévue dans [2] ne s’applique pas. Ainsi, le déployeur doit informer les personnes physiques exposées du fonctionnement du système et traiter leurs données à caractère personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680 [2]. L’utilisation est autorisée, à condition de respecter ces obligations de transparence et de traitement des données personnelles.
```

</details>

Temps : recherche 2.2 s · génération 23.3 s (2272 tokens lus, 459 écrits, 36.0 tokens/s) · contrôle de pertinence 4.5 s

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
Si l'outil d'IA que vous avez acheté se trompe et écarte injustement un candidat, la responsabilité incombe au fournisseur du système d'IA, car il est considéré comme un fournisseur d’un système d’IA à haut risque lorsqu’il est utilisé pour des décisions affectant des personnes physiques, notamment dans des contextes de recrutement [2]. Le fournisseur est responsable de la conformité du système d’IA, notamment en ce qui concerne la transparence et l’information des utilisateurs [4], et doit fournir les informations, les capacités et l’accès technique nécessaires pour respecter les obligations réglementaires [3]. L’obligation de coopération et d’assistance du fournisseur initial est également établie [1]. Cependant, si le système a été modifié de manière substantielle ou si sa destination a été changée de façon à le rendre un système à haut risque, le déployeur ou le distributeur peut également être considéré comme fournisseur [2]. Aucune obligation de responsabilité n’est énoncée pour l’utilisateur final (vous) dans les textes.
```

</details>

Temps : recherche 2.2 s · génération 38.7 s (2561 tokens lus, 881 écrits, 34.7 tokens/s) · contrôle de pertinence 6.8 s

## e24 — À partir de quand les règles de l'AI Act s'appliquent vraiment ? Qu'est-ce qui est déjà en vigueur ?

Article attendu : AI Act art. 113 — passage [1].

### Réponse du copilote

> Les règles de l'AI Act s'appliquent vraiment à partir du 2 août 2026 [1]. Cependant, certaines parties du règlement sont déjà en vigueur : le chapitre I et le chapitre II s'appliquent à partir du 2 février 2025 [1], le chapitre III, section 4, le chapitre V, le chapitre VII, le chapitre XII et l’article 78 s’appliquent à partir du 2 août 2025 [1], et les articles 102 à 110 s'appliquent à partir du 27 juillet 2026 [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Il est applicable à partir du 2 août 2026. »
  [1] « les chapitres I et II s'appliquent à partir du 2 février 2025, à l'exception de l'article 5, paragraphe 1, premier alinéa, points b bis) et b ter), et de l'article 5, paragraphes 1 bis et 1 ter, qui s'appliquent à partir du 2 décembre 2026; »
  [1] « le chapitre III, section 4, le chapitre V, le chapitre VII, le chapitre XII et l’article 78 s’appliquent à partir du 2 août 2025, à l’exception de l’article 101; »
  [1] « les articles 102 à 110 sont applicables à partir du 27 juillet 2026. »

Sources citées :
  [1] AI Act — règlement (UE) 2024/1689, article 113 : Entrée en vigueur et application (version du 2026-07-27)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_113
Passages consultés mais non cités :
  [2] AI Act — règlement (UE) 2024/1689, article 111 : Systèmes d’IA déjà mis sur le marché ou mis en service et modèles d’IA à usage général déjà mis sur le marché
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_111
  [3] AI Act — règlement (UE) 2024/1689, article 79, paragraphe 8 : Procédure applicable au niveau national aux systèmes d’IA présentant un risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_79
  [4] AI Act — règlement (UE) 2024/1689, article 79, paragraphe 1 : Procédure applicable au niveau national aux systèmes d’IA présentant un risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_79
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

RÉPONSE :
Les règles de l'AI Act s'appliquent vraiment à partir du 2 août 2026 [1]. Cependant, certaines parties du règlement sont déjà en vigueur : le chapitre I et le chapitre II s'appliquent à partir du 2 février 2025 [1], le chapitre III, section 4, le chapitre V, le chapitre VII, le chapitre XII et l’article 78 s’appliquent à partir du 2 août 2025 [1], et les articles 102 à 110 s'appliquent à partir du 27 juillet 2026 [1].
```

</details>

Temps : recherche 2.2 s · génération 33.1 s (3498 tokens lus, 385 écrits, 33.2 tokens/s) · contrôle de pertinence 4.8 s

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
Oui, cela peut être un problème car le copiage de données clients par des salariés dans un outil comme ChatGPT constitue un traitement automatisé de données à caractère personnel, notamment si ces données sont sensibles (ex. : données personnelles, informations commerciales). Cela peut violer le droit de ne pas faire l'objet de décisions fondées exclusivement sur un traitement automatisé, conformément à l'article 22 du RGPD [1]. De plus, le transfert de données à caractère personnel au sein d’un groupe d’entreprises, ou dans un outil externe, doit être encadré par des règles d’entreprise contraignantes qui précisent la nature juridiquement contraignante des règles, les droits des personnes concernées et les mesures de contrôle sur le lieu de travail [1], [3].  

Pour encadrer ce comportement, vous devez mettre en place des règles d’entreprise contraignantes qui :  
- interdisent ou régissent le traitement de données clients par des outils externes comme ChatGPT ;  
- précisent que les données clients ne peuvent être copiées sans autorisation explicite ;  
- garantissent la transparence du traitement et les droits des personnes concernées, notamment le droit de ne pas faire l'objet de décisions fondées sur un traitement automatisé [1], [3] ;  
- incluent des mécanismes de contrôle (ex. : audits, formation) pour vérifier le respect de ces règles [1].  

Si un salarié copie des données clients sans autorisation, cela constitue une violation de données à caractère personnel susceptible d’engendrer un risque élevé pour les droits et libertés des personnes concernées [5]. Dans ce cas, le responsable du traitement doit alors notifie la violation à l’autorité de contrôle compétente dans les meilleurs délais, et, si nécessaire, communiquer la violation à la personne concernée [4], [5].  

Ces obligations s’appliquent à l’ensemble du groupe d’entreprises, y compris les salariés, et doivent être intégrées dans les règles d’entreprise contraignantes [1], [3].
```

</details>

Temps : recherche 2.2 s · génération 53.2 s (3862 tokens lus, 878 écrits, 31.8 tokens/s) · contrôle de pertinence 4.6 s

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

Temps : recherche 2.1 s · génération 13.6 s (2414 tokens lus, 31 écrits, 37.0 tokens/s)

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

Temps : recherche 2.2 s · génération 12.2 s (2370 tokens lus, 26 écrits, 36.8 tokens/s)

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

Temps : recherche 2.2 s · génération 17.5 s (2966 tokens lus, 26 écrits, 35.9 tokens/s)
