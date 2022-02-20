from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from projReturn import ProjReturn

def calculateTotalCapital(allocation, prices):

    return

def calculateActualAllocation(ProportionalAllocation, totalCapital, prices):

    return

def day_main():

    #comparedReturns = {"date":[],"real":[], "projected":[]}
    #sigmas =  []
    priceB = 621
    priceG = 1324.6
    length = 60

    alocations = {1:[0, 1000, 0]}
    totalCapital = 1000.00
    comparedReturnsB= {"date":[],"real":[], "projected":[0]}
    comparedReturnsG = {"date":[],"real":[], "projected":[0]}
    

    bitcoinDF = pd.read_csv('/home/lfickling/Spring 22/MCM/MCM-BitcoinGold/data_frames/bitcoin_df.csv')
    goldDF = pd.read_csv('/home/lfickling/Spring 22/MCM/MCM-BitcoinGold/data_frames/bitcoin_df.csv')

    for i in range(0,length):

        rowB = bitcoinDF.loc[i].to_list()
        rowG = goldDF.loc[i].to_list()

        date = rowB[1]
        sigmas = [0, rowB[10], rowG[10]]
        mus = [0, rowB[9], rowG[9]]
        prices = [1, rowB[2], rowG[2]]

        if i <= 1:
            sigmas[1, 2] = 0, 0
            mus[1, 2] = 0, 0
            prices[1, 2] = priceB, priceG

        RowReturnerB = ProjReturn(sigmas[1], mus[1], prices[1]) #sigma (or sigma hat), mu, value(price)
        projectedReturnB = RowReturnerB.getReturn()
        
        RowReturnerG = ProjReturn(sigmas[1], mus[2], prices[2]) #sigma (or sigma hat), mu, value(price)
        projectedReturnG = RowReturnerG.getReturn()

        comparedReturnsB["date"].append(date)
        comparedReturnsB["real"].append(prices[1]])
        comparedReturnsB["projected"].append(projectedReturnB)

        comparedReturnsG["date"].append(date)
        comparedReturnsG["real"].append(prices[2]])
        comparedReturnsG["projected"].append(projectedReturnG)
             
        #send data to optimalportfolio

        #change proportional to actual based on capital and price

        #append alocations with new alocations

        #call calctotalcapital and update
    
    #comparedReturnsDF = pd.DataFrame(comparedReturns)

if __name__ == '__main__':
    day_main()