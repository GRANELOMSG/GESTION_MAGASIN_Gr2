from charger_donnees import * 

def recherche_produit():
    liste_produits = charger_produit()
    choix_utilisateur = input("Saisisez l'Identifiant ou le Nom de l'article a rechercher : ")
    compt = 0
    for produit in liste_produits:
        if produit['NOM'].lower() == choix_utilisateur.lower() or str(produit['ID']) == choix_utilisateur:
            compt += 1
            print(f"ID : {produit['ID']} | NOM : {produit['NOM']} | PRIX : {produit['PRIX']} | QUANTITE : {produit['QUANTITE']} | DATE : {produit['DATE']} | HEURE : {produit['HEURE']}")

    if compt == 0 : 
        print(f"il y a aucun produit qui porte le nom ou l'ID {choix_utilisateur}")
        return 0,0
    else:
        return 1,produit['ID'] 

