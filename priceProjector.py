from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from projReturn import ProjReturn

def trader_main():

    comparedReturns = {"date":[],"real":[], "projected":[]}
    sigmas =  []
    yesterdayPrice = 621
    sigma = 0
    yesterdayMu = 0
    meanSquaredError = 0
    length = 60

    bitcoinDF = pd.read_csv('/home/lfickling/Spring 22/MCM/MCM-BitcoinGold/data_frames/bitcoin_df.csv')

    for i in range(0,length):
        row = bitcoinDF.loc[i].to_list()
        
        #print("****** ", i)

        RowReturner = ProjReturn(sigma, yesterdayMu, yesterdayPrice) #sigma (or sigma hat), mu, value(price)
        projectedReturn = RowReturner.getReturn()
        comparedReturns["date"].append(row[1])
        comparedReturns["real"].append(row[2])
        comparedReturns["projected"].append(projectedReturn)
        meanSquaredError += ((row[2]- projectedReturn) ** 2)

        yesterdayPrice = row[2]
        if i >= 2:
            sigma = ((row[9] ) * 100 )
            yesterdayMu = (row[8] / i)
        
        sigmas.append(sigma)     
    
    meanSquaredError = (meanSquaredError / length)
    comparedReturnsDF = pd.DataFrame(comparedReturns)

    print(comparedReturnsDF)
    print(meanSquaredError)

    ax = plt.gca() 
    comparedReturnsDF.plot(kind = 'line',
            x = 'date',
            y = 'real',
            color = 'green',ax = ax)
    comparedReturnsDF.plot(kind = 'line',x = 'date',
            y = 'projected',
            color = 'blue',ax = ax)
      
    # set the title
    plt.title('LinePlots')
    
    # show the plot
    plt.show()
    

if __name__ == '__main__':
    trader_main()