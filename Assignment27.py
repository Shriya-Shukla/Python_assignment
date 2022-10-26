#                                                  Exception Handling

#Question1: Write a python script to create a ArithmeticError
class ArithError:
    a = 5
    b = 0
    c = a/b
    print(c)

#Question2: Write a python script to create a ValueError   
class ValError:
    a = int(input("enter a number: "))
# during input if we r giving other than 'int' it will throw valueError    
    print(a)

#Question3:Write a python script to handle the ArithmeticError
class ArithError:
    a = 5
    b = 0
    try:
        c = a/b
        print(c)
    except ArithmeticError:
        print("we can't divide any number by zero")

# Question 4:Write a python script to handle a ValueError
class valueError:
    try:
        b = int(input("enter any number: "))
    except ValueError:
        print("Please enter integer value only")

# Question 5: Write a python script to handle multiple Exception in one try
def Single_Try():
    try:
        a = int(input("enter a number: "))
        b = int(input("enter a number: "))
        c = a/b  
        print(d)
    except ValueError:
        print("Please enter a interger value")
    except ZeroDivisionError:
        print("we can't divide number by zero")
    except NameError:
        print("Any variable is not defined")
    except Exception:
        print("something went wrong") 
    finally:
        print("the output after dividing number",c)    

Single_Try()

# Question6. Write a python script to create a calculator with 4 basic operations, and handle a maximum number of exceptions.
def calculator():
    choice = 0
    try:
        a = int(input("enter a number: "))
        b = int(input("enter a number: "))
    except ValueError as ERROR:
        print("Invalid Number input")
        print("Error")
        # print("\n Try again")
        # return    
    try:
        choice = input("enter your choice: + - * / : ")
    except ValueError:
        print("enter an operation: + - * /: ")

    if choice == "+":
        print("the sum of given number : ",a+b)
    
    elif choice == '-':
        print("The subtraction of given: ",a-b)

    elif choice == '*':
        print("The multiplication of given number: ",a*b)

    elif choice == '/':
        try:
            print("the output after dividing: ",a/b)  
        except ZeroDivisionError:
            print("We can't divide number by zero")
    else:
        print("Invalid oeration")

calculator()                  

# Question 7. Write a python script to add a finally block for the above script
def calculator_finally():
    choice = 0 
    c = 0
    try:
        a = int(input("enter a number"))
        b = int(input("enter a number"))
    except ValueError as ERROR:
        print("Invalid Number input")
        print("Error")   
    try:
        choice = input("enter your choice: + - * / :")
    except ValueError:
        print("enter an operation: + - * /")

    if choice == "+":
        print("the sum of given number : ",a+b)
    
    elif choice == '-':
        print("The subtraction of given: ",a-b)

    elif choice == '*':
        print("The multiplication of given number: ",a*b)

    elif choice == '/':
        try:
            c = a/b
            print("the output after dividing: ",c)  
        except ZeroDivisionError:
            print("We can't divide number by zero")
        finally:
            print("the value of a , b, c are :",a,b,c)
    else:
        print("Invalid oeration")

calculator_finally()

# Question 8. Write a python script to implement try except and else block for division
def Try_Else():
    c = 0
    try:
        a = int(input("enter a number"))
        b = int(input("Enter a number"))
        c = a/b
    except ValueError:
        print("please enter a integer value")
    except ZeroDivisionError:
        print("we can't divide any number by zero")
    else:
        print("we didn't got any exception",c) 
Try_Else()     

# Question 9. Write a python script to raise a ValueError.
import math
def Num_square(a):
    if a < 0:
        raise ValueError("Numbers should be greater than zero")
    else:
        print("the sqrt of given number ",math.sqrt(a))    

n = int(input("enter a number"))    
Num_square(n)    

# Question 10. Write a python script to implemented a nested Try Except block
def Nested_Except():
    try:
        a = int(input("enter a number"))
        b = int(input("enter a number"))
    except ValueError:
        print("Please enter a interger value")  
    
    try:      
        c = a/b  
    except ZeroDivisionError:
        print("we can't divide number by zero")

    try:
        if a < b:
            d = a
        print(d)
    except NameError:
        print("Any variable is not defined")

    except Exception:
        print("something went wrong") 

    finally:
        print("the output after dividing number",c)    

Nested_Except()

