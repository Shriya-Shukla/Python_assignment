#                                                                         Decision Control

#Question 1: Write a python script to check whether a given number is positive or non-positive
a = int(input("enter a number: "))
print("Output of Question1:")
if (a>0):
    print("given number is positive")
else:
    print("given number is non positive")

#Question 2: Write a python script to check whether a given number is divisible by 5 or not
print("given no. is divisible by 5")if int(input("enter a no.: "))%5 == 0 else print("given no. is not divisible by 5")

#Qestion 3: Write a python script to check whether a given number is even or odd
print("given number is odd" if int(input("enter a number: ")) %2 else "given number is even")

#Question 4: rite a python script to print greater between two numbers. Print number only once even if the numbers are the same.
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
print("Output of Question4:")
print(a if a>b else b)

#Question 5: Write a python script to print two given words in dictionary order
s1 = input("enter 1st word: ")
s2 = input("enter 2nd word: ")
print("Output of Question5:")
if s1 > s2:
    print(s1," ",s2)
else:
    print(s2," ",s1)

#Question 6: Write a python script to check whether a given number is a three digit number or not
a = int(input("enter a number: "))
print("Output of Question6:")
print("given number is three digit number") if a >=100 and a <= 999 else print("given number is not three digit number")
print("another way to check given number is three digit number or not")
s = 0
while(a != 0):
    a=a//10
    s +=1
else:
    if(s == 3):
        print("given number is three digit number")
    else:
        print("given number is not three digit number")
print()

#Question 7: Write a python script to check whether a given number is positive, negative or zero.
a = int(input("Enter number"))
print("Output of Question7:")
if (a == 0):
    print("zero")
elif a > 0:
    print("positive")
else:
    print("Negative")
print()

#Question 8: Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots
a = int(input("enter the cofficient of x^2"))
b = int(input("enter the cofficient of x"))
c = int(input("enter the constant term"))
d = b**2-4*a*c
print("Output of Question8:")
if (d == 0):
    print("the roots a2re imaginary")
elif d > 0:
    print("the roots are real & equal")
else:
    print("the roots are real & distinct")
print()

#Question 9:Write a python script to check whether a given year is a leap year or not.
a = int(input("enter year"))
print("Output of Question9:")
print("given year is a leap year")if a% 4 == 0 and a%100!=0 else print("given year is not a leap year")

#Question 10: Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
a = int(input("enter 1st no."))
b = int(input("enter 2nd no."))
c = int(input("enter 3rd no."))
print("Output of Question10:")
if a>b and a>c:
    print("a is greater")
elif b>c :
    print("b is greater")
else:
    print("c is greater")

#Question 11:Write a python script to take the month value in numeric format and display the number of days in it.
a = int(input("enter month no."))
print("Output of Question11:")
match a:
    case 1: print("31 days in month ",a)
    case 2: print("29 days in month ",a)
    case 3: print("31 days in month ",a)
    case 4: print("30 days in month ",a)
    case 5: print("31 days in month ",a)
    case 6: print("30 days in month ",a)
    case 7: print("31 days in month ",a)
    case 8: print("31 days in month ",a)
    case 9: print("30 days in month ",a)
    case 10: print("31 days in month ",a)
    case 11: print("31 days in month ",a)
    case 12: print("31 days in month ",a)
    
#Question 12: Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part
a =  complex(input("enter a complex number"))
print("Output of Question12:")
if a.real > a.imag:
    print("real is greater than imaginary")
else:
    print("imaginary is greater")