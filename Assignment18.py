#                                                                    Dictionary

#1. Write a python program to create and print a dictionary which stores your information.
d1 = {"Name": "shriya","Age": 22,"Gender": "Female" }
print("Output of Question1")
print(d1)

#2. Write a python program to access the items of a dictionary by referring to its key name.
d1 = {"Name": "shriya","Age": 22,"Gender": "Female" }
print("Output of Question2")
for k in d1:
    print(d1[k])

#3. Write a python program to get a list of the values from a dictionary.
d1 = {102: "Sidd",103: "Shri",104:"Pragati",105: "Krishna"}
print("Output of Question3")
print(d1.values())

#4. Write a python program to change the value of a specific item by referring to its key name.
d1 = {102: "Sidd",103: "Shri",104:"Pragati",105: "Krishna"}
d1[102] = "Abhishek"
print("Output of Question4")
print(d1)

#5. Write a python program to print all key names in the dictionary, one by one.
d1 = {102: "Sidd",103: "Shri",104:"Pragati",105: "Krishna"}
print("Output of Question5")
for k in d1:
    print(k)
    
#6. Write a python program to create a dictionary that contains three dictionaries.(nested)
myfamily = {"child1":{"Name":"shri","Age":22},"child2":{"Name":"Sidd","Age":18},"child3":{"Name":"Pragati","Age":20}}
print("Output of Question6")
print(myfamily)
print()

#7. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.
child1 = {"Name":"shri","Age":22}
child2 = {"Name":"Sidd","Age":18}
child3 = {"Name":"Pragati","Age":20}
Myfamily = {"Child1":child1,"Child2":child2,"Child3":child3}
print("Output of Question7")
print(Myfamily)
print()

#8. Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.
l1 = [102,103,104,105]
l2 = ["Shri","Rk","Sidd","Pragati"]
d1 = {}
d2 = {}
d1 = {l1[i] :l2[i] for i in range(len(l1))}
print("Output of Question8")
print(d1)

#9. Write a python program to merge two python dictionaries into one dictionary.
d1 = {'C': 92,'Java': 66,'Python': 85}
d2 = {'Cpp': 98,'DS': 68,'Python': 90}
d1.update(d2)
print("Output of Question9")
print(d1)

#10. Write a python program to get the key of lowest value from the dictionary. sample_dict = {'C': 92,'Java': 66,'Python': 85}
sample_dict = {'C': 92,'Java': 66,'Python': 85}
print("Output of Question10")
print(min(sample_dict))
