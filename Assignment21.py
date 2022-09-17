
#                                 Recursion
#1. Write a recursive python function to print first N natural numbers.
def PrintN1(n):
    if n>0:
        PrintN1(n-1)
        print(n)
        
N = int(input("Enter number"))
print("Output of Question1:")
PrintN1(N)

#2. Write a recursive python function to print first N natural numbers in reverse order
def PrintN2(n):
    if n>0:
        print(n)
        PrintN2(n-1)
        
N = int(input("Enter number"))
print("Output of Question2:")
PrintN2(N)
        
#3. Write a recursive python function to print first N odd natural numbers
def NOdd(n):
    if n==1 :
        print(1)
    else:
        NOdd(n-1)
        print(2*n-1)
        
N = int(input("Enter number"))
print("Output of Question3:")
NOdd(N)

#4. Write a recursive python function to print first N odd natural numbers in reverse order
def NOddRev(n):
    if n == 1:
        print(1)
    else:
        print(2*n-1)
        NOddRev(n-1)
        
N = int(input("enter number"))
print("Output of Question4:")
NOddRev(N)
         
#5. Write a recursive python function to print first N even natural numbers.
def NEven(n):
    if n == 1:
        print(2)
    else:
        NEven(n-1)
        print(2*n)
        
N = int(input("enter number"))
print("Output of Question5:")
NEven(N)
#6. Write a recursive python function to print first N even natural numbers in reverse order.
def NEvenRev(n):
    if n == 1:
        print(2)
    else:
        print(2*n)
        NEvenRev(n-1)

N = int(input("enter number"))
print("Output of Question6:")
NEvenRev(N)

#7. Write a recursive python function to print squares of first N natural numbers
def PrintNSqr(n):
    if n>0:
        PrintNSqr(n-1)
        print(n*n)
N = int(input("Enter number"))
print("Output of Question7:")
PrintNSqr(N)        
        
#8. Write a recursive python function to print cubes of first N natural numbers.
def PrintNCube(n):
    if n>0:
        PrintNCube(n-1)
        print(n**3)
N = int(input("Enter number"))
print("Output of Question8:")
PrintNCube(N)        
        
#9. Write a recursive python function to print first N multiples of a given number.
def MultipleN(n,num):
    if  n == 1:
        print(num)
    else:
        MultipleN(n-1,num)
        print(n*num)
        
Num = int(input("enter a number"))
N = int(input("How any multiples you want to display of given number"))
print("Output of Question9:")
MultipleN(N,Num)

#10. Write a recursive python function to print a number in reverse order
def NumRev(n):
    global rev
    if n>0:
        a = n%10
        rev = rev*10+a
        NumRev(n//10)
    return rev

rev = 0
N = int(input("Enter number"))
rev = NumRev(N)
print("Reverse of a given number",rev)
