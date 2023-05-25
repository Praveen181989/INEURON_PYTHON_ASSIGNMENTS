#!/usr/bin/env python
# coding: utf-8

# In[1]:


### 1.Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?. Examples stutter('incredible') ➞ 'in... in... incredible?' stutter('enthusiastic') ➞ 'en... en... enthusiastic?' stutter('outstanding') ➞ 'ou... ou... outstanding?'
def stutter(word):
    return (2*(word[:2]+'... '))+word+'?'
word = input('Enter word : ')
print(stutter(word))


# In[2]:


### 2.Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.
def radians_to_degrees(radian):
    pi = 3.14159
    #formula
    degree = radian * (180/pi)
    return degree
radian = float(input('Enter the Radian : '))
print("degree =",(radians_to_degrees(radian)))


# In[3]:


### 3.In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number. Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.
def checkIfCurzonNumber(n):
 
    power, product = 0, 0
 
    # Find 2**n + 1
    power = pow(2, n) + 1
 
    # Find 2*n + 1
    product = 2 * n + 1
 
    # Check for divisibility
    if (power % product == 0):
        print(n, "is Curzon Number")
    else:
        print(n, "is not a Curzon Number")
        
n = int(input('Enter a number : '))
checkIfCurzonNumber(n)


# In[4]:


### 4.Given the side length x find the area of a hexagon.
import math
def area_of_hexagon(s):     
    return ((3 * math.sqrt(3) * (sideLength * sideLength)) / 2);
     
#length of a side.
sideLength = float(input('Enter the length : '))

print("Area:","{0:.4f}".format(area_of_hexagon(sideLength)))


# In[5]:


### 5.Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.
def decimalToBinary(n):
    return bin(n).replace("0b", "")
   
for i in range(0,50):
    print(decimalToBinary(i))


# In[ ]:




