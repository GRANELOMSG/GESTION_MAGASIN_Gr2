from charger_donnees import * 

def afficher_produit():
    liste_produits = charger_produit()

    for produit in liste_produits:
        print(f"ID : {produit['ID']} | NOM : {produit['NOM']} | PRIX : {produit['PRIX']} | QUANTITE : {produit['QUANTITE']} | DATE : {produit['DATE']} | HEURE : {produit['HEURE']}")



def afficher_ventes():
    produit_vendus=afficher_ventes
    liste_produits=charger_produit()
    