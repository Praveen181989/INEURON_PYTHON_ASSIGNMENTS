#!/usr/bin/env python
# coding: utf-8

# In[5]:


### 1. Write a Python Program to Find the Factorial of a Number.
num = int(input("Enter a number: "))

factorial = 1

for i in range(1,num + 1):
    factorial = factorial*i
print("The factorial of",num,"is",factorial)


# In[16]:


### 2. Write a Python Program to Display the multiplication Table.
num = int(input("Display the Multiplication Number = "))

for i in range(1,10):
    num1 = num * i
    print(num1)


# In[17]:


### 3. Write a Python Program to Print the Fibonacci sequence.

nterms = int(input("How many terms? "))
n1 = int(input("Enter First Number = "))
n2 = int(input("Enter Second Number = "))
count = 0

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


# In[21]:


### 4. Write a Python Program to Check Armstrong Number.
num = int(input("Enter a number: "))

sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")


# In[31]:


### 5. Write a Python Program to Find Armstrong Number in an Interval.
num = int(input("Enter a number: "))

for num in range(100, 2000):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)

