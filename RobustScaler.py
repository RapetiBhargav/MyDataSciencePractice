# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 20:55:31 2020

@author:  Bhargav
"""
from sklearn.preprocessing import RobustScaler
import numpy as np

data=np.array([[ 1.2,  2.3],
       [ 2.1,  4.2],
       [-1.9,  3.1],
       [-2.5,  2.5],
       [ 0.8,  3. ],
       [ 6.3,  2.1],
       [-1.5,  2.7],
       [ 1.4,  2.9],
       [ 1.8,  3.2]])
print('{}\n'.format(repr(data)))
robust_scaler = RobustScaler()
transformed = robust_scaler.fit_transform(data)
print('{}\n'.format(repr(transformed)))