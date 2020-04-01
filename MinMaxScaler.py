# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 20:52:38 2020

@author: Bhargav
"""

from sklearn.preprocessing import MinMaxScaler
import numpy as np

data=np.array([[ 1.2,  3.2],
       [-0.3, -1.2],
       [ 6.5, 10.1],
       [ 2.2, -8.4]])
print('{}\n'.format(repr(data)))
default_scaler = MinMaxScaler() # the default range is [0,1]
transformed = default_scaler.fit_transform(data)
print('{}\n'.format(repr(transformed)))

custom_scaler = MinMaxScaler(feature_range=(-2, 3))
transformed = custom_scaler.fit_transform(data)
print('{}\n'.format(repr(transformed)))