# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 21:05:13 2020

@author: Bhargav
"""

#When exploring medium-dimensional data, a useful approach is to draw multiple 
#instances of the same plot on different subsets of your dataset. 
#This technique is sometimes called either “lattice” or “trellis” plotting, 
#and it is related to the idea of “small multiples”.

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
flights = sns.load_dataset("flights")
# Subset the data to years >= 1956 to more easily fit on the plot
flights = flights[flights.year >= 1956]

g = sns.FacetGrid(flights, row="year", margin_titles=True)
#Once we have our FacetGrid, we call the map function in order to map data onto our grid. 
#In this example, we use a line plot from Matplotlib.
g.map(plt.plot, "passengers", color="steelblue")