# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:59:39 2020

@author: Bhargav
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
flights_long = sns.load_dataset("flights")
# Pivot the dataset from long to wide format
flights = flights_long.pivot("month", "year", "passengers")

# Create a larger figure size to plot on
#Matplotlib to adjust the figure size to make it larger, (12,6). 
#That returns a value we called “ax”
f, ax = plt.subplots(figsize=(12, 6))

# Create the heat map
sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax, cmap='Blues')