#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('/Users/senorpete/Downloads/Ex_Files_Python_Data_Science_Tips/Exercise Files/data/MonthlyProductSales.csv', encoding='latin-1')


# In[3]:


df.head()


# In[4]:


# show first 10 rows
df.head(n=10)


# In[5]:


# show last 10 rows
df.tail(n=10)


# In[6]:


# show summary stats of the sales column
df.describe()


# In[7]:


df.info()


# In[8]:


# return as a series
s = df['Product Name']

# get count of values
s.value_counts(dropna=False)


# In[ ]:




