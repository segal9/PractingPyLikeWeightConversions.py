# indexing = accessing elements of a sequence using [] (indexing operation)
#   [start : end : step]
# example:
creditCardNum = "1234-5679-9012-3456"

#print(creditCardNum[0 : 5])
#print(creditCardNum[ 6 : 10])
#print(creditCardNum[11:15])
#print(creditCardNum[5:])
#print(creditCardNum[-2])
#print(creditCardNum[::3])
#LastDigitsOfCard = creditCardNum [-4:]
creditCardNum = creditCardNum [::-1]
#print(f"XXXX-XXXX-XXXX-{LastDigitsOfCard}")

# in reversed order
print(creditCardNum)