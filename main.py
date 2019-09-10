#coding:utf-8

"""
Programme de gestion d'une Pharmacie :
Données clients     : Nom - Crédits du - médicaments acheter - nb de medciaments achetés
Données médicaments : Nom - prix - stocks

"""
# --------------------------------------------------- MODULES ---------------------------------------------------

import tkinter
from tkinter import messagebox
from tkinter import ttk
#import des modules customs
import clients
import medicaments
import controls_entry

# --------------------------------------------------- LOAD DATA ---------------------------------------------------
try:
    controls_entry.load_data("data/clients.data", clients.lst_client)
    controls_entry.load_data("data/medicaments.data", medicaments.lst_medic)
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
    new_client_quit = tkinter.Button(win_nClient, text="Quitter", command=win_nClient.destroy)
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
    new_medoc_quit = tkinter.Button(win_nMedoc, text="Quitter", command=win_nMedoc.destroy)
    # Positionnement
    new_medoc_name_label.pack()
    new_medoc_name_entry.pack()
    new_medoc_price_label.pack()
    new_medoc_price_entry.pack()
    new_medoc_quantity_label.pack()
    new_medoc_quantity_entry.pack()
    new_medoc_valid.pack()
    new_medoc_quit.pack()

def win_buy():
    """
    Fenetre pour l'achat

    """
    # Fenetre
    win_buy = tkinter.Toplevel(root)
    win_buy.geometry(f"300x200+{posX}+{posY}")
    win_buy.title("Achat")
    # Widgets
    win_buy_name_client_label = tkinter.Label(win_buy, text="Selectionner le nom du client")
    win_buy_name_medoc_label = tkinter.Label(win_buy, text="Selectionner le nom du medicament")
    win_buy_quantity_medoc_label = tkinter.Label(win_buy, text="Entrer la quantité")
    global win_buy_name_client_cbbox
    win_buy_lst_client_name = []
    for client in clients.lst_client:
        win_buy_lst_client_name.append(client.name.capitalize())
    win_buy_name_client_cbbox = ttk.Combobox(win_buy, value=win_buy_lst_client_name)
    global win_buy_name_medoc_cbbox
    win_buy_lst_medoc_name = []
    for medoc in medicaments.lst_medic:
        win_buy_lst_medoc_name.append(medoc.name.capitalize())
    win_buy_name_medoc_cbbox = ttk.Combobox(win_buy, value=win_buy_lst_medoc_name)
    global win_buy_quantity_medoc_entry
    win_buy_quantity_medoc_entry = tkinter.Entry(win_buy)
    win_buy_valid = tkinter.Button(win_buy, text="Valider", command=buy_medoc)
    win_buy_quit = tkinter.Button(win_buy, text="Quitter", command=win_buy.destroy)
    # Positionnement
    win_buy_name_client_label.pack()
    win_buy_name_client_cbbox.pack()
    win_buy_name_medoc_label.pack()
    win_buy_name_medoc_cbbox.pack()
    win_buy_quantity_medoc_label.pack()
    win_buy_quantity_medoc_entry.pack()
    win_buy_valid.pack()
    win_buy_quit.pack()

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
        assert ok == False
        client = clients.Clients(nom, credit)
        clients.lst_client.append(client)
        controls_entry.log(f"ENREGISTREMENT OK : {client.name} : {client.credits}")
        controls_entry.save("clients", clients.lst_client)
        var_text.set(f"Le client {client.name} a bien été créé. Son crédit est de {client.credits}€")
    except ValueError:
        messagebox.showerror(title="Erreur", message="Valeur invalide")
        controls_entry.log(f"ERREUR : {credit} la valeur entré n'est pas valide")
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
        assert  ok == False
        medoc = medicaments.Medicaments(nom, price, stock)
        medicaments.lst_medic.append(medoc)
        controls_entry.log(f"ENREGISTREMENT OK : {medoc.name.capitalize()} :  prix - {medoc.price} / stock - {medoc.stock}")
        controls_entry.save("medicaments", medicaments.lst_medic)
        var_text.set(f"Le medicament \"{medoc.name.capitalize()}\" a bien été créé. Son stock est de {medoc.stock} au prix unitaire de {medoc.price}€")
    except ValueError:
        messagebox.showerror(title="Erreur", message="La valeur du stock ne peut être négative")
        controls_entry.log(f"ERREUR : {stock} - La valeur ne peut pas être négative")
    except TypeError:
        messagebox.showwarning(title="Alerte", message="Le prix ne peut être a négatif")
        controls_entry.log(f"ERREUR : {price} - La valeur ne peut pas être négative")
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
    entry_search = inv_entry.get()
    if entry_search != "":
        ok_client, client = controls_entry.verif_name(entry_search, clients.lst_client)
        ok_medoc, medoc = controls_entry.verif_name(entry_search, medicaments.lst_medic)
        if ok_client:
            var_text.set(f"Le client {client.name.capitalize()} possède un crédit de {client.credits}€")
            controls_entry.log(f"OK : Le client {client.name.capitalize()} possède un crédit de {client.credits}€")
        elif ok_medoc:
            var_text.set(f"{medoc.name.capitalize()} : le stock est de {medoc.stock} au prix unitaire de {medoc.price}€")
            controls_entry.log(f"OK : {medoc.name.capitalize()} : le stock est de {medoc.stock} au prix unitaire de {medoc.price}€")
        else:
            var_text.set(f"le client ou le medicaments \"{entry_search}\" n'existe pas")
            controls_entry.log(f"ERREUR : le client ou le medicaments \"{entry_search}\" n'existe pas")
    else:
        var_transit = ""
        var_transit += f"\n------------------------ Clients -----------------------\n\n"
        for client in clients.lst_client:
            var_transit += f"Le client {client.name.capitalize()} possède un crédit de {client.credits}€\n"
        var_transit += f"\n---------------------- Medicaments ---------------------\n\n"
        for medoc in medicaments.lst_medic:
            var_transit += f"{medoc.name.capitalize()} : le stock est de {medoc.stock} au prix unitaire de {medoc.price}€\n"
        var_text.set(var_transit)
        controls_entry.log("OK : Inventaire OK")

def buy_medoc():
    """Fonction d'activation d'achat

        Recupère les valeurs "entry" du formulaire
        Controle avec block try
        2nd controle avec la fonction verif_name du module controls_entry afin de vérifier l'existence des noms fournit (Clients & Medicaments)
        log des evenements et retour console utilisateur

        Execute la méthode "achat" de la classe Clients.

    """
    medoc_name = win_buy_name_medoc_cbbox.get()
    client_name = win_buy_name_client_cbbox.get()
    medoc_quantity = win_buy_quantity_medoc_entry.get()

    try:
        medoc_quantity = int(medoc_quantity)

        assert medoc_quantity > 0
        ok , client = controls_entry.verif_name(client_name, clients.lst_client)
        old_credit = client.credits
        client.achat(medoc_name, medoc_quantity)
        var_text.set(f"Achat effectué : {client_name.capitalize()} a acheté {medoc_quantity} boîte(s) de {medoc_name.capitalize()}. \nLe nouveau solde client est de {client.credits}€")
        controls_entry.log(f"OK : {client_name.capitalize()} a acheté {medoc_quantity} de {medoc_name.capitalize()}\nAncien solde : {old_credit}\nNouveau solde : {client.credits}")
    except ValueError:
        messagebox.showerror(title="Erreur", message="Valeur invalide")
        controls_entry.log(f"ERREUR : Valeur invalide")
    except AssertionError:
        messagebox.showerror(title="Valeur invalide", message="La quantité doit être supérieur a 0")
        controls_entry.log(f"ERREUR : \"{medoc_quantity}\" doit être supérieur a 0")
    finally:
        win_buy_name_medoc_cbbox.delete(0, tkinter.END)
        win_buy_name_client_cbbox.delete(0, tkinter.END)
        win_buy_quantity_medoc_entry.delete(0, tkinter.END)


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

# Bouton achat

buy = tkinter.Button(root, text="Achat", command=win_buy)
buy.pack()

# listing client et crédit d'un ou tout les clients

inv_button = tkinter.Button(root, text="Recherche", command=inv_client)
inv_entry = tkinter.Entry(root)
inv_label = tkinter.Label(root, text="*Inventaire complet si le champ est vide")
inv_button.pack(side="left")
inv_entry.pack(side="left")
inv_label.pack(side="left")

# Console

var_text = tkinter.StringVar()
console = tkinter.Message(console_frame, textvariable=var_text, bg="white", fg="red", width=500)
var_text.trace("w", nouveau_client)
console.pack(expand=True)

root.mainloop()