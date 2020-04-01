#!/usr/bin/env python
# coding: utf-8

# # Slicing

# In[44]:


s = 'Computer'


# In[45]:


s[1:]


# In[65]:


s[-3:]


# In[49]:


s[1::2]


# In[51]:


s[::-1].upper()


# # IN & not IN

# In[52]:


print(i in s)


# In[53]:


print(i not in s)


# # Iteration

# In[54]:


x = [2,4,5,6]


# In[60]:


for i in x:
    print(i*2,end =" ") # printing in same line for python 3.7


# In[64]:


for item, index in enumerate(x):
    print(item,index,end='')


# # Sorting

# In[72]:


y = ['dog','cat','horse']
j = [3,6,1,206,20]


# In[75]:


print(sorted(y))
print(sorted(j))


# # If else

# In[78]:


age = int(input())
if age < 17:
    print("You are not allowed to watch this PG-18 movie")
elif age > 55:
    print("You are too old for this shit!")
else:
    print("You good to go!")


# In[ ]:


f_name = input("Name:").strip()
l_name = input("Surname:").strip()
age = int(input("Age:"))
goal = input("Goals:").strip()



print('Hello ' + f_name.capitalize() +' '+  l_name.capitalize()+ "!\n")
print("After 5 years you'll be",age+5, "y/o and would complete your goal of" + goal )


# In[10]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
   if i<5: 
       print(i,end="")


# In[ ]:





# In[ ]:




