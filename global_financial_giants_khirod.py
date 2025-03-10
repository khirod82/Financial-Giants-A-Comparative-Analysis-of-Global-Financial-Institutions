# -*- coding: utf-8 -*-
"""Global Financial Giants_Khirod.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uaI60F-ahpS_FBj7Ce5tZ4QBH0BUeecG
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/financial services companies.csv')
df.head()

import matplotlib.pyplot as plt
# Check for missing values
print(df.isnull().sum())

# Summary statistics
print(df.describe())

# Data types of each column
print(df.dtypes)

# Distribution of numerical features
plt.figure(figsize=(5, 3))
sns.histplot(df['Revenue in (USD Million)'], kde=True)
plt.title('Distribution of Revenue')
plt.show()

plt.figure(figsize=(5, 3))
sns.histplot(df['Net Income in (USD Millions)'], kde=True)
plt.title('Distribution of Net Income')
plt.show()

plt.figure(figsize=(5, 3))
sns.histplot(df['Total Assest in (USD Millions)'], kde=True)
plt.title('Distribution of Total Assets')
plt.show()

# Relationship between revenue and net income
plt.figure(figsize=(5, 3))
sns.scatterplot(x='Revenue in (USD Million)', y='Net Income in (USD Millions)', data=df)
plt.title('Revenue vs. Net Income')
plt.show()

# Relationship between revenue and total assets
plt.figure(figsize=(5, 3))
sns.scatterplot(x='Revenue in (USD Million)', y='Total Assest in (USD Millions)', data=df)
plt.title('Revenue vs. Total Assets')
plt.show()

# Count of companies by industry
plt.figure(figsize=(5, 3))
sns.countplot(x='Industry', data=df)
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability
plt.title('Number of Companies per Industry')
plt.show()

# Boxplot of revenue by industry
plt.figure(figsize=(6, 3))
sns.boxplot(x='Industry', y='Revenue in (USD Million)', data=df)
plt.xticks(rotation=45, ha='right')
plt.title('Revenue Distribution by Industry')
plt.show()

# Correlation matrix
correlation_matrix = df[['Revenue in (USD Million)', 'Net Income in (USD Millions)', 'Total Assest in (USD Millions)']].corr()
plt.figure(figsize=(4, 3))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()