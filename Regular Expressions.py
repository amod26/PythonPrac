
# coding: utf-8

# In[1]:

import re


# In[10]:

regex= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=regex.search("Call me on 222-333-4444")
print('Phone number is:', mo.group())


# In[11]:

a1=input('Enter your msg:')
a0=regex.search(a1)
print("Number to call:", a0.group())


# ## Grouping with parenthesis

# In[19]:

b1=input("Enter your msg:")
regex1= re.compile('(\d\d\d)-(\d\d\d-\d\d\d\d)')
b0=regex1.search(b1)
b0.group(1)


# In[20]:

b0.group(2)


# In[21]:

b0.group() # printing everything


# In[22]:

b0.groups() # using plural 


# In[24]:

areaCode, mainNumber = b0.groups() 
print(areaCode)
print(mainNumber)


# ## Matching with multiple groups with Pipe.
# > The | character is called a pipe. You can use it anywhere you want to match one of many expressions. For example, the regular expression r'Batman|Robin' will match either 'Batman' or 'Robin'.

# In[27]:

heroRegex = re.compile ('Batman|Robin') 
mo1 = heroRegex.search('Batman & Robin.') 
mo1.group()


# In[28]:

mo2 = heroRegex.search('Robin & Batman.') 
mo2.group()


# In[29]:

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') 
mo = batRegex.search('Batmobile lost a wheel')
mo.group()


# In[32]:

mo.group() 


# ## Optional Matching with the question Mark
# > Sometimes there is a pattern that you want to match only optionally. That is, the regex should find a match whether or not that bit of text is there. The ? character flags the group that precedes it as an optional part of the pattern.

# In[33]:

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman') 
mo1.group()


# In[34]:

mo2 = batRegex.search('The Adventures of Batwoman') 
mo2.group()


# ## Matching Specific Repetitions with Curly Brackets
# > If you have a group that you want to repeat a specific number of times, fol- low the group in your regex with a number in curly brackets. For example, the regex (Ha){3} will match the string 'HaHaHa', but it will not match 'HaHa', since the latter has only two repeats of the (Ha) group.

# In[35]:

haRegex = re.compile(r'(Ha){3}') 
mo1 = haRegex.search('HaHaHa') 
mo1.group()


# In[36]:

mo2 = haRegex.search('Ha') 
mo2 == None


# In[ ]:



