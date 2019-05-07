#!/usr/bin/env python
# coding: utf-8

# In[19]:


d={'c':"India", 'Capital':"Delhi", 'PM':"Modi"}


# In[26]:


print(d['c'])


# In[32]:


list=[5,69,220,1,4,6,7,10]
#list = [int(i) for i in list]


# In[37]:


list.sort(reverse=True)
print(list)


# In[52]:


print(min(list))


# In[53]:


print(max(list))


# In[55]:


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
Bob = User('Bob', 20)
Alice = User('Alice', 30)
Leo = User('Leo', 15)
L = [Bob, Alice, Leo]


# In[59]:


w="word"
print(len(w))


# ## If the array has < 2 numbers return 0 else return the second smallest number.

# In[99]:


arr=[0],[0,1],[4,2,13,10]

def smallno():
    for i in arr:
        print(i)
        if len(i)<2:
            print(0)
        else:
            arr1=i.sort()
            print(i[1])
smallno()


# In[171]:


def remove(duplicate):
    final_list=[]
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
duplicate=[2,4,6,4,2,8,6]
print(remove(duplicate))


# In[ ]:




