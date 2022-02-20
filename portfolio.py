from random import uniform

class Portfolio():

    portfolio = []

    def __init__(self, bits, cash, gold):
        self.portfolio = [bits, cash, gold]
    
    def __init__(self):
        self.portfolio = [0]*3

    def getPortfolio(self):
        return self.portfolio

    def shuffle(self, prices):
        valueInUSD = 0
        for i in range(3):
            valueInUSD += prices[i] * self.portfolio[i]
        a = 1
        assert a > 0
        weights = []
        n = 0
        for idx in range(2):
            weights.append(uniform(0,(a-n)))
            self.portfolio[i] = (weights[i] * valueInUSD * prices[i])
            n += weights[idx]
        weights.append(a-n)

        return self.portfolio

#def trader_main(): 


#if __name__ == '__main__':
 #   trader_main()