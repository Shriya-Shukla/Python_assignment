#                                                          More on Recursion
#1. Write a recursive python function to calculate sum of first N natural numbers
def SumN(N):
    if N == 1:
        return 1
    s = N+SumN(N-1)
    return s    
n = int(input("Enter no."))
s = SumN(n)
print("The sum of first n natural numbers:",s)
#2. Write a recursive python function to calculate sum of first N odd natural numbers
def SumNOdd(N):
    if N==1:
        return 1
    return 2*N-1+SumNOdd(N-1)               
n = int(input("Enter no."))
s = SumNOdd(n)
print("The sum of first n natural numbers:",s)
#3. Write a recursive python function to calculate sum of first N even natural numbers
def SumNEven(N):
    if N == 1:
        return 2
    return 2*N+SumNEven(N-1)
n = int(input("Enter no."))
s = SumNEven(n)
print("The sum of first N even numbers:",s)
#4. Write a recursive python function to calculate sum of squares of first N natural numbers
def SumSqrN(N):
    if N == 1:
        return 1
    return N*N + SumSqrN(N-1)
n = int(input("Enter no."))
s = SumSqrN(n)
print("The sum of squares of first N natural numbers:",s)

#5. Write a recursive python function to calculate sum of cubes of first N natural numbers
def SumCubeN(N):
    if N == 1:
        return 1
    return N**3 + SumCubeN(N-1)
n = int(input("Enter no."))
s = SumCubeN(n)
print("The sum of cube of first N natural numbers:",s)

#6. Write a recursive python function to calculate the factorial of a number.
def Fact(N):
    if N == 1:
        return 1
    return N*Fact(N-1)
n = int(input("Enter no."))
s = Fact(n)
print("The factorial of given number:",s)

#7. Write a recursive python function to calculate sum of the digits of a given number
def SumDigit(N):
    if N==0:
        return 0
    a = N%10
    return a + SumDigit(N//10)
n = int(input("Enter no."))
s = SumDigit(n)
print("The sum of digit of given numbers:",s)
  
#8. Write a recursive python function to print binary of a given decimal number.
def DecToBin(N):
    if N >= 1:
        DecToBin(N//2)
    print(N%2,end = '')
n = int(input("Enter no."))
DecToBin(n)
print()

    
#9. Write a recursive python function to print octal of a given decimal number
def DecToOct(N):
    if N > 0:
        DecToOct(N//8)
        print(N%8,end='')
        
n = int(input("Enter no."))
print("Octal: ", end='')
DecToOct(n)
  
#10. Write a recursive python function to find the Nth term of the Fibonacci series
def NFibo(N):
    if a == 0:
        return 0,1
    print
