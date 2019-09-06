#coding:utf-8

"""
Module de controles des entrées utilisateurs

"""
import datetime
import clients
import pickle

def log(record):
    """
    Fonction d'enregistrement des logs

        Enregistre les actions et erreurs du programme avec le date/time

        Fichier sous "data/log.txt"

        Prend 1 paramètre :
            - l'action 'str'

    """
    log_time = datetime.datetime.now()
    with open("data/log.txt", "a") as file:
        file.write(f"{log_time} >>> {record}\n")

def verif_name(name, lst):
    """
    Fonction de vérification de la présence d'un nom client ou médicament dans la liste

        Prend 2 paramètres :
            - Le nom a chercher
            - la liste dans laquelle chercher
    """
    name = name.lower()
    ok = True
    for obj in lst:
        if name == obj.name:
            ok = False
    return ok

def load_data(directory_file, lst):
    """
    Fonctions de chargement des données enregistrées dans les fichiers .data en byte

        Elle remplit les listes avec les données sauvegardées

        Prend 1 paramètre :
            - Le chemin + nom du fichier (Ex : data/clients.data)

        Celle ci est appelé au début du programme

    """
    with open(f"{directory_file}", "rb") as file:
        datas = pickle.Unpickler(file).load()
        for obj in datas:
            lst.append(obj)

def save(file, backup_file):
    """
    Fonction de sauvegarde des données dans les fichiers "clients.data" & "medicaments.data"


        Prend en paramètres :
            - Le nom du fichier cible (Ex : "medicaments", intégrer les doubleQuotes)
            - La liste a sauvegarder ( Ex : clients.lst_clients)

        Celle ci est appelé dans les fonctions de création de nouveaux clients ou médicaments

    """
    cible = f"data/{file}.data"
    with open(cible, "wb") as backup:
        record = pickle.Pickler(backup)
        record.dump(backup_file)
