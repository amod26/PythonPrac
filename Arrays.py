#!/usr/bin/env python
# coding: utf-8

# Creating an array

# In[2]:


import array as arr
import numpy as np


# In[14]:


from array import *


# In[3]:


arr.array


# In[4]:


val= array('i',[2,4,5,6,7,8,8])
print(val.buffer_info)


# Add or remove elements in the array

# In[5]:


#val.append(3)
#val.remove()
print(val)


# Reversing Array

# In[6]:


val.reverse()
print(val)


# Indexing

# In[7]:


print(val[0],val[4])


# Using loop boop boop (printing all elements on different lines) when you know the length of array)

# In[8]:


for i in range(6):
    print(val[i])


# When you don't know the length of array

# In[9]:


for i in range(len(val)):
    print(val[i])


# Squaring the output

# In[10]:


sq = array(val.typecode,(a*a for a in val))
for e in sq:
    print(e)
    


# Taking input from user

# In[17]:


arr = array('i',[])


# In[18]:


n=int(input("Enter the length of array:"))
for i in range(n):
    x = int(input("Enter the next value:"))
    arr.append(x)


# finding the value:

# In[23]:


val=int(input("Enter the value for search:"))
k=0

for e in arr:
    if e==val:
        print(k)
        break
    
    k+=1
#OR

print(arr.index(val))


# In[3]:


np. arange(0,10)


# In[4]:


np.zeros(3)


# In[5]:


np.ones(3)


# In[7]:


np.zeros((3,3))


# In[8]:


np.ones((3,3))


# In[10]:


arr=  np.arange(1,25)
arr


# In[13]:


arr1 = np.random.randint(0,25,10)
arr1


# In[ ]:




