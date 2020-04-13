#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import re
from urllib.request import urlopen
import csv


# In[2]:


with urlopen("https://opendata.ecdc.europa.eu/covid19/casedistribution/json/") as response:
    source = response.read()


# In[3]:


data= json.loads(source)
#print(json.dumps(data,indent=2))


# In[5]:


records = data['records'] 

# now we will open a file for writing 
data_file = open('Dailycount.csv', 'w') 


# In[6]:


# create the csv writer object 
csv_writer = csv.writer(data_file) 

# headers to the CSV file 
count = 0


# In[7]:


for rec in records: 
    if count == 0: 
  
        # Writing headers of CSV file 
        header = rec.keys() 
        csv_writer.writerow(header) 
        count += 1
  
    # Writing data of CSV file 
    csv_writer.writerow(rec.values()) 
  
data_file.close()


# In[ ]:




