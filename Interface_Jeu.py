from tkinter import *
from Game import *
from Player import *


class Interface(Frame):
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=3000, height=1880, **kwargs)
        self.pack(fill=BOTH)

        global var_choix
        var_choix = StringVar()
        self.easy = Radiobutton(fenetre, text="Facile", variable=var_choix, value="easy")
        self.medium = Radiobutton(fenetre, text="Moyen", variable=var_choix, value="medium")
        self.hard = Radiobutton(fenetre, text="Difficile", variable=var_choix, value="hard")
        self.message_bienvenu = Label(self, text="Bienvenue au jeu de batons !")
        self.message_bienvenu.pack()
        self.message_guide = Label(self, text="Commencer une nouvelle partie ?")
        self.message_guide.pack()
        self.message = Label(self, text="Entrez votre nom :")
        self.message.pack()
        self.input = Entry(self)
        self.input.pack()
        self.bouton_cliquer = Button(self, text="Commencer la partie", fg="green", command=self.cliquer)
        self.bouton_cliquer.pack(side=BOTTOM)
        self.easy.pack()
        self.medium.pack()
        self.hard.pack()

    def cliquer(self):
        """Il y a eu un clic sur le bouton.
        On lance notre jeu."""
        try:
            if self.input.get() != "":
                human = HumanPlayer(self.input.get())
                cpu = CPUPlayer("La Machine", var_choix.get(), 15)
                self.input.destroy()
                self.bouton_cliquer["command"] = self.jouer(human, cpu)
        except:
            input("Vous devez fournir un nom !")

    def jouer(self, human, cpu):
        jeu = Game(15)
        jeu.start(human, cpu, True)
