#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#life sim


# In[1]:


import random
import time
import random
import numpy as np


# In[2]:


print("hello")
time.sleep(3)
print("there")


# In[3]:


def intro():
    
    print("Welcome you where born in an affair ")
    print("Your name is  ")
    print("You are born in America")
    print()


# In[11]:


names=["Jacobus","Ruan","Dina","Michael","Brendan","Shana","Dirk","Werner"]
country=["Amreica","France","Australia","Switzerland","China","Scotland","Portugal","South Africa","Argentina","Mexico","Nigeria","India",]
concieved=["an affair","a planned pregnancy","a scandal","a Lab","an adoption","a cardboard box"]
health=[]
happiness=[]
intelligence=[]

looks=[]
age=0
def intro():
    
    
    
    
    a=random.randint(0,len(concieved)-1)
    b=random.randint(0,7)
    c=random.randint(0,len(country)-1)
    print("Welcome you were born in ",concieved[a])
    print("Your name is:",names[b] )
    print("You are born in:",country[c])
    print()
    print("age :",age)
    print()
    if  a== 5:
        print("unfortunately your parents did not love you enough and left you to die")
        print()
        print("game over")
    else:    
        print("your stats at birth are:")
        
        if c <= 6 :
            health=100
            happiness=random.randint(80,100)
            intelligence=random.randint(40,100)
            looks=random.randint(0,100)
            print("health:",health)
            print("happiness:",happiness)
            print("intelligence:",intelligence)
            print("Looks:",looks)
        elif c > 6 and c <= 9:
            health=random.randint(60,90)
            happiness=random.randint(0,80)
            intelligence=random.randint(10,100)
            looks=random.randint(0,100)
            print("health:",health)
            print("happiness:",happiness)
            print("intelligence:",intelligence)
            print("Looks:",looks)
        elif c> 10:
            health=random.randint(5,50)
            happiness=random.randint(0,70)
            intelligence=random.randint(10,100)
            looks=random.randint(0,100)
            print("health:",health)
            print("happiness:",happiness)
            print("intelligence:",intelligence)
            print("Looks:",looks)
            
    
def path():
    
    path = ""
    while path != "1" and path != "2":
        path = input ("which path will you take? (1 or 2)")
        
    return path

def checkpath(path):
    print("")


# In[16]:


intro()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




