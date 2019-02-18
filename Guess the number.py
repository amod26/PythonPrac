
# coding: utf-8

# In[ ]:

import random 
secretNumber = random.randint(1, 20)


# In[ ]:

print("I'm thinking of a number between 1 to 20.")
print("Can you guess which is that number?")
print("You get 5 chances...")


for guessesTaken in range(1,6):
    print("Take a guess..")
    guess=int(input())
    
    if guess < secretNumber:
        print("Your guess is too low!")
    elif guess > secretNumber:
        print("Your guess is too high!")
    else:
        break

if guess == secretNumber:
    print("Damn! you picked the correct number in", str(guessesTaken), "guesses!")
else:
    print("Nope! the number I was thinkng was ", str(secretNumber))
        


# In[ ]:



