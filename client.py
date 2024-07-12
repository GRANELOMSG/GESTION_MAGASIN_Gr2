import json
from Vente import*

def afficher_vente_par_client():
    try:
        with open("ventes.json","r") as fichier:
            ventes_enregistrees=json.load(fichier)
    except(FileNotFoundError,json.JSONDecodeError):
        print("Aucune vente enregistrée !")
        return
    nom = input("Entrez le nom du client : ")
    ventes_client=[]
    for vente in ventes_enregistrees:
        if vente['nom_client']== nom:
            ventes_client.append(vente)
    if not ventes_client:
        print(f"Aucune vente trouvée pour Mr, Mme: {nom} ")
        return
    print(f"\n Ventes pour le client {nom}:")
    for vente in ventes_client:
        print(f"-{vente['article']}:{vente['qte']} à {vente['prix']}")
