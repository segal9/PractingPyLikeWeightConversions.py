# list for 2d lists
'''
fruits =     ["apples", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

for collection in groceries:
    for food in collection:
        print(food, end = " ")
print(groceries[1][2]) # this can display coordinates like on a grid
''' # to display a grid quickly
# then making a 2-d tuple:
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0,"#"))

for row in num_pad:
    for num in row:
        print(num, end = " ")
    print()