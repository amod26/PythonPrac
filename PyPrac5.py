#!/usr/bin/env python
# coding: utf-8

# # When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
# 
# 

# In[2]:


def cigar_party(cigars, is_weekend):
    if is_weekend:
        return cigars>=40
    else:
        return cigars>=40 and cigars<=60
    
cigar_party(30, False) 


# # #Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
# 
# 

# In[3]:


def sorta_sum(a, b):
    return 20 if a+b in range(10,20) else a+b
sorta_sum(9, 4) 


# # The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.

# In[6]:


def squirrel_play(temp, is_summer):
    if 60 <= temp <= 90:
        return True
    elif is_summer and 60<=temp<=100:
        return True
    return False
squirrel_play(95, False)


# In[ ]:




