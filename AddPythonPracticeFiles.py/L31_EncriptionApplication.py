# an encription application:
import random
import string

chars = string.punctuation + string.digits + " " + string.ascii_letters
chars = list(chars)
key = chars.copy()

# for testing
#print(chars)

# next shuffle it:
random.shuffle(key)

# meaning each time an O is usef for example then it is replaced 
# hide the chars and key
#print(f"chars: {chars}")# a list of the chars
#print(f"key: {key}") # a copied list of the chars

# encription time:
plain_txt = input("Enter a message to encript: ")
cipher_txt = ""

for letter in plain_txt: # strings are iterable
    index = chars.index(letter)
    cipher_txt += key[index]

print(f"orginal message : {plain_txt}")
print(f"encripted message : {cipher_txt}")

# dencription is the 2nd bit:
cipher_txt = input("Enter a message to encript: ")
plain_txt = ""

for letter in cipher_txt: # strings are iterable
    index = key.index(letter)
    plain_txt += chars[index]

print(f"orginal message : {cipher_txt}")
print(f"encripted message : {plain_txt}")