# function = a block of resusable code 
# a place () after the function name is invoked
# and the order of parameters matters too.
'''
example 1
def happy_birthday(name, age): 
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

happy_birthday("Rob", 35)
'''
# example 2:
'''
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of {amount:.2f} is due: {due_date}")
# rob's bill of 450.27 is due febuary 1st
display_invoice("Rob", 450.27, "02/01")
'''
# example 3 adding two nums together and then subtract them in a diff func:
# then other functions to multiply and another to divide the two numbers
'''
def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x + y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(2, 2))
print(subtract(2,2))
print(multiply(2,2))
print(divide(2,2))
'''
# example 4 creates a name:
def make_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = make_name("spongebob", "squarepants")

print(full_name)