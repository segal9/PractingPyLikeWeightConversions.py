# collection = single "variable" used to store multiple values.
# list = [] ordered and changable. Duplicates OK
# set = {} unordered and immutable, but add/remove - OK. No duplicate
# Tuple = () ordered and unchangable. Duplicates OK. FASTER
# careful with naming

# lastly tuples:
# good for ordered and unchangable items
fruits = ("apple", "orange", "banana", "coconut", "coconut") # tuples are faster than list 
print(fruits)
#print(dir(fruits))
#print(len(fruits))
#print("pineapple" in fruits)
print(fruits.index("apple"))
print(fruits.count("coconut"))

for fruit in fruits:
    print(fruit)

#fruits = {"apple", "orange", "coconut", "banana", "coconut"} # good for work with constants
#print(fruits) # it is unordered
#print(dir(fruits)) # and can use the help function on it
# plus length
#print(len(fruits)) # and can use the in operator

#print("pineapple" in fruits)
# and can't use indexing in a set
#fruits.add("pineapple")
#fruits.remove("apple")
#fruits.pop() # but it is random
#fruits.clear()
#print(fruits)


#fruits = ["apple", "orange", "coconut", "banana"]

# display attributes 
#print(dir(fruits))
# and can see how to use them with the help function
#print(help(fruits))

#print(len(fruits))
#print("pineapple" in fruits)

#fruits[0] = "pineapple"
#fruits.append("pineapple")
#fruits.remove("apple")
#fruits.insert(0, "pineapple")

# sorts in alphebetical order:
#fruits.sort()

# reversed based on order they were put in:
#fruits.reverse()

# but to put them first in alphebetical order use sort(), then reverse()
#fruits.sort()
#fruits.reverse()
#fruits.clear()
# but if not in list there is an error then
#print(fruits.index("apple"))
#print(fruits.count("banana"))

#print(fruits)

#for fruit in fruits:
#    print(fruit)

#print(fruits[0 : :-1])
#for fruit in fruits:
#    print(fruit)