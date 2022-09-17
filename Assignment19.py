#1. Write a python program to create a simple function which prints “MySirG” .
def f1():
    print("MySirG")
print("Output of Question1")    
f1()    

#2. Write a python program to create a function which expects two arguments and print them in the function body.
def f2(a,b):
    print("a is =" ,a,"b is =",b)
print("Output of Question2")     
f2(10,20)

#3. Write a python program to create a function which expects an unknown number of arguments.
def f3(*t):
    print("the sum is",sum(t))
print("Output of Question3")     
f3(2,3)
f3(50,3,2)
f3(32,12,45,56)
f3(56,34,12,34,4)
f3(9,5,3,2,1,3,4,5,3,4)

#4. Write a python program to create a function which expects kwargs arguments.
def f4(a,b,c):
    print("the value of a , b & c are",a,b,c)
print("Output of Question4")     
f4(30,c = 10,b=50)

#5. Write a python program to create a function which expects a list as an argument.
def f5(list):
    print(list)
l = [2,"shriya",4,"Rk",5,"sidd",7,"Pragati"]
print("Output of Question5") 
f5(l)

#6. Write a python program to create a function that finds a maximum of four numbers.
def f6(a,b,c,d):
    print(max(a,b,c,d))
print("Output of Question6")     
f6(10,100,1000,45)

#7. Write a python program to sum all the numbers in a list.
def f7(l1):
    print("the sum ",sum(l1))
list = [2,40,234,123,456,200,500]
print("Output of Question7") 
f7(list)

#8. Write a python program to multiply all the numbers in a list.
def f8(l1):
    c = 1
    for i in l1:
        c = c * i
    print("the multiplication of every element",c)
list1 = [2,40,234,123,456,200,500]
print("Output of Question8") 
f8(list)

#9. Write a python program to create a function to check whether a number falls in a given range.
def f9(r,number):
    for i in r:
        if (i == number):
            print("number Present in given range",i)
            break;
    else:
        print("Number not present in given range")
print("Output of Question9")         
f9(range(10),8)

#10. Write a python program to create a function to check whether a given number is even or odd.
def f10(n):
    if n % 2 == 0:
        print("Given no. is even")
    else:
        print("Given no. is odd")
n = int(input("enter a number"))
print("Output of Question10") 
f10(n)        
