#!/usr/bin/python3
#coding:utf-8

import tkinter
from tkinter import messagebox
import random

def nb_au_hasard():
    nb = random.randint(1,50)
    var_label.set(f"Le nombre est aléatoire est {scale_nb.set(nb)}")

def scale_modif_nb(*args):
    var_label.set(f"Le nombre est {scale_nb.get()}")

def pop():
    result = messagebox.askyesno("Bonjour", "es tu sur de vouloir quitter ?")
    if result == True:
        mainapp.destroy()

def suppress_barre():
    block3.destroy()

def show_param():
    # Fenetre
    win_param = tkinter.Toplevel(mainapp)
    win_param.geometry(f"300x200+{posX}+{posY}")
    # Blocks
    win_param_blockTitre = tkinter.Frame(win_param)
    win_param_blockWidget = tkinter.Frame(win_param)
    # Wdigets
    win_param.title("Paramètres")
    win_param_lb = tkinter.Label(win_param ,text="PARAMETRES")
    win_param_rd_btn0 = tkinter.Radiobutton(win_param ,text="Oui", value=0)
    win_param_rd_btn1 = tkinter.Radiobutton(win_param ,text="Non", value=1)
    # Disposition
    win_param_blockTitre.pack()
    win_param_blockWidget.pack()
    win_param_lb.grid()
    win_param_rd_btn0.pack()
    win_param_rd_btn1.pack()


mainapp = tkinter.Tk()

screen_x = mainapp.winfo_screenwidth()
screen_y = mainapp.winfo_screenheight()
windows_x = 800
windows_y = 250
posX = (screen_x // 2 )-(windows_x //2)
posY = (screen_y // 2)-(windows_y // 2)
center = f"{windows_x}x{windows_y}+{posX}+{posY}"
mainapp.geometry(center)

#mainapp.resizable(False, False)

mainapp.title("Mon programme fenêtre")

titre_fenetre = tkinter.Label(mainapp, text="Hello World !", fg="green")
titre_fenetre.grid()
message_fenetre = tkinter.Message(mainapp, text="Bienvenue sur mon programme", width=300, fg="red", bg="white")
message_fenetre.grid()

main_menu = tkinter.Menu(mainapp)

menu1 = tkinter.Menu(main_menu, tearoff=0)
menu1.add_command(label="Ouvrir")
menu1.add_command(label="Enregistrer")
menu1.add_command(label="Enregistrer sous")
menu1.add_separator()
menu1.add_command(label="Quitter", command=mainapp.quit)

menu2 = tkinter.Menu(main_menu, tearoff=0)
menu2.add_command(label="Paramètres", command=show_param)
menu2.add_command(label="Editer")

main_menu.add_cascade(label="Ficher", menu=menu1)
main_menu.add_cascade(label="Edition", menu=menu2)

block1=tkinter.Frame(mainapp, bg="blue")
block1.grid()

block2=tkinter.Frame(mainapp,bg="cyan")
block2.grid()

block3=tkinter.Frame(mainapp)
block3.grid()

button_ok = tkinter.Button(block1, text="Ok", command=nb_au_hasard)
button_ok.grid(padx=5, pady=5, ipadx=10, ipady=5)

button_quit = tkinter.Button(block1, text="Quit", command=pop)
button_quit.grid(column=1, row=0 ,padx=5, pady=5, ipadx=10, ipady=5)

var_label = tkinter.StringVar()
label_rep= tkinter.Label(block2, textvariable = var_label,bg="White", fg="red")
label_rep.grid(padx=5, pady=5, ipadx=10, ipady=5)


var_label.trace("w", scale_modif_nb)
scale_nb = tkinter.Scale(block3, from_=0, to=50, orient="horizontal", length=500, tickinterval=5, variable=var_label)
scale_nb.grid(padx=5, pady=5)

suppress_button = tkinter.Button(block3, text="Supprimer la barre", command=suppress_barre)
suppress_button.grid()

mainapp.config(menu=main_menu)
mainapp.mainloop()