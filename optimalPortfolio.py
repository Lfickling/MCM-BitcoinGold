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
from projReturn import ProjReturn


# of simulation runs
num_runs = 20

class Portfolio():

    #keep track of vital numbers and stats. the two outputted alos, the strading costs, and the max sortino
    maxSortAloTomorrow = []
    trading_costs = 0
    dailyOptimalAlo = []
    sortino = 0
    
    #initialize and run sims. assign optimal values to variables
    def __init__(self, expectedReturns, returns, currentAlocation, prices, capital, N, noGoldDay = False): #N = trading day
        
        if  noGoldDay: #if the gold market is closed
            maxSortToday = self.simulationsNoGold(returns, N, currentAlocation, capital, prices, True)
            self.dailyOptimalAlo = maxSortToday[5:8]
            
            maxSortTomorrow = self.simulationsNoGold(expectedReturns, N, currentAlocation, capital, prices)
            self.maxSortAloTomorrow = maxSortTomorrow[5:8]
            
            
        else: #if gold can be traded today
            maxSortToday = self.simulations(returns, N, currentAlocation, capital, prices, True)
            self.dailyOptimalAlo = maxSortToday[5:8]
            
            maxSortTomorrow = self.simulations(expectedReturns, N, currentAlocation, capital, prices)
            self.maxSortAloTomorrow = maxSortTomorrow[5:8]

        self.trading_costs = maxSortTomorrow[8] 
        self.sortino = maxSortTomorrow[4]

    #return the optimal alocation (percentage) for tomorrow as determined by the historical + expected prices
    def getOptimalPortfolio(self):

        return self.maxSortAloTomorrow

    #return the ideal alocation for today
    def getDailyOptimalAlo(self):

        return self.dailyOptimalAlo

    #return the maximum sortino value from tomorrows optimal alo
    def getSortino(self):

        return self.sortino
    
    #return trading costs associated with the optimal alo
    def getTradingCosts(self):
        return self.trading_costs
    
    #ruuun simulations when gold can be traded. return optimal alo and it's sortino and trading costs in a list
    def simulations(self, returns, N, currentAlo = [0], capital = 0, prices = [0], justSortino = False): #n=trading day
        # Creating 10000 random simulations of each portfolio weight configuration
        

        # Creating a Matrix with 10000 rows, with each row representing a random portfolio:
        #first 3 columns are Mean Returns, Standard Deviation, and Sortino Ratio
        # remaining columns are each assets random weight within that random portfolio
        result = np.zeros((num_runs,9))

        df = pd.DataFrame(returns)
        #df = np.log(df + 1)

        for i in range(num_runs):
            
            weights = np.random.dirichlet(np.ones(3), size =1)[0].tolist()
            
            # daily return of the portfolio based on a given set of weights
            df['portfolio_ret'] = df.iloc[:,0]*weights[0]+df.iloc[:,1]*weights[1]+df.iloc[:,2]*weights[2]
            
            # Calculating Mean
            E = df['portfolio_ret'].mean()
            
            # Calculating Downside Standard Deviation
            std_neg = df['portfolio_ret'][df['portfolio_ret']<0].std()*np.sqrt(N)
            
            # Calculating Upside Standard Deviation
            std_pos = df['portfolio_ret'][df['portfolio_ret']>=0].std()*np.sqrt(N)
            
            # Calculating Volatility Skewness
            volSkew = std_pos/std_neg
            
            # Sortino
            sortino = E/std_neg

            

        #solve adjusted distance (trading cost) between simulatedAlo(1) and realAlo(0), if x is Bit and y is gold: distance = 2|x1-x0| + |y1-y0|
            tradingCost = 0
            if not justSortino:
                #trading cost
                x = abs(currentAlo[1] - (weights[1] * capital)) 
                y = abs(currentAlo[2] - (weights[2] * capital))
                tradingCost = (0.2)*x + (0.1)*y  #maybe 2 times this? have a think!
            
                
                

            # Populating the 'result' array with the required values: Mean, SD, Sharpe followed by the weights                   
            result[i,0] = E
            result[i,1] = std_neg
            result[i,2] = std_pos
            result[i,3] = volSkew
            result[i,4] = sortino
            result[i,8] = tradingCost
            
            for j in range(3):
                result[i,j+5]= weights[j]

        columns = ['Mean','Downside SD', 'Upside SD', 'Volatility Skewness', 'Sortino', 'USD%', 'bitcoin%', 'gold%', 'adjustedDistance'] 
        result = pd.DataFrame(result,columns=columns)

        #do some calculation involving the sortino ratio and the adjusted distance to find some value M
        #maybe norm[sortino] + norm[adjusteddistance]?
        #our selection optimal alocation ratio is the one associated with highest M
        #M-value (which one to pick?) a function of sortino and adjusted distance
        
        maxIndex = int(result['Sortino'].idxmax())
        bestRow = result.loc[maxIndex].to_list()
        if not justSortino:
            max_Sortino = bestRow[4]
            min_Sortino = result['Sortino'].min()
            result['NormedSortino'] = ((result.Sortino - min_Sortino) / (max_Sortino - min_Sortino))

            max_distance = result['adjustedDistance'].max()
            min_distance = result['adjustedDistance'].min()
            result['NormedDistance'] = ((result['adjustedDistance'] - min_distance) / (max_distance - min_distance))

            result['M-Value'] = result['NormedSortino'] - (2*result['NormedDistance'])

            maxIndex = result['M-Value'].idxmax()
            bestRow = result.loc[maxIndex].to_list()

        #get plots we need
        if N == 50:
            self.plotMinsMaxs(result)

        
        return bestRow

    #ruuun simulations when gold cant be traded. return optimal alo and it's sortino and trading costs in a list
    def simulationsNoGold(self, returns, N, currentAlo = [0], capital = 1000, prices = [0], justSortino = False): #n=trading day
        # Creating 10000 random simulations of each portfolio weight configuration
        

        # Creating a Matrix with 10000 rows, with each row representing a random portfolio:
        #first 3 columns are Mean Returns, Standard Deviation, and Sortino Ratio
        # remaining columns are each assets random weight within that random portfolio
        result = np.zeros((num_runs,9))

        df = pd.DataFrame(returns)
        #df = np.log(df/df.shift(1))

        goldWeight = (currentAlo[2] / capital)

        for i in range(num_runs):
            
            #weights with gold fixed
            weights = np.random.dirichlet(np.ones(2), size =1)[0].tolist()
            weights = [weight * (1-goldWeight) for weight in weights]
            weights.append(goldWeight)
            
            # daily return of the portfolio based on a given set of weights (with no gold)
            df['portfolio_ret'] = df.iloc[:,0]*weights[0]+df.iloc[:,1]*weights[1]
            
            # Calculating Mean
            E = df['portfolio_ret'].mean()
            
            # Calculating Downside Standard Deviation
            std_neg = df['portfolio_ret'][df['portfolio_ret']<0].std()*np.sqrt(N)
            
            # Calculating Upside Standard Deviation
            std_pos = df['portfolio_ret'][df['portfolio_ret']>=0].std()*np.sqrt(N)
            
            # Calculating Volatility Skewness
            volSkew = std_pos/std_neg
            
            # Sortino
            sortino = E/std_neg

            
            tradingCost = 0
        #solve adjusted distance (trading cost) between simulatedAlo(1) and realAlo(0), if x is Bit and there is no gold: distance = 2|x1-x0| 
            if not justSortino:
                #trading cost
                x = abs(currentAlo[1] - (weights[1]*capital))
                
                tradingCost = 0.2*x  #maybe 2 times this? have a think!
            
                

            # Populating the 'result' array with the required values: Mean, SD, Sharpe followed by the weights                   
            result[i,0] = E
            result[i,1] = std_neg
            result[i,2] = std_pos
            result[i,3] = volSkew
            result[i,4] = sortino
            result[i,8] = tradingCost
            
            for j in range(3):
                result[i,j+5]= weights[j]

        columns = ['Mean','Downside SD', 'Upside SD', 'Volatility Skewness', 'Sortino', 'USD%', 'bitcoin%', 'gold%', 'adjustedDistance'] 
        result = pd.DataFrame(result,columns=columns)

        #do some calculation involving the sortino ratio and the adjusted distance to find some value M
        #maybe norm[sortino] + norm[adjusteddistance]?
        #our selection optimal alocation ratio is the one associated with highest M
        #M-value (which one to pick?) a function of sortino and adjusted distance
        maxIndex = int(result['Sortino'].idxmax())
        
        bestRow = result.loc[maxIndex].to_list()
        
        if not justSortino:
            max_Sortino = bestRow[4]
            min_Sortino = result['Sortino'].min()
            result['NormedSortino'] = ((result.Sortino - min_Sortino) / (max_Sortino - min_Sortino))

            max_distance = result['adjustedDistance'].max()
            min_distance = result['adjustedDistance'].min()
            result['NormedDistance'] = ((result.adjustedDistance - min_distance) / (max_distance - min_distance))

            result['M-Value'] = result['NormedSortino'] - (2 * result['NormedDistance'])

            maxIndex = int(result['M-Value'].idxmax())
            bestRow = result.loc[maxIndex].to_list()


        #get plots we need
        if N == 50:
            self.plotMinsMaxs(result)

        return bestRow
    
    #plot the sortino ratios for all sims for a day. called from the simulations methods once they are finished running. but only on certain days
    def plotMinsMaxs(self, result):

        Max_Sortino = result.iloc[result['Sortino'].idxmax()]

        plt.figure(figsize=(12,8))
        plt.scatter(x=result['Downside SD'],y=result['Mean'],c=result['Sortino'],cmap='viridis')
        plt.colorbar(label='Sortino Ratio')
        plt.xlabel('Downside Volatility')
        plt.ylabel('Return')

        plt.title('Maximum Sortino Ratio')
        #Plot a red star to highlight position of the portfolio with highest Sortino Ratio
        plt.scatter(Max_Sortino[1],Max_Sortino[0],marker=(5,1,0),color='r',s=600)

        plt.savefig("max_sortino_radio_day.jpg")

        plt.show()