#coding:utf-8

"""
Programme de gestion d'une Pharmacie :
Données clients     : Nom - Crédits du - médicaments acheter - nb de medciaments achetés
Données médicaments : Nom - prix - stocks

"""
#TODO : Position graphique

# --------------------------------------------------- MODULES ---------------------------------------------------

import tkinter
from tkinter import messagebox
from tkinter import ttk
#import des modules customs
import clients, medicaments, controls_entry

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
    win_buy_name_client_cbbox = ttk.Combobox(win_buy, value=lst_client_name)
    global win_buy_name_medoc_cbbox
    win_buy_name_medoc_cbbox = ttk.Combobox(win_buy, value=lst_medoc_name)
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

def win_edit_client():
    """
    Fenetre d'edition d'un obj Clients

    """
    #Fenetre
    win_edit_client = tkinter.Toplevel(root)
    win_edit_client.geometry(f"300x300+{posX}+{posY}")
    win_edit_client.title("Edition Client")
    # Widgets
    win_edit_client_old_name_label = tkinter.Label(win_edit_client, text="Selectionner le client a editer")
    win_edit_client_new_name_label = tkinter.Label(win_edit_client, text="Entrer le nouveau nom")
    win_edit_client_new_credit_label = tkinter.Label(win_edit_client, text="Entrer le crédit a ajouter au compte client")
    win_edit_client_suppress_label = tkinter.Label(win_edit_client, text="Supprimer le client selectionné")
    global win_edit_client_old_name_cbbox
    win_edit_client_old_name_cbbox = ttk.Combobox(win_edit_client, value=lst_client_name)
    global win_edit_client_new_name_entry
    win_edit_client_new_name_entry = tkinter.Entry(win_edit_client)
    global win_edit_client_new_credit_spinbx
    win_edit_client_new_credit_spinbx = tkinter.Spinbox(win_edit_client, from_=0, to=1000)
    win_edit_client_valid = tkinter.Button(win_edit_client, text="Valider", command=lambda:[fedit_client(), win_edit_client.destroy()])
    win_edit_client_quit = tkinter.Button(win_edit_client, text="Quitter", command=win_edit_client.destroy)
    win_edit_client_suppress = tkinter.Button(win_edit_client, text="Supprimer", command=lambda:[suppress(win_edit_client_old_name_cbbox.get()), win_edit_client.destroy()])
    # Positionnement
    win_edit_client_old_name_label.pack()
    win_edit_client_old_name_cbbox.pack()
    win_edit_client_new_name_label.pack()
    win_edit_client_new_name_entry.pack()
    win_edit_client_new_credit_label.pack()
    win_edit_client_new_credit_spinbx.pack()
    win_edit_client_suppress_label.pack()
    win_edit_client_suppress.pack()
    win_edit_client_valid.pack()
    win_edit_client_quit.pack()

