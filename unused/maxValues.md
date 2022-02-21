Max_Sortino = result.iloc[result['Sortino'].idxmax()]
Max_Sortino

Min_DSD = result.iloc[result['Downside SD'].idxmin()]
Min_DSD

min_skew = result.iloc[result['Volatility Skewness'].idxmin()]
min_skew

max_skew = result.iloc[result['Volatility Skewness'].idxmax()]
max_skew

max_mean = result.iloc[result['Mean'].idxmax()]
max_mean

max_UP = result.iloc[result['Upside SD'].idxmax()]
max_UP

min_skew = result.iloc[result['Volatility Skewness'].idxmin()]
min_skew