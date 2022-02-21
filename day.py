from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from optimalPortfolio import Portfolio
from projReturn import ProjReturn


priceB = 621
priceG = 1324.6

alocations = [[0, 1000, 0], [0, 1000, 0], [0, 1000, 0]]
proportionalAlocations = [[0, 1, 0], [0, 1, 0]], [0, 1, 0]
totalCapital = [1000.00, 1000.00, 1000.00]
comparedReturns= {"date":[],"realB":[621.65, 609.67], "projectedB":[0, 0, 0],"realG":[1324.6, 1324.6], "projectedG":[0, 0, 0]}
expectedReturnRates = []
#historicReturns = [[0, 0, 0], [0, -11.98, 0]]
#yesterdayPrices = [1, 609.67, 1324.6]

def calculateTotalCapital(allocation, prices):
    capital = 0
    for i in range(3):
        capital += prices[i] * allocation[i]
    return capital

def calculateActualAllocation(ProportionalAllocation, totalCapital, prices):
    portfolio = [0,0,0]
    for i in range(3):
        portfolio[i] = ProportionalAllocation[i] * totalCapital * prices[i]
    return portfolio

def getProportionalAllocation(allocation, totalCapital):
    portfolio = [0,0,0]
    for i in range(3):
        portfolio[i] =  totalCapital / allocation[i]
    return portfolio

def getPlots(start, stop):
    comparedReturnsDF = pd.DataFrame(comparedReturns)

    #graph optimal returns compared to real returns
    #other graphs
    # print results tables
    # print(comparedReturnsDF)
    
    ax = plt.gca() 
    comparedReturnsDF[start:stop].plot(kind = 'line',
            x = 'date',
            y = 'realB',
            color = 'green',ax = ax)
    comparedReturnsDF[start:stop].plot(kind = 'line',x = 'date',
            y = 'projectedB',
            color = 'blue',ax = ax)
    comparedReturnsDF[start:stop].plot(kind = 'line',x = 'date',
            y = 'realG',
            color = 'blue',ax = ax)
    comparedReturnsDF[start:stop].plot(kind = 'line',x = 'date',
            y = 'projectedG',
            color = 'blue',ax = ax)
      
    # set the title
    plt.title('GMB expected Return vs. Real Return')
    
    # save the plot
    plt.savefig("GBM_expected_vs_real.jpg")

    #show the plot
    plt.show()

def day_main():
    """
    #comparedReturns = {"date":[],"real":[], "projected":[]}
    #sigmas =  []
    priceB = 621
    priceG = 1324.6
    alocations = [[0, 1000, 0]]
    proportionalAlocations = [0, 1, 0]
    totalCapital = [1000.00]
    comparedReturns= {"date":[],"realB":[], "projectedB":[0],"realG":[], "projectedG":[0]}
    """
    historicReturns = [[0, -11.98, 0]]
    yesterdayPrices = [1, 609.67, 1324.6]
    length = 20

    bitcoinDF = pd.read_csv('/home/lfickling/Spring 22/MCM/MCM-BitcoinGold/data_frames/bitcoin_df.csv')
    goldDF = pd.read_csv('/home/lfickling/Spring 22/MCM/MCM-BitcoinGold/data_frames/bitcoin_df.csv')

    comparedReturns["date"].append(bitcoinDF.iloc[0,1])
    comparedReturns["date"].append(bitcoinDF.iloc[1,1])

    for i in range(2,length):

        rowB = bitcoinDF.loc[i].to_list()
        rowG = goldDF.loc[i].to_list()

        date = rowB[1]
        sigmas = [0, rowB[10], rowG[10]]
        mus = [0, rowB[9], rowG[9]]
        prices = [1, rowB[2], rowG[2]]

        expectedReturns = [0, 0, 0]

        RowReturnerB = ProjReturn(sigmas[1], mus[1], prices[1]) #sigma (or sigma hat), mu, value(price)
        expectedReturns[1] = RowReturnerB.getReturn()
        
        RowReturnerG = ProjReturn(sigmas[1], mus[2], prices[2]) #sigma (or sigma hat), mu, value(price)
        expectedReturns[2] = RowReturnerG.getReturn()

        comparedReturns["date"].append(date)
        comparedReturns["realB"].append(prices[1])
        comparedReturns["projectedB"].append(RowReturnerB.getProjPrice)
        comparedReturns["realG"].append(prices[2])
        comparedReturns["projectedG"].append(RowReturnerG.getProjPrice)

        historicReturns.append([0, (prices[1] -yesterdayPrices[1]), (prices[2] -yesterdayPrices[2])])
        expectedReturnRates = historicReturns.append(expectedReturns)

        if rowG[11] is True:
            portfolio = Portfolio(expectedReturnRates, historicReturns, alocations[i], prices, totalCapital[i], i+1, True)
        else:
            portfolio = Portfolio(expectedReturnRates, historicReturns, alocations[i], prices, totalCapital[i], i+1, False)
        #send data to optimalportfolio
        proportialAlo = portfolio.getOptimalPortfolio()

        #change proportional to actual based on capital and price
        realAlo = calculateActualAllocation(proportialAlo, totalCapital, prices)

        #append alocations with new alocations
        proportionalAlocations.append(proportialAlo)
        alocations.append(realAlo)

        #call calctotalcapital and update
        totalCapital.append(calculateTotalCapital(realAlo, prices)) 

        yesterdayPrices = prices
    
    getPlots(5, 15)


if __name__ == '__main__':
    day_main()