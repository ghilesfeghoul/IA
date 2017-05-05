from Game import *
from Player import *

jeu = Game(15)
player1 = CPUPlayer("La Machine 1", "hard", 15)
player2 = CPUPlayer("La Machine 2", "hard", 15)

NB_PARTIES = 100000

for i in range(1, NB_PARTIES + 1):
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
