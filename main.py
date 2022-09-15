import random


class perceptron :
    #construtor
    def __init__(self, nb):
        self.weight = [p for p in range(0, nb)]
        for i in range(0,nb):
            self.weight[i] = random.random()

    #train method
    def train(self, set):
        for i in range(0,len(self.weight)):
            self.weight[i] =

    #result method
    def result(self):
        res =
        for w in self.weight:
            res 

p = perceptron(6)
print(p.weight)
p.train()
print(p.weight)