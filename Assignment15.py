#                                                                     Strings
# Question1: Write a python script to create a String in 3 different possible ways
s1 = "Mysirg"
s2 = str(5.6)
s3 = str()
s3 = s3+s2
print("Output of Question1")
print(s1,s2,s3,end = ' ')
print()

# Question2: Write a python script to Get the characters from the start to position 5 (Given String “iNeuron” using the slice syntax)
s1 = "iNeuron"
print("Output of Question2")
print(s1[0:5:1])
print()

# Question3: Write a python script to Get the characters from position 2 to position 5 (Given String “Hello Learners” using the slice syntax)
s2 = "Hello Learners"
print("Output of Question3")
print(s2[1:5:1])
print()

# Question4: Write a python script to demonstrate String Concatenation adding space in between (Given Strings a=”Learning” b=”Python” )
a ="Learning"
b = "Python"
l1 = [a,b]
print("Output of Question4")
print(' '.join(l1))

# Question5: Write a python script to get the count of total number of characters in String a= “iNeuron”
a = "iNeuron"
count = 0
for i in a:
    count += 1
print("Output of Question5")    
print("Number of chrarcters in given string:",count)

# Question6: Write a python script to reverse a String. (“iNeuron”)
a = "iNeuron"
print("Output of Question6")
print(a[-1:-len(a)-1:-1])

# Question7: Write a python script to determine whether a string contains a specific substring.
a = input("enter a string")
print("Output of Question8")
if a.find(input("Enter substring"))!= -1:
    print("substring is present in given string")
else:
    print("substring is not present")

# Question8: Write a python script to check if a string contains only numbers.
print("yes string contain only numbers" if input("enter a string").isdigit() else "string not containing all numbers")

# Question9: Write a python script to check if a string contains only characters of the alphabet.

print("yes string contain only alphabets" if input("enter a string").isalpha() else "string not containing all alphabets")

# Question10: Write a python script to convert an integer to a string.
a = int(input("enter a string"))
b = str(a)
print("Output of Question10")
print(type(b))
print(str(a))
     
