# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:42:41 2020

@author: Bhargav
"""

import pandas as pd
names = ['age', 'workclass', 'fnlwgt', 'education', 'educationnum', 'maritalstatus', 'occupation', 'relationship', 'race',
        'sex', 'capitalgain', 'capitalloss', 'hoursperweek', 'nativecountry', 'label']
train_df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",
                      header=None, names=names)

# Group by relationship and then get the value counts of label with normalization                   
print(train_df.groupby('relationship')['label'].value_counts(normalize=True))
#When we use normalize=True, it gives %'s of label

#Here label is categorical, change it to numeric by using lambda fn, and calculate correlation
train_df['label_int'] = train_df.label.apply(lambda x: ">" in x)
print(train_df.corr())