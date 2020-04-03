# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:59:16 2020

@author: Bhargav
"""
# joint plots can plot the histogram of two variables on one plot and 
# also show the scatter plot in the middle

from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Set the palette and style to be more minimal
sns.set(style='ticks', palette='Set2')

# Load data as explained in introductory lesson
boston_data = load_boston()
boston_df = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)

# Create the violin plot
sns.jointplot(boston_df.CRIM, boston_df.NOX, kind="hex")
# Remove excess chart lines and ticks for a nicer looking plot
sns.despine()