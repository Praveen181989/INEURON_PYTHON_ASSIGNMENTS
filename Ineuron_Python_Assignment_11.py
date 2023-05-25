#!/usr/bin/env python
# coding: utf-8

# In[2]:


### 1.Write a Python program to find words which are greater than given length k.
sentence = input("Enter the String: ")
length = 4
print([word for word in sentence.split() if len(word) > length])


# In[4]:


### 2.Write a Python program for removing i-th character from a string.
def remove(string, i):
    a = string[: i]
    b = string[i + 1:]
    return a + b
  
if __name__ == '__main__':
  
    string = input("Enter The String: ")
    i = 5
    print(remove(string, i))


# In[8]:


### 3.Write a Python program to split and join a string.
def split_string(string):
    list_string = string.split(' ')
     
    return list_string
 
def join_string(list_string):
    string = '-'.join(list_string)
     
    return string
 
if __name__ == '__main__':
    string = input("Enter The String: ")
     
    list_string = split_string(string)
    print(list_string)
 
    new_string = join_string(list_string)
    print(new_string)


# In[9]:


### 4.Write a Python to check if a given string is binary string or not.
def check(string):
    p = set(string)
    s = {'0', '1'}

    if s == p or p == {'0'} or p == {'1'}:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
 
    string = input("Enter The String: ")
 
    check(string)


# In[10]:


### 5.Write a Python program to find uncommon words from two Strings.
def UncommonWords(A, B):
    count = {}
    for word in A.split():
        count[word] = count.get(word, 0) + 1

    for word in B.split():
        count[word] = count.get(word, 0) + 1

    return [word for word in count if count[word] == 1]
 
A = input("Enter The First String: ")
B = input("Enter The Second String: ")

print(UncommonWords(A, B))


# In[11]:


### 6.Write a Python to find all duplicate characters in string.
def duplicate_characters(string):
    chars = {}
    for char in string:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
 
    duplicates = []
 
    for char, count in chars.items():
        if count > 1:
            duplicates.append(char)
    return duplicates
 
print(duplicate_characters("Praveen"))

