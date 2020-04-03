# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:47:46 2020

@author: Bhargav
"""
#Bar plots can be useful when comparing categories.

from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Set the palette and style to be more minimal
sns.set(style='ticks', palette='Set2')

# Load data as explained in introductory lesson
boston_data = load_boston()
boston_df = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)

# Only keep for ages 96 and 98.2
boston_df = boston_df[boston_df["AGE"].isin([96, 98.2])]

# Create the bar plot
sns.barplot(boston_df['AGE'], boston_df['NOX'])
# Remove excess chart lines and ticks for a nicer looking plot
sns.despine()

#Seaborn also plots the error bars (the black lines). 
#The error bars are calculated via bootstrapping which randomly resamples our data 
#with replacement. It then draws 95% error bars which are the 95th and 5th percentiles.