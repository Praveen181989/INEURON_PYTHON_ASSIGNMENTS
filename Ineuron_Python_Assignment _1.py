#!/usr/bin/env python
# coding: utf-8

# In[1]:


### 1. Write a Python program to print \"Hello Python\"?"
print("Hello Python");


# In[6]:


### 2. Write a Python program to do arithmetical operations addition and division.
num1 = int(input("ENTER FIRST NUMBER = "))
num2 = int(input("ENTER SECOND NUMBER = "))

sum = num1+ num2
print("The Two number of addition is = ", sum)

div = num1 / num2
print("The Two number of division is = ", div)


# In[8]:


### 3. Write a Python program to find the area of a triangle.
Base = float(input("Enter the Base = "))
Height = float(input("Enter the Height = "))

Area = (Base*Height)/2
print(" The Area of Triangle = ", Area)


# In[12]:


### 4. Write a Python program to swap two variables.
a = int(input("Enter the value = "))
b = int(input("Enter the value = "))

temp = a
a = b
b = temp

print("Value a after swapping = ", a)
print("Value b after swapping = ", b)


# In[13]:


### 5. Write a Python program to generate a random number.
import random
random.randint(0,9)

