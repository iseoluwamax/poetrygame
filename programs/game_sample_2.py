# a sample for the frame work of how poetry game is going to work.

introduction = """Complete the poem
use the answer to the riddle to fill in the gaps in the poem."""
print(introduction)

print("Have a fun time with poetry game!")

print("Remo")

poem = """Remo! The land of my ancestors
Remo! Where culture and ----- reign supreme
Remo! The kingdom of peace and prosperity"""
print(poem + "\n")

riddle = """I am passed down, yet I am not a thing.
I shape how you dance, how you feast, how you sing.
Old as the past, yet alive every day,
In families, cultures, and games that we play.
What am I?"""
print("Riddle: \n" + riddle)

active = True 

while active: 
    answer = input("Your answer is a 9 letter word, put in your guess here: ")
    if answer == "tradition":
        print("correct")
        active = False
    else:
        print("Try again!")
        continue
