# Réponses du copilote — v6b_remote_v2

> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel ou à la CNIL.

Générées le 23/11/2026 à 15:11 par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.

- Génération : `qwen/qwen3.8-27b` via l'API compatible OpenAI https://api.groq.com/openai/v1 (expérience de la séance 7, questions de test seulement ; modèle tel que servi par l'API à la date ci-dessus) — température 0.1, raisonnement : réglage par défaut du modèle, passages calculés pour un contexte de 8192 tokens comme en local, 2000 tokens au plus par réponse (raisonnement compris) ; le juge est le même modèle
- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié
- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, règlement non nommé quand la réponse mêle RGPD et AI Act
- Recherche : `bge-m3` (sur CPU), mode « vector », lexique « all », 5 passages par question, 2 au plus par article, 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu, reranker `BAAI/bge-reranker-v2-m3` sur CPU (20 candidats reclassés avant la limite par article), reformulation de la question par le modèle avant la recherche (termes juridiques ajoutés, sans conclusion)
- Contrôle de pertinence (juge) : activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par « Les passages trouvés ne traitent pas directement de votre question. »
- Corpus : versions consolidées RGPD du 2016-05-04, AI Act du 2026-07-27
- Questions : `eval/questions_v2.jsonl` (9 + 2 hors sujet)
- Sélection : seules les questions choisies avec --ids ont été posées (les autres ne figurent pas dans ce fichier)
- Reprise : 4 réponse(s) conservée(s) d'une série précédente arrêtée en cours de route (par exemple par le quota de l'API), 7 générée(s) à la date ci-dessus

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q30 | Pouvons-nous refuser automatiquement une demande d'inscription à notre service à partir d'un score calculé par un logiciel, sans qu'une personne ne vérifie ? | 4/6 | non | 2 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1], [1]) : ignoré(s).; La réponse met entre « » un texte introuvable dans les extraits vérifiés : « autorisée par le droit de l'Union ou le droit de l'État membre auquel le responsable du traitement est soumis et qui … » (et 1 autre(s)). | 42 s |
| q33 | Nous avons acheté un fichier de prospects à une autre entreprise : devons-nous informer ces personnes, et dans quel délai ? | 6/6 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 31 s |
| q34 | Puis-je installer des caméras dans l'atelier pour surveiller le travail de mes salariés ? | 6/6 | non | La réponse met entre « » un texte introuvable dans les extraits vérifiés : « les systèmes de contrôle sur le lieu de travail ». | 32 s |
| q36 | Un ancien bénévole menace de se plaindre de nous auprès de la CNIL : en a-t-il le droit, et quels autres recours a-t-il ? | 6/6 | non | — | 43 s |
| q38 | Notre club de sport peut-il demander un extrait de casier judiciaire aux bénévoles qui encadrent des enfants ? | 2/2 | non | — | 60 s |
| q39 | Si nous remplaçons les noms de nos adhérents par des numéros, les données sont-elles encore des données personnelles ? | 2/2 | non | — | 30 s |
| q42 | Un candidat refusé après l'analyse de sa candidature par un outil d'IA à haut risque nous demande pourquoi : devons-nous lui expliquer ? | 3/3 | non | — | 30 s |
| q43 | Le règlement européen sur l'IA prévoit-il des mesures particulières pour les PME ? | 6/6 | non | La réponse met entre « » un texte introuvable dans les extraits vérifiés : « organiser des activités spécifiques de sensibilisation et de formation à l'application du présent règlement, adaptées … » (et 1 autre(s)). | 36 s |
| q44 | À partir de quelle date devrons-nous respecter les obligations sur les systèmes d'IA à haut risque utilisés pour le recrutement ? | 2/2 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question. | 25 s |
| h06 | Quelles mentions obligatoires doivent figurer sur une facture ? | 0/0 | oui | — | 27 s |
| h08 | Quelles sont les règles pour embaucher un apprenti dans une PME ? | 0/0 | oui | — | 25 s |

## q30 — Pouvons-nous refuser automatiquement une demande d'inscription à notre service à partir d'un score calculé par un logiciel, sans qu'une personne ne vérifie ?

Article attendu : RGPD art. 22 — passage [1].

### Réponse du copilote

