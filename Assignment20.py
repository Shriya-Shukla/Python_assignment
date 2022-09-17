#                                                           More on functions

#1. Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.
def f1(list1):
    list2 = list(set(list1))
    return list2    
l1 = [2,3,1,2,3,5,6,7,8,9,5]
l2 = f1(l1)
print("Output of Question1") 
print(l2)

#2. Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.
def f2(n):
    for i in range(2,n,1):
        if n%i == 0:
            print("Given nuber is not prime")
            break
    else:
        print("Given number is prime")
number = int(input("Enter a number"))
print("Output of Question2")
f2(number)

#3. Write a python program to create a function that prints the even numbers from a given list. Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
def f3(list):
    for i in list:
        if i % 2 == 0:
            print(i,end = ' ')
print()            
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Output of Question3")
f3(l1)

#4. Write a python program to create a function that checks whether a passed string is palindrome or not.
def f4(str):
    print("Given string is palindrome" if str[::-1] == str else "Given string is not palindrome")
s1 = input("Enter string")
print("Output of Question4")
f4(s1)
   
#5. Write a python program to create a function to find the Min of three numbers.
def f5(n1,n2,n3):
   print((n1 if n1<n3 else n3) if n1<n2 else (n2 if n2<n3 else n3))
number1 = int(input("Enter number"))
number2 = int(input("Enter number"))
number3 = int(input("Enter number"))
print("Output of Question5")
f5(number1,number2,number3)

#6. Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.
def f6():
    l1 = []
    i = 1
    while i<= 30:
        l1.append(i*i)
        i += 1
    print(l1)
print("Output of Question6")    
f6()

#7. Write a python program to access a function inside a function.
def f7():
    f3()
    print("My Name is shriya")
def f3():
    print("Hi All")
print("Output of Question7")    
f7()

#8. Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.
def f8(str):
    count1 = 0
    count2 = 0
    for i in str:
        if i.isupper():
            count1 += 1
        elif i.islower():
            count2 +=1
    print("number of uppercase letters in given string = ",count1)
    print("number of lowercase letters in given string = ",count2)
s1 = input("Enter string")
print("Output of Question8")
f8(s1)

#9. Write a python program to create a function to check whether a string is a pangram or not.
def f9(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str:
            return False
            break;
    return True
S1 = input("Enter string")
print("Output of Question9")
s2 = f9(S1)
if s2 == True:
    print("Given string is pangram")
else:
    print("Given string is not pangram")

#10. Write a python program to create a function to check whether a string is an anagram or not
def f10(s1,s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False 
s1 = input("Enter 1st string")
s2 = input("Enter 2nd string")
print("Output of Question10")
s3 = f10(s1,s2)
if s3 == True:
    print("Given string is anagram")
else:
    print("Given string is not anagram")

