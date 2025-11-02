#format specifiers = {value:flags} format a vale based on what flags are inserted
#                   flags are inserted
# .(number)f =rond to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = alocate and zero pad that many spaces
# :< = left justify 
# :> = right justify 
# :^ = center align
# :+ = use a plus sign to indicate positive value
# :+ = place a sign to leftmost position 
# :  = insert a space before positive numbers
# :, = comma serparator
price1 = 3000.14159
price2 = -98700.65
price3 = 12000.34

print(f"Price 1 is: ${price1:+,.3f}")
print(f"Price 2 is: ${price2:+,.2f}")
print(f"Price 3 is: ${price3:+,.2f}")
 