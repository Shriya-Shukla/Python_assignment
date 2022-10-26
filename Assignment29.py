#                                           File Handling

#Question1. Write a Python script to print the following status of a file:
#a. Whether a file is read only
#b. Whether a file is closed or not
#c. Which file opening mode is used
#d. Name of the file"""

f1 = open('test.text','w')
f1.write("Be a good listner")
f1.close()
if f1.mode == 'r':
    print("yes file is a read only mode")
else:
    print("file is not in read only mode")      
if f1.closed == True:
    print("file closed")
else:
    print("file open")
print("File opening mode is:",f1.mode)
print("Name of the file: ",f1.name)
    
# Question2. Write a Python script to create a new file ‘myfile.txt’ and store user entered text.
f2 = open('myfile.text','w')
user_input = input("Enter text: ") 
f2.write(user_input)
f2.close()

# Question3. Write a Python script to read the above created file ‘myfile.txt’ and display content on the console.
try:
    f2 = open('myfile.text','r')
    print(f2.read())
except FileNotFoundError:
    print("File Doesn't exist") 
finally:       
    f2.close()
    
# Question4. Write a Python script to store a list of city names in a file ‘cities.txt’
def Write_city(filename,list):
    with open(filename,'w') as f4:
        for e in list:
            f4.write(e) 
            f4.write("\n")
    f4.close()        
    f4 = open(filename,'r')      
    print(f4.readlines())
    f4.close()

list = ['kanpur','Lucknow','Delhi','Prayagraj','Noida','Banda','Mumbai','Bangalore','Bhopal']
Write_city('cities.text',list)   

# Question5. Write a Python script to append list of city names in a file ‘cities.txt’
def Append_city(filename,list):
    with open('cities.text','a') as f5:
        for e in list:
            f5.write(e)
            f5.write("\n")
    f5.close()        
    f5 = open('cities.text','r')    
    print(f5.readlines()) 
    f5.close() 

list = ['Unnao ','Agra ','Mathura ','Gaziabad ','kalyanpur ','Ravatpur ']
Append_city('cities.text',list)   

# Question6. Write a Python script to search whether a particular city is there in the file ‘cities.txt’ or not
def Search_city(filename,word):
      f6 = open(filename,'r')
      content = f6.read()        
      if word in content:
        print('City present in file')
      else:
        print('city not present in file') 
Search_city('cities.text','Bhopal')           

# Question7. Write a Python script to count the number of Python keywords occurring in a python source file.
from keyword import kwlist
def Search_keyword(filename):
    f7 = open(filename,'r')
    count = 0
    for line in f7.readlines():
        word = line.split(' ')
        for w in word:
            if w in kwlist:
                count = count +1
    print(count)
    f7.close()
    
Search_keyword('DEMO.py')

# Question8. Write a Python script to create a copy of a file.
import os
import shutil
def Copyfile():
    D = r"F:\python_practice\Assignments"
    print(os.listdir(D))
    src = r"F:\python_practice\Assignments\myfile.text"
    dest = r"F:\python_practice\Assignments\myfilecpy.text"
    path = shutil.copyfile(src,dest)
    print("after copying file: ")
    print(os.listdir(D))
    print("Path of the duplicate file is: ", path)

Copyfile()

# Question9. Write a Python script to store book data in a file. Book data is in the form of a dictionary in which book name is the key and price is its value. Use pickle to storedata into a file (say bookfile)
import pickle
def Pickling_lib_dump():
    lib = {'C':500,'Python':1000,'DS':750,'History':650,'English':550,'Math':350}
    f9 = open('library.text','wb')
    pickle.dump(lib,f9)
    f9.close()

Pickling_lib_dump()

# Question10. Write a Python script to extract book data from a bookfile using pickle. Also print extracted book data
def Pickling_lib_load(filename):
    f9 = open(filename,'rb')
    s = pickle.load(f9)
    for key in s:
        print(key,' ',s[key])
    f9.close()

Pickling_lib_load('library.text')    