# list comprehension = A concise way to create lists in py
#                       Compact & easier to read than traditional loops
#                       [expression for value in iterable if condition]
'''
doubles = []

for i in range(1, 11):
    doubles.append(i*2)

print(doubles)
'''
# but can be more compac with list comprehension
#doubles=[expression for value in iterable]
'''
doubles = [i * 2 for i in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 15)]
print(doubles)
print(triples)
print(squares)
'''
# next example:
'''
fruits= ["apple", "orange", "banana", "coconut"]
fruit_chars = [fruit[0] for fruit in fruits]

print(fruit_chars)
'''
# 3rd ex
'''
numbers = [1 , -2, 3, -4, 5, -6, 8, -7]

pos_nums = [num for num in numbers if num >= 0]
neg_nums = [num for num in numbers if num <= 0]
even_nums = [num for num in numbers if num % 2==0]
odd_nums = [num for num in numbers if num % 2==1]
print(pos_nums)
print(neg_nums)
print(even_nums)
print(odd_nums)
'''
# last ex:
grades = [85, 42, 79, 90, 56, 61, 30]

passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)