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
rfi_counts.plot(kind='bar', title='Frequency of RFI By Theme')
plt.xlabel('RFI Theme')
plt.ylabel('RFI')
plt.show()
'''
Key Trends Identified:
RFI (AML/CTF and sanctions) are distributed evenly accross all board. However, Sanctions-related RFI accounts for 56.97% of RFIs, while AML/CTF- related RFIs makes up the remaining 43.2135% if active accounts alone are considered, suggesting a focus area for further investigation.
'''

'''
2. Partner Banks Generating RFIs:
I grouped data by `PARTNER BANK` to understand which banks submitted the highest number of RFIs.
'''
#partner_rfi = data.groupby('Partner bank')['Transaction ID'].count()
#partner_rfi.plot(kind='bar', title='RFIs by Partner Bank')
#plt.xlabel('Partner Bank')
#plt.ylabel('Number of RFIs')
#plt.show()

partner_rfi = data.groupby('Partner bank')['Transaction ID'].count()
partner_rfi.plot(kind='pie', autopct='%1.1f%%', title='RFIs by Partner Bank')
plt.show()
'''
Key Trends Identified:
Indicates Bank A and B are responsible for 67.901% Overall RFIs reports/suspension and 66% of suspension considering (active accounts alone), warranting a deeper dive into their transaction patterns.
'''

'''
3. Impact of Previous Suspensions:**
I analyzed accounts with a history of suspensions to determine whether they were more likely to be flagged.
'''
#previous_suspensions = data['Previous Suspensions'].value_counts()
#print(previous_suspensions)
# Group by 'PREVIOUS SUSPENSIONS' and 'TRANSFER STATUS' to see the comparison
suspension_comparison = pd.crosstab(data['Previous Suspensions '], data['Transfer Status'], margins=True)
print(suspension_comparison)

# Visualizing the comparison with a bar chart
suspension_comparison.drop(index='All', columns='All').plot(
    kind='bar',
    stacked=True,
    figsize=(10, 6),
    title='Comparison of Previous Suspensions and Current Transfer Status'
)
plt.xlabel('Previous Suspension Status')
plt.ylabel('Number of Accounts')
plt.legend(title='Current Transfer Status', loc='upper right')
plt.show()

'''
Key Trends Identified:
Indicates/Confirms accounts with prior suspensions were 78.26% more likely to receive new RFIs overall and 94.12% more likely to receive new RFIs when considering (active accounts alone), highlighting the importance of monitoring repeat offenders.
'''

'''
4. Geographic Patterns - CUSTOMER ADDRESS COUNTRY:
Analyzed RFIs by CUSTOMER ADDRESS COUNTRY to identify regions with higher scrutiny.
'''
country_rfi = data['Customer Address Country'].value_counts()
country_rfi.plot(kind='bar', title='RFIs by Customer Country')
plt.xlabel('Customer Address Country')
plt.ylabel('Number of RFIs')
plt.show()
'''
Key Trends Identified:
Indicates on average, Customers from countries Germany to UK accounted for the high RFI flags, with UK and UAE ranking the highest. 
'''

'''
5. Geographic Patterns - RECIPIENT COUNTRY:
Analyzed RFIs by RECIPIENT COUNTRY to identify regions with higher scrutiny.
'''
country_rfi = data['Recipient Country'].value_counts()
country_rfi.plot(kind='bar', title='RFIs by Recipient Country')
plt.xlabel('Recipient Address Country')
plt.ylabel('Number of RFIs')
plt.show()

'''
Key Trends Identified:
Indicates on average, Recipient across between Switzerland to UK accounted for the high RFI flags, with UK and Japan ranking the highest. 
'''

'''
6. Account Type Trends:
Investigated differences in RFIs between business and personal accounts.
'''
account_type_rfi = data.groupby('Account type')['Transaction ID'].count()
account_type_rfi.plot(kind='pie', autopct='%1.1f%%', title='RFIs by Account Type')
plt.show()
'''
Key Trends Identified:
Indicates Business accounts were involved in 59.26% of RFIs, compared to 40.74% Personal account. This suggests higher scrutiny for business accounts
'''

'''
7. Suspended Transactions and Amounts:
To examine whether transaction amounts influenced suspensions.
'''
# Plot average transaction amount by transfer status
# # Aggregate data for bar chart
transfer_status_summary = data.groupby('Transfer Status')['Amount (USD)'].agg(['mean', 'sum']).reset_index()

plt.figure(figsize=(10, 6))
plt.bar(transfer_status_summary['Transfer Status'], transfer_status_summary['mean'], color=['blue', 'red'])
plt.title('Average Transaction Amount by Transfer Status')
plt.xlabel('Transfer Status')
plt.ylabel('Average Transaction Amount (USD)')
plt.show()

'''
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
All displayed chart are from Tableau. Tableau present clearer and more relatable chart.Albeit when code is run it produces similar chart.

Tableau visualizations tool provide actionable insights and highlighted key patterns in the data.

---
Step 4: Findings and Recommendations

Key Trends Identified:
1. RFI concerns (AML/CTF and Sanction concerns are the most common RFI theme.
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
