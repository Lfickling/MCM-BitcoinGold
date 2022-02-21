        #imputs: exp.return(t+1) for G and B in format [0,ER(B), ER(G)], and risk(t) for G and B in form [0, R(B), R(G))], 
        # also current total capital($)(t)current allocation(t)) [$, B, G] and current prices(t) [1,P(B), P(G)] 

        #based on our current total capital: map all possible allocations(t+1) [$, B, G] porportionally
            # alocations taking into account no gold trading on weekends
            # we will need to know the dayoftheweek

        #calculate total expected return(t+1) for each of those alloactions(t+1) in $ as a function of [$, B, G] and [0,ER(B), ER(G)]

        #for each possible allocation(t+1) take [exp.total.return(t+1) - trading costs(from curre.alo(t) to proj.alo(t+1) per prices(t))] 
        # = exp.net.return (t+1) in $

        #use [0, sigma(B), sigma(G)] as risk

        #compare with net.return(t+1) with risk(t)(n) to choose best path (somehow) Max[exp.return(n) / risk(t)] choose max for [$, B, G]

from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from unused.portfolio import Portfolio
from projReturn import ProjReturn

class Portfolio():

    portfolio = []
    maxSortAloToday = []
    maxSortTomorrow = []
    #maxSortStats = []
    #maxSortStatsTomorrow = []
    
    def __init__(self, expectedReturns, mus, N):

        maxSortToday = self.simulations(mus, N)
        maxSortTomorrow = self.simulations(expectedReturns, N+1)
        self.maxSortAloToday = maxSortToday[5:]
        self.maxSortAloTomorrow = maxSortTomorrow[5:]

        #self.maxSortStats = maxSortToday[:5]
        #self.maxSortStatsTomorrow = maxSortTomorrow[:5]


    def getOptimalPortfolio(self, risks, currentAlocation, currentPrices, N):
        #here we decide which portfolio to use and return it
        

        return self.portfolio

    def simulations(mus, N): #n=trading day
        # Creating 10000 random simulations of each portfolio weight configuration
        num_runs = 10000 # number of rows/iterations

        # Creating a Matrix with 10000 rows, with each row representing a random portfolio:
        #first 3 columns are Mean Returns, Standard Deviation, and Sortino Ratio
        # remaining columns are each assets random weight within that random portfolio
        result = np.zeros((num_runs,8))

        df = pd.DataFrame()

        for i in range(num_runs):
    
            # randomized weights
            weights = np.array(np.random.random(3)) 
            #Rebalance w/ constraints (SUM of all weights CANNOT BE > 1)
            weights = weights/np.sum(weights)
            
            # daily return of the portfolio based on a given set of weights
            df['portfolio_ret'] = mus[0]*weights[0]+mus[1]*weights[1]+mus[2]*weights[2]
            
            # Calculating Mean
            E = df['portfolio_ret'].mean()
            
            # Calculating Downside Standard Deviation
            std_neg = df['portfolio_ret'][df['portfolio_ret']<0].std()*np.sqrt(N)
            
            # Calculating Upside Standard Deviation
            std_pos = df['portfolio_ret'][df['portfolio_ret']>=0].std()*np.sqrt(N)
            
            # Calculating Volatility Skewness
            volSkew = std_pos/std_neg
            
            # Sortino
            Sortino = E/std_neg

            # Populating the 'result' array with the required values: Mean, SD, Sharpe followed by the weights                   
            result[i,0] = E
            result[i,1] = std_neg
            result[i,2] = std_pos
            result[i,3] = volSkew
            result[i,4] = Sortino
            
            for j in range(3):
                result[i,j+5]= weights[j]

        columns = ['Mean','Downside SD', 'Upside SD', 'Volatility Skewness', 'Sortino', 'USD%', 'bitcoin%', 'gold%'] 
        result = pd.DataFrame(result,columns=columns)

        Max_Sortino = result.iloc[result['Sortino'].idxmax()]

        return Max_Sortino
    
    def plotMinsMaxs(self, result):

        plt.figure(figsize=(12,8))
        plt.scatter(x=result['Downside SD'],y=result['Mean'],c=result['Sortino'],cmap='viridis')
        plt.colorbar(label='Sortino Ratio')
        plt.xlabel('Downside Volatility')
        plt.ylabel('Return')

        plt.title('Maximum Sortino Ratio')
        #Plot a red star to highlight position of the portfolio with highest Sortino Ratio
        plt.scatter(Max_Sortino[1],Max_Sortino[0],marker=(5,1,0),color='r',s=600)

        plt.show()