import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def trader_main():

    #get price, volatility(sigma), and mu()

    bitcoinDF = pd.read_csv('/home/lfickling/Spring 22/MCM/MCM-BitcoinGold/data_frames/bitcoin_df.csv')

    for i in range(1826):
        
    
    print(bitcoinDF)

if __name__ == '__main__':
    trader_main()