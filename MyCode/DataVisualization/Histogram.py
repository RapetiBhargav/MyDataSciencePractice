# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:48:52 2020

@author: Bhargav
"""

from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Set the palette and style to be more minimal
sns.set(style='ticks', palette='Set2')

# Load data as explained in introductory lesson
boston_data = load_boston()
boston_df = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)

# Create the histogram plot
sns.distplot(boston_df.NOX, kde=False)

#You can see the increased variance by increasing the number of bins.
sns.distplot(boston_df.NOX, bins=100, kde=False)

#it plots the shape of the distribution.
sns.distplot(boston_df.NOX, kde=True)

# Remove excess chart lines and ticks for a nicer looking plot
sns.despine()