# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 20:59:34 2020

@author: bhargav
"""

from sklearn.impute import SimpleImputer
import numpy as np

data=np.array([[ 1.,  2., np.nan,  2.],
       [ 5.,None,  1.,  2.],
       [ 4., np.nan,  3., np.nan],
       [ 5.,  6.,  8.,  1.],
       [np.nan,  7., np.nan,  0.]])

print('{}\n'.format(repr(data)))

imp_mean = SimpleImputer()
transformed = imp_mean.fit_transform(data)
print('{}\n'.format(repr(transformed)))

imp_median = SimpleImputer(strategy='median')
transformed = imp_median.fit_transform(data)
print('{}\n'.format(repr(transformed)))

imp_frequent = SimpleImputer(strategy='most_frequent')
transformed = imp_frequent.fit_transform(data)
print('{}\n'.format(repr(transformed)))

imp_constant = SimpleImputer(strategy='constant',fill_value=-1)
transformed = imp_constant.fit_transform(data)
print('{}\n'.format(repr(transformed)))
