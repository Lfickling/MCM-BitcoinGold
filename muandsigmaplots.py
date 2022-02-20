from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from projReturn import ProjReturn

def plots_main():

    bitcoinDF = pd.read_csv('/home/lfickling/Spring 22/MCM/MCM-BitcoinGold/data_frames/bitcoin_df.csv')

    ax = plt.gca() 
    bitcoinDF.plot(kind = 'line',
            x = 'Date',
            y = 'volatility',
            color = 'green',ax = ax)
    bitcoinDF.plot(kind = 'line',x = 'Date',
            y = 'price',
            color = 'blue',ax = ax)

      
    # set the title
    plt.title('LinePlots')
    
    # show the plot
    plt.show()
    

if __name__ == '__main__':
    plots_main()