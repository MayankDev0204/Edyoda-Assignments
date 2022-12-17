#!/usr/bin/env python
# coding: utf-8

# # Edyoda Assignment - 1 Batch DS

# # Assignment-1, Q1 - Write a Python program to get the Fibonacci series between 0 to 50
# 
# Note : The Fibonacci Sequence is the series of numbers :
# 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# 
# Every next number is found by adding up the two numbers before it.
# 
# Expected Output : 0 1 1 2 3 5 8 13 21 34 

# In[ ]:


x=int(input("provide no. of terms till the fibonacci series should be printed it must be >1 for visible series: "))
first_term=0
second_term=1
count=0
if x<=0:
    print("Please enter a valid Term, Thank You")
elif x==1:
    print("Although, it's not a recommended term for visible series, still the series is", first_term,)
else:
    print("Fibonacci series upto: ", x, "terms")
    while count<x:
        print(first_term)
        final_term=first_term+second_term
        first_term=second_term
        second_term=final_term
        count+=1


# # Assignment - 1 Q2 - Write a Python program that accepts a word from the user and reverse it.
# 
# Sample Test Case
# 
# Input : Edyoda
# 
# output: adoydE

# In[3]:


x=input("enter string to reverse: ")
for i in range(len(x)-1,-1,-1):
    print(x[i], end="")


# # Assignment - 1 Q3 - Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# 
# Expected Output :
# 
# Number of even numbers : 4
# 
# Number of odd numbers : 5
# 
# 

# In[39]:


mylist=[]
x=int(input("enter higher range of list to sort even odd : "))
count_odd=0
count_even=0
for i in range(1,x+1):
    a=int(input("enter element: "))
    if a%2==0:
        count_even=count_even+1
        print("you've entered an even value", count_even)
    else:
        count_odd=count_odd+1
        print("you've entered an odd value", count_odd)
print("Total count of odd values: ", count_odd)
print("Total count of even values:", count_even)
 


# ##### 

# In[ ]:




