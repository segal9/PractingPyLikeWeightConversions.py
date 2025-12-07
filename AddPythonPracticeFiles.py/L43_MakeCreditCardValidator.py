# py credit card validator program
# use test credit card numbers .com
# '1234-5678-9012-3456'
# 1. remove any '-' or ' '
# 2. add all digits in the odd places from right to left
# 3. double every second digit from right to left
#        (if result is a two-digit number,
#           aff the two-digit number together to get a single digit.)
# 4. sum the totals of the steps 2, & 3
# if the sum is divisible by 10, the credit card num is valid
'''
Test Credit Card Account Numbers
American Express 378282246310005
American Express 371449635398431
American Express Corporate 378734493671000
Australian Bankcard 5610591081018250
Diners Club 30569309025904
Diners Club 38520000023237
Discover 6011111111111117
Discover 6011000990139424
JCB 3530111333300000
JCB 3566002020360505
MasterCard 5555555555554444
MasterCard 5105105105105100
Visa 4111111111111111
Visa 4012888888881881
'''
sum_odd_digits = 0
sum_even_digits = 0
total = 0
# step 1 
cardNum = input("Enter a credit card number please: ")
cardNum = cardNum.replace("-","") #and cardNum.replace(" ", "")
cardNum = cardNum.replace(" ", "")
cardNum = cardNum[::-1]
# testing : print(cardNum)
#print(cardNum)
# step 2
for x in cardNum[::2]:
    sum_odd_digits += int(x)

#step 3
for x in cardNum[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

# step 4
total = sum_odd_digits + sum_even_digits
# step 5
if total % 10 == 0:
    print("Valid!")
else:
    print("Invalid!")