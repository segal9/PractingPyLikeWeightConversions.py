# keywrd args = an argument preceded by an identifier
#               helps w/ readiabity
#               order of args does not matter
#               !. positional 2. default 3. KEYWORD 4. arbitrary
'''
def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")
# but put positional arguments come before keyword args
hello("Hello", title="Mr.", first="Spongebob", last="Squarepants")
'''
# example 2 with a for loop
'''
for x in range(1, 11):
    print(x, end = " ")
'''
# another example:
#print("1", "2","3","4","5", sep = "-")
# next a func with phone #
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country =1, area=123 , first =456 , last=7890)

print(phone_num)