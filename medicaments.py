#coding:utf-8

"""
Module de création de la classe MEDICAMENT

"""
import controls_entry

lst_medic = []

class Medicaments:
    def __init__(self, name, price, stock):
        self._name = name
        self._price = price
        self._stock = stock

    def _getName(self):
        return self._name.capitalize()

    def _setName(self, new_name):
        controls_entry.log(f"INFO : Le nouveau nom du medicament {self._name} est {new_name}")
        self._name = new_name.lower()

    def _getPrice(self):
        var = str(self._price)
        var += "€"
        return var

    def _setPrice(self, new_price):
        self._price = new_price
        controls_entry.log(f"INFO : le nouveau montant unitaire du medicament {self._name} est de {self._price} ")

    def _getStock(self):
        return self._stock

    def _setStock(self, add):
        self._stock += add

    name = property(_getName, _setName)
    price = property(_getPrice, _setPrice)
    stock = property(_getStock, _setStock)
