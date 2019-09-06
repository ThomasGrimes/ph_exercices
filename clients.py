#coding:utf-8

"""
Module de création de la classe Client

"""
import medicaments
import controls_entry

lst_client = []

class Clients:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits

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

