# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:58:03 2020

@author: sowja
"""
# python code to demonstrate working of reduce() 


from tqdm import tqdm, tqdm_notebook
tqdm_notebook().pandas()
# importing functools for reduce() 
from functools import reduce 
import pandas as pd

df = pd.DataFrame({'c1': [1,2,3,4,5,1,2,3,4], 'year': [2016, 2017,2016,2017,2016,2015,2014,2016,2015],
                   'Team': ['MI', 'MI','CSK','CSK','KKR','DC','DC','DDD','KKR'],'c3': [5, 6,3,4,5,6,2,1,10]})

groups=df.groupby(['year','Team'])

no2015 = groups.filter(lambda x: x['c3'] > 4)

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
'foo', 'bar'],
'B' : [1, 2, 3, 4, 5, 6],
'C' : [2.0, 5., 8., 1., 2., 9.]})
grouped = df.groupby('A')
grouped.filter(lambda x: x['B'].mean() > 3.)

print(df)
df['NewA'] = df.apply(lambda x: x['A']+'bhargav I am alright',axis=1)

print(df)

#we want to filter those rows where the number of words in the NewA is greater than or equal 
#to than 4.

#new_df = df[len(df['NewA'].split(" "))>=4]
#This will give an error, since there is no split attribute in series.

#One way is to first create a column which contains no of words 
#in the title using apply and then filter on that column.
#create a new column
df['num_words'] = df.apply(lambda x : len(x['NewA'].split(" ")),axis=1)

#simple filter on new column
new_df = df[df['num_words']>=4]

#I would rather prefer
new_df = df[df.apply(lambda x : len(x['NewA'].split(" "))>=4,axis=1)]

#To show progress of apply
new_df = df[df.progress_apply(lambda x : len(x['NewA'].split(" "))>=4,axis=1)]

#Incase you need to deal with Price which has , like 13,000
#df['Price'] = df.apply(lambda x: int(x['Price'].replace(',', '')),axis=1)

