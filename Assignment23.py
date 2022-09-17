#                                                    Iterator, Generator and Decorator

#1. Use iter and next method to access all the elements of a given set using while loop
l1 = [23,43,24,54,9,45]
it = iter(l1)
i = 0
print("Output of Question1:")
while i< len(l1):
    print(next(it),end = ' ')
    i += 1
print()

#2. Create a generator to produce first n odd natural numbers
def OddN(N):
    i = 1
    while N:
        yield i
        i += 2
        N -= 1
n = int(input("Enter n"))
print("Output of Question2:")
for e in OddN(n):
    print(e ,end = ' ')
print()

#3. Create a generator to produce first n even natural numbers
def OddN(N):
    i = 2
    while N:
        yield i
        i += 2
        N -= 1
n = int(input("Enter n"))
print("Output of Question3:")
for e in OddN(n):
    print(e ,end = ' ')
print()

#4. Create a generator to produce squares of first N natural numbers
def SqrN(n):
    i = 1
    while i<=n:
        yield i*i
        i+=1
n = int(input("Enter n"))
print("Output of Question4:")
for e in SqrN(n):
    print(e ,end = ' ')
print()

#5. Create a generator to produce first n terms of Fibonacci series
def fiboN(n):
    a,b = 0,1
    while n:
        yield a
        a,b = b,a+b
        n -= 1
n = int(input("Enter n"))
print("Output of Question5:")
for e in fiboN(n):
    print(e ,end = ' ')
print()

#6. Create a generator to produce first n prime numbers
def NPrime(N):
    i=2
    count = 0
    while count != N:
        for j in range(2,i,1):
            if i% j == 0:
               i += 1 
               break
        else:
            yield i
            count +=1
            i += 1
n = int(input("Enter n"))
print("Output of Question6:")
for e in NPrime(n):
    print(e ,end = ' ')
print()            
                   
#7. Create an endless iterator using generator method to produce terms of Fibonacci series
def Endlessfib():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b
it = Endlessfib()
fib_list = []
print("OUtput of Question 7:")
while True:
    print("Do you want to generate another element[Y/N]")
    ans = input()
    if ans == 'Y':
        fib_list.append(next(it))
        print(fib_list)
    else:
        break
#8. Create an endless iterator using generator method to produce Prime numbers
def EndlessPrime():
    i = 2
    while True:
        for j in range(2,i,1):
            if i%j == 0:
                i += 1
                break
        else:
            yield i
            i += 1
pr = EndlessPrime()
Prime_List = []
print("Output of Question 8")
while True:
    print("Do you want to generate another Prime number[Y/N]")
    ans = input()
    if ans == 'Y':
        Prime_List.append(next(pr))
        print(Prime_List)
    else:
        break
    
#9. Define a function which takes lengths of three sides of a triangle as arguments and display the perimeter or triangle. Define and apply a decorator which checks for the validity of the triangle on the basis of lengths of the side. This makes the perimeter to be displayed when the triangle can exist with the given lengths of the sides.
def Perimeter_Decor(func):
    def TriValid(a,b,c):
        if a+b > c and a < b+c and b < a+c:
            print("It is valid Trinagle")
            print("the perimteter of triangle:",func(a,b,c))
        else:
            print("It is not a valid triangle")
    return TriValid       
        
@Perimeter_Decor
def TriPerimeter(a,b,c):
    perimeter = (a+b+c)
    return perimeter
A = int(input("enter 1st side of triangle"))
B = int(input("enter 2nd side of triangle"))
C = int(input("enter 3rd side of triangle")) 
print("Output of Question9:")
TriPerimeter(A,B,C)    

#10. Define a function which calculates HCF of two numbers. Define and apply a decorator to check whether two given numbers are co-prime or not
def HCF_Decor(result_func):
    def CoPrime(A,B):
        b = result_func(A,B)
        if b == 1:
            print("The given numbers are Co-prime") 
        else:
            print("The given numbers are not co-prime") 
    return CoPrime        

@HCF_Decor
def HCF(A,B):
    min = A if A<B else B
    for i in range(1,min+1):
        if ((A%i == 0) and (B%i == 0)):
            hcf = i
    print("The HCF of given numbers:",hcf)        
    return hcf
r = int(input("enter 1st number"))
s = int(input("enter 2nd number"))
print("Output of Question10:")
HCF(r,s)    
