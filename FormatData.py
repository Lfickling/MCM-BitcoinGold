#https://medium.com/python-data-analysis/linear-regression-on-time-series-data-like-stock-price-514a42d5ac8a


from cmath import log
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import datetime
#from sklearn.linear_model import LinearRegression
import financialanalysis as fa


goldData = pd.read_csv("./LBMA-GOLD.csv", parse_dates=['Date'], index_col='Date')
#bitcoinData = pd.read_csv("./BCHAIN-MKPRU.csv", parse_dates=['Date'])

#changes dates to datetime format (rather than strings)
goldData["datetime"] = fa.stringToDatetime(goldData["Date"].to_list())








