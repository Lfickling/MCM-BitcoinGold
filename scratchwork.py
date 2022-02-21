
from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from optimalPortfolio import Portfolio
from projReturn import ProjReturn

def scratch_main(): 
    #bitcoinDF = pd.read_csv('/home/lfickling/Spring 22/MCM/MCM-BitcoinGold/data_frames/bitcoin_dfnew.csv')
    goldDF = pd.read_csv('/home/lfickling/Spring 22/MCM/MCM-BitcoinGold/data_frames/gold_dfnew.csv')

    for i in range(4,5):
        #rowB = bitcoinDF.loc[i].to_list()
        rowG = goldDF.loc[i].to_list()
        print(rowG)
    if rowG[12]:
        print('a bool')
    else:
        print('not')


if __name__ == '__main__':
    scratch_main()