def win_edit_medoc():
    """
    Fenetre d'edition d'un obj Medicaments

    """
    #Fenetre
    win_edit_medoc = tkinter.Toplevel(root)
    win_edit_medoc.geometry(f"300x300+{posX}+{posY}")
    win_edit_medoc.title("Edition medicament")
    # Widgets
    win_edit_medoc_old_name_label = tkinter.Label(win_edit_medoc, text="Selectionner le medicament a editer")
    win_edit_medoc_new_name_label = tkinter.Label(win_edit_medoc, text="Entrer le nouveau nom")
    win_edit_medoc_new_credit_label = tkinter.Label(win_edit_medoc, text="Entrer le nouveau prix du medicament")
    win_edit_medoc_suppress_label = tkinter.Label(win_edit_medoc, text="Supprimer le medicament selectionné")
    global win_edit_medoc_old_name_cbbox
    win_edit_medoc_old_name_cbbox = ttk.Combobox(win_edit_medoc, value=lst_medoc_name)
    global win_edit_medoc_new_name_entry
    win_edit_medoc_new_name_entry = tkinter.Entry(win_edit_medoc)
    global win_edit_medoc_new_price_spinbx
    win_edit_medoc_new_price_spinbx = tkinter.Spinbox(win_edit_medoc, from_=0, to=1000)
    win_edit_medoc_valid = tkinter.Button(win_edit_medoc, text="Valider", command=lambda:[fedit_medoc(), win_edit_medoc.destroy()])
    win_edit_medoc_quit = tkinter.Button(win_edit_medoc, text="Quitter", command=win_edit_medoc.destroy)
    win_edit_medoc_suppress = tkinter.Button(win_edit_medoc, text="Supprimer", command=lambda:[suppress(win_edit_medoc_old_name_cbbox.get()), win_edit_medoc.destroy()])
    # Positionnement
    win_edit_medoc_old_name_label.pack()
    win_edit_medoc_old_name_cbbox.pack()
    win_edit_medoc_new_name_label.pack()
    win_edit_medoc_new_name_entry.pack()
    win_edit_medoc_new_credit_label.pack()
    win_edit_medoc_new_price_spinbx.pack()
    win_edit_medoc_suppress_label.pack()
    win_edit_medoc_suppress.pack()
    win_edit_medoc_valid.pack()
    win_edit_medoc_quit.pack()

def win_add_stock():
    """
    Fenetre d'approvisionement du stock de medicament

    """
    # Fenetre
    win_add_stock = tkinter.Toplevel(root)
    win_add_stock.geometry(f"300x200+{posX}+{posY}")
    win_add_stock.title("Approvisionement medicament")
    # Widgets
    win_add_stock_medoc_label = tkinter.Label(win_add_stock, text="Selectionner le medicament a approvisionner")
    win_add_stock_nb_label = tkinter.Label(win_add_stock, text="Indiquer la quantité a ajouter au stock")
    global win_add_stock_medoc_cbbox
    win_add_stock_medoc_cbbox = ttk.Combobox(win_add_stock, value=lst_medoc_name)
    global win_add_stock_nb_spbox
    win_add_stock_nb_spbox = tkinter.Spinbox(win_add_stock, from_= 0, to=100)
    win_add_stock_valid = tkinter.Button(win_add_stock, text="Valider", command=add_stock)
    win_add_stock_quit = tkinter.Button(win_add_stock, text="Quitter", command=win_add_stock.destroy)
    # Postionnement
    win_add_stock_medoc_label.pack()
    win_add_stock_medoc_cbbox.pack()
    win_add_stock_nb_label.pack()
    win_add_stock_nb_spbox.pack()
    win_add_stock_valid.pack()
    win_add_stock_quit.pack()
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

        ok, ko = controls_entry.verif_name(nom, clients.lst_client)
        assert ok == False
        client = clients.Clients(nom, credit)
        clients.lst_client.append(client)
        lst_client_name.append(client.name)
        controls_entry.log(f"ENREGISTREMENT OK : {client.name} : {client.credits}")
        controls_entry.save(*file_clients)
        var_text.set(f"Le client {client.name} a bien été créé. Son crédit est de {client.credits}")
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

        ok, ko = controls_entry.verif_name(nom, medicaments.lst_medic)
        assert  ok == False
        medoc = medicaments.Medicaments(nom, price, stock)
        medicaments.lst_medic.append(medoc)
        lst_medoc_name.append(medoc.name)
        controls_entry.log(f"ENREGISTREMENT OK : {medoc.name} :  prix - {medoc.price} / stock - {medoc.stock}")
        controls_entry.save(*file_medicaments)
        var_text.set(f"Le medicament \"{medoc.name}\" a bien été créé. Son stock est de {medoc.stock} au prix unitaire de {medoc.price}")
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


        - Si le champ est vide : Tous les clients et leurs crédits sont renvoyés dans la console ainsi que tout les medicaments
            leurs stocks et leurs prix a l'unité
        - Si le champ est remplit :

            - Vérifie que le client ou le medicaments existe
            - Renvoi dans la console le client ou le medicament mentionné uniquement

    """
    entry_search = inv_entry.get()
    if entry_search != "":
        ok_client, client = controls_entry.verif_name(entry_search, clients.lst_client)
        ok_medoc, medoc = controls_entry.verif_name(entry_search, medicaments.lst_medic)
        if ok_client:
            var_text.set(f"Le client {client.name} possède un crédit de {client.credits}")
            controls_entry.log(f"OK : Le client {client.name} possède un crédit de {client.credits}")
        elif ok_medoc:
            var_text.set(f"{medoc.name} : le stock est de {medoc.stock} au prix unitaire de {medoc.price}")
            controls_entry.log(f"OK : {medoc.name} : le stock est de {medoc.stock} au prix unitaire de {medoc.price}")
        else:
            var_text.set(f"le client ou le medicaments \"{entry_search}\" n'existe pas")
            controls_entry.log(f"ERREUR : le client ou le medicaments \"{entry_search}\" n'existe pas")
    else:
        var_transit = ""
        var_transit += f"\n------------------------ Clients -----------------------\n\n"
        for client in clients.lst_client:
            var_transit += f"Le client {client.name} possède un crédit de {client.credits}\n"
        var_transit += f"\n---------------------- Medicaments ---------------------\n\n"
        for medoc in medicaments.lst_medic:
            var_transit += f"{medoc.name} : le stock est de {medoc.stock} au prix unitaire de {medoc.price}\n"
        var_text.set(var_transit)
        controls_entry.log("OK : Inventaire OK")


def buy_medoc():
    """Fonction d'activation d'achat

        Recupère les valeurs "Combobox" & "entry" du formulaire
        Controle avec block try la valeur "Quantity"
        log des evenements et retour console utilisateur
        Execute la fonction vérif name avec retour de l'obj client si trouvé
        Execute la méthode "achat" de la classe Clients.

    """
    #TODO : Historique d'achat
    medoc_name = win_buy_name_medoc_cbbox.get()
    client_name = win_buy_name_client_cbbox.get()
    medoc_quantity = win_buy_quantity_medoc_entry.get()
    try:
        medoc_quantity = int(medoc_quantity)

        assert medoc_quantity > 0
        ok , client = controls_entry.verif_name(client_name, clients.lst_client)
        old_credit = client.credits
        ok = client.achat(medoc_name, medoc_quantity)
        if ok == 2:
            var_text.set("ERREUR : Il n'y a plus de medicament en stock")
        elif ok == 1:
            var_text.set("ERREUR : La quantité demandé n'est pas disponible")
        else:
            var_text.set(f"Achat effectué : {client.name} a acheté {medoc_quantity} boîte(s) de {medoc_name}. \nLe nouveau solde client est de {client.credits}")
            controls_entry.log(f"OK : {client.name} a acheté {medoc_quantity} de {medoc_name}\n   Ancien solde : {old_credit}€\n   Nouveau solde : {client.credits}")
    except ValueError:
        messagebox.showerror(title="Erreur", message="Valeur quantité invalide")
        controls_entry.log(f"ERREUR : Valeur invalide")
    except AssertionError:
        messagebox.showerror(title="Valeur invalide", message="La quantité doit être supérieur a 0")
        controls_entry.log(f"ERREUR : \"{medoc_quantity}\" doit être supérieur a 0")
    finally:
        win_buy_name_medoc_cbbox.delete(0, tkinter.END)
        win_buy_name_client_cbbox.delete(0, tkinter.END)
        win_buy_quantity_medoc_entry.delete(0, tkinter.END)


def fedit_client():
    """Fonction d'edition client

        Permet d'editer le nom du client via un champs "entry" et créditer son compte
        Selectionne le nom du client a modifier via une combobox et la lst lst_client_name généré au début de programme
        Actualise le nom de l'objet dans la liste clients.lst_client
        Modifie le nom dans la liste lst_client_name
            Pour le dynamisme de la liste Combobox, si le nom est modifié :
                - Ferme la fenêtre et la regénère
        Ajoute le montant choisit via le setter de la prop credit de l'obj client
        Sauvegarde et fait un retour console

    """
    old_name = win_edit_client_old_name_cbbox.get()
    new_name = win_edit_client_new_name_entry.get()
    new_credit = int(win_edit_client_new_credit_spinbx.get())
    ok, client = controls_entry.verif_name(old_name, clients.lst_client)
    var_transit = ""
    if new_name != "":
        client.name = new_name
        controls_entry.save(*file_clients)
        var_transit += f"Le client {old_name} a été renommé en {client.name}\n"
        ind = lst_client_name.index(old_name)
        lst_client_name[ind] = client.name
    if new_credit > 0:
        client.credits = new_credit
        var_transit += f"{new_credit}€ ont été ajouté au crédit du client {client.name}. Son nouveau solde est de {client.credits}"
    var_text.set(var_transit)
    win_edit_client()


def fedit_medoc():
    """Fonction d'edition d'un medicament

            Permet d'editer le nom du medoc via un champs "entry" et son prix
            Selectionne le nom du medoc a modifier via une combobox et la lst lst_medoc_name généré au début de programme
            Actualise le nom de l'objet dans la liste medicaments.lst_medic
            Modifie le nom dans la liste lst_medoc_name
                Pour le dynamisme de la liste Combobox, si le nom est modifié :
                    - Ferme la fenêtre et la regénère
            Modifie le prix unitaire
            Sauvegarde et fait un retour console

        """
    old_name = win_edit_medoc_old_name_cbbox.get()
    new_name = win_edit_medoc_new_name_entry.get()
    new_price = int(win_edit_medoc_new_price_spinbx.get())
    ok, medoc = controls_entry.verif_name(old_name, medicaments.lst_medic)
    var_transit = ""
    if new_name != "":
        medoc.name = new_name
        controls_entry.save(*file_medicaments)
        var_transit += f"Le medoc {old_name} a été renommé en {medoc.name}\n"
        ind = lst_medoc_name.index(old_name)
        lst_medoc_name[ind] = medoc.name
    if new_price > 0:
        medoc.price = new_price
        var_transit += f"Le montant unitaire du medicament {medoc.name} est dorénavant de {medoc.price}"
    var_text.set(var_transit)
    win_edit_medoc()


def add_stock():
    """"
    Fonction d'approvisionnement du stock d'un medicament

        Selectionner le medicaments a approvisionner
        Choisir la quantité a ajouté
        Utilise le setter de la prop stock de la classe Medicament

    """
    medoc_name = win_add_stock_medoc_cbbox.get()
    stock_add = int(win_add_stock_nb_spbox.get())

    ok, medoc = controls_entry.verif_name(medoc_name, medicaments.lst_medic)
    medoc.stock = stock_add
    controls_entry.save(*file_medicaments)
    var_text.set(f"Le stock de {medoc.name} est de {medoc.stock}")
    controls_entry.log(f"OK : Ajout de {stock_add} boite(s) de {medoc.name}. Nouveau stock : {medoc.stock}")
    win_add_stock_medoc_cbbox.delete(0, tkinter.END)
    win_add_stock_nb_spbox.delete(0, tkinter.END)


def suppress(obj_a_supp):
    valid = messagebox.askyesno(title="Supprimer", message="Êtes-vous sur de vouloir supprimer ?")
    if valid:
        ok_client, C_obj = controls_entry.verif_name(obj_a_supp, clients.lst_client)
        ok_medoc, M_obj = controls_entry.verif_name(obj_a_supp, medicaments.lst_medic)
        if ok_client:
            var_text.set(f"Le client {C_obj.name} à été supprimé")
            controls_entry.log((f"SUPPRESSION OK : Le client {C_obj.name} a été supprimé "))
            ind = lst_client_name.index(C_obj.name)
            lst_client_name.pop(ind)
            ind_Obj = clients.lst_client.index(C_obj)
            clients.lst_client.pop(ind_Obj)
            controls_entry.save(*file_clients)
            win_edit_client()
        elif ok_medoc:
            var_text.set(f"Le medicament {M_obj.name} à été supprimé")
            controls_entry.log(f"SUPPRESSION OK : Le medicament {M_obj.name} a été supprimé")
            ind = lst_medoc_name.index(M_obj.name)
            lst_medoc_name.pop(ind)
            indObj = medicaments.lst_medic.index(M_obj)
            medicaments.lst_medic.pop(indObj)
            controls_entry.save(*file_medicaments)
            win_edit_medoc()
        else:
            messagebox.showerror(title="ERREUR", message="La sélection est vide")


def quit():
    if messagebox.askyesno(title="Quitter", message="Êtes-vous sur de vouloir quitter"):
        root.quit()
# ----------------------------------------------------- MAIN ------------------------------------------------------

root = tkinter.Tk()
root.title("Pharma Gestion")

# --------------------------------------------------- LOAD DATA ---------------------------------------------------

file_medicaments = ("medicaments", medicaments.lst_medic)
file_clients = ("clients", clients.lst_client)

controls_entry.load_data(*file_clients)
controls_entry.load_data(*file_medicaments)

lst_medoc_name = []
for medoc in medicaments.lst_medic:
    lst_medoc_name.append(medoc.name)

lst_client_name = []
for client in clients.lst_client:
    lst_client_name.append(client.name)

# --------------------------------------------------- ROOT WINDOWS ---------------------------------------------------
# Definissions de la dimension et du centrage de la fenetre

screen_x = root.winfo_screenwidth()
screen_y = root.winfo_screenheight()
windows_x = 800
windows_y = 400
posX = (screen_x // 2 )-(windows_x //2)
posY = (screen_y // 2)-(windows_y // 2)
center = f"{windows_x}x{windows_y}+{posX}+{posY}"
root.geometry(center)

# Barre de Menu

main_menu = tkinter.Menu(root)

menu1 = tkinter.Menu(main_menu, tearoff=0)
menu1.add_command(label="Enregistrer", command=lambda:[controls_entry.save(*file_clients), controls_entry.save(*file_medicaments)])
menu1.add_separator()
menu1.add_command(label="Quitter", command=quit)

menu2 = tkinter.Menu(main_menu, tearoff=0)
menu2.add_command(label="Modifier client", command=win_edit_client)
menu2.add_command(label="Modifier medicament", command=win_edit_medoc)

menu3 = tkinter.Menu(main_menu, tearoff=0)
menu3.add_command(label="Client", command=win_new_client)
menu3.add_command(label="Medicament", command=win_new_medicament)

main_menu.add_cascade(label="Ficher", menu=menu1)
main_menu.add_cascade(label="Editer", menu=menu2)
main_menu.add_cascade(label="Nouveau", menu=menu3)

# Frame Console

console_frame = tkinter.LabelFrame(root, text="Console", labelanchor="n", bg="white")

# Bouton achat

buy = tkinter.Button(root, text="Achat", command=win_buy)
buy.pack()

# Approvisionnement
ajout_stock = tkinter.Button(root, text="Approvisionner stock medicament", command=win_add_stock)
ajout_stock.pack()

# listing client et crédit d'un ou tout les clients

inv_button = tkinter.Button(root, text="Recherche", command=inv_client)
inv_entry = tkinter.Entry(root)
inv_label = tkinter.Label(root, text="*Inventaire complet si le champ est vide")
inv_entry.pack()
inv_button.pack()
inv_label.pack()

# Console

var_text = tkinter.StringVar()
console = tkinter.Message(console_frame, textvariable=var_text, bg="white", fg="red", width=500)
var_text.trace("w", nouveau_client)
console.pack(expand=True)

# Bouton Quit

quit_button = tkinter.Button(root, text="Quitter", command=quit)
quit_button.pack(side="bottom", fill="x")

console_frame.pack(side="bottom", expand=True, padx=15, pady=15, ipadx=5, ipady=5, fill="both")

root.config(menu=main_menu)
root.mainloop()