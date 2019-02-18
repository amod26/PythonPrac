
# coding: utf-8

# ## Take integer inputs from user and print the number generated in words.

# ### Using Inflect package: <br>
# inflect.py - Correctly generate plurals, singular nouns, ordinals, indefinite articles; convert numbers to words.<br>
# >pip install inflect

# In[34]:

import inflect 


# In[35]:

p=inflect.engine()


# In[42]:

p1=int(input("Enter your number:"))
print("Your number is:",p.number_to_words(p1))


# ### Taking 2 numbers, concatinate and print the generated number in words.

# In[40]:

t1=int(input("Enter your first number:"))
t2=int(input("Enter your second number:"))
t3= str(t1)+str(t2)
print(t3)
print('Number in words:',p.number_to_words(t3),".")


# ### Using Pynum2word Library

# Install the library via terminal: <br>
# > pip install num2words
# 

# In[61]:

import num2words


# In[62]:

num2words.num2words(20)


# In[64]:

num2words.num2words(1000000)


# In[ ]:



