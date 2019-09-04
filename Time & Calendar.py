#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import datetime
import calendar


# In[2]:


### Get the current date and time
print(datetime.datetime.now())


# In[3]:


### Get just the current time
print(datetime.datetime.now().time())


# In[4]:


start = time.time()
print("hello")
end = time.time()
print(end - start)


# In[5]:


#print calender of the given month,year
yy = 2019
mm = 12
    
# display the calendar  
print(calendar.month(yy, mm))  


# In[6]:


print ("The calender of year 2019 is : ")  
print (calendar.calendar(2020, 3, 1, 2))   # year, width, height , spacing


# In[ ]:




