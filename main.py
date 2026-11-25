"""Point d'entrée : un mini exemple pour vérifier que tout se branche.

Lancer depuis la racine du repo : uv run python -m src.main
"""

import pandas as pd

from paths import DATA_DIR

# from src.models.popular import Model   # à décommenter quand popular.py existe


def main():
    # 1. Voir ce qu'il y a dans data/
    for csv_path in sorted(DATA_DIR.glob("*.csv")):
        print(csv_path.name)

    # 2. Charger les données (remplace par les vrais noms de fichiers)
    history = pd.read_csv(DATA_DIR / "orders.csv")
    catalog = pd.read_csv(DATA_DIR / "catalog.csv")
    print(history.head())
    print(catalog.head())

    # 3. Entraîner le modèle et demander un exemple (quand il existera)
    # model = Model()
    # model.fit(history, catalog)
    # for s in model.recommend("V-0042", k=5):
    #     print(s["product_id"], s["score"], s["reason"])


if __name__ == "__main__":
    main()