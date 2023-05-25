#!/usr/bin/env python
# coding: utf-8

# In[1]:


### 1.Write a Python Program to Add Two Matrices.
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for r in result:
    print(r)


# In[2]:


### 2.Write a Python Program to Multiply Two Matrices.

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)


# In[3]:


### 3.Write a Python Program to Transpose a Matrix.

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[j][i] = X[i][j]

for r in result:
    print(r)


# In[4]:


### 4.Write a Python Program to Sort Words in Alphabetic Order.

my_str = input("Enter the String: ")

words = [word.lower() for word in my_str.split()]

words.sort()

print("The sorted words are:")
for word in words:
    print(word)


# In[5]:


### 5. Write a Python Program to Remove Punctuation From a String.
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = input("Enter a string: ")
no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char

print(no_punct)

