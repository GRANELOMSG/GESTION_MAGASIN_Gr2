from Recherche import*
from stocker_donnees import *
from charger_donnees import *
from Vente import*

def toutes_vente():

    lite_ventes.append(ventes)
    liste_produits[indice]['QUANTITE'] = int(liste_produits[indice]['QUANTITE'])- int(qte) 

    sauvegarder_produit(liste_produits)
    sauv_vente(lite_ventes)