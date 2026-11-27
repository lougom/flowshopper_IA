import pandas as pd

from src.interface import Suggestion


class Model:
    name = "habitual"

    def __init__(self):
        self.per_user = pd.DataFrame()        # une ligne par (villageois, produit)
        self.global_counts = pd.DataFrame()   # une ligne par produit, tous villageois confondus
        self.dates_per_user = {}              # nombre de dates d'achat par villageois

    def fit(self, history: pd.DataFrame, catalog: pd.DataFrame) -> None:
        # Copie, pour ne pas modifier le tableau reçu, et identifiants en texte
        history = history.copy()
        history["user_id"] = history["user_id"].astype(str)

        # Un achat = (villageois, produit, date) : deux achats le même jour comptent pour un seul
        achats = history[["user_id", "product_id", "order_date"]].drop_duplicates()

        # Par villageois et par produit : le nombre d'achats distincts est le nombre de dates
        self.per_user = (
            achats.groupby(["user_id", "product_id"])
            .size()
            .reset_index(name="dates")
            .merge(catalog[["id", "name"]], left_on="product_id", right_on="id", how="left")
        )

        # Tous villageois confondus : nombre d'achats distincts par produit
        self.global_counts = (
            achats.groupby("product_id")
            .size()
            .reset_index(name="dates")
            .merge(catalog[["id", "name"]], left_on="product_id", right_on="id", how="left")
        )

        # Nombre de dates d'achat de chaque villageois, pour la raison
        self.dates_per_user = history.groupby("user_id")["order_date"].nunique().to_dict()

    def recommend(self, villager_id: str | None = None, k: int = 10,
                  context: dict | None = None) -> list[Suggestion]:
        # Sans identifiant : tous les villageois. Avec : seulement ce villageois
        if villager_id is None:
            table = self.global_counts
            total = None
        else:
            vid = str(villager_id)
            table = self.per_user[self.per_user["user_id"] == vid]
            total = self.dates_per_user.get(vid, 0)

        top = table.sort_values("dates", ascending=False).head(k)

        suggestions = []
        for _, row in top.iterrows():
            if total is None:
                reason = f"Acheté {row['dates']} fois sur l'île : {row['name']}"
            else:
                reason = f"Acheté à {row['dates']} dates sur vos {total} : {row['name']}"
            suggestions.append({
                "product_id": row["product_id"],
                "score": float(row["dates"]),
                "reason": reason,
            })
        return suggestions