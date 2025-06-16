import json

def sauvegarder_utilisateur(utilisateur, filename="utilisateur.json"):
    data = {
        "id": utilisateur.id_utilisateur,
        "nom": utilisateur.nom,
        "prenom": utilisateur.prenom,
        "points": utilisateur.points
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def charger_utilisateur(filename="utilisateur.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            from models.utilisateur import Utilisateur
            u = Utilisateur(data["id"], data["nom"], data["prenom"])
            u.ajouter_points(data["points"])
            return u
    except FileNotFoundError:
        return None
