
# coding: utf-8

# ## Findall()
# > In addition to the search() method, Regex objects also have a findall() method. While search() will return a Match object of the first matched text in the searched string, the findall() method will return the strings of every match in the searched string.

# In[2]:

import re


# In[3]:

phonenumregex=re.compile('\d\d\d-\d\d\d-\d\d\d\d')
phonenumregex.findall('Cell 222-333-4444 & work 111-333-4444')


# ## Character Classes
# > 
# \d Any numeric digit from 0 to 9. <br>
# \D Any character that is not a numeric digit from 0 to 9. <br>
# \w Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.) <br>
# \W Any character that is not a letter, numeric digit, or the underscore character.<br> 
# \s Any space, tab, or newline character. (Think of this as matching “space” characters.) <br>
# \S Any character that is not a space, tab, or newline.

# In[8]:

charclass=re.compile('[aeiouAEIOU]')
charclass.findall('There is a sea shell ON THE SEA SHELL')


# ## By placing a caret character (^) just after the character class’s opening bracket, you can make a negative character class.
# > A negative character class will match all the characters that are not in the character class

# In[14]:

charclass=re.compile('[^aeiouAEIOU]')
d=charclass.findall('There is a sea shell ON THE SEA SHELL')
print(d)


# ## Wildcard Character
# > The . (or dot) character in a regular expression is called a wildcard and will match any character except for a newline.

# In[16]:

wild=re.compile('.at')
wild.findall('that cat had a hat while he sat with a bat')


# ## Matching everything with dot star
# > Sometimes you will want to match everything and anything. For example, say you want to match the string 'First Name:', followed by any and all text, followed by 'Last Name:', and then followed by anything again. <br> You can use the dot-star (.*) to stand in for that “anything.” Remember that the dot character means “any single character except the newline,” and the star character means “zero or more of the preceding character.”

# In[25]:

name=re.compile('Firstname: (.*) Lastname: (.*)')
a=name.search('Firstname: Jack Lastname: Sparrow')
a.group(1)


# In[21]:

a.group(2)


# In[26]:

a.groups()


# In[ ]:



