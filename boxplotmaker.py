#!/usr/bin/python3

#Simple script for making boxplots with given csv -file
import pandas as pd
import matplotlib.pyplot as plt
from time import sleep

#add csv file to dataframe
try:
    dataFrame = pd.read_csv("data.csv")

    # Create boxplot with number of observations (sample size) and own title
    noobs = dataFrame["Variables"].count()
    print("Please insert title for the graph: ")
    titleBoxplot = input()
    titleNoobs = "n= ", noobs 

    #Blue boxplot
    boxplot = dataFrame.boxplot(figsize = (5,5), showmeans=True, color = 'blue', vert=False)

    #add main title
    plt.title(titleBoxplot)
    #add right title
    plt.title(titleNoobs, loc="right")
    #print the boxplot
    plt.show()

    #Same again, but with a vertical boxplot
    boxplot = dataFrame.boxplot(figsize = (5,5), showmeans=True, color = 'blue', vert=True)
    plt.title(titleBoxplot)
    plt.title(titleNoobs, loc="right")
    
    plt.show()

    with open('statistics.txt', 'w') as f:
        print((dataFrame.describe()), file=f)
#In case of error some instructions for the users   
except FileNotFoundError:
    print("Did not find the data.csv -file")
    sleep(5)
except KeyError:
    print("Something wrong with the data.") 
    print("The title in the sheet should be \"Hours\". Each occurrence must be in its own cell in the same column.\n")
    print("Example: \n")
    print("Variables")
    print("10")
    print("3")
    print("45")
    print("33")
    sleep(10)
