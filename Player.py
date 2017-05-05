from Neuron import *


class Player:
    def __init__(self, name):
        self.name = name
        self.nbWin = 0

    def getName(self):
        return self.name

    def getNbWin(self):
        return self.nbWin

    def addWin(self):
        self.nbWin += 1

    def addLoss(self):
        pass


class HumanPlayer(Player):
    def play(self, batons_dispo):
        global nbr_batons_pris
        if batons_dispo == 1:
            return 1
        else:
            correct = False
            while not correct:
                nbr_batons_pris = input('Prenez des batons (entre 1 et 3)\n')
                try:
                    nbr_batons_pris = int(nbr_batons_pris)
                    if nbr_batons_pris >= 1 and nbr_batons_pris <= 3 and batons_dispo - nbr_batons_pris >= 0:
                        correct = True
                        print("\n")
                except:
                    input("Vous devez fournir un nombre compris entre 1 et 3 !")
            return nbr_batons_pris


class CPUPlayer(Player):
    def __init__(self, name, mode, batons_dispo):
        super().__init__(name)
        self.mode = mode
        self.netw = NeuronNetwork(3, batons_dispo)
        self.previousNeuron = None
        self.nbErreur = 0
        self.nbTour = 0

    def getMode(self):
        return self.mode

    def play(self, batons):
        if self.mode == 'easy':
            return self.playEasy(batons)
        elif self.mode == 'hard':
            return self.playHard(batons)
        else:
            return self.playMedium(batons)

    def playMedium(self, batons):
        if batons == 4:
            return 3
        elif batons == 3:
            return 2
        elif batons == 2:
            return 1
        else:
            return self.playRandom(batons)

    def playEasy(self, batons):
        return self.playRandom(batons)

    @staticmethod
    def playRandom(batons):
        if batons < 4:
            return random.randint(1, batons)
        else:
            return random.randint(1, 3)

    def playHard(self, batons):
        if self.previousNeuron is None:  # PREMIER TOUR
            self.previousNeuron = self.netw.getNeuron(batons)
            neuron_precedent = self.previousNeuron
            prochain_neuron = neuron_precedent.chooseConnectedNeuron(0)
            self.previousNeuron = prochain_neuron
            self.netw.activateNeuronPath(neuron_precedent, prochain_neuron)
            # Taux erreur
            if prochain_neuron.index % 4 != 1 and neuron_precedent.index % 4 != 1:
                self.nbErreur = self.nbErreur + 1
            self.nbTour = self.nbTour + 1
            return neuron_precedent.index - prochain_neuron.index
        elif batons == 1:  # DERNIER TOUR (joué automatiquement)
            self.nbTour = self.nbTour + 1
            return 1
        else:  # TOURS INTERMEDIAIRES
            neuron_precedent = self.previousNeuron
            prochain_neuron = neuron_precedent.chooseConnectedNeuron(neuron_precedent.index - batons)
            self.previousNeuron = prochain_neuron
            self.netw.activateNeuronPath(neuron_precedent, prochain_neuron)
            # Taux d'erreur
            if prochain_neuron.index % 4 != 1 and batons % 4 != 1:
                self.nbErreur = self.nbErreur + 1
            self.nbTour = self.nbTour + 1
            return batons - prochain_neuron.index

    def getNeuronNetwork(self):
        return self.netw

    def setNeuronNetwork(self, ns):
        self.netw = ns

    def getTauxErreur(self):
        return int((self.nbErreur / self.nbTour) * 100)

    def resetTauxErreur(self):
        self.nbErreur = 0
        self.nbTour = 0

    def addWin(self):
        super().addWin()
        self.netw.recompenseConnections()
        self.previousNeuron = None

    def addLoss(self):
        super().addLoss()
        self.previousNeuron = None
