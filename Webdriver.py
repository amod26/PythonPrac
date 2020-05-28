#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver


# In[2]:


driver= webdriver.Chrome()
driver.get('https://www.youtube.com')
searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('Casey Neistat')
searchButton= driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()


# In[ ]:





# In[ ]:





# In[ ]:




