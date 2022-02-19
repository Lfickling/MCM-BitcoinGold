import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from projReturn import ProjReturn

def trader_main():

    #get price, volatility(sigma), and mu()
    comparedReturns = {"date":[],"real":[], "projected":[]}

    bitcoinDF = pd.read_csv('/home/lfickling/Spring 22/MCM/MCM-BitcoinGold/data_frames/bitcoin_df.csv')

    for i in range(5):
        row = bitcoinDF.loc[i].to_list()
        RowReturner = ProjReturn(row[5], row[8], row[2]) #volatility, cumulative mu, value
        projectedReturn = RowReturner.getReturn()
        comparedReturns["date"].append(row[1])
        comparedReturns["real"].append(row[2])
        comparedReturns["projected"].append(projectedReturn)       
    
    comparedReturnsDF = pd.DataFrame(comparedReturns)

    print(comparedReturnsDF.head())

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