#logical operators = used on conditional statements

# and = checks two ormore conditions if true
# or = checks if at least one condition is true
# not = True if condition is false, and vice versa
# check temp
temp = 20
sunny = True

if temp <= 0  or temp >=30:
    print(f"\nThe Temperature is bad!")

else:
    print(f"\nThe Temperature is good!")

if not sunny:
    print("It is cloudy out.")
else:
    print("Its sunny out.")