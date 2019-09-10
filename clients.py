#coding:utf-8

"""
Module de création de la classe Client

"""
import medicaments
import controls_entry

lst_client = []

class Clients:

    def __init__(self, name, credits):
        self._name = name
        self._credits = credits

    def _getName(self):
        return self._name.capitalize()

    def _setName(self, new_name):
        controls_entry.log(f"MODIFICATION : Le nouveau nom du client {self._name} est {new_name}")
        self._name = new_name.lower()

    def _getCredits(self):
        return self._credits

    def _setCredits(self, add_credits):
        if add_credits > 0:
            self._credits += add_credits
            controls_entry.log(f"Le nouveau crédit du client {self._name} est de {self._credits}")

    name = property(_getName, _setName)
    credits = property(_getCredits, _setCredits)

# definit l'achat du medicament avec la quantite a soustraire et le prix a ajouter au credit du client
    def achat(self, medoc, quantite):
        for med in medicaments.lst_medic:
            if med.name == medoc:
                self.credits -= med.price*quantite
                med.stock -= quantite
                if med.stock < 0:
                    med.stock = 0
                controls_entry.save("clients", lst_client)
                controls_entry.save("medicaments", medicaments.lst_medic)

