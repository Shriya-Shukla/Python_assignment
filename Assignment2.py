#                                                             Assignment-2: Python Basics

# Question1: Write a python script to add comments and print “Learning Python” on screen.
# I am writing a program to understand the use of one line comment in python
print("output of Question1:")
print("Learning Python")

#Question2 :Write a python script to add multi line comments and print values of four variables,each in a new line. Variable contains any values.
#I am writing a program to understand the use of multi line comment in python                                                                  
a = 5
b = 5.46
c = 5+8j
d = "MySirg"
print("output of Question2:")
print(a,b,c,d,sep = '\n')

#Question3 :Write a python script to print types of variables. Create 5 variables each of them containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)
a = 35
b = True
c = "MySirg"
d = 5.46
e = 3+4j
print("output of Question3:")
print(type(a),type(b),type(c),type(d),type(e),sep = '\n')

#Quesion4 :Write a python script to print the id of two variables containing the same integer values.
A = 45
B = 45
print("output of Question4:")
print(id(A),id(B),sep = '\n')

#Question5 :Create four variables in a Python script and assign values of different data types to them. Write a Python script to print value, its type and id of each variable
a = 5
b = 5.46
c = 5+8j
d = "MySirg"
print("output of Question5:")
print("value of a",a,"value of b",b,"Value of c",c,"Value of d",d,"type of a",type(a),"type of b",type(b),"type of c",type(c),"type of d",type(d),"id of a",id(a),"id of b",id(b),"id of c",id(c),"id of d",id(d),sep = '\n')

#Question6 : Write a python script to print all the keywords
import keyword
print("output of Question6:")
print(keyword.kwlist)

#Question7 : On Python shell use help() function and display the list of keywords
print("output of Question7:")
help('keywords')


#Question8 :Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some value to it. Write a python script to import A1 module in A0 and print value of the variable created in A0.py
import DEMO
print("output of Question8:")
print(DEMO.A)

#Question9 : Name the keywords, used as data in the Python script.
print("output of Question9:")
print("None, True & False keywords are used as data in python.")


#Question10 : Write a python script to display the current date and time. First create variables to store date and time, then display date and time in proper format (like: 13-8-2022 and 9:00 PM
from datetime import datetime 
dt = datetime.today()
print("output of Question10:")
d1=dt.strftime("%d-%m-%Y and %I:%M:%p")
print(d1)



