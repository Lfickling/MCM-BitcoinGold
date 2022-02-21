from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from optimalPortfolio import Portfolio
from projReturn import ProjReturn



length = 20

alocations = [[0, 1000, 0], [0, 1000, 0], [0, 1000, 0], [0, 1000, 0]]
proportionalAlocations = [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
totalCapital = [1000.00, 1000.00, 1000.00, 1000.00]
comparedReturns= {"date":[],"realB":[621.65, 609.67, 610.92], "projectedB":[0, 0, 0, 0],"realG":[1324.6, 1324.6, 1323.65], "projectedG":[0, 0, 0, 0]}
expectedReturnRates = []
#historicReturns = [[0, 0, 0], [0, -11.98, 0]]
#yesterdayPrices = [1, 609.67, 1324.6]

def calculateTotalCapital(allocation):
    capital = 0
    for i in range(3):
        capital += allocation[i]
    return capital

def calculateActualAllocation(proportionalAlo, capital, prices):
    portfolio = [0,0,0]
    for i in range(3):
        portfolio[i] = proportionalAlo[i] * capital[i] / prices[i]
    return portfolio

def getProportionalAllocation(allocation, totalCapital):
    portfolio = [0,0,0]
    for i in range(3):
        portfolio[i] =  totalCapital / allocation[i]
    return portfolio

def getPlots(start, stop):
    print(comparedReturns)
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
    yesterdaySigmaG = 0
    yesterdayMuG = 0

    bitcoinDF = pd.read_csv('/home/lfickling/Spring 22/MCM/MCM-BitcoinGold/data_frames/bitcoin_dfnew.csv')
    goldDF = pd.read_csv('/home/lfickling/Spring 22/MCM/MCM-BitcoinGold/data_frames/gold_dfnew.csv')

    comparedReturns["date"].append(bitcoinDF.iloc[0,2])
    comparedReturns["date"].append(bitcoinDF.iloc[1,2])
    comparedReturns["date"].append(bitcoinDF.iloc[2,2])

    for i in range(3,length):

        rowB = bitcoinDF.loc[i].to_list()
        rowG = goldDF.loc[i].to_list()

        if rowG[12]: #just trading bitcoin
            date = rowB[2]
            sigmas = [0, rowB[11], yesterdaySigmaG]
            mus = [0, rowB[10], yesterdayMuG]
            prices = [1, rowB[3], yesterdayPrices[2]]

            
            expectedReturns = [0, 0, 0]

            RowReturnerB = ProjReturn(sigmas[1], mus[1], prices[1]) #sigma (or sigma hat), mu, value(price)
            expectedReturns[1] = RowReturnerB.getReturn()
            
            
            RowReturnerG = ProjReturn(sigmas[1], mus[2], prices[2]) #sigma (or sigma hat), mu, value(price)
            expectedReturns[2] = RowReturnerG.getReturn()
            

            comparedReturns["date"].append(date)
            comparedReturns["realB"].append(prices[1])
            comparedReturns["realG"].append(prices[2])
            if i != (length-1):
                comparedReturns["projectedB"].append(RowReturnerB.getProjPrice())
                comparedReturns["projectedG"].append(RowReturnerG.getProjPrice())

            historicReturns.append([0, (prices[1] -yesterdayPrices[1]), (prices[2] -yesterdayPrices[2])])
            expectedReturnRates = historicReturns 
            expectedReturns += expectedReturns

            portfolio = Portfolio(expectedReturnRates, historicReturns, alocations[i], prices, totalCapital[i], i, noGoldDay =True)
        else: #trading gold and bitcoin
            date = rowB[2]
            sigmas = [0, rowB[11], rowG[11]]
            mus = [0, rowB[10], rowG[10]]
            prices = [1, rowB[3], rowG[3]]
            
            expectedReturnRates = [0, 0, 0]
            expectedReturns = [0, 0, 0]

            RowReturnerB = ProjReturn(sigmas[1], mus[1], prices[1]) #sigma (or sigma hat), mu, value(price)
            expectedReturnRates[1] = RowReturnerB.getReturn()
            
            RowReturnerG = ProjReturn(sigmas[1], mus[2], prices[2]) #sigma (or sigma hat), mu, value(price)
            expectedReturnRates[2] = RowReturnerG.getReturn()

            comparedReturns["date"].append(date)
            comparedReturns["realB"].append(prices[1])
            comparedReturns["projectedB"].append(RowReturnerB.getProjPrice())
            comparedReturns["realG"].append(prices[2])
            comparedReturns["projectedG"].append(RowReturnerG.getProjPrice())

            historicReturns.append([0, (prices[1] -yesterdayPrices[1]), (prices[2] -yesterdayPrices[2])])
            expectedReturnRates = historicReturns 
            expectedReturns += expectedReturns

            portfolio = Portfolio(expectedReturnRates, historicReturns, alocations[i], prices, totalCapital[i], i, noGoldDay=False)

            yesterdayMuG = mus[2]
            yesterdaySigmaG = sigmas[2]
        
        #send data to optimalportfolio
        proportialAlo = portfolio.getOptimalPortfolio()
        print(proportialAlo)

        #change proportional to actual based on capital and price
        realAlo = calculateActualAllocation(proportialAlo, totalCapital, prices)

        #append alocations with new alocations
        proportionalAlocations.append(proportialAlo)
        alocations.append(realAlo)

        #call calctotalcapital and update
        totalCapital.append(calculateTotalCapital(realAlo)) 

        yesterdayPrices = prices
    
    getPlots(5, 15)


if __name__ == '__main__':
    day_main()