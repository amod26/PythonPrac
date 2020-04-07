#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[48]:


people_string =''' {
	"people": [{
			"name": "John",
			"age": 30,
			"email": "jon@gmail.com",
			"cars": {
				"car1": "Ford",
				"car2": "BMW",
				"car3": "Honda"
			},
			"children": {
				"c1": "Jack",
				"c2": "Jill"
			},
			"phone": "202-456-3214"
		},
		{
			"name": "Tami",
			"age": 28,
			"email": "tami@gmail.com",
			"cars": {
				"car1": "Tesla"
			},
			"children": {
				"c1": "Cylia",
				"c2": "Honey"
			},
			"phone": "232-478-4514"
		}
	]
}
'''


# In[49]:


print(type(people_string))


# In[50]:


type(people_string)


# In[51]:


data = json.loads(people_string)


# In[52]:


for person in data['people']:
    print(person['name']," ",end='')
    print(person['children'])


# In[53]:


for contact in data['people']:
    print(contact['name'],contact['email'],contact['phone'])


# In[55]:


#tidying in json format

tidy = json.dumps(data,indent=3,sort_keys=True)
print(tidy)


# # Loading Data in a file

# In[88]:




with open('people.json','w') as f:
    for contact in data['people']:
        f.write(contact['name']  + " " +  contact['email'] + " " + contact['phone'])
    f.close()


# # Reading data from a file

# In[78]:


with open('/Users/amodpanchal/Desktop/States.json') as f:
    data1=json.load(f)
    
#print(data1)
tidy_data = json.dumps(data1,indent=2)
print(tidy_data)


# In[95]:


for states in data1['states']:
    print(states['name'],states['abbreviation'])


# In[97]:


for states in data1['states']:
    print(states['abbreviation'])


# In[ ]:




