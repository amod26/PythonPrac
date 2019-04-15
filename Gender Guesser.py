#!/usr/bin/env python
# coding: utf-8

# > ## pip install gender-guesser

# In[ ]:


import gender_guesser.detector as gender


# In[ ]:


d = gender.Detector()
gen= input("What is your name? ")
print("Seems like you are a",d.get_gender(gen).title(),'.')


# In[ ]:


print(d.get_gender(u"Bob"),gen)


# In[ ]:


print(d.get_gender(u"Sally"))


# ### You can also use a detector that is not case sensitive.

# In[ ]:


d1 = gender.Detector(case_sensitive=False)
print(d1.get_gender(u"sally"))


# In[ ]:


print(d.get_gender(u"Sally"))


# ### Additionally, you can give preference to specific countries:

# In[ ]:


print(d.get_gender(u"Jamie"))


# In[ ]:


print(d.get_gender(u"Jamie", u'great_britain'))


# In[ ]:




