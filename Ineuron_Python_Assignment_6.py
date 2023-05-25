#!/usr/bin/env python
# coding: utf-8

# In[1]:


### 1.Write a Python Program to Display Fibonacci Sequence Using Recursion.

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("Enter the terms"))

if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))


# In[3]:


### 2.Write a Python Program to Find Factorial of Number Using Recursion.

def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)

num = int(input("Enter the number"))

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))


# In[5]:


### 3.Write a Python Program to calculate your Body Mass Index.

def bodymassindex(height, weight):
    return round((weight / height**2),2)


h = float(input("Enter your height in meters: "))
w = float(input("Enter your weight in kg: "))


print("Welcome to the BMI calculator.")

bmi = bodymassindex(h, w)
print("Your BMI is: ", bmi)


if bmi <= 18.5:
    print("You are underweight.")
elif 18.5 < bmi <= 24.9:
    print("Your weight is normal.")
elif 25 < bmi <= 29.29:
    print("You are overweight.")
else:
    print("You are obese.")


# In[6]:


### 4.Write a Python Program to calculate the natural logarithm of any number.

import math

num = float(input("Enter the number"))

print ("math.log(num) : ", math.log(num))


# In[7]:


### 5.Write a Python Program for cube sum of first n natural numbers.

n = int(input("Enter the number"))
s=0
for i in range(1,n+1):
    s=s+pow(i,3)
print(s) 

