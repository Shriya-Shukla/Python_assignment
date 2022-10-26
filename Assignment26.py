# Question1:Write a python script to multiple 2 or 3 or 4 numbers with a single multiply method in a class using method overloading
class multiplication:
    def multiply(self,n1,n2=1,n3=1):
        print(n1*n2*n3)

m1 = multiplication()
m1.multiply(20,30)
m2 = multiplication()
m2.multiply(30,50,40)

# Question2: Write a python script to create a user account class with 2 instance variables (userid and balance). Create 3 user objects and add all the users using operator overloading.
class Account:
    def __init__(self,user_id,balance):
        self.user_id = user_id
        self.balance = balance

    def __add__(self,other1):
        total_user_id = self.user_id + other1.user_id 
        total_balance = self.balance + other1.balance  
        return  Account(total_user_id,total_balance)

a1 = Account(101,500000)
a2 = Account(102,600000)
a3 = Account(103,80000000)
a4 = a1+a2+a3
print(a4.user_id,a4.balance)

# Question3: Write a python script to create a to print the above user account object using operator overloading (hint __str__ method).
class Account:
    def __init__(self,user_id,balance):
        self.user_id = user_id
        self.balance = balance

    def __add__(self,other1):
        total_user_id = self.user_id + other1.user_id 
        total_balance = self.balance + other1.balance 
        return  Account(total_user_id,total_balance)
        
    def __str__(self):
        return str(self.balance)

a1 = Account(101,500000)
a2 = Account(102,600000)
a3 = Account(103,80000000)
print(a1+a2+a3)           

#Question 4: Write a python script to create two Threads. First thread will print all Even numbers and Second thread will print all Odd numbers till 100.
from time import sleep
from threading import *
class Even(Thread):
    def run(self):
        i = 1
        print("Even Numbers:")
        while(i<=100):
            if i % 2 == 0:
                print(i,end =' ')
            i += 1
        print()

class Odd(Thread):
    def run(self):
        print("Odd Numbers:")
        j = 1
        while j <= 100:
            if j%2 != 0:
                print(j, end = ' ')
            j += 1
    print()

e1 = Even()
e1.start()
sleep(1)
o1 = Odd()
o1.start()
e1.join()
o1.join()      

#Question 5: Write a python script to create 2 threads to add all the values from 1 to 100.
import threading
from threading import Thread
import time
def add1(beg,end):
    print("sum of elements from 1 to 50: ")
    i = 1
    s = 0
    for i in range(beg,end+1,1):
        s = s+i 
        i += 1
        print(s,end = ' ')
    time.sleep(1) 
    print()

def add2(beg,end):
    print("sum of elements from 51 to 100: ")
    i = 1
    s = 0
    for i in range(beg,end+1,1):
        s = s+i 
        i += 1
        print(s,end = ' ')
    time.sleep(1)

a1 = threading.Thread(target = add1, args = (1,50))
a2 = threading.Thread(target = add2, args = (51,100))
a1.start()
a1.join()
a2.start()
a2.join()

#Question6. Write a python script to create 5 threads to fill a list with random numbers till 100.
import threading
from threading import Thread
import random
import time
l1 = []
def RandomList1():
    for i in range(1,21,1):
        l1.append(random.randint(1,20))
    print(l1)
    time.sleep(2)

def RandomList2():
    for i in range(1,21,1):
        l1.append(random.randrange(21,40))
    print(l1)
    time.sleep(2)

def RandomList3():
    for i in range(1,21,1):
        l1.append(random.randint(41,60))
    print(l1)
    time.sleep(2)

def RandomList4():
    for i in range(1,21,1):
        l1.append(random.randrange(61,80))
    print(l1)
    time.sleep(2)

def RandomList5():
    for i in range(1,21,1):
        l1.append(random.randint(81,100))
    print(l1) 
    time.sleep(2)

r1 = threading.Thread(target = RandomList1)
r2 = threading.Thread(target = RandomList2)
r3 = threading.Thread(target = RandomList3)
r4 = threading.Thread(target = RandomList4)
r5 = threading.Thread(target = RandomList5)
r1.start()
r1.join()
r2.start()
r2.join()
r3.start()
r3.join()
r4.start()
r4.join()
r5.start()
r5.join()

#Question7. Write a python script to create a clock where 1st thread will print the current time every second and 2nd will print “1 Minute Completed” after every 1 minute.
import time
import threading
from threading import Thread
from datetime import datetime
def clock1():
    for i in range(1,61,1):
        now = datetime.now()
        time.sleep(1)
        print(now.strftime("%H:%M:%S"))

def clock2():
    print("1 Minute completed")

c1 = threading.Thread(target=clock1)
c2 = threading.Thread(target=clock2) 
c1.start()
c1.join()
c2.start()
c2.join() 

#Question8. Write a python script to change the name of the Thread.
import threading
from threading import Thread
def clock1():
    print("1 Minute completed")

c1 = threading.Thread(target=clock1)
print("Before changing Thread name: ",c1.name)
c1.name = 'MyThread'
print("After changing Thread name: ",c1.name)

#Question9. Write a python script to join 2 threads after printing completing the first Question.
import threading
from threading import Thread
def t1(a):
    for i in range(a):
        print("First Thread")

def t2(b):
    for i in range(b):
        print("Second Thread")

c1 = threading.Thread(target=t1,args = (7,))
c2 = threading.Thread(target=t2, args = (5,)) 
c1.start()
c1.join()
c2.start()
c2.join() 

#Question 10: Write a python script to check whether a given number is prime or armstrong number using 2 different threads
import threading
from threading import Thread
def Armstrong(n):
    a = n
    s = 0
    while(n!=0):
        b = n%10
        s = s + (b**3)
        n = n//10 
    if a == s:
        print("Number is armstrong")
    else:
        print("Number is not armstrong")

def Prime(n):
    for i in range(2,n,1):
        if n%i == 0:
            print("Number is not prime")
            break
    else:
        print("Number is prime")

num = int(input("enter an number"))
t1 = threading.Thread(target=Armstrong,args = (num,))
t2 = threading.Thread(target=Prime,args = (num,))
t1.start()
t2.start()

