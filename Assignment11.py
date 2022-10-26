#                                                                  loops

#Question 1:Write a python script to calculate sum of first N natural numbers
N = int(input("Enter the value of N"))
i=1
s=0
while(i<=N):
    s = s+i
    i += 1
print(s)

#Question 2:Write a python script to calculate sum of squares of first N natural numbers
N = int(input("Enter the value of N"))
i=1
s=0
while(i<=N):
    s = s+i*i
    i += 1
print(s)

#Question 3:Write a python script to calculate sum of cubes of first N natural numbers
N = int(input("Enter the value of N"))
i=1
s=0
while(i<=N):
    s = s+i**3
    i += 1
print(s)

#Question 4:Write a python script to calculate sum of first N odd natural numbers
N = int(input("Enter the value of N"))
i=1
s=0
while(i<=2*N-1):
    s = s+i
    i += 2
print(s)

#Question 5: Write a python script to calculate sum of first N even natural number
N = int(input("Enter the value of N"))
i=0
s=0
while(i<=2*N-2):
    s = s+i
    i += 2
print(s)

#Qestion 6:Write a python script to calculate factorial of a given number
N = int(input("Enter the value of N"))
s = 1
for i in range(1,N+1,1):
    s =  s*i
print(s)

#Question 7: Write a python script to count digits in a given number
c = 0
N = int(input("Enter the value of N"))
while(N!=0):
    N = N//10
    c += 1
print("The no. of digit in given number:",c)

#2nd way to solve
N = input("Enter number")
print(len(N))

#Question 8: Write a python script to calculate sum of digits of a given number
s =0
N = int(input("Enter the value of N"))
while(N!=0):
    a = N%10
    s = s+a
    N = N//10
print("The sum of digits of given number:",s)   

#Question 9: Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
N = int(input("Enter the value of N"))
s = ''
while N:
    s = str(N%2)+s
    N = N//2
print(s)
print()
  
#Question 10: Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method
N = int(input("Enter the value of N"))
s = ''
while N:
    s = str(N%8)+s
    N = N//8    

print(s)
print() 
