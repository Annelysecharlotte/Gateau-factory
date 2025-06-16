# models/ingredient.py

class Ingredient:
    def __init__(self, id_ingredient, nom, type, quantite_disponible=0):
        self.id_ingredient = id_ingredient
        self.nom = nom
        self.type = type
        self.quantite_disponible = quantite_disponible

    def mettre_a_jour_quantite(self, nouvelle_qte):
        self.quantite_disponible = nouvelle_qte

    def retirer_quantite(self, qte):
        if self.quantite_disponible >= qte:
            self.quantite_disponible -= qte
            return True
        else:
            print(f"⚠️ Pas assez de {self.nom} en stock.")
            return False

