import json

def charger_produit():
    with open("produit.json","r") as Fichier:
        liste_produits = json.load(Fichier)
    return liste_produits

def charger_Vente():
    with open ("ventes.json","r") as FICHIER:
        ventes = json.load(FICHIER)
    return ventes 


 
