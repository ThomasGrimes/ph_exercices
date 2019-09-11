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
        controls_entry.log(f"INFO : Le nouveau nom du client {self._name} est {new_name}")
        self._name = new_name.lower()

    def _getCredits(self):
        var = str(self._credits)
        var += "€"
        return var

    def _setCredits(self, add_credits):
        if add_credits > 0:
            self._credits += add_credits
            controls_entry.log(f"INFO : Le nouveau crédit du client {self._name} est de {self._credits}")

    name = property(_getName, _setName)
    credits = property(_getCredits, _setCredits)

# definit l'achat du medicament avec la quantite a soustraire et le prix a ajouter au credit du client
    def achat(self, medoc, quantite):
        ok = 0
        for med in medicaments.lst_medic:
            if med.name == medoc:
                if med.stock == 0:
                    controls_entry.log("ERREUR : Il n'y a plus de medicament en stock")
                    ok = 2
                    return ok
                elif med.stock < quantite:
                    controls_entry.log("ERREUR : La quantité demandé n'est pas disponible")
                    ok = 1
                    return ok
                else:
                    price = int(med._price)
                    self._credits -= price*quantite
                    med._stock -= quantite
                controls_entry.save("clients", lst_client)
                controls_entry.save("medicaments", medicaments.lst_medic)

