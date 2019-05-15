#!/usr/bin/env python
# coding: utf-8

# # Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

# In[2]:


def first_last6(nums):
    return 6 in [nums[0],nums[-1]]
first_last6([13, 6, 1, 2, 3]) 


# # Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
# 
# 

# In[3]:


def rotate_left3(nums):
    return [nums[1],nums[2],nums[0]]
rotate_left3([5, 11, 9]) 


# # Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
# 
# 

# In[6]:


def sum2(nums):
    return sum(nums[:2])
sum2([1, 1, 1, 1])


# # Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
# 
# 

# In[7]:


def common_end(a, b):
    return a[0]==b[0] or a[-1]==b[-1]
common_end([1, 2, 3], [7, 3, 2]) 


# # Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
# 
# 

# In[8]:


def same_first_last(nums):
    return len(nums)>=1 and nums[0]==nums[-1]
same_first_last([1, 2, 3, 1])


# # Given an array of ints length 3, return the sum of all the elements.

# In[9]:


def sum3(nums):
    return sum(nums)
sum3([5, 11, 2]) 


# In[ ]:




