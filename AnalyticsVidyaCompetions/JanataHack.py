# -*- coding: utf-8 -*-
"""
Created on Sat May 30 14:10:16 2020

@author: sowja
"""
import re
import numpy as np
import pandas as pd
import os
from sklearn import ensemble, model_selection

dir = 'E:/JanataHack'
train = pd.read_csv(os.path.join(dir, 'train.csv'))
print(train.info())
print(train.columns)

X_train = train[ ['Loan_ID','Loan_Amount_Requested','Length_Employed','Home_Owner','Annual_Income',
'Income_Verified','Purpose_Of_Loan','Debt_To_Income', 'Inquiries_Last_6Mo','Months_Since_Deliquency','Number_Open_Accounts','Total_Accounts','Gender'] ]
y_train = train['Interest_Rate']


X_train['Loan_Amount_Requested']= X_train['Loan_Amount_Requested'].replace(',', '',regex=True)

X_train.Length_Employed.count
X_train.dtypes

X_train.isnull().sum()
X_train['Loan_Amount_Requested'] = X_train['Loan_Amount_Requested'].str.replace(r'\D', '')
X_train['Loan_Amount_Requested'] = X_train['Loan_Amount_Requested'].astype(float)


X_train['Length_Employed'].unique()


def experience(x):
    if x=="< 1 year":
        return "0"
    elif x=="1 year":
        return "1"
    elif x=="2 years":
        return "2"
    elif x=="3 years":
        return "3"
    elif x=="4 years":
        return "4"
    elif x=="5 years":
        return "5"
    elif x=="6 year":
        return "6"
    elif x=="7 years":
        return "7"
    elif x=="8 years":
        return "8"
    elif x=="9 years":
        return "9"
    elif x=="10+ years":
        return "10"
    else:
        return "-1"

X_train["Length_Employed"] = X_train["Length_Employed"].apply(experience)

X_train['Home_Owner'].unique()
X_train['Purpose_Of_Loan'].unique()
X_train['Income_Verified'].unique()

X_train[(X_train['Income_Verified'] == 'not verified')].count
#51873

X_train.Length_Employed.value_counts()

X_train[(X_train['Length_Employed'] == '0')].count

condition_3 = (X_train['Income_Verified'] == 'not verified') & (X_train['Length_Employed'] =='10')
filtered_df = X_train[condition_3]

temp_df_AI = X_train[pd.isna(X_train['Annual_Income'])][['Length_Employed','Income_Verified','Annual_Income','Debt_To_Income','Loan_Amount_Requested']]
X_train['Annual_Income'] = X_train['Annual_Income'].fillna(X_train['Annual_Income'].median())

temp_df_AI.isnull().sum()

X_train['IsDeliquent']=X_train['Months_Since_Deliquency'].map(lambda x : 0 if np.isnan(x) else 1)
X_train['IsDeliquent'].value_counts()

del(X_train['IsDeliquent'])

X_train['Months_Since_Deliquency']=X_train['Months_Since_Deliquency'].map(lambda x : -1 if np.isnan(x) else x)

X_train.drop(X_train.loc[pd.isna(X_train['Number_Open_Accounts']),:].index,inplace=True)










