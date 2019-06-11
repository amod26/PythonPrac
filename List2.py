#!/usr/bin/env python
# coding: utf-8

# #  Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1

# # def count_evens(nums):
#     count = 0
#     for n in nums:
#         count -= n%2-1
#     return count
# count_evens([2, 1, 2, 3, 4])
# 

# # Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

# In[2]:


def sum67(nums):
  count =0
  blocked= False
  for n in nums:
    if n == 6:
      blocked = True
      continue
    if n == 7 and blocked:
      blocked = False
      continue
    if not blocked:  
      count += n
  
  return count
sum67([1, 2, 2, 6, 99, 99, 7])


# # Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

# In[4]:


def big_diff(nums):
  return max(nums)-min(nums)

big_diff([7, 2, 10, 9]) 


# # Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
# 
# 

# In[5]:


def has22(nums):
  for i,v in enumerate(nums[:-1]):
    if v == 2 and nums[i+1] == 2:
      return True
  return False

has22([1, 2, 1, 2]) 





