import random


class perceptron :
    #construtor
    def __init__(self, nb,lr):

        # learning rate
        self.lr = lr

        #setup weight with a random value
        self.weight = [p for p in range(0, nb)]
        for i in range(0,nb):
            self.weight[i] = random.random()


    #result method
    def result(self,input):
        res = 0
        for i in range(0,len(self.weight)):
            res += self.weight[i] * input[i]
        if(res >= 0):
            return 1
        else :
            return -1

    #train method
    def train(self, set, label):
        res = self.result(set)
        err = label-res
        for i in range(0,len(self.weight)):
            self.weight[i] += err * set[i] * self.lr




p = perceptron(2,1)
print(p.weight)
p.train([1,2],-1)
print(p.weight)
  j