#!/usr/bin/env python
# coding: utf-8

# # Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
# 
# 
# front_times('Chocolate', 2) → 'ChoCho' <br>
# front_times('Chocolate', 3) → 'ChoChoCho' <br>
# front_times('Abc', 3) → 'AbcAbcAbc' <br>
# 

# In[28]:


def front_times(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  
  result = ""
  for i in range(n):
    result = result + front
  return result

front_times('Chocolate', 5)


# # Given an array of ints, return the number of 9's in the array.
# 
# 

# In[10]:


def array_count9(nums):
    count = 0
  # Standard loop to look at each value
    for num in nums:
        if num == 9:
            count = count + 1
    return count
array_count9([1, 9, 9, 3, 9]) 


# # Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

# In[29]:


def without_end(str):
    return str[1:-1]
without_end('coding') 


# # Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

# In[30]:


def left2(str):
    return str[2:] + str[:2]
left2('java') 


# # The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
# 
# 

# In[31]:


def make_tags(tag, word):
    return '<'+ tag +'>' + word + '<'+ '/' +tag +'>'  
make_tags('cite', 'Yay') 


# # Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
# 
# 

# In[32]:


def first_two(str):
    return str[:2]
first_two('abcdefg')


# In[ ]:




