#!/usr/bin/env python
# coding: utf-8

# In[15]:


from tkinter import *
import os
os.system('clear')


# In[53]:


# Tkinter GUI

root=Tk()
root.title('Welcome to Earth') # gives title
root.geometry('400x600') # size of the window


# In[54]:


def hello():
    hello_label= Label(root,text='Wassup homies from ' + myTextbox.get() + '!') # gets the input and appends to the function
    hello_label.pack()


# In[55]:


myLabel = Label(root,text="Enter your planet's name:") # Label(where, What= "")
myLabel.pack() # packs everything 


# In[56]:


myTextbox = Entry(root,width=40)
myTextbox.pack()


# In[57]:


myButton= Button(root,text='Submit',command=hello) 
myButton.pack()


# In[ ]:


root.mainloop() # every time you cursor moves, the program will loop instead of quiting


# In[ ]:




