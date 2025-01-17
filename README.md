# Automatidata Project: Fare Amount and Payment Type Analysis
Course: The Power of Statistics
Project: Analyze the relationship between fare amount and payment type for New York City TLC.

# Project Overview
# This project was conducted as part of a collaboration between Automatidata and the New York City Taxi & Limousine Commission (NYC TLC). The objective was to analyze the relationship between fare amounts and payment types and evaluate if significant differences exist between these groups. The analysis includes exploratory data analysis (EDA) and hypothesis testing.

# Key Components
Dataset
The dataset used is 2017_Yellow_Taxi_Trip_Data.csv, which contains trip-level data on fares, payment types, and additional variables.

# Payment Types Encoding:
1: Credit Card
2: Cash
3: No Charge
4: Dispute
5: Unknown
Tasks Completed

# Task 1: Imports and Data Loading
Necessary libraries (Pandas, NumPy, SciPy) were imported, and the dataset was loaded into a DataFrame.

# Task 2: Data Exploration
Conducted exploratory data analysis to understand distributions and descriptive statistics of fare amounts for each payment type.

Used grouping and descriptive statistics to compare average fares between payment types.
# Task 3: Hypothesis Testing
Performed a two-sample t-test to determine whether there is a statistically significant difference in fare amounts between customers who use credit cards and those who pay in cash.

# Task 4: Insights and Recommendations
Interpreted the results of the hypothesis test and communicated actionable business insights.

# Hypothesis Testing
Null Hypothesis ($H_0$):
There is no difference in the average total fare amount between customers who use credit cards and those who use cash.

Alternative Hypothesis ($H_A$):
There is a difference in the average total fare amount between customers who use credit cards and those who use cash.

Methodology:

Significance Level: 5%
Statistical Test: Two-sample t-test
# Results
P-value: The p-value was significantly smaller than 0.05.
Conclusion: Rejected the null hypothesis. There is a statistically significant difference in the average total fare amount between payment types.
# Key Insights
Business Insight: Encouraging credit card payments may result in higher revenue for taxi drivers.
Assumptions and Limitations:
Assumes fare amount and payment type are independent variables, which may not reflect real-world conditions.
Data limitations include the inability to capture undeclared cash tips, which may skew the comparison.
# Files Included
analysis_notebook.ipynb: Jupyter Notebook with full analysis and code.
2017_Yellow_Taxi_Trip_Data.csv: Dataset used for the analysis.
README.md: Project overview and documentation (this file).
