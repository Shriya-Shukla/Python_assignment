
#                                                                        More on loops

#1. Write a python script to reverse a number.
s = 0
n = int(input("Enter a number"))
while(n!=0):
    a = n%10
    s = s*10+a
    n = n//10
print("the reverse of a given no. is",s)

#2. Write a python script to check whether a given number is Prime or not
n1 = int(input("Enter a number"))
for i in range(2,n1,1):
    if (n1% i == 0):
        print("Given number is not prime")
        break
else:
    print("Given number is prime")
    
#3. Write a python script to print all Prime numbers under 100
for j in range(2,101,1):
    for i in range(2,j,1):
        if (j% i == 0):
            break
    else:
        print(j)
        
#4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)
beg = int(input("Enter the begining value of range"))
end = int(input("Enter the end value of range"))
for j in range( beg+1,end,1):
    for i in range(2,j,1):
        if j% i == 0:
            break
    else:
        print(j)        

#5. Write a python script to find next prime number of a given number
n = int(input("Enter a no."))
#for i in range(n+1,,1):
i = n+1
while i > n:
    for j in range(2,i,1):
        if i % j == 0:
            i +=1
            break
    else:
        print("Next prime number of a given number" ,i)
        break
    
#6. Write a python script to print first N prime numbers
N = int(input("Enter the value of N"))
i = 2
count = 0
while count != N:
    for j in range(2,i,1):
        if i % j == 0:
            i += 1
            break
    else:
        print(i)
        i += 1
        count += 1

#7. Write a python script to check whether a given pair of numbers are co-Prime numbers or not.
a = int(input("enter 1st value of pair ")) 
b = int(input("enter 2nd value of pair"))
for i in range(2,min(a,b),1):
    if a % i == 0 or b % i == 0:
        print("Given pair is not co-prime pair")
        break
else:
    print("given pair is co-prime pair")
    
#8. Write a python script to print first N terms of a Fibonacci series
# logic need to see    
N = int(input("Enter the value of N"))
First = 0
second = 1
print(First,second,end = ' ')
for i in range(1,N-1,1):
    sum = First +second
    print(sum,end = ' ')
    First = second
    second = sum
print()    

#9. Write a python script to calculate LCM of two numbers
a = int(input("enter 1st number")) 
b = int(input("enter 2nd number"))
max = a if a>b else b
while True:
    if (max%a == 0 and max%b == 0):
        lcm = max
        break
    max += 1
print(lcm)          
        
#10. Write a python script to calculate HCF of two numbers
a = int(input("enter 1st number")) 
b = int(input("enter 2nd number"))
min = b if a>b else a
for i in range(min+1):
    if (a%i == 0 and b%i == 0):
        hcf = i
print(hcf)    
        
