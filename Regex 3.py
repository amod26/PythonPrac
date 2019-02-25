
# coding: utf-8

# In[1]:

import re


# ## Case - Insensitive Matching
# > include re.I or re.IGNORECASE to make regex case insensitive

# In[11]:

g1 = re.compile('jack Sparrow', re.I)
g1.findall("Why is the rum gone JACK SpArrOw")


# ## Substituting strings 
# > The regular expression \d+\s\w+ will match text that has one or more numeric digits (\d+), followed by a whitespace character (\s), followed by one or more letter/digit/underscore characters (\w+).

# In[18]:

a1=re.compile('Pass: \w+')
a1.sub('*****','Name: Jack Pass: Sparrow')


# In[75]:

j=re.compile('Jack',re.I)
j.sub('****', 'Jack Sparrow is Notorious,jack was Jack ')


# In[77]:

agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')


# In[ ]:



