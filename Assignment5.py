#                                                         Operators

#Question 1:Write a python script to remove the last digit from a given number. (for example, if user enters 2534 then your output should be 253)
a = int(input("enter number"))
print("Output of Question 1")
print("number after removing last digit:",a//10)

#Question 2:Write a python script to get the last digit from a given number. (for example, if user enters 2089 then your output should be 9)
b = int(input("Enter number"))
print("Output of Question 2")
print("last digit of given number:",b%10)

#Question 3: Write a python script to swap data of two variables
r = int(input("Enter 1st number"))
s = int(input("Enter 2nd number"))
(r,s) = (s,r)
print("Output of Question 3")
print("the value of r is %d and s is %d " %(r,s))
temp = r;
r = s
s = temp

#Question 4: Write a python script to find x power y, where values of x and y are given by user
x = int(input("enter the value of number"))
y = int(input("enter the power of given number"))
print("Output of Question 4")
print("the x power y :", x**y)

#Question 5: Write a python script which takes a three digit number from the user and displays only its first digit.
q = int(input("Enter number"))
print("Output of Question 5")
print("the 1st digit of given number:",int(q/100))

#Qestion 6: Write a python script which takes a three digit number from the user and displays only its middle digit.
p = int(input("Enter number"))
print("Output of Question 6")
p = int(p/10)
print("the middle digit of given number:",p%10)

#Question 7:Write a python script which takes a three digit number from the user and displays only its last digit.
m = int(input("Enter number"))
print("Output of Question 7")
print("the last digit of given no.",m%10)

#Question 8: Write a python script to use IN operator to display the data present in the list
list1 = [0,2,3,4,10]
num = int(input("enter a number"))
#check whether number exist or not
for e in range(len(list1)):
    if num in list1:
        print("number in list1")
        break
else:
    print("number not in list1")
          

#Question 9:Write a python script to use NOT IN operator to display the data not present in list

list1 = [0,2,3,4,10]
num = int(input("enter a number"))
for e in range(len(list1)):
    if num not in list1:
        print("number not in list1")
        break
else:
    print("number in list1")
#Question 10: Write a python script to use IS operator to display if both variables are the same object or not?
a = int(input("enter 1st no."))
b = int(input("enter 2nd no."))
print("Output of Question 10:")
if (a is b):
    print("both object are same")
else:
    print("both object are different")
print()



    

        
        
