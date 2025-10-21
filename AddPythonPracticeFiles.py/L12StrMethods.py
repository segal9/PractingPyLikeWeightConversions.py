#-----------------------------------------------
# Str methodd
#-----------------------------------------------
# name = 
#name = input("Enter your full name: ")
#PhoneNum = input("Enter your phone number: ")
#result = len(name)
#result = name.find("l")
#result = name.rfind("q")
#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#result = name.isdigit()
#result = name.isalpha()
#result = PhoneNum.count("-")
# most useful:
#PhoneNum = PhoneNum.replace("-", "")
# for manual use print(help(str)) and the str refers to that method

#print(PhoneNum)
# ex 1 - validate the user input:
# 2. username must be 12 chars long
# 3. username must contain spaces
# 4. user must not have digits in the name:
UserName = input("Enter your username: ")

if len(UserName) < 12:
    print("The username must be at least 12 chars long. Try Again!")
elif not UserName.find(" ") == -1:
    print("No spaces in your username please. Try again!")
elif not UserName.isalpha():
    print("No digits in your username. Try again!")
else:
    print(f"Hi {UserName}!")