#MONGA ILUNGA GRACIA
#MONGA SEYA GRANELO
#MOZA FATUMA BENEDICTE
#MPENGE MULUMBU LOIS

from Ajouter_produit import *
from Afficher_prosuits import * 
from Recherche import * 
from supprimer_produit import*
from Vente import * 
from client import*
from affichage_de_vente import*

def menu_principal():
    print("====BARRE DE MENU====\n")
    print("1. Ajouts des produits")
    print("2. Affichage des produits")
    print("3. Recherche des produits")
    print("4. Achats des produits")
    print("5. Suppression des produits")
    print("6. Affichage des ventes")
    print("7. Ventes par client")
    print("8. Chargement de données")
    print("9. Quitter")
    return input("Faites le choix d'option: ")

def main():
    
    liste_produits = [] 
    while True:
        choix = menu_principal()
        if choix == '1':
            ajouter_produit(liste_produits)
        elif choix == '2':
            afficher_produit()
        elif choix == '3':
           recherche_produit()
        elif choix == '4':
            enregistrer_vente()
        elif choix == '5':
            supprimer_produits()
        elif choix == '6':
            toutes_vente()
        elif choix == '7':
            afficher_vente_par_client()
        elif choix == '8':
            charger_produit()
        elif choix == '9':
            break
        else:
            print("Choix invalide, veuillez réessayer.")


main()