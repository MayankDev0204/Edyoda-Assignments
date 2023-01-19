#!/usr/bin/env python
# coding: utf-8

# # Challenge - 1 - Sum of Square problem

# In[38]:


class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def sqSum(self):
        return (self.x**2+self.y**2+self.z**2)
x1 = int(input("enter the first value: "))
y1 = int(input("enter the second value: "))
z1 = int(input("enter the third value: "))
a=Point(x1,y1,z1)
print("Sq sum is :", a.sqSum())


# # Challenge -- 2 - Calculator Problem

# In[174]:


class Calculator:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.y+self.x
    def subtract(self):
        return self.y-self.x
    def multiply(self):
        return self.y*self.x
    def divide(self):
        return self.y/self.x
num1=int(input("enter first no.: "))
num2=int(input("enter second no.:"))
obj = Calculator(num1,num2)
print("Addition is: ",obj.add())
print("Subtraction is: ",obj.subtract())
print("Multiplicaiton is: ",obj.multiply())
print("Division is: ",obj.divide())


# # Challenge 3 - getter and setter method
# 
# Method - 1 (without exception handling of errors)

# In[ ]:


class Student:
    def __init__(self,Name,Rollno):
        self.__Name = Name
        self.__Rollno = Rollno
    def set_Name(self,x):
        self.__Name = x
    def get_Name(self):
        print("Your Name:" ,self.__Name)
        return ""
    def set_Rollno(self,y):
        self.__Rollno = y
    def get_Rollno(self):
        print("Your Roll No.:" ,self.__Rollno)
        return ""
b1=str(input("Enter Name :"))
b2=int(input("Enter Roll No."))
print("*"*50)
b=Student(b1,b2)
b.set_Name(b1)
print(b.get_Name())
b.set_Rollno(b2)
print(b.get_Rollno())


# # Challenge 3 - getter and setter method
# 
# Method - 2 (with exception handling of errors)

# In[170]:


class Student:
    def __init__(self,Name,Rollno):
        self.__Name = Name
        self.__Rollno = Rollno
    def set_Name(self,x,f=False):
        if f:
            self.__Name = x
        else:
            raise ValueError("Invalid Value in Name")
        #self.__Name = x
    def get_Name(self):
        print("Your Name:" ,self.__Name)
        return ""
    def set_Rollno(self,y,g=False):
        if g:
            self.__Rollno = y
        else:
            raise ValueError("Enter Valid Value in Roll No.")
    def get_Rollno(self):
        print("Your Roll No.:" ,self.__Rollno)
        return ""
b1=str(input("Enter Name :"))
b2=int(input("Enter Roll No."))
print("*"*50)
b=Student(b1,b2)
b.set_Name(b1)
print(b.get_Name())
b.set_Rollno(b2)
print(b.get_Rollno())


# # challenge - 4 - Implementing a Bank Account

# In[167]:


class Account(object):
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance
    def display(self): 
        print("Name of Account Holder:" ,self.title) 
        print("Balance amount in account:", self.balance) 

class SavingsAccount(Account):
    def __init__(self,title,balance,interest_Rate):
        self.interest_Rate=interest_Rate
        Account.__init__(self,title,balance)
    def show(self): 
        print("interest rate is", self.interest_Rate) 
        
demo1 = SavingsAccount('Ashish',5000,5)
demo1.display()
demo1.show()


# # challenge - 5 - implmenting handling a bank account

# In[5]:


import sys
class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance=self.balance-amount
        return self.balance
       
    def deposit(self, amount):
        self.balance=self.balance+amount
        return self.balance
    
    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=5, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
            print("Customer name: ", self.title)
            print("Account balance: ", self.balance)
            print("Interest Rate: ", self.interestRate)          
    
    def interestAmount(self):
        self.int_amount=(self.balance*5)/100
        print("Annual interest Amount at 5 %: ", self.int_amount)
        
demo1 = SavingsAccount("Ashish", 2000, 5)   # initializing a SavingsAccount object
print("*"*50)
dep=int(input("Enter the amount to be deposited:"))
print("Balance after deposition :",demo1.deposit(dep))
print("*"*50)
wdr= int(input("Enter the amount to be withdrawn:"))
print("Balance after withdrawal : ",demo1.withdrawal(wdr))
print("*"*50)
print("Updated Balance in Account",demo1.getBalance())
print("*"*50)
demo1.interestAmount()


# In[ ]:




