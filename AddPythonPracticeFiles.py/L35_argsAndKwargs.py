# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments
#            # unpacking operator
#            1. positional 2. default 3. keyword 4.ARBITRARY 
'''
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3))
'''
# another example covers a display name:
'''
def display_name(*args):
    for arg in args:
        print(arg, end = " ")

display_name("Dr.","Spongebob", "Harold", "Squarepants", "III")
'''
'''
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
# allows for a varying amount of keyword args
print_address(street ="123 Fake St." ,
              apt = "100",
              city = "Lexington" , 
              state= "KY", 
              zip = "54320")
'''
# example with *args and **kwargs covering shipping lables:
# must have *args, then **kwargs
def shipping_label(*args, **kwargs):
   for arg in args:
       print(arg, end = " ")
   print()   
   #for value in kwargs.values():
   #    print(value, end= " ")   
   if "apt" in kwargs:  
       print(f"{kwargs.get('street')}, {kwargs.get('apt')}")
   elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
   else:
       print(f"{kwargs.get('street')}")    
   print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('zip')}")
shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street = "123 Fake St.",
               pobox = "POBOX #1001",
               city = "Lexington",
               state = "KY",
               zip = "53421")