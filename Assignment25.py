#                                                                      OOPs and Inheritance
#1. Write a python script to create a Profile class with 3 attributes (name, email, age).
class Profile:
    def __init__(self,name,email,age):
        self.Name = name
        self.Email = email
        self.Age = age
        
print("Output of Question 1:")        
p1 = Profile("sidd","sidd12@gmail.com",18)
print(p1.Name,p1.Email,p1.Age)
        
#2. Write a python script to update the above Profile class with encapsulation.
class  Profile:
    def __init__(self,name,email,age):
        self.Name = name
        self.Email = email
        self.Age = age
        
    def set_Name(self,name):
        self.Name = name

    def set_Email(self,email):
        self.Email = email

    def set_Age(self,age):
        self.Age = age

    def get_Details(self):
        return self.Name ,self.Email,self.Age

print("Output of Question 2:")
p1 = Profile("sidd","sidd12@gmail.com",18)
print(p1.Name,p1.Email,p1.Age)
p1.set_Name("shri")
p1.set_Email("shri@gmail.com")
p1.set_Age(20)
print(p1.get_Details())
print(p1.Name,p1.Email,p1.Age)
        
#3. Write a python script to update 2nd Question, change email and age to __email and __age.
class  Profile:
    def __init__(self,name,email,age):
        self.Name = name
        self.__Email = email
        self.__Age = age
        
    def set_Name(self,name):
        self.Name = name

    def set_Email(self,email):
        self.__Email = email

    def set_Age(self,age):
        self.__Age = age

    def get_Details(self):
        return self.Name ,self.__Email,self.__Age

print("Output of Question 3:")
p1 = Profile("sidd","sidd12@gmail.com",18)
p1.set_Name("shri")
p1.set_Email("shri@gmail.com")
p1.set_Age(20)
print(p1.get_Details())
#4. Write a python script to update 2nd Question, add a class variable (platform) and create a classmethod to access it.
class Profile:
    platform = 20
    def __init__(self,name,email,age):
        self.Name = name
        self.__Email = email
        self.__Age = age
        
    def set_Name(self,name):
        self.Name = name

    def set_Email(self,email):
        self.__Email = email

    def set_Age(self,age):
        self.__Age = age

    @classmethod
    def get_platform(cls):
        return cls.platform
        
    def get_Details(self):
        return self.Name ,self.__Email,self.__Age

print("Output of Question 4:")    
p1 = Profile("sidd","sidd12@gmail.com",18)
p1.set_Name("shri")
p1.set_Email("shri@gmail.com")
p1.set_Age(20)
print(p1.get_Details())
print(p1.get_platform())
#5. Write a python script to create a Calculator class with 2 methods for adding and subtracting 2 values.
class Calculator:
    def __init__(self):
        self.a = 0
        self.b = 0

    def Addition(self,a,b):
        return a+b

    def Subtraction(self,a,b):
        return a-b

print("Output of Question 5:")
c1 = Calculator()
print(c1.Addition(20,30))
print(c1.Subtraction(50,30))

#6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication and division of 2 values and inherit it from the Calculator class.
class Calculator2(Calculator):
    def __init__(self):
        self.a = 0
        self.b = 0

    def Multiplication(self,a,b):
        return a * b

    def Division(self,a,b):
        return a//b
print("Output of Question 6:")
c2 = Calculator2()
print(c2.Addition(100,60))
print(c2.Subtraction(100,60))
print(c2.Multiplication(100,60))
print(c2.Division(100,60))        
        
#7. Write a python script to create a Phone class with 2 methods to print the features (calling and sms).
class Phone:
    def Call(self):
        return "calling"
        
    def SMS(self):
        return "SMS"

print("Output of Question 7:")        
ph1 = Phone()
print(ph1.Call())
print(ph1.SMS())

#8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and Phone Class.
class SmartPhone(Calculator2,Phone):
    def __init__(self):
        print("Smartphone")

print("Output of Question 8:")
s1 = SmartPhone()
print(s1.Addition(100,60))
print(s1.Subtraction(100,60))
print(s1.Multiplication(100,60))
print(s1.Division(100,60))
print(s1.Call())
print(s1.SMS())
    
#9. Write a python script to create an application like Truecaller where names and numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a number and 2nd to add a new entry).
class Truecaller:
    d1 = {'9199876544':"shri",'8943343432':"sidd",'9212345567':"Pragati",'9123492931':"mamata",'8342242412':"Rk"}
    
    def __init__(self):
        self.Name = ' '
        self.Number = ''

    @classmethod
    def FetchName(cls,Number):
        print(cls.d1[Number])
    @classmethod
    def AddDetail(cls,Number,Name):
        cls.d1[Number] = Name

print("Output of Question 9:")
T1 = Truecaller()
T1.FetchName("8943343432")
print(T1.d1)
T1.AddDetail('734242344','Sunil')
print(T1.d1)
        
#10. Write a python script to add the new method in SmartPhone class which accepts Truecaller object as a parameter and call the fetch method of Truecaller
class SmartPhone(Calculator2,Phone,Truecaller):
    def __init__(self):
        print("Smartphone")
    def smart(self)
print("Output of Question 10:")
s1 = SmartPhone()
print(s1.Addition(100,60))
print(s1.Subtraction(100,60))
print(s1.Multiplication(100,60))
print(s1.Division(100,60))
print(s1.Call())
print(s1.SMS())