> En principe, vous ne pouvez pas refuser automatiquement une demande d'inscription si ce refus produit des effets juridiques ou affecte significativement la personne, car elle a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé [1]. Ce refus est considéré comme du profilage s'il consiste à utiliser des données pour évaluer des aspects personnels de la personne [2].
>
> Toutefois, cette interdiction ne s'applique pas si la décision est « nécessaire à la conclusion ou à l'exécution d'un contrat entre la personne concernée et un responsable du traitement » [1], si elle est « autorisée par le droit de l'Union ou le droit de l'État membre auquel le responsable du traitement est soumis et qui prévoit également des mesures appropriées pour la sauvegarde des droits et libertés et des intérêts légitimes de la personne concernée » [1], ou si elle est « fondée sur le consentement explicite de la personne concernée » [1].
>
> Si vous vous appuyez sur l'une de ces exceptions (notamment le contrat ou le consentement), vous devez impérativement mettre en œuvre des mesures appropriées, incluant « au moins du droit de la personne concernée d'obtenir une intervention humaine de la part du responsable du traitement, d'exprimer son point de vue et de contester la décision » [1].

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
  [5] RGPD — règlement (UE) 2016/679, article 21 : Droit d'opposition
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_21
Attention : 2 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1], [1]) : ignoré(s).
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « autorisée par le droit de l'Union ou le droit de l'État membre auquel le responsable du traitement est soumis et qui … » (et 1 autre(s)).

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
- [2] « «profilage», toute forme de traitement automatisé de données à caractère personnel consistant à utiliser ces données à caractère personnel pour évaluer certains aspects personnels relatifs à une personne physique, notamment pour analyser ou prédire des éléments concernant le rendement au travail, la situation économique, la santé, les préférences personnelles, les intérêts, la fiabilité, le comportement, la localisation ou les déplacements de cette personne physique; »

RÉPONSE :
En principe, vous ne pouvez pas refuser automatiquement une demande d'inscription si ce refus produit des effets juridiques ou affecte significativement la personne, car elle a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé [1]. Ce refus est considéré comme du profilage s'il consiste à utiliser des données pour évaluer des aspects personnels de la personne [2].

Toutefois, cette interdiction ne s'applique pas si la décision est « nécessaire à la conclusion ou à l'exécution d'un contrat entre la personne concernée et un responsable du traitement » [1], si elle est « autorisée par le droit de l'Union ou le droit de l'État membre auquel le responsable du traitement est soumis et qui prévoit également des mesures appropriées pour la sauvegarde des droits et libertés et des intérêts légitimes de la personne concernée » [1], ou si elle est « fondée sur le consentement explicite de la personne concernée » [1].

Si vous vous appuyez sur l'une de ces exceptions (notamment le contrat ou le consentement), vous devez impérativement mettre en œuvre des mesures appropriées, incluant « au moins du droit de la personne concernée d'obtenir une intervention humaine de la part du responsable du traitement, d'exprimer son point de vue et de contester la décision » [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : décision automatisée ; profilage ; décision fondée exclusivement sur un traitement automatisé ; droit d'obtenir une intervention humaine

Temps : recherche 39.6 s · génération 2.0 s (2555 tokens lus, 706 écrits, 439.4 tokens/s) · contrôle de pertinence 0.1 s · reformulation 0.3 s · attente des limites de l'API 21 s (non comptée)

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
  [3] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
  [4] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [5] RGPD — règlement (UE) 2016/679, article 29 : Traitement effectué sous l'autorité du responsable du traitement ou du sous-traitant
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_29
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [4] « Lorsque des données à caractère personnel relatives à une personne concernée sont collectées auprès de cette personne, le responsable du traitement lui fournit, au moment où les données en question sont obtenues, toutes les informations suivantes: »
- [4] « les finalités du traitement auquel sont destinées les données à caractère personnel ainsi que la base juridique du traitement; »
- [4] « les destinataires ou les catégories de destinataires des données à caractère personnel, s'ils existent; et »
- [4] « le cas échéant, le fait que le responsable du traitement a l'intention d'effectuer un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale, et l'existence ou l'absence d'une décision d'adéquation rendue par la Commission ou, dans le cas des transferts visés à l'article 46 ou 47, ou à l'article 49, paragraphe 1, deuxième alinéa, la référence aux garanties appropriées ou adaptées et les moyens d'en obtenir une copie ou l'endroit où elles ont été mises à disposition; »
- [4] « la durée de conservation des données à caractère personnel ou, lorsque ce n'est pas possible, les critères utilisés pour déterminer cette durée; »
- [4] « l'existence du droit de demander au responsable du traitement l'accès aux données à caractère personnel, la rectification ou l'effacement de celles-ci, ou une limitation du traitement relatif à la personne concernée, ou du droit de s'opposer au traitement et du droit à la portabilité des données; »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question, car l'article 13 du RGPD, qui est le seul texte fourni concernant l'information des personnes, s'applique spécifiquement « lorsque des données à caractère personnel relatives à une personne concernée sont collectées auprès de cette personne » [4]. Dans votre cas, les données proviennent d'une autre entreprise et non directement des prospects, ce qui signifie que les extraits fournis ne précisent pas si vous devez les informer ni quel délai s'applique à cette situation spécifique. Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données à caractère personnel ; responsable du traitement ; sous-traitant ; information des personnes concernées ; consentement

