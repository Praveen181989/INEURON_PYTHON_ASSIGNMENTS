#!/usr/bin/env python
# coding: utf-8

# In[2]:


### 1.Write a Python program to check if the given number is a Disarium Number.
def calculateLength(n):    
    length = 0    
    while(n != 0):    
        length = length + 1   
        n = n//10    
    return length  
     
num = int(input("Enter the number"))    
rem = sum = 0    
len = calculateLength(num)    
        
n = num   
        
while(num > 0):    
    rem = num%10   
    sum = sum + int(rem**len)   
    num = num//10    
    len = len - 1   
       
if(sum == n):    
    print(str(n) + " is a disarium number")    
else:    
    print(str(n) + " is not a disarium number")


# In[3]:


### 2.Write a Python program to print all disarium numbers between 1 to 100.
def calculateLength(n):    
    length = 0    
    while(n != 0):    
        length = length + 1    
        n = n//10   
    return length   
       
def sumOfDigits(num):    
    rem = sum = 0   
    len = calculateLength(num)   
        
    while(num > 0):    
        rem = num%10    
        sum = sum + (rem**len)    
        num = num//10    
        len = len - 1    
    return sum;    
      
result = 0;    
       
print("Disarium numbers between 1 and 100 are");    
for i in range(1, 101):    
    result = sumOfDigits(i)    
        
    if(result == i):    
        print(i)    


# In[5]:


### 3.Write a Python program to check if the given number is Happy Number.
def isHappyNumber(num):    
    rem = sum = 0    
           
    while(num > 0):    
        rem = num%10   
        sum = sum + (rem*rem)   
        num = num//10 
    return sum;    
        
num = int(input("Enter The Happy Number"))    
result = num    
     
while(result != 1 and result != 4):    
    result = isHappyNumber(result)    
        
if(result == 1):    
    print(str(num) + " is a happy number")     
elif(result == 4):    
    print(str(num) + " is not a happy number"); 


# In[11]:


### 4.Write a Python program to print all happy numbers between 1 and 100.
def isHappyNumber(num):    
    rem = sum = 0    
           
    while(num > 0):    
        rem = num%10    
        sum = sum + (rem*rem)    
        num = num//10    
    return sum    
               
print("List of happy numbers between 1 and 100: ")    
for i in range(1, 101):    
    result = i    
  
    while(result != 1 and result != 4):    
        result = isHappyNumber(result)    
        
    if(result == 1):    
        print(i)     


# In[8]:


### 5.Write a Python program to determine whether the given number is a Harshad Number.
num = int(input("Enter The Harshad Number"))   
rem = sum = 0    
      
n = num;    
        
while(num > 0):    
    rem = num%10   
    sum = sum + rem    
    num = num//10   
      
if(n%sum == 0):    
    print(str(n) + " is a harshad number")    
else:    
    print(str(n) + " is not a harshad number")


# In[10]:


### 6.Write a Python program to print all pronic numbers between 1 and 100.
def isPronicNumber(num):    
    flag = False    
        
    for j in range(1, num+1):       
        if((j*(j+1)) == num):    
            flag = True    
            break    
    return flag    
        
print("Pronic numbers between 1 and 100: ")    
for i in range(1, 101):    
    if(isPronicNumber(i)):    
        print(i)     

