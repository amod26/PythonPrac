#!/usr/bin/env python
# coding: utf-8

# 1. Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# 
# Extras:
# 
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
# 

# In[1]:


import datetime
now = datetime.datetime.now()

name = input("Enter your name: ")
age = int(input("Enter your age: "))

aga = 100 - age
year = now.year + aga

#print(year)
print("Hi "+ name + '!' + " you will turn 100 years old in the year " + str(year) + ".")


# 2. Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
# 
# Extras:
# 
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

# In[2]:


num = int(input("Enter 1st number: "))
num2= int(input("Enter 2nd number: "))

if num % 2 == 0:
    print("Your 1st number is an Even number!")
else:
    print("Your 1st number is an Odd Number!")
    
if num2 % 4 == 0:
    print("Your 2nd number is a Multiple of 4")
else:
    print("Your 2nd number is Not a multiple of 4!")


# 3. a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
# 
# 

# In[3]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 

print([aa for aa in a if aa <= 5])

    


# 4. Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
# 
# 

# In[4]:


div= int(input("Enter a number:"))

listRange = list(range(1,num+1))
div_list=[]

for number in listRange:
    if div % number == 0:
        div_list.append(number)
print(div_list)


# 5. Take 2 lists & write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# In[5]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c=[]

for i in b:
    if i in a:
        c.append(i)

print(c)


# In[ ]:




