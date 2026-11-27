import pandas as pd

from src.models.habitual import Model


def donnees():
    history = pd.DataFrame({
        "user_id": ["1", "1", "1", "1", "2", "2", "2"],
        "product_id": ["A", "A", "A", "B", "B", "B", "B"],
        "order_date": [
            "2026-01-01", "2026-01-01", "2026-01-08",  # 2 achats de A le 01/01 : un seul compte
            "2026-01-01",
            "2026-01-03", "2026-01-10", "2026-01-17",
        ],
    })
    catalog = pd.DataFrame({
        "id": ["A", "B"],
        "name": ["Pomme", "Pain"],
    })
    return history, catalog


def test_habitual_compte_une_seule_fois_les_achats_du_meme_jour():
    history, catalog = donnees()
    model = Model()
    model.fit(history, catalog)

    result = model.recommend(villager_id="1", k=10)

    # Pour le villageois 1 : A a été acheté sur 2 dates (01/01 et 08/01), pas 3 fois
    assert result[0]["product_id"] == "A"
    assert result[0]["score"] == 2.0
    assert result[0]["reason"] == "Acheté à 2 dates sur vos 2 : Pomme"


def test_habitual_sans_identifiant_classe_tous_les_villageois():
    history, catalog = donnees()
    model = Model()
    model.fit(history, catalog)

    result = model.recommend(villager_id=None, k=10)

    # Tous confondus : B a 4 dates d'achat, A en a 2
    assert result[0]["product_id"] == "B"
    assert result[0]["score"] == 4.0
    assert result[0]["reason"] == "Acheté 4 fois sur l'île : Pain"


def test_habitual_villageois_sans_historique_renvoie_liste_vide():
    history, catalog = donnees()
    model = Model()
    model.fit(history, catalog)

    assert model.recommend(villager_id="99", k=10) == []