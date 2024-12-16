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

Suggested Next Steps:
The is need to review our Sanction policies to see if we are uptodate. This entails meeting with the right team/stakeholder. And then passing to senior management for 
for approval.
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

Suggested Next Steps:
We need to engage with partner banks submitting the most RFIs to understand their concerns and improve processes.
Sometimes after perform our due diligence as company (Analyze transaction routes), with good reason awe can reroute,
payments through less risky corridors or intermediaries to minimize RFIs flags.
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
Key Trends Identified: Accounts with prior suspensions are at higher risk of further investigation.
In the chart above, accounts with prior suspensions were 78.26% more likely to receive new RFIs overall and 94.12% more likely to receive new RFIs when considering (active accounts alone), highlighting the importance of monitoring repeat offenders.

Suggested Next Steps:
Develop a focused review framework for accounts with previous suspensions, such as;
Establish a dedicated risk category for accounts with prior suspensions and apply enhanced transaction monitoring protocols.
Conduct periodic reviews of accounts with prior suspensions to reassess their risk and determine if continued enhanced monitoring is necessary.(E.g Wise BRC review model).
Work closely with internal compliance and fraud detection teams to develop tailored monitoring rules for previously suspended accounts.
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
Key Trends Identified: Customers from certain countries experience higher scrutiny.
The chart above indicates on average, Customers from countries Germany to UK accounted for the high RFI flags, with UK and UAE ranking the highest. 

Suggested Next Steps:
Implement an enhanced due diligence (EDD) process for customers from countries flagged as high-risk.
Adopt a risk-based approach to monitor transactions from high-scrutiny countries.
Partner with relevant team in wise/ compliance expert in the flagged regions to understand local regulations and practices.
Collaborate with regulators/Partner banks to understand specific concerns associated with flagged countries.
Worst Case scenario, temporarily suspend that transaction route till we figure out that the is to mitigate riske for Wise
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
Key Trends Identified: recipients from certain countries experience higher scrutiny.
The chart above, Indicates on average, recipient across between Switzerland to UK accounted for the high RFI flags, with UK and Japan ranking the highest. 

Suggested Next Steps:
Implement an enhanced due diligence (EDD) process for customers from countries flagged as high-risk.
Adopt a risk-based approach to monitor transactions from high-scrutiny countries.
Partner with relevant team in wise/ compliance expert in the flagged regions to understand local regulations and practices.
Collaborate with regulators/Partner banks to understand specific concerns associated with flagged countries.
Worst Case scenario, temporarily suspend that transaction route till we figure out that the is to mitigate riske for Wise
'''

'''
6. Account Type Trends:
Investigated differences in RFIs between business and personal accounts.
'''
account_type_rfi = data.groupby('Account type')['Transaction ID'].count()
account_type_rfi.plot(kind='pie', autopct='%1.1f%%', title='RFIs by Account Type')
plt.show()
'''
Key Trends Identified: Business accounts are flagged more frequently than personal accounts.
In the chart above, Business accounts were involved in 59.26% of RFIs, compared to 40.74% Personal account. This suggests higher scrutiny for business accounts

Suggested Next Steps:
We need to work with relevant team to review/revise our internal RFI Policies. Majorly our AML policies as we have high AML/CTF flags of our business account.
Introduce stricter onboarding and ongoing due diligence processes tailored to business accounts. 
Analyze business accounts by industry or sector and assign risk levels based on sector-specific attributes- In DD, business are onbaorded with different level of scrutiny based on Wise internal AML risk score, that I believe was generated due data's like this
Establish tailored transaction monitoring rules for business accounts, focusing on abnormal patterns such as unusually high transaction amounts or frequencies. (VELOCITY REVIEW) in Wise
'''

'''
7. Account Entity Trends:
Investigated differences in RFIs between business and personal accounts.
'''
account_Entity_rfi = data.groupby('RFI entity')['Transaction ID'].count()
account_Entity_rfi.plot(kind='pie', autopct='%1.1f%%', title='RFIs by RFI Entity')
plt.show()
'''
Key Trends Identified: 
In the chart above, recipient were involved in 56.79% of RFIs, compared to 43.21% Wise customer. This suggests higher scrutiny for Recipients.

Suggested Next Steps:
Tighten due diligence processes for transactions sent to high-risk regions or countries with elevated recipient flags.
Conduct periodic reviews of frequently flagged recipients to identify common patterns or risks, such as repeated involvement in high-value or suspicious transactions.

'''

'''
8. Suspended Transactions and Amounts:
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
Key Trends Identified: Larger transaction amounts are more likely to be suspended.
In the chart above, suspended transactions considering on Active account tended to involve higher amounts, which could indicate a correlation between transaction size and risk.

Suggested Next Steps:
Introduce tiered thresholds for monitoring high-value transactions based on risk levels.
Require enhanced due diligence (EDD) for larger transactions- Like the creating of HAT TEAM and the HVT team.
Adjust transaction limits dynamically based on the customer's risk profile.
Provide clear guidance to customers on the documents required for high-value transactions.
'''
########################################################################################################################

### Step 3: Visualization in Tableau

'''
No data cleaning or export necessary

data.to_csv('processed_data.xlsx', index=False)
data.to_csv('processed_data.csv', index=False)
data2.to_excel('blogme_clean.xlsx', sheet_name = 'blogmedata', index=False)
'''

'''
All displayed chart are from Tableau. Tableau present clearer and more relatable chart.Albeit when code is run it produces similar chart.

Tableau visualizations tool provide actionable insights and highlighted key patterns in the data.

---
Step 4 :  Recommendations

In General:
1. We need engage with partner banks submitting the most RFIs to understand their concerns and improve processes and streamline our compliance protocols accordingly.

I believe these insights and recommendations will support Wise in enhancing its financial crime prevention strategies while improving operational efficiency. Please find the Python code, Tableau visualizations, and summary PDF attached for your review.

'''
