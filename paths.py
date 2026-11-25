"""Configuration du projet : les chemins utilisés partout dans le repo.

Ce fichier définit les chemins une seule fois. Les autres fichiers
(modèles, évaluation, routes) les importent au lieu de les recalculer :
    from src.config import DATA_DIR
"""

from pathlib import Path

# Racine du repo : config.py est dans src/, donc on remonte d'un cran.
ROOT_DIR = Path(__file__).resolve().parents[1]

# Dossier contenant les CSV (catalogue et historique d'achats).
DATA_DIR = ROOT_DIR / "data"