from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from optimalPortfolio import Portfolio
from projReturn import ProjReturn



length = 10

proportionalAlocations = {"date": [], "real_cash": [1, 1, 1, 1], "real_bit": [0, 0, 0, 0], "real_gold": [0, 0, 0, 0]}
alocations = [[1000, 0, 0], [1000, 0, 0], [1000, 0, 0], [1000, 0, 0]]
totalCapital = [1000.00, 1000.00, 1000.00, 1000.00]
dailyReturns = {"date":[], "returns": [0, 0, 0, 0]}

dailyOptimalAlo = {"Opt_cash": [1000, 1000, 1000, 1000], "Opt_bit": [0, 0, 0, 0], "Opt_gold": [0, 0, 0, 0]}
dailySortinos = []

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
        portfolio[i] = proportionalAlo[i] * capital / prices[i]
    return portfolio

def getProportionalAllocation(allocation, totalCapital):
    portfolio = [0,0,0]
    for i in range(3):
        portfolio[i] =  totalCapital / allocation[i]
    return portfolio

def getGoldExpectedVsRealPlot(comparedReturnDF, start, stop):
    #graph optimal returns compared to real returns
    
    ax = plt.gca() 
    comparedReturnDF[start:stop].plot(kind = 'line',
            x = 'date',
            y = 'realG',
            color = 'green',ax = ax)
    comparedReturnDF[start:stop].plot(kind = 'line',x = 'date',
            y = 'projectedG',
            color = 'blue',ax = ax)
      
    # set the title
    plt.title('GMB Expected Gold Return vs. Real GoldReturn')
    # save the plot
    plt.savefig("GBM_expected_vs_real_gold.jpg")
    #show the plot
    plt.show()

def getBitExpectedVsRealPlot(comparedReturnDF, start, stop):
    #graph optimal returns compared to real returns
    
    ax = plt.gca() 
    comparedReturnDF[start:stop].plot(kind = 'line',
            x = 'date',
            y = 'realB',
            color = 'green',ax = ax)
    comparedReturnDF[start:stop].plot(kind = 'line',x = 'date',
            y = 'projectedB',
            color = 'blue',ax = ax)
      
    # set the title
    plt.title('GMB Expected Bitcoin Return vs. Real Bitcoin Return')
    # save the plot
    plt.savefig("GBM_expected_vs_real_bitcoin.jpg")
    #show the plot
    plt.show()

def getAloPlot(start, stop):

    for key in proportionalAlocations:
        print(len(proportionalAlocations[key]))
    comparedAlocationsDF = pd.DataFrame(proportionalAlocations)

    ax = plt.gca() 
    comparedAlocationsDF[start:stop].plot(kind = 'line',
            x = 'date',
            y = 'real_cash',
            color = 'green',ax = ax)
    comparedAlocationsDF[start:stop].plot(kind = 'line',x = 'date',
            y = 'real_bit',
            color = 'blue',ax = ax)
    comparedAlocationsDF[start:stop].plot(kind = 'line',x = 'date',
            y = 'real_gold',
            color = 'yellow',ax = ax)
    comparedAlocationsDF[start:stop].plot(kind = 'line',x = 'date',
            y = 'Opt_cash',
            color = 'red',ax = ax)
    comparedAlocationsDF[start:stop].plot(kind = 'line',x = 'date',
            y = 'Opt_bit',
            color = 'pink',ax = ax)
    comparedAlocationsDF[start:stop].plot(kind = 'line',x = 'date',
            y = 'Opt_gold',
            color = 'purple',ax = ax)
      
    # set the title
    plt.title('real proportional alocations vs optimal proportional alocations')
    # save the plot
    plt.savefig("comparedAlocations.jpg")
    #show the plot
    plt.show()
    return

def printStats(sortinosList, netReturns):
    print('the optimal sortino ratios on days 3, 5 10, and the last day:')
    print(sortinosList[0], ' ', sortinosList[5], ' ', sortinosList[length-4])
    print('the net returns are: ', netReturns)

def day_main():

    historicReturns = [[0, -11.98, 0]]
    yesterdayPrices = [1, 609.67, 1324.6]
    yesterdaySigmaG = 0
    yesterdayMuG = 0
    netReturns = 0

    bitcoinDF = pd.read_csv('/home/lfickling/Spring 22/MCM/MCM-BitcoinGold/data_frames/bitcoin_dfnew.csv')
    goldDF = pd.read_csv('/home/lfickling/Spring 22/MCM/MCM-BitcoinGold/data_frames/gold_dfnew.csv')

    comparedReturns["date"].append(bitcoinDF.iloc[0,2])
    comparedReturns["date"].append(bitcoinDF.iloc[1,2])
    comparedReturns["date"].append(bitcoinDF.iloc[2,2])

    dailyReturns["date"].append(bitcoinDF.iloc[0,2])
    dailyReturns["date"].append(bitcoinDF.iloc[1,2])
    dailyReturns["date"].append(bitcoinDF.iloc[2,2])
    dailyReturns["date"].append(bitcoinDF.iloc[3,2])

    proportionalAlocations["date"].append(bitcoinDF.iloc[0,2])
    proportionalAlocations["date"].append(bitcoinDF.iloc[1,2])
    proportionalAlocations["date"].append(bitcoinDF.iloc[2,2])
    proportionalAlocations["date"].append(bitcoinDF.iloc[3,2])

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
            comparedReturns["realG"].append(prices[2])
            if i != (length-1):
                comparedReturns["projectedB"].append(RowReturnerB.getProjPrice())
                comparedReturns["projectedG"].append(RowReturnerG.getProjPrice())

            historicReturns.append([0, (prices[1] -yesterdayPrices[1]), (prices[2] -yesterdayPrices[2])])
            expectedReturnRates = historicReturns 
            expectedReturns += expectedReturns

            portfolio = Portfolio(expectedReturnRates, historicReturns, alocations[i], prices, totalCapital[i], i, noGoldDay=False)

            yesterdayMuG = mus[2]
            yesterdaySigmaG = sigmas[2]
        
        #send data to optimalportfolio
        proportialAlo = portfolio.getOptimalPortfolio()

        tradingCost = portfolio.getTradingCosts()
        #change proportional to actual based on capital and price
        realAlo = calculateActualAllocation(proportialAlo, totalCapital[i]-tradingCost, prices)

        #append alocations with new alocations
        proportionalAlocations["date"].append(date)
        proportionalAlocations['real_cash'].append(proportialAlo[0])
        proportionalAlocations['real_bit'].append(proportialAlo[1])
        proportionalAlocations['real_gold'].append(proportialAlo[2])
        alocations.append(realAlo)

        optPort = portfolio.getDailyOptimalAlo()
        dailyOptimalAlo['Opt_cash'].append(optPort[0])
        dailyOptimalAlo['Opt_bit'].append(optPort[1])
        dailyOptimalAlo['Opt_gold'].append(optPort[2])

        dailySortinos.append(portfolio.getSortino())

        #call calctotalcapital and update
        totalCapital.append(calculateTotalCapital(realAlo)) 
        
        returns = totalCapital[i] - totalCapital[i-1]
        dailyReturns["returns"].append(returns)
        netReturns += returns

        yesterdayPrices = prices
    
    comparedReturnsDF = pd.DataFrame(comparedReturns)
    getGoldExpectedVsRealPlot(comparedReturnsDF, 5, 15)
    getBitExpectedVsRealPlot(comparedReturnsDF, 5, 15)

    proportionalAlocations.update(dailyOptimalAlo)
    getAloPlot(5, 15)

    printStats(dailySortinos, netReturns)


if __name__ == '__main__':
    day_main()