# dice roller game:
import random

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518") # these asci produce the art to make the
# dice

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"
# dict for dice art:
# the key value pairs: with a tuple made of strings
dice_art = {
    1 : ("┌─────────┐",
         "│         │",
         "│    ●    │",
         "│         │",
         "└─────────┘",),
     2 :("┌─────────┐",
         "│  ●      │",
         "│         │",
         "│      ●  │",
         "└─────────┘",), 
     3 :("┌─────────┐",
         "│  ●      │",
         "│    ●    │",
         "│      ●  │",
         "└─────────┘",),
     4 :("┌─────────┐",
         "│  ●   ●  │",
         "│         │",
         "│  ●   ●  │",
         "└─────────┘",),
     5:("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",), 
     6 :("┌─────────┐",
         "│  ●   ●  │",
         "│  ●   ●  │",
         "│  ●   ●  │",
         "└─────────┘",)          
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: ")) # to avoid fractions 
# to add dice
for die in range(num_of_dice): # must use range to grab the num of dice selected
    dice.append(random.randint(1,6))
# a way to test it with print(dice)
print(dice)

# next display the asci art:
# this displays each line of the dice art:
#for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#        print(line)
# or print the dice art horizontally:
# and die is a num: 1-6 & test it each time
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end = "")
    print()

# to gather the total:
for die in dice:
    total += die
print(f"Total: {total}")