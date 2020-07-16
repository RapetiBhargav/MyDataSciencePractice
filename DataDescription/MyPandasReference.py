# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 04:27:37 2020

@author: sowja
"""

import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randint(0,10,size=(5,4)),columns=list('ABCD'))
df.to_csv('t.csv',index=False)
#df=pd.read_csv('t.csv', index_col=0)

df.columns

df=pd.read_csv('t.csv')

df.sort_values(by='A',ascending=False)

df[0:2]

df[::-1] #reverse the dataframe

df[:3]

df[:]

#Using Loc and iLoc

df.iloc[3:5, 0:2]
df.iloc[[1, 2, 4], [0, 2]]
df.loc[3:5, ['A','B']] #Basically you give names of indexes and rows in loc

df[df['A'] > 6]
df[df > 6]

#Masking:
#Used to find and replace some values
mask = df['A'].isin([6])

#Replace the  rows of the entire rows
#df.loc[mask] = 0

#Or you can apply the mask result on multiple columns of the masked rows
#df.loc[mask , 'X'] = 1
#df.loc[mask , ['B','C','D']] = 1

fruits_dict = { 'apples': 10,
                'oranges': 8,
                'bananas': 3,
                'strawberries': 20}


dict=pd.Series(fruits_dict)
dict


s=pd.Series([1,2,3,4.2,np.nan])
s

d=s.to_frame()
d

df2=pd.DataFrame({'a':pd.Series([1.0,2.0]),'b':pd.Timestamp('20200607'),'c':pd.Series([3,4,5,6]),'d':pd.Categorical(["test","train","hi","bye"])})
df2

df2=pd.DataFrame({'a':1.0,'b':pd.Timestamp('20200607'),'c':pd.Series([3]*4),'d':pd.Categorical(["test","train","hi","bye"])})

df2.drop(columns=['d','a'])

df

df.iloc[1:3, 0:2]
df.iloc[1,1]

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                           'foo', 'bar', 'foo', 'foo'],
                     'B': ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                    'C': np.random.randn(8),
                      'D': np.random.randn(8)})

grouped=df.groupby('A')

for name, group in grouped:
    print(name)
    print(group)

grouped.get_group('foo')



ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}

df=pd.DataFrame(ipl_data)
grouped = df.groupby('Team')

for name, group in grouped:
    print(name)
    print(group)


print(grouped.agg(np.size))
print(grouped['Points'].agg([np.sum, np.mean, np.std,np.size]))
score = lambda x: (x - x.mean()) / x.std()*10

for name, group in grouped:
    print(name)
    print(group)

print(grouped.Points)

print(grouped.transform(np.mean))

print(grouped.agg(np.mean))
print(grouped.agg({'Year': np.max, 'Points': np.mean}))
#print(grouped.transform({'Year': np.max, 'Points': np.mean})) #Does'nt work

print(grouped['Points'].transform(score))


grouped.apply(lambda x: x.describe())

grouped.agg({'Year': np.max, 'Points': np.mean})

#Or you if you want to rename it to different columns, follow below
df1=df.groupby('Team').agg(Max_Year=('Year',np.max),MeanOfPoints=('Points', np.mean))
df1.columns

df2=df.groupby('Rank').agg(Team=('Team',))
df2.columns

df1.merge(df2.reset_index())

df
gs=df.groupby(['Team', 'Rank'])
for name, group in gs:
    print(name)
    print(group)

gs.xs('March', level='Month')

gs['Points'].mean().unstack().plot()

type(gs['Points'].mean())

temp=pd.DataFrame(np.random.randint(1,4,size=(10,4)),columns=list('ABCD'))
temp

gs=temp.groupby(['A', 'B'])
for name, group in gs:
    print(name)
    print(group)
    

name

gs['C'].mean().unstack().plot()

temp.stack().unstack()


YMData=pd.DataFrame([[1990,1,7,2],[2000,4,3,9]],columns=['Year','Jan.','Feb.','Mar.'])
YMData.set_index('Year',inplace=True) #Pivot a column to index

YMData.stack()
type(YMData.stack())


x=pd.concat([df,df],ignore_index=True) # Toreplace index with Range Index
x

######################################################################
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})

left
right

mod=pd.merge(left, right, on='key')
mod
######################################################################
left = pd.DataFrame({'long': ['aaaa', 'bbbb'], 'X': ['a', 'b']})
right = pd.DataFrame({'Y': ['b', 'c'], 'short': ['bb', 'cc']})

left
right

pd.merge(left, right, how='outer',left_on='X',right_on='Y')
pd.merge(left, right, how='inner',left_on='X',right_on='Y')
pd.merge(left, right, how='left',left_on='X',right_on='Y')
pd.merge(left, right, how='right',left_on='X',right_on='Y')
######################################################################
left.join(right)
######################################################################
pd.concat(df_list) ## Used to stack over rows of same columns


#To datetime
pd.to_datetime('2000-01-13')
dt_obj=pd.to_datetime('2000-01-13')
type(dt_obj)
time_df=pd.DataFrame([['2000-01-13','2000-01-14'],['2000-01-15','2000-01-16']])
time_df.dtypes
time_df[0]=pd.to_datetime(time_df[0])
time_df.dtypes

#To period
dt_obj.to_period(freq='5min')
time_df[0][0:1].to_period(freq='5min')  ##Throwed error

##Creating Date Range
rng = pd.date_range('2000-01-13', periods=100, freq='S')
len(rng)
rng
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts
ts.resample('5min').sum()

#####################################################################
#pd.period_range(start=None, end=None,periods=None, freq=offset)
##Creating Period Range
prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
prng
ts = pd.Series(np.random.randn(len(prng)), prng)
ts.index
#####################################################################

##String operations

s=pd.DataFrame([['Apples and Oranges','Banana'],['Sapota','Guava']],columns=list('AB'))
s
s['A'].str.len()
s['A'].str.lower()
s['A'].str[0] #Returns 1st letter of each element in the series
s['A'].str.contains('pple')
s['A'].str.split().str.get(1)

s['A'].str.split(expand=True)  # Return a dataframe instead of a list
s['A'].str.replace('Apple', 'Mapple')
s['A'].str.extract('')
#####################################################################

##Difference between map, applymap, apply and map methods in Pandas
#Apply
 
gfg_string = 'geeksforgeeks'
gfg_list = 5 * [pd.Series(list(gfg_string))] 
gfg_series = pd.Series(list(gfg_string))
gfg_df = pd.DataFrame(data = gfg_list) 

gfg_df

#Apply
gfg_df.apply(lambda x:x.sort_values(), axis = 1) #series_to_series  -->Gives a dataframe
gfg_df.apply(lambda x:x.mode(), axis = 1)        #series_to_value  -->Gives a series
gfg_series.apply(str.upper)                      #value_to_value   -->Gives a series

gfg_df.applymap(str.upper)                       #applymap works on dataframe.Applies fn on every element

gfg_series.map(str.upper)             #func      #map works on Series, But input can be func,list or dictionary
dic = {'g': "G", 'e': "E"}
gfg_series.map(dic)                   #Dictionary #Unmapped ones will be NaN, use replace instead   


re = pd.DataFrame({'col2': {0: 'a', 1: 2, 2: np.nan}, 'col1': {0: 'w', 1: 1, 2: 2}})
re
di = {1: "A", 2: "B"}
re.replace({"col1": di})   # use replace on df
re['col1'].replace(di)     # use replace on series

######################################################################
#Visualization

import matplotlib.pyplot as plt
df

df['A'].plot()
ax=df.plot()

ax=df.plot(subplots=True,set_xlabel('Rows'))
ax=df.plot(x='A',y='B',subplots=True)

ax.set_xlabel('Rows')
ax.set_ylabel('Value')
ax.set_title('Experiment With Plots')
ax.plot()

df.plot.scatter(x='A',y='B')
df.plot.bar()
df.plot.hist(subplots=True)
df.plot.box()
ax.violinplot()

type(ax)

#ax.legend(labels, loc='best')

############################################################################

d = {'num_legs': [4, 4, 2, 2,2],
     'num_wings': [0, 0, 2, 2,2],
     'class': ['mammal', 'mammal', 'mammal', 'bird','bird'],
     'animal': ['cat', 'dog', 'bat', 'penguin','cat'],
     'locomotion': ['walks', 'walks', 'flies', 'walks','runs']}
df = pd.DataFrame(data=d)
df = df.set_index(['class', 'animal', 'locomotion'])
df


df.xs('mammal',level='class')

df.xs('mammal',level=0)

df.xs('cat',level='animal') #Other than 1st index

df.xs(('mammal', 'dog'))

x=x.reset_index()
x.columns

#############################################################################
#Matplotlib 

#Bar plots
import matplotlib.pyplot as plt

x=[2,4,6,8,10]
y=[6,7,8,2,4]

x2=[1,3,5,7,9]
y2=[7,8,2,4,2]

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()

plt.plot(x,y,label="FirstLine")
plt.plot(x2,y2,label="SecondLine")

plt.bar(x,y,label='Bars1',color='r')
plt.bar(x2,y2,label='Bars2',color='c')

plt.show()

#Legends--if you are plotting multiple series of data

#Histogram
    
population_ages=[22,55,62,45,21,22,34,42,42,4,99,102,110]
ids=[x for x in range(len(population_ages))]
plt.bar(ids,population_ages)

bins=[0,10,20,30,40,50,60,70,80,90,100,110]
plt.hist(population_ages,bins,histtype='bar',rwidth=1)


import datetime as dt



