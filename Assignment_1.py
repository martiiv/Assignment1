import pandas as pd #We use pandas for csv file management
import matplotlib
from matplotlib import pyplot as plt #Pyplot for plotting scatterplot
import numpy as np
import scipy 
from sklearn import svm


# Task 1.1 
trainData = pd.read_csv("a1_train.csv",encoding="UTF-8")    #Read from csv 
x = trainData["AttrX"]                                      #Defining x attribute 
y = trainData["AttrY"]                                      #Defining y attribute
attrClass = trainData["Class"]

colors = {"A":"red", "B":"blue"}                            #We map the colors to the different classtypes from the csv file 

fig, ax = plt.subplots(figsize=(8,8))                       #Defining figure and labeling  

plt.xlabel("AttrX")
plt.ylabel("AttrY")
plt.scatter(x, y, c=attrClass.map(colors))                  #Plotting the scatterplot


# Task 1.2
# See a1_task1_2_lines.png

plt.show()                                              