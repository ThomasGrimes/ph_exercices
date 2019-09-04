#coding:utf-8

"""
Programme de gestion d'une Pharmacie :
Données clients     : Nom - Crédits du - médicaments acheter - nb de medciaments achetés
Données médicaments : Nom - prix - stocks

"""

import tkinter
#import des modules customs
import clients
import medicaments
import controls_entry

# fenetre nouveau client

def win_new_client():
    # Fenetre
    win_nClient = tkinter.Toplevel(root)
    win_nClient.geometry(f"300x200+{posX}+{posY}")
    win_nClient.title("Nouveau Client")
    # Widgets
    new_client_name_label = tkinter.Label(win_nClient, text="Entrer le nom du client ")
    new_client_name_entry = tkinter.Entry(win_nClient)
    new_client_credit_label = tkinter.Label(win_nClient, text="Entrer le crédit du client ")
    new_client_credit_entry = tkinter.Entry(win_nClient)
    new_client_valid = tkinter.Button(win_nClient, text="Valider")
    new_client_quit = tkinter.Button(win_nClient, text="Annuler", command=win_nClient.destroy)
    #Positionnement
    new_client_name_label.pack()
    new_client_name_entry.pack()
    new_client_credit_label.pack()
    new_client_credit_entry.pack()
    new_client_valid.pack()
    new_client_quit.pack()


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

# Frame d'affichage des données

console_frame = tkinter.LabelFrame(root, text="Console", labelanchor="n")
console_frame.pack(side="bottom", padx=15, pady=15, ipadx=15, ipady=15, fill="x")

console = tkinter.Label(console_frame, text="test", bg="white", fg="red")
console.pack()

# Bouton pour création nouveau client

new_client = tkinter.Button(root, text="Nouveau client", command = win_new_client)
new_client.pack()

root.mainloop()