#coding:utf-8

"""
Module de création de la classe MEDICAMENT

"""
lst_medic = []

class Medicaments:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def affichage(self):
        pass
#affiche le nom du medicaments et sont stock

    def approvisionnement(self):
        pass
# check le nom du medicaments et ajoute la quantité set()*