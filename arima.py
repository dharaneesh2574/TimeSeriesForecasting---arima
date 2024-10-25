import numpy as np
import pandas as pd
import pickle
from statsmodels.tsa.arima.model import ARIMA

data = pd.read_csv("../TSLA.csv") 
data = data[["Date","Close"]] 
data = data.rename(columns = {"Date":"ds","Close":"y"})
data['ds'] = pd.to_datetime(data['ds'])
data.set_index('ds', inplace=True)
model = ARIMA(data['y'], order=(1,1,1))
model = model.fit()

with open('arima.pkl', 'wb') as f:
    pickle.dump(model, f)