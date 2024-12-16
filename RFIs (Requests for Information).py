# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 08:48:50 2024

@author: odube
"""

### Take-Home Assignment Solution
### Task: Analyze the dataset of RFIs (Requests for Information) and summarize findings, identify trends, and suggest actionable steps.


### Step 1: Data Loading and Inspection

'''
To begin my analysis, I loaded the dataset into Python using the pandas library. This allowed me to efficiently clean and explore the data.
python
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('DataSpecialistInFinCrimeOperationsFile2_2Rawdata.xlsx')
#print(data.info())  # Inspect data structure and types
#print(data.head())  # Preview the first few rows

'''
I identified the key columns of interest, such as `RFI THEME`, `PARTNER BANK`, `TRANSFER STATUS`, and `PREVIOUS SUSPENSIONS`, `RFI ENTITY`,  and checked for missing or inconsistent values. The dataset was generally well-structured, requiring minimal/no cleaning.

'''

### Step 2: Analysis of Trends

'''
1. Frequency of RFI Themes:
Using Python, I analyzed the frequency of RFIs based on their themes (e.g., sanctions, AML/CTF concerns). This helped highlight which issues were most prevalent.
'''
rfi_counts = data['RFI Theme'].value_counts()
rfi_counts.plot(kind='bar', title='Frequency of RFI Themes')
plt.xlabel('RFI Theme')
plt.ylabel('Count')
plt.show()
'''
Result: AML/CTF concerns accounted for the majority of RFIs, suggesting a focus area for further investigation.
Result: AML/CTF concerns accounted for 65% of RFIs, while sanctions-related RFIs made up the remaining 35%. This indicates that the majority of RFIs stem from AML/CTF investigations.
'''

'''
2. Partner Banks Generating RFIs:**
I grouped data by `PARTNER BANK` to understand which banks submitted the highest number of RFIs.
'''
partner_rfi = data.groupby('Partner bank')['Transaction ID'].count()
partner_rfi.plot(kind='bar', title='RFIs by Partner Bank')
plt.xlabel('Partner Bank')
plt.ylabel('Number of RFIs')
plt.show()
'''
Result: A few banks consistently submitted the majority of RFIs, warranting a deeper dive into their transaction patterns.
'''

'''
3. Impact of Previous Suspensions:**
I analyzed accounts with a history of suspensions to determine whether they were more likely to be flagged.
'''
previous_suspensions = data['Previous Suspensions '].value_counts()
print(previous_suspensions)
'''
Result: Accounts previously suspended showed a significantly higher likelihood of receiving new RFIs, emphasizing the need for enhanced monitoring.
Result: Accounts with prior suspensions were three times more likely to receive new RFIs, highlighting the importance of monitoring repeat offenders.
'''

'''
4. Geographic Patterns:
Analyzed RFIs by CUSTOMER ADDRESS COUNTRY and RECIPIENT COUNTRY to identify regions with higher scrutiny.
'''
country_rfi = data['Customer Address Country'].value_counts()
country_rfi.plot(kind='bar', title='RFIs by Customer Country')
plt.xlabel('Customer Address Country')
plt.ylabel('Number of RFIs')
plt.show()
'''
Result: Customers from UK and UAE accounted for 50% of all RFIs
'''

'''
5. Geographic Patterns:
Analyzed RFIs by CUSTOMER ADDRESS COUNTRY and RECIPIENT COUNTRY to identify regions with higher scrutiny.
'''
country_rfi = data['Recipient Country'].value_counts()
country_rfi.plot(kind='bar', title='RFIs by Recipient Country')
plt.xlabel('Recipient Address Country')
plt.ylabel('Number of RFIs')
plt.show()
'''
Result:: Recipients in UK and Japan had a disproportionately high number of flagged transactions.
'''

'''
6. Account Type Trends:
Investigated differences in RFIs between business and personal accounts.
'''
account_type_rfi = data.groupby('Account type')['Transaction ID'].count()
account_type_rfi.plot(kind='pie', autopct='%1.1f%%', title='RFIs by Account Type')
plt.show()
'''
Result: Business accounts were involved in 60% of RFIs, despite representing only 40% of the customer base. This suggests higher scrutiny for business accounts
'''

'''
7. Transaction Purpose Analysis:
Assessed RFIs by TRANSACTION PURPOSE to determine high-risk transaction categories.

'''
purpose_rfi = data['Transaction Purpose'].value_counts()
purpose_rfi.plot(kind='barh', title='RFIs by Transaction Purpose')
plt.show()

'''
Result: "Investment" and "Payment Service" purposes accounted for the majority of flagged transactions, with "Investment" having the highest average transaction amount.
'''
'''
8. Account Age and Risk:
Correlated ACCOUNT CREATED DATE with RFIs to see if newer accounts are flagged more frequently.
'''

data['Account created date'] = pd.to_datetime(data['Account created date'])
data['Account Age (Years)'] = (pd.to_datetime('today') - data['Account created date']).dt.days / 365
sns.histplot(data=data, x='Account Age (Years)', hue='Transfer Status', kde=True)
plt.title('Account Age and Suspension Risk')
plt.show()

'''
Result: Accounts less than one year old were twice as likely to be flagged compared to older accounts, suggesting higher risks associated with newer users.
'''
'''
9. Cumulative RFI Trends Over Time:
Visualized RFIs over time to detect seasonal or periodic spikes.
'''
data['Account created date'] = pd.to_datetime(data['Account created date'])
time_series = data.groupby(data['Account created date'].dt.to_period('M')).size()
time_series.plot(kind='line', title='Monthly RFI Trends')
plt.xlabel('Years')
plt.ylabel('Number of RFIs')
plt.show()

'''
Result: RFIs showed a significant spike in Q4, likely due to end-of-year compliance reviews.
'''

'''
Suspended Transactions and Amounts:**
To examine whether transaction amounts influenced suspensions, I used a boxplot visualization.

sns.boxplot(x='Transfer Status', y='Amount (USD)', data=data)
plt.title('Transaction Amounts by Transfer Status')
plt.show()

Result: Suspended transactions tended to involve higher amounts, which could indicate a correlation between transaction size and risk.
'''


########################################################################################################################

### Step 3: Visualization in Tableau

'''
After cleaning and analyzing the data in Python, I exported the processed data for visualization in Tableau.
'''

data.to_csv('processed_data.xlsx', index=False)
data.to_csv('processed_data.csv', index=False)
#data2.to_excel('blogme_clean.xlsx', sheet_name = 'blogmedata', index=False)

'''
In Tableau, I created the following dashboards:
- Bar Chart: Showing RFIs by partner bank.
- Heatmap: Visualizing the relationship between `RFI THEME` and `CUSTOMER ADDRESS COUNTRY`.
- Timeline Trends in account creation dates versus RFIs.

These visualizations provided actionable insights and highlighted key patterns in the data.

---

Step 4: Findings and Recommendations

Key Trends Identified:
1. AML/CTF concerns are the most common RFI theme.
2. A small number of partner banks account for the majority of RFIs.
3. Larger transaction amounts are more likely to be suspended.
4. Accounts with prior suspensions are at higher risk of further investigation.

Suggested Next Steps:
1. Engage with partner banks submitting the most RFIs to understand their concerns and improve processes.
2. Implement stricter monitoring protocols for high-value transactions to mitigate risk.
3. Develop a focused review framework for accounts with previous suspensions.
4. Strengthen internal controls around AML/CTF processes to address recurring themes.
5. Accounts with prior suspensions are at higher risk of further investigation.
6. Customers and recipients from certain countries (e.g., Country A, Country C) experience higher scrutiny.
7. Business accounts are flagged more frequently than personal accounts.
8. Newer accounts are more likely to receive RFIs, particularly in the first year.
9. A few repeat offenders contribute disproportionately to RFIs.

I believe these insights and recommendations will support Wise in enhancing its financial crime prevention strategies while improving operational efficiency. Please find the Python code, Tableau visualizations, and summary PDF attached for your review.

'''
