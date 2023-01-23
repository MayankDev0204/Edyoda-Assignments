#!/usr/bin/env python
# coding: utf-8

# # Assignment - 1
# Question- 1 
# 1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. 
# Each employee information consists of Name, DOB, Height, City, State. 
# Write a python program that reads this information from the JSON file and saves the 
# information into a list of objects of Employee class. 
# Finally print the list of the Employee objects.

# In[1]:


import json
employee={
    "employee_details":[
    
    {"Name": "Mayank", "DOB:":"14122018", "Height:":"5ft 8 inch", "City:":"Dehradun","State":"UK"},
    
    {"Name": "Sandeep", "DOB:":"14122019", "Height:":"5ft 7 inch", "City:":"kanpur","State":"UP"},
    
    {"Name": "Dinesh", "DOB:":"14122022", "Height:":"5ft 6 inch", "City:":"Gandhinagar","State":"Gujarat"},
    
    {"Name": "Nitesh", "DOB:":"14122023", "Height:":"5ft 5 inch", "City:":"Jaipur","State":"Rajasthan"},
    
    {"Name": "Saurabh", "DOB:":"14122021", "Height:":"6ft 2 inch", "City:":"Chandigrah","State":"Haryana"},
    ]
}

with open("employee.json", "w") as f:
    json.dump(employee,f, indent=4)

f = open ('employee.json', "r")
data = json.loads(f.read())
for i in data['employee_details']:
    print(i)
f.close()


# In[ ]:





# # Assignment - 1
# Question- 2 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

# In[74]:


import json
  
indian_states1 ={
    "j & K " : "Kashmir",
    "Punjab" : "Chandigarh",
    "U P " : "Lucknow",
    "U K " : "Dehradun",
    "Rajasthan " : "Jaipur",
    "Bihar" : "Patna",
    "Maharashtra" : "Mumbai"
}
  
with open("indian_states1.json", "w") as f:
    json.dump(indian_states1,f, indent=4)
print("Appended JSON: \n",indian_states1)


# # Assignment - 2
# 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:
# 
# 🔴 a. It should have a function ‘description()’ which prints the name and age of the dog.
# 🔴 b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# 🔴 c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
# 🔴 d. Create objects and implement the above functionalities.

# In[73]:


class Dog:
    def __init__(self,name,age,coat_color):
        self.name=name
        self.age=age
        self.coat_color=coat_color
    def description(self):
        print("Name of Dog: " ,self.name)
        print("Age of the dog: " ,self.age)
    def get_info(self):
        print("Coat color of this Dog :" ,self.coat_color)    
class JackRussellTerrier(Dog):
    def __init__(self,name,age,coat_color,j_f,j_nf):
        self.j_f=j_f
        self.j_nf = j_nf
        Dog.__init__(self,name,age,coat_color)
    def friend(self):
        print("This in Jack Russell's class : ",self.j_f)
    def no_friend(self):
        print("This in Jack Russell's class : ",self.j_nf) 
class Bulldog(Dog):
    def __init__(self,name,age,coat_color,b_w,b_nw):
        self.b_w=b_w
        self.b_nw = b_nw
        Dog.__init__(self,name,age,coat_color)
    def wild(self):
        print("This in Bull Dog's class : ",self.b_w) 
    def not_wild(self):
        print("This in Bull Dog's class : ",self.b_nw)        

x=Dog("Bull Dog", "13", "Black")
x.description()
x.get_info()
z=Bulldog("BuLL Dog","12","Brown","wild","not wild")
z.not_wild()
z.wild()
a=JackRussellTerrier("Russell","14","polka","friendly","non friendly")
a.friend()
a.no_friend()


# In[ ]:




