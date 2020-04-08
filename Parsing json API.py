#!/usr/bin/env python
# coding: utf-8

# # Parsing public json API for New York City Bike sharing 

# In[1]:


import json
from urllib.request import urlopen


# In[3]:


with urlopen("http://citibikenyc.com/stations/json") as response:
    source = response.read()


# In[19]:


#print(source)

data= json.loads(source)
print(json.dumps(data,indent=2))


# In[36]:


print('No. of available bikes:')
for available in data['stationBeanList']:
    print(available['stationName'],':',available['availableBikes'],'/',available['totalDocks'])


# In[ ]:




