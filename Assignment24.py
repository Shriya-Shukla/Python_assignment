#                                                        Classes and Objects
#1. Write a python program to create a user class with 3 properties : name, age, email.
class Info:
    def __init__(self,Name,Age,Email):
        self.Name = Name
        self.Age = Age
        self.Email = Email
    def Show(self):
        print(self.Name,self.Age,self.Email)
    
obj1 = Info("Rk",24,"rk@gmail.com")
obj2 = Info("Sidd",18,"Sidd@gmail.com")
obj1.Show()
obj2.Show()
    
#2. Write a python program to create a user class with a method to greet the user.
class Greeting:
    def __init__(self,Name):
        self.Name = Name
    def Greet(self):
        print("Hi,Welocome to Mysirg Education Platform")
        print("Hi, it's ",self.Name)
g1 = Greeting("Shri")
g2 = Greeting("Rk")
g1.Greet()
g2.Greet()
        
#3. Write a python program to create 2 objects of the user class and assign different values.
class Computer:
    def __init__(self,CPU,RAM):
        self.cpu = CPU
        self.Ram = RAM
    def show(self):
        print("The properties of Computer",self.cpu,self.Ram)
c1 = Computer("i9",16)
c2 = Computer("i11",32)
c1.show()
c2.show()
    
#4. Write a python program to init default values for user object using __init__ method.
class Computer:
    def __init__(self):
        self.Ram = 16
        self.Cpu = "i9"
        self.Brand = "HP"
    def Show(self):
        print("The Properties of compute: Brand= ",self.Brand,"RAM= ",self.Ram,"CPU= ",self.Cpu)
c1 = Computer()
c2 = Computer()
c1.Show()
c2.Show()

#5. Write a python program to delete the age property of the user.
class Info:
    def __init__(self,Name,Age,Email):
        self.Name = Name
        self.Age = Age
        self.Email = Email
    def show(self):
        print(self.Name,self.Age,self.Email)
person1 = Info("Rk",24,"Rk@gmail.com")
person2 = Info("shri",22,"Shri@gmail.com")
person1.show()
person2.show()
del person2.Age

#6. Write a python program to create 3 user objects and find the youngest of all.
class Info:
    def __init__(self,Name,Age,Email):
        self.Name = Name
        self.Age = Age
        self.Email = Email
    def show(self):
        print(self.Name,self.Age,self.Email)
    def younger(person1,person2,person3):
        print((person1.Age if person1.Age < person3.Age else "the youngest person:",person3.Name,person3.Age)if person1.Age < person2.Age else(person2.Age if person2.Age < person3.Age else person3.Age))
person1 = Info("Rk",24,"Rk@gmail.com")
person2 = Info("shri",22,"Shri@gmail.com")
person3 = Info("Sidd",18,"sidd@gmail.com")
person1.show()
person2.show()
person3.show()
person1.younger(person2,person3)


#7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the values).
class Laptop:
    def __init__(self,Brand,Ram,Cpu,Hdd):
        self.Brand = Brand
        self.Ram = Ram
        self.Cpu = Cpu
        self.Hdd = Hdd
    def Show_config(self):
        print("The Attributes of Laptop",self.Brand,self.Ram,self.Cpu,self.Hdd)
l1 = Laptop("HP",16,"i9",4)
l2 = Laptop("DELL",32,"i10",6)
l3 = Laptop("ACER",16,"i7",8)
l1.Show_config()
l2.Show_config()
l3.Show_config()

#8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted order based on the ram size.
class Laptop:
    list = []
    def __init__(self,B,R,C,H):
        self.Brand = B
        self.Ram = R
        self.Cpu = C
        self.Hdd = H
        Laptop.list.append(self.Ram)

    def Show_config(self):
        print("The Attributes of Laptop",self.Brand,self.Ram,self.Cpu,self.Hdd)
l1 = Laptop("HP",64,"i9",4)
l2 = Laptop("DELL",32,"i10",6)
l3 = Laptop("ACER",16,"i7",8)
l1.Show_config()
l2.Show_config()
l3.Show_config()
print(sorted(Laptop.list))

#9. Write a python program to create a School class and 3 instance variables and 1 class variable.
class Student:
    College = "MPEC"
    def __init__(self,Name,Roll_No,Course):
        self.Name = Name
        self.Roll_No = Roll_No
        self.Course = Course
    def Show(self):
        print("Detail of Student:",Student.College,self.Name,self.Roll_No,self.Course)
s1 = Student("Sidd",10203220,"B.Tech")
s2 = Student("Pragati",10434335,"BBA")
s3 = Student("Shri",12335357,"B.Tech")
s1.Show()
s2.Show()
s3.Show()

#10. Define a class Employee with instance object variables empid, name, salary. Write__init__() method in the class to initialize instance object variables. Also define instance methods to input fields and display field value
class employee:
    def __init__(self):
       pass 

    @classmethod
    def input(cls):
        cls.empid = int(input("enter empid"))
        cls.name = input("enter name")
        cls.salary= int(input("enter salary"))

    def show(self):
        print(self.empid)    
        print(self.name)
        print(self.salary)
e1 = employee() 
e2 = employee()
e1.input() 
e1.show()  
e2.input()
e2.show() 
