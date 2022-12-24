#!/usr/bin/env python
# coding: utf-8

# # Q1: # Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
# 
# 
# 
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# 
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# 
# 

# In[ ]:


a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("unsorted : ",a)
y=len(a)
temp=0
for i in range(0,y): 
        for j in range(0,y-i-1): 
            if (a[j][-1] > a[j + 1][-1]): 
                temp = a[j] 
                a[j]= a[j + 1] 
                a[j + 1]= temp 
print("sorted  :  ",a)


# # Q2: Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values. Method1 is below:
# 

# In[ ]:


dict1={'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
print("The dictionary is:", dict1)


# # Q2 - Method2

# In[ ]:


text=str(input("Enter a String: "))
text_length = len(text)
for char in text:
    asc = ord(char)
    print(char, "\t", asc)

