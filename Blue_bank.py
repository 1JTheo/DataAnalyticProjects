# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 09:40:44 2024

@author: odube
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:03:47 2024

@author: odube
"""
# PROJECT 2
"""
Project 1: Sales Analysis for Value Inc

Value Inc is a retail store that sells household items all over the world by bulk. 

The Sales Manager has no sales reporting but he has a brief idea of current sales but doesn’t have any reporting system to help him make decisions.

He also has no idea of the ---> monthly cost <---- , ---> profit <--- and ---> top selling products <--- . He wants a dashboard on this and says the data is currently stored in an excel sheet.


GUIDE TO SOLUTION

1. Data Cleaning
2. Data transforming
3. Cal monthly cost and adding it to the table
4.Data exporting

"""

#1 Bring the data into my workspace or script 
# I need functions from the Data analysis LIBRARY call

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# READING imported data file - in this case Json data file

#json_file = open('loan_data_json.json')
#data = json.load(json_file)

with open('loan_data_json.json') as json_file:
    data=json.load(json_file)
    #print(data)

# transform data into a data frame with Pandas
loandata = pd.DataFrame(data)

#finding unique value from the PURPOSE COLUMN
loandata['purpose'].unique()

#describe  - used for Statistical description of a dataset
loandata.describe()

#using EXP() to get the annual income
income = np.exp(loandata['log.annual.inc'])

#Adding it back to our data
loandata['AnnualIncome'] = income

# Rating 'Fico' score using conditional statement forloop and loc for 'int.rate' 
ficocat=[]

for x in range(0, len(loandata)):
    category = loandata['fico'][x]
    if category >= 300 and category < 400: 
        cat = 'Very Poor'
    elif category >= 400 and category < 600: 
        cat = 'Poor'
    elif category >= 600 and category < 660: 
        cat = 'Fair'
    elif category >= 660 and category < 700: 
        cat = 'Good'
    elif category >= 700: 
        cat = 'Excellent'
    else:
        cat = 'unknown'
        
    ficocat.append(cat)


#convert to series
ficocat = pd.Series(ficocat)

#adding to loandata
loandata['fico.category'] = ficocat

# Rating 'int.rate' score using conditional 'loc statement'
loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

# prepare data extraction to perform quick diagram ploting
# counting individual loan borrower based on the fico cat created above and putting them in a group
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar()
plt.show()

purposeplot = loandata.groupby(['purpose']).size()
purposeplot.plot.bar(color = 'purple', width = 0.7)
plt.show()

#scatter plot

plt.scatter(loandata['AnnualIncome'], loandata['dti'])
plt.show()


#writing to csv

loandata.to_csv('loanDataCleaned.csv', index=True)