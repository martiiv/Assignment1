import pandas as pd #We use pandas for csv file management
import matplotlib as mat #We use matplotlib for div math
import matplotlib.pyplot as plt #Pyplot for plotting scatterplot

trainData = pd.read_csv("a1_train.csv",encoding="UTF-8")    #Read from csv 
x = trainData["AttrX"]                                      #Defining x attribute 
y = trainData["AttrY"]                                      #Defining y attribute
attrClass = trainData["Class"]

colors = {"A":"red", "B":"blue"}                            #We map the colors to the different classtypes from the csv file 

fig = plt.figure(figsize=(8,8))                             #Defining figure   
plt.scatter(x, y, c=attrClass.map(colors))                  #Plotting the scatterplot
plt.show()                                              