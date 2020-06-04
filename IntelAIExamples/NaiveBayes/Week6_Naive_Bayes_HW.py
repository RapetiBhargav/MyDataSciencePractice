#!/usr/bin/env python
# coding: utf-8

# # Naive Bayes

# ## Introduction
# 
# We will start by working on the Iris dataset. Recall that Iris dataset contains iris species and sepal and petal measurements. We will quickly explore the dataset and jump into Naive Bayes.

# In[ ]:


from __future__ import print_function
import os
#Data Path has to be set as per the file location in your system
#data_path = ['..', 'data']
data_path = ['data']


# ## Question 1
# 
# * Load the Iris dataset.
# * Take a quick look at the data types.
# * Look at the skew values and decide if any transformations need to be applied. You can use skew value 0.75 as a threshold.
# * Use `sns.pairplot` to plot the pairwise correlations and histograms. Use `hue="species"` as a keyword argument in order to see the distribution of species.

# In[ ]:


import pandas as pd
import numpy as np
#The filepath is dependent on the data_path set in the previous cell 
filepath = os.sep.join(data_path + ['Iris_Data.csv'])
data = pd.read_csv(filepath, sep=',', header=0)


# In[ ]:


data.dtypes


# Notice that aside from the predictor variable, everything is float.

# In[ ]:


skew = pd.DataFrame(data.skew())
skew.columns = ['skew']
skew['too_skewed'] = skew['skew'] > .75
skew


# Fields are not too badly skewed.

# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.pairplot(data, hue='species')


# ## Question 2
# 
# Let's now fit a Naive Bayes classifier to this data in order to predict "species".
# 
# * Pick the appropriate type of Naive Bayes given the nature of your dataset (data types of columns). Recall, choices are
#     * GaussianNB
#     * MultinomialNB
#     * BernoulliNB
# * Use `cross_val_score` to see how well your choice works.

# In[ ]:


# Since the features are continuous, the right choice is GaussianNB

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score
X = data[data.columns[:-1]]
y = data.species

GNB = GaussianNB()
cv_N = 4
scores = cross_val_score(GNB, X, y, n_jobs=cv_N, cv=cv_N)
print(scores)
np.mean(scores)


# ## Question 3:
# 
# Now let's try all types of Naive Bayes and observe what happens
# 
# * Compare the cross validation scores for Gaussian, Bernouilli and Multinomial Naive Bayes.
# * Why is BernoulliNB performing like it does?

# In[ ]:


from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
X = data[data.columns[:-1]]
y = data.species
nb = {'gaussian': GaussianNB(),
      'bernoulli': BernoulliNB(),
      'multinomial': MultinomialNB()}
scores = {}
for key, model in nb.items():
    s = cross_val_score(model, X, y, cv=cv_N, n_jobs=cv_N, scoring='accuracy')
    scores[key] = np.mean(s)
scores


# Looks like BernoulliNB results are very bad, but MultinomialNB is doing a very good job.
# 
# Why are the results of Bernoulli bad? Find out the reason.

# ## Question 4:
# 
# Let's see what happens when we take away the predictive features.
# 
# * Check the pairplot histograms (diagonal) you produced above and identify the two most predictive features visually.
# * Remove the *petal_* features which are very predictive, and re-do the comparison above. That is, get the cross validation scores for all types of Naive Bayes.

# In[ ]:


X = data[['sepal_length', 'sepal_width']]
y = data.species

nb = {'gaussian': GaussianNB(),
      'bernoulli': BernoulliNB(),
      'multinomial': MultinomialNB()}

# Try other variants on the lines shown in the previous cell for GaussianNB and compare the results on scoring = 'accuracy'. 
# Run the piece of code as shown in array in question 3


# #Come up with your observations after taking away the very predictive features, which model works better

# ## Question 5
# 
# This question explores how Naive Bayes algorithms can be affected when we push the underlying (naive) assumption too much. Recall that the naive assumption is that the features in the training set are *independent* from each other.
# 
# * Create **0, 1, 3, 5, 10, 50, 100** copies of `sepal_length` and fit a `GaussianNB` for each one.
# * Keep track of the save the average `cross_val_score`.
# * Create a plot of the saved scores over the number of copies.

# In[ ]:


X = data[data.columns[:-1]]
y = data.species

n_copies = [0, 1, 3, 5, 10, 50, 100]


def create_copies_sepal_length(X, n):
    X_new = X.copy()
    for i in range(n):
        X_new['sepal_length_copy%s' % i] = X['sepal_length']
    return X_new


def get_cross_val_score(n):
    X_new = create_copies_sepal_length(X, n)
    scores = cross_val_score(GaussianNB(), X_new, y, cv=cv_N, n_jobs=cv_N)
    return np.mean(scores)


avg_scores = pd.Series(
    [get_cross_val_score(n) for n in n_copies],
    index=n_copies)

ax = avg_scores.plot()
ax.set(
    xlabel='number of extra copies of "sepal_length"',
    ylabel='average accuracy score',
    title='Decline in Naive Bayes performance');


# ## Question 6 - Naive Bayes on Human Activity Recongnition
# 
# In this question, we'll explore discretizing the dataset and then fitting MultinomialNB.  
# 
# * Load the Human Activity Recognition dataset. 
# * Look at the data types. It's all continuous except for the target.
# * Create `X` and `y` from `data`. `y` is the "Activity" column.
# * Create training and test splits.
# * Fit a GaussianNB to the training split.
# * Get predictions on the test set.
# * use `sns.heatmap` to plot the confusion matrix for predictions.

# In[ ]:





# ## Question 7
# 
# Now, let's discretize the dataset from Question 6. There are many ways to do this, but we'll use `pd.DataFrame.rank(pct=True)`.
# 
# a. Create `X_discrete` from `X` using .rank(pct=True)
# 
# b. Look at the values. They are still not discrete. Modify `X_discrete` so that it is indeed discrete. (Hint: try to get the first 2 digits using `.applymap`)
# 
# c. Split `X_discrete` and `y` into training and test datasets
# 
# d. Fit a MultinomialNB to the training split.
# 
# e. Get predictions on the test set.
# 
# f. Plot the confusion matrix for predictions.

# In[ ]:




