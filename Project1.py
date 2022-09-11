#                                                                    Word Puzzle Game
"""
Problem Statement: You have to write a Word Puzzle Game in which the user has to form the correct word out of a given set of characters. In the game the user has to solve this puzzle for 5 words, one at a time. Problem words are stored in a list and appear to the user
in random sequence. Give the user score +1 for each correct answer and give -1 for each wrong answer. At last print the final score. You can store any number of words in the list, butin each round of the game only 5 words are shown to the user."""

import random
def WordPuzzle():
    list1 = ["Father","Sequence","Aeroplane","Break","GREEN","Mysirg","EDUCATION","PROBLEMS","PRINCIPLE","Education","ORANGE","UNITED","France","Oxford","Enthusiasm","Laptop","COMPUTER","PENCIL","PYTHON","MAINFRAME","DATABASE"]
    Ques = 5
    count = 0
    while Ques > 0:
# randrange will return any random index no. of list         
        s1 = list1[random.randrange(0,len(list1))]
        
# random.sample will return list of characters in random orders & join will return a string with radomly organized characters of string        
        print("Your Question on screen:  ",''.join(random.sample(s1,len(s1))))  
        Output = input("Enter your Answer:  ")
        if Output.casefold() == s1.casefold():
            count += 1
            print("You Guessed it right")
        else:
            print("You guessed it wrong")
        Ques -= 1
    print()
    return count


count = WordPuzzle()
print("Your final score is",count)
