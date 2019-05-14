#!/usr/bin/env python
# coding: utf-8

# # Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

# In[1]:


def reverse3(nums):
    return nums[::-1]
reverse3([1, 2, 3]) 


# # Given an int array length 2, return True if it contains a 2 or a 3.

# In[3]:


def has23(nums):
    for i in nums:
        if i == 2 or i==3:
            return True
    return False
has23([2, 5]) 


# # Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.

# In[7]:


def common_end(a, b):
    if a[0]==b[0] or a[:-1] == b[:-1]: 
        return True
    else:
        return False
    if len(a)>=1 and len(b)>=1:
        return True
    return False
common_end([1, 2, 3], [7, 3, 2]) 


# # Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
# 
# 

# In[8]:


def reverse3(nums):
    return nums[::-1]

reverse3([5, 11, 9]) 


# # Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

# In[9]:


def middle_way(a, b):
    return [a[1] , b[1]]
middle_way([7, 7, 7], [3, 8, 0]) 


# # Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.

# In[11]:


def make_ends(nums):
    for i in nums:
        return [nums[0],nums[-1]] 
    
make_ends([7, 4, 6, 2]) 


# In[ ]:




