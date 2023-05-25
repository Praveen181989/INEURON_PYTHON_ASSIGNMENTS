#!/usr/bin/env python
# coding: utf-8

# In[6]:


### 1.Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
def generate(n):
    for i in range(n+1):
        if i % 35 == 0:
            yield i

n = int(input())
resp = [str(i) for i in generate(n)]
print(",".join(resp))


# In[5]:


### 2.Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
n = int(input())

for i in range(0, n+1, 2):
    if i < n - 1:
        print(i, end = ',' )
    else:
            print(i)


# In[12]:


### 3.Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
def fib(n):    
    if n == 0: 
            return 0    
    elif n == 1: 
            return 1    
    else: 
            return fib(n-1)+fib(n-2)
n=int(input('Enter a number :')) 
values = [str(fib(x)) for x in range(0, n+1)] 
print(",".join(values))


# In[10]:


### 4.Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
import re

email = "john@google.com elise@python.com"
pattern = "\w+@(\w+).com"
ans = re.findall(pattern,email)
print(ans)


# In[11]:


### 5.Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

Asqr = Square(5)
print(Asqr.area())  

print(Square().area())

