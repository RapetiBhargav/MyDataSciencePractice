# -*- coding: utf-8 -*-
"""
Created on Fri May  1 10:29:20 2020

@author: sowja
"""

import numpy as np
import pandas as pd
import math

X = pd.DataFrame(
    np.array([5,7,8, np.NaN, np.NaN, np.NaN, -5,
              0,25,999,1,-1, np.NaN, 0, np.NaN])\
              .reshape((5,3)))
X.columns = ['f1', 'f2', 'f3'] #feature 1, feature 2, feature 3

X.dropna(axis=0, thresh=1, inplace=True)
X.reset_index(inplace=True)
X.drop(['index'], axis=1, inplace=True)

from sklearn.impute import MissingIndicator
X.replace({999.0 : np.NaN}, inplace=True)
indicator = MissingIndicator(missing_values=np.NaN)
indicator = indicator.fit_transform(X)
#If the MissingIndicator does not detect any missing values in a feature,
#it does not create a new feature from this feature.
indicator = pd.DataFrame(indicator, columns=['m1', 'm3'])
#We will add this new features later to our original data.Let them now be in a seperate dataframe

#Most learning algorithms perform poorly when missing values are expressed 
#as not a number (np.NaN) and need some form of missing value imputation. 
#Be aware that some libraries and algorithms, such as XGBoost, 
#can handle missing values and impute these values automatically 
#by learning.

from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
SimpleImputerTransformed=imp.fit_transform(X) 
#When you apply simpleImputer on a dataframe, you get a numpy array, 
#losing all the metadata information. So instead use pandas fillna
#also provides options to fill forward (ffill) or fill backward (bfill), 
#which are convenient when working with time series.

X.fillna(X.mean(), inplace=True)

#Other imputing methods: k-nearest neighbor (KNN) algorithm or interpolating the values 
#using a wide range of interpolation methods.

#Before handling missing values, you need to decide if you want to use polynomial features or not. 
#If you for example replace all the missing values by 0, all the cross-products using this feature will be 0. 
#Moreover, if you don’t replace missing values (NaN), creating polynomial features will raise a value error 
#in the fit_transform phase, since the input should be finite.

#when degree is set to two and X=x1, x2, the features created will be 1, x1, x2, x1², x1x2 and x2².interaction_only=True will not have the square terms here.

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=3, interaction_only=True)
#polynomials = pd.DataFrame(poly.fit_transform(X),
#                           columns=['0','1','2','3','p1', 'p2', 'p3', 'p4'])[['0','1','2','3','p1', 'p2', 'p3', 'p4']]

polynomials = pd.DataFrame(poly\
                           .fit_transform(X), 
                           columns=['0','1','2','3', 
                                    'p1', 'p2', 'p3', 'p4'])\
                                        [['p1', 'p2', 'p3', 'p4']]

#degree 3 will create 0-1,1-f1,2-f2,3-f3, p1-f1f2,p2-f2f3,p3-f3f1,p4-f1f2f3

# Lets combine all indicator and polynomials
X = pd.concat([X, indicator, polynomials], axis=1)

#it is important to create polynomial features before doing any feature scaling.

Y = pd.DataFrame(
    np.array(['M', 'O-', 'medium',
             'M', 'O-', 'high',
              'F', 'O+', 'high',
              'F', 'AB', 'low',
              'F', 'B+', np.NaN])
              .reshape((5,3)))
Y.columns = ['sex', 'blood_type', 'edu_level']

#Convert categorical variable into dummy/indicator variables using get_dummies.

#Ordinal and Nominal categorical features
#Ordinal -Categorical features which can be put in order.Like medium , high , low
#Nominal -Categorical features which cannot be put in order.

lencoder = preprocessing.LabelEncoder()
lencoder.fit(titanic_train['Sex'])
print(lencoder.classes_)

from sklearn.preprocessing import OrdinalEncoder
encoder = OrdinalEncoder()
#print(Y.edu_level)
#print(type(Y.edu_level)) #Series
#print(type(Y['edu_level'])) #Series
#print(type(Y[['edu_level']])) #Dataframe
#print(Y.edu_level.values.reshape(-1, 1))
#print(type(Y.edu_level.values.reshape(-1, 1))) # reshape(-1,1) modifies series to ndarray object
Y.edu_level = encoder.fit_transform(Y.edu_level.values.reshape(-1, 1))
#print(Y.edu_level) #Series

# Problem 1: missing values are also encoded
# Problem 2: Ordering is not respected

#c = pd.Series(["a", "b", "d", "a", "d"], dtype ="category") 
#print ("\nCategorical without pandas.Categorical() : \n", c) 
#
#c1 = pd.Categorical([1, 2, 3, 1, 2, 3]) 
#print ("\n\nc1 : ", c1)

Z = pd.DataFrame(
    np.array(['M', 'O-', 'medium',
             'M', 'O-', 'high',
              'F', 'O+', 'high',
              'F', 'AB', 'low',
              'F', 'B+', np.NaN])
              .reshape((5,3)))
Z.columns = ['sex', 'blood_type', 'edu_level']

cat = pd.Categorical(Z.edu_level, 
                     categories=['missing', 'low', 
                                'medium', 'high'], 
                     ordered=True)
print(cat)

cat.fillna('missing') ## Not sure why this is used , since mising values are taken care by factorize anyways.
#Comment this out and you will get the same result

#The factorize method provides an alternative that can handle missing values and 
#respects the order of our values. 

labels, unique = pd.factorize(cat, sort=True)
print(pd.factorize(cat, sort=True))
Z.edu_level = labels

from sklearn.preprocessing import OneHotEncoder
onehot = OneHotEncoder(dtype=np.int, sparse=True)
print(type(Z[['sex', 'blood_type']]))
nominals = pd.DataFrame(onehot.fit_transform(Y[['sex', 'blood_type']]).toarray(),columns=['F', 'M', 'AB', 'B+','O+', 'O-'],)
#Need to convert to array since it returns a sparse matrix.Or just set sparse=False during initialization
nominals['edu_level'] = Z.edu_level

#To handle missing values use fillna('missing') and use one-hot encoder or 
#just set the handle_unkown to ignore, it will add a feature will all zeroes

#Categoroical to Numerical we saw
#Now Numerical to categorical

from sklearn.preprocessing import KBinsDiscretizer
disc = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
Discret=disc.fit_transform(X)
print(disc.bin_edges_) # To check how bins are divided, based on strategy

#Feature binarization is the process of thresholding numerical features to get boolean values.
#binarization is an extreme form of two-bin discretization.
#useful as a feature engineering technique for creating new features that indicate something meaningful.
from sklearn.preprocessing import Binarizer
binarizer = Binarizer(threshold=0, copy=True)
BinerizedData=binarizer.fit_transform(X.f3.values.reshape(-1, 1))

#CustomTransformer: This class can be useful if you’re working with a Pipeline in sklearn
#You can use lambda functions instead of this
from sklearn.preprocessing import FunctionTransformer
transformer = FunctionTransformer(np.log1p, validate=True)
CustomTransformedData=transformer.fit_transform(X.f2.values.reshape(-1, 1)) #same output
X.f2.apply(lambda x : np.log1p(x)) #same output

#Feature scaling
#Before applying any scaling transformations it is very important to split your data into a train set and a test set. 
#Types:StandardScaler, MinMaxScaler, MaxAbsScaler and RobustScaler

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
StandardScalarData=scaler.fit_transform(X.f3.values.reshape(-1, 1))
#for sparse matrices you can set the with_mean parameter to False in order not to center the values around zero.

#scaling each feature to a given range,default [0,1].Sensitive to outliers 
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(-3,3))
MinMaxScalarData=scaler.fit_transform(X.f3.values.reshape(-1, 1))

#scales the data to a [-1,1] range based on the absolute maximum. x/max(abs(x))
#This scaler is meant for data that is already centered at zero or sparse data. It does not shift/center the data, 
#and thus does not destroy any sparsity.
from sklearn.preprocessing import MaxAbsScaler
scaler = MaxAbsScaler()
MaxAbsScalarData=scaler.fit_transform(X.f3.values.reshape(-1, 1))

#Use If your data contains many outliers
#It removes the median and scales the data according to the quantile range.
from sklearn.preprocessing import RobustScaler
robust = RobustScaler(quantile_range = (0.1,0.9)) #Default is 0.25 to 0.75(i.e IQR)
robust.fit_transform(X.f3.values.reshape(-1, 1))

#Normalizer:
from sklearn.preprocessing import Normalizer
data=np.array([[4, 1, 2, 2],
       [3, 4, 0, 0],
       [7, 5, 9, 2]])
normalizer = Normalizer() # You can have the norm parameter to specify l1 , l2 or max
transformed = normalizer.fit_transform(data)

NormData=pd.DataFrame(data)
#You can also use below formulas to check how the normalizers work.This gives the denominator of each one
#max
norm_max = list(max(list(abs(i) for i in NormData.iloc[r])) for r in range(len(NormData)))

#l1
norm_l1 = list(sum(list(abs(i) for i in NormData.iloc[r])) for r in range(len(NormData)))

#l2
norm_l2 = list(math.sqrt(sum(list((i**2) for i in NormData.iloc[r]))) for r in range(len(NormData)))