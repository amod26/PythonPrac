#!/usr/bin/env python
# coding: utf-8

# In[1]:


from faker import Faker


# In[2]:


fake = Faker()
fake.name()


# In[3]:


fake.text()


# In[4]:


fake.timezone()


# In[5]:


for i in range(10):
    print('Hey',fake.name() + '!')


# In[6]:


fake.catch_phrase()


# In[7]:


# only gives Indian names
Ind = Faker('hi-IN') # localized provider


# In[8]:


Ind.name()


# In[9]:


fake.address()


# In[10]:


fake.sentence()


# In[ ]:




