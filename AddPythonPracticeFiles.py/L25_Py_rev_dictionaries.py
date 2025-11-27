# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates
# meaning like an id and a name for {key:value}
capitals = {"USA" : "Washington D.C.",
            "India" : "New Delhi",
             "China" : "Beijing",
             "Russia" : "Moscow"}
# displays all the attributes and methods of it, then look them up with the help()
#print(dir(capitals))
#print(capitals.get("USA")) # this method prints the value

#if capitals.get("Japan"):
#    print("That capital exists.")
#else:
#    print("That capital does not exist!")
#capitals.update({"Germany":"Berlin"}) # to update or add key and value pairs
# or the remove it with pop:
#capitals.pop("China")
#capitals.popitem()
# or on can clear it:
#capitals.clear()
# or just get the keys:

#keys = capitals.keys()

#print(capitals)

#for key in capitals.keys():

#    print(key)

# or use the values method:
#values = capitals.values()

#for value in capitals.values():
#    print(value)

# the items method:
items = capitals.items()
#print(items) # prints a 2d - list of tuples

for key, value in capitals.items():
    print(f"{key} : {value}") # to print every key and value pair