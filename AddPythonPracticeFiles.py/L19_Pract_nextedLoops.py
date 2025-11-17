# nested Loops = a loop within another loop (outer, inner)
#               Outer loop:
#                   Inner loop:

rows = int(input("Enter a number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol , end = "")
    print()
# example:
#for x in range(1, 10):
#    print(x, end="") # end is to keep numbers on the same line