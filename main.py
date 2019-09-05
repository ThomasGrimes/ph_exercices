#coding:utf-8

"""
Programme de gestion d'une Pharmacie :
Données clients     : Nom - Crédits du - médicaments acheter - nb de medciaments achetés
Données médicaments : Nom - prix - stocks

"""
# --------------------------------------------------- MODULES ---------------------------------------------------

import tkinter
from tkinter import messagebox
#import des modules customs
import clients
import medicaments
import controls_entry

# --------------------------------------------------- LOAD DATA ---------------------------------------------------
try:
    controls_entry.load_data("data/clients.data")
    controls_entry.load_data("data/medicaments.data")
except EOFError:
    pass

# --------------------------------------------------- WINDOWS ---------------------------------------------------

def win_new_client():
"""
Fenetre tkinter de définission d'un nouveau client

"""
    # Fenetre
    win_nClient = tkinter.Toplevel(root)
    win_nClient.geometry(f"300x200+{posX}+{posY}")
    win_nClient.title("Nouveau Client")
    # Widgets
    new_client_name_label = tkinter.Label(win_nClient, text="Entrer le nom du client ")
    global new_client_name_entry
    new_client_name_entry = tkinter.Entry(win_nClient)
    new_client_credit_label = tkinter.Label(win_nClient, text="Entrer le crédit du client ")
    global new_client_credit_entry
    new_client_credit_entry = tkinter.Entry(win_nClient)
    new_client_valid = tkinter.Button(win_nClient, text="Valider", command=nouveau_client)
    new_client_quit = tkinter.Button(win_nClient, text="Annuler", command=win_nClient.destroy)
    # Positionnement
    new_client_name_label.pack()
    new_client_name_entry.pack()
    new_client_credit_label.pack()
    new_client_credit_entry.pack()
    new_client_valid.pack()
    new_client_quit.pack()

def win_new_medicament():
"""
Fenetre de définission d'un nouveau medicament

"""
    # Fenetre
    win_nMedoc = tkinter.Toplevel(root)
    win_nMedoc.geometry(f"300x200+{posX}+{posY}")
    win_nMedoc.title("Nouveau medicament")
    # Widgets
    new_medoc_name_label = tkinter.Label(win_nMedoc, text="Entrer le nom du medicament ")
    global new_medoc_name_entry
    new_medoc_name_entry = tkinter.Entry(win_nMedoc)
    new_medoc_price_label = tkinter.Label(win_nMedoc, text="Entrer le prix unitaire du medicament ")
    global new_medoc_price_entry
    new_medoc_price_entry = tkinter.Entry(win_nMedoc)
    new_medoc_quantity_label = tkinter.Label(win_nMedoc, text="Entrer la quantité")
    global new_medoc_quantity_entry
    new_medoc_quantity_entry = tkinter.Entry(win_nMedoc)
    new_medoc_valid = tkinter.Button(win_nMedoc, text="Valider", command=nouveau_medoc)
    new_medoc_quit = tkinter.Button(win_nMedoc, text="Annuler", command=win_nMedoc.destroy)
    # Positionnement
    new_medoc_name_label.pack()
    new_medoc_name_entry.pack()
    new_medoc_price_label.pack()
    new_medoc_price_entry.pack()
    new_medoc_quantity_label.pack()
    new_medoc_quantity_entry.pack()
    new_medoc_valid.pack()
    new_medoc_quit.pack()


# --------------------------------------------------- FONCTIONS ---------------------------------------------------

def nouveau_client():
"""
Fonction de création d'un nouveau client :

     - Recupère les Entry "new_client_name_entry" & "new_client_credit_entry"
     - Lance un block try pour vérification
     - Envoi le nom en controle pour vérification de la non existence du client
     - Ajout le client a la liste
     - Renseigne les logs du traitement Ok ou Erreur
     - Lance la fonction de sauvegarde dans le fichier clients.data en byte
     - Fini en vidant les champs
"""
    nom = new_client_name_entry.get()
    credit = new_client_credit_entry.get()
    try:
        credit = float(credit)
        nom = nom.lower()

        ok = controls_entry.verif_name(nom, clients.lst_client)
        assert  ok == True
        client = clients.Clients(nom, credit)
        clients.lst_client.append(client)
        controls_entry.log(f"{client.name} : {client.credits}")
        controls_entry.save("clients", clients.lst_client)
        var_message.set(f"Le client {client.name} a bien été créé. Son crédit est de {client.credits}")
    except ValueError:
        messagebox.showerror(title="Erreur", message="Valeur invalide")
    except AssertionError:
        messagebox.showwarning(title="Alerte", message="Le client existe deja !")
        controls_entry.log(f"ERREUR : {nom} existe deja")
    finally:
        new_client_name_entry.delete(0, tkinter.END)
        new_client_credit_entry.delete(0, tkinter.END)

def nouveau_medoc():
"""
Fonction de création d'un nouveau medicament :

     - Recupère les Entry "new_medoc_name_entry", "new_medoc_quantity_entry" & "new_medoc_price_entry"
     - Lance un block try pour vérification avec des raise pour la vérification de la bonne valeur du prix et stock
     - Envoi le nom en controle pour vérification de la non existence du medicament
     - Ajout le medicament a la liste
     - Renseigne les logs du traitement Ok ou Erreur
     - Lance la fonction de sauvegarde dans le fichier medicaments.data en byte
     - Fini en vidant les champs

"""
    nom = new_medoc_name_entry.get()
    price = new_medoc_price_entry.get()
    stock = new_medoc_quantity_entry.get()

    try:
        price = float(price)
        stock = int(stock)
        nom = nom.lower()
        if stock < 0:
            raise ValueError
        if price < 0:
            raise TypeError

        ok = controls_entry.verif_name(nom, medicaments.lst_medic)
        assert  ok == True
        medoc = medicaments.Medicaments(nom, price, stock)
        medicaments.lst_medic.append(medoc)
        controls_entry.log(f"{medoc.name} :  prix - {medoc.price} / stock - {medoc.stock}")
        controls_entry.save("medicaments", medicaments.lst_medic)
        var_message.set(f"Le medicament \"{medoc.name}\" a bien été créé. Son stock est de {medoc.stock} au prix unitaire de {medoc.price}")
    except ValueError:
        messagebox.showerror(title="Erreur", message="La valeur du stock ne peut être négative")
    except TypeError:
        messagebox.showwarning(title="Alerte", message="Le prix ne peut être a négatif")
    except AssertionError:
        messagebox.showwarning(title="Alerte", message="Le medicament existe deja !")
        controls_entry.log(f"ERREUR : {nom} existe deja")
    finally:
        new_medoc_name_entry.delete(0, tkinter.END)
        new_medoc_price_entry.delete(0, tkinter.END)
        new_medoc_quantity_entry.delete(0, tkinter.END)

def inv_client():
"""
Fonction inventoriant le(s) client(s) et renvoyant l'information dans la console


    - Si le champ est vide : Tous les clients sont renvoyés dans la console
    - Si le champ est remplit :

        - Vérifie que le client existe
        - Renvoi dans la console le client mentionné uniquement

"""
    entry_name_client = inv_entry.get()
    if entry_name_client != "":
        ok = controls_entry.verif_name(entry_name_client)
        if ok == False:
            for client in clients.lst_client:
                if client.name == entry_name_client:
                    var_message.set(f"Le client {client.name} possède un crédit de {client.credits}")
        else:
            var_message.set(f"le client {entry_name_client} n'existe pas")
    else:
        var_transit = ""
        for client in clients.lst_client:
            var_transit += f"Le client {client.name} possède un crédit de {client.credits}\n"
        var_message.set(var_transit)

# --------------------------------------------------- MAIN WINDOW ---------------------------------------------------

root = tkinter.Tk()
root.title("Pharma Gestion")

# Definissions de la dimension et du centrage de la fenetre

screen_x = root.winfo_screenwidth()
screen_y = root.winfo_screenheight()
windows_x = 800
windows_y = 400
posX = (screen_x // 2 )-(windows_x //2)
posY = (screen_y // 2)-(windows_y // 2)
center = f"{windows_x}x{windows_y}+{posX}+{posY}"
root.geometry(center)

# Frame Console

console_frame = tkinter.LabelFrame(root, text="Console", labelanchor="n", bg="white")
console_frame.pack(side="bottom", expand=True, padx=15, pady=15, ipadx=5, ipady=5, fill="both")

# Bouton pour création nouveau client

new_client = tkinter.Button(root, text="Nouveau client", command = win_new_client)
new_client.pack()

# Bouton pour création nouveau medicaments

new_medoc = tkinter.Button(root, text="Nouveau medicaments", command = win_new_medicament)
new_medoc.pack()

# listing client et crédit d'un ou tout les clients

inv_client = tkinter.Button(root, text="client", command=inv_client)
inv_entry = tkinter.Entry(root)
inv_client.pack(side="left")
inv_entry.pack(side="left")

# Console

var_message = tkinter.StringVar()
console = tkinter.Message(console_frame, textvariable=var_message, bg="white", fg="red", width=500)
var_message.trace("w", nouveau_client)
console.pack(expand=True)

root.mainloop()