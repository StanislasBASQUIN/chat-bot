# Creation of Graphical Interface.

from tkinter import *
import datetime

# Construction Interface Graphique
root = Tk()

def envoi():
    envoi = "Client : " + e.get()
    txt.insert(END, "\n" + envoi)
    if 'Bonjour' in e.get():
        txt.insert(END, "\n" + "Bot : Bonjour Client")

    elif 'heure' in e.get():
        heure = datetime.datetime.now().strftime('%H:%M minutes')
        txt.insert(END, "\n" + "Bot : il est "+ heure)

    elif 'Nom' in e.get():
        txt.insert(END, "\n" + "Bot : Mon nom est Manu")

    elif 'appel' in e.get():
        txt.insert(END, "\n" + "Bot : Mon nom est Bot")

    else:
        txt.insert(END, "\n" + 'Bot : Désolé pouvez-vous répéter?')

    e.delete(0, END) # Efface le contenu dans Input



#Creation de la Grille
txt=Text(root)
txt.grid(row=0, column=0, columnspan=2)

# Saisie du message
# Entrée saisie par User.
e = Entry(root, width=100)

e.grid(row=1, column=0)
# Creation Bouton pour executer Entrée du User.
send = Button(root, text="Envoyer", command=envoi).grid(row=1, column=1)


root.title("Manu")
root.mainloop()