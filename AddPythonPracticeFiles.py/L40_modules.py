# module = a file containing code you want to include in your program
#           use 'import' to include a module (built in or your own)
#           useful to break up a large program reusable serparate files
# it can be useful to build your own modules too

# print(help("modules"))
#import math
# or another way is with:

#import math as m

# or import something more specific
#from math import pi
# but from math import e can have naming conflicts
#from math import e

#print(math.pi)

#print(m.pi)
#print(pi)
'''
a, b, c, d, e= 1, 2, 3, 4, 5
print( e ** a)
print(e ** b)
print(e ** c)
print(e ** d)
print( e ** e)
'''
# this can cause mistakes if missed
# otherwise:
'''
import math

a, b, c, d, e = 1, 2, 3, 4, 5

print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)
print(math.e ** e)
'''
import exampleModule
# place the module in files above the main under .venv for one
#result = exampleModule.pi
result = exampleModule.square(3)
result = exampleModule.cube(3)
result = exampleModule.circumference(3)
result = exampleModule.area(3)
print(result)