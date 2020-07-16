#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Loading libraries 
import numpy as np 
import pandas as pd
from pandas_profiling import ProfileReport
import pandas_profiling as pp
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = (10.0, 8.0)
import seaborn as sns
from scipy import stats
from scipy.stats import norm


# In[536]:


pp.__version__


# In[537]:


pd.__version__


# In[538]:


train=pd.read_csv("Train.csv")
test=pd.read_csv("Test.csv")


# In[539]:


train.head()


# In[540]:


train.shape


# In[541]:


test.shape


# In[542]:


train.dtypes


# In[543]:


train['MULTIPLE_OFFENSE'].value_counts()


# In[544]:


train.DATE=pd.to_datetime(train.DATE)


# In[545]:


train.dtypes


# In[546]:


train['YEAR'], train['MONTH'] = train['DATE'].dt.year, train['DATE'].dt.month


# In[547]:


train['DATE'],pd.DatetimeIndex(train.DATE).dayofweek // 5 == 1


# In[594]:


train['DAY_OF_WEEK']=(pd.DatetimeIndex(train.DATE).dayofweek).astype(int)


# In[549]:


#days = {0: "Monday", 1: "Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}


# In[550]:


train['DAY_OF_WEEK']=train['DAY_OF_WEEK'].replace(days)


# In[551]:


train.head()


# In[552]:


### To Create the Simple report quickly
profile = ProfileReport(train, title='Pandas Profiling Report', explorative=True)


# In[26]:


profile.to_file("output.html")


# In[553]:


#Columns which have null values
train.isnull().any()


# In[554]:


train[['INCIDENT_ID','DATE','X_1','X_2','X_3']].sort_values('DATE')


# # The CR_Numbers don't necessarily follow a strict pattern

# In[555]:


value_counts_dict = {c: train[c].value_counts().to_dict() for c in train.filter(like='X_', axis=1)}


# In[556]:


value_counts_dict_test = {c: test[c].value_counts().to_dict() for c in test.filter(like='X_', axis=1)}


# In[557]:


value_counts_dict


# In[558]:


print ({key:value for key, value in value_counts_dict.items() if len(value)<20})


# In[559]:


print ({key:sorted(value.keys()) for key, value in value_counts_dict.items() if len(value)<30})


# In[560]:


print ({key:sorted(value.keys()) for key, value in value_counts_dict_test.items() if len(value)<20})


# In[561]:


def minMax(x):
    return pd.Series(index=['min','max'],data=[x.min(),x.max()])


# In[562]:


train.filter(like='X_', axis=1).apply(minMax)


# In[563]:


test.filter(like='X_', axis=1).apply(minMax)


# In[564]:


##Based on the min and max values we can arbitrarily consider below below columns into categorical and continuous

#Cat:X_1,X_4,X_5
#Cont:X_2,X_3,X_11(high values),X_12(float values),X_13,X_14,X_15

#Similar
#X_6,X_7-->0-19
#X_8,X_10-->0-99(somewhat similar) 


# In[565]:


train.dtypes


# # Visualization

# In[566]:


#Univariate Analysis


# In[567]:


sns.countplot(x='X_1',data=train,hue="MULTIPLE_OFFENSE") #Max at 0
#sns.countplot(x='X_2',data=train)  #Max at 4
#sns.countplot(x='X_3',data=train)
#sns.countplot(x='X_4',data=train)
#sns.countplot(x='X_5',data=train)
#sns.countplot(x='X_6',data=train)
#sns.countplot(x='X_7',data=train)
#sns.countplot(x='X_8',data=train)
#sns.countplot(x='X_9',data=train)
#sns.countplot(x='X_10',data=train)
#sns.countplot(x='X_11',data=train)
#sns.countplot(x='X_12',data=train)
#sns.countplot(x='X_13',data=train)
#sns.countplot(x='X_14',data=train)
#sns.countplot(x='X_15',data=train)
#sns.countplot(x='MULTIPLE_OFFENSE',data=train) #1 values are high.Its skewed.


# In[568]:


#Cat vs Cat
#sns.catplot(x="X_1", hue="MULTIPLE_OFFENSE", data=train, kind="count", height=6) # X1 >1 , we get mostly 1(hacked)
#sns.factorplot(x="X_2", hue="MULTIPLE_OFFENSE", data=train, kind="count", size=10)
#sns.factorplot(x="X_4", hue="MULTIPLE_OFFENSE", data=train, kind="count", size=10) #No 5 values for X_4
#sns.factorplot(x="X_5", hue="MULTIPLE_OFFENSE", data=train, kind="count", size=10) #No 2 values for X_5
#sns.factorplot(x="X_10", hue="MULTIPLE_OFFENSE", data=train, kind="count", size=10) #Most of the values are 0,1
#sns.factorplot(x="X_14", hue="MULTIPLE_OFFENSE", data=train, kind="count", size=20) # Though range is more, it looks discrete
#sns.factorplot(x="X_15", hue="MULTIPLE_OFFENSE", data=train, kind="count", size=20)  #Highest at 34


# In[ ]:





# In[569]:


#continuous  vs categorical
#sns.FacetGrid(train, hue="MULTIPLE_OFFENSE",size=20).map(sns.kdeplot, "X_12").add_legend()
#sns.FacetGrid(train, hue="MULTIPLE_OFFENSE",size=20).map(sns.distplot, "X_12").add_legend()

sns.FacetGrid(train[train['X_12']>16], hue="MULTIPLE_OFFENSE",size=20).map(sns.distplot, "X_12").add_legend()

#We conclude here that values X_12 > 17 always have MULTIPLE_OFFENSE=1

#sns.FacetGrid(train, hue="MULTIPLE_OFFENSE",size=10).map(sns.distplot, "X_8").add_legend()
#sns.FacetGrid(train[train['X_8']>20], hue="MULTIPLE_OFFENSE",size=10).map(sns.kdeplot, "X_8").add_legend()

#We conclude here that values X_8 >= 20 always have MULTIPLE_OFFENSE=1


# In[570]:


sns.FacetGrid(train,hue='MULTIPLE_OFFENSE',size=4).map(plt.scatter,"X_6","X_7").add_legend();

# These plots are not helpful, since its quite difficult to get any inference


# In[571]:


#train.filter(like='X_', axis=1).columns
features = train.filter(like='X_', axis=1).columns

PairPlotData=train[features].join(train['MULTIPLE_OFFENSE'])
sns.pairplot(PairPlotData)

# This is not a good way to view pairwise plots , especially when there are many features


# In[572]:


corr=train.filter(like='X_', axis=1).join(train['MULTIPLE_OFFENSE']).corr()
sns.heatmap(corr,cmap="YlGnBu")


# In[573]:


#removing the diagnol elements in heatmap

mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(7, 5))
    ax = sns.heatmap(corr, mask=mask, cmap="YlGnBu", square=True)


# In[574]:


#Checking correlation of all fields with MULTIPLE_OFFENSE

print (corr['MULTIPLE_OFFENSE'].sort_values(ascending=False)[:5], '\n') #top 5 values
print ('----------------------')
print (corr['MULTIPLE_OFFENSE'].sort_values(ascending=False)[-5:]) #last 5 values

#here we see MULTIPLE_OFFENSE does'nt have a good correlation with any of the X_ columns


# In[575]:


#Checking correlation of all fields with each other

print (corr['X_2'].sort_values(ascending=False)[:3], '\n') #top 3 values
print ('----------------------')
print (corr['X_2'].sort_values(ascending=False)[-3:]) #last 3 values

#here we see MULTIPLE_OFFENSE does'nt have a good correlation with any of the X_ columns

#Correlated elements: [X2,X3]-0.99,[X_10,X_12]-0.877


# In[576]:


import plotly.express as px
#df = px.data.iris()
fig = px.scatter_3d(train, x='X_10', y='X_11', z='X_14',log_x=True,
    log_y=False,
    log_z=False,color='MULTIPLE_OFFENSE')
fig.show()


# In[577]:


get_ipython().run_line_magic('pinfo', 'px.scatter_3d')


# In[578]:


#Box plots- Multivariate analysis

sns.FacetGrid(train, col="X_1", hue="MULTIPLE_OFFENSE").map(sns.kdeplot, "X_11").add_legend()


# In[579]:


#Trying to do a Chi-Square test

table_1=pd.crosstab(train['X_2'],train['X_4'])
print(table_1)

val=stats.chi2_contingency(table_1)

