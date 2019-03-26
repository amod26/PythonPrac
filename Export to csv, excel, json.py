#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


df = pd.read_csv('/Users/senorpete/Desktop/MonthlyProductSales.csv',  encoding='cp1252')


# In[7]:


# yearly product sales totals
df_export = df.groupby([df['Month of Order Date'].str[:4], 'Product Name']).sum().reset_index()
df_export = df_export.rename(columns={'Month of Order Date': 'Year of Order'})


# In[8]:


# export to csv, check csv when finished
df_export.to_csv('/Users/senorpete/Desktop/YearlyProductSalesTotals.csv', header=True, index=False, encoding='utf-8')


# In[9]:


# export to json, check json when finished
df_export.to_json('/Users/senorpete/Desktop/YearlyProductSalesTotals.json', orient='records')


# In[10]:


# export to excel, check excel file when finished
df_export.to_excel('/Users/senorpete/Desktop/YearlyProductSalesTotals.xlsx', header=True, index=False)


# In[ ]:




