#!/usr/bin/env python
# coding: utf-8

# # Return the number of times that the string "hi" appears anywhere in the given string.
# 
# 

# In[1]:


def count_hi(str):
    return str.count("hi")
count_hi('hihihihi')


# # Given a string, return a string where for every char in the original, there are two chars.
# 
# 

# In[2]:


def double_char(str):
    new_str = ""
    for char in str:
        new_str += char*2
    return new_str
double_char('Hi-There') 


# # Return True if the string "cat" and "dog" appear the same number of times in the given string.

# In[4]:


def cat_dog(str):
    return str.count('cat') == str.count('dog')

cat_dog('1cat1cadodog') 


# In[ ]:




