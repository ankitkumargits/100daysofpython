print("Hello High order function")


def cube(x):
    return x*x*x

cub = lambda x: x*x*x

print(cub(2))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# newL = []
# for item in l:
#     newL.append(cube(item))

# map function in python
# newL = list(map(cube, l))
newL = list(map(lambda x: x*x*x, l))
print(newL)

# filter function in python

def filter_function(a):
    return a>4

neL = list(filter(filter_function, l))
print(neL)

# reduce function in python

from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum = reduce(lambda x, y: x+y, numbers)

print(sum)
