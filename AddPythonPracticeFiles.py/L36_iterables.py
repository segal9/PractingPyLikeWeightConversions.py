# iterables = an object/ collections that can return its elements one at a time,
# allowing it to be iterated over in a loop
'''
nubers = (1, 2, 3, 4, 5)

for number in numbers:
    print(number, end = " - ")
'''
'''
# next rview sets:
fruits = {"apple", "orange", "banana", "coconut"}
# but cannot reverse sets
for fruit in fruits:
    print(fruit)
'''
# cover strings
'''
name = "Bob James"

for character in name:
    print(character, end = " ")
    '''
# lastly reviewing dict:
my_dictionary = {"A" : 1, "B": 2,"C": 3}
# can only iterate over the keys
#for key in my_dictionary:
#    print(key)
# otherwise to get a the values:
#for value in my_dictionary.values():
#    print(value)
# or can get both keys and values:
for key, value in my_dictionary.items():
    print(f"{key} = {value}")