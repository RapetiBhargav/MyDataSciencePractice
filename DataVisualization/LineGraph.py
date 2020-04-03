# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 21:01:28 2020

@author: Bhargav
"""

#Line graphs are very useful for showing a value over time, 
#such as a stock’s price. Typically, one would use a line graph over a scatter plot 
#if there is a connecting component between the values, such as time.

#variations in data along time can be mapped with a line graph.

import seaborn as sns            # importing seaborn functionality    
import pandas as pd
import matplotlib.pyplot as plt
 
flights_long=sns.load_dataset("flights")   # importing dataset
 
# filtering the dataset to obtain the January records for all years
flights_long=flights_long[flights_long.month == 'January']

#plotting a line graph
plot=sns.lineplot(flights_long.year, flights_long.passengers)

