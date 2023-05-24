#!/usr/bin/env python
# coding: utf-8

# In[5]:


### 1. Write a Python Program to Check if a Number is Positive, Negative or Zero.

num = int(input("Enter a number = "))

if num > 0:
    print("Positive Number")
elif num == 0:
    print("Zero")
else:
    print("Negative Number")


# In[8]:


### 2. Write a Python Program to Check if a Number is Odd or Even.

num = int(input("Enter the Number = "))

if (num % 2) == 0:
    print("Even Number")
else:
    print("Odd Number")


# In[10]:


### 3. Write a Python Program to Check Leap Year.
Year = int(input("Enter a year = "))

if (Year % 400 == 0) and (Year % 100 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")


# In[18]:


### 4. Write a Python Program to Check Prime Number.
num = int(input("Enter the Number"))
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")
        break
else:
    print(num, "is not a prime number")


# In[25]:


### 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000.
lower = 1
upper = 9999

print ("The Prime Numbers in the range are: ")  
for number in range (lower, upper + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  


# In[ ]:





# In[ ]:




