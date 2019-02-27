
# coding: utf-8

# ## Writing a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. 
# 

# In[ ]:

import pyperclip, re

passwordRegex = re.compile(r'''(
    ^(?=.*[A-Z].*[A-Z])                # at least two capital letters
    (?=.*[!@#$&*])                     # at least one of these special characters
    (?=.*[0-9].*[0-9])                 # at least two numeric digits
    (?=.*[a-z].*[a-z].*[a-z])          # at least three lower case letters
    .{8,}                              # at least 8 total digits
    $
    )''', re.VERBOSE)

def StrongPassCheck():
    ppass = input("Check the strength of your password: ")
    m1 = passwordRegex.search(ppass)
    if (not m1):
        print("Not strong, Try again!")
        return False
    else:
        print("Now that's an strong password! ")
        return True

print("Your password should have 2 capital char, 1 special char, 2 numbers, 3 lower char & min 8 digits.")
StrongPassCheck()


# In[ ]:



