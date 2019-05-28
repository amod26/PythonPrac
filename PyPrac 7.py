#!/usr/bin/env python
# coding: utf-8

# # Return True if the string "cat" and "dog" appear the same number of times in the given string.
# 
# 

# In[1]:


def cat_dog(str):
    return str.count("cat")==str.count("dog")

cat_dog('1cat1cadodog') 


# # Return the number of times that the string "hi" appears anywhere in the given string.
# 
# 

# In[4]:


def count_hi(str):
    return str.count("hi")
count_hi('abc hi ho hi')


# # Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

# In[6]:


def lucky_sum(a, b, c):
    sum = 0
    list = [a,b,c,13]
    for n in list[:list.index(13)]:
        sum += n
    return sum
lucky_sum(1, 2, 13) 


# In[ ]:




