# py number guess game:
import random 

lowestNum = 1
highestNum = 100

answer = random.randint(lowestNum, highestNum)
#print(answer) testing round
guesses = 0
is_running = True # a flag
print("Py-Number guessing game.")
print(f"Select a number between {lowestNum} and {highestNum}")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        #pass
        # once a digit:
        guess = int(guess)
        guesses += 1

        if guess < lowestNum or guess > highestNum:
            print("That number is out of range")
            print(f"Select a number between {lowestNum} and {highestNum}!")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"Right! The answer was: {answer}")
            print(f"The number of guess was: {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Select a number between {lowestNum} and {highestNum}!")