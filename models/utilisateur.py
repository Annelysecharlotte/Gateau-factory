# models/utilisateur.py

class Utilisateur:
    def __init__(self, id_utilisateur, nom, prenom):
        self.id_utilisateur = id_utilisateur
        self.nom = nom
        self.prenom = prenom
        self.points = 0  # Par défaut

    def ajouter_points(self, points):
        self.points += points

    def afficher_info(self):
        print(f"Utilisateur : {self.nom} {self.prenom}")
        print(f"ID : {self.id_utilisateur}")
        print(f"Points : {self.points}")
