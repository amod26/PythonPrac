
# coding: utf-8

# ## To know about flow control in python, we need to learn comparison operators, boolean & loop.

# ### Comparison Operators: <br>
# > == (is equal to) <br>
# != (not equal to) <br>
# < (less than) <br>
# '>' (greater than) <br>
# '<=' (less than equal to) <br>
# '>=' (greater than equal to) <br>
# 

# In[13]:

42==42


# In[14]:

10!=10


# In[15]:

20>100


# In[16]:

100 >= 99


# ### Boolean Operators: <br>
# > True <br>
# > False

# In[23]:

True and True


# In[24]:

True and False


# In[25]:

False or True 


# In[27]:

False or False


# In[29]:

not True


# In[30]:

not False


# ### Mixing Boolean and Comparison

# In[32]:

(2>1) and ( 5<10)


# In[34]:

(5>10) and (10>5)


# ### Flow Control Elements: <br>
# > If statement <br>
# Else statement <br>
# Elif statement

# In[36]:

# using if and else statement
name =input("Enter your name:") 
if name == 'Jack':
    print("Howdy Cap'n")
else:
    print("Hello Stranger")


# In[53]:

# using if, else and elif statement
n1= input("Enter your name:")
age= int(input("Enter your age"))
if n1 == 'Aladin':
    print("Welcome Aladin! I'm Ginie!")
elif age<60:
    print("I'm Ginie, Tell me your wish!")
else: 
    print("You are too old for a wish.")
    


# ### While Loop Statement: <br>
# >    You can make a block of code execute over and over again with a while statement. The code in a while clause will be executed as long as the while statement’s condition is True.

# In[54]:

spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1


# ### Break Statement: <br>
# >    There is a shortcut to getting the program execution to break out of a while loop’s clause early. If the execution reaches a break statement, it immediately exits the while loop’s clause

# In[63]:

while True:
    print('Please type your name:')
    name = input()
    if name == 'Jack': 
        break 
print('Thank you!')


# ### For loop & Range

# In[68]:

print('My name is')
for i in range(5):
    print('Captain Jack Sparrow')


# In[ ]:



