from tokenize import Double
import numpy as np
import matplotlib.pyplot as plt
from math import e

np.random.seed(0)

class ProjReturn():
    
    sigma = 0
    mu = 0
    averageReturn = 0
    averageTomorrowPrice = 0
    

    def __init__(self,sigma=0.0, mu=0.0, price = 0.0, k = 1000):
        self.sigma = sigma
        self.mu = mu
        sumReturns = 0
        for i in range(k):
            sumReturns += self.getPriceInstance(price)
        self.averageTomorrowPrice = sumReturns / k
        self.averageReturn = (self.averageTomorrowPrice - price) / price
        #print("mu is ", self.mu)
        #print("sigma is ", self.sigma)
        #print("price is ", price)
        #print("projectedPrice is ", self.averageReturn)

    def getPriceInstance(self, price):
        norm = np.random.normal(0, 1)
        returnInstance = price * (e ** ( (self.mu - (0.5 * (self.sigma**2))) + (self.sigma * norm)))  
        #print("scalar is ", (returnInstance / price))
        #print("exponent is ", (-1 * (self.mu - (0.5 * (self.sigma**2))) * (self.sigma * norm)))
        return returnInstance
        
    def getReturn(self):
        return self.averageReturn
    
    def getProjPrice(self):
        return self.averageTomorrowPrice
    
    