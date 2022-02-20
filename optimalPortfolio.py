#imputs: exp.return(t+1) for G and B, and risk(t) for G and B, also current total capital($)(t), current allocation(t)) and current prices(t)

#based on our current total capital: map all possible allocations(t+1)

#calculate total expected return(t+1) for each of those alloactions(t+1) in $

#for each possible allocation(t+1) take [exp.total.return(t+1) - trading costs(from curre.alo(t) to proj.alo(t+1) per prices(t))] = exp.net.return(t+1)

#compare with net.return(t+1) with risks(t) to choose best path (somehow)

