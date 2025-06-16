from models.utilisateur import Utilisateur
from models.ingredient import Ingredient
from models.gateau import Gateau
from models.commande import Commande
from models.recette import Recette
from models.patissier import Patissier
import json
import os

# 🔄 JSON : sauvegarde et chargement utilisateur
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
            u = Utilisateur(data["id"], data["nom"], data["prenom"])
            u.ajouter_points(data["points"])
            return u
    except FileNotFoundError:
        return None

# 💡 Menu principal
def afficher_menu():
    print("\n🍰 MENU GÂTEAU FACTORY 🍰")
    print("1. Créer un utilisateur")
    print("2. Commander un gâteau")
    print("3. Préparer un gâteau")
    print("4. Voir les recettes")
    print("5. Voir le stock")
    print("6. Quitter")

# 📦 Ingrédients
stock_ingredients = {
    "Sucre": Ingredient(1, "Sucre", "sucre", 500),
    "Farine": Ingredient(2, "Farine", "farine", 1000),
    "Chocolat": Ingredient(3, "Chocolat", "pâte", 300)
}

# 🧁 Gâteaux
gateau1 = Gateau(101, "Moelleux chocolat", "Gâteau au chocolat moelleux.")
gateau1.ajouter_ingredient(stock_ingredients["Sucre"], 200)
gateau1.ajouter_ingredient(stock_ingredients["Farine"], 300)
gateau1.ajouter_ingredient(stock_ingredients["Chocolat"], 250)

gateau2 = Gateau(102, "Fraisier", "Gâteau à la fraise et crème.")
gateau2.ajouter_ingredient(stock_ingredients["Sucre"], 150)
gateau2.ajouter_ingredient(stock_ingredients["Farine"], 250)

gateau3 = Gateau(103, "Tarte aux pommes", "Tarte traditionnelle aux pommes.")
gateau3.ajouter_ingredient(stock_ingredients["Sucre"], 100)
gateau3.ajouter_ingredient(stock_ingredients["Farine"], 200)

gateaux_disponibles = [gateau1, gateau2, gateau3]

# 📚 Recettes
recette1 = Recette(1, "Recettes disponibles")
for g in gateaux_disponibles:
    recette1.ajouter_gateau(g)

# 👤 Chargement de l’utilisateur si existant
utilisateur = charger_utilisateur()
if utilisateur:
    print(f"\n👋 Bienvenue de retour, {utilisateur.nom} ! Points : {utilisateur.points}")

# 👩‍🍳 Pâtissier
patissier = Patissier(1, "Lucie", "Martin")
commande = None

# ▶️ Boucle du menu
while True:
    afficher_menu()
    choix = input("Choix : ")

    if choix == "1":
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        utilisateur = Utilisateur(1, nom, prenom)
        sauvegarder_utilisateur(utilisateur)
        print(f"✅ Utilisateur {nom} créé avec succès.")

    elif choix == "2":
        if not utilisateur:
            print("⚠️ Crée d'abord un utilisateur.")
            continue

        print("\n🍰 Gâteaux disponibles à la commande :")
        for idx, g in enumerate(gateaux_disponibles):
            print(f"{idx + 1}. {g.nom}")

        try:
            choix_gateau = int(input("Choisissez un gâteau (numéro) : "))
            if choix_gateau < 1 or choix_gateau > len(gateaux_disponibles):
                print("❌ Choix invalide.")
                continue
        except ValueError:
            print("❌ Entrée non valide.")
            continue

        selected_gateau = gateaux_disponibles[choix_gateau - 1]
        commande = Commande(1, f"CMD{selected_gateau.id_gateau}")
        commande.ajouter_gateau(selected_gateau)
        commande.valider_commande()
        utilisateur.ajouter_points(20)
        sauvegarder_utilisateur(utilisateur)

    elif choix == "3":
        if not commande:
            print("⚠️ Passe d’abord une commande.")
            continue
        for g in commande.gateaux:
            patissier.preparer_gateau(g)

    elif choix == "4":
        recette1.afficher_recette()

    elif choix == "5":
        print("\n📦 Stock d'ingrédients :")
        for ing in stock_ingredients.values():
            print(f"{ing.nom} : {ing.quantite_disponible}g")

    elif choix == "6":
        if utilisateur:
            sauvegarder_utilisateur(utilisateur)
        print("👋 Merci d’avoir joué à Gâteau Factory !")
        break

    else:
        print("❌ Choix invalide.")
