import random

BASE_WEIGHT = 10
RECOMPENSE = 8


class NeuronNetwork:
    def __init__(self, maxDist, nbSticks):
        self.neurons = []
        for i in range(1, nbSticks + 1):
            self.neurons.append(Neuron(self, i))
        for neuron in self.neurons:
            neuron.makeConnections(maxDist, nbSticks, BASE_WEIGHT)
        self.initPath()

    def initPath(self):
        self.path = {}

    def getNeuron(self, index):
        if index - 1 >= 0 and index <= len(self.neurons):
            return self.neurons[index - 1]
        else:
            return None

    def activateNeuronPath(self, neuron1, neuron2):
        self.path[neuron1] = neuron2

    def recompenseConnections(self):
        for neuron1, neuron2 in self.path.items():
            neuron1.recompenseConnection(neuron2)
        self.initPath()

    def printAllConnections(self):
        for neuron in self.neurons: neuron.printConnections()

    def printScores(self):
        scores = {}
        for neuron in self.neurons:
            for n, s in neuron.connections.items():
                if n not in scores:
                    scores[n] = s
                else:
                    scores[n] = scores[n] + s
        for neuron, score in scores.items():
            print(neuron.asString(), score)

    def agregatTousNeurons(self, netw2):
        for n1 in self.neurons:
            for n2 in netw2.neurons:
                if n1.index == n2.index:
                    n1.agregatNeuronParNeuron(n2)

class Neuron:
    def __init__(self, network, index):
        self.network = network
        self.index = index
        self.connections = {}

    def makeConnections(self, maxDist, nbSticks, baseWeight):
        if self.index != nbSticks:
            nb = maxDist * 2 + 1
        else:
            nb = maxDist + 1
        for i in range(1, nb):
            neuron = self.network.getNeuron(self.index - i)
            if neuron is not None: self.connections[neuron] = baseWeight

    def chooseConnectedNeuron(self, shift):
        neuron = None
        # SHIFT = décalage (ce que le joueur précédent à joué)
        test = False
        connectionsCopie = self.connections.copy()
        while not test:
            neuron = self.weighted_choice(connectionsCopie)
            connectionsCopie.pop(neuron)
            test = neuron.testNeuron(self.index - shift)
            if test:
                return neuron
            if len(connectionsCopie) == 0:
                return None

    def testNeuron(self, neuron):
        # InValue : Neuron suivant à tester - Shift
        if 1 <= neuron - self.index <= 3:
            return True
        else:
            return False

    def recompenseConnection(self, neuron):
        self.connections[neuron] = self.connections[neuron] + RECOMPENSE
        pass

    def printConnections(self):
        print("Connections of", self.asString() + ":")
        for neuron in self.connections:
            print(neuron.asString(), self.connections[neuron])

    def asString(self):
        return "N" + str(self.index)

    @staticmethod
    def weighted_choice(connections):
        total = sum(w for c, w in connections.items())
        r = random.uniform(0, total)
        upto = 0
        for c, w in connections.items():
            if upto + w >= r: return c
            upto += w

    def agregatNeuronParNeuron(self, neuron2):
        for i, j in self.connections.items():
            for c2, w2 in neuron2.connections.items():
                if i.index == c2.index:
                    self.connections[i] += w2
