from Game import *
from Player import *
import pickle

NB_BATON = 15

jeu = Game(NB_BATON)

# Nom du joueur (l'humain)
playerName = input('Entrez votre nom : \n')

# Mode de jeu (easy, medium, hard)
gameMode = ""
while (gameMode != "easy") and (gameMode != "medium") and (gameMode != "hard"):
    gameMode = input('Choisir la difficulté (easy, medium, hard) : \n')

# Instanciation des joueurs
human = HumanPlayer(playerName)
machine = CPUPlayer("La Machine", gameMode, NB_BATON)

if gameMode == "hard":
    with open('reseau', 'rb') as inp: ns = pickle.load(inp)
    machine.setNeuronNetwork(ns)

# Début du jeu
jeu.start(human, machine, True)
