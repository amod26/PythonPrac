#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[3]:


### Return the current working directory
os.getcwd()


# In[9]:


### Create a single folder
os.mkdir("/users/senorpete/Desktop/PythonPrac")


# In[13]:


### Create folders recursively
### The below line creates a folder "Documents" with a subfolder 
### inside it called "Data Science Projects" with a subfolder inside ### that one called "Project 1"
os.makedirs("/users/senorpete/Desktop/PythonPrac/Project 1")


# In[14]:


### List all of the files and sub-directories in a particular folder
os.listdir("/users/senorpete/Desktop/PythonPrac")


# In[16]:


f= open("/users/senorpete/Desktop/PythonPrac/test.txt","w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
f.close()


# In[18]:


### Delete a file 
os.remove("/users/senorpete/Desktop/PythonPrac/test.txt")  


# In[19]:


## Delete a folder
os.rmdir("/users/senorpete/Desktop/PythonPrac/Project 1")  


# In[ ]:


### Rename a file or folder
os.rename("My Documents", "Your Documents")


# In[ ]:




