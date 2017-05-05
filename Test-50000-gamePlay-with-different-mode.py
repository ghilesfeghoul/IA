from Game import *
from Player import *
import pickle

NB_PARTIES = 50000

jeu = Game(15)

# ----------- EASY VS EASY -----------
player1 = CPUPlayer("La Machine 1 Easy", "easy", 15)
player2 = CPUPlayer("La Machine 2 Easy", "easy", 15)

for i in range(1, NB_PARTIES + 1):
    jeu.start(player1, player2, False)

print(str(player1.getName()) + " : " + str(player1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(player2.getName()) + " : " + str(player2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")

# ----------- EASY VS MEDIUM -----------
player1 = CPUPlayer("La Machine 1 Easy", "easy", 15)
player2 = CPUPlayer("La Machine 2 Medium", "medium", 15)

for j in range(1, NB_PARTIES + 1):
    jeu.start(player1, player2, False)

print(str(player1.getName()) + " : " + str(player1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(player2.getName()) + " : " + str(player2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")

# ----------- MEDIUM VS HARD -----------
player1 = CPUPlayer("La Machine 1 Medium", "medium", 15)
player2 = CPUPlayer("La Machine 2 Hard", "hard", 15)

for k in range(1, NB_PARTIES + 1):
    jeu.start(player1, player2, False)

print(str(player1.getName()) + " : " + str(player1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(player2.getName()) + " : " + str(player2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")

# ----------- EASY VS HARD -----------
player1 = CPUPlayer("La Machine 1 Easy", "easy", 15)
player2 = CPUPlayer("La Machine 2 Hard", "hard", 15)

for a in range(1, NB_PARTIES + 1):
    jeu.start(player1, player2, False)

print(str(player1.getName()) + " : " + str(player1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(player2.getName()) + " : " + str(player2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")

# ----------- MEDIUM VS MEDIUM -----------
player1 = CPUPlayer("La Machine 1 Medium", "medium", 15)
player2 = CPUPlayer("La Machine 2 Medium", "medium", 15)

for b in range(1, NB_PARTIES + 1):
    jeu.start(player1, player2, False)

print(str(player1.getName()) + " : " + str(player1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(player2.getName()) + " : " + str(player2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")

# ----------- HARD VS HARD -----------
player1 = CPUPlayer("La Machine 1 Hard", "hard", 15)
player2 = CPUPlayer("La Machine 2 Hard", "hard", 15)

for c in range(1, NB_PARTIES + 1):
    jeu.start(player1, player2, False)

print(str(player1.getName()) + " : " + str(player1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(player2.getName()) + " : " + str(player2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")

if player1.getNbWin() > player2.getNbWin():
    neurons = player1.getNeuronNetwork()
else:
    neurons = player2.getNeuronNetwork()

# Enregistrement du réseau de neurones
with open('reseau', 'wb') as output:
    pickle.dump(neurons, output, pickle.HIGHEST_PROTOCOL)
