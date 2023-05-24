#!/usr/bin/env python
# coding: utf-8

# In[6]:


### 1. Write a Python program to convert kilometers to miles.
Kilometer = float(input("Enter the Kilometer Value"))

Conversion_factor = 0.62137119
miles = Conversion_factor * Kilometer
print("Kilometer =", Kilometer, "Miles = ", miles)


# In[8]:


### 2.Write a Python program to convert Celsius to Fahrenheit.
Celsius = float(input("Enter the Celsius Value"))

Fahrenheit = (Celsius*9/5)+32
print("Celsius Value =", Celsius, "Fahrenheit Value =", Fahrenheit)


# In[13]:


### 3. Write a Python program to display calendar.
import calendar

Year = int(input("Enter The Year"))
Month = int(input("Enter The Month"))

print(calendar.month(Year, Month))


# In[16]:


### 4. Write a Python program to solve quadratic equation.
import cmath

a = int(input("Enter The First Value = "))
b = int(input("Enter The Second Value = "))
c = int(input("Enter The Third Value = "))


sol1 = (-b -cmath.sqrt((b**2) - (4*a*c)))/(2*a)
sol2 = (-b +cmath.sqrt((b**2) - (4*a*c)))/(2*a)

print("The Solution of Quadratic Equation =", sol1,sol2)


# In[22]:


### 5. Write a Python program to swap two variables without temp variable.

num1 = int(input("Enter First Variable = "))
num2 = int(input("Enter Second Variable = "))

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("The Variable After Swapping = ", num1, num2)

