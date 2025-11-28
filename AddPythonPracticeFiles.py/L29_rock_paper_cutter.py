# rock, paper, cutter game:
import random

options = ("rock", "paper", "knife")

playing = True

while playing:
    player = None
    computer = random.choice(options)#  make sure only : rock, paper, knife:
    while player not in options:

        player = input("Enter a choice (rock, paper, knife): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("it is a tie!") # tie condition
    elif player == "rock" and computer == "knife":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "knife" and computer == "paper":
        print("You win")
    else:
        print("You lost!")
    if not input("play again? (y/n): ").lower() == "y":
    
        playing = False
        
print("Thank for playing!")