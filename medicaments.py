#coding:utf-8

"""
Module de création de la classe MEDICAMENT

"""

class Medicaments:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def affichage(self):
        #affiche le nom du medicaments et sont stock

    def approvisionnement(self):
        # check le nom du medicaments et ajoute la quantité set()*