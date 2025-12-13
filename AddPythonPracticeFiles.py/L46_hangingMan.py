# a simple hanging man game:
# reqs a set of words
# and wordList had to be moved to the file with the other file for this to work.
from wordList import words
import random

# and make it a set of words for the proj
#words = ("pokemon", "church", "run", "walk", "demon", "computer", "alien")
# and we have 6 guess
# next asci art for the hangMan with a dict
hangManArt = {0:("   ",
                 "   ",
                 "   "),
              1:(" o ",
                "    ",
                "    "),
              2:("   o  ",
                "   |  ",
                "     "),
              3: ("  o ",
                " /| ",
                "     "),
              4: ("   o ",
                " / | \\",
                "     "),
              5: ("   o ",
                " / | \\",
                "  /   "),
              6:("   o ",
                " / | \\",
                "  / \\  "),}
# test with print
#print(hangManArt[0])
#for line in hangManArt[6]:
#    print(line)
# functions needed:
def display_man(wrong_guesses):
  #  pass
    print("***************************")
    for line in hangManArt[wrong_guesses]:
        print(line)   
    print("***************************")
def display_hint(hint):
    #pass
    print(" ".join(hint))

def display_ans(answer):
    #pass
    print(" ".join(answer))

def main():
    #pass
    # to choose a word at random
    answer = random.choice(words)
    #print(answer)
    hint = ["_"] * len(answer)
    print(hint)
    wrong_guesses = 0
    guessed_letters = set() # to have an empty set
    is_running = True

    while is_running:
        
        display_man(wrong_guesses)
        
        display_hint(hint)
        #display_ans(answer)

        guess = input("Enter a letter for your guess, or else get hung: ").lower()

        if len(guess) != 1 or  not guess.isalpha():
            print("Invalid input!")
            continue

        if guess in guessed_letters:
            print(f"'{guess}' was already used!")
            continue

        guessed_letters.add(guess)
    
        if guess in answer:
           for i in range(len(answer)):
               if answer[i] == guess:
                   hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_ans(answer)
            print("\nYou Won.")
            is_running = False
        elif wrong_guesses >= len(hangManArt) - 1:
            display_man(wrong_guesses)
            display_ans(answer)
            print("\nYou lost.")
            is_running = False

if __name__ == "__main__":
    main()