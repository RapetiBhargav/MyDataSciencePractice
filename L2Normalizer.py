# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 20:57:13 2020

@author: Bhargav
"""

from sklearn.preprocessing import Normalizer
import numpy as np

data=np.array([[4, 1, 2, 2],
       [3, 4, 0, 0],
       [7, 5, 9, 2]])

print('{}\n'.format(repr(data)))
normalizer = Normalizer()
transformed = normalizer.fit_transform(data)
print('{}\n'.format(repr(transformed)))