# models/recette.py

class Recette:
    def __init__(self, id_recette, nom):
        self.id_recette = id_recette
        self.nom = nom
        self.gateaux = []

    def ajouter_gateau(self, gateau):
        self.gateaux.append(gateau)

    def afficher_recette(self):
        print(f"\nRecette : {self.nom} (ID : {self.id_recette})")
        for gateau in self.gateaux:
            gateau.afficher_details()
