#!/usr/bin/env python
# coding: utf-8

# In[4]:


### 1.Write a Python Program to find sum of array.

def _sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return(sum)
 
if __name__ == "__main__":
    arr = [12, 3, 4, 15]
    n = len(arr)
    ans = _sum(arr)
    print('Sum of the array is ', ans)


# In[5]:


### 2.Write a Python Program to find largest element in an array.
def largest(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)


# In[6]:


### 3.Write a Python Program for array rotation.

def reverse(start,end,arr):
    no_of_reverse=end-start+1
    count=0
    while((no_of_reverse)//2!=count):
        arr[start+count],arr[end-count]=arr[end-count],arr[start+count]
        count+=1
    return arr

def left_rotate_array(arr,size,d):
    start=0
    end=size-1
    arr=reverse(start,end,arr)
    
    start=0
    end=size-d-1
    arr=reverse(start,end,arr)

    start=size-d
    end=size-1
    arr=reverse(start,end,arr)
    return arr

arr=[1,2,3,4,5,6,7,8]
size=8
d=1
print('Original array:',arr)

if(d<=size):
    print('Rotated array: ',left_rotate_array(arr,size,d))
else:
    d=d%size
    print('Rotated array: ',left_rotate_array(arr,size,d))


# In[8]:


### 4.Write a Python Program to Split the array and add the first part to the end.
def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]
        arr[n-1] = x

arr = [4,48,67,34,95,36]
n = len(arr)
position = 2

splitArr(arr, n, position)

for i in range(0, n):
    print(arr[i], end=' ')


# In[10]:


### 5. Write a Python Program to check if given array is Monotonic.
def isMonotonic(A):
    x, y = [], []
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    if(x == A or y == A):
        return True
    return False

A = [7,6,5,4,3]
print(isMonotonic(A))

