
# coding: utf-8

# ## Installing Pyperclip
# > pip install pyperclip

# In[ ]:

import pyperclip,re


# In[ ]:

pyperclip.copy('Hello!')


# In[ ]:

pyperclip.paste()


# ## Step1: Creating regex for phone number

# In[ ]:

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # separator
(\d{3}) # first 3 digits
(\s|-|\.) # separator
(\d{4}) # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
  )''', re.VERBOSE)


# ## Step 2: Creating regex for Email 

# In[ ]:

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+ # username
@ # @ symbol
[a-zA-Z0-9.-]+ # domain name
(\.[a-zA-Z]{2,4}) # dot-something
  )''', re.VERBOSE)


# ## Step 3: Find all the matches in the Clip Board Text

# In[ ]:

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])


# ## Step 4: Join the matches into string and intro the clipboard

# In[ ]:

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('All copied to Clipboard : ')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails was found! ')


# ## Running this program

# For an example, open your web browser to the No Starch Press contact page at http://www.nostarch.com/contactus.htm, press ctrl-A to select all the text on the page, and press ctrl-c to copy it to the clipboard.

# In[ ]:



