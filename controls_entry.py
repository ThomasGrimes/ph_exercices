#coding:utf-8

"""
Module de controles des entrées utilisateurs

"""
import datetime
import clients
import pickle

# Enregistrement des logs

def log(record):
    log_time = datetime.datetime.now()
    with open("data/log.txt", "a") as file:
        file.write(f"{log_time} >>> {record}\n")

# Vérification de l'existance du client
def verif_name(name):
    ok = True
    for obj in clients.lst_client:
        if name == obj.name:
            ok = False
    return ok

# Chargement du fichier client

def load_data(directory_file):
    with open(f"{directory_file}", "rb") as file:
        datas = pickle.Unpickler(file).load()
        print(datas)
        for obj in datas:
            clients.lst_client.append(obj)

def lireClient(client):
    pass
# Vérifie l'existance du client dans la base

def lireMedicament(medoc):
    pass
# Vérifie que le nom du medicaments existe et control sa quantitée