Temps : recherche 29.4 s · génération 1.4 s (3579 tokens lus, 478 écrits, 521.7 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.2 s

## q34 — Puis-je installer des caméras dans l'atelier pour surveiller le travail de mes salariés ?

Article attendu : RGPD art. 88 — passage [1].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question, car ils ne mentionnent pas explicitement l'installation de caméras, mais ils posent les principes généraux applicables au traitement des données des salariés. En tant qu'employeur, vous devez respecter les règles spécifiques prévues par les États membres, qui peuvent inclure des dispositions sur « les systèmes de contrôle sur le lieu de travail » [1]. Le traitement des images doit être « licite, loyale et transparente au regard de la personne concernée » [4]. Vous devez également garantir que les données sont « adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités pour lesquelles elles sont traitées » [4]. Enfin, les données doivent être « conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées » [4] et traitées de façon à garantir une « sécurité appropriée des données à caractère personnel » [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Les États membres peuvent prévoir, par la loi ou au moyen de conventions collectives, des règles plus spécifiques pour assurer la protection des droits et libertés en ce qui concerne le traitement des données à caractère personnel des employés dans le cadre des relations de travail, aux fins, notamment, du recrutement, de l'exécution du contrat de travail, y compris le respect des obligations fixées par la loi ou par des conventions collectives, de la gestion, de la planification et de l'organisation du travail, de l'égalité et de la diversité sur le lieu de travail, de la santé et de la sécurité au travail, de la protection des biens appartenant à l'employeur ou au client, aux fins de l'exercice et de la jouissance des droits et des avantages liés à l'emploi, individuellement ou collectivement, ainsi qu'aux fins de la résiliation de la relation de travail. »
  [1] « Ces règles comprennent des mesures appropriées et spécifiques pour protéger la dignité humaine, les intérêts légitimes et les droits fondamentaux des personnes concernées, en accordant une attention particulière à la transparence du traitement, au transfert de données à caractère personnel au sein d'un groupe d'entreprises, ou d'un groupe d'entreprises engagées dans une activité économique conjointe et aux systèmes de contrôle sur le lieu de travail. »
  [4] « Les données à caractère personnel doivent être: a) traitées de manière licite, loyale et transparente au regard de la personne concernée (licéité, loyauté, transparence); »
  [4] « c) adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités pour lesquelles elles sont traitées (minimisation des données); »
  [4] « e) conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées; »
  [4] « f) traitées de façon à garantir une sécurité appropriée des données à caractère personnel, y compris la protection contre le traitement non autorisé ou illicite et contre la perte, la destruction ou les dégâts d'origine accidentelle, à l'aide de mesures techniques ou organisationnelles appropriées (intégrité et confidentialité); »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 88 : Traitement de données dans le cadre des relations de travail (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_88
  [4] RGPD — règlement (UE) 2016/679, article 5 : Principes relatifs au traitement des données à caractère personnel (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_5
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 47, paragraphe 2, points a) à k) : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
  [3] RGPD — règlement (UE) 2016/679, article 47, paragraphe 1 : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
  [5] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « les systèmes de contrôle sur le lieu de travail ».

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Les États membres peuvent prévoir, par la loi ou au moyen de conventions collectives, des règles plus spécifiques pour assurer la protection des droits et libertés en ce qui concerne le traitement des données à caractère personnel des employés dans le cadre des relations de travail, aux fins, notamment, du recrutement, de l'exécution du contrat de travail, y compris le respect des obligations fixées par la loi ou par des conventions collectives, de la gestion, de la planification et de l'organisation du travail, de l'égalité et de la diversité sur le lieu de travail, de la santé et de la sécurité au travail, de la protection des biens appartenant à l'employeur ou au client, aux fins de l'exercice et de la jouissance des droits et des avantages liés à l'emploi, individuellement ou collectivement, ainsi qu'aux fins de la résiliation de la relation de travail. »
- [1] « Ces règles comprennent des mesures appropriées et spécifiques pour protéger la dignité humaine, les intérêts légitimes et les droits fondamentaux des personnes concernées, en accordant une attention particulière à la transparence du traitement, au transfert de données à caractère personnel au sein d'un groupe d'entreprises, ou d'un groupe d'entreprises engagées dans une activité économique conjointe et aux systèmes de contrôle sur le lieu de travail. »
- [4] « Les données à caractère personnel doivent être: a) traitées de manière licite, loyale et transparente au regard de la personne concernée (licéité, loyauté, transparence); »
- [4] « c) adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités pour lesquelles elles sont traitées (minimisation des données); »
- [4] « e) conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées; »
- [4] « f) traitées de façon à garantir une sécurité appropriée des données à caractère personnel, y compris la protection contre le traitement non autorisé ou illicite et contre la perte, la destruction ou les dégâts d'origine accidentelle, à l'aide de mesures techniques ou organisationnelles appropriées (intégrité et confidentialité); »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question, car ils ne mentionnent pas explicitement l'installation de caméras, mais ils posent les principes généraux applicables au traitement des données des salariés. En tant qu'employeur, vous devez respecter les règles spécifiques prévues par les États membres, qui peuvent inclure des dispositions sur « les systèmes de contrôle sur le lieu de travail » [1]. Le traitement des images doit être « licite, loyale et transparente au regard de la personne concernée » [4]. Vous devez également garantir que les données sont « adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités pour lesquelles elles sont traitées » [4]. Enfin, les données doivent être « conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées » [4] et traitées de façon à garantir une « sécurité appropriée des données à caractère personnel » [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : vidéosurveillance ; traitement de données à caractère personnel ; surveillance des salariés ; consentement ; information des personnes concernées ; protection des données

Temps : recherche 29.3 s · génération 2.3 s (3450 tokens lus, 718 écrits, 466.6 tokens/s) · contrôle de pertinence 0.1 s · reformulation 0.2 s · attente des limites de l'API 48 s (non comptée)

## q36 — Un ancien bénévole menace de se plaindre de nous auprès de la CNIL : en a-t-il le droit, et quels autres recours a-t-il ?

Article attendu : RGPD art. 77 — passage [1].

### Réponse du copilote

> Oui, l'ancien bénévole a le droit de se plaindre auprès de la CNIL, car « toute personne concernée a le droit d'introduire une réclamation auprès d'une autorité de contrôle » si elle estime que le traitement de ses données viole le règlement [1]. Ce droit s'exerce « en particulier dans l'État membre dans lequel se trouve sa résidence habituelle, son lieu de travail ou le lieu où la violation aurait été commise » [1].
>
> En plus de la réclamation auprès de la CNIL, il dispose d'autres recours :
> 1.  Il peut « mandater un organisme, une organisation ou une association à but non lucratif » pour qu'elle introduise la réclamation en son nom ou exerce d'autres droits [2].
> 2.  Il a « droit à un recours juridictionnel effectif » s'il considère que ses droits ont été violés par le traitement [3].
> 3.  Il peut exercer ses droits directement auprès de vous, en tant que responsable du traitement, notamment le « droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées » et l'accès à ces données [4].
> 4.  Il peut également demander la « rectification ou l'effacement de données à caractère personnel, ou une limitation du traitement des données à caractère personnel relatives à la personne concernée, ou du droit de s'opposer à ce traitement » [4].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « toute personne concernée a le droit d'introduire une réclamation auprès d'une autorité de contrôle, en particulier dans l'État membre dans lequel se trouve sa résidence habituelle, son lieu de travail ou le lieu où la violation aurait été commise, si elle considère que le traitement de données à caractère personnel la concernant constitue une violation du présent règlement. »
  [2] « La personne concernée a le droit de mandater un organisme, une organisation ou une association à but non lucratif, qui a été valablement constitué conformément au droit d'un État membre, dont les objectifs statutaires sont d'intérêt public et est actif dans le domaine de la protection des droits et libertés des personnes concernées dans le cadre de la protection des données à caractère personnel les concernant, pour qu'il introduise une réclamation en son nom, exerce en son nom les droits visés aux articles 77, 78 et 79 et exerce en son nom le droit d'obtenir réparation visé à l'article 82 lorsque le droit d'un État membre le prévoit. »
  [3] « chaque personne concernée a droit à un recours juridictionnel effectif si elle considère que les droits que lui confère le présent règlement ont été violés du fait d'un traitement de ses données à caractère personnel effectué en violation du présent règlement. »
  [4] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: »
  [4] « e) l'existence du droit de demander au responsable du traitement la rectification ou l'effacement de données à caractère personnel, ou une limitation du traitement des données à caractère personnel relatives à la personne concernée, ou du droit de s'opposer à ce traitement; »
  [4] « f) le droit d'introduire une réclamation auprès d'une autorité de contrôle; »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 77 : Droit d'introduire une réclamation auprès d'une autorité de contrôle (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_77
  [2] RGPD — règlement (UE) 2016/679, article 80 : Représentation des personnes concernées (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_80
  [3] RGPD — règlement (UE) 2016/679, article 79 : Droit à un recours juridictionnel effectif contre un responsable du traitement ou un sous-traitant (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_79
  [4] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15
Passages consultés mais non cités :
  [5] RGPD — règlement (UE) 2016/679, article 78 : Droit à un recours juridictionnel effectif contre une autorité de contrôle
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_78

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « toute personne concernée a le droit d'introduire une réclamation auprès d'une autorité de contrôle, en particulier dans l'État membre dans lequel se trouve sa résidence habituelle, son lieu de travail ou le lieu où la violation aurait été commise, si elle considère que le traitement de données à caractère personnel la concernant constitue une violation du présent règlement. »
- [2] « La personne concernée a le droit de mandater un organisme, une organisation ou une association à but non lucratif, qui a été valablement constitué conformément au droit d'un État membre, dont les objectifs statutaires sont d'intérêt public et est actif dans le domaine de la protection des droits et libertés des personnes concernées dans le cadre de la protection des données à caractère personnel les concernant, pour qu'il introduise une réclamation en son nom, exerce en son nom les droits visés aux articles 77, 78 et 79 et exerce en son nom le droit d'obtenir réparation visé à l'article 82 lorsque le droit d'un État membre le prévoit. »
- [3] « chaque personne concernée a droit à un recours juridictionnel effectif si elle considère que les droits que lui confère le présent règlement ont été violés du fait d'un traitement de ses données à caractère personnel effectué en violation du présent règlement. »
- [4] « La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées et, lorsqu'elles le sont, l'accès auxdites données à caractère personnel ainsi que les informations suivantes: »
- [4] « e) l'existence du droit de demander au responsable du traitement la rectification ou l'effacement de données à caractère personnel, ou une limitation du traitement des données à caractère personnel relatives à la personne concernée, ou du droit de s'opposer à ce traitement; »
- [4] « f) le droit d'introduire une réclamation auprès d'une autorité de contrôle; »

RÉPONSE :
Oui, l'ancien bénévole a le droit de se plaindre auprès de la CNIL, car « toute personne concernée a le droit d'introduire une réclamation auprès d'une autorité de contrôle » si elle estime que le traitement de ses données viole le règlement [1]. Ce droit s'exerce « en particulier dans l'État membre dans lequel se trouve sa résidence habituelle, son lieu de travail ou le lieu où la violation aurait été commise » [1].

En plus de la réclamation auprès de la CNIL, il dispose d'autres recours :
1.  Il peut « mandater un organisme, une organisation ou une association à but non lucratif » pour qu'elle introduise la réclamation en son nom ou exerce d'autres droits [2].
2.  Il a « droit à un recours juridictionnel effectif » s'il considère que ses droits ont été violés par le traitement [3].
3.  Il peut exercer ses droits directement auprès de vous, en tant que responsable du traitement, notamment le « droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées » et l'accès à ces données [4].
4.  Il peut également demander la « rectification ou l'effacement de données à caractère personnel, ou une limitation du traitement des données à caractère personnel relatives à la personne concernée, ou du droit de s'opposer à ce traitement » [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit d'introduction d'une réclamation ; autorité de contrôle ; droit de recours juridictionnel ; droit d'obtenir réparation ; droit d'accès aux données ; droit à l'effacement

Temps : recherche 39.3 s · génération 2.5 s (2799 tokens lus, 762 écrits, 449.5 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.8 s · attente des limites de l'API 452 s (non comptée)

## q38 — Notre club de sport peut-il demander un extrait de casier judiciaire aux bénévoles qui encadrent des enfants ?

Article attendu : RGPD art. 10 — passage [1].

### Réponse du copilote

> Votre club de sport ne peut traiter ces données que si le traitement est « autorisé par le droit de l’Union ou par le droit d’un État membre qui prévoit des garanties appropriées pour les droits et libertés des personnes concernées » [1]. En l'absence de cette autorisation légale spécifique, le traitement de données relatives aux condamnations pénales n'est permis que « sous le contrôle de l’autorité publique » [1]. Les passages trouvés ne précisent pas si une telle autorisation existe spécifiquement pour les clubs de sport encadrant des enfants, mais ils imposent cette condition stricte pour la licéité du traitement [1].

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Le traitement des données à caractère personnel relatives aux condamnations pénales et aux infractions ou aux mesures de sûreté connexes fondé sur l’article 6, paragraphe 1, ne peut être effectué que sous le contrôle de l’autorité publique, ou si le traitement est autorisé par le droit de l’Union ou par le droit d’un État membre qui prévoit des garanties appropriées pour les droits et libertés des personnes concernées. »
  [1] « Tout registre complet des condamnations pénales ne peut être tenu que sous le contrôle de l’autorité publique. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 10 : Traitement des données à caractère personnel relatives aux condamnations pénales et aux infractions (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_10
Passages consultés mais non cités :
  [2] RGPD — règlement (UE) 2016/679, article 6, paragraphe 1 : Licéité du traitement
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_6
  [3] RGPD — règlement (UE) 2016/679, article 40, paragraphe 2 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [4] RGPD — règlement (UE) 2016/679, article 40, paragraphe 1 : Codes de conduite
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_40
  [5] RGPD — règlement (UE) 2016/679, article 14, paragraphe 2 : Informations à fournir lorsque les données à caractère personnel n'ont pas été collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_14

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Le traitement des données à caractère personnel relatives aux condamnations pénales et aux infractions ou aux mesures de sûreté connexes fondé sur l’article 6, paragraphe 1, ne peut être effectué que sous le contrôle de l’autorité publique, ou si le traitement est autorisé par le droit de l’Union ou par le droit d’un État membre qui prévoit des garanties appropriées pour les droits et libertés des personnes concernées. »
- [1] « Tout registre complet des condamnations pénales ne peut être tenu que sous le contrôle de l’autorité publique. »

RÉPONSE :
Votre club de sport ne peut traiter ces données que si le traitement est « autorisé par le droit de l’Union ou par le droit d’un État membre qui prévoit des garanties appropriées pour les droits et libertés des personnes concernées » [1]. En l'absence de cette autorisation légale spécifique, le traitement de données relatives aux condamnations pénales n'est permis que « sous le contrôle de l’autorité publique » [1]. Les passages trouvés ne précisent pas si une telle autorisation existe spécifiquement pour les clubs de sport encadrant des enfants, mais ils imposent cette condition stricte pour la licéité du traitement [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : traitement de données à caractère personnel ; données relatives à des condamnations pénales ; consentement ; intérêt légitime ; responsable du traitement

Temps : recherche 57.9 s · génération 1.0 s (2534 tokens lus, 283 écrits, 488.3 tokens/s) · contrôle de pertinence 0.4 s · reformulation 0.8 s

## q39 — Si nous remplaçons les noms de nos adhérents par des numéros, les données sont-elles encore des données personnelles ?

Article attendu : RGPD art. 4, définition 5 — passage [2].

### Réponse du copilote

> Oui, les données restent des données à caractère personnel car une personne physique est réputée identifiable si elle peut l'être « directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification » [1]. Le remplacement des noms par des numéros constitue une pseudonymisation, qui est définie comme un traitement permettant d'empêcher l'attribution directe des données à une personne « sans avoir recours à des informations supplémentaires » [2]. Pour que ces données ne soient plus considérées comme personnelles, il faudrait que les informations supplémentaires (la clé de correspondance entre le numéro et le nom) soient « conservées séparément et soumises à des mesures techniques et organisationnelles afin de garantir que les données à caractère personnel ne sont pas attribuées à une personne physique identifiée ou identifiable » [2].

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
  [4] RGPD — règlement (UE) 2016/679, article 13 : Informations à fournir lorsque des données à caractère personnel sont collectées auprès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_13
  [5] RGPD — règlement (UE) 2016/679, article 15 : Droit d'accès de la personne concernée
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_15

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « est réputée être une «personne physique identifiable» une personne physique qui peut être identifiée, directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification, des données de localisation, un identifiant en ligne, ou à un ou plusieurs éléments spécifiques propres à son identité physique, physiologique, génétique, psychique, économique, culturelle ou sociale; »
- [2] « le traitement de données à caractère personnel de telle façon que celles-ci ne puissent plus être attribuées à une personne concernée précise sans avoir recours à des informations supplémentaires, pour autant que ces informations supplémentaires soient conservées séparément et soumises à des mesures techniques et organisationnelles afin de garantir que les données à caractère personnel ne sont pas attribuées à une personne physique identifiée ou identifiable; »

RÉPONSE :
Oui, les données restent des données à caractère personnel car une personne physique est réputée identifiable si elle peut l'être « directement ou indirectement, notamment par référence à un identifiant, tel qu'un nom, un numéro d'identification » [1]. Le remplacement des noms par des numéros constitue une pseudonymisation, qui est définie comme un traitement permettant d'empêcher l'attribution directe des données à une personne « sans avoir recours à des informations supplémentaires » [2]. Pour que ces données ne soient plus considérées comme personnelles, il faudrait que les informations supplémentaires (la clé de correspondance entre le numéro et le nom) soient « conservées séparément et soumises à des mesures techniques et organisationnelles afin de garantir que les données à caractère personnel ne sont pas attribuées à une personne physique identifiée ou identifiable » [2].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : données à caractère personnel ; pseudonymisation ; données pseudonymisées ; personne concernée

Temps : recherche 28.3 s · génération 1.4 s (3248 tokens lus, 364 écrits, 459.2 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.2 s

## q42 — Un candidat refusé après l'analyse de sa candidature par un outil d'IA à haut risque nous demande pourquoi : devons-nous lui expliquer ?

Article attendu : AI Act art. 86 — passage [1].

### Réponse du copilote

> Oui, vous devez lui fournir des explications, car l'analyse de candidatures par un système d'IA relève des systèmes à haut risque listés dans l'annexe III [2]. En tant que déployeur, vous avez l'obligation de fournir à la personne concernée « des explications claires et pertinentes sur le rôle du système d’IA dans la procédure décisionnelle et sur les principaux éléments de la décision prise » [1]. Cette obligation s'applique sauf si des exceptions ou des restrictions découlent du droit de l'Union ou du droit national [1].

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
  [5] AI Act — règlement (UE) 2024/1689, article 9, paragraphe 6 : Système de gestion des risques
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
Oui, vous devez lui fournir des explications, car l'analyse de candidatures par un système d'IA relève des systèmes à haut risque listés dans l'annexe III [2]. En tant que déployeur, vous avez l'obligation de fournir à la personne concernée « des explications claires et pertinentes sur le rôle du système d’IA dans la procédure décisionnelle et sur les principaux éléments de la décision prise » [1]. Cette obligation s'applique sauf si des exceptions ou des restrictions découlent du droit de l'Union ou du droit national [1].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : droit à une explication ; décision automatisée ; profilage ; système d'IA à haut risque ; transparence ; mesures appropriées

Temps : recherche 26.3 s · génération 3.2 s (2183 tokens lus, 397 écrits, 250.5 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.4 s

## q43 — Le règlement européen sur l'IA prévoit-il des mesures particulières pour les PME ?

Article attendu : AI Act art. 62 — passage [1].

### Réponse du copilote

> Oui, le règlement européen sur l'IA (AI Act) prévoit plusieurs mesures particulières pour les PME et les jeunes pousses. Les États membres doivent leur accorder « un accès prioritaire aux bacs à sable réglementaires de l’IA, dans la mesure où elles remplissent les conditions d’éligibilité et les critères de sélection » [1]. Ils doivent également « organiser des activités spécifiques de sensibilisation et de formation à l'application du présent règlement, adaptées aux besoins des PME, y compris les jeunes pousses, les déployeurs et, si nécessaire, les pouvoirs publics locaux » [1]. De plus, les États membres « utilisent des canaux privilégiés existants et, s’il y a lieu, en établissent de nouveaux avec les PME, y compris les jeunes pousses, les déployeurs, d’autres innovateurs et, si nécessaire, les pouvoirs publics locaux, afin de fournir des conseils et de répondre aux questions relatives à la mise en œuvre du présent règlement, y compris en ce qui concerne la participation à des bacs à sable réglementaires de l’IA » [1]. Ils doivent aussi « faciliter la participation des PME et d’autres parties concernées au processus d’élaboration de la normalisation » [1]. Concernant les coûts, « les intérêts et les besoins spécifiques des PME fournisseuses, y compris les jeunes pousses, sont pris en considération lors de la fixation des frais liés à l’évaluation de la conformité visée à l’article 43, ces frais étant réduits proportionnellement à leur taille, à la taille de leur marché et à d’autres indicateurs pertinents » [1]. Enfin, en matière de conformité technique, « les PME, y compris les jeunes pousses, peuvent se conformer de manière simplifiée à certains éléments du système de gestion de la qualité requis par l'article 17, pour autant qu'elles n'aient pas d'entreprises partenaires ou d'entreprises liées au sens de la recommandation 2003/361/CE » [4].

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
Oui, le règlement européen sur l'IA (AI Act) prévoit plusieurs mesures particulières pour les PME et les jeunes pousses. Les États membres doivent leur accorder « un accès prioritaire aux bacs à sable réglementaires de l’IA, dans la mesure où elles remplissent les conditions d’éligibilité et les critères de sélection » [1]. Ils doivent également « organiser des activités spécifiques de sensibilisation et de formation à l'application du présent règlement, adaptées aux besoins des PME, y compris les jeunes pousses, les déployeurs et, si nécessaire, les pouvoirs publics locaux » [1]. De plus, les États membres « utilisent des canaux privilégiés existants et, s’il y a lieu, en établissent de nouveaux avec les PME, y compris les jeunes pousses, les déployeurs, d’autres innovateurs et, si nécessaire, les pouvoirs publics locaux, afin de fournir des conseils et de répondre aux questions relatives à la mise en œuvre du présent règlement, y compris en ce qui concerne la participation à des bacs à sable réglementaires de l’IA » [1]. Ils doivent aussi « faciliter la participation des PME et d’autres parties concernées au processus d’élaboration de la normalisation » [1]. Concernant les coûts, « les intérêts et les besoins spécifiques des PME fournisseuses, y compris les jeunes pousses, sont pris en considération lors de la fixation des frais liés à l’évaluation de la conformité visée à l’article 43, ces frais étant réduits proportionnellement à leur taille, à la taille de leur marché et à d’autres indicateurs pertinents » [1]. Enfin, en matière de conformité technique, « les PME, y compris les jeunes pousses, peuvent se conformer de manière simplifiée à certains éléments du système de gestion de la qualité requis par l'article 17, pour autant qu'elles n'aient pas d'entreprises partenaires ou d'entreprises liées au sens de la recommandation 2003/361/CE » [4].
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : petites et moyennes entreprises ; micro-entreprises ; mesures d'accompagnement ; soutien à l'innovation ; obligations proportionnées

Temps : recherche 32.5 s · génération 2.2 s (2699 tokens lus, 858 écrits, 455.0 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.9 s

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
  [3] AI Act — règlement (UE) 2024/1689, annexe III, point 4 : Systèmes d'IA à haut risque visés à l'article 6, paragraphe 2
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_III
  [4] AI Act — règlement (UE) 2024/1689, article 6, paragraphe 5 : Règles relatives à la classification de systèmes d’IA comme systèmes à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_6
  [5] AI Act — règlement (UE) 2024/1689, article 26, paragraphe 11 : Obligations incombant aux déployeurs de systèmes d’IA à haut risque
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_26
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question. La réponse du modèle n'est pas affichée ; consultez les passages ci-dessous ou reformulez la question.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS :
- [1] « Au plus tard le 2 août 2027, la Commission adopte des actes délégués conformément à l'article 97 afin de compléter le présent règlement afin de préciser les systèmes d'IA à haut risque concernés, les exigences ou obligations qui peuvent être limitées, les conditions dans lesquelles cette limitation s'applique et la portée de la limitation. »
- [4] « Après consultation du Comité européen de l’intelligence artificielle (ci-après dénommé «Comité IA»), et au plus tard le 2 février 2026, la Commission fournit des lignes directrices précisant la mise en œuvre pratique du présent article, conformément à l’article 96, assorties d’une liste exhaustive d’exemples pratiques de cas d’utilisation de systèmes d’IA qui sont à haut risque et de cas d’utilisation qui ne le sont pas. »

RÉPONSE :
Les passages trouvés ne traitent pas directement de votre question. Ils mentionnent des dates limites pour l'adoption d'actes délégués précisant les conditions de limitation des obligations [1] et pour la fourniture de lignes directrices par la Commission [4], mais ils n'indiquent pas la date d'entrée en vigueur des obligations applicables aux systèmes d'IA à haut risque utilisés pour le recrutement.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : systèmes d'IA à haut risque ; recrutement ; obligations ; date d'application

Temps : recherche 23.6 s · génération 1.4 s (2241 tokens lus, 293 écrits, 454.2 tokens/s) · contrôle de pertinence 0.2 s · reformulation 0.3 s

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
  [2] AI Act — règlement (UE) 2024/1689, annexe V : Déclaration UE de conformité
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_V
  [3] AI Act — règlement (UE) 2024/1689, annexe VII, point 4 a : Conformité fondée sur une évaluation du système de gestion de la qualité et une évaluation de la documentation technique
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#anx_VII
  [4] RGPD — règlement (UE) 2016/679, article 4, définition 1 : Définitions
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_4
  [5] AI Act — règlement (UE) 2024/1689, article 50, paragraphe 5 : Obligations de transparence pour les fournisseurs et les déployeurs de certains systèmes d’IA
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02024R1689-20260727#art_50

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : identité du fournisseur ; identité du client ; numéro de la facture ; date de la facture ; description des biens ou services ; prix unitaire

Temps : recherche 25.8 s · génération 0.5 s (2072 tokens lus, 25 écrits, 467.6 tokens/s) · reformulation 0.2 s · attente des limites de l'API 9 s (non comptée)

## h08 — Quelles sont les règles pour embaucher un apprenti dans une PME ?

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
  [2] RGPD — règlement (UE) 2016/679, article 47, paragraphe 2, points a) à k) : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
  [3] RGPD — règlement (UE) 2016/679, article 47, paragraphe 1 : Règles d'entreprise contraignantes
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_47
  [4] RGPD — règlement (UE) 2016/679, article 28, paragraphe 3 : Sous-traitant
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28
  [5] RGPD — règlement (UE) 2016/679, article 28, paragraphe 1 : Sous-traitant
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_28

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
EXTRAITS : aucun
RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question.
```

</details>

Reformulation de la question (termes ajoutés avant la recherche) : contrat d'apprentissage ; personne en formation ; durée du contrat ; rémunération de l'apprenti

Temps : recherche 23.5 s · génération 0.8 s (3129 tokens lus, 25 écrits, 401.1 tokens/s) · reformulation 0.3 s
