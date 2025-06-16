# models/patissier.py

class Patissier:
    def __init__(self, id_patissier, nom, prenom):
        self.id_patissier = id_patissier
        self.nom = nom
        self.prenom = prenom

    def preparer_gateau(self, gateau):
        print(f"\n👨‍🍳 {self.nom} {self.prenom} prépare le gâteau : {gateau.nom}")
        for ing, qte in gateau.ingredients:
            print(f"- Vérification de {ing.nom}... ({ing.quantite_disponible}g en stock)")
            if not ing.retirer_quantite(qte):
                print("❌ Préparation interrompue : stock insuffisant.")
                return
        print("✅ Tous les ingrédients sont disponibles.")
        print("🧁 Préparation terminée avec succès !\n")

