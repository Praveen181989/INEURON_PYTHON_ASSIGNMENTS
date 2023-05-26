#!/usr/bin/env python
# coding: utf-8

# In[3]:


### 1.Write a program that calculates and prints the value according to the given formula:
##Q = Square root of [(2 C D)/H]
##Following are the fixed values of C and H:
##C is 50. H is 30.
##D is the variable whose values should be input to your program in a comma-separated sequence.

import math

numbers = input("Provide D: ")
numbers = numbers.split(',')
C = 50
H = 30
result_list = []
for D in numbers:
    Q = round(math.sqrt(2 * C * int(D) / H))
    result_list.append(Q)

print(result_list)


# In[4]:


### 2.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
X = int(input("Input number of rows: "))
Y = int(input("Input number of columns: "))
multi_list = [[0 for j in range(Y)] for i in range(X)]

for i in range(X):
    for j in range(Y):
        multi_list[i][j]= i*j

print(multi_list)


# In[6]:


### 3.Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
items = input("Input comma separated sequence of words: ")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))


# In[4]:


### 4.Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
items=[x for x in input('Enter space sepeated words ').split(' ')]
print(' '.join(sorted(list(set(items)))))


# In[1]:


### 5. Write a program that accepts a sentence and calculate the number of letters and digits.
s = input("Input a string : ")
digits=letters=0
for c in s:
    if c.isdigit():
        digits += 1
    elif c.isalpha():
        letters += 1
    else:
        pass
print("Letters", letters)
print("Digits", digits)


# In[3]:


### 6. A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
import re
password= input("Enter your password : ")
x = True
while x:  
    if (len(password) < 6 or len(password) > 12):
        break
    elif not re.search("[a-z]",password):
        break
    elif not re.search("[0-9]",password):
        break
    elif not re.search("[A-Z]",password):
        break
    elif not re.search("[$#@]",password):
        break
    elif re.search("\s",password):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")

