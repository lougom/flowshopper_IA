"""Règle commune : la forme que doit avoir chaque modèle de recommandation.

Ce fichier ne contient aucune logique. Il décrit seulement ce que les modèles
(popular.py, habitual.py, ...) doivent proposer, pour que l'API et les tests
puissent tous les appeler de la même façon.
"""

from typing import Protocol, TypedDict


class Suggestion(TypedDict):
    """Une recommandation renvoyée au site."""

    product_id: str   # identifiant du produit
    score: float      # plus il est haut, plus le produit est recommandé
    reason: str       # phrase simple, ex. "Dans 8 de vos 10 dernières commandes"


class Recommender(Protocol):
    """Ce que tout modèle doit avoir."""

    name: str  # nom du modèle, ex. "popular"

    def fit(self, history, catalog) -> None:
        """Prépare le modèle avec l'historique d'achats et le catalogue."""
        ...

    def recommend(self, villager_id: str, k: int = 10,
                  context: dict | None = None) -> list[Suggestion]:
        """Renvoie au plus k suggestions pour ce villageois.

        context sert à passer des infos en plus, par exemple
        {"product_id": "..."} pour « Similar products ».
        """
        ...