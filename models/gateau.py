# models/gateau.py

class Gateau:
    def __init__(self, id_gateau, nom, description):
        self.id_gateau = id_gateau
        self.nom = nom
        self.description = description
        self.ingredients = []  # Liste de tuples : (ingredient, quantité)

    def ajouter_ingredient(self, ingredient, quantite):
        self.ingredients.append((ingredient, quantite))

    def afficher_details(self):
        print(f"Gâteau : {self.nom} (ID : {self.id_gateau})")
        print(f"Description : {self.description}")
        print("Ingrédients :")
        for ing, qte in self.ingredients:
            print(f"- {ing.nom} ({ing.type}) : {qte}g")
