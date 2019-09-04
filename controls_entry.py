#coding:utf-8

"""
Module de controles des entrées utilisateurs

"""
import datetime
import clients
from tkinter import messagebox

# Enregistrement des logs

def log(record):
    log_time = datetime.datetime.now()
    with open("data/log.txt", "a") as file:
        file.write(f"{log_time} >>> {record}\n")

def verif_name(name):
    for obj in clients.lst_client:
        name = name.lower()
        if name == obj.name:
            log(f"{name} existe deja")
            messagebox.showwarning(title="Alerte", message="Le client existe deja !")
            return False
        else:
            return True


def lireClient(client):
    pass
# Vérifie l'existance du client dans la base

def lireMedicament(medoc):
    pass
# Vérifie que le nom du medicaments existe et control sa quantitée

