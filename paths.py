"""Configuration du projet : les chemins utilisés partout dans le repo.

Ce fichier définit les chemins une seule fois. Les autres fichiers
(modèles, évaluation, routes) les importent au lieu de les recalculer :
    from src.config import DATA_DIR
"""

from pathlib import Path

# Racine du repo : paths.py est dans reco/flowshopper_IA/, donc parents[2].
ROOT_DIR = Path(__file__).resolve().parents[2]

# Dossier contenant les CSV (catalogue et historique d'achats).
DATA_DIR = ROOT_DIR / "data"