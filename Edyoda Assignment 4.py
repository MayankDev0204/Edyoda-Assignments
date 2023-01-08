#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
# 
# 
# 
# sample input: 10
# 
# sample output: 35

# In[8]:


x = int(input("enter input: "))
a = lambda x:x+25
print(a(x))


# In[ ]:





# # Write a Python program to triple all numbers of a given list of integers. Use Python map.
# 
# 
# 
# sample list: [1, 2, 3, 4, 5, 6, 7]
# 
# 
# 
# Triple of list numbers:
# 
# [3, 6, 9, 12, 15, 18, 21]

# In[10]:


list1 = eval(input("enter list: ") )
list_new = list(list1)
print("Original list: ", list_new)
result = map(lambda x: 3*x, list_new) 
print("\nTriple of list ")
print(list(result))


# In[ ]:





# # Write a Python program to square the elements of a list using map() function.
# 
# Sample List: [4, 5, 2, 9]
# 
# Square the elements of the list:
# 
# [16, 25, 4, 81]

# In[ ]:





# In[12]:


def sq_num(n):
    return n * n
inputs = [4, 5, 2, 9]
print("Original List: ",inputs)
res_ult = map(sq_num, inputs)
print("Square of list using map():")
print(list(res_ult))


# In[ ]:





# In[ ]:




