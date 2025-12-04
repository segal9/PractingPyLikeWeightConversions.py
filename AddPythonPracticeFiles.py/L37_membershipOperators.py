# membership operators = used to test wether a value or variable is found in a squence
#                         (string, list, tuple, set, or dictionary)
#                       1. in
#                       2. not in
'''
word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter not in word:
    print(f"{letter} was not found!")
    
else:
    print(f"There is a {letter}")
'''
# another example:
# focus on sets and tuples
''' 
students = {"Spongebob", "Patrick", "Sandy"} # sets

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")
'''
# next example with dict
'''
grades = {"Sandy": "A", 
          "Squidward": "B", 
          "Spongebob": "C", 
          "Patrick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")
'''
# another example covers emails
email = "AGuy@gmail.com"
# checks 2 conditions
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email!")