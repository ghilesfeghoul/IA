from Game import *
from Player import *
import pickle

NB_PARTIES = 50000

jeu = Game(15)

# ----------- EASY VS EASY -----------
machine1 = CPUPlayer("La Machine 1 Easy", "easy", 15)
machine2 = CPUPlayer("La Machine 2 Easy", "easy", 15)

for i in range(1, NB_PARTIES + 1):
    jeu.start(machine1, machine2, False)

print(str(machine1.getName()) + " : " + str(machine1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(machine2.getName()) + " : " + str(machine2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")

# ----------- EASY VS MEDIUM -----------
machine1 = CPUPlayer("La Machine 1 Easy", "easy", 15)
machine2 = CPUPlayer("La Machine 2 Medium", "medium", 15)

for j in range(1, NB_PARTIES + 1):
    jeu.start(machine1, machine2, False)

print(str(machine1.getName()) + " : " + str(machine1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(machine2.getName()) + " : " + str(machine2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")

# ----------- MEDIUM VS HARD -----------
machine1 = CPUPlayer("La Machine 1 Medium", "medium", 15)
machine2 = CPUPlayer("La Machine 2 Hard", "hard", 15)

for k in range(1, NB_PARTIES + 1):
    jeu.start(machine1, machine2, False)

print(str(machine1.getName()) + " : " + str(machine1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(machine2.getName()) + " : " + str(machine2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")

# ----------- EASY VS HARD -----------
machine1 = CPUPlayer("La Machine 1 Easy", "easy", 15)
machine2 = CPUPlayer("La Machine 2 Hard", "hard", 15)

for a in range(1, NB_PARTIES + 1):
    jeu.start(machine1, machine2, False)

print(str(machine1.getName()) + " : " + str(machine1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(machine2.getName()) + " : " + str(machine2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")

# ----------- MEDIUM VS MEDIUM -----------
machine1 = CPUPlayer("La Machine 1 Medium", "medium", 15)
machine2 = CPUPlayer("La Machine 2 Medium", "medium", 15)

for b in range(1, NB_PARTIES + 1):
    jeu.start(machine1, machine2, False)

print(str(machine1.getName()) + " : " + str(machine1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(machine2.getName()) + " : " + str(machine2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")

# ----------- HARD VS HARD -----------
machine1 = CPUPlayer("La Machine 1 Hard", "hard", 15)
machine2 = CPUPlayer("La Machine 2 Hard", "hard", 15)

for c in range(1, NB_PARTIES + 1):
    jeu.start(machine1, machine2, False)

print(str(machine1.getName()) + " : " + str(machine1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(machine2.getName()) + " : " + str(machine2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")

if machine1.getNbWin() > machine2.getNbWin():
    neurons = machine1.getNeuronNetwork()
else:
    neurons = machine2.getNeuronNetwork()

# Enregistrement du réseau de neurones
with open('reseau.nnw', 'wb') as output:
    pickle.dump(neurons, output, pickle.HIGHEST_PROTOCOL)
