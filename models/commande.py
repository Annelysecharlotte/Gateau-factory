# models/commande.py

class Commande:
    def __init__(self, id_commande, num_commande):
        self.id_commande = id_commande
        self.num_commande = num_commande
        self.gateaux = []

    def ajouter_gateau(self, gateau):
        self.gateaux.append(gateau)

    def valider_commande(self):
        print(f"\nCommande n°{self.num_commande} (ID : {self.id_commande})")
        print("Contenu de la commande :")
        for g in self.gateaux:
            g.afficher_details()
        print("Commande validée ✅\n")
