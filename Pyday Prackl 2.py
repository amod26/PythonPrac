#!/usr/bin/env python
# coding: utf-8

# In[29]:


from types import *
import math


def guess_type(x):
    if type(x)==int():
        print ("Value passed in:" + x)
        print("A number was passed.")
    else:
        print("Something else was passed.")

radius = 10
name_of_shape = str("Circle")

area = str(2 * math.pi * radius * radius)

print ("Area of " + name_of_shape + " is " + area)
print ("Variable radius is passed into guess_type")
guess_type(radius)
print ("Variable name_of_shape is passed into guess_type:" )
guess_type(name_of_shape)


# In[32]:


greeting_statement = "Welcome to Strings in Python"

print(greeting_statement.partition('to'))
print(greeting_statement.split())


# In[40]:


def fibonacci(f, l, n):
    t = f + l
    if (t < n):
        print(t)
        return fibonacci(l, t, n)
    else:
        return t

n = int(input("Enter the upper limit of the series : "))
fibonacci(0, 1, n)


# In[ ]:




