#                                                                  User Input Problems

#Question 1: Write a python script to take your name as input from the user and then print it.
Name = input("enter your name")
print("Output of Question 1:")
print(Name)

#Question 2: Write a python script to take input from the user. Input must be a number.
N = int(input("enter number"))
print("Output of Question 2:")
print(N)

#Question 3: Write a python script which takes two numbers from the user, then calculate their sum and display the result.
a = int(input("enter 1st no."))
b = int(input("enter 2nd no."))
print("Output of Question 3:")
print("the sum is:", a+b)

#Question 4: Write a python script which takes the radius from the user and display area of a circle.
import math
r = float(input("enter radius of a circle "))
print("Output of Question 4:")
a = math.pi*r**2
print("the area of a circle is:", a)

#Question 5:  Write a python script to calculate the square of a number. Number is entered by the user.
N = float(input("enter number"))
print("Output of Question 5:")
print("the Sqaure of given no. is:",N**2)

#Question 6: Write a python script to calculate the area of Triangle. Number is entered by the user.
HALF = 0.5
b = float(input("enter base"))
h = float(input("enter height"))
print("Output of Question 6:")
print("area of a triangle :",HALF*b*h)

#Question 7: Write a python script to calculate average of three numbers, entered by the user
a = float(input("enter 1st no."))
b = float(input("enter 2nd no."))
c = float(input("enter 3rd no."))
print("Output of Question 7:")
print("average of three number is :",(a+b+c)/3)

#Question 8: Write a python script to calculate simple interest
p = float(input("enter principal amt"))
r = float(input("enter rate of interest"))
t = float(input("enter time period"))
SI = (p*r*t)/100
print("Output of Question 8:")
print("simple interest:",SI)

#Question 9 : Write a python script to calculate the volume of a cuboid.
l = float(input("enter the length of cuboid"))
b = float(input("enter the breadth of cuboid"))
h = float(input("enter the height of cuboid"))
print("Output of Question 9:")
print("the area of cuboid:",l*b*h)

#Question 10: Write a python script to calculate area of a rectangle
l = float(input("enter the length of rectangle"))
b = float(input("enter the breadth of rectangle"))
print("Output of Question 10:")
print("the area of rectangle:",l*b)
