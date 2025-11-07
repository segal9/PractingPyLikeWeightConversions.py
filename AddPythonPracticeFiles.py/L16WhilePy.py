# while loop = execute some code WHILE some condition remains true
''' Ex 1
name = input("Enter your name:  ")

while name == "":
    print("you did not enter your name.")
    # if the next line is not below, then you remain stuck in forever loop
    name = input("Enter your name:  ")

# once exited the while loop
print(f"Hello {name}!")
''' 
#Ex 2:
'''
age = int(input("Enter your age: "))
while age < 0:
    print("The age can't be negative")
    age = int(input("Enter your age: "))
print(f"You are {age} years old!")
'''
# ex 3:
'''
food = input("Tell me a food you like (q to quit): ")

while food != 'q':
    print(f"You like {food}")
    food = input("Tell me another food you like (q to quit): ")

print("\nSo long sucker!")
'''
#ex 4
num = int(input("Enter a # between 1 and 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid.")
    num = int(input("Enter a # between 1-10: "))

print(f"You picked the number {num}!")