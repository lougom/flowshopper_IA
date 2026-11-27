import pandas as pd

from src.models.popular import Model


def test_popular_classe_par_quantite_totale():
    history = pd.DataFrame({
        "user_id": ["1", "2", "1"],
        "product_id": ["A", "B", "B"],
        "quantity": [1, 5, 2],
    })
    catalog = pd.DataFrame({
        "id": ["A", "B"],
        "name": ["Pomme", "Pain"],
    })

    model = Model()
    model.fit(history, catalog)
    result = model.recommend(villager_id="1", k=10)

    # B a 7 au total (5 + 2), A n'en a que 1 : B doit être en premier
    assert result[0]["product_id"] == "B"
    assert len(result) == 2


def test_popular_respecte_k():
    history = pd.DataFrame({
        "user_id": ["1", "2"],
        "product_id": ["A", "B"],
        "quantity": [1, 1],
    })
    catalog = pd.DataFrame({
        "id": ["A", "B"],
        "name": ["Pomme", "Pain"],
    })

    model = Model()
    model.fit(history, catalog)
    result = model.recommend(villager_id="1", k=1)

    assert len(result) == 1