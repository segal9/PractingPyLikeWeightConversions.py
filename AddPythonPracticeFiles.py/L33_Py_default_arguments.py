# default arguements = A default value for certain parameters
                    #  defualt is used when that argument is omitted 
                    #  make your functions more flexibke, reduces # of arguments
                    # 1. positional, 2. DEFAULT, 3. keyword, 4. aribitrary
'''
def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

#print( net_price (500))
#print(net_price(500, .1))
print(net_price(500, .1, 0))
'''
# an ex. with an cnter:
import time
# but defualt args come after the regular args
def count(end, start = 0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Boom!")

count(30, 15)