from tokenize import Double
import numpy as np
import matplotlib.pyplot as plt
from math import e

np.random.seed(0)

class Return():
    
    sigma = 0
    mu = 0
    averageReturn = 0

    def __init__(self,sigma, mu, price = 0, k = 10000):
        self.sigma = sigma
        self.mu = mu
        sumReturns = 0
        for i in range(k-1):
            sumReturns += self.getReturnInstance(price)
        self.averageReturn = sumReturns / k


    def getReturnInstance(self, price):
        norm = np.random.normal(loc=self.mu, scale=self.sigma)
        returnInstance = price * e**(-(self.mu-0.5(self.sigma**2)) * (self.sigma * norm)) 
        return returnInstance
        
    def getReturn(self):
        return self.averageReturn
    
    