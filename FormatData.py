#https://medium.com/python-data-analysis/linear-regression-on-time-series-data-like-stock-price-514a42d5ac8a

import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import datetime
from sklearn.linear_model import LinearRegression
import financialanalysis as fa


goldData = pd.read_csv("./LBMA-GOLD.csv", parse_dates=['Date'], index_col='Date')
#bitcoinData = pd.read_csv("./BCHAIN-MKPRU.csv", parse_dates=['Date'])

#changes dates to datetime format (rather than strings)
goldData["datetime"] = fa.stringToDatetime(goldData["Date"].to_list())

writer = csv.writer("./priceReturn.csv")


for i,j in goldData.iterrows():
    




## Prepare data
X = goldData["datetime"].to_list() # convert Series to list
X = fa.datetimeToFloatyear(X) # for example, 2020-07-01 becomes 2020.49589041
print(X) # [2020.0054794520547, 2020.0082191780823, 2020.01643835616, ...]
X = np.array(X) # convert list to a numpy array
X -= X[0] # make it begin with 0.
print(X) # [0., 0.00273973, 0.0109589, ..., 1.29589041]
X = X[::,None] # convert row vector to column vector (just column vector is acceptable)
y = goldData["relative_price_change_CTtoBS"] # get y data (relative price)
y = y.values # convert Series to numpy
y = y[::,None] # row vector to column vector (just column vector is acceptable)




