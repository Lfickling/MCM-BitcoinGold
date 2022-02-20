# MCM-BitcoinGold
modelling bitcoin and gold trading for the mathematical contest in modelling

how: 
main driver is day.py
        will cycle through data on each day t.
        will get expected return from priceProjector.py for gold and bitcoin
        will get risk in the form [0, R(B), R(G))]
        will keep track of current alocation (and store that information)
        will keep track of current total capital in usd (and store)
        will send exp.return(t+1)'s , risks, current alo, current prices, and current totalcapital to optimal portfolio which will output the best new proportional alocation and trading costs
        calc actually allocation from proportional alocation
        will set alocation for next day to optimal projected and update total capital 
        will go to next day

requisite pieces:

    optimalPortfolio.py
        #imputs: exp.return(t+1) for G and B in format [0,ER(B), ER(G)], and risk(t) for G and B in form [0, R(B), R(G))], also current total capital($)(t)current allocation(t)) [$, B, G] and current prices(t) [1,P(B), P(G)] 

        #based on our current total capital: map all possible allocations(t+1) [$, B, G] porportionally
            # alocations taking into account no gold trading on weekends
            we will need to know the dayoftheweek

        #calculate total expected return(t+1) for each of those alloactions(t+1) in $ as a function of [$, B, G] and [0,ER(B), ER(G)]

        #for each possible allocation(t+1) take [exp.total.return(t+1) - trading costs(from curre.alo(t) to proj.alo(t+1) per prices(t))] = exp.net.return (t+1) in $

        #use [0, sigma(B), sigma(G)] as risk

        #compare with net.return(t+1) with risk(t)(n) to choose best path (somehow) Max[exp.return(n) / risk(t)] choose max for [$, B, G]

    priceprojector.py:

        takes in current price, sigma hat and new mu  and projects and calculates a projected price

        takes projected price - current price for projected return

        returns expected return



    




