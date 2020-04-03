# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 12:14:17 2020

@author: Bhargav
"""

import pandas.util.testing as tm; tm.N = 3
import numpy as np
import pandas as pd 

def unpivot(frame):
    N, K = frame.shape
    data = {'value' : frame.values.ravel('F'),
            'variable' : np.asarray(frame.columns).repeat(N),
            'date' : np.tile(np.asarray(frame.index), K)}
    return pd.DataFrame(data, columns=['date', 'variable', 'value'])
df = unpivot(tm.makeTimeDataFrame())
print(df)

# Convert to wide format
# Use pivot to keep date as the index and value as the values, but use the vaiable column to create new columns
df_pivot = df.pivot(index='date', columns='variable', values='value')
print(df_pivot)

# Convert back to long format
print(df_pivot.unstack())