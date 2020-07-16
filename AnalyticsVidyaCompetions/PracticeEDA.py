# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:08:39 2020

@author: sowja
"""
import pandas as pd
import numpy as np

df=pd.read_csv("E:/JanataHack/train.csv")

Top100=df.head(100)

Top100.info()

Top100.columns

Top100.dtypes

Top100.isnull().sum()

Top100.head()

type(Top100.Loan_ID)

TestDF=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],dtype=np.float32)
TestDF

print(TestDF)

test=np.array([1,2,3],dtype=np.object)

print(repr(test))

test=np.array(['s',2,3])

type(test)

Top100.dtypes

Top100.to_csv("Top100.csv")

pd.Series([['zcsdvsv'],'wefhwv','cgwecj',['cjwh'],[['acjhva'],['asjcv']]],name='MySeries')


values=[1,2,3,4,[5,6,7],[8,9]]
index=1
name='learn'
ser=pd.Series(values, index=[1,2,3,4,5,6])
pd.DataFrame({'idx1': ['val1'], 'idx2': ['val2']})

Top100.isnull().sum()

labels_To_Drop=['Gender']
Top100.drop(labels_To_Drop,axis=1,inplace=True)

Top100.columns

Top100.values
Top100.shape
Top100.drop(columns=['Loan_ID'],inplace=True)
Top100.rename(columns={'Length_Employed':'Experience'},inplace=True)

Top100['Loan_Amount_Requested'].replace(',','',regex=True,inplace=True)
Top100.dtypes
len(Top100)
Top100['Experience'].unique()
Top100['Loan_Amount_Requested'].describe()
Top100[['Loan_Amount_Requested']]=Top100[['Loan_Amount_Requested']].astype('float')

Temp=Top100.sort_values(['Experience'],ascending=[True])[['Experience','Loan_Amount_Requested']]
Temp1=Top100.sort_values(['Experience','Loan_Amount_Requested'],ascending=[True,True])[['Experience','Loan_Amount_Requested']]

Top100.info()
Top100.loc[0:50]
Top100.iloc[0:50]

Top100.drop(labels=['IsEmployed'],axis=1,inplace=True)

Top100['UnEmployed']=Top100['Experience'].isna()

Interpolated=Top100.interpolate(method='linear')

print('{}\n'.format(Top100.loc['Experience']))

T = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
                   'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])

print('{}\n'.format(T.loc['r2']))

d = {'num_legs': [4, 4, 2, 2],
     'num_wings': [0, 0, 2, 2],
     'class': ['mammal', 'mammal', 'bird', 'bird'],
     'animal': ['tiger', 'fox', 'penguin', 'sparrow'],
     'locomotion': ['walks', 'walks', 'walks', 'flies']}
Sample = pd.DataFrame(data=d)

Sample.dtypes

g=Sample.groupby('num_legs')

for name, group in g:
  print('Number Of Legs: {}'.format(name))
  print('{}\n'.format(group))

print('{}\n'.format(g.get_group(2)))
print('{}\n'.format(g.sum()))
print('{}\n'.format(g.mean()))

no2 = g.filter(lambda x: x.name > 2)
no2

def normalize(grp):
    return (grp - grp.mean()) / grp.var()

g.transform(normalize)

Sample.plot()

Top100.head()

ax = Top100.plot()
Top100.plot.scatter('Loan_Amount_Requested', 'Interest_Rate')


Top100.set_xlabel('Loan_Amount_Requested')
Top100.set_ylabel('Interest_Rate')
Top100.set_title('Loan Amt vs Interest Rate')
Top100.legend(loc='best')

g.apply(lambda x: x.describe())

