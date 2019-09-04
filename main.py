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


root.mainloop()