#!/usr/bin/env python
# coding: utf-8

# In[1]:


# normal Python function
def shouting(word, shout):
#All caps words and adds exclamation points

    shouts = word.upper() + ('!' * shout)
    return shouts


# In[2]:


shouts = lambda word, shout: word.upper() + ('!' * shout)


# As you can see we wrote a lot less code here to achieve the same result. This is the essence of lambda they simplify your code.

# ## Filter() function
# > The filter() function offers a way to filter out elements from a list that don’t meet certain criteria.

# In[3]:


nums = [1, 5, 4, 6, 8, 11, 3, 12]


# In[4]:


even_numbers = list(filter(lambda x: (x%2 == 0) , nums))


# In[5]:


print(even_numbers)


# ## Reduce() Function
# >The reduce() function is useful for performing  computations on a lists. In order to use it we need to import it from the functools library.

# In[6]:


from functools import reduce


# In[7]:


nums = [10, 72, 13, 4, 9, 52]


# In[8]:


# Use reduce() to apply a lambda function over nums: sum
sum = reduce(lambda item1, item2: item1 + item2, nums)


# In[9]:


print(sum)


# In[ ]:




