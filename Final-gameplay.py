from Game import *
from Player import *
import pickle

NB_BATON = 15

jeu = Game(NB_BATON)

# Nom du joueur (l'humain)
playerName = input('Entrez votre nom : \n')

# Mode de jeu (easy, medium, hard)
gameMode=""
while (gameMode != "easy") and (gameMode != "medium") and (gameMode != "hard"):
    gameMode = input('Choisir la difficulté (easy, medium, hard) : \n')

# Instanciation des joueurs
human = HumanPlayer(playerName)
machine = CPUPlayer("La Machine", gameMode, NB_BATON)

#si le mode du jeu est 'hard' on récupère notre réseau de neurones enregistré dans un fichier
if (gameMode=="hard"):
    # On donne à l'utilisateur de choisir entre les 2 fichiers existants
    print("choisir l'un des fichiers suivants (1/2)\n")
    print("1-> reseau.nnw")
    print("2-> reseau_amelioreAgregat.nnw")
    choix=input("")
    while choix not in ['1','2']:
        choix = input("entrée invalide !\n")

    if choix=="1":
        file="reseau.nnw"
    else:
         file="reseau_amelioreAgregat.nnw"
    machine.netw = pickle.load(open(file, "rb"))

#On donne la main à l'utilisateur pour choisir s'il commence en premier ou pas
premier=input("Voulez-vous commencer (O/N) ?\n")
while premier not in ['O','N']:
    premier= input("Tapez 'O' pour dire Oui et 'N'pour dire Non\n")

# Début du jeu
if premier == "O": # L'utilisateur commence en premier
    jeu.start(human, machine, True)
else: # La machine commence en premier
    jeu.start(machine, human, True)
