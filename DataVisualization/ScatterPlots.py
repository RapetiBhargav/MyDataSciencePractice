# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:59:39 2020

@author: bhargav
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

# Create the scatter plot
sns.lmplot(x="CRIM", y="NOX", data=boston_df)
# Remove excess chart lines and ticks for a nicer looking plot
sns.despine()


#By default, it plots a regression line so you can see potential linear relationships more 
#easily. Our variables appear to be somewhat positively correlated. 
#The lighter shade around the line is the 95% confidence interval for our regression line and
#is calculated using bootstraps of our data.

