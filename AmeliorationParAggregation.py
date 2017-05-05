from Game import *
from Player import *

jeu = Game(15)
player1 = CPUPlayer("La Machine 1", "hard", 15)
player2 = CPUPlayer("La Machine 2", "hard", 15)
player3 = CPUPlayer("La Machine 3", "hard", 15)
player4 = CPUPlayer("La Machine 4", "medium", 15)

NB_PARTIES = 100000

for i in range(1, NB_PARTIES+ 1):
    jeu.start(player1, player2, False)
    jeu.start(player4,player3,False)

print(str(player1.getName()) + " : " + str(player1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(player2.getName()) + " : " + str(player2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")


player1.getNeuronNetwork().agregatTousNeurons(player4.netw)
player1.getNeuronNetwork().printAllConnections()

# Enregistrement du réseau de neurone
with open('reseau_amelioreAgregat.nnw', 'wb') as output:
    pickle.dump(player1.getNeuronNetwork(), output, pickle.HIGHEST_PROTOCOL)
