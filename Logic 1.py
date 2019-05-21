#!/usr/bin/env python
# coding: utf-8

# # You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
# 
# 

# In[1]:


def date_fashion(you, date):
    if you <= 2 or date <=2:
        return 0
    elif you >=8 or date >=8:
        return 2
    else:
        return 1
    
date_fashion(5, 10) 


# # The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.
# 
# 

# In[2]:


def love6(a, b):
    return a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6

love6(6, 4) 


# # Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
# 
# 

# In[4]:


def alarm_clock(day, vacation):
    week_preset = "7:00" if not vacation else "10:00"
    weekend_preset = "10:00" if not vacation else "off"
    return week_preset if day not in [6,0] else weekend_preset
alarm_clock(0, False) 


# # You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases

# In[6]:


def caught_speeding(speed, is_birthday):
    speeding = speed - (65 if is_birthday else 60)
    if speeding > 20:
        return 2
    elif speeding > 0:
        return 1
    else:
        return 0
caught_speeding(65, False) 


# In[ ]:




