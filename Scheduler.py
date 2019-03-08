
# coding: utf-8

# In[ ]:

import schedule
import time

def Sec():
    print("I'm Awesome...")
    
def Sec1():
    print("Oh its still true I'm Awesome")
    
def Min():
    print("You know I'm Awesome!")

def Hr():
    print("About time you know that I'm Awesome!")

def Day():
    print("Wake up and see that I'm still Awesome as hell!")

schedule.every(5).seconds.do(Sec)
schedule.every(30).seconds.do(Sec1)
schedule.every(1).minutes.do(Min)
schedule.every(1).hours.do(Hr)

while True:
    schedule.run_pending()
    time.sleep(1)





