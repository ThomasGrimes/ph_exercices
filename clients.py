#coding:utf-8

"""
Module de création de la classe Client

"""
import pickle
lst_client = []

class Clients:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits

# affiche le nom du client et son crédit
    def affichage(self):
        pass

# definit l'achat du medicament avec la quantite a soustraire et le prix a ajouter au credit du client
    def achat(self, medoc, quantite):
        pass

    def save(self):
        with open("data/clients.data", "wb") as backup:
            record = pickle.Pickler(backup)
            record.dump(lst_client)