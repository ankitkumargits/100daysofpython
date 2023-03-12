print("Recursion in python is very most dangerous topic")


def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)
        
print(factorial(3))