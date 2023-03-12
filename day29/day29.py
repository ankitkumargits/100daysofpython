print("Hello Day 29 in doc strings in python ")

def sqr(n):
    '''it takes a number of arguments and returns a numbers __doc__ string
    '''
    print(n**2)

sqr(5)
print(sqr.__doc__)