# Résultats de la séance 5 — avant / après

Toutes les mesures sont produites par les scripts du dépôt. Les questions `eval/questions_v1.jsonl` ont été écrites et commitées **avant** toute amélioration : elles servent seulement à mesurer, on ne règle rien dessus.

## 1. Mesure de départ (recherche par vecteurs seuls, avant toute amélioration)

Commande : `scripts/evaluate_retrieval.py --questions …` (rang cherché parmi les 20 premiers passages ; les questions hors sujet ne sont pas comptées).

| Jeu de questions | hit@1 | hit@5 |
|---|---|---|
| v0 (10 questions) | 6/10 | 7/10 |
| v1 (17 questions + 3 hors sujet) | 9/17 | 11/17 |

Échecs de départ sur v1 (rang du premier article attendu) : q14 prospection (non trouvé), q15 sous-traitant (6), q16 hébergeur aux États-Unis (6), q18 données de santé (non trouvé), q21 sécurité (non trouvé), q24 émotions au travail (9).
