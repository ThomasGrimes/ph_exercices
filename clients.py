#coding:utf-8

"""
Module de création de la classe Client

"""

class Clients:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits

    def affichage(self):
        # affiche le nom du client et son crédit

    def achat(self, medoc, quantite):
        #definit l'achat du medicament avec la quantite a soustraire et le prix a ajouter au credit du client