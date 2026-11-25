"""Modèle « Populaire » : les produits les plus achetés sur l'île.

Aucun apprentissage : fit compte les achats, recommend lit le classement.
"""

import pandas as pd

from src.interface import Suggestion


class Model:
    name = "popular"

    def __init__(self):
        self.ranking = pd.DataFrame()  # sera rempli par fit

    def fit(self, history: pd.DataFrame, catalog: pd.DataFrame) -> None:
        # 1. Total acheté par produit, du plus grand au plus petit
        totals = (
            history.groupby("product_id")["quantity"]
            .sum()
            .sort_values(ascending=False)
            .reset_index(name="total")
        )

        # 2. Ajouter le nom du produit (merge avec le catalogue)
        self.ranking = totals.merge(
            catalog[["id", "name"]],
            left_on="product_id",
            right_on="id",
            how="left",
        )

    def recommend(self, villager_id: str, k: int = 10,
                  context: dict | None = None) -> list[Suggestion]:
        # Même liste pour tout le monde : villager_id n'est pas utilisé.
        top = self.ranking.head(k)
        return [
            {
                "product_id": row.product_id,
                "score": float(row.total),
                "reason": f"Parmi les plus achetés sur l'île : {row['name']}",
            }
            for _, row in top.iterrows()
        ]