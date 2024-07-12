from Recherche import*
from stocker_donnees import *
from charger_donnees import * 

def enregistrer_vente():
    lite_ventes = charger_Vente()
    liste_produits = charger_produit()  
  
    indice,verificateur  = recherche_produit()

    if  verificateur == 0:
         print("le produit ne pas disponible")
    else:
            
      nom=input("entrez le nom du client: ")
      qte=input("entrez la quantité vendue: ")
      prix=input("entrez le prix de l'article: ")
      article=input("entrez le nom du produit vendu :")
      
      
      ventes = {
           "qte":qte,
           "prix":prix,
           "nom_client":nom,
           "article":article
      }
      lite_ventes.append(ventes)
      liste_produits[indice]['QUANTITE'] = int(liste_produits[indice]['QUANTITE'])- int(qte) 

      sauvegarder_produit(liste_produits)
      sauv_vente(lite_ventes)
      
    
      