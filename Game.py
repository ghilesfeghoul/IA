# Inutile de modifier cette classe normalement
import pickle


class Game:
    def __init__(self, nbr_batons):
        self.batons = nbr_batons

    def start(self, Joueur1, Joueur2, verbose):
        if verbose: print("====Nouvelle partie====")
        batons = self.batons
        joueur_courant = Joueur1

        while batons > 0:
            if verbose: print("Batons restants:", batons)
            n = joueur_courant.play(batons)
            if n < 1 or n > 3: print("Erreur : vous devez prendre au moins un baton au minimum et 3 au maximum !")
            if verbose: print(joueur_courant.getName(), " a pris", n," baton(s)")
            batons -= n
            if joueur_courant == Joueur1:
                joueur_courant = Joueur2
            else:
                joueur_courant = Joueur1

        if verbose: print(joueur_courant.getName(), " a gagné !")

        if Joueur1 == joueur_courant:
            Joueur1.addWin()
            Joueur2.addLoss()
        else:
            Joueur1.addLoss()
            Joueur2.addWin()
