#!/usr/bin/env python
# coding: utf-8

# # Swapping Values

# In[1]:


x,y = 10, 5
print(x,y)


# In[2]:


x,y =y,x
print(x,y)


# # Combining a list of strings into a single one
# 

# In[3]:


sentence = ['Why','is','the','rum','gone','?']
concat_sen = "".join(sentence)
print(concat_sen)


# # Initiallizing a list

# In[4]:


[0]*10


# In[5]:


[7]*10


# # Merging List

# In[6]:


x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)


# # Reversing a String

# In[7]:


name = "Jack Sparrow"
name[::-1]


# # List Comprehension

# In[8]:


a = [1, 2, 3]
b = [i*2 for i in a] # Create a new list by multiplying each element in a by 2
print(b)


# # Iterating over a dictionary

# In[9]:


m = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
for key, value in m.items():
    print('{0}: {1}'.format(key, value))


# # Iterating over list values while getting the index too

# In[10]:


m = ['a', 'b', 'c', 'd']
for index, value in enumerate(m):
    print('{0}: {1}'.format(index, value))


# # Removing useless characters on the end of your string

# In[11]:


name = "Jack "
name_2 = "Sparrow///"
name.strip() # prints "Jack"


# In[12]:


name_2.strip("/") # prints "Sparrow"


# # Found the most frequent value in the list

# In[13]:


test = [1, 2, 3, 4, 2, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key = test.count))


# In[ ]:




