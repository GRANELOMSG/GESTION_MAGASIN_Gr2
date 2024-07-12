from datetime import datetime
import time
from stocker_donnees import * 
from charger_donnees import *

def ajouter_produit(liste_parametre):
    liste_parametre = charger_produit()
    id = len(liste_parametre)+1
    liste_provisoire = {"ID":0,"NOM":0,"PRIX":0,"QUANTITE":0,"DATE":0,"HEURE":0}
    nom = input("entrez le nom du produit : ")
    nom.isalpha()
    while nom.isalpha()==False:
        nom = input("entrez le nom du produit : ")
    nom_produit = nom.upper()
 
    quantite_produit = input("Entrez la quantité du produit : ")
    quantite_produit.isdigit()
    while quantite_produit.isdigit()==False:
         quantite_produit = input("Entrez la quantité du produit : ")

    prix_produit = input("Entrez le prix du produit : ")
    prix_produit.isdigit()
    while prix_produit.isdigit()==False:
        prix_produit = input("Entrez le prix du produit : ")

    verificateur = 0
    for produit in liste_parametre:
        if produit['NOM'].lower() == nom_produit.lower():
            verificateur +=1
    if verificateur == 0:
        liste_provisoire["ID"] = id
        liste_provisoire["NOM"] = nom_produit
        liste_provisoire["PRIX"] = prix_produit
        liste_provisoire["QUANTITE"] = quantite_produit
        heure = time.strftime('%H:%M:%S')
        date = datetime.today().strftime('%d/%m/%y')
        liste_provisoire["HEURE"] = heure
        liste_provisoire["DATE"] = date
        

        liste_parametre.append(liste_provisoire)

        sauvegarder_produit(liste_parametre)
        print("===Produit enregristré :)=== ")
    else:
        print("erreur!!! le produit existe déjà!")