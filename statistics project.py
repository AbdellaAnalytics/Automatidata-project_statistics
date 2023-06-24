#!/usr/bin/env python
# coding: utf-8

# # Automatidata project 
# **Course 4 - The Power of Statistics**

# You are a data professional in a data consulting firm, called Automatidata. The current project for their newest client, the New York City Taxi & Limousine Commission (New York City TLC) is reaching its midpoint, having completed a project proposal, Python coding work, and exploratory data analysis.
# 
# You receive a new email from Uli King, Automatidata’s project manager. Uli tells your team about a new request from the New York City TLC: to analyze the relationship between fare amount and payment type. A follow-up email from Luana includes your specific assignment: to conduct an A/B test. 
# 
# A notebook was structured and prepared to help you in this project. Please complete the following questions.
# 

# ### Task 1. Imports and data loading

# Import packages and libraries needed to compute descriptive statistics and conduct a hypothesis test.

# In[2]:


import pandas as pd
import numpy as np
from scipy import stats


# In[4]:


# Load dataset into dataframe
taxi_data = pd.read_csv("2017_Yellow_Taxi_Trip_Data.csv", index_col = 0)


# ### Task 2. Data exploration
# 
# Use descriptive statistics to conduct Exploratory Data Analysis (EDA). 

# **Note:** In the dataset, `payment_type` is encoded in integers:
# *   1: Credit card
# *   2: Cash
# *   3: No charge
# *   4: Dispute
# *   5: Unknown
# 
# 

# In[52]:


taxi_data.head()
taxi_data.describe(include='all')


# In[71]:


credit = taxi_data[taxi_data['payment_type'] == 1]['total_amount']
cash = taxi_data[taxi_data['payment_type'] == 2]['total_amount']
no_charge = taxi_data[taxi_data['payment_type'] == 3]['total_amount']
Dispute = taxi_data[taxi_data['payment_type'] == 4]['total_amount']
Unknown = taxi_data[taxi_data['payment_type'] == 5]['total_amount']






# You are interested in the relationship between payment type and the total fare amount the customer pays. One approach is to look at the average total fare amount for each payment type. 

# In[ ]:


print(taxi_data.groupby('payment_type').count()
taxi_data.groupby('payment_type')['fare_amount'].mean()


# Based on the averages shown, it appears that customers who pay in credit card tend to pay a larger total fare amount than customers who pay in cash. However, this difference might arise from random sampling, rather than being a true difference in total fare amount. To assess whether the difference is statistically significant, you conduct a hypothesis test.

# 
# ### Task 3. Hypothesis testing
# 
# Before you conduct your hypothesis test, consider the following questions where applicable to complete your code response:
# 
# 1. Recall the difference between the null hypothesis and the alternative hypotheses. Consider your hypotheses for this project as listed below.
# 
# $H_0$: There is no difference in the average total fare amount between customers who use credit cards and customers who use cash.
# 
# $H_A$: There is a difference in the average total fare amount between customers who use credit cards and customers who use cash.

# 
# 
# Your goal in this step is to conduct a two-sample t-test. Recall the steps for conducting a hypothesis test: 
# 
# 
# 1.   State the null hypothesis and the alternative hypothesis
# 2.   Choose a signficance level
# 3.   Find the p-value
# 4.   Reject or fail to reject the null hypothesis 
# 
# 

# **Note:** For the purpose of this exercise, your hypothesis test is the main component of your A/B test. 

# You choose 5% as the significance level and proceed with a two-sample t-test.

# In[73]:


stats.ttest_ind(a=credit, b=cash, equal_var=False)


# ## DECISION TO ACCEPT OR REJECT THE NULL HYPOTHESIS

# Since the p-value is significantly smaller than the significance level of 5%, i reject the null hypothesis.
# i conclude that there is not a statistically significant difference in the average total fare amount between customers who use credit cards and customers

# ### Task 4. Communicate insights with stakeholders

# *Ask yourself the following questions:*
# 
# 1. What business insight(s) can you draw from the result of your hypothesis test?
# 2. Consider why this A/B test project might not be realistic, and what assumptions had to be made for this educational project.

# # The Answer

# The key business insight is that encouraging customers to pay with credit cards can generate more revenue for taxi cab drivers.
# 
# This project requires an assumption that passengers were forced to pay one way or the other, and that once informed of this requirement, they always complied with it. The data was not collected this way; so, an assumption had to be made to randomly group data entries to perform an A/B test. This dataset does not account for other likely explanations. For example, riders might not carry lots of cash, so it's easier to pay for longer/farther trips with a credit card. In other words, it's far more likely that fare amount determines payment type, rather than vice versa. The difference between average card payment fare and cash fare is inflated, because we use the total amount as the comparing variable. But cash fares all have tip values of $0, while card payments have non-zero values. A possible reason for this occurance is because cash tips aren't declared. In turn, this means that we capture tips in one group but not in the other. Instead, one could compare the fare_amount column.
