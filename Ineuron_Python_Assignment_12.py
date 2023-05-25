#!/usr/bin/env python
# coding: utf-8

# In[1]:


### 1.Write a Python program to Extract Unique values dictionary values.
test_dict = {'Praveen': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}

print("The original dictionary is : " + str(test_dict))
res = list(sorted({ele for val in test_dict.values() for ele in val}))
print("The unique values list is : " + str(res))


# In[2]:


### 2.Write a Python program to find the sum of all items in a dictionary.
def returnSum(myDict):
 
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)
 
    return final
 
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))


# In[3]:


### 3.Write a Python program to Merging two Dictionaries.
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print(dict_1 | dict_2)


# In[12]:


### 5.Write a Python program to insertion at the beginning in OrderedDict.
from collections import OrderedDict
 
ini_dict1 = OrderedDict([('akshat', '1'), ('nikhil', '2')])
ini_dict2 = OrderedDict([("manjeet", '4'), ("akash", '4')])
 
both = OrderedDict(list(ini_dict2.items()) + list(ini_dict1.items()))
 
print ("Resultant Dictionary :"+str(both))


# In[32]:


### 6. Write a Python program to check order of character in string using OrderedDict().
from collections import OrderedDict
 
def checkOrder(input, pattern):
     
    dict = OrderedDict.fromkeys(input)
 
    ptrlen = 0
    for key,value in dict.items():
        if (key == pattern[ptrlen]):
            ptrlen = ptrlen + 1
         
        if (ptrlen == (len(pattern))):
            return 'true'
 
    return 'false'

if __name__ == "__main__":
    input = 'engineers rock'
    pattern = 'er'
    print (checkOrder(input,pattern))


# In[33]:


### 7. Write a Python program to sort Python Dictionaries by Key or Value.

myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
 
myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}
 
print(sorted_dict)

