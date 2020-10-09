# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:55:25 2020

@author: Bhargav
"""

#Very similar to a box plot. With this plot you have 
#removed the box part of the box plot 
#and replaced it with the kde curve we saw from the distplot() function.
#kde can allow us to see the modality of your distribution.Its bi-modal here.

#Note: kde curves can look smooth with small amounts of data

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
sns.violinplot(boston_df['INDUS'], orient="v")
# Remove excess chart lines and ticks for a nicer looking plot
sns.despine()