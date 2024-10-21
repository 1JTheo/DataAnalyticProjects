# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:11:44 2024

@author: odube
"""
# Reading  the file

#import json
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# READING imported data file - in this case Json data file

data = pd.read_excel('articles.xlsx')

#describe my data
data.describe()

data.info()

#want to know number of article by source = grouby function
data.groupby(['source_id'])['article_id'].count()

#want to know number of comment reacived by an article by source = grouby function
data.groupby(['source_id'])['engagement_reaction_count'].sum()

#droping column engagement_comment_plugin_count, remember axis = 1 mean it is a columne/list not anything else.

data2 = data.drop('engagement_comment_plugin_count', axis = 1)

'''
Keyword = 'crash'

#creating a loop to isolate each title row and pick certain words from it

Keyword_flag = []

for x in range(0,len(data2)):
    heading = data2['title'][x]
    try:
        if Keyword in heading:
            flag = 1
        else:
            flag = 0
    except:
        flag = 0
    Keyword_flag.append(flag)
'''   

#transfermong that device above to a calculator machine called FUNCTION

def KeyWordPicker(keyword):
    
    Keyword_flag = []
    
    for x in range(0,len(data2)):
        
        heading = data2['title'][x]
        
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        
        Keyword_flag.append(flag)
    
    return Keyword_flag

Keywordflag=KeyWordPicker('murder')


#Adding keyword_flag to Data2

data2['Keyword_flag']= pd.Series(Keywordflag)


'''SENTIMENT ANALYSIS or OPINION MINNING - not always accurate'''

# SentimentIntensityAnalyzer

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

for x in range(0,len(data2)):
    try:
        sent_int =  SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(data2['title'][x])
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0  
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data2['title_neg_sentiment'] = title_neg_sentiment
data2['title_pos_sentiment'] = title_pos_sentiment
data2['title_neu_sentiment'] = title_neu_sentiment

# exporting final result to excel

data2.to_excel('blogme_clean.xlsx', sheet_name = 'blogmedata', index=False)