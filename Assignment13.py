#                                                                          List

#Question 1: Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using list
L1 = ["Java","Python","SQL","C"]
print("Output of Question1: ")
print(L1)

#Question 2: Write a python script to get the data type of a list.
L1 = ["java",1,"shri","MySirG"]
print("Output of Question2: ")
print(type(L1))

#Question 3: Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])
mylist = ["Java","C","Python"]
print("Output of Question3: ")
print(mylist[-1])

#Question 4: Write a python script to Change the values "SQL" and "Reactnative" with the values "NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
thislist = ["Java","SQL","C","Reactnative","Javascript","Pyhton"]
thislist[thislist.index("SQL")] = "NoSQL"
thislist[thislist.index("Reactnative")] = "Flutter"
print("Output of Question4: ")
print(thislist)

#Question 5: Write a python script to add an item to the end of the list (item “Python”. (mylist = ["Java", "SQL", "C", "Reactnative"]
thislist = ["Java","SQL","C","Reactnative"]
thislist.append("Python")
print("Output of Question5: ")
print(thislist)

#Question 6: Write a python program to append elements from another list to the current list.(firstlist = ["Java", "Python", "SQL"] secondlist = ["C", "Cpp", "NoSQL"] )
firstlist = ["java","Python","SQL"]
secondlist = ["C","Cpp","NoSQL"]
for i in firstlist:
    secondlist.append(i)
print("Output of Question6: ")    
print(secondlist)    

#Question 7:  Write a python program to Print all items by referring to their index number (thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
thislist = ["Java","SQL","C","Reactnative","Javascript","Pyhton"]
for i in thislist:
    print(i,end = ' ')
print("Output of Question7: ")    
print()    

#Question 8: Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]
thislist = ["Java","SQL","C","Reactjs","Javascript","Pyhton"]
thislist.sort()
print("Output of Question8: ")
print(thislist)

#Question 9: Write a Python script to create a list of city names taken from the user.
mylist = []
n = int(input("enter the no. of elemnets in list"))
i = 1
while (i<=n):
    mylist.append(input())
    i += 1
print("Output of Question9: ")    
print(mylist)                  

#Qestion 10: Write a Python script to create a list, where each element of the list is a digit of a given number
n = int(input("enter number: "))
list1 = []
while n!= 0:
    list1.append(n%10)
    n = n//10
print("Output of Question10: ")    
for x in list1:
    print(x,end = ' ')
