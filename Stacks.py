
# coding: utf-8

# # Stacks 

# - Follows LIFO (Last in first out) concept.
# - Linear Data Structures.
# - Flexible size.

# Eg: Going through pages on a website and then pressing back button will take you to the previous number page.<br>
#     for eg: [1,2,3] <- [1,2]

# append() # adds value to the stack <br>
# pop()    # removes value from the stack <br>
# if not   # checks if stack is empty <br>
# [-1]     # points at the last index <br>

# In[27]:

web_session = []       # Creating an empty stack

web_session.append(2)  # adding values to the stack
web_session.append(3)
web_session.append(4) 
print(web_session)     # printing the stack


# In[35]:

# Removing a value from array
last= web_session.pop()  # removes value from stack
print(last)             # prints the last number that was removed 
print(web_session)     # prints the current stack


# In[33]:

# redirecting to the last current page after popping 
print("redirect",web_session[-1])


# In[37]:

# tells user if there are pages remaining
if not (web_session):
    print("disable")
else:
    print("Press Back")

