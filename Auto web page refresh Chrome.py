
# coding: utf-8

# # Script for automatically refreshing chrome webpage.

# First we install selenium via terminal which is an open source tool which is used for automating the tests carried out on web browsers (Web applications are tested using any web browser). 

# In[ ]:

# pip install -U selenium


# Then we install Chromedriver which is a separate executable that WebDriver uses to control Chrome. <br>
# 

# In[ ]:

# brew cask install chromedriver


# In[ ]:

from selenium import webdriver
import time


# In[ ]:

driver = webdriver.Chrome()

driver.get('Enter your url')
while True:
    time.sleep('Enter time in seconds')
    driver.refresh()
driver.quit()


# In[ ]:



