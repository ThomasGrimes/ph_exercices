#coding:utf-8

"""
Module de création de la classe MEDICAMENT

"""
lst_medic = []

class Medicaments:
    def __init__(self, name, price, stock):
        self._name = name
        self._price = price
        self._stock = stock

    def _getName(self):
        return self._name.capitalize()

    def _getPrice(self):
        return self._price

    def _getStock(self):
        return self._stock

    name = property(_getName)
    price = property(_getPrice)
    stock = property(_getStock)
