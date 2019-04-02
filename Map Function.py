#!/usr/bin/env python
# coding: utf-8

# In[1]:


get = ['three ', 'nine ', 'your ', '.', 'it ',  'you ', 'it ', 'me ',  'more '] 
low = ['six ', 'damn ', 'fine ',  ' Move ', 'till ', 'sock ', 'to ', 'one ', 'time'] 


# In[2]:


# using the map function
get_low = map(lambda list1, list2: list1 + list2, get, low)


# In[3]:


# checking output
print(get_low)


# In[4]:


# converting map object to a list to print
print(list(get_low))

