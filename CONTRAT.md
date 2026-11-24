# CONTRAT.md

**Version : 0.1**

## Rôle du fichier

Ce fichier décrit les routes du service de recommandation (équipe IA) que le site (équipe Web) peut appeler.

## Format d'une suggestion

Chaque route de recommandation renvoie une courte liste :

```json
[
  { "product_id": "P-0012", "score": 0.87, "reason": "Dans 8 de vos 10 dernières commandes" }
]
```

## Routes disponibles


| Route | Paramètres | Usage |
|---|---|---|
| `GET /reco/popular` | `k` | Populaire sur l'île |
| `GET /reco/usual` | `villager_id`, `k` | Vos produits habituels |
| `POST /events` | liste d'événements | Le site envoie ce que fait le villageois |
| `DELETE /villagers/{id}` | | Efface ses données chez nous (RGPD) |

Le paramètre k, c'est le nombre de produits qui seront reçues en réponse.

Si le service ne répond pas ou si un modèle manque, le site affiche « Populaire » ou rien.

---
Version 0.1