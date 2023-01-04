#!/usr/bin/env python
# coding: utf-8

# # Assignment - 3
# 
#  Q1: Write a Python function to sum all the numbers in a list.
# 
# 
# 
# Sample List : (8, 2, 3, 0, 7)
# 
# Expected Output : 20

# In[7]:


#z = input("enter list values: ")
z= (8, 2, 3, 0, 7)
n = list(z)
print("No. of elements : ", len(z), "\nlist is: ", n)
#print(n)
def sum_all(a):
    sum_a1=0
    for i in z: 
        sum_a1+=i
    return sum_a1
print("sum of elements is: ", sum_all(z))


# # Q2: Write a Python program to reverse a string.
# 
# ﻿Sample String : "1234abcd"
# 
# Expected Output : "dcba4321"
# 

# In[26]:


x=str(input("enter the string to reverse: "))
print("original string: ",x)
#z=str(x)
def rev_str():
    for i in x:
        rev=(x[::-1])
    return rev
#rev_str(x)
print("reverse string is:", rev_str())
    


# # Q3 Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# 
# ﻿Sample String : 'The quick Brow Fox'
# 
# Expected Output :
# 
# No. of Upper case characters : 3
# 
# No. of Lower case Characters : 12

# In[35]:


def test_uplow(s):
    u_case = 0
    l_case = 0
    for c in s:
        if c.isupper():
           u_case +=1
        elif c.islower():
           l_case +=1
        else:
           pass
    return "No.of Upper case characters: ", u_case,"No. of Lower case Characters", l_case
a=str(input("Enter the string to count no. of Upper and Lowercase Characters: "))
print(test_uplow(a))


# In[ ]:




