# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:14:41 2020

@author: Bhargav
"""

from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA

def separate_data(component_data, labels,
                  label_names):
  separated_data = []
  for class_label in range(len(label_names)):
    separated_data.append(get_label_info(
      component_data, labels, class_label, label_names))
  return separated_data

def get_label_info(component_data, labels,
                   class_label, label_names):
  label_name = label_names[class_label]
  print(component_data)
  label_data = component_data[labels == class_label]
  #labels == class_label -- This actually returns a list of True or False
  return (label_name, label_data)


bc = load_breast_cancer()
pca_obj = PCA(n_components=2)
component_data = pca_obj.fit_transform(bc.data)
labels = bc.target
label_names = bc.target_names
# Using the completed separate_data function
separated_data = separate_data(component_data,
                              labels, label_names)

# Plotting the data
import matplotlib.pyplot as plt
for label_name, label_data in separated_data:
  col1 = label_data[:, 0]  # 1st column (1st pr. comp.)
  col2 = label_data[:, 1]  # 2nd column (2nd pr. comp.)
  plt.scatter(col1, col2, label=label_name) # scatterplot
plt.legend()  # adds legend to plot
plt.title('Breast Cancer Dataset PCA Plot')
plt.show()


