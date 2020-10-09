# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 21:17:03 2020

@author: Bhargav
"""

#You pass one parameter which is a dataframe consisting of the columns 
#you wish to plot.

from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Set the palette and style to be more minimal
sns.set(style='ticks', palette='Set2')

boston_data = load_boston()
boston_df = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)

# Create and map the PairGrid
g = sns.PairGrid(boston_df[['CRIM', 'NOX', 'INDUS']])
g.map(plt.scatter);

# Remove excess chart lines and ticks for a nicer looking plot
sns.despine()

#The result reminds me of a correlation matrix