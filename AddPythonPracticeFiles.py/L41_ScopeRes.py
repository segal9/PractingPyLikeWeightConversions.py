# var scope = where a var us visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> built-in
# follow the order of operations
'''
def func1():
    x = 1
    #print(a)

    def func2():
        x = 2
        print(x)
    func2()

#x = 3

func1()
#func2()
'''
# then for a global example:
'''
def func1():
    print(x)
def func2():
    print(x)
x = 3
func1()
func2()
'''
# another example
from math import e

def func1():

    print(e)

e = 3

func1()