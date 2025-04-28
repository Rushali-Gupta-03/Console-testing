import pandas as pd
import numpy as np
import plotly.express as px
from Console.package import Functions
import statsmodels.api as sm

f = Functions()

df = f.get_args("df")
# your code here

def arimax_func(df,target,order):
  X = df.drop(columns=[target,'Date'])
  y = np.asarray(df[target])
  model =  sm.tsa.ARIMA(endog=y, order=order, exog=X)
  res_arimax = model.fit()
  return res_arimax

order = (5, 2, 0)  
arimax_result = arimax_func(df, 'DJI_log', order)

exogenous_vars = ['UE_log_diff_4_lag_3','DR_Finance']

f.create_model_ts(arimax_result, "ARIMAX", "chk_insample", "DJI_log", exogenous_vars)
