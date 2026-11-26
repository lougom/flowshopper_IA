"""Modèle « Habituel » : les produits qu'un villageois achète le plus souvent.

Variante fréquence : nombre de commandes distinctes où le produit apparaît.
La variante récence viendra ensuite.
"""

import pandas as pd

from src.interface import Suggestion

class Model:
    name = "hybrid"
    
    def __init__(self):
        self.ranking = pd.DataFrame()  # sera rempli par fit

    def fit(self, history: pd.DataFrame, catalog: pd.DataFrame , people = None ) -> None:
        # 1. Total acheté par produit, du plus grand au plus petit
        totals = (
            history.groupby("product_id")["quantity"]
            .sum()
            .sort_values(ascending=False)
            .reset_index(name="total")
        )