Observed_Values = table_1.values 
print("Observed Values :-\n",Observed_Values)


# In[580]:


val


# In[581]:


Expected_Values=val[3]


# In[582]:


Expected_Values


# In[583]:


no_of_rows=table_1.shape[0]
no_of_columns=table_1.shape[1]
ddof=(no_of_rows-1)*(no_of_columns-1)
print("Degree of Freedom:-",ddof)
alpha = 0.05


# In[584]:


from scipy.stats import chi2
chi_square=sum([(o-e)**2./e for o,e in zip(Observed_Values,Expected_Values)])
chi_square_statistic=chi_square[0]+chi_square[1]


# In[585]:


print("chi-square statistic:-",chi_square_statistic)


# In[586]:


critical_value=chi2.ppf(q=1-alpha,df=ddof)
print('critical_value:',critical_value)


# In[587]:


#p-value
p_value=1-chi2.cdf(x=chi_square_statistic,df=ddof)
print('p-value:',p_value)
print('Significance level: ',alpha)
print('Degree of Freedom: ',ddof)


# In[588]:


if chi_square_statistic>=critical_value:
    print("Reject H0,There is a relationship between 2 categorical variables")
else:
    print("Retain H0,There is no relationship between 2 categorical variables")
    
if p_value<=alpha:
    print("Reject H0,There is a relationship between 2 categorical variables")
else:
    print("Retain H0,There is no relationship between 2 categorical variables")


# In[589]:


#Using Chi Square test, I have seen if there is a relationship between categorical variables
#X10,X_12 -- There is a relationship between 2 categorical variables
#X_1,X_2 --There is no relationship between 2 categorical variables
#X_2,X_3--There is a relationship between 2 categorical variables
#X_2,X_4--There is a relationship between 2 categorical variables

#But the chi-quare test will not give us proper inferences, 
#the target label is skewed and most of the categories are also skewed


# In[590]:


train[train['X_12'].isna()].MULTIPLE_OFFENSE.value_counts()


# In[591]:


#Since we came to a conclusion from our plots that anything above X_12=16 is hacked, we will replace these null values with some 
#common 999.

train['X_12']=train['X_12'].fillna('999')


# In[595]:


#Train-Test split

from sklearn import model_selection

features = ['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7',
       'X_8', 'X_9', 'X_10', 'X_11', 'X_12', 'X_13', 'X_14', 'X_15', 'YEAR', 'MONTH', 'DAY_OF_WEEK']
X = train[ features ]
y = train['MULTIPLE_OFFENSE']

X_train, X_eval, y_train, y_eval = model_selection.train_test_split(X, y, test_size=0.1, random_state=1)


# In[599]:


#Implementing Adaboost

from sklearn import tree,ensemble

base_estimator = tree.DecisionTreeClassifier()
ada_estimator = ensemble.AdaBoostClassifier(base_estimator)
ada_grid = {'base_estimator__max_depth': [3,4,5], 'n_estimators':list(range(30, 200, 50)), 'learning_rate':[0.1,0.3,0.5,1.0]}
ada_grid_estimator = model_selection.GridSearchCV(ada_estimator, ada_grid, scoring='recall', cv=10)
ada_grid_estimator.fit(X_train, y_train)


# In[600]:


print(ada_grid_estimator.best_params_)
print(ada_grid_estimator.best_score_)
print(ada_grid_estimator.best_estimator_.estimators_)
print(ada_grid_estimator.score(X_train, y_train))


# In[601]:


print(ada_grid_estimator.score(X_eval, y_eval))


# In[604]:


#Data Preprocessing for test set

test.DATE=pd.to_datetime(test.DATE)
test['YEAR'], test['MONTH'] = test['DATE'].dt.year, test['DATE'].dt.month
test['DAY_OF_WEEK']=(pd.DatetimeIndex(test.DATE).dayofweek).astype(int)
test['X_12']=test['X_12'].fillna('999')
X_test = test[features]


# In[605]:


#Predict on test set
test['MULTIPLE_OFFENSE'] = ada_grid_estimator.best_estimator_.predict(X_test)
test.to_csv('submission_10June.csv', columns=['INCIDENT_ID', 'MULTIPLE_OFFENSE'], index=False)


# In[606]:





# In[607]:





# In[611]:




