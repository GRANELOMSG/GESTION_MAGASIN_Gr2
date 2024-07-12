import json
def sauv_vente(liste_parametre):
    with open('ventes.json','w+') as fichier:
        json.dump(liste_parametre,fichier)


def sauvegarder_produit(liste_parametre):
    with open('produit.json','w+') as fichier:
        json.dump(liste_parametre,fichier)



