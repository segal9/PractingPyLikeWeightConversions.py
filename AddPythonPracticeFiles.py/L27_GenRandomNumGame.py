import random
# this roll a 6 sided die:
low = 1
high = 100
#options =("rock", "paper", "scissors")
# or deck of cards:
#cards = ["2", "3", "4", "5", "6", "8", "9", "10", "J", "Q", "K", "A"]

#number = random.randint(low,high)
# and to get a random floating pt num
#number = random.random()
#option = random.choice(options) # to randomly choose which it is from rock, paper, scissors
#then shuffle thru cards
#random.shuffle(cards)# to shuffle cards

#print(number)
#print(option)

#print(cards)

# after the examples, I will start the number guessing:

guesses = 0

number = random.randint(low, high)

while True:
    guess =int( input(f"Guess a number between ({low} - {high}): "))
    guesses += 1
    if guess < number:
        print(f"{guess} is too low!")
    elif guess > number:
        print(f"{guess} is too high!")
    else:
        print(f"{guess} is right!")
        break

print(f"This round took you this number of attempts: {guesses}")