from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from projReturn import ProjReturn

def trader_main():

    #get price, volatility(sigma), and mu()
    comparedReturns = {"date":[],"real":[], "projected":[]}
    cumVolatility = 0
    sigmas =  []

    bitcoinDF = pd.read_csv('/home/lfickling/Spring 22/MCM/MCM-BitcoinGold/data_frames/bitcoin_df.csv')

    for i in range(0,15):
        row = bitcoinDF.loc[i].to_list()
        sigma = row[5]
        
        if i >= 3:
            cumVolatility += (sigma ** 2)
            newSigma = (sqrt((1/(i-2)) * cumVolatility))/(i-1)
            sigmas.append(newSigma)
            sigma = newSigma
        else:
            sigma = 0

        RowReturner = ProjReturn(sigma, row[8], row[2]) #volatility, cumulative mu, value(price)
        projectedReturn = RowReturner.getReturn()
        comparedReturns["date"].append(row[1])
        comparedReturns["real"].append(row[2])
        comparedReturns["projected"].append(projectedReturn)       
    
    comparedReturnsDF = pd.DataFrame(comparedReturns)

    print(comparedReturnsDF)

    #ax = plt.gca() 
    #comparedReturnsDF.plot(kind = 'line',
            #x = 'date',
            #y = 'real',
            #color = 'green',ax = ax)
    #comparedReturnsDF.plot(kind = 'line',x = 'name',
     #       y = 'projected',
      #      color = 'blue',ax = ax)
      
    # set the title
    #plt.title('LinePlots')
    
    # show the plot
    #plt.show()

if __name__ == '__main__':
    trader_main()