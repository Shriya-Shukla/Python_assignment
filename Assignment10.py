#                                                                 For loop and range
 
#Question 1: Write a python script to print MySirG N times on the screen
for i in range(int(input("Enter the value of N"))):
    print("MySirG")
print()

#Question 2:Write a python script to print first N natural numbers
for i in range(1,int(input("Enter tbe value of N"))+1,1):
    print(i,end=' ')
print()    

#Question 3: Write a python script to print first N natural numbers in reverse order
N = int(input("Enter the value of N"))
for i in range(N,0,-1):
    print(i, end=' ')
print()

#Question 4:Write a python script to print first N odd natural numbers
for i in range(1,2*int(input("Enter the value of N")),2):
    print(i,end = ' ')
print()

#Question 5:Write a python script to print first N odd natural numbers in reverse order
for i in range(2*int(input("Enter the value of N"))-1,0,-2):
    print(i,end = ' ')
print()

#Question 6:Write a python script to print first N even natural numbers
for i in range(0,2*int(input("Enter the value of N"))-1,2):
               print(i, end = ' ')
print()

#Question 7:Write a python script to print first N even natural numbers in reverse order
for i in range(2*int(input("Enter the value of N"))-2,0,-2):
               print(i,end=' ')
print()

#Question 8:Write a python script to print squares of first N natural numbers
for i in range(1,int(input("enter the value of N"))+1,1):
               print(i*i,end = ' ')
print()

#Question 9:Write a python script to print cubes of first N natural numbers
for i in range(1,int(input("enter the value of N"))+1,1):
               print(i**3,end = ' ')
print()

#Question 10:Write a python script to print first 10 multiples of N
for i in range(int(input("Enter the value of N")),N*10+1,N):
               print(i,end = ' ')
print()               














               
               
               



