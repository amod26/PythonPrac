#!/usr/bin/env python
# coding: utf-8

# 6. Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

# In[3]:


word = input("Enter a word: ")

word=str(word)
rvs=word[::-1]
print(rvs)
if word == rvs:
    print("This word is a palindrome!")
else:
    print("This word is not a palindrome.")


# 7. Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

# In[24]:


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 

b=print([x for x in a if x % 2 == 0])


# 8. Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
# 
# 

# In[69]:


u1= input("1st player Enter Rock, Paper, Scissors: ")
u2= input("2nd player Enter Rock, Paper, Scissors: ")

if u1 == u2:
    print("It's a tie!")
elif u1 == 'Rock':
    if u2 == 'Scissors':
        print("Rock wins!")
    else:
        print("Paper wins!")
elif u1 == 'Scissors':
    if u2 == 'Paper':
        print("Scissors win!")
    else:
        print("Rock wins!")
elif u1 == 'Paper':
    if u2 == 'Rock':
        print("Paper wins!")
    else:
        print("Scissors win!")
else:
        print("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()
        


# 9. Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

# In[95]:


import random

a= random.randint(1,10)
count= 0
guess=0

while ask!=a and ask!='exit':
    ask=int(input("Enter a number: "))
    
    if ask== 'exit':
        break
    
    count+=1
    ask=int(ask)
    
    if ask < a:
        print("Aim higher!")
    elif ask > a:
        print("Aim lower!")
    else:
        print("Perfect Match!")
        print("Kudos! You guessed it in " + str(count) + " tries!")


# 10. Take two lists, say for example these two:
# 
# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension.

# In[145]:


import random
a = random.sample(range(100),5)
b = random.sample(range(100),8)

result= [i for i in a if i in b]
print(result)

