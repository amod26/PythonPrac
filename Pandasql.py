#!/usr/bin/env python
# coding: utf-8

# ## We can install the Pandasql with a quick pip:
# 
# 

# In[1]:


# pip install pandasql


# In[3]:


import pandasql
import seaborn as sns

data = sns.load_dataset('iris')


# In[4]:


data.head(20)


# ## With pandasql we can write out our standard SQL query in the exact same way we normally do when running it on an SQL database. Just pass the name of the pandas dataframe as the name of the table you are parsing and the data will be retrieved

# In[5]:


sub_data = pandasql.sqldf("SELECT * FROM data LIMIT 20;", globals())
print(sub_data)


# ## The regular filtering operations that we can do with WHERE in SQL are also applicable. Let’s pull all the data where petal_length is greater than 5 using pandas first

# In[13]:


sub_data = data[data["petal_length"] > 5.0]
sub_data.head()


# ## To do it in SQL, we certain rows simply add our WHERE call to do the same filtering:
# 
# 

# In[11]:


sub_data = pandasql.sqldf("SELECT * FROM data WHERE petal_length > 5.0;", globals())
print(sub_data.head())


# ## We can of course, always select only the columns we want as well:
# 
# 

# In[17]:


sub_data = pandasql.sqldf("SELECT petal_width, petal_length FROM data WHERE petal_length > 5.0;", globals())
print(sub_data.head(10))


# In[ ]:




