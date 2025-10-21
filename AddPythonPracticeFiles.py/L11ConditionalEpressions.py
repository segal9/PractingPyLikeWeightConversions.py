#conditional expressions = A one-line shortcut for the if-else statement(ternary operato)
# print or assign one of two values based on a condition
# x if condition else y
num = 5
a = 6
b = 7
age = 17
temperature = 19

UserRole = "guest"
#print("Positive" if num > 0 else "Negative")
#result = "Even" if num % 2 == 0 else "Odd"
#MaxNum = a if a > b else b
#MinNum = a if a < b else b
#status = "Adult" if age >= 18 else "Child"
#weather = "Hot" if temperature > 20 else "Cold"
AccessLevel = "Full Access" if UserRole == "admin" else "Limited Access"
print(AccessLevel)