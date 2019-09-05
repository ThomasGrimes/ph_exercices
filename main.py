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
try:controls_entry.load_data("data/clients.data")
except EOFError:
    pass

# --------------------------------------------------- WINDOWS ---------------------------------------------------

# fenetre nouveau client

def win_new_client():
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

# --------------------------------------------------- FONCTIONS ---------------------------------------------------

# Fonction de définition d'un nouveau client

def nouveau_client():
    nom = new_client_name_entry.get()
    credit = new_client_credit_entry.get()
    try:
        credit = float(credit)
        nom = nom.lower()

        ok = controls_entry.verif_name(nom)
        assert  ok == True
        client = clients.Clients(nom, credit)
        clients.lst_client.append(client)
        controls_entry.log(f"{client.name} : {client.credits}")
        client.save()
        var_message.set(f"Le client {client.name} a bien été créé. Son crédit est de {client.credits}")
    except ValueError:
        messagebox.showerror(title="Erreur", message="Valeur invalide")
    except AssertionError:
        messagebox.showwarning(title="Alerte", message="Le client existe deja !")
        controls_entry.log(f"{nom} existe deja")
    finally:
        new_client_name_entry.delete(0, tkinter.END)
        new_client_credit_entry.delete(0, tkinter.END)

# Fonction d'inventaire client

def inv_client():
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

# --------------------------------------------------- MAIN CODE ---------------------------------------------------

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