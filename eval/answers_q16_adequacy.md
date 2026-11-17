# q16 — règle « décisions d'adéquation » et note fixe (séance 7 bis, branche fix/adequacy)

- Date : 17/11/2026 ; secteur : oui (BatteryStatus = 2).
- Question : Puis-je stocker les fichiers de mon association chez un hébergeur situé aux États-Unis ?
- Articles attendus : gdpr:art_44, gdpr:art_45:par_1, gdpr:art_46.
- Configuration v4 (lexique, 5 passages, 2 par article, 1er paragraphe, juge, reranker désactivé) + règle 12 du prompt + note fixe du code.
- Local : `qwen3:4b-instruct` (Ollama) ; distant : `qwen/qwen3.8-27b` (Groq, `reasoning_effort=none`). Réponses sans retouche, telles qu'affichées.

## Local, essai 1

### Réponse du copilote

> Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, à condition que l’un des mécanismes prévus par le RGPD soit respecté. Si les États-Unis ont été reconnus comme assurant un niveau de protection adéquat par la Commission européenne (article 45, [1]), le transfert est autorisé sans autorisation spécifique. Si ce n’est pas le cas, vous devez mettre en place des garanties appropriées (article 46, [2]), telles que des clauses types de protection des données approuvées par la Commission, un code de conduite approuvé ou un mécanisme de certification, accompagné d’un engagement contraignant et exécutoire pour appliquer les droits des personnes concernées. Ces garanties doivent permettre aux personnes concernées de disposer de droits opposables et de voies de droit effectives. Le transfert ne peut avoir lieu que si les conditions du chapitre 4 du RGPD sont respectées, notamment en ce qui concerne les droits des personnes concernées et les mécanismes de contrôle (article 44, [3]). En l'absence d’un accord international comme un traité d’entraide judiciaire en vigueur entre les États-Unis et l’Union européenne, une décision d’un organisme américain exigeant un transfert ne peut pas être reconnue ou rendue exécutoire (article 48, [4]). Les conditions de l’adéquation ou des garanties appropriées doivent être vérifiées avant tout transfert.

### Extraits, sources, note, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. Un tel transfert ne nécessite pas d'autorisation spécifique. »
  [2] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
  [3] « Un transfert, vers un pays tiers ou à une organisation internationale, de données à caractère personnel qui font ou sont destinées à faire l'objet d'un traitement après ce transfert ne peut avoir lieu que si, sous réserve des autres dispositions du présent règlement, les conditions définies dans le présent chapitre sont respectées par le responsable du traitement et le sous-traitant, y compris pour les transferts ultérieurs de données à caractère personnel au départ du pays tiers ou de l'organisation internationale vers un autre pays tiers ou à une autre organisation internationale. »
  [4] « Toute décision d'une juridiction ou d'une autorité administrative d'un pays tiers exigeant d'un responsable du traitement ou d'un sous-traitant qu'il transfère ou divulgue des données à caractère personnel ne peut être reconnue ou rendue exécutoire de quelque manière que ce soit qu'à la condition qu'elle soit fondée sur un accord international, tel qu'un traité d'entraide judiciaire, en vigueur entre le pays tiers demandeur et l'Union ou un État membre, sans préjudice d'autres motifs de transfert en vertu du présent chapitre. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 45, paragraphe 1 : Transferts fondés sur une décision d'adéquation (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
  [2] RGPD — règlement (UE) 2016/679, article 46 : Transferts moyennant des garanties appropriées (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_46
  [3] RGPD — règlement (UE) 2016/679, article 44 : Principe général applicable aux transferts (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_44
  [4] RGPD — règlement (UE) 2016/679, article 48 : Transferts ou divulgations non autorisés par le droit de l'Union (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_48
Passages consultés mais non cités :
  [5] RGPD — règlement (UE) 2016/679, article 45, paragraphe 2 : Transferts fondés sur une décision d'adéquation
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
Note : La liste des pays bénéficiant d'une décision d'adéquation n'est pas dans les textes utilisés par le copilote : consultez la page de la Commission européenne sur les décisions d'adéquation (en anglais) : https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en
Attention : La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à condition que l’un des mécanismes prévus par le RGPD soit respecté ». Vérifiez-la dans les textes.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

Passages : RGPD — règlement (UE) 2016/679, article 45, paragraphe 1 : Transferts fondés sur une décision d'adéquation, RGPD — règlement (UE) 2016/679, article 46 : Transferts moyennant des garanties appropriées, RGPD — règlement (UE) 2016/679, article 44 : Principe général applicable aux transferts, RGPD — règlement (UE) 2016/679, article 48 : Transferts ou divulgations non autorisés par le droit de l'Union, RGPD — règlement (UE) 2016/679, article 45, paragraphe 2 : Transferts fondés sur une décision d'adéquation

Temps : recherche 5.0 s · génération 56.0 s · contrôle de pertinence 6.4 s

## Local, essai 2

### Réponse du copilote

> Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, à condition que l’un des mécanismes prévus par le RGPD soit respecté. Si les États-Unis ont été reconnus comme assurant un niveau de protection adéquat par une décision de la Commission européenne (article 45, [1]), alors le transfert peut avoir lieu sans autorisation spécifique. Si ce n’est pas le cas, vous devez mettre en place des garanties appropriées (article 46, [2]), telles que des clauses types de protection des données approuvées par la Commission, un code de conduite approuvé, ou un mécanisme de certification, accompagné d’un engagement contraignant et exécutoire de respecter les droits des personnes concernées. Le transfert ne peut avoir lieu que si les conditions du présent chapitre sont respectées, notamment pour les transferts ultérieurs (article 44, [3]). Les décisions de transfert doivent être fondées sur un accord international, comme un traité d’entraide judiciaire, si une autorité américaine exige un transfert (article 48, [4]). Les passages trouvés ne précisent pas que les États-Unis ont une décision d’adéquation en vigueur, donc la possibilité dépend de l’existence d’un tel avis, qui n’est pas indiquée ici.

### Extraits, sources, note, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. Un tel transfert ne nécessite pas d'autorisation spécifique. »
  [2] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
  [3] « Un transfert, vers un pays tiers ou à une organisation internationale, de données à caractère personnel qui font ou sont destinées à faire l'objet d'un traitement après ce transfert ne peut avoir lieu que si, sous réserve des autres dispositions du présent règlement, les conditions définies dans le présent chapitre sont respectées par le responsable du traitement et le sous-traitant, y compris pour les transferts ultérieurs de données à caractère personnel au départ du pays tiers ou de l'organisation internationale vers un autre pays tiers ou à une autre organisation internationale. »
  [4] « Toute décision d'une juridiction ou d'une autorité administrative d'un pays tiers exigeant d'un responsable du traitement ou d'un sous-traitant qu'il transfère ou divulgue des données à caractère personnel ne peut être reconnue ou rendue exécutoire de quelque manière que ce soit qu'à la condition qu'elle soit fondée sur un accord international, tel qu'un traité d'entraide judiciaire, en vigueur entre le pays tiers demandeur et l'Union ou un État membre, sans préjudice d'autres motifs de transfert en vertu du présent chapitre. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 45, paragraphe 1 : Transferts fondés sur une décision d'adéquation (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
  [2] RGPD — règlement (UE) 2016/679, article 46 : Transferts moyennant des garanties appropriées (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_46
  [3] RGPD — règlement (UE) 2016/679, article 44 : Principe général applicable aux transferts (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_44
  [4] RGPD — règlement (UE) 2016/679, article 48 : Transferts ou divulgations non autorisés par le droit de l'Union (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_48
Passages consultés mais non cités :
  [5] RGPD — règlement (UE) 2016/679, article 45, paragraphe 2 : Transferts fondés sur une décision d'adéquation
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
Note : La liste des pays bénéficiant d'une décision d'adéquation n'est pas dans les textes utilisés par le copilote : consultez la page de la Commission européenne sur les décisions d'adéquation (en anglais) : https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en
Attention : La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à condition que l’un des mécanismes prévus par le RGPD soit respecté ». Vérifiez-la dans les textes.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

Passages : RGPD — règlement (UE) 2016/679, article 45, paragraphe 1 : Transferts fondés sur une décision d'adéquation, RGPD — règlement (UE) 2016/679, article 46 : Transferts moyennant des garanties appropriées, RGPD — règlement (UE) 2016/679, article 44 : Principe général applicable aux transferts, RGPD — règlement (UE) 2016/679, article 48 : Transferts ou divulgations non autorisés par le droit de l'Union, RGPD — règlement (UE) 2016/679, article 45, paragraphe 2 : Transferts fondés sur une décision d'adéquation

Temps : recherche 4.8 s · génération 25.8 s · contrôle de pertinence 2.6 s

## Local, essai 3

### Réponse du copilote

> Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, à condition que l’un des mécanismes prévus par le RGPD soit respecté. Si les États-Unis ont été reconnus comme assurant un niveau de protection adéquat par une décision de la Commission européenne (article 45, [1]), alors le transfert est autorisé sans autorisation spécifique. Si ce n’est pas le cas, vous devez mettre en place des garanties appropriées (article 46, [2]), telles que des clauses types de protection des données approuvées par la Commission, un code de conduite approuvé, ou un mécanisme de certification, accompagné d’un engagement contraignant et exécutoire de respecter les droits des personnes concernées. Le transfert ne peut avoir lieu que si les conditions du chapitre 4 du RGPD sont respectées (article 44, [3]), notamment en ce qui concerne le niveau de protection des données. Les États-Unis ne sont pas reconnus comme assurant un niveau de protection adéquat par une décision de la Commission, donc le transfert ne peut être effectué que sous garanties appropriées (article 46, [2]). La décision de la Commission sur le niveau de protection des États-Unis n’est pas mentionnée dans les extraits, donc la situation reste incertaine sans preuve d’une décision d’adéquation. Les garanties appropriées doivent être prévues par le responsable du traitement ou le sous-traitant, et les droits des personnes concernées doivent être opposables et effectifs (article 46, [2]).

### Extraits, sources, note, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [1] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. Un tel transfert ne nécessite pas d'autorisation spécifique. »
  [2] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
  [3] « Un transfert, vers un pays tiers ou à une organisation internationale, de données à caractère personnel qui font ou sont destinées à faire l'objet d'un traitement après ce transfert ne peut avoir lieu que si, sous réserve des autres dispositions du présent règlement, les conditions définies dans le présent chapitre sont respectées par le responsable du traitement et le sous-traitant, y compris pour les transferts ultérieurs de données à caractère personnel au départ du pays tiers ou de l'organisation internationale vers un autre pays tiers ou à une autre organisation internationale. »
  [4] « Toute décision d'une juridiction ou d'une autorité administrative d'un pays tiers exigeant d'un responsable du traitement ou d'un sous-traitant qu'il transfère ou divulgue des données à caractère personnel ne peut être reconnue ou rendue exécutoire de quelque manière que ce soit qu'à la condition qu'elle soit fondée sur un accord international, tel qu'un traité d'entraide judiciaire, en vigueur entre le pays tiers demandeur et l'Union ou un État membre, sans préjudice d'autres motifs de transfert en vertu du présent chapitre. »

Sources citées :
  [1] RGPD — règlement (UE) 2016/679, article 45, paragraphe 1 : Transferts fondés sur une décision d'adéquation (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
  [2] RGPD — règlement (UE) 2016/679, article 46 : Transferts moyennant des garanties appropriées (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_46
  [3] RGPD — règlement (UE) 2016/679, article 44 : Principe général applicable aux transferts (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_44
  [4] RGPD — règlement (UE) 2016/679, article 48 : Transferts ou divulgations non autorisés par le droit de l'Union (version du 2016-05-04)
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_48
Passages consultés mais non cités :
  [5] RGPD — règlement (UE) 2016/679, article 45, paragraphe 2 : Transferts fondés sur une décision d'adéquation
      https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016R0679-20160504#art_45
Note : La liste des pays bénéficiant d'une décision d'adéquation n'est pas dans les textes utilisés par le copilote : consultez la page de la Commission européenne sur les décisions d'adéquation (en anglais) : https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en
Attention : La réponse formule une exception qui ne reprend pas les extraits vérifiés : « à condition que l’un des mécanismes prévus par le RGPD soit respecté ». Vérifiez-la dans les textes.

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

Passages : RGPD — règlement (UE) 2016/679, article 45, paragraphe 1 : Transferts fondés sur une décision d'adéquation, RGPD — règlement (UE) 2016/679, article 46 : Transferts moyennant des garanties appropriées, RGPD — règlement (UE) 2016/679, article 44 : Principe général applicable aux transferts, RGPD — règlement (UE) 2016/679, article 48 : Transferts ou divulgations non autorisés par le droit de l'Union, RGPD — règlement (UE) 2016/679, article 45, paragraphe 2 : Transferts fondés sur une décision d'adéquation

Temps : recherche 2.3 s · génération 27.4 s · contrôle de pertinence 2.5 s

## Distant, essai 1

### Réponse du copilote

> Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, à condition de respecter les règles du RGPD relatives aux transferts de données vers un pays tiers [3]. Ce transfert est possible si la Commission européenne a constaté par voie de décision que ce pays assure un niveau de protection adéquat, auquel cas « un tel transfert ne nécessite pas d'autorisation spécifique » [1]. À défaut de cette décision d'adéquation, vous ne pouvez transférer les données que si vous avez prévu des « garanties appropriées » et que les personnes concernées disposent de « droits opposables et de voies de droit effectives » [2]. Parmi ces garanties, vous pouvez utiliser des « clauses types de protection des données adoptées par la Commission » sans autorisation particulière [2], ou des « clauses contractuelles » entre vous et l'hébergeur, mais ces dernières sont « sous réserve de l'autorisation de l'autorité de contrôle compétente » [2]. Les passages trouvés ne permettent pas de savoir si une décision d'adéquation est actuellement en vigueur pour les États-Unis ; la liste des pays reconnus est publiée par la Commission européenne.

### Extraits, sources, note, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « Un transfert, vers un pays tiers ou à une organisation internationale, de données à caractère personnel qui font ou sont destinées à faire l'objet d'un traitement après ce transfert ne peut avoir lieu que si, sous réserve des autres dispositions du présent règlement, les conditions définies dans le présent chapitre sont respectées par le responsable du traitement et le sous-traitant, y compris pour les transferts ultérieurs de données à caractère personnel au départ du pays tiers ou de l'organisation internationale vers un autre pays tiers ou à une autre organisation internationale. »
  [1] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. »
  [1] « Un tel transfert ne nécessite pas d'autorisation spécifique. »
  [2] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
  [2] « Les garanties appropriées visées au paragraphe 1 peuvent être fournies, sans que cela ne nécessite une autorisation particulière d'une autorité de contrôle, par: … c) des clauses types de protection des données adoptées par la Commission en conformité avec la procédure d'examen visée à l'article 93, paragraphe 2; … »

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
Note : La liste des pays bénéficiant d'une décision d'adéquation n'est pas dans les textes utilisés par le copilote : consultez la page de la Commission européenne sur les décisions d'adéquation (en anglais) : https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en
Attention : 1 extrait(s) introuvable(s) mot pour mot dans le passage cité ([2]) : ignoré(s).
Attention : La réponse met entre « » un texte introuvable dans les extraits vérifiés : « sous réserve de l'autorisation de l'autorité de contrôle compétente ».

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

Passages : RGPD — règlement (UE) 2016/679, article 45, paragraphe 1 : Transferts fondés sur une décision d'adéquation, RGPD — règlement (UE) 2016/679, article 46 : Transferts moyennant des garanties appropriées, RGPD — règlement (UE) 2016/679, article 44 : Principe général applicable aux transferts, RGPD — règlement (UE) 2016/679, article 48 : Transferts ou divulgations non autorisés par le droit de l'Union, RGPD — règlement (UE) 2016/679, article 45, paragraphe 2 : Transferts fondés sur une décision d'adéquation

Temps : recherche 2.3 s · génération 2.0 s · contrôle de pertinence 0.2 s

## Distant, essai 2

### Réponse du copilote

> Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, à condition de respecter les règles du RGPD concernant les transferts de données vers un pays tiers [3]. Ce transfert est possible si la Commission européenne a constaté par voie de décision que ce pays assure un niveau de protection adéquat, auquel cas il ne nécessite pas d'autorisation spécifique [1]. En l'absence de telle décision, vous ne pouvez transférer les données que si vous avez prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives [2]. Parmi ces garanties, vous pouvez utiliser des clauses types de protection des données adoptées par la Commission, sans autorisation particulière, ou des clauses contractuelles, sous réserve de l'autorisation de l'autorité de contrôle compétente [2].

### Extraits, sources, note, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « Un transfert, vers un pays tiers ou à une organisation internationale, de données à caractère personnel qui font ou sont destinées à faire l'objet d'un traitement après ce transfert ne peut avoir lieu que si, sous réserve des autres dispositions du présent règlement, les conditions définies dans le présent chapitre sont respectées par le responsable du traitement et le sous-traitant, y compris pour les transferts ultérieurs de données à caractère personnel au départ du pays tiers ou de l'organisation internationale vers un autre pays tiers ou à une autre organisation internationale. »
  [1] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. »
  [1] « Un tel transfert ne nécessite pas d'autorisation spécifique. »
  [2] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
  [2] « Les garanties appropriées visées au paragraphe 1 peuvent être fournies, sans que cela ne nécessite une autorisation particulière d'une autorité de contrôle, par: … c) des clauses types de protection des données adoptées par la Commission en conformité avec la procédure d'examen visée à l'article 93, paragraphe 2; … »
  [2] « Sous réserve de l'autorisation de l'autorité de contrôle compétente, les garanties appropriées visées au paragraphe 1 peuvent aussi être fournies, notamment, par: a) des clauses contractuelles entre le responsable du traitement ou le sous-traitant et le responsable du traitement, le sous-traitant ou le destinataire des données à caractère personnel dans le pays tiers ou l'organisation internationale; … »

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
Note : La liste des pays bénéficiant d'une décision d'adéquation n'est pas dans les textes utilisés par le copilote : consultez la page de la Commission européenne sur les décisions d'adéquation (en anglais) : https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

Passages : RGPD — règlement (UE) 2016/679, article 45, paragraphe 1 : Transferts fondés sur une décision d'adéquation, RGPD — règlement (UE) 2016/679, article 46 : Transferts moyennant des garanties appropriées, RGPD — règlement (UE) 2016/679, article 44 : Principe général applicable aux transferts, RGPD — règlement (UE) 2016/679, article 48 : Transferts ou divulgations non autorisés par le droit de l'Union, RGPD — règlement (UE) 2016/679, article 45, paragraphe 2 : Transferts fondés sur une décision d'adéquation

Temps : recherche 2.3 s · génération 1.8 s · contrôle de pertinence 0.2 s · attente des limites de l'API 12 s (non comptée)

## Distant, essai 3

### Réponse du copilote

> Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, à condition de respecter les règles du RGPD relatives aux transferts de données vers un pays tiers [3]. Ce transfert est possible si la Commission européenne a constaté par voie de décision que le pays tiers assure un niveau de protection adéquat, auquel cas le transfert « ne nécessite pas d'autorisation spécifique » [1]. À défaut de cette décision d'adéquation, vous ne pouvez transférer les données que si vous avez prévu des « garanties appropriées » et que les personnes concernées disposent de « droits opposables et de voies de droit effectives » [2]. Parmi ces garanties, vous pouvez utiliser des « clauses types de protection des données adoptées par la Commission » sans autorisation particulière, ou des « clauses contractuelles » sous réserve de l'autorisation de l'autorité de contrôle compétente [2]. La liste des pays reconnus comme offrant un niveau de protection adéquat est publiée par la Commission européenne.

### Extraits, sources, note, contrôles et avertissement (ajoutés par le code)

```text
Extraits vérifiés (recopiés mot pour mot des textes) :
  [3] « Un transfert, vers un pays tiers ou à une organisation internationale, de données à caractère personnel qui font ou sont destinées à faire l'objet d'un traitement après ce transfert ne peut avoir lieu que si, sous réserve des autres dispositions du présent règlement, les conditions définies dans le présent chapitre sont respectées par le responsable du traitement et le sous-traitant, y compris pour les transferts ultérieurs de données à caractère personnel au départ du pays tiers ou de l'organisation internationale vers un autre pays tiers ou à une autre organisation internationale. »
  [1] « Un transfert de données à caractère personnel vers un pays tiers ou à une organisation internationale peut avoir lieu lorsque la Commission a constaté par voie de décision que le pays tiers, un territoire ou un ou plusieurs secteurs déterminés dans ce pays tiers, ou l'organisation internationale en question assure un niveau de protection adéquat. »
  [1] « Un tel transfert ne nécessite pas d'autorisation spécifique. »
  [2] « En l'absence de décision en vertu de l'article 45, paragraphe 3, le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. »
  [2] « Les garanties appropriées visées au paragraphe 1 peuvent être fournies, sans que cela ne nécessite une autorisation particulière d'une autorité de contrôle, par: … c) des clauses types de protection des données adoptées par la Commission en conformité avec la procédure d'examen visée à l'article 93, paragraphe 2; … »
  [2] « Sous réserve de l'autorisation de l'autorité de contrôle compétente, les garanties appropriées visées au paragraphe 1 peuvent aussi être fournies, notamment, par: a) des clauses contractuelles entre le responsable du traitement ou le sous-traitant et le responsable du traitement, le sous-traitant ou le destinataire des données à caractère personnel dans le pays tiers ou l'organisation internationale; … »

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
Note : La liste des pays bénéficiant d'une décision d'adéquation n'est pas dans les textes utilisés par le copilote : consultez la page de la Commission européenne sur les décisions d'adéquation (en anglais) : https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en

Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, demandez l'avis d'un professionnel ou de la CNIL.
```

Passages : RGPD — règlement (UE) 2016/679, article 45, paragraphe 1 : Transferts fondés sur une décision d'adéquation, RGPD — règlement (UE) 2016/679, article 46 : Transferts moyennant des garanties appropriées, RGPD — règlement (UE) 2016/679, article 44 : Principe général applicable aux transferts, RGPD — règlement (UE) 2016/679, article 48 : Transferts ou divulgations non autorisés par le droit de l'Union, RGPD — règlement (UE) 2016/679, article 45, paragraphe 2 : Transferts fondés sur une décision d'adéquation

Temps : recherche 2.3 s · génération 2.1 s · contrôle de pertinence 0.2 s · attente des limites de l'API 46 s (non comptée)
