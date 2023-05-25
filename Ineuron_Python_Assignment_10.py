#!/usr/bin/env python
# coding: utf-8

# In[1]:


### 1. Write a Python program to find sum of elements in list.
total = 0
list = [11, 5, 17, 18, 23]
for ele in range(0, len(list)):
    total = total + list[ele]
print("Sum of all elements in given list: ", total)


# In[3]:


### 2.Write a Python program to Multiply all numbers in the list.
def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

list = [1, 2, 3]
print(multiplyList(list))


# In[4]:


### 3. Write a Python program to find smallest number in a list.
list = [10, 20, 4, 45, 99]
list.sort()
print("Smallest element is:", list[0])


# In[5]:


### 4. Write a Python program to find largest number in a list.
list = [10, 20, 4, 45, 99]
list.sort()
print("Largest element is:", list[-1])


# In[6]:


### 5.Write a Python program to find second largest number in a list.
list = [10, 20, 4, 45, 99]
list.sort()
print("Largest element is:", list[-2])


# In[7]:


### 6.Write a Python program to find N largest elements from a list.
def Nmaxelements(list, N):
    final_list = []
 
    for i in range(0, N):
        max1 = 0
 
        for j in range(len(list)):
            if list[j] > max1:
                max1 = list[j]
 
        list.remove(max1)
        final_list.append(max1)
 
    print(final_list)

list = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2

Nmaxelements(list, N)


# In[8]:


### 7.Write a Python program to print even numbers in a list.
list = [10, 21, 4, 45, 66, 93]
for num in list:
    if num % 2 == 0:
        print(num, end=" ")


# In[9]:


### 8. Write a Python program to print odd numbers in a List.
list = [10, 21, 4, 45, 66, 93]
for num in list:
    if num % 2 != 0:
        print(num, end=" ")


# In[10]:


### 9.Write a Python program to Remove empty List from List.

test_list = [5, 6, [], 3, [], [], 9]
print("The original list is : " + str(test_list))
res = [ele for ele in test_list if ele != []]
print("List after empty list removal : " + str(res))


# In[11]:


### 10.Write a Python program to Cloning or Copying a list.

def Cloning(list):
    list_copy = list[:]
    return list_copy

list = [4, 8, 2, 10, 15, 18]
list1 = Cloning(list)
print("Original List:", list)
print("After Cloning:", list1)


# In[12]:


### 11.Write a Python program to Count occurrences of an element in a list.

def countX(list, x):
    count = 0
    for ele in list:
        if (ele == x):
            count = count + 1
    return count

list = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, countX(list, x)))

