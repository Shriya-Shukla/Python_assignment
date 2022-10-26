#                                                                      Set
#1. Write a python program to store all the programming languages known to you using Set.
s1 ={"C","Java","Python","Cobol"}
print("Output of Question1")
print(s1)

#2. Write a python program to store your own information {name, age, gender, so on..}
s2 = {"Shriya","Shukla",22,"Female"}
print("Output of Question2")
print(s2)

#3. Write a python script to get the data type of a Set.
s3 = {"Python", "Django", "JavaScript", "SQL"}
print("Output of Question3")
print(type(s3))

#4. Write a Python script to find if “Python” is present in the set thisset = {"Java","Python", "Django"}
thisset = {"Java","Python", "Django"}
print("Output of Question4")
print("yes Python is present in given set" if "Python" in thisset else "Not Present")

#5. Write a python program to add items from another set to the current set. thisset = {"Java", "Python", "SQL"} secondset= {"C", "Cpp", "NoSQL"}
print("Output of Question5")

#6. Write a python program to add elements of list to a set. thisset = {"Python", "Django", "JavaScript"} mylist = ["Java", "C"]
print("Output of Question6")

#7. Write a python program to remove last item of the given set. thisset = {"Python", "Django", "JavaScript", “SQL”}
s1 = {"Python", "Django", "JavaScript", "SQL"}
s1.remove("SQL")
print("Output of Question7")
print(s1)

#8. Write a python program to delete the set completely.
s1 = {"Python", "Django", "JavaScript", "SQL"}
s1.clear()
print("Output of Question8")
print(s1)

#9. Write a python program to loop through the set and print values thisset = {"Python", "Django", "JavaScript", “SQL”}
s1 = {"Python", "Django", "JavaScript", "SQL"}
print("Output of Question9")
for i in s1:
    print(i, end=' ')
print()    
#10. Write a python program to find the maximum and minimum value in a set.
s1 = {"Python", "Django", "JavaScript", "SQL"}
print("Output of Question10")
print(max(s1))
print(min(s1))
