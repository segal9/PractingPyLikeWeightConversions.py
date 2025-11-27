# a dictionary used in a concession stand:
menu = {"pizza" : 3.00,
        "nachos" : 4.50,
        "popcorn" : 6.00,
        "fries" : 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

# use a list for the cart:
cart = []
total = 0
print("-------------Menu-----------------")
for key, value in menu.items(): # prints every key and value
    print(f"{key:10}:${value:.2f}") # .2f is for the decimals and : 10 is the format specs
print("----------------------------------")

while True:
    food = input("Select an item ( q to Quiz ): ").lower() # .lower accounts for upper case
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food) # adds food
print("--------------Your order!----------------")
for food in cart:
    total += menu.get(food)
    print(food, end = " ")

print(f"\nTotal is: ${total:.2f}")
#print(cart) to see the cart requested

