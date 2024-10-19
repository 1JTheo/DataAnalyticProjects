# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:03:47 2024

@author: odube
"""
# PROJECT 1 
"""
Project 1: Sales Analysis for Value Inc

Value Inc is a retail store that sells household items all over the world by bulk. 

The Sales Manager has no sales reporting but he has a brief idea of current sales but doesn’t have any reporting system to help him make decisions.

He also has no idea of the ---> monthly cost <---- , ---> profit <--- and ---> top selling products <--- . He wants a dashboard on this and says the data is currently stored in an excel sheet.


GUIDE TO SOLUTION

1. Data Cleaning
2. Data transforming
3. Cal monthly cost and adding it to the table

"""

#1 Bring the data into my workspace or script 
# I need functions from the Data analysis LIBRARY called PANDA

import pandas as pd

# file_name = pd.read_csv('file_name.csv') <---- the read your data file - the IMPORT

#Data_file = pd.read_csv('transaction.csv')

#use this because the data in this data frame is saparated by ; and not ,
Data_file_Proper = pd.read_csv('transaction.csv',sep=';')

# Cal monthly cost of each itema and adding it to the table
'''
1. Get TotalCostPerItem =  CostPerItem * NumberOfItemsPurchased
2. Add this section to a column on the table
'''
Data_file_Proper['TotalCostPerItem'] = Data_file_Proper['CostPerItem'] * Data_file_Proper['NumberOfItemsPurchased']
Data_file_Proper['TotalSellingPricePerItem'] = Data_file_Proper['SellingPricePerItem'] * Data_file_Proper['NumberOfItemsPurchased']

#Profit calculation
Data_file_Proper['ProfitPerTransaction'] = Data_file_Proper['TotalSellingPricePerItem'] - Data_file_Proper['TotalCostPerItem']

#Profit Mark up = the percentage of profit made = ProfitPerTransaction/TotalCostPerItem
Data_file_Proper['ProfitMarkUp'] = round((Data_file_Proper['ProfitPerTransaction'] / Data_file_Proper['TotalCostPerItem']),2) 

# Looking ata the data file, we can see that the year,Month and day are written separately.
# We want to put them together, but Year and day are 'intergers' so we must change them to be able to add them together

Data_file_Proper['DateInFull'] = Data_file_Proper['Day'].astype(str)+' - '+Data_file_Proper['Month']+' - ' + Data_file_Proper['Year'].astype(str)


# Uisng split to split client_keyWords field
split_col = Data_file_Proper['ClientKeywords'].str.split(',' , expand = True)

#Creating a new column for the splitted columns in Client_KeyWord
Data_file_Proper['ClientAge']= split_col[0]
Data_file_Proper['ClientType']=split_col[1]
Data_file_Proper['LengthOfContract'] = split_col[2]


#Removing the ' sign with replace function
Data_file_Proper['ClientAge']= Data_file_Proper['ClientAge'].str.replace('[', '')
#Data_file_Proper['ClientType']=split_col[1]
Data_file_Proper['LengthOfContract'] = Data_file_Proper['LengthOfContract'].str.replace(']','')

#using lowercase function
Data_file_Proper['ItemDescription'] = Data_file_Proper['ItemDescription'].str.lower()


#Bringing in Value Inc dATA file
Data_value_inc_Proper = pd.read_csv('value_inc_seasons.csv',sep=';')
# Uisng split to split client_keyWords field
#split_col = Data_file_Proper['ClientKeywords'].str.split(',' , expand = True)


#Merge two data file together
Data_file_Merged = pd.merge(Data_file_Proper, Data_value_inc_Proper, on = 'Month')

# Drop some columns that not necessary at this point
Data_file_Proper_formated= Data_file_Merged.drop(['ClientKeywords', 'Day', 'Year', 'Month' ], axis =1)


#Export New data for Tableu use
Data_file_Proper_formated.to_csv('valueInc_Cleaned.csv', index = False)
