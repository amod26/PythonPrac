#!/usr/bin/env python
# coding: utf-8

# In[1]:


import shutil 
import os


# In[ ]:


# copy files from source to destination
shutil.copy('/Users/senorpete/Desktop/src/1.txt', '/Users/senorpete/Desktop/des')


# In[3]:


# move files from source to destination
shutil.move('/Users/senorpete/Desktop/src/1.txt', '/Users/senorpete/Desktop/des')


# In[16]:


#will remove the folder at path, and all files and folders it contains will also be deleted.
shutil.rmtree('/Users/senorpete/Desktop/src')


# ## Using send2trash is much safer than Python’s regular delete functions, because it will send folders and files to your computer’s trash or recycle bin instead of permanently deleting them

# In[17]:


import send2trash


# In[21]:


baconFile = open('/Users/senorpete/Desktop/src/bacon.txt', 'a') # creates the file


# In[22]:


baconFile.write('Bacon is not a vegetable.') #writes inside
baconFile.close() #closes after writing


# In[24]:


send2trash.send2trash('/Users/senorpete/Desktop/src/bacon.txt') # sends to trash 


# In[ ]:




