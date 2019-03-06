
# coding: utf-8

# In[1]:

import os


# ## Check Current Working directory

# In[4]:

os.getcwd()


# ## Create a new folder 

# In[12]:

os.makedirs('/Users/senorpete/Desktop/Pydesk/pyfol')


# ## Check size of the folder/file

# In[19]:

os.path.getsize('/Users/senorpete/Desktop/Pydesk/pyfol')


# ## Add contents to txt file

# In[86]:

baconFile = open('/users/senorpete/Desktop/Hello.txt', 'w') 
baconFile.write('Hello Pirates!\n') 


# In[87]:

baconFile.close()
baconFile = open('/users/senorpete/Desktop/Hello.txt', 'a')
baconFile.write('Why is the rum gone?') 


# In[88]:

baconFile.close()
baconFile = open('/users/senorpete/Desktop/Hello.txt')
content = baconFile.read()
baconFile.close()
print(content)


# ## Read contents of txt file

# In[89]:

opa = open('/users/senorpete/Desktop/Hello.txt')
content= opa.read()
content


# In[ ]:



