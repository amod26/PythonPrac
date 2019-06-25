#!/usr/bin/env python
# coding: utf-8

# # Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!
# 
# 

# In[1]:


def l3():
    a=int(input("Enter 1st:"))
    b=int(input("Enter 2nd:"))
    c=int(input("Enter 3rd:"))
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

print(l3())


# # Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function

# In[2]:


a = [5, 10, 15, 20, 25]

def listend(x):
    return [x[0], x[-1]]

print(listend(a))


# # Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and return the birthday of that person back to them

# In[4]:


birthdays={"dad":'9/4/1957',
          "mom": '8/7/1960',
          "bro": '17/9/1989',
          "self": '26/1/1994'}

print('Welcome to the birthday dictionary. We know the birthdays of:')
for name in birthdays:
    print(name)

print('Who\'s birthday do you want to look up?')
name = input()
if name in birthdays:
    print('{}\'s birthday is {}.'.format(name, birthdays[name]))
else:
    print('Sadly, we don\'t have {}\'s birthday.'.format(name))


# In[ ]:



