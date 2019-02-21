
# coding: utf-8

# ## Finding phone number from text

# In[1]:

def isPhoneNumber(text):
    if len(text) != 12:
        return(False)
    for i in range(0, 3):
        if not text[i].isdecimal():
            return(False)
    if text[3] != '-':
        return(False)
    for i in range(4, 7):
        if not text[i].isdecimal():
            return(False)
    if text[7] != '-':
        return(False)
    for i in range(8, 12):
        if not text[i].isdecimal():
            return(False)
    return(True)


# In[2]:

print('123-456-7890 is a phone number:')
print(isPhoneNumber('123-456-7890'))
print('Jack Sparrow is a phone number:')
print(isPhoneNumber('Jack Sparrow'))


# ## Taking input from the user and finding the phone number from it!

# In[3]:

t1=input("Enter your msg:")
for i in range(len(t1)): 
    chunk = t1[i:i+12]  
    if isPhoneNumber(chunk):
         print('Phone number found: ' + chunk)
print('Done')


# In[ ]:



